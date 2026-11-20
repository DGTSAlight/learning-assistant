# Power electronics domain

Read only when the learner is studying power electronics. General rules still apply; this file
adds domain scope, order, and checks.

## Contents

1. Before teaching
2. Textbook and scope
3. Knowledge map
4. Teaching order
5. What "really understanding" means here
6. Checks
7. Simulation
8. Sources
9. Boundaries

## 1. Before teaching

- Confirm the course scope and whether **Simulink** is part of the assessment.
- Confirm the textbook edition; chapter and page numbers differ between editions.
- Ask whether the learner has syllabus marks (excluded / maybe / key topics) on their copy.
- Ask whether lab work or hardware experiments are assessed.

## 2. Textbook and scope

Default textbook: 《电力电子技术》刘进军、王兆安 主编，第 6 版，机械工业出版社，2022.6
（2025.1 重印），ISBN 978-7-111-70337-2.

The learner's copy carries hand marks on the table of contents: crosses, question marks,
ticks, and notes such as 掌握 / 概念 / 了解 / 不考 / 没考过. **Treat these as hints, not an
official syllabus** — confirm with the learner before excluding anything.

Frequently marked as excluded or light (verify before relying on it):

- 2.5 其他全控型器件, 2.6 功率集成电路, 2.7 宽禁带器件
- 3.3.3 电容滤波电路的谐波分析, 3.4.2 多重化整流电路, 3.6 相位控制的实现
- 4.4 多重逆变与多电平逆变
- 6.3 交-交变频电路, 6.4 矩阵式变频电路
- 7.4 PWM 整流电路, 第 8 章 软开关技术
- 9.1.4 宽禁带器件驱动, 9.2.3 缓冲电路, 9.3.4 并联使用
- 第 10 章 电力电子技术的应用

Frequently marked as key (verify):

- 3.4 大功率可控整流, 5.1 降压/升压斩波, 5.2.1/5.2.2 正激/反激,
  5.3.1 非隔离双向, 6.1 交流调压, 7.1/7.2 PWM 原理, 9.1 器件驱动, 9.3 串并联使用

## 3. Knowledge map

1. **绪论** — what power electronics is; applications.
2. **电力电子器件** — diode, thyristor, GTO, GCT/IGCT, power MOSFET, IGBT; characteristics,
   parameters, drive requirements.
3. **整流电路** — single/three-phase controlled rectifiers; transformer leakage; harmonics
   and power factor; high-power rectifiers; active inversion.
4. **逆变电路** — commutation; voltage-source; current-source.
5. **直流-直流变流电路** — buck, boost, buck-boost, Cuk; forward, flyback, half-bridge,
   full-bridge, push-pull; bidirectional.
6. **交流-交流变流电路** — AC voltage control, AC choppers, cycloconverters, matrix.
7. **脉宽调制（PWM）** — principles, modulation methods, harmonic analysis, hysteresis control.
8. **软开关技术** — ZVS/ZCS, resonant circuits.
9. **器件的应用技术** — driving, protection, series/parallel use.
10. **应用** — drives, variable-speed systems, UPS, switching supplies, PFC.

## 4. Teaching order

Devices → rectifiers → inverters → DC-DC → AC-AC → PWM → soft switching → applications.

Every later topology reuses device behaviour and the commutation idea. Teaching PWM before the
learner can read a commutation waveform produces memorised formulas with no model behind them.

Within a chapter, go **waveform first**: what the switches do, what the output looks like,
then the formula. Never start with the gain equation.

When an explanation splits into cases — resistive vs inductive load, continuous vs
discontinuous conduction, before vs after a commutation instant, switch on vs off — do not
write it as one linear paragraph. Produce a one-page visual explainer with one panel per case
(a waveform or a comparison table), and keep the reply body to the conclusion. This is the
default for a learner who is shaky on device turn-off or commutation: the distinction between
"the device turns off at the supply zero crossing" and "the next pair commutates the current
away" must be visible, not narrated. The same applies to the continuous/discontinuous boundary
where a gain formula silently stops holding.

**Real figures are mandatory here, not decorative.** For each topology, show the circuit with
device labels and the conducting pair, then show the supply voltage, output voltage, and device
current on a shared time axis with `alpha`, `pi`, and `pi + alpha` marked. **For the circuit
itself, search for a sourced figure first** — a full bridge with gate drives has too many
elements to hand-draw reliably; only draw it when no suitable source is found. **For the
waveforms, prefer matplotlib.** Label the idealising assumptions (no commutation overlap, no
device drops, continuous current) and verify the result before claiming it exists. A comparison
table of resistive vs inductive load may accompany the waveforms but must never replace them;
the same holds for a chain of flow boxes describing the negative-voltage interval.

## 5. What "really understanding" means here

- **Topology ↔ mode.** For a given circuit, name the conducting devices in each interval.
  Reciting the gain formula is not enough.
- **Waveform reasoning.** Predict or sketch the output and device-current waveform before
  calculating. A correct number with a wrong waveform means the model is wrong.
- **Device stress.** Peak voltage and current; what happens at the continuous/discontinuous
  conduction boundary.
- **Selection trade-offs.** Why this topology or device, and what it costs in loss, size, EMI,
  and price.
- **Simulation vs theory.** When the Simulink waveform disagrees, the usual causes are
  parameter values, solver step, missing snubber/parasitic elements, or a wrong gate signal.

## 6. Checks

- Give a waveform → ask which topology and which interval.
- Give a topology → ask for the waveform and the gain.
- Give a design target → ask for device choice and parameter calculation.
- Give a plausible wrong design → ask what breaks.
- Give a conduction-boundary question → ask what happens either side of it.

Use multiple choice only for quick recall of device symbols and parameter names.

## 7. Simulation

Simulink is part of the course. Separate two abilities:

- computing gain and stresses by hand;
- building the model, choosing solver and step, and reading the scope correctly.

Check them separately. A model that "looks right" is not evidence: ask for the specific
waveform and the measured value, and whether the result was actually run.

## 8. Sources

The textbook above; official MATLAB/Simulink documentation for blocks and solver settings.
Manufacturer datasheets when device parameters matter. Do not invent figure numbers, page
numbers, exercise numbers, or simulation results.

## 9. Boundaries

- Do not reproduce the textbook or its figures.
- Do not treat hand marks as an official syllabus; confirm scope first.
- Do not claim a simulation was run unless it was.
