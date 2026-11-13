# learning-assistant

Task/question driven learning guidance as an Agent Skill. Practical first, no unnecessary
breadth, suitable for a tight deadline, while keeping enough depth to survive after the
task or exam.

**Status: v0.1.0 skeleton.** Structure and rules are in place; trigger evals and the three
scenario walkthroughs have not been run yet.

## What it is not

Not a tutor that explains a whole subject systematically. It sets one verifiable goal, finds
where the user's existing knowledge is shallow, fills only the gaps that goal needs, verifies
real understanding through tasks and questions, and leaves short linked notes for later
review.

## Layout

```
learning-assistant/
├── SKILL.md                          metadata, core loop, selection table, resource index
├── references/
│   ├── general-learning.md           domain-independent rules (always read)
│   ├── code-learning.md              code domain (read only when selected)
│   ├── presentation.md               graphics, inline cards, degradation
│   └── knowledge-network.md          long-term notes, optional vault enhancement
├── demo/
│   ├── inline-card-basic.html        domain-neutral card example
│   └── inline-card-code-quiz.html    code card example
└── evals/
    └── trigger-queries.json          20 trigger queries, including near-miss negatives
```

`SKILL.md` is the only index. Reference files are self-contained and do not reference each
other, keeping file references one level deep.

## Triggering

Activates when the user wants to learn, be taught, be checked, set a learning goal, or fix
shallow prior knowledge — including vague "I want to learn X" and exam-cram requests.

Does not activate for one-off questions, pure task execution (fix a bug, run tests, generate a
file, look up an API), or when the user asks for the answer only.

Code-specific rules load only when the user explicitly wants to learn or understand code. If
the intent is ambiguous, the skill asks one short question first.

## Install

Copy this directory into your agent's user-level skills directory, for example:

```bash
cp -r learning-assistant ~/.workbuddy-ai/skills/
```

Start a new session so the skill appears in the available-skills list. Some installers place
skills in a different directory (for example `~/.codebuddy/skills/`); make sure the copy ends
up in the directory your agent actually reads.

No installation step belongs inside `SKILL.md` or the reference files — those are loaded on
every activation.

## Optional tools

All are enhancements with a plain-Markdown fallback; none is required.

- **answer-me-with-html** — single-page HTML explainers. Its CLI is a script inside the skill
  directory, not a guaranteed global `am` command. Install guide:
  https://github.com/QingYunA/answer-me-with-html/blob/main/INSTALL.md
- **Obsidian** — wikilinks, properties, and `.canvas` relation maps for the knowledge
  network. Plain Markdown with `[[wikilinks]]` is the required baseline.
- **Inline chat cards** — require host theme variables and a message-return API. Without
  them, cards degrade to text choices or copyable prompts.

Domain files for mathematics, power electronics, and sensors are **planned, not shipped**.
Do not create them until the user supplies domain details and approves.

## Development notes

- Keep `SKILL.md` under 500 lines; move detail into `references/`.
- Every change to the `description` field is a routing change — record before/after text and
  trigger rates.
- Progress and notes are user data and never written into this directory.
- The local git repository has no remote. Do not push until the user decides to open-source.

## Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-11-13 | Initial skeleton: general + code domain, presentation, knowledge network, demos, trigger eval set |
