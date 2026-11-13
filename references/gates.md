# Optional gates (hard checks)

Self-contained rules for turning a few critical teaching rules into hard checks.
`SKILL.md` is the only index; this file does not reference another reference file.

## Why gates exist

Prompt rules alone are easy to skip: a point gets marked mastered without two checks, code is
shown as if it had been run, or a stage ends with no notes. Gates make those steps observable.
They are **optional** for this skill — the learning session must never stop because a gate
mechanism is unavailable.

## What to check

| # | Gate | Pass condition |
| --- | --- | --- |
| 1 | Goal set | A verifiable goal and a depth tier were agreed before teaching started |
| 2 | Mastery evidence | A point marked `mastered` has at least two independent checks, one of them unprompted recall |
| 3 | Prep verification | Commands, code, or worked results shown in an explanation were actually run or checked; otherwise labelled unverified |
| 4 | Notes landed | At a stage end, short notes were written or updated and the review result recorded |
| 5 | Honest status | No unverified result is described as tested; `learned`, `reviewed`, `statically checked`, and `executed` stay distinct |

These mirror the general rules; this file only makes them checkable at a stage boundary.

## Environment detection

The host may or may not expose lifecycle hooks. WorkBuddy / CodeBuddy Code **does** support
them, with important conditions:

- Hooks are configured under the `hooks` key of a user-level `settings.json` (or project
  settings). Events include `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`,
  `SessionStart`, and more. The format matches Claude Code; on Windows, hook commands run
  under **Git Bash**, not cmd.exe or PowerShell.
- `PreToolUse` can block a tool call. Hooks run with the user's credentials, so review any
  script before enabling it.
- **`SKILL.md` frontmatter hooks are conditional**: only `context: fork` skills register them.
  Injected skills — the default, including this one — parse the field but do not register it.
- Frontmatter hooks additionally require `allowUntrustedFrontmatterHooks: true` in
  `settings.json`; it is off by default and silently skipped otherwise. The feature is Beta.

Therefore this skill **does not declare `hooks:` in its frontmatter**. Declaring it here would
not work for an injected skill and would make the skill depend on a non-standard field.

Detect before enabling:

1. Does the host expose `/hooks` or a `hooks` key in settings?
2. If frontmatter hooks are wanted, is `allowUntrustedFrontmatterHooks` on, and is the user
   willing to switch this skill to `context: fork` (which changes how it is invoked)?
3. If either answer is no, use the degradation ladder below.

## Optional hooks configuration (opt-in only)

Two ways, neither enabled by default. Replace the placeholder path with the installed skill
directory; never hard-code a machine-specific absolute path in a published file.

**A. Session-level `settings.json`** — applies to all tasks in that project:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "node <path-to-skill>/scripts/check-gates.mjs" }
        ]
      }
    ]
  }
}
```

**B. `SKILL.md` frontmatter** — only for a `context: fork` variant, and only with the
security gate enabled. Use a separate copy of the skill; do not convert the default one:

```yaml
---
name: learning-assistant
description: ...
context: fork
agent: Explore
hooks:
  Stop:
    - hooks:
        - type: command
          command: "node ${CODEBUDDY_SKILL_DIR}/scripts/check-gates.mjs"
---
```

Keep hooks small and side-effect free: no network calls, no writes outside the user's
project, short timeouts, and a clear failure message instead of a silent pass.

## Degradation ladder

Use the first level that is actually available:

1. **Hooks available and enabled** — the script runs automatically at a stage end and blocks
   or reports on a failed gate.
2. **No hooks** — **script constraint**: at a stage end, run
   `node scripts/check-gates.mjs` with the current session state. It is voluntary rather than
   automatic, but the check itself is deterministic.
3. **No script either** — **document constraint**: at a stage end, walk through the five
   gates above as a short self-check and state the result in one line. This is the required
   baseline and always works.

Never claim a gate passed unless it actually ran. Never let a missing gate mechanism
interrupt the learning session or replace the user's control commands.

## Script input (optional)

`scripts/check-gates.mjs` reads a JSON state object from stdin or a file argument. It is a
convenience, not a new source of truth; the state comes from the session, not from the skill
directory.

```json
{
  "goal": "compute eigenvalues of a 2x2 matrix and explain them",
  "depth": "usable",
  "prepVerified": true,
  "notesWritten": true,
  "points": [
    { "name": "determinant", "checks": 2, "unpromptedRecall": true, "status": "mastered" },
    { "name": "characteristic polynomial", "checks": 1, "unpromptedRecall": false, "status": "shaky" }
  ]
}
```
