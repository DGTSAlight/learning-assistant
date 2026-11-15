# Technical figures

Self-contained rules for figures in science and engineering explanations. `SKILL.md` is the
only index; this file does not reference another reference file.

## Contents

1. When a real figure is required
2. What a table or a flow box cannot replace
3. How to obtain the figure
4. Drawing requirements
5. Embedding the figure in an HTML explainer page
6. Verify before claiming
7. Degradation
8. Boundaries

---

## 1. When a real figure is required

A figure is **required**, not optional, when the reader must see any of the following. One
signal is enough.

| The reader needs to see | What must be shown |
| --- | --- |
| Shape, slope, zero crossings, discontinuities, phase or period | A plotted waveform or function curve |
| Topology, device labels, current paths, bridge arms | A circuit diagram |
| Nonlinearity, hysteresis, saturation, a conduction boundary | A characteristic curve with the boundary marked |
| Time order of intervals, commutation instants, switching states | A timing diagram; a flow box may accompany it but not replace it |
| Spatial layout, geometry, field lines, coordinate transforms | A geometric drawing |

This applies to power electronics, mathematics, sensors, control, signals, mechanics, and any
subject whose content is inherently graphical. The default page components of a renderer —
tables, flow boxes, callouts — are not a substitute for these.

## 2. What a table or a flow box cannot replace

A table compares **discrete attributes**. A flow box shows **causal or procedural order**.
Neither carries shape, continuity, geometry, or connectivity. A panel that lists "resistive
load: u_d = 0 / inductive load: u_d follows the supply negative" has stated the conclusion but
has not shown the waveform that makes it believable; a chain of boxes reading "supply reverses →
inductor holds the voltage → energy returns" has not shown the negative interval on a time axis.

Keep the table or the flow box as a **companion** when it adds a comparison or a causal reading,
but add the figure. Do not write "see the table above" where a diagram was needed. Do not let the
page renderer's preference for built-in components decide this: the shape of the information
decides it.

The same rule applies to `chart` components. A chart suits discrete numbers compared across
items or over sampled points. A piecewise waveform with a firing angle, a negative interval, a
commutation jump, and labelled instants (`alpha`, `pi`, `pi + alpha`) is not a discrete series;
draw it.

## 3. Choose the route by content type

Pick the route from what the figure is, not from what is easiest to produce.

| Content | First choice | If it is unavailable |
| --- | --- | --- |
| Function plots, waveforms, characteristic curves — anything needing accurate axes, scale, or many computed points | Python + matplotlib | Ask the user: recommend an SVG sketch as the fallback, offer installing matplotlib as the alternative |
| Complex circuit diagrams (many devices, bridge arms, gate drives), classic rectifier / inverter topologies, real device photos | Search for an existing sourced figure | Only when no suitable source is found, draw it and label it as a self-drawn sketch |
| Simple diagrams: a few components, block relations, geometric sketches, timing bars | Hand-written SVG | — |

Why this order: a hand-drawn complex bridge takes a long time, is easy to get wrong at the
device level, and still lacks textbook detail; a sourced figure is faster and more reliable. A
hand-drawn function curve cannot be numerically accurate, so a real plotting library wins there.

### 3.1 Finding a Python that has matplotlib

Do not test only the interpreter bundled with the agent. Check in this order:

1. `python` / `python3` on PATH, and the agent's own interpreter.
2. `conda env list` when `conda` is on PATH.
3. The conda environment registry `~/.conda/environments.txt`
   (`%USERPROFILE%\.conda\environments.txt` on Windows). It lists every environment conda knows
   about **even when the `conda` command is not on PATH** — this is the usual reason a capable
   environment is missed.
4. Common roots: `~/miniconda3/envs/`, `~/anaconda3/envs/`,
   `~/AppData/Local/miniconda3/envs/`, `C:/ProgramData/miniconda3/envs/`, `/opt/conda/envs/`,
   plus project-local `envs/`, `.venv/`, `venv/`.
5. For each candidate run `<python> -c "import matplotlib; print(matplotlib.__version__)"`.
   Use the first one that succeeds and record the interpreter path actually used.

**Ask once, before the first figure of a project.** Probing works, but it costs a turn in every
session, and the user usually already knows the answer. The first time a figure is needed, run
the probe above, then ask one short question: whether to save the interpreter you found as the
default for this project. Name the exact path and version, so the answer is a yes or a no rather
than a research task.

- **Yes** → write one line into the notes-root `INDEX.md` (create the file if it does not exist
  yet): `- 绘图解释器：<absolute path>（<date> 由用户指定）`. Read that line first in later
  sessions and skip the probe. If the path has disappeared, say so and fall back to probing.
- **No** → use the interpreter found for this session and probe again next time. Do not ask
  again in the same session, and never ask when no figure is being drawn.
- Several candidates have matplotlib → list them one per line with their versions and let the
  user choose, instead of picking silently.
- No candidate has matplotlib → the question becomes "do you have an interpreter path I should
  use", followed by the fallback options below.

If none has matplotlib and the user names no path, **ask the user before falling back**. State
which interpreters were checked, and offer two options: draw an SVG sketch instead (recommended
when only the shape matters), or install matplotlib into an existing environment with
`<python> -m pip install matplotlib` and then plot. Never install a package without the user's
agreement, and never claim matplotlib was unavailable without running the checks above.

### 3.2 Searching for a sourced figure

For a complex circuit, search first. Prefer a textbook figure with a named edition, official
course material, a manufacturer application note or datasheet, or a reputable teaching page.
Confirm the topology, device labels, load type, and firing angle actually match the case being
taught. Give the source in the page, respect its licence, and download the image to a local
absolute path before embedding — the page does not load remote images. If no suitable figure is
found, say so, then draw it as a labelled self-drawn sketch that still needs checking against
the textbook.

Never invent a figure, a figure number, or a source.

## 4. Drawing requirements

- Label axes with quantity and unit; label key instants and values (`alpha`, `pi`, `pi + alpha`,
  `U_m`, zero crossings); give a legend when more than one curve is present.
- Mark device labels, current direction, and conducting pairs on circuit diagrams. Check the
  topology against a verified source before drawing it; a plausible-looking but wrong bridge is
  worse than no drawing.
- State the simplifying assumptions next to the figure: ideal switches, no commutation overlap,
  no device drops, continuous current, linear approximation, and so on. Mark the result as an
  **illustrative sketch** when it is derived from general mechanisms rather than copied from a
  source.
- One figure, one focus. Align several waveforms on a shared time axis, or split them into
  panels; do not overlay unrelated quantities.
- Keep the figure readable at page width. Use flat colours and theme-safe contrast; do not rely
  on colour alone to distinguish curves — use dashes or labels too.
- Show subscripts as subscripts. In page text put the symbol inside `$...$`; in SVG labels use
  Unicode subscript characters or a `tspan`. A bare `u_d` reads as an underscore, not a
  subscript.
- Write the generated file to the user's own project or session output directory with a
  topic-based name. Never write session artefacts into this skill directory and never overwrite
  an existing file without asking.

## 5. Embedding the figure in an HTML explainer page

When using the `answer-me-with-html` skill, embed a real local file, not a description of one:

- Its `image` component takes a local absolute path on a line of its own:
  `![what the figure shows](/absolute/path/to/figure.svg)`. It accepts PNG, JPG, GIF, WebP,
  AVIF, and SVG up to 5 MB. Remote images do not load in the page.
- A fenced code block with the `svg` language tag is embedded as-is. Use it when no component
  can express the content — a waveform or a circuit topology is exactly that case. Keep it to
  plain shapes, paths, and text; no scripts, no external references.
- Put the figure in its own panel with a caption that says what to look at. Give that panel a
  `span` equal to the page's column count so the figure gets a full row. A waveform squeezed
  into a one-third column is unreadable and fails the same purpose as having no figure. If the
  labels are still too small, enlarge the SVG text or split the figure into several panels.
- The reply body and the lead still carry the conclusion; the figure is evidence, not a
  replacement for it.
- State the file path in the reply so the user can open the figure directly.
- Do not embed the same figure twice on one page.

## 6. Verify before claiming

1. Run the drawing script. Check its exit status and check that the output file exists and is
   non-empty. A script that was written but not run produced no figure.
2. Inspect the produced image — view it, or parse the SVG and check its structure. Confirm the
   axes, labels, curve segments, and legends are actually present and legible.
3. Check the physics or mathematics of the sketch against the mechanism being taught: sign
   after the zero crossing, continuity of inductor current, which pair conducts in each
   interval, where the formula stops holding.
4. After generating the page, confirm the image really appears in it **and its axis labels are
   legible at page width**. A successful render command alone proves neither. Widen the panel
   or enlarge the SVG text when they are not.
5. Only then say the figure was produced. If any step failed, say so and use the degradation
   below. Never report an unverified sketch as a checked figure.

## 7. Degradation

| Missing | Behaviour |
| --- | --- |
| No matplotlib in any discovered interpreter | **Ask the user first** (section 3.1): recommend an SVG sketch, offer installing matplotlib as an alternative |
| A named interpreter fails | Report the exact error, try the next candidate, then ask |
| No retrieval tool | For a complex circuit, say the search was unavailable and draw a labelled sketch |
| No suitable sourced figure found | Say so, then draw it and label it a self-drawn sketch |
| No script execution | Hand-written SVG fenced block inside the page |
| Page cannot embed images | Produce the file anyway, give its path in the reply, keep a table as a companion, and say explicitly that the figure is not shown in the page |
| No image inspection | Say the figure was not visually checked and mark it unverified |
| No drawing ability at all | Structured text (a table plus a numbered description of the shape) **with an explicit note** that a circuit diagram or waveform is required here |

Reducing richness never means silently substituting a table for a figure. Always name the gap.

## 8. Boundaries

- Do not reproduce textbook figures, invent figure or page numbers, or invent simulation results.
- Do not claim a figure was generated, downloaded, or checked unless it actually was.
- Do not let a decorative diagram crowd out the conclusion, the check, or the task.
- Figures are session artefacts: they live in the user's directory, never in this skill.
