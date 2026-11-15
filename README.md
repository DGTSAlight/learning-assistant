# learning-assistant

An Agent Skill for learning one specific thing, fast. It agrees a goal you can actually check,
finds where your existing knowledge is thin, teaches only what that goal needs, then tests you by
making you do something — and leaves behind a state note plus an interactive review page you can
reopen days later.

English | [简体中文](README.zh-CN.md)

## What it does

- **Agrees one checkable goal first.** Not "learn power electronics" but "given a single-phase
  bridge with an inductive load at α = 30°, say which devices conduct in each interval, sketch
  u_d and i_d, and compute U_d without notes". Everything after that is measured against it.
- **Diagnoses before teaching.** A short set of discriminating questions, delivered as one card,
  to find the part that is shallow or wrong — instead of re-teaching what you already know.
- **Fills only the gaps that goal needs.** If the broken link is a prerequisite, it goes back and
  repairs that first, then returns to your goal. It does not walk a syllabus.
- **Tests by making you do.** Predict, sketch, explain, decide. Feedback names the layer where
  the reasoning broke, not just whether the answer was right.
- **Leaves two artefacts.** A short state note so a later session — or a different model — can
  resume, and an interactive review page for you.

## What makes it different

Most "AI tutor" prompts produce a wall of explanation. This one is built around the opposite
assumption: reading an explanation is not evidence of understanding, and a deadline makes breadth
worthless.

- **One goal, not a course.** Breadth is the first thing cut when time is short.
- **Depth is chosen, not fixed.** You pick a tier (usable / solid / deep) and it changes how much
  is covered, never whether you get checked.
- **Wrong answers are the input.** The note records the error you actually made, and that error
  becomes a distractor on your review page later.
- **It says when it does not know.** Volatile facts get a source or an explicit "unverified".

## When to use it

| Your situation | Something you can say |
| --- | --- |
| Exam in a few days, too much material | "Cram for the final in three days — I only need to pass" |
| You studied it, it never clicked | "I never really got this; I get it wrong on every exam" |
| Reading code you did not write | "Walk me through this code line by line" |
| You do not know where to start | "I want to learn X but I don't know where to begin" |
| You want to know what you forgot | "Quiz me on X and see how much I have lost" |
| A concept keeps biting you | "Explain X the way you would teach it, not a one-off answer" |

These are examples, not commands. There is no special syntax to learn, and the skill answers in
whatever language you write in.

## When it will not help

- A one-off fact question — "what is X", "explain X in one sentence".
- Pure task execution — fix this bug, run the tests, generate this file, look up an API.
- You only want the answer, with no interest in the reasoning.

In those cases it answers normally and does not start a lesson. If you explicitly ask for its way
of teaching on a single concept, it runs a short version — explain, one check, feedback — without
setting up a course, notes, or a review schedule.

## How to use it

Just say what you want to learn and why. The first reply will usually ask for:

1. the goal, in terms you can check;
2. how deep you need to go, and by when;
3. whether there is a textbook or an exam scope to follow;
4. once, whether you want Obsidian for the notes (optional, off by default).

Then it starts asking you questions. Answering "I don't know" is useful information, not a
failure — a blank is recorded as evidence, never filled in for you.

### Commands you can use mid-session

| Say | Effect |
| --- | --- |
| `skip` | drop a knowledge point, recorded as skipped, never as mastered |
| `just tell me` | suspend the questioning style for this one question |
| `explain fully` | pause checks and explain systematically |
| `deeper` / `lighter` | change the depth tier |
| `show progress` | print the compact state block |
| `save state` / `resume from:` | carry progress into a new session |

## What you actually see

### Question cards, inside the chat

When the host supports interactive cards, questions arrive as a card rather than a wall of text:
single choice, multiple select, fill-in-the-blank, several blanks in one question, or a
multi-question diagnostic set.

Every card works the same way: the judgement happens **inside the card** (nothing is sent), a
reason box is always available, one confirm sends a single message with the question, your answer,
the verdict and your reasoning, and two fixed options sit apart from the answers —

- `难度太高，需要大幅降低难度` (too hard — lower the difficulty)
- `难度太低，可以快速提升难度` (too easy — raise the difficulty)

These two labels are fixed in Chinese by the card contract, so they stay as written; the gloss is
for readers. Both send immediately and are never graded.

### Explainer pages, when prose is the wrong shape

If the content has cases, branches, a waveform, a circuit, or three concepts that must be held
together, it produces a single-page HTML explainer with one panel per case, and states the
conclusion in the reply as well. Figures are chosen by content type: a plotting library for
waveforms and curves, a sourced figure for complex circuits, hand-written SVG for simple
diagrams. A table of attributes is never accepted as a substitute for a waveform.

### Two kinds of notes

- **`notes/N01-<point>.md`** — a terse state record: conclusion, the error you actually made,
  relations, last result. Its reader is the assistant resuming your session.
- **`review/R01-<point>.html`** — a single-file page you reopen: one-screen recap, the key
  figure, wrong-question redo with local checking, a relation map, links to neighbours. Works
  offline, remembers what you mastered.

They share a number and live in `<CODE>-<subject>/{notes,review,explain,figures}`, so a folder
stays readable at thirty files.

The review page never phones home: answers are judged in the page, progress sits in your browser's
local storage, and the "copy review prompt" button only copies text.

## Install

### Option A — let your agent install it

Copy the block below into your agent (Claude Code, WorkBuddy, Codex, Cursor, Gemini CLI, …). It
asks before writing anything, and checks the result afterwards.

```
Please install an Agent Skill for me.

Source: https://github.com/DGTSAlight/learning-assistant
(If that URL does not open, ask me for the correct one instead of guessing.)

1. Tell me which agent I am using, then find its user-level skills directory:
   WorkBuddy       ~/.workbuddy/skills/  or  ~/.workbuddy-ai/skills/
   Claude Code     ~/.claude/skills/
   Codex           ~/.codex/skills/
   OpenCode        ~/.config/opencode/skills/
   Cursor          ~/.cursor/skills/
   Gemini CLI      ~/.gemini/skills/
   GitHub Copilot  ~/.copilot/skills/
   CodeBuddy       ~/.codebuddy/skills/
   Anything else:  wherever that agent discovers SKILL.md files.
   If you are unsure, ask me before writing.

2. Download the repository (git clone; if git is unavailable, download the zip and extract it)
   and copy the learning-assistant folder into that directory. The end state must be:
   <skills dir>/learning-assistant/SKILL.md

3. Check the result and report it:
   - SKILL.md exists at that path and opens
   - references/, assets/, scripts/, evals/ are all present
   - there is no doubled folder (not learning-assistant/learning-assistant/)

4. Do not edit SKILL.md, and do not install anywhere outside my skills directory.

5. Tell me what to do so the skill shows up — usually starting a new session.
```

### Option B — do it by hand

Copy this directory into your agent's user-level skills directory, or into its project-level
directory if you want the skill in one repository only.

| Agent | User-level | Project-level |
| --- | --- | --- |
| WorkBuddy | `~/.workbuddy/skills/` (some builds: `~/.workbuddy-ai/skills/`) | `.workbuddy/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.codex/skills/` (also reads `~/.agents/skills/`) | `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.agents/skills/` |
| Pi | `~/.agents/skills/` | `.agents/skills/` |
| DSH (DeepSeek Harness) | `~/.dsh/skills/` | `.dsh/skills/` |
| Cursor | `~/.cursor/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.agents/skills/` |
| GitHub Copilot | `~/.copilot/skills/` | `.agents/skills/` |
| CodeBuddy | `~/.codebuddy/skills/` | `.codebuddy/skills/` |

```bash
git clone https://github.com/DGTSAlight/learning-assistant
cp -r learning-assistant ~/.workbuddy/skills/
```

If your agent is not listed, put the directory wherever that agent discovers `SKILL.md` files.
DSH can also install a skill as a plugin with `dsh plugin add`.

Start a new session so the skill appears in the available-skills list.

## Optional tools

All are enhancements with a plain-Markdown fallback; none is required.

- **answer-me-with-html** — single-page HTML explainers. Its CLI is a script inside that skill's
  directory, not a guaranteed global `am` command. Install guide:
  https://github.com/QingYunA/answer-me-with-html/blob/main/INSTALL.md
- **A Python with matplotlib** — only needed for plotted waveforms and curves. If the default
  interpreter has none, the skill looks in your conda environments and other installs, then offers
  to save the one it found as the default for the project. Without it you get an SVG sketch.
- **Obsidian** — wikilinks, properties, and `.canvas` relation maps for the knowledge network.
  Plain Markdown with `[[wikilinks]]` is the required baseline.
- **Inline chat cards** — require host theme variables and a message-return API. Without them,
  cards degrade to text choices or copyable prompts.

## What's inside

```
learning-assistant/
├── SKILL.md                          metadata, core loop, selection table, resource index
├── references/
│   ├── general-learning.md           domain-independent rules (always read)
│   ├── code-learning.md              code domain (read only when selected)
│   ├── mathematics.md                mathematics domain
│   ├── power-electronics.md          power electronics domain
│   ├── sensors.md                    sensors and measurement domain
│   ├── presentation.md               explainers, inline cards, math notation
│   ├── technical-figures.md          when a figure is required, and how to produce it
│   ├── knowledge-network.md          notes, review pages, optional vault
│   └── gates.md                      optional hard checks
├── assets/                           worked examples: question cards, a review page, a waveform
├── scripts/                          a runnable waveform script and an optional gate check
└── evals/                            25 trigger cases, 50 queries, Chinese and English
```

`SKILL.md` is the only index; reference files are self-contained and do not reference each other,
so file references stay one level deep. The domain references are optional — the general layer
alone can run a session, and a domain file only adds scope, order, and checks.

## Scope and limits

- **It does not replace your textbook.** For a course with an exam scope, it asks which textbook
  and which chapters before using them.
- **Its output quality depends on your honesty.** "I know this" without a check is taken as a
  claim, not a fact — and it will test it.
- **Notes are yours.** They are written into your project directory, never into the skill
  directory, and the skill keeps no state of its own.
- **Nothing is uploaded.** Review pages are local files; the skill has no network behaviour of
  its own beyond the searches you can see it run.

## License

MIT — see [LICENSE](LICENSE).
