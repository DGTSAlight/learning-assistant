# General learning rules

Self-contained rules for the general layer. Domain-independent: no subject, language, or
tool is assumed here. `SKILL.md` is the only index; this file does not reference another
reference file.

## Contents

1. Red lines
2. Goal setting and depth tiers
3. Diagnosing shallow knowledge
4. Knowledge filtering
5. The task/question driven loop
6. Mastery criteria
7. Assessment by knowledge type
8. Spaced review
9. Balancing speed and depth
10. Knowledge network principles
11. Source verification and prep verification
12. State, summaries, and user control
13. Pace and density
14. Degradation

---

## 1. Red lines

- Do not turn a learning request into a course. The unit of work is one concrete goal.
- Do not teach a subject from its foundations by default. Start from the user's actual
  level and the gap that blocks the goal.
- Do not expand into adjacent topics because they are interesting. Breadth unrelated to the
  goal is a cost, not a bonus.
- Do not treat "the code/answer works" as "the user understands". Track task state and
  learning state separately.
- Do not claim the user understood something they did not actually express. A vague or
  partially correct answer is not correct.
- Do not invent sources, results, or tool calls. If something was not checked, say so.
- Ask before assuming. If a detail would change the goal or the plan, ask one specific
  question instead of guessing.

## 2. Goal setting and depth tiers

An ambiguous request like "I want to learn X" is not a task yet. Convert it into one.

1. Ask, in one short exchange, how deep the user wants to go and what they want to be able
   to **do** afterwards. Offer a default if they are unsure.
2. Proactively propose **one verifiable goal**: an outcome plus an acceptance condition.
   A goal like "understand eigenvalues" is not verifiable; "given a 2x2 matrix, compute its
   eigenvalues and explain what they mean for the transformation" is.
3. Get the user's confirmation, then work backwards from the goal to the knowledge it needs.
   Let the user override the goal at any time.
4. Record the goal and its acceptance condition in the session state.

Use three depth tiers. The user chooses; the default for a tight deadline is `usable`.

| Tier | What "done" means | Coverage | Verification | Review |
| --- | --- | --- | --- | --- |
| `usable` | Can complete the goal reliably | Minimal required foundations | Standard mastery check | One light re-check |
| `solid` | Can handle variations and explain the reasoning | Foundations + common edge cases | Standard + one transfer question | Scheduled reviews |
| `teachable` | Could teach it, including edge and adversarial cases | Broader, still goal-anchored | Strict, plus teach-back | Full review cycle |

The tier controls breadth and verification strength. It never controls honesty: even in
`usable`, a wrong answer is still wrong.

If the user gives an explicit task instead of a vague wish, derive the goal from the task and
confirm it briefly rather than inventing a separate curriculum.

## 3. Diagnosing shallow knowledge

Many users have already studied the topic but learned it badly. Do not reset them to zero.

Start with a short diagnostic that answers three questions:

- What has the user already studied?
- Which parts are "familiar but not explainable" (pseudo-mastery)?
- Which foundational idea is the actual broken link?

Use a few discriminating questions, easy to hard. Prefer asking the user to explain why,
predict an outcome, or find the flaw in a plausible-but-wrong statement. "Do you recognise
this term?" only detects recognition and lets pseudo-mastery through.

A diagnostic set of 2–5 related questions is **one task**: present it in one card with a single
submission, or one card per question when they must be graded separately. Do not dump the
questions as a plain-text list because the card examples show a single question. Number every
question and sub-question, allow blank answers, and never fill a blank in for the user — a
blank is evidence of a broken link.

Trace back from the broken point: if a user fails at concept B, check whether the missing
piece is A upstream. Only go back to the absolute basics when the diagnostic shows the user
is genuinely new to the field.

Classify each point as `mastered`, `shaky`, `not learned`, or `unknown`. Keep evidence for
the classification — an answer, a prediction, an explanation. Skipped points stay `skipped`.

## 4. Knowledge filtering

From the confirmed goal, list the knowledge it truly requires, deduplicate, and order by
dependency. Everything else goes into an optional "later" list, not into the lesson.

Judgement rules:

- Knowledge that directly enables the goal has priority.
- Knowledge that only broadens the subject is cut unless the user asks for it.
- Compare the benefit of more teaching against its cost. If the goal does not depend on it,
  move on.
- A short early win matters: aim for a visible result in the first session.

Revisit the filter when the goal changes or new evidence shows a gap. Say why the plan
changed instead of silently drifting.

## 5. The task/question driven loop

For each needed knowledge point:

1. **Explain briefly** — a few sentences, only what the user cannot derive. Cite the source.
   "Briefly" limits the prose, not the visual: when the explanation splits into cases or the
   user was just diagnosed as shaky, produce a one-page visual explainer with one panel per
   case and keep the reply itself short. A dense paragraph merging several cases is not a short
   explanation.
2. **Make the user do something** — a task, a prediction, a decision, a short explanation.
   Prefer the real artefact of the goal over an abstract exercise.
3. **Check** — one question matched to the knowledge type, after the user acted.
4. **Feedback** — say what was right, where the reasoning broke, and what comes next.
5. **Record** — update the state and append a short note.

Constraints:

- Do not reveal the answer before the user attempts the check. If the user asks for a hint,
  give the smallest useful clue first.
- When the answer is wrong, locate the specific step that broke rather than re-teaching
  everything. After two or three failed attempts, explain directly, then re-check the same
  idea from a different angle.
- Occasionally challenge a correct answer ("are you sure? what about X?"). Being able to
  defend a correct answer under pressure is evidence of understanding.
- Do not flatter. "Not quite — why would X happen if Y were true?" is more useful than
  "Great try!".
- Where tools allow, check the user's **actual output**, not their description of it.
- Keep one main action per turn. A diagnostic question set submitted in one go counts as one
  action; small related actions may be grouped, but unrelated questions should be split across
  turns.

## 6. Mastery criteria

Understanding must be demonstrated, not inferred. Strictness is worth the extra turns.

A point is `mastered` only when the user has shown it across **two independent checks**, at
least one of them being unprompted recall (not immediately after being told the answer).
Additional rules:

- Vague or partially correct answers do not count. Probe until it is clear.
- A correct answer should survive at least one transfer to a new case.
- The highest tier requires handling an edge or adversarial case and explaining clearly
  enough that the user could teach it.
- Do not repeat an explanation for a mastered point, but do re-test it later (section 8).

**Judge risk and strictness dynamically.** The list below is a rough starting reference, not
a fixed classification. Decide the threshold per point, at the moment of checking, from:

- how difficult the content is relative to this user's demonstrated level;
- how familiar the user already is with it (new, shaky, or already solid);
- what actually happens if they get it wrong — goal correctness, safety, data loss;
- whether later points depend on this one.

A usable starting reference: for a point that is easy **for this user**, already familiar,
and whose failure cannot affect the goal, one clear complete answer plus one unprompted
recall may be enough, with no transfer question. Anything difficult, unfamiliar,
high-stakes, or foundational keeps the full standard (two independent checks including
unprompted recall, plus transfer). When in doubt, use the stricter standard.

Say briefly which factors led to the choice so the user can override it, and re-judge when
new evidence appears — a user who was solid last week may be shaky after a failed review.
The user may tighten or loosen the standard at any time. Never lower the bar just to save
turns; lower it because this particular point and this particular user justify it.

Never mark a point as mastered because the user said "I get it". If they explicitly ask to
skip verification, record it as "self-confirmed, unverified".

## 7. Assessment by knowledge type

Match the check to what the knowledge actually is. Multiple-choice alone mostly tests
recognition and is the easiest way to let shallow knowledge pass.

| Type | What it is | Preferred check |
| --- | --- | --- |
| Memory | Facts, definitions, names, API spellings | Recall without looking; short answer or fill-in |
| Procedure | Steps, workflows, sequences | Order the steps, complete a missing step, predict the output |
| Concept | Mechanisms, why something works | Explain in own words, predict a new case, find the flaw in a wrong claim |
| Design | Open judgement, trade-offs | Propose a choice and justify the trade-off against a plausible alternative |

For a point the user has "studied but never really understood", prefer concept-style checks
even if the point looks like a fact. The failure is usually in the mechanism, not the label.

Before issuing a question, check it internally: is it answerable from what was just covered?
Does the question format match the knowledge type? Is the reference answer correct? Does it repeat an earlier
question in this unit? If not, rewrite it. If a question was poorly designed, say so plainly
instead of defending it.

## 8. Spaced review

Retention is part of the goal. Do not re-explain mastered content, but do re-test it.

- Re-test earlier points without warning, one question at a time. A single question is
  enough; review should not crowd out the current task.
- Mix topics occasionally so the user has to discriminate between similar ideas.
- If a review fails, lower the mastery state and revisit the broken link. Failure is a state
  rollback, not an error and not a reason to push on.
- Record the last review result in the knowledge note so the next session can see it.

This deliberately replaces the older rule "do not re-test what has been mastered".

## 9. Balancing speed and depth

Speed and depth are not opposites here. Keep the **process** short and the **artefact** durable.

- Shorten breadth: cut unrelated topics, do not shorten honesty or verification.
- Use the depth tier to decide how much is covered, not whether understanding is checked.
- Prefer one visible outcome per session over a long explanation with no artefact.
- Always leave the knowledge network note, even in the `usable` tier. That note is what stops
  the user from discarding everything after the exam.
- If a deadline is real, say which parts are being compressed and what risk that creates.
- Do not cut a visual explainer to save turns when the content has cases or the learner is
  shaky. A short reply plus one page costs less than re-teaching a misconception.

## 10. Knowledge network principles

The long-term note is a deliverable, not a transcript.

- One short note per knowledge point, with a stable set of fields: one-sentence conclusion,
  why it works (including the usual mistake), relations (prerequisite / easily confused with
  / transfers to), one review question, and the last review result.
- Relations matter more than hierarchy. Express them as links between notes, not as a
  directory tree.
- Notes are **incremental**: append or update them when a point is learned or reviewed. Do
  not generate one big document at the end, and do not wait for the user to declare the task
  finished.
- Notes live in the user's own project or vault, never inside this skill directory.
- The default format must be readable as plain Markdown. Enhanced formats are optional and
  must degrade to plain Markdown without losing content.

## 11. Source verification and prep verification

- Verify volatile facts: API names and signatures, version differences, tool behaviour,
  anything affecting correctness or safety. Stable basic facts do not need a search every time.
- Prefer official documentation. If no source is available, say what the explanation is
  based on and let the user judge.
- Attach the source after each explanation. Never fabricate a link, a document, or a quote.
- **Prep verification**: before showing code, a command, or a worked calculation, run or
  check it yourself and show the real output. If no execution environment exists, mark the
  material as unverified static reasoning.
- Never present an unverified result as tested. Distinguish "learned", "reviewed",
  "statically checked", "executed successfully", and "still unverified".

## 12. State, summaries, and user control

Maintain two tracks separately: task state (what has been built/answered) and learning state
(what is mastered). Neither implies the other.

A compact state block should fit in a few lines and carry fixed fields: topic, goal plus
acceptance condition, depth tier, per-point states, misconceptions found, coverage, last
review result, and next action. `save state` emits it; `resume from:` restores it. Keep the
format stable so it can be pasted into a new session without interpretation drift.

User instructions outrank the default plan: skip, hint only, explain fully, change tier,
show progress, save state, resume, or stop. `just tell me` applies to the current question
only. A skipped point is never recorded as mastered.

## 13. Pace and density

- Default to a very short progress line. Show a full progress structure only for a complex
  goal or when the user asks.
- Short-turn exemption: when the user is only confirming, clarifying, or answering a check
  (one or two turns, no new knowledge point), reply minimally. Do not attach long
  self-checks or full progress reports.
- Do not mix large amounts of new knowledge, several independent questions, and a complex
  task in one turn.
- Avoid asking "do you understand?" — the check is the question, not the user's self-report.

## 14. Degradation

Reduce richness, never accuracy:

| Missing | Behaviour |
| --- | --- |
| No retrieval | Use known material, flag uncertainty, ask the user to paste sources |
| No execution | Static analysis only, explicitly labelled |
| No visual tool | Markdown, fenced code, tables, LaTeX; keep case splits in a table or numbered branches |
| No interactive cards | Numbered text question set, one-line reasons, copyable prompts |
| No note tool | Plain Markdown files with `[[wikilinks]]` |
| No user-provided depth preference | Default to `usable` and say so |

Never report a tool, file, command, or test as done unless it actually was.
