# Code learning rules

Self-contained domain rules, read **only** when the selection table in `SKILL.md` says so.
General rules (goal setting, diagnosis, mastery, review, notes) still apply; this file adds
only what is specific to learning programming. Do not re-state them here.

## Contents

1. Scope
2. Analysing a coding task
3. Splitting into functional blocks
4. Candidate code and answer rules
5. Implementation and review
6. Integration
7. Testing and verification states
8. Delivery
9. Code-specific pitfalls
10. Environment degradation

---

## 1. Scope

Use this file when the user wants to **understand** code while building it: a language, a
library, an algorithm's implementation, or a program they are writing as a learning task.
If the user only wants code produced, this file does not apply.

The learning goal is still a concrete program or behaviour, not "know the language". Breadth
outside what the program needs is cut.

## 2. Analysing a coding task

Before any teaching or implementation, establish:

- Required functions, inputs, outputs, and data formats.
- Explicit constraints, target language and version, and runtime environment.
- Standard library / third-party / service dependencies that may be involved.
- Important boundary conditions, failure cases, and risks.
- Acceptance criteria that tell you the program is done.

Do not require the user to write a formal spec first. Help them clarify as you go. Ask one
key question when missing information would materially change architecture, dependencies,
correctness, or cost; otherwise state a low-risk assumption and proceed.

Form an initial plan internally: modules and their responsibilities, main data and control
flow, relations between functions and modules, key technical choices and alternatives,
knowledge the user will need, and how it will be tested. The plan is revisable, not a
contract. Show only enough of it to orient the user and define the first step.

### Knowledge dependencies

Classify only the knowledge the task actually needs:

- **Basics** — variables, types, expressions, conditionals, loops, functions.
- **Task-specific** — data structures, library calls, file I/O, network, async, language features.
- **Thinking** — decomposition, module responsibility, data flow, error handling, boundaries,
  readability, complexity, maintenance cost.
- **High-risk** — anything that can cause data loss, security problems, resource leaks,
  concurrency bugs, or serious logic errors.

Record knowledge that is not needed yet as optional, not as required curriculum.

### Version and environment

Confirm language version and runtime early. Do not present one version's syntax or one
platform's behaviour as universal. If the version is unknown but does not affect the first
step, proceed and confirm before implementation depends on it.

## 3. Splitting into functional blocks

Divide by responsibility, not by line count. A block should be independently understandable,
with clear inputs and outputs or a clear behaviour:

- reading and validating input
- processing core data
- implementing main business logic
- calling an external API
- saving or producing output
- handling errors and exceptional cases

Do not slice tightly coupled logic into fragments. One block may contain several functions,
or only the key part of one function.

For each block, state as needed: its name and function, its relation to the whole program,
inputs/outputs/dependencies/side effects, key syntax and library calls, design choices and
common traps, and what the user is expected to do this round. Not every block needs every
item.

## 4. Candidate code and answer rules

Comparisons are powerful for learning when the differences are real. Prefer comparing:

- Boundary conditions (`<` vs `<=`).
- Execution order and control flow.
- Return values vs side effects.
- Mutable vs immutable behaviour.
- Choice of data structure.
- Error handling and exception propagation.
- Sync vs async behaviour.
- Resource lifetime.
- Correctness, readability, and complexity trade-offs.

Candidate snippets must be valid syntax for the target language. Distractors should be
plausible mistakes, not word games or deliberately unparseable code. If several answers are
reasonable, state the dimension being compared instead of inventing a single correct one.

Give candidates clear labels and keep labels consistent with the explanation. Do not reveal
the correct option or the full derivation before the user answers. After the answer: judge
it, explain the decisive difference, point out the condition they may have missed, and
decide whether another check is needed. If the user asks for a hint, give it in layers.

Avoid dumping a whole implementation early. Build understanding first, then reveal code in
steps, unless the user explicitly asks for the full code.

## 5. Implementation and review

Prefer the simplest solution that satisfies the requirement and is easy to understand, test,
and maintain. Do not add abstractions, patterns, classes, frameworks, or helpers just to
look professional. Introduce a more complex option only when it brings real value, and
explain its cost.

Keep quality high regardless of who wrote the code: consistent with requirements, clear
module responsibilities, meaningful names, explicit dependencies, consistent interfaces,
reasonable error handling, and complexity proportional to project size.

When reviewing the user's approach, rank findings by severity:

- **Minor** — readability, slight performance, simpler phrasing: present as an option with
  pros and cons.
- **Important** — hard-to-maintain structure, clear bottleneck, fragile error handling:
  explain the consequence and offer an alternative.
- **Severe** — wrong results, data corruption, security holes, resource leaks, reliability
  collapse: warn clearly and prioritise a fix.

Do not present a personal style preference as an absolute error. If several options are
valid, compare correctness, readability, performance, maintenance, and learning cost.

## 6. Integration

Check when combining blocks:

- Function definitions match their call sites; parameters and return values agree.
- Variable scope and data types are sensible.
- Data passed between modules is correct.
- External dependencies are declared.
- File paths, environment variables, and configuration are correct.
- Error handling covers the important failure cases.
- The assembled program still satisfies the original requirement.

Blocks looking reasonable in isolation is not evidence that the whole is correct.

## 7. Testing and verification states

**Prep verification is mandatory here.** Before showing a command, a snippet, or a worked
result, run it yourself and show the real output. If nothing can be executed, mark the
material as unverified static reasoning.

With an execution environment: run the program, test the main path with normal input, probe
boundaries and invalid input, design targeted tests for important logic, and fix what the
results reveal.

Without one: check syntax, structure, interfaces, and obvious logic errors; design test
cases the user can run; state clearly what was only statically analysed; never claim tests
were run.

Keep five states distinct and update them only on evidence:

1. `learned` — the user met the understanding standard for the block.
2. `code confirmed` — the code was reviewed or checked.
3. `integration verified` — combined modules were checked together.
4. `tests passed` — actually executed successfully, with environment and inputs recorded.
5. `unverified` — tests not run, unknown dependencies, unconfirmed behaviour.

Do not inflate limited test results into "the program is correct".

## 8. Delivery

Default to progressing through the learning route, but never use the learning flow to block
access to code. If the user explicitly asks for the full program, provide it immediately.

When delivering early: integrate what exists, mark unfinished or assumed parts, note key
knowledge not yet verified, do not describe unverified code as tested, and do not reset
learning records.

Final delivery contains: the complete program (with file names, entry point, dependencies),
run and configuration notes (install, versions, environment variables, commands), test
results (what ran, what passed, what is still unverified), and a short learning summary
(core syntax/functions/libraries, design choices, important boundaries and traps, what is
mastered vs still shaky). Do not generate a long tutorial unless asked.

## 9. Code-specific pitfalls

- "It compiles / runs" is not "I understand it". Keep the two tracks separate.
- Recognising a correct snippet from four options is weaker evidence than predicting its
  output or explaining why it works.
- Language version differences are a common source of confident but wrong explanations.
- Do not teach a whole standard library because the task uses one function from it.
- Do not skip error handling and boundaries because the happy path works.
- Never present an unrun code block as demonstrated output.

## 10. Environment degradation

- No execution environment: static analysis only, explicitly labelled; supply runnable test
  cases for the user.
- No retrieval: rely on known stable behaviour, flag uncertainty about APIs and versions,
  ask the user to paste the relevant docs.
- No diff/test tooling: describe checks as manual steps and record them as unverified.
- Tool limitations reduce verification strength, never the honesty of the status labels.
