# Knowledge network notes

Self-contained rules for the long-term learning artefact. `SKILL.md` is the only index;
this file does not reference another reference file.

## Why this exists

A short deadline makes it easy to discard everything once the task or exam ends. The network
is the counterweight: small, browsable notes that show how ideas relate, so depth accumulates
across sessions instead of resetting.

The tool is not the point. Depth comes from explaining, transferring, and reviewing. A vault
app only makes the relations easier to see.

## Core format

One short note per knowledge point. Keep it short enough to reread in a minute. Use a stable
set of fields:

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

Keep an `INDEX.md` that lists the current goal, the depth tier, and links to the notes.
Relations are links between notes, not a directory tree: prerequisite, easily confused with,
and transfers-to are the ones worth recording.

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

The default output must be **plain Markdown that any editor can read**. `[[wikilinks]]` are
just text in a plain viewer and still convey the relation. This is the required baseline.

Enhanced formats are optional and only applied when the user has the corresponding tool:

- Note properties / tags / callouts for an Obsidian vault.
- A `.canvas` relation map: nodes are notes, edges carry a label such as "prerequisite",
  "easily confused with", or "transfers to". Validate that every edge points to an existing
  node and that the JSON parses before claiming the map is done.
- A tabular index of points, mastery state, and last review result.

If the enhanced tool is missing, degrade to the plain Markdown baseline without losing any
content. Never make the network depend on a specific app.

## Incremental maintenance

- Append or update a note when a point is learned, corrected, or reviewed — not in one big
  batch at the end.
- Do not wait for the user to declare the task finished. Reaching a stage goal or an explicit
  request is enough.
- When a review fails, update `last-review` and the result field, and lower `status`.
- Notes are **user data**. They live in the user's own project or vault directory, never
  inside the skill directory. The skill stays stateless.

## Common failure modes

- Copying whole explanations into notes. A note is a retrieval cue, not a transcript.
- Recording hierarchy only. "Chapter 3 > section 2" does not help someone who confused two
  ideas.
- Writing notes once and never revisiting them. The review field is what keeps the network
  alive.
- Making the notes depend on a plugin, so they become unreadable after a change of tools.

## Source discipline

When a note states a volatile fact (API signature, version behaviour, tool output), attach
the source or record that it was unverified. Do not invent links or quote documents that
were not read.
