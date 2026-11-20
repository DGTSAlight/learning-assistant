# Sensors domain

Read only when the learner is studying sensors and measurement. General rules still apply;
this file adds domain scope, order, and checks.

## Contents

1. Before teaching
2. Textbook and scope
3. Knowledge map
4. Teaching order
5. What "really understanding" means here
6. Checks
7. Sources
8. Boundaries

## 1. Before teaching

- Confirm the course scope, and whether lab work is assessed.
- Ask whether the learner also needs the signal-conditioning and microcontroller side, or only
  the sensor principles.
- Confirm the textbook edition; chapter numbering differs between editions.
- Ask whether the learner has syllabus marks on their copy.

## 2. Textbook and scope

Default textbook: 《传感器与检测技术》胡向东 等编著，第 4 版，机械工业出版社，2021.2，
ISBN 978-7-111-67268-5. The textbook is a fallback for chapter names and figure numbering — ask
which edition the learner has before citing anything.

**The scope comes from the learner, not from this file.** Exam scope differs by school, by
teacher, and by year. Ask for it. If the learner has marks on their table of contents (crosses,
question marks, notes such as 掌握 / 概念 / 不考), take those as the working scope, read them back
for confirmation, and only then exclude anything.

### Sample marks (one copy, unverified — offer only on request)

The lists below come from a single copy of the textbook above. They are **not** a syllabus, not
this course's scope, and not evidence about anyone else's course. Do not volunteer them. Mention
them only when the learner asks for a default scope, or has no goal or scope of their own and
needs somewhere to start — and say plainly that they are one copy's marks and need confirming.

Light or excluded on that copy:

- 第 11 章 化学传感器（气体、湿度）
- 第 12 章 生物传感器
- parts of 第 10 章 辐射与波式传感器（微波、超声波）

Marked as key on that copy:

- 第 2 章 基本特性（静态、动态、标定）
- 第 3 章 电阻式，第 4~6 章 电感式 / 电容式 / 压电式
- 第 8 章 热电式（热电偶、热电阻）

## 3. Knowledge map

**上篇 传感器原理**

1. **概述** — definition, composition, classification, development trends.
2. **基本特性** — static: linearity, sensitivity, resolution, threshold, hysteresis,
   repeatability, drift, accuracy; dynamic: transfer function, frequency response;
   calibration and static/dynamic calibration.
3. **电阻式** — strain effect, gauge types, temperature error and compensation, bridge
   circuits, applications.
4. **电感式** — variable-reluctance (self-inductance), differential transformer (mutual),
   eddy-current.
5. **电容式** — variable area / dielectric / gap; measurement circuits (frequency, op-amp,
   transformer bridge, diode twin-T, PWM); applications.
6. **压电式** — piezoelectric effect, materials, equivalent circuit, charge amplifier,
   connections.
7. **磁敏式** — magneto-electric induction, Hall effect and applications.
8. **热电式** — thermocouple (thermoelectric laws, cold-junction compensation, practical
   circuits), RTD (platinum, copper), thermistor (NTC/PTC).
9. **光电式** — photoelectric effect, CCD image sensors, optical fiber, encoders, gratings.
10. **辐射与波式** — infrared, microwave, ultrasonic.
11. **化学** — gas sensors, humidity sensors.
12. **生物** — principles, biochips, applications.

## 4. Teaching order

Basic characteristics → resistive → inductive / capacitive → piezoelectric → thermoelectric →
photoelectric → others.

Every later sensor is an instance of **physical quantity → conversion mechanism → signal
chain**. Chapter 2 supplies the vocabulary (sensitivity, linearity, drift) used everywhere, so
skipping it makes later chapters a list of devices to memorise.

Within a sensor family, teach the signal chain before the catalogue: what changes, what the
circuit measures, then the variants.

## 5. What "really understanding" means here

- **Quantity → mechanism → signal.** For any sensor, trace: what is measured, what physical
  effect converts it, what the circuit outputs.
- **Indicator trade-offs.** Sensitivity vs range, linearity vs simplicity, drift vs cost. A
  sensor is chosen, not memorised.
- **Error sources.** Calibration, temperature drift, nonlinearity, noise, installation.
- **Interface.** Bridge vs charge amplifier vs divider, and why the choice matters for the
  measured quantity.
- **Selection.** Given a scenario, choose and justify, including what would go wrong with the
  alternative.

## 6. Checks

- Scenario → choose a sensor and justify; then ask what fails with the alternative.
- Given a characteristic curve → ask for sensitivity, linearity, range, and the error at a
  point.
- Given a circuit → ask what it measures and why that amplifier or bridge is required.
- Given a measurement error → ask for the most likely source.
- Given a datasheet excerpt → ask whether the sensor fits the stated range and environment.

Avoid pure definition recall for chapters the learner has already seen; go to mechanism and
selection. Multiple choice is acceptable for symbol and term recall.

Show the characteristic curve itself when one is involved: sensitivity as a slope, linearity
error against a fitted line, hysteresis as two branches, drift as a shifted curve, and the
usable range as marked limits. A table of indicators lists the values but does not show these
shapes; prefer matplotlib for characteristic curves, ask the user before falling back to SVG,
and state whether the figure is illustrative or taken from a datasheet.

## 7. Sources

The textbook above; manufacturer datasheets for real devices when available. Do not invent
datasheet values, page numbers, or lab results. If a value is not verified, say so.

## 8. Boundaries

- Do not reproduce the textbook or its figures.
- Do not treat hand marks as an official syllabus.
- Do not claim a lab measurement that was not performed.
