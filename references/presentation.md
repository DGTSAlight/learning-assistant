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
- The worked examples are standalone HTML documents. An inline card is a fragment: strip the
  document shell and keep only the card markup, its styles, and its script.

### Question card contract

Every card that presents a question, of any type, follows the same four-part flow. The point is
to judge the learner's reasoning, not only the selected option.

1. **Answer controls** — one of single choice, multiple select, or fill-in-the-blank. Multiple
   select needs a local check control because the set is complete only after the last toggle;
   fill-in-the-blank needs one because free text must be normalised and compared against a list
   of acceptable answers. Note the question text in the card so the sent prompt can quote it.
2. **Free-text reasoning field** — present on **every** question card, including choice cards,
   so a short explanation can be requested at any time. It is optional by default; the task text
   may make it required. A choice question must never be answer-only: a correct option without a
   reason may be a lucky guess.
3. **Local verdict, then one confirm gate** — clicking an answer control, or the local check,
   shows correct/incorrect immediately inside the card and sends nothing. A wrong verdict gives
   a direction hint, not the full solution. One explicit confirm control then sends a **single**
   message containing the question, the answer(s), the local verdict, the free-text explanation,
   and an instruction to evaluate the reasoning rather than the option. Confirm stays disabled
   until a local verdict exists; any change to the answer invalidates that verdict and requires
   a new local check.
4. **Two reserved difficulty options** — added to every question card, visually separate from
   the answer controls, never judged right or wrong, never counted as an answer. They are the
   only exception to the confirm gate: clicking one sends immediately.

The reserved options are a fixed contract with these exact labels. An English gloss follows the
Chinese text in the button so the card stays usable across languages.

| Reserved label | What the sent prompt asks for |
| --- | --- |
| `难度太高，需要大幅降低难度` | Replace the current question with a much easier one on the same knowledge point; supply the missing prerequisite first, then re-check. Do not just reveal the answer. |
| `难度太低，可以快速提升难度` | Skip the current difficulty tier and give a clearly harder question or a transfer variant on the same knowledge point, then re-check. |

Both prompts must be complete and standalone: restate the exact label, name the current
question, and state that the question was not answered. The assistant responds by re-setting the
difficulty, not by grading an answer. All other card text follows the user's language; only
these two labels are fixed.

### Buttons bound to prompts

When message return is supported, a button may carry a preset prompt. Requirements:

- The button label must match what is actually sent; a decorative arrow is not part of the label.
- The prompt must be complete and standalone: it carries the question text, not "this question".
- The confirm gate sends one consolidated message per question; never one message per click.
- If message return is unavailable, degrade to copying the assembled prompt to the clipboard
  and tell the user. If that also fails, show the prompt inside the card so it can be pasted.
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
| No inline cards | Text choices, a written one-line reason, and the two difficulty commands as copyable text |
| No theme variables | Neutral solid colours |
| No message-return API | Copy prompt to clipboard |
| No source-fetch tool | Say what the explanation is based on |

Never claim a tool, page, file, or command was used unless it actually was.
