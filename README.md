# learning-assistant

Task/question driven learning guidance as an Agent Skill. Practical first, no unnecessary
breadth, suitable for a tight deadline, while keeping enough depth to survive after the
task or exam.

English | [简体中文](README.zh-CN.md)

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
├── assets/
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
the intent is ambiguous, the skill asks one short question first. Other subjects use the
general layer.

## Install

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
cp -r learning-assistant ~/.workbuddy/skills/
```

If your agent is not listed, put the directory wherever that agent discovers `SKILL.md`
files. DSH can also install a skill as a plugin with `dsh plugin add`.

Start a new session so the skill appears in the available-skills list.

## Optional tools

All are enhancements with a plain-Markdown fallback; none is required.

- **answer-me-with-html** — single-page HTML explainers. Its CLI is a script inside the skill
  directory, not a guaranteed global `am` command. Install guide:
  https://github.com/QingYunA/answer-me-with-html/blob/main/INSTALL.md
- **Obsidian** — wikilinks, properties, and `.canvas` relation maps for the knowledge
  network. Plain Markdown with `[[wikilinks]]` is the required baseline.
- **Inline chat cards** — require host theme variables and a message-return API. Without
  them, cards degrade to text choices or copyable prompts.
