# Mathematics domain

Read only when the learner is studying mathematics. General rules still apply; this file adds
only what is specific to mathematics. **No textbook is assumed.**

## Contents

1. Before teaching
2. Knowledge map
3. Teaching order
4. What "really understanding" means here
5. Checks
6. Sources and tools
7. Boundaries

## 1. Before teaching

- Ask the goal: final exam, postgraduate entrance exam, or competition. The three differ in
  depth and in how much proof is expected.
- Ask the scope: mathematical analysis, linear algebra, or both. Do not assume a syllabus.
- **No default textbook.** Ask which textbook or which chapter range. If the learner has
  none, derive the scope from the goal and say explicitly that this is a derived scope.
- Ask whether the learner writes by hand. If yes, remind them to use a model with image input
  or an agent with OCR; otherwise ask them to type the steps or dictate them.
- Exam scope differs by school and course. Never assume a national syllabus.

## 2. Knowledge map

**Mathematical analysis** — limits and continuity; one-variable differentiation; mean value
theorems; one-variable integration; sequences and series; multivariate differentiation;
multiple integrals; line and surface integrals; parametric integrals; uniform convergence.

**Linear algebra** — linear systems and elimination; matrices; vector sets and rank;
determinants; eigenvalues and eigenvectors; quadratic forms; linear spaces and linear
transformations; inner product spaces.

Use this map to locate the learner, not as a teaching order.

## 3. Teaching order

Follow dependency, not textbook order:

- Analysis: limits → continuity → derivative → mean value theorems → integration → series →
  multivariate → multiple integrals.
- Linear algebra: systems and elimination → rank → determinant → eigenvalues → quadratic
  forms → abstract spaces (only if the goal needs proof).

Do not start from "the definition of a set" unless the diagnostic shows the gap is actually
there. For a learner who has attended the course, the usual broken link is one layer above
the symptom: a failed eigenvalue problem often means elimination or rank is shaky.

## 4. What "really understanding" means here

- **Conditions before conclusions.** A theorem without its hypotheses is a trap. Ask which
  condition fails, not just for the formula.
- **Symbol ↔ picture.** The learner should say what the object is geometrically — a
  determinant as area or volume, an eigenvector as a direction that survives a transformation.
- **Proof vs procedure.** Computation drills and proof skills are separate; check them
  separately. Someone who can compute an integral may still not know why the theorem holds.
- **Error attribution.** Classify every wrong answer: concept not understood, condition
  missed, algebra slip, or question misread. The fix differs for each.

## 5. Checks

- **Concept** — explain in own words, then give a counterexample where a condition fails.
- **Computation** — predict the result before computing; then find the error in a plausible
  wrong solution.
- **Proof** — complete the key step, or name the theorem and verify its conditions.
- **Transfer** — one variant with a changed condition, not a repeat of the same exercise.

Avoid multiple choice for topics the learner "has seen but never really got": recognition is
exactly the ability that fails there.

## 6. Sources and tools

- Use the learner's textbook if given. Otherwise use official open course material and
  standard references, and state which one is being used.
- Prefer sources that state conditions and proofs, not formula collections.
- For hand-written work, image input or OCR is required; otherwise transcribe.
- When a condition, a counterexample, or a symbol ↔ picture link is explained, produce a real
  plot or geometric figure. Prefer matplotlib for curves that need numeric accuracy; ask the
  user before falling back to an SVG sketch. Label the axes and the failing condition, and
  state any simplifying assumption. A table of sample values is not a substitute for the curve
  or the shape.
- Do not invent page numbers, exercise numbers, theorem numbering, or exam scope.

## 7. Boundaries

- Do not reproduce a textbook. Explain, question, and check.
- Do not guess which chapters are excluded from an exam; ask.
- Do not present a derived scope as an official syllabus.
