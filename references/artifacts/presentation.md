# Presentation rules

Self-contained rules for how an explanation is shown. These are means, not the content.
`SKILL.md` is the only index; this file does not reference another reference file.

## Priority order

**Step 0, before choosing anything:** will the learner reopen this artefact? If yes, it is a page —
rule 1 — whatever the host happens to offer. If no, any of the three is acceptable.

1. **Graphical content** — when the explanation contains parts that relate, branch, change
   over time, or depend on a condition, **produce** a single-page HTML explainer via the
   `answer-me-with-html` skill. Do not wait for the user to ask for a diagram, and do not
   require a long answer as a precondition. Its CLI is a bundled script inside that skill's
   directory, not a guaranteed global `am` command; use the actual script path, and verify the
   tool exists before claiming a page was generated.
2. **Interactive content** — when the user needs to click, choose, switch, or adjust, first
   try an inline chat card rather than describing "you could try this".
3. **Fallback** — plain Markdown, fenced code, lists, tables, and LaTeX. Never force a
   visual when the environment does not support it, and never drop content because of it.

A long-term knowledge note is a **deliverable**, not a per-turn presentation. It follows the
note rules, not this priority list.

The same applies to the review page the user reopens weeks later. Build it from the note
template by hand, **not** with the page renderer: it needs local judgement, a wrong-question
pool, and stored progress, and a generated explainer page has none of those. An explainer page
explains once; a review page is used repeatedly.

### A host drawing widget is not a page

Many hosts can draw an SVG, a diagram, or a small chart inline — a `show_widget`-style tool, or a
"render this HTML" preview. That is a **one-turn sketch**: it lives inside the message, scrolls
away, disappears when the conversation is compacted, cannot be opened from disk, and cannot be
linked from a note or a review page.

Use one only when all three hold: the picture is a small aside, nothing durable was asked for, and
no learning task is in progress. Otherwise produce a standalone HTML file.

| Content | Lifetime it needs | What to use |
| --- | --- | --- |
| A quick sketch inside one explanation, no case split | this turn | the host's inline widget is fine |
| Cases, branches, a waveform, a circuit, or three linked concepts | the user will re-read it | standalone HTML page |
| Anything a note or review page will link to | permanent, on disk | standalone HTML page |

Once a learning task is running — a goal was set, notes exist — the default is a **standalone
page**, not an inline sketch. The user paid for a session; the artefact should outlive it. Do not
choose the inline widget because it is one call away.

### When a page is the default, not an option

Generate a page proactively when **any one** of these signals is present. One signal is enough.

| Signal | Why prose fails |
| --- | --- |
| The learner is diagnosed as shaky / not learned, has just answered wrong twice, or is confusing two mechanisms | A paragraph lets the wrong model survive; a page makes the split visible |
| The content has **two or more conditions or cases** (A vs B, on vs off, continuous vs discontinuous, before vs after a boundary) | Linear text cannot show which fact belongs to which case |
| There is a branch, flow, state transition, commutation, or waveform sequence | Order and timing are the content |
| Three or more concepts must be held together (mechanism → consequence → usual mistake) | A sentence chain loses the links |
| A comparison, trade-off, or can/cannot list across two or more dimensions | A table or panel is the shape of the answer |
| The reader must see shape, slope, zero crossings, phase, connectivity, or device labels | A real plotted figure or circuit diagram is required; the figure resource listed in the skill index gives the method |

**A weak foundation raises the priority, it does not lower it.** When the diagnostic shows the
user is new or shaky, generate the page before the next check instead of compressing the
explanation into a dense paragraph to save turns. "Explain briefly" limits the prose, not the
visual: a short reply plus one page is still brief, and is not an expansion into adjacent
topics.

Do not require three separate concepts, a long answer, or an explicit request as a gate. The
only reasons to stay in prose are: one isolated fact with no relation, a pure confirmation, or
a renderer that is unavailable. If the host has the `answer-me-with-html` skill configured as
always-on, follow that setting.

### Case splits need a page, not a paragraph

If an explanation contains "only two ways", "if A ... but if B ...", "on one side of the
boundary ... on the other", or any list of conditions, render it as a flow, comparison table,
or timeline with **one panel per case**, then state the conclusion in the reply body. A single
paragraph that mixes several mechanisms and several cases without showing which statement
belongs to which case is the failure mode to avoid.

### A figure next to prose belongs in a page

Do not post an image after a paragraph and describe it above. The reader scrolls between the
picture and the sentence that refers to it, and on a narrow screen it is worse. When an
explanation needs both, they go into one page: the figure with its labels, then the prose that
reads it, in that order. A figure floating at the end of a chat message is not a figure — it is a
tab the reader has to keep switching to.

Formulas are the same problem in another form. Chat renders plain text, so `U_d = 0.9 U_2 cos α`
arrives as characters with a visible underscore, not as a formula. If the explanation turns on a
formula, that is a second, independent reason to produce the page — the page typesets it.

### A table is not a figure

When the content is a circuit topology, a waveform, a characteristic curve, or a timing
diagram, a table of attributes or a chain of flow boxes states the conclusion but does not show
the shape. A panel that lists "resistive load: u_d = 0 / inductive load: u_d goes negative" has
not shown the negative interval on a time axis. Add a real figure and keep the table or flow
box only as a companion. Pick the route by content type (the figure reference listed in the
skill index gives the full method): matplotlib for function plots and waveforms, a sourced
figure first for complex circuits, hand-written SVG for simple diagrams. Do not let the page
renderer's built-in components decide this: `chart` suits discrete numbers, `flow` suits causal
order, and neither carries a piecewise waveform with a firing angle or a labelled conduction
interval.

## Pages are a supplement

The reply body still carries the conclusion and the key explanation. Do not move everything
into a page. After generating one, state its path and main panels so the user can find it
later. Skip a page only for one isolated fact with no relation, or a pure confirmation. Do not
use "a sentence could answer it" to skip a page when a signal above is present. Content
accuracy beats decoration.

## Math and notation in explainer pages

Page renderers typeset TeX at build time, not in the browser. **Only text inside `$...$` or
`$$...$$` is typeset.** A bare `U_i`, `u_L`, or `t_on` in prose or a table cell stays plain text:
the underscore is visible, the subscript is missing, and the CLI reports **no warning**. That is
why a page can look partly rendered — a block formula is fine while every inline symbol in the
body and the tables is not. This is a draft-writing error, not a renderer bug.

- Wrap **every** symbol with a subscript, superscript, fraction, Greek letter, or operator in
  `$...$` — in prose, lists, captions, **and table cells**. `$U_o = D U_i$` renders; `U_o = D U_i`
  does not. Table cells support inline math.
- Use braces for multi-character subscripts: `$t_{\mathrm{on}}$`, `$U_{o}$`, `$i_{L}$`. Never
  write `$t_on$`, and never leave `t_on` bare.
- Use `$$` on its own lines for a long or important formula; a block scrolls inside its panel.
- A closing `$` followed directly by a letter or underscore does not close the formula: write
  `$n$-th`, not `$n$th`. Put a space or punctuation after the closing `$`.
- In a table cell write `\vert x \vert`, not `|x|` — the pipe breaks the table.
- Do not use `\ref`, `\eqref`, or `\label`; `\tag{1}` works in a block.
- **Inspect the rendered page** and check inline and table formulas. A clean render with zero
  warnings proves nothing about subscripts, because bare text is not an error. Raw red TeX means
  the syntax on that line must be fixed and the page rendered again.

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
- **Never find the card with `document.currentScript`.** In several inline renderers it returns
  `null`; the first line then throws, every listener below it is never bound, and the result is a
  card that looks perfect and has only dead buttons. Give the wrapper an `id` and locate it with
  `document.getElementById('…')`, or bind in bulk with `querySelectorAll('.some-class')`. If the
  script needs its own container, pass the id in as a constant instead of discovering it.
- **Do not build the card's script around a single top-level statement.** Wrap the whole script in
  an IIFE and bind each control in its own loop, so one missing element cannot kill the rest.
- Local judgements (right/wrong, toggles, small calculations) happen inside the card; do not
  send a chat message just to evaluate a click.
- The worked examples are standalone HTML documents. An inline card is a fragment: strip the
  document shell and keep only the card markup, its styles, and its script.

### Question card contract

Every card that presents a question, of any type, follows the same four-part flow. The point is
to judge the learner's reasoning, not only the selected option.

1. **Answer controls** — one of single choice, multiple select, fill-in-the-blank, several
   blanks in one question, or a set of related questions. One card is scoped to **one task**,
   not to one question. Multiple select needs a local check control because the set is complete
   only after the last toggle; fill-in-the-blank needs one because free text must be normalised
   and compared against a list of acceptable answers. Note every question text in the card so
   the sent prompt can quote it.
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
   a new local check. Open answers are the exception — see below: no verdict is fabricated, the
   prompt says the verdict is unavailable, and confirm is enabled once at least one answer is
   written.
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

### Question sets and multiple blanks

A card is scoped to **one task**, not to one question. A diagnostic set of 2–5 related
questions, one question with several blanks, or one question with several sub-questions is one
task. When the plan asks several questions at once, do **not** fall back to a plain-text list
because a worked example happens to show a single question. Choose one of these shapes:

| Situation | Card shape |
| --- | --- |
| Questions should be answered together and graded together (diagnostic, "answer all, then I will give feedback") | One **question-set card**: one field per question or sub-question, one confirm, one consolidated prompt |
| Questions are independent and should be graded one at a time | Several single-question cards, one per question, each with its own confirm |
| One question has several blanks | One **multi-blank card**: one input per blank, one local check, one confirm |

Rules for question-set cards:

- Number every question and sub-question. The confirm prompt quotes each question text and each
  answer, and marks unanswered ones as `(unanswered)`. A blank is diagnostic evidence, not a
  skipped point; never fill it in for the user.
- Keep the single confirm gate and the two reserved difficulty options. Local interactions
  such as revealing a direction hint stay inside the card and send nothing.
- **Open answers have no local verdict.** Do not fabricate correct/incorrect for free text.
  State that the verdict is unavailable and ask the assistant to grade each answer separately,
  name the layer where the reasoning broke, and set the next difficulty.
- Confirm stays disabled until at least one answer is non-empty. Editing an already-checked
  multi-blank card invalidates its local verdicts and requires a new local check.

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
| No page renderer | Markdown / code fences / tables / LaTeX; still split cases into a Markdown table or numbered branches, not a dense paragraph |
| No inline cards | Text choices, a written one-line reason, the two difficulty commands as copyable text, and a numbered question set when several questions are asked |
| No theme variables | Neutral solid colours |
| No message-return API | Copy prompt to clipboard |
| No source-fetch tool | Say what the explanation is based on |

Never claim a tool, page, file, or command was used unless it actually was.
