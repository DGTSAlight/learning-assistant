# Knowledge network notes

Self-contained rules for the long-term learning artefact. `SKILL.md` is the only index;
this file does not reference another reference file.

## Why this exists

A short deadline makes it easy to discard everything once the task or exam ends. The network
is the counterweight: small, browsable notes that show how ideas relate, so depth accumulates
across sessions instead of resetting.

The tool is not the point. Depth comes from explaining, transferring, and reviewing. A vault
app only makes the relations easier to see.

## Two artefacts, two readers

The network is not one file. Two artefacts do different jobs, and mixing them is the usual
reason a note ends up useful to nobody.

| Artefact | Path | Reader | Job |
| --- | --- | --- | --- |
| Note | `notes/N01-<point>.md` | the assistant, next session | restore state after a context reset or a model switch |
| Review page | `review/R01-<point>.html` | the user, days later | make re-learning cheap: recap, wrong-question redo, relation map, links |

- A note is **terse on purpose** — conclusion, the error actually made, relations, last
  result. It is a state record, not a study text. Do not pad it so that it "reads better";
  its reader is a model resuming work, and short fields are exactly what it needs.
- A review page is **for the eye** — a one-screen recap, one figure, questions the user can
  redo without the assistant, and links to the neighbours. It never carries the state fields;
  the note owns those.
- Same point, same number: `N01` and `R01` are one knowledge point for two readers. Never
  number them independently.
- The page is optional per point; the note is not. A point without a page still has its
  state; a point without a note loses it.

## Layout and naming

```
<notes root>/
  INDEX.md                     the map: goal, depth, status table, one link per page
  PE-<subject>/                one folder per subject
    notes/N01-<point>.md
    review/R01-<point>.html
    explain/E01-<subject>.html
    figures/
```

- `<notes root>` is chosen by the user; `learning-notes/` inside the task directory is the
  fallback. Never write notes inside the skill directory.
- One folder per subject, named `<CODE>-<subject>`. The code is 2–4 uppercase ASCII letters:
  `PE` power electronics, `MATH` mathematics, `SEN` sensors, `CODE` programming, `GEN` for
  anything unclassified. Register a new code in `INDEX.md` when the folder is created, and
  never reuse a code for a different subject.
- **The folder states the type; the name states the subject.** That is why suffixes such as
  `-讲解页` or `-笔记` disappear: `explain/E01-buck-电路图与工作原理.html` already says it is
  an explainer page, and the folder keeps it out of the note list.
- Prefixes: `N` note, `R` review page, `E` explainer page. Two digits, assigned in creation
  order within the folder, **never renumbered and never reused** — links and the user's memory
  survive a deletion. Widen to three digits only if a folder passes 99.
- Keep the point name in the user's own language after the prefix. The ASCII prefix keeps
  sorting and linking stable; the native name keeps it recognisable. No dates in file names —
  the date lives inside the file.
- `figures/` belongs to the subject folder and is named after the page that uses it, e.g.
  `figures/R01-i-d-comparison.svg`. A script that generates those figures lives beside them —
  regeneration stays next to its output.
- `INDEX.md` stays at the notes root, so a page in `review/` reaches it as `../../INDEX.md`,
  its note as `../notes/N01-…`, an explainer as `../explain/E01-…`, and a figure as
  `../figures/…`. Every link inside a page is relative; an absolute path breaks the moment the
  folder is moved or copied.

Sorting matters more than it looks. With prefixes a folder view reads `N01 N02 R01 R02 E01`,
grouped by type and stable at thirty files. Without them, a folder of bare titles has no
stable order and no way to tell a note from an explainer page.

### Migrating a flat folder

When the user already has a flat folder, propose the mapping and **move nothing until they
agree** — their files, their call.

| Old | New |
| --- | --- |
| `<point>.md` | `PE-<subject>/notes/N01-<point>.md` |
| `<subject>-讲解页.html` | `PE-<subject>/explain/E01-<subject>.html` |
| `figures/` | `PE-<subject>/figures/` |
| `INDEX.md` | stays at the root; its status table gains a page column |

Migrate in one pass, keep the numbers monotonic (oldest point gets `N01`), and say what was
renamed. Do not renumber later to "tidy up".

## Note format

One short note per knowledge point. Short enough to reread in a minute. A stable field set:

```markdown
---
title: <point name>
tags: [<topic>]
status: mastered | shaky | not-learned | skipped
last-review: <date>
---

# <point name>

**Conclusion** — one or two sentences.

**Why / usual mistake** — the mechanism and the error the user actually made.

**Relations**
- prerequisite: [[<note>]]
- easily confused with: [[<note>]]
- transfers to: [[<note>]]

**Review question** — one question that tests the mechanism, not the label.

**Last review result** — passed / failed, and what broke.
```

Keep an `INDEX.md` at the notes root with the current goal, the depth tier, and a status
table whose first column links to the review page. Relations are links between notes, not a
directory tree: prerequisite, easily confused with, and transfers-to are the ones worth
recording.

## The review page

A page exists so the user can re-learn a point **without starting a session**. It is opened
from the folder, works offline, and remembers what was already mastered.

### What a page must contain

| Section | Required | Content |
| --- | --- | --- |
| Header | yes | point name, code (`R01`), status chip, last review date, next review date |
| Recap | yes | 3–5 lines on the mechanism, plus the one figure that carries the shape |
| Quiz | yes | 4–8 single-choice questions, local verdict, one "why" line per question |
| Map | yes, when the point has two or more neighbours | relation graph; every node links to the sibling page |
| Links | yes | sibling pages, explainer pages, and the `N` note file |
| Next action | yes | what to do per score band, written before the user asks |

Keep that order. A page with a quiz and no recap is a test, not a review page.

### Interaction rules

- **Every judgement is local.** Clicking an option shows right or wrong inside the page and
  sends nothing. The page never calls the network.
- A wrong answer reveals the "why" immediately; a correct one leaves it collapsed so the
  reason can still be checked.
- Two consecutive correct answers retire a question from the wrong-question pool; one wrong
  answer resets its streak. "Only the wrong ones" filters to the live pool.
- Every question is single choice. Multi-select makes re-checking slow and the verdict fuzzy;
  one choice plus a "why" line tests the mechanism, which is the point.
- The explanation must name **the error the user actually made**, not the textbook fact. A
  "why" that reads like a definition means the note was copied instead of the mistake.
- Progress persists in `localStorage` under `review:<CODE>-<NN>`, wrapped in `try/catch`.
  When storage is unavailable, say so in the page and keep working — never block on it.
- A button that needs the assistant assembles a **complete** prompt and copies it. Label it
  `复制…`, not `发送…`: a local page cannot send, and a label that lies is worse than no
  button. Fall back to showing the prompt in a `<textarea>` when the clipboard is blocked.
- Buttons, not radios, for the options: real `<button>` elements with `aria-pressed` are
  reachable with Tab and Enter. Do not claim a radio-group pattern without implementing arrow
  navigation. Bind with `addEventListener`, never inline handlers.

### Technical constraints

- **One file, no CDN, no build step, no framework.** No KaTeX, MathJax, web fonts, or icon
  URLs: the page is opened from `file://` on a machine that may be offline. Write formulas as
  `U<sub>d</sub>`, `<i>α</i>`, `π + α`.
- Flat visual language, same as the cards: solid fills, 1px borders, 8–12px radius, no
  gradients, shadows, glow, or emoji.
- Light and dark through `prefers-color-scheme` and CSS variables. Check both.
- Add a `@media print` block — a printed page is a legitimate offline review.
- Reading survives with JavaScript disabled: the recap, the map, and the questions are static
  markup; the script only adds judgement and memory.

### Building one

1. Copy the worked example listed in the skill index. Keep its styles and script; replace the
   content. Set `data-key`, `data-code`, and `data-title` on `<main>` — the script reads the
   page's identity from there, so no JavaScript needs editing.
2. Fill the header from the note's front matter: same title, same status, same dates.
3. Write the recap from the note's conclusion and why fields — same mechanism, more prose, no
   new claims.
4. Write 4–8 questions. At least one must be a question the user has **already answered
   wrong**; keep the wrong option as a distractor and put the real error in its "why".
5. Draw the map from the note's relations. Mark a neighbour without a page as `待建` and
   leave it unlinked rather than linking to a file that does not exist.
6. Set the next review date from the status: `failed` +1 day, `shaky` +3 days,
   `mastered` +14 days, `not-learned` no date.
7. Save as `review/R<NN>-<point>.html`, then add its row to `INDEX.md`.

### Check before claiming it works

- Click a wrong option: the verdict, the "why", and the wrong-pool counter must update with
  no network access.
- Grep the file for `http` — every hit must be a comment or a link the user is meant to
  follow, never a `<script src>`, `<link href>`, or `url(...)`.
- Check every relative `href` against the real folder. A page linking to a sibling that does
  not exist is worse than one with no map.
- Reload: mastered questions stay mastered, and nothing throws when storage is blocked.
- Look at it in both themes. Unreadable dark mode counts as broken.

## Where a page is written, and when

A page is created **in its final location, at the moment it is made**. Not in a temporary
directory that will be tidied up later, and not "after the round finishes".

| Artefact | Final path |
| --- | --- |
| Explainer page | `<notes root>/<CODE>-<subject>/explain/E01-<subject>.html` |
| Review page | `<notes root>/<CODE>-<subject>/review/R01-<point>.html` |
| Figure | `<notes root>/<CODE>-<subject>/figures/…` |

Never stage a page in `.tmp/`, `tmp/`, a cache directory, or the current working directory and
plan to move it later. A file in a temp directory is a file the user will not find: the path
scrolls out of the conversation, the directory may be cleaned without warning, and nothing links
to it. The intent to file it properly later does not survive the end of the session.

If the notes root does not exist yet, create the folder (or ask once where notes should live)
**before** writing the page — not afterwards. Say the path out loud when you hand the page over,
so the user knows where it went.

## Offering and setting up Obsidian

Obsidian is **off by default**. Ask about it at exactly two moments:

1. When a learning task starts, alongside setting the goal.
2. When a stage ends and notes are about to be written.

Ask once, in one short question. A "no" stands until the user changes their mind; do not
ask every turn. If the user wants it but has no Obsidian installed, walk them through it
instead of assuming:

- **Download** — https://obsidian.md/download has installers for Windows, macOS, and Linux.
- **Install and launch**, then create or open a **vault** (just a normal folder on disk).
- **Point the notes at it** — ask for the vault path, or agree on a notes folder inside it.
  Prefer a path relative to the user's project; never hard-code a machine-specific path.
- **Optional companion skills** — https://github.com/obsidianmd/obsidian-skills ships
  `obsidian-markdown` (wikilinks, properties, callouts), `json-canvas` (relation maps),
  and `obsidian-cli` / `obsidian-headless` (read and write a vault without a GUI). None is
  required for the plain-Markdown baseline.
- **Check before claiming** — ask the user or verify that an installation/vault exists.
  Never assume it is installed, and never say it was configured unless it actually was.

If installation is not possible or not wanted, stay on plain Markdown: no content is lost.

**Notes location.** Notes go into a directory the user chooses. If none is given, ask once;
a relative `learning-notes/` folder in the current task directory is a usable fallback.
Notes never go inside the skill directory.

## Reading format first

The **note** must stay plain Markdown that any editor can read. `[[wikilinks]]` are just text
in a plain viewer and still convey the relation. This is the required baseline.

The **review page** is HTML, because its job is interaction and it cannot do that in
Markdown. It stays a single self-contained file with no dependency, so it is still "plain"
in the sense that matters: it opens anywhere, forever.

Enhanced formats are optional and only applied when the user has the corresponding tool:

- Note properties / tags / callouts for an Obsidian vault.
- A `.canvas` relation map: nodes are notes, edges carry a label such as "prerequisite",
  "easily confused with", or "transfers to". Validate that every edge points to an existing
  node and that the JSON parses before claiming the map is done.
- A tabular index of points, mastery state, and last review result.

If the enhanced tool is missing, degrade to the plain baseline without losing any content.
Never make the network depend on a specific app.

## Incremental maintenance

- Append or update a note when a point is learned, corrected, or reviewed — not in one big
  batch at the end.
- Do not wait for the user to declare the task finished. Reaching a stage goal or an explicit
  request is enough.
- When a review fails, update `last-review` and the result field, and lower `status`.
- **A failed check is not only a status change: it becomes a question on the page.** That is
  the loop closing. Add the question, keep the user's wrong option as a distractor, and put
  the real error in the "why".
- Do not build a page per point on day one. Build one when a stage ends, when a point is
  `shaky` or `failed`, or when the user asks.
- Edit a page in place instead of regenerating it: question ids (`data-q`) key the stored
  progress, so keep existing ids stable when adding questions.
- Notes and pages are **user data**. They live in the user's own project or vault directory,
  never inside the skill directory. The skill stays stateless.

## Common failure modes

- Copying whole explanations into notes. A note is a retrieval cue, not a transcript.
- Recording hierarchy only. "Chapter 3 > section 2" does not help someone who confused two
  ideas.
- Writing notes once and never revisiting them. The review field is what keeps the network
  alive.
- Making the notes depend on a plugin, so they become unreadable after a change of tools.
- A review page that is the note re-typed in HTML. If it reads like the note, it will not be
  reread.
- Twenty questions to feel thorough. Four to eight mechanism questions beat twenty
  definitions, and a long bank is a bank nobody finishes.
- A page that needs a server, a CDN, or a build step, and is blank the first time the user is
  offline.
- Renumbering files after a deletion, which breaks every link and every note the user
  remembers by number.

## Source discipline

When a note states a volatile fact (API signature, version behaviour, tool output), attach
the source or record that it was unverified. Do not invent links or quote documents that
were not read.
