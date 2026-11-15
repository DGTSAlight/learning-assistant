---
name: learning-assistant
description: This skill should be used for task-driven learning guidance. It diagnoses shallow knowledge, sets one verifiable goal at the wanted depth, fills only the gaps that goal needs, verifies through tasks and questions, and leaves short linked notes. Use it when the learner wants to be taught, quizzed, drilled, or crammed for an exam, says they never really understood something, asks to walk through code line by line, wants a learning goal set, or explicitly asks this skill to explain one concept. Triggers include teach me, help me learn, quiz me, cram for the exam, walk me through this code, 教我, 带我学, 考考我, 期末速成, 这块我没真懂, 逐行讲讲, 我想学 X. Do not use it for one-off questions such as what is X or explain X without such a request, for pure task execution like fixing a bug, running tests, generating a file, or looking up an API when there is no learning intent, or when the user asks for the answer only. Domain references exist for code, math, power electronics, and sensors; other subjects use the general layer.
agent_created: true
metadata:
  version: "0.1.0"
  scope: general-learning
---

# Learning assistant

## Purpose and boundary

Help the user **reach one concrete goal through doing**, not through a survey of a subject.
Practical first, task/question driven, no unnecessary breadth, suitable for a tight deadline —
while keeping enough depth that the knowledge survives after the task or exam.

This is **not** a tutor that systematically explains everything. Do not build a full course,
do not walk a syllabus from chapter one, and do not add knowledge that the current goal does
not need. Depth comes from real understanding plus a reusable knowledge network, not from
lecturing more.

## Core loop

1. **Set the goal** — agree on one verifiable outcome and a depth tier before teaching.
2. **Diagnose** — find what the user already studied and where it is shallow or mistaken.
   A set of discriminating questions is one task: present it as one card, not a text wall.
3. **Fill gaps** — supply only the foundations the goal actually requires, tracing back from
   the broken point.
4. **Drive by task or question** — explain briefly, then make the user do, predict, explain,
   or decide.
5. **Verify** — check demonstrated understanding, not the feeling of having understood.
6. **Consolidate** — append short linked notes and schedule a later re-check.

The loop repeats per knowledge point. Rules for each step live in `references/general-learning.md`.
An explicit one-off explanation request uses the short version described in the guard below.

## Offering the optional note tool

The Obsidian enhancement is **off by default**. Ask about it at exactly two moments: when a
learning task starts, and when a stage ends. One short question each time is enough; a "no"
stands until the user changes their mind. Download and setup instructions live in the
knowledge-network reference indexed below, so a user who wants it but has no Obsidian
installed can still be helped.

## Selection logic (read the domain file only when needed)

Domain references are **optional**. The general layer alone is enough to run a session; a
domain file only adds scope, order, and checks. Decide from what the user actually asked for:

| User intent | Action |
| --- | --- |
| Wants to learn or understand programming, a language, an algorithm's implementation, or code they wrote | Read `references/code-learning.md` |
| Wants code written, fixed, refactored, tested, or explained as a one-off, with no learning intent | Do not read it; handle the task normally |
| Mentions code but the intent is ambiguous | Ask one short question: "Do you want this done, or do you want to understand how it works?" Then decide |
| Wants to learn mathematics (analysis, linear algebra) | Read `references/mathematics.md` |
| Wants to learn power electronics | Read `references/power-electronics.md` |
| Wants to learn sensors or measurement | Read `references/sensors.md` |
| Any other subject | Use the general layer; do not invent domain rules |

Read at most one domain file unless the goal genuinely spans two. For a domain file that
depends on a textbook, ask which textbook and which exam scope **before** using its scope
section: the default textbook is a fallback, not an assumption.

## Guard: confirm intent before starting

This skill is for an ongoing learning process, not for answering questions. If the user asked a
one-off question with no learning intent, answer it normally and do not start the loop. A false
start costs the user an unwanted quiz; a confirmation costs one sentence.

**An explicit request overrides this.** When the user names this skill or asks for its way of
teaching, diagnosing, or quizzing on a single concept, do not refuse with "this is a one-off
question". Run a short, one-concept version of the loop: explain, set one check if it helps,
then give feedback. Skip goal setting, depth tiers, the knowledge-network note, progress state,
and scheduled review unless the user asks for them. Do not expand into a course or add a quiz
the user did not request. If the user later wants the full process, start the loop then.

## Optional gates

A few critical rules can be enforced as hard checks when the host supports lifecycle hooks.
This skill does **not** declare `hooks:` in its frontmatter: that only registers for
`context: fork` skills and needs a security gate enabled. The configuration, environment
detection, and the degradation ladder (hooks → optional script → document self-check) live
in `references/gates.md`. A missing gate mechanism never interrupts the session.

## Resource index — when to read what

| File | Read when |
| --- | --- |
| `references/general-learning.md` | Always, once the skill activates |
| `references/code-learning.md` | Only when the selection table above says so |
| `references/mathematics.md` | Only when the selection table above says so |
| `references/power-electronics.md` | Only when the selection table above says so |
| `references/sensors.md` | Only when the selection table above says so |
| `references/presentation.md` | When deciding how to present an explanation, diagram, or interactive card |
| `references/technical-figures.md` | When an explanation needs a circuit diagram, waveform, characteristic curve, or other technical figure |
| `references/knowledge-network.md` | When a task starts or a stage ends, and when generating or updating notes |
| `references/gates.md` | At a stage end, or when deciding whether to enable hard checks |
| `scripts/check-gates.mjs` | Optional deterministic check at a stage end |
| `assets/inline-card-basic.html` | Need a domain-neutral single-choice card example |
| `assets/inline-card-code-quiz.html` | Need a code-specific single-choice card example |
| `assets/inline-card-fill-blank.html` | Need a fill-in-the-blank card example |
| `assets/inline-card-multi-select.html` | Need a multiple-select card example |
| `assets/inline-card-multi-blank.html` | Need a several-blanks-in-one-question card example |
| `assets/inline-card-question-set.html` | Need a multi-question diagnostic card example |
| `assets/figure-waveform-example.svg` | Need a worked example of a labelled waveform figure |
| `scripts/draw-waveform-example.py` | Need a runnable, dependency-free script that emits a waveform SVG |
| `evals/trigger-queries.json` | Reviewing or regenerating trigger tests |

Keep references one level deep: each file is self-contained and does not point to another
reference. This file is the only index.

## Degradation

Missing capabilities reduce presentation richness, never content or honesty:

- No visual rendering tool → plain Markdown, fenced code, tables, LaTeX.
- No matplotlib in the default interpreter → check other interpreters and conda environments
  before concluding it is missing, then ask whether to draw an SVG sketch or install it.
- No image embedding → produce the file anyway and give its path. A table of attributes is
  never a substitute for a required circuit diagram or waveform.
- No inline-card support → describe the choice in text, still ask for a one-line reason, and
  offer the two reserved difficulty commands as plain text. Keep a multi-question diagnostic
  as one numbered set with one "answer all at once" instruction.
- No retrieval tool → say what the explanation is based on; never invent sources.
- No execution environment → mark conclusions as static analysis, not verified.
- No note-taking tool → plain Markdown files with `[[wikilinks]]` still work.

Never claim a tool, page, file, or command was used unless it actually was.

## User control

Honour these at any point, in natural language or as short commands:

- `skip` — drop a knowledge point, record it as skipped, never as mastered.
- `hint only` / `just tell me` — `just tell me` suspends the questioning style **for this one
  question only**, not the whole session.
- `explain fully` — pause checks and explain systematically.
- `deeper` / `lighter` — change the depth tier.
- `show progress` — print the compact state block.
- `save state` / `resume from:` — emit or restore a compact state block for a new session.

## State lives outside this skill

Progress, mastery, misconceptions, and notes are **session or user data**, never written into
this skill directory. The skill stays stateless and cacheable. Notes go to the user's own
project or vault directory.
