# Presentation rules

Self-contained rules for how an explanation is shown. These are means, not the content.
`SKILL.md` is the only index; this file does not reference another reference file.

## Priority order

1. **Graphical content** — when a diagram, multi-panel layout, comparison, flow, or
   structure would help, first try a single-page HTML explainer via the `answer-me-with-html`
   skill. Its CLI is a bundled script inside that skill's directory, not a guaranteed global
   `am` command; use the actual script path, and verify the tool exists before claiming a
   page was generated.
2. **Interactive content** — when the user needs to click, choose, switch, or adjust, first
   try an inline chat card rather than describing "you could try this".
3. **Fallback** — plain Markdown, fenced code, lists, tables, and LaTeX. Never force a
   visual when the environment does not support it, and never drop content because of it.

A long-term knowledge note is a **deliverable**, not a per-turn presentation. It follows the
note rules, not this priority list.

## Pages are a supplement

The reply body still carries the conclusion and the key explanation. Do not move everything
into a page. After generating one, state its path and main panels so the user can find it
later. Do not make a page for something a sentence can answer. Content accuracy beats
decoration.

## Inline card style

- Flat: solid fills, 0.5px borders, 8–12px corner radius. No gradients, shadows, glow,
  decorative illustration, or emoji.
- Use the host's theme variables for background, text, borders, and semantic colours so both
  light and dark themes stay readable. If they are unavailable, substitute neutral colours
  and keep it flat.
- Type: headings 14–15px, body 13px, helper text 12px, nothing below 11px; only regular and
  medium weights.
- One card, one task. Do not cram a concept, a question, a progress bar, and controls into
  the same card.
- Bind events with `addEventListener`, not inline `onclick` attributes — some hosts block
  inline handlers via CSP.
- Local judgements (right/wrong, toggles, small calculations) happen inside the card; do not
  send a chat message just to evaluate a click.

### Buttons bound to prompts

When message return is supported, a button may carry a preset prompt. Requirements:

- The button label must match what is actually sent.
- The prompt must be a complete, standalone instruction, not a fragment relying on context.
- If message return is unavailable, degrade to copying the prompt to the clipboard and tell
  the user.
- Worked card examples are listed in the skill index; they are resources, not rules to
  inline here.

### Limits

Inline cards are valid only in the current conversation. They cannot read local files, cannot
run commands, and disappear when the session restarts. For something durable, large, or
repeatedly opened, produce a note or a standalone page instead.

## Degradation

| Missing | Behaviour |
| --- | --- |
| No page renderer | Markdown / code fences / tables / LaTeX |
| No inline cards | Text choices, or copyable prompts |
| No theme variables | Neutral solid colours |
| No message-return API | Copy prompt to clipboard |
| No source-fetch tool | Say what the explanation is based on |

Never claim a tool, page, file, or command was used unless it actually was.
