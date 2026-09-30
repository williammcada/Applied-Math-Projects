# Powers of Ten v0.1.0 — Implementation Specification

**Specification revision:** Approved revision 1 · 30 September 2026  
**Status:** Approved for production by William McAda with “Proceed with production” on 30 September 2026. SN-I01–SN-I08 are accepted. See ../decisions/POWERS-OF-TEN-v0.1.0-APPROVAL.md. Approval does not establish application verification.  
**Owner:** William McAda · **Credit:** A WILLIAM MCADA PRODUCT  
**Student title:** Powers of Ten · **Subtitle:** Scale of Reality Lab  
**Canonical repository:** [williammcada/Applied-Math-Projects](https://github.com/williammcada/Applied-Math-Projects)  
**Repository source baseline:** `b1f9ae4158631043314e8a88e5f56549cebd319c` on `main`  
**Initial source:** Applied Mathematics Project Series Dossier v1.0.0, 15 September 2026; Powers of Ten is a planning subproject at the consulted baseline.  
**Target versions:** application `0.1.0`; content `1.0.0`; save schema `1.0.0`  
**Project ID / scenario ID:** `powers-of-ten` / `SN-BASE`  
**Proposed repository destination:** `docs/change-specs/POWERS-OF-TEN-v0.1.0.md`  
**Implementation intake:** Current repository baseline refreshed to `d728dff8f8553f7db5cd26304d9bc403ad790ad9`. This approved specification is recorded before implementation; section 14 retains the historical preparation record. No handbook rule is changed.

## 1. Purpose, source authority, and scope

Create a complete, independent classroom application in which pairs repair the quantitative evidence for a science museum exhibit, **Too Small, Too Far**. Students work with microscopic and astronomical quantities, perform all four operations in scientific notation in both ranges, plan and construct a physical model, record measurements, and explain the model's limits.

The central question is: **How can a model represent something too small or too large to experience directly, and what does it leave out?**

The source of requirements is the [preserved dossier at the consulted commit](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md), sections 01–12, 33–38, and 39–42. The [family PROJECT-BRIEF](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/PROJECT-BRIEF.md), [Powers of Ten README](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/powers-of-ten/README.md), source provenance, original reference fixtures, and Food Truck v0.1.0 specification were also read. Food Truck supplies a specification/process precedent only; its business mathematics and local rules do not apply here.

The family brief contains older Food Truck status text, while the consulted commit and Food Truck specification record its approval. That discrepancy does not change Powers of Ten's source requirements. This task prepares Powers of Ten documentation; it does not reorder or interrupt other builds. The dossier expressly permits Powers of Ten to move earlier for the cross-curricular calendar.

### Audience and delivery

- Advanced Grade 5 Introduction to Pre-Algebra / Saxon 8/7; ELL-friendly English.
- Default: two students sharing one iPad, with complete desktop keyboard/mouse support. Use aliases and alternate Planner/Checker, then Builder/Verifier roles.
- Two proposed 45-minute lessons **after** scientific notation and integer exponent operations have been taught. Add a bridge lesson or third session if needed; retain every operation, both magnitude ranges, and the physical build.
- One self-contained HTML application with embedded pictures, inline styles/scripts, system fonts, and a byte-identical deployable `index.html`.
- Intended host: the existing repository's GitHub Pages site, at `/Applied-Math-Projects/powers-of-ten/`. This is a planned path, not a claim that a Powers of Ten application is live.
- Downloaded desktop HTML must run offline. iPad use is primarily through the hosted page. Hosted reopening without a network connection is not promised.
- Outputs: portable progress JSON; student report; build/calculation sheets and templates; source-labeled exhibit placard; visitor passport; individual transfer slips; teacher reference.

No generator, suite dashboard, backend, student account, live AI generation, multiplayer, telemetry, automatic submission, music, audio files, countdown, leaderboard, or speed score. No microscope, live specimen, biological sample, or laboratory experiment is required. Do not add formal logarithms, significant-figure grading, cell-organelles recall, artistic grading, or a complete solar-system simulation.

### Handbook baseline

Consulted [McAda Project Handbook v0.1.1](https://github.com/williammcada/mcada-project-handbook/tree/00cbde605ab08203b6b5fd2374d225155608fc29), commit `00cbde605ab08203b6b5fd2374d225155608fc29`:

| File | Consulted file blob SHA |
| --- | --- |
| `AI-START-HERE.md` | `6557a45aaa6d29d7d1abde808e6d0ac248b08820` |
| `UNIVERSAL-RULES.md` | `61edfde857762153535b21a0a63d9b912c0027f7` |
| `CONDITIONAL-STANDARDS.md` | `dad2d3a05ca0f18260196ea51ac6351bffffdc1c` |
| `RELEASE-CHECKLIST.md` | `301cb6fc784338a1449301b04c198c1a9fb1ea66` |

Use U-01–U-08 as the family-selected project guidance; apply approved U-09 to saved work. Select S-02 (curriculum/evidence), S-04 (distribution/classroom operation), and S-05 (Applied Mathematics). Their seeded/draft/approved handbook statuses remain unchanged. S-01 is inapplicable: importing a student's progress is not importing externally generated AI content. No AAC quotas, benchmark formats, or game rules are imported. No handbook amendment is proposed.

## 2. Approved implementation decisions

The source objectives, eight operation expressions, teaching constants, track scales, and physical tolerances are retained. The following details resolve gaps for implementation; they are approved for this initial implementation by the owner’s production instruction. They were first proposed in Draft 1.

| ID | Approved decision | Reason |
| --- | --- | --- |
| SN-I01 | Use one fixed core investigation and the exact C01–C03/C12 tasks below; no random task generator or editable science constants in v0.1.0. | Gives the first release a reproducible answer contract and bounded workload. |
| SN-I02 | Require the same C01–C07 evidence for both tracks. Preserve inactive track drafts when switching; only the selected track supplies the current exhibit. | Changing the physical choice must not erase learning evidence or avoid a numerical range. |
| SN-I03 | Allow a basic coefficient calculator for C04–C10. Students still enter exponent work, common units, normalization, and scale direction. C01–C03 and independent exit work do not include an in-app calculator. | Makes calculator support field-specific; no claim that external calculators can be prevented. |
| SN-I04 | Judge Moon construction against the disclosed 5.5 mm target, while retaining 5.46875 mm as the exact calculated diameter. Tolerance endpoints are inclusive. | Separates mathematical precision from classroom construction precision. |
| SN-I05 | Featured exhibit requires current recorded physical inspection and accepted interpretation/transfer review where those responses are teacher-reviewed. Pending review produces Exhibit ready for review. | Resolves the dossier's overlap between “all evidence current” and “review pending”; prose is never auto-approved. |
| SN-I06 | Provide three joined 200 mm distance-template segments for the 600 mm Earth–Moon separation, plus ruler-built instructions. Never fit the complete distance to one page. | Makes the physical output possible on A4 and Letter without changing scale. |
| SN-I07 | One saved session is the whole work group: both track drafts, attempts, build records, reviews, transfers, and report state. No class/year administration. | Implements U-09 without adding unrelated management. |
| SN-I08 | Keep museum completion and review separate from independent mastery. Digital transfers may be corrected, but retain first responses; paper/oral transfers require an actual recorded submission and review. | Prevents corrected pair work or self-reported physical work from becoming a mastery claim. |

## 3. Fixed reference data and scientific meaning

Use the supplied rounded teaching values consistently. Arithmetic on those values is exact unless the field states rounding. Extra digits in a calculation do not increase the accuracy of the original scientific data. Sources [R1–R6] are listed in section 15; these values are inherited from the dossier, not new observations.

| Data ID | Object / property | Teaching value | Source and qualification |
| --- | --- | --- | --- |
| SN-D01 | DNA helix width | `2 × 10^-9 m` | R1; approximate molecular width |
| SN-D02 | Human red blood cell exemplar diameter | `8 × 10^-6 m` | R2; chosen exemplar within the source's approximately 7–8 µm range |
| SN-D03 | Earth equatorial diameter | `1.28 × 10^7 m` | R3; rounded teaching value |
| SN-D04 | Moon diameter | `3.5 × 10^6 m` | R4; deliberately rounded |
| SN-D05 | Mean Earth–Moon center-to-center distance | `3.84 × 10^8 m` | R3/R4; not surface-to-surface separation |
| SN-D06 | Sun diameter | `1.4 × 10^9 m` | R5; approximate |
| SN-D07 | Mean Earth–Sun distance | `1.5 × 10^11 m` | R3; mean distance, not a fixed instantaneous separation |
| SN-D08 | Light speed in the calculation model | `3 × 10^8 m/s` | R6; rounded from the exact SI vacuum value, 299,792,458 m/s |
| SN-D09 | Hypothetical person height | `1.7 m` | Authored comparison; not a biological constant |
| SN-D10 | Display length / smallest visible item | `3 m` / `2 mm` | Authored museum constraints |

Microchannels, specimen layers, viewing widths, and probe path segments below are authored science-context examples. Display that status. A row of diameters is a one-dimensional model; it does not count cells packed into an area. Adding two logged path lengths does not establish a current distance between planets.

Each data record contains `id`, object, property, value, unit, source ID, approximation status, and explanation. Each image separately records whether it is an observation, explanatory diagram, or decorative illustration. Do not derive real size from arbitrary image pixels or resized magnification labels.

The magnitude explorer shows **lengths in meters** only: do not put light speed on the same length axis. Equal decade spacing represents multiplication by ten, not equal physical distance. Use positions `n + log10(a)` for positive `a × 10^n` if plotting within decades; logarithms are an implementation detail, not a student requirement. Provide a selectable list/table alternative and label icons as not drawn at a common physical scale.

## 4. Objectives and checkpoint contracts

Keep source objective IDs `SN-01`–`SN-12` and checkpoint IDs `C01`–`C12`. Persist fully qualified field IDs such as `SN-C04a.coefficientWork`. Each instantiated field record must include prompt, data/source IDs, value range, mathematical action, dimensions, representation, allowed answer form, evaluator, unit/precision rule, prerequisites, help, error messages, and evidence/review status. The tables below define that content; implementation must not replace them with generic “correct answer” checks.

All numerical answers in sections 4–7 are **teacher/specification values**. Student screens show the givens and requested work, not the current answer. Reveal accepted results after checking. Source cards used for a conversion must not simultaneously display that conversion's answer.

### C01–C03: notation, magnitude, and units

| Checkpoint / objective | Required student response | Evaluator and evidence |
| --- | --- | --- |
| C01 / SN-01 | Four conversions: `0.000008 m → 8 × 10^-6 m`; `12,800,000 m → 1.28 × 10^7 m`; `2 × 10^-9 m → 0.000000002 m`; `3.84 × 10^8 m → 384,000,000 m`. | First two require normalized coefficient/exponent fields; last two require ordinary decimal notation. Exact equality plus requested representation. Capture each first and final response. |
| C02 / SN-02 | Order DNA width `2 × 10^-9 m`, an authored specimen depth `6 × 10^-6 m`, and cell diameter `8 × 10^-6 m`, smallest first. Then give ten times the cell diameter: `8 × 10^-5 m`, and identify that it is one decade larger. | Exact order and factor. Same-exponent cards require coefficient comparison. Use tap/keyboard reorder controls as well as optional drag. |
| C03 / SN-03 | Two linked cases: (a) convert `8 µm` into meters, millimeters, and nanometers: `0.000008 m`, `0.008 mm`, `8000 nm`; (b) convert `1.28 × 10^9 cm` into meters: `1.28 × 10^7 m`. | Exact dimension-aware conversion; decimal or equivalent scientific notation permitted. Supply conversion references: `1 m = 100 cm = 1000 mm = 10^6 µm = 10^9 nm`. Unit recall is not an additional test. |

Numerical entries are positive for these tasks; exponent fields permit signed integers. C01–C03 are independent of build choice. Help explains coefficient, exponent, decade, and quantity preservation with different numbers. Reject misplaced decimal points, unsupported units, incomplete orders, and equivalent values in the wrong requested representation with distinct messages.

### C04–C07: eight mandatory scientific calculations

| Field / objective | Required context and operation | Exact final result |
| --- | --- | --- |
| C04a / SN-04 | Ideal end-to-end row of 25 cell diameters: `(8 × 10^-6 m)(2.5 × 10^1)` | `2 × 10^-4 m` |
| C04b / SN-04 | Light travels for 1.28 seconds in the model: `(3 × 10^8 m/s)(1.28 s)` | `3.84 × 10^8 m` |
| C05a / SN-05 | Viewing width divided by one cell diameter: `(6.4 × 10^-5 m)/(8 × 10^-6 m)` | `8` diameter-widths, dimensionless; `8 × 10^0` also accepted |
| C05b / SN-05 | Approximate sunlight travel time: `(1.5 × 10^11 m)/(3 × 10^8 m/s)` | `5 × 10^2 s` |
| C06a / SN-06 | Two straight microchannel segments: `2.4 × 10^-5 m + 7.5 × 10^-6 m` | `3.15 × 10^-5 m` |
| C06b / SN-06 | Sequential logged probe paths: `3.84 × 10^8 m + 6 × 10^7 m` | `4.44 × 10^8 m` |
| C07a / SN-07 | Uncoated depth: `8 × 10^-6 m − 2 × 10^-6 m` | `6 × 10^-6 m` |
| C07b / SN-07 | Difference between supplied Sun and Earth diameters | `1.3872 × 10^9 m` |

Multiplication/division require coefficient work, exponent addition/subtraction, final normalized value, and unit choice. Treat `1.28` as `1.28 × 10^0`. For C05a, the raw coefficient is `0.8`, exponent difference is `1`, and normalized result is `8 × 10^0`; a correct final answer does not excuse wrong intermediate work.

Addition/subtraction require a chosen common exponent and the two correctly rewritten coefficients before combining. Accept any supported common exponent that exactly represents both inputs; do not force one teacher method. Final results must be normalized, except C05a's explicitly allowed ordinary integer. Retain the setup in the report. Give separate feedback for wrong coefficient operation, wrong exponent operation, mismatched powers, failed normalization, and wrong dimension. Do not use a broad numerical tolerance.

### C08–C12: model, evidence, and transfer

| Checkpoint / objective | Required response | Evaluation / review |
| --- | --- | --- |
| C08 / SN-08 | Choose a build track; convert model and actual lengths to common units; calculate `k = model/actual`; enter model:actual ratio and enlargement/reduction. Earth–Moon teams also calculate Moon diameter and separation. | Exact arithmetic and ratio direction, using section 6. Scale is dimensionless. Retain intended dimensions separately from later measurements. |
| C09 / SN-09 | Record real model measurements, units, tool/resolution, and calculated deviations; submit for teacher/peer inspection. | Format and deviation arithmetic checked automatically. Physical truth remains self-reported until an inspection is recorded. An accurate out-of-tolerance measurement is valid reporting, with a repair outcome. |
| C10 / SN-10 | Calculate one selected limitation for the chosen track; compare Earth's diameter with the cell's diameter and the permitted museum display ratio. | Exact numerical evidence from section 6; select that one linear scale is mathematically possible but impractical under the supplied limits. A short explanation is reviewed, not keyword-scored. |
| C11 / SN-11 | Match DNA→width, cell/Earth/Moon/Sun→diameter, Earth–Moon/Earth–Sun→distance, light→speed. Distinguish explanatory diagrams from observations. Submit a source-linked placard statement and inspect the other track or teacher example. | Objective matching is checked; source IDs/property/unit/scale-label consistency is checked; interpretation is teacher-reviewed. Visitor record names the other model, its scale direction, and one feature it preserves or omits. |
| C12 / SN-12 | Each student independently completes a fresh numerical task and scale-label interpretation using the two variants below. | Digital exact checking with preserved first response, or paper/oral submission with teacher review. Two separate aliases/evidence records; shared completion cannot fill both. |

**Transfer A:** an authored microscopic strip is `6 × 10^-6 m` long. Five strips end to end measure `3 × 10^-5 m = 0.00003 m`. Interpret `model:actual = 5000:1`: an enlargement; 1 mm actual becomes 5000 mm in the model.

**Transfer B:** an authored probe travels at `2 × 10^7 m/s` for 30 s. Distance is `6 × 10^8 m = 600,000,000 m`. Interpret `model:actual = 1:5000`: a reduction; 1 mm in the model represents 5000 mm actual.

These are authored transfer contexts, not scientific measurements. Each learner gives the normalized result, corresponding ordinary decimal, and one scale interpretation. Present a separate learner view/slip without the partner's answers or worked help; disclose that the application cannot certify unaided work.

## 5. Student journey and classroom rhythm

| Stage | Purpose and controls | Exit / lesson timing |
| --- | --- | --- |
| SN-S01 — Museum commission | Illustrated tiny/huge introduction, team/student aliases, role assignment, brief central question. | Save session; Day 1, 0–5 min. |
| SN-S02 — Notation lab | C01–C03, magnitude map, conversion references and help. | Required checks current; 5–13 min. |
| SN-S03 — Scientific calculations | C04–C07 in four operation pairs; visible micro/macro completion. | All eight checked; 13–35 min. |
| SN-S04 — Exhibit planning | Choose track, complete C08, preview material needs and print build plan. | Export progress; assign Builder/Verifier; 35–45 min. |
| SN-S05 — Construction bench | Resume plan; inspect scale direction; show step-by-step physical construction and optional calibrated templates. | Confirm model built before measurement; Day 2, 0–25 min. |
| SN-S06 — Verification desk | C09 measurements, deviations, tolerance comparison, repair, inspection request/record. | Valid measurement record; inspection can remain pending; 25–33 min. |
| SN-S07 — Mini gallery | C10–C12, other-track visitor passport, short interpretation and independent transfers. | Submit evidence; pending reviews remain visible; 33–42 min. |
| SN-S08 — Publish exhibit | Placard, personalized museum verdict, printable report and export. | 42–45 min; return to any affected work for revision. |

The timing is a trial target, not a verified classroom result. Long stages may scroll normally; avoid nested scrolling and tiny card grids. A persistent header shows project/version, progress, active track, and save status. Use Back, Save, Help, and Check & Continue. Locked future stages explain the prerequisite. Draft printing and export remain available when work is incomplete.

Each substantive field/group has keyboard/touch `?` help: meaning, unit/format, action, and a worked example using different numbers. Close, Escape, and outside tap dismiss it. Typical task prompts use one action per sentence and remain under about 45 words excluding data. Glossary terms include coefficient, exponent, diameter, center-to-center, enlargement, reduction, scale factor, tolerance, and observation. Do not penalize help, revision count, spelling, or grammar.

## 6. Physical models and measurement rules

Both tracks require all eight operations. Both culminate in a physical object, calculation/build sheet, source-labeled placard, measurement record, and visitor passport. Materials: ruler, paper/card, pencil, eraser, markers, child-appropriate scissors, and tape; cosmic teams also need a 60 cm string or joined paper strip. Prepare an example of each track. No photo upload or automatic image inspection is needed.

### Track A — Microscopic Enlargement

| Quantity | Exact result / construction requirement |
| --- | --- |
| Actual cell diameter | `8 × 10^-6 m` |
| Model diameter | `16 cm = 0.16 m = 160 mm` |
| Scale factor | `0.16/(8 × 10^-6) = 20,000` |
| Required label | `model:actual = 20,000:1 — enlargement` |
| Physical diameter tolerance | `160 ± 2 mm`; acceptable interval `[158,162] mm` |
| Hypothetical 1.7 m person at this scale | `34,000 m = 34 km` |
| 2 nm DNA width at this scale | `0.04 mm`, below the supplied 2 mm visibility threshold |

Represent a biconcave disc with a shallow central depression, not a hole or a cell nucleus. Diameter is the assessed scale claim; optional thickness is illustrative unless separately specified. Select and calculate at least one limitation: the person is too large, or the DNA detail too small. Record the numerical result and an appropriate constraint comparison.

### Track B — Earth–Moon Desktop Model

| Quantity | Exact result / construction requirement |
| --- | --- |
| Model Earth diameter | `20 mm = 0.02 m` |
| Scale factor | `0.02/(1.28 × 10^7) = 1/640,000,000 = 1.5625 × 10^-9` |
| Required label | `model:actual = 1:640,000,000 — reduction` |
| Moon diameter, calculated | `5.46875 mm` |
| Moon construction target | `5.5 mm`, rounded once to nearest 0.1 mm |
| Earth–Moon center-to-center distance | `600 mm` |
| Earth tolerance | `20 ± 1 mm`; interval `[19,21] mm` |
| Moon tolerance | `5.5 ± 1 mm`; interval `[4.5,6.5] mm` |
| Separation tolerance | `600 ± 5 mm`; interval `[595,605] mm` |
| Sun diameter at this scale | `2.1875 m` |
| Earth–Sun distance at this scale | `234.375 m` |

Students calculate both exact Moon diameter and construction target. Keep them distinctly labeled in print and save data. Never round the exact diameter before calculating a different quantity. Select at least one cosmic limitation: the Sun's diameter or Earth–Sun distance exceeds the 0.6 m desktop model span.

Mark and measure circle centers. The 600 mm string/strip measures center-to-center distance; circle edges may extend beyond its endpoints. Do not substitute edge-to-edge distance. An enlarged Moon symbol may supplement the model only if labeled “symbol—not to size scale”; it cannot replace the required scaled Moon.

### Common-scale limitation

The largest-to-smallest display ratio is `3 m / 0.002 m = 1500`. The actual Earth/cell diameter ratio is `(1.28 × 10^7)/(8 × 10^-6) = 1.6 × 10^12`. Both tracks calculate these values and identify the practical conflict. A single linear scale exists mathematically; it cannot keep both items within the supplied 3 m / 2 mm limits. Do not teach that one scale is inherently impossible.

### Measurement, repair, and inspection

Use `deviation = measured − target` and `withinTolerance = abs(deviation) ≤ tolerance` after exact unit conversion. Lengths must be finite, positive, and within a disclosed generous entry limit of 10,000 mm; decimals are allowed. Wrong format/unit/arithmetic blocks that checkpoint. A physically poor result with correct calculation proceeds to analysis and Calibration required.

No measurement field is prefilled with the target or an invented “actual.” Require the learner's measurement, unit, tool, and declared resolution. Students may report half-millimeter estimates; do not label them more precise than their tool. Construction tolerances describe classroom acceptance, not scientific uncertainty.

Inspection records include reviewer alias, teacher/peer role, track/build revision, dimensions actually inspected, recorded measurements/units, timestamp, and status `pending`, `accepted`, or `repair-needed`. Retain disagreements with the team's report visibly. A reviewer can correct a measurement with a recorded reason; never silently replace it. A later build/measurement edit makes the related inspection stale. Software checks a record's consistency, not whether the physical inspection truly happened.

## 7. Exact input and validation behavior

Use exact decimal/rational arithmetic, including powers of ten; do not evaluate student text as code. Keep raw text and parsed value separately. Canonical numeric storage uses bounded decimal strings or numerator/denominator strings, not floating-point approximations or JSON nonfinite values.

| Field type | Acceptance contract |
| --- | --- |
| Ordinary decimal | Valid optional sign, decimal point, and correctly grouped thousands separators. No exponent notation when ordinary notation is the requested representation. |
| Scientific notation | Separate coefficient and integer exponent, rendered preview. Up to 12 significant coefficient digits; entered exponent −24 through 24. Requested nonzero normalized output requires `1 ≤ abs(a) < 10`. |
| Equivalent numeric value | Allow decimal or normalized scientific form when the field explicitly permits either. Fractions permitted for scale factors; ratio fields use two positive numbers in the stated direction. |
| Model:actual ratio | Exact cross-product equivalence with the expected ratio. Require common units and explicit enlargement/reduction; equivalent ratios may be accepted then displayed in the canonical form. |
| Measurement | Numeric value plus explicit metric unit; exact conversion before deviation/tolerance checks. Physical tolerance never becomes academic-answer tolerance. |

Normalize surrounding spaces and Unicode minus; accept `µm`, `μm`, and `um` as micrometers. Provide an on-screen minus control where the tablet keyboard omits it. Reject comma decimals such as `1,28`, malformed grouping, blank values, division by zero, unsupported units, and overlong input with actionable messages. Bound raw numeric fields to 100 characters. Supporting zero uses its own canonical form; zero must never pass a nonzero microscopic answer.

Distinguish numerical correctness from representation correctness: `31.5 × 10^-6` equals `3.15 × 10^-5`, but requires normalization at C06a. `8` and `8 × 10^0` both pass C05a. `500` is numerically correct for C05b but requires the requested normalized form. Do not score hidden significant-figure conventions. Positive midpoint rounding uses half-up only in explicitly rounded construction fields.

Validate on deliberate Check or blur, not each partial keystroke. A failed Continue moves focus to a linked error summary, keeps valid siblings, and leaves Back/Save/Help available. Required calculations must be current before downstream approval; legitimate repair and pending-review outcomes remain reachable.

## 8. State, dependencies, and evidence

Separate four kinds of state: academic check status; physical fit; human review; museum outcome. A single `complete=true` flag cannot represent them faithfully.

Each checkpoint stores current response/status, dependency fingerprint, first checked response, attempts, support used, teacher override, and evidence references. Attempts retain input context, scenario/content revision, result, and timestamp. Historical responses are never regraded against a new context.

| Changed input | Must become Needs recheck / stale | Must remain preserved |
| --- | --- | --- |
| A C01–C07 response | Its affected checkpoint and overall academic completion/ending | Other independent tasks and existing build work |
| Active track | Selected-track C08–C11 readiness, placard, build/review association, report outcome | C01–C07, both learners' transfers, inactive track history |
| C08 scale/plan response | Dependent target/label confirmation, build readiness, limitation work and relevant review | All entered measurements and previous attempts, clearly contextualized |
| Recorded physical measurement or declared rebuild | Deviations/fit, physical inspection, outcome | Fixed planned scale and unrelated academic work |
| Limitation, interpretation, source or placard edit | Related review and published report state | Correct independent operations and unrelated inspection |
| Student transfer edit | That student's transfer/review and completion | Partner's evidence |

Upstream edits must identify why rechecking is needed. Retain old entries; do not erase or quietly certify them. Returning to an unchanged inactive track may restore evidence only when its fingerprint still matches; ask whether the physical object was rebuilt or changed.

Teacher Mode exposes answers, review, diagnostics, and logged bypass with reason, reviewer alias, field, time, and revision. Bypass never becomes verified mathematics; it produces Provisional status. A later genuine successful check may clear the active bypass while retaining history. Any PIN is only a classroom deterrent; client-side answers and records are not secure assessment evidence.

## 9. Save, import, and deletion

Namespaced keys: `mcada:powers-of-ten:session:<id>` and `mcada:powers-of-ten:index`. Never use `localStorage.clear()` or another project's namespace. Keep edits in memory immediately, autosave confirmed edits/transitions, and show “Saved on this device” only after a successful write. Probe storage safely. Storage denial, quota, corruption, or `file:` limitations produce an in-memory fallback with a persistent Export progress reminder.

Visible controls: New session; Resume; Duplicate for revision; Export progress; Import progress; Export all as backup; Delete session; Clear all Powers of Ten sessions. New/duplicate work receives a new ID. Detect newer tab revisions and offer Reload or Save as copy rather than silent merging.

Use the dossier's `mcada-project-progress` envelope with schemaVersion, projectId, appVersion, contentVersion, sessionId, scenarioId, teamAlias, currentStage, inputs, attempts, checkpoints, teacherOverrides, and completedAt. Add student aliases, role assignments, local revision, active track, per-track plans/build revisions/measurements/inspections, limitations, placard, visitor record, independent transfers, reviews, and imported provenance. Give all fields a defined schema; do not infer completion from imported flags.

Draft bounds: 5 MiB per session import; 25 MiB per backup; at most 25 sessions in one backup; alias/title ≤64 characters; interpretation ≤600; review/override note ≤400; ≤10,000 attempts and ≤100 build revisions per session. At a limit, preserve evidence and offer export/new session; do not silently discard first attempts. The backup envelope is separately identified as `mcada-project-progress-bundle`, with version, projectId, exportedAt, and sessions.

Import into temporary state, validate the complete file, then preview aliases, versions, stages, and ID collisions. Validate allowed keys/types, lengths, numeric bounds, known source/field/track IDs, dependency references, and supported schema/content. Reject malformed, wrong-project, future-schema, unsupported-content, or inconsistent state with current work untouched. Imported strings are inert text. Recompute mathematics and current dependencies; preserve reported history and reviews as imported records, not newly witnessed evidence.

Default import is as new copies. Replacing an existing session requires named confirmation and a backup option. Implement transactional writes/rollback so an index failure cannot partially overwrite working records. Compatible older saves require explicit migration with raw backup; matching app versions alone is neither sufficient nor necessary for compatibility.

**U-09:** Delete session removes that complete session and associated track drafts, attempts, reviews, transfers, and report state. Clear all affects only Powers of Ten sessions in this browser's applicable storage scope. Confirm scope and record count, explain permanence, provide Cancel and Export backup, and require explicit confirmation. Downloaded files, source content, and other apps remain untouched. No class/year grouping is introduced. Report partial failures truthfully; verify cancellation, reload, backup recovery, empty state, and creation of fresh work.

## 10. Museum outcomes and reporting

Apply precedence in this order. Keep a separate visible list of repairs/reviews even when an earlier status controls the main heading.

| Priority | Outcome | Predicate / behavior |
| --- | --- | --- |
| 1 | **Draft — finish checks** | Required academic fields are missing, incorrect, or stale; model measurements are absent; interpretation/limitation/visitor submission or either transfer submission is absent. Missing labels alone use Calibration required once other work is submitted. |
| 2 | **Provisional — teacher review** | An active bypass supplied required academic completion. Never award ordinary Featured status from bypass. |
| 3 | **Calibration required** | Valid analyzed measurements are outside tolerance; inspection records a build mismatch; source/scale/property labels are missing or inconsistent; or interpretation/review identifies a substantive repair. State the exact issue. |
| 4 | **Exhibit ready for review** | Required work and labels are submitted/current and measured fit passes, but physical inspection, interpretation, or paper/oral transfer review is pending/stale. Not scientific approval. |
| 5 | **Featured exhibit** | All academic checks current, both transfers complete under their response mode, measurements within tolerance, current inspection accepted, labels correct, numerical limitation documented, and required human reviews accepted. |

Completed-but-imperfect work may receive Calibration required and a final report; it is not a false arithmetic failure. Student prose is only marked submitted until reviewed. No keyword detector, hidden quality score, speed reward, or artistic ranking. Optional teacher-applied 20-point rubric from the dossier: mathematics 8, representations 4, evidence-based interpretation 4, usable documentation 4; disabled by default and never presented as individual mastery.

Each ending references actual saved choices and numbers. For example, a cell team's ending can identify its measured diameter, 20,000:1 enlargement, and selected numerical limitation. A pending inspection remains explicit. Do not print an ideal target as though it were a measured result.

### Printable artifacts

| Output | Required content / layout |
| --- | --- |
| Student report | Target four A4/Letter portrait pages: (1) notation/unit/magnitude evidence; (2) all eight operations and work; (3) selected scale plan and measured-versus-target table with review; (4) limitation, source-supported interpretation, visitor/transfer responses, ending, and first-versus-final/support summary. Permit clearly labeled continuation pages for bounded long responses; never shrink text to force a count. |
| Build/calculation sheet | Track, givens, checked scale/targets, construction steps, tolerances, blank real-measurement fields, and inspection space. A Day 1 output must not imply a model has already been measured. |
| Dimensional templates | 160 mm cell guide, or 20 mm Earth / 5.5 mm Moon guides and three 200 mm distance segments. Measured construction is still required. |
| Exhibit placard | One readable display card: object/property, supplied actual size, intended ratio/direction, measured model size, source credit, numerical limitation, and outcome/review status. |
| Visitor passport and transfer slips | Compact other-track prompts and two separate answer-free transfer variants. |
| Teacher reference | All answer forms, intermediate work, model calculations, tolerances, common misconceptions, review criteria, source notes, and ending predicates. |

Use native selectable text and code-rendered mathematics/SVG; exponents must be superscripted and fractions stacked where helpful. No screenshot-based math. Native Word Equation Editor is not a requirement for an HTML/print product; this release does not promise DOCX export.

All prints include title, credit, app/content versions, alias, date, page labels, and Draft/Provisional/pending status where relevant. Select exactly one print view so teacher answers cannot leak into student pages. Test A4 and Letter at 100%, grayscale, long text, negative exponents, source labels, page breaks, and browser-header/footer settings.

**Template calibration:** every dimensionally significant page has a 50 mm calibration line and “Print at 100%, not Fit to page.” Proposed teacher check: line within 0.5 mm of 50 mm. If calibration fails, reprint correctly or construct by ruler; never certify the print scale automatically. On-screen diagrams are responsive previews, not physical rulers.

The 600 mm distance uses three 200 mm measured segments with separate 10 mm joining tabs that do not contribute to length. Number segments and mark joins/centers. Fit each segment on A4/Letter without rescaling. Verify the assembled 600 mm with a ruler; paper joins and printer settings can introduce error.

## 11. Visual and accessibility requirements

Contemporary science-museum identity: midnight navy/white, magenta microscopic accents, cyan astronomical accents; clear editorial typography and generous mathematical workspace. Pictures must be present at release. The exhibit scene evolves with the selected track, recorded measurements, labels, and outcome. Do not disguise quantitative diagrams as decorative art.

| Asset ID | Required asset / behavior |
| --- | --- |
| SN-A01 | Wide museum title scene linking the two size ranges |
| SN-A02–A09 | Eight reference cards, one for each SN-D01–D08 quantity, with code-rendered property/value/source labels |
| SN-A10 | Accessible logarithmic decade explorer for lengths, explicitly not one physical scale |
| SN-A11 | Microchannel/specimen and operation diagrams with correct labels and matching-exponent overlays |
| SN-A12 | Earth–Moon guide/template with exact centers, size guides, and dimensional scale bars |
| SN-A13 | Cell construction guide showing an intact biconcave disc; inspection view |
| SN-A14–A16 | Visibly distinct Featured, review-pending, and calibration-required exhibit states |

Original explanatory SVG diagrams are acceptable and must be labeled as such. If authentic scientific imagery is used, review and record its asset-specific credit/license and observation context before embedding. Do not call generated pictures microscopy or measured evidence. NASA attribution is not blanket permission for every third-party asset or endorsement. No external image selection or image licensing is completed by this specification.

Record asset ID, purpose, stage, dimensions, alt text, original/source/license status, and whether scale is meaningful. Render exact labels and scale bars in code. Aim for HTML ≤8 MB; require review above 12 MB. No emoji-only substitute for the required illustration set.

Controls/help target at least 44 × 44 CSS pixels; body/input text at least 16 px; visible focus; meaningful text errors and contrast. Every drag has keyboard/tap alternatives. Use accessible math descriptions and SVG data equivalents; decorative art has empty alt text. Respect reduced motion. Test iPad portrait/landscape, desktop, enlarged text, and the on-screen keyboard so the prompt, active field, errors, and navigation remain reachable without horizontal overflow or trapped scrolling.

## 12. Verification and acceptance contract

Use independent expected values, not the application's own evaluator as its answer oracle. Preserve reference checks separately from runtime/UI/physical evidence. All application checks below are **Not run** in this specification task.

| ID | Required implementation evidence |
| --- | --- |
| SN-Q01 | All twelve objectives required; eight operations present for both physical tracks; eight stages complete; no extension blocks core completion. |
| SN-Q02 | Exact expected values for C01–C07, both transfer variants, both scale plans, all model comparisons, and common-scale ratios. |
| SN-Q03 | Coefficient/exponent/common-power work checked independently of final result; equivalent methods accepted; no answer leakage. |
| SN-Q04 | Normalization, exponent zero/negative/bounds, 12-digit limit, tiny nonzero answers, Unicode minus, unit aliases, grouping, and zero rejection. |
| SN-Q05 | Ratio direction, common units, exact versus rounded Moon diameter, dimensionless division, speed×time and distance/speed units. |
| SN-Q06 | Tolerance endpoints pass and just-outside values fail fit; correct out-of-tolerance reporting reaches repair rather than academic rejection. |
| SN-Q07 | Center-to-center measurement; cell morphology guide; no fabricated measurements; changed build makes inspection stale. |
| SN-Q08 | Exact dependency invalidation, preserved valid siblings, track switching/restoration, unchanged independent transfers, contextual attempt history. |
| SN-Q09 | Every outcome reachable for both tracks; Draft/Provisional precedence; pending interpretation cannot become Featured; repairs retain explanations. |
| SN-Q10 | Physical/interpretation/paper-transfer reviews pending/accepted/repair states; oral alternatives; bypass history and later real recheck. |
| SN-Q11 | Save/reload/duplicate; multiple sessions; denied/quota/corrupt storage; newer-tab conflict; truthful status. |
| SN-Q12 | Single/bundle export-import, default copies, confirmed replacement, backup/migration, rollback; malformed/wrong-project/future/inconsistent state rejection. |
| SN-Q13 | Delete complete session and clear-all with count/scope, Cancel, export backup, partial-failure handling, reload, recovery, new work; other apps preserved. |
| SN-Q14 | All help/control paths by keyboard/touch; complete correct, error, repair, track-switch, resume, and teacher-review journeys. |
| SN-Q15 | Desktop/emulated layouts and, separately, physical iPad Safari/on-screen keyboard/school network; never substitute emulation for physical evidence. |
| SN-Q16 | A4/Letter outputs, all math and sources, grayscale, bounded long text, no teacher leakage; physical 50 mm calibration and assembled 600 mm strip. |
| SN-Q17 | Embedded art and standalone offline runtime; no required CDN/font/audio/API requests; imported text inert; recoverable errors. |
| SN-Q18 | Diagnostics run without mutating student work; source and approximation labels match data; explorer does not mix speed and length. |
| SN-Q19 | Versioned HTML/index byte equality; product/credit/version consistency; measured file size; answer/reference/report consistency. |
| SN-Q20 | Real deployed Powers of Ten subpath and served bytes/version/assets; hosted resume/export/import/print preview; existing subprojects unaffected. |

Required saved fixtures: Featured cell; Featured cosmic; pending physical review; pending interpretation review; each track outside tolerance with correct analysis; missing/incorrect label; stale upstream work; active bypass; pending paper transfer. Add wrong-answer and malformed-import fixtures. Use synthetic aliases and measurements for test fixtures, clearly identified as fixtures; never present them as student observations.

### Reference cases required before runtime testing

| Case | Expected result |
| --- | --- |
| Eight source operations, in C04a…C07b order | `2e-4`, `3.84e8`, `8`, `5e2`, `3.15e-5`, `4.44e8`, `6e-6`, `1.3872e9` |
| Microscopic scale | `20,000:1`; 160 mm; 34 km person; 0.04 mm DNA width |
| Cosmic scale | `1:640,000,000`; Moon 5.46875 mm exact / 5.5 mm construction; centers 600 mm |
| Cosmic limitations | Sun 2.1875 m; Earth–Sun distance 234.375 m |
| Common-scale comparison | available ratio 1500; Earth/cell ratio `1.6e12` |
| Exact tolerance endpoints | Cell 158/162; Earth 19/21; Moon 4.5/6.5; centers 595/605 mm all pass fit |
| Just beyond endpoints | Cell 157.9/162.1; Earth 18.9/21.1; Moon 4.4/6.6; centers 594.9/605.1 mm fail fit |
| Transfer results | A `3e-5 m`; B `6e8 m`; correct reciprocal scale interpretations |

At delivery, every reported check must be Passed, Failed, Not run, or Not applicable with its environment/evidence. No physical iPad, school-network, physical-print, student-model inspection, runtime, or deployment verification is implied by mathematical reference checking.

## 13. Implementation, checkpoint, release, and deployment

Follow **DESIGN → CHANGE SPEC → IMPLEMENT → CHECKPOINT → VERIFY → VERIFIED CHECKPOINT → RELEASE → DEPLOY**.

1. Review Draft 1, especially SN-I01–SN-I08. Record accepted changes as a versioned specification and approval record in the canonical repository. Add `powers-of-ten/docs/PROJECT-BRIEF.md` identifying the source commit, must-retain features, devices, deployment method, handbook baseline, and selected standards. Update documentation indexes without overwriting concurrent work on other apps.
2. Implement fixed content, pure exact evaluators, and meaningful reference tests; then the complete eight-stage journey, dependencies, review state, saves/imports/deletion, print outputs, and embedded art. Suitable helpers may be copied from reviewed project source; do not create a shared runtime or depend on another HTML file.
3. Preserve a complete source checkpoint before extended testing: for example, **Powers of Ten v0.1.0 implementation checkpoint**. Record the full commit and candidate hashes.
4. Run SN-Q01–SN-Q20 where applicable, record unrun physical checks, fix defects, checkpoint changed bytes, and rerun affected checks. Do not transfer a previous candidate's pass claims to changed code.
5. Preserve the exact verified candidate. Use a “verified release” commit label only when that exact committed candidate has passed its required gates; otherwise retain release-candidate wording and explicit limits.
6. Package documentation and deployment materials without adding features. Recover the preserved candidate after ZIP/upload/packaging failure; never rebuild a verified implementation merely to redeliver it.
7. On authorized release/deployment, use the repository's GitHub Pages arrangement after checking its current configuration. Verify the actual hosted entry point, app version, bytes, assets, save/import/export, and print preview. Repository upload alone is not deployment verification.

Proposed deliverable layout:

```text
docs/change-specs/POWERS-OF-TEN-v0.1.0.md
docs/decisions/POWERS-OF-TEN-v0.1.0-APPROVAL.md
powers-of-ten/
  PowersOfTen_v0.1.0.html
  index.html
  README.md
  CHANGELOG.md
  docs/PROJECT-BRIEF.md
  docs/TEACHER-GUIDE.md
  docs/ASSET-MANIFEST.md
  docs/QA-REPORT-v0.1.0.md
  docs/DEPLOYMENT-v0.1.0.md
  tests/reference-cases-v0.1.0.json
  tests/verify_spec_reference.py
  tests/                         # implementation/browser fixtures as needed
```

Only the HTML is needed to play. Development sources/build scripts may be retained for maintenance, but cannot become runtime dependencies. Preserve `docs/sources/dossier-v1.0.0/` unchanged and do not alter other subprojects' application files, storage, or deployment routes.

## 14. Preparation record and limits

| Preparation item | Result |
| --- | --- |
| Canonical repository/source baseline | Read through connected GitHub tools at the commit identified above. |
| Dossier and project rules | Relevant common, Powers of Ten, acceptance, handoff, reference, and source sections read; original fixtures read. |
| Handbook | Four files and exact revision recorded in section 1; no new rule ratified. |
| Science source check | R1–R6 consulted on 30 September 2026; supplied rounded values retained. No external scientific images licensed or embedded by this task. |
| Standards/technical check | R7–R10 consulted for the narrow references described below. Alignment remains partial; no full standards certification. |
| Independent specification arithmetic | Passed — 62/62 exact reference checks using Python rational/decimal arithmetic: eight operations, conversions, scales, limitations, transfers, tolerance/calibration boundaries, and template length. This is not an application test. |
| Required-ID coverage | Passed — 40/40 presence checks for 12 objectives, 8 stages, and 20 acceptance-test IDs. This confirms document coverage, not implemented behavior. |
| Application, physical devices, school network, printer and physical model | Not run; this task produces a specification only. |
| Approval / implementation / deployment | Not performed. Draft decisions remain reviewable. |
| Repository write | Not performed; proposed canonical destination identified on the first page. |

This document preserves the twelve source objectives, eight required operations, both physical tracks, original numerical defaults/tolerances, physical evidence distinction, all museum outcomes, embedded visual requirements, help, saving, printing, and release discipline. There is no identified conflict with the owner's current request. The previously proposed decisions were subsequently approved for implementation; see the approval record.

## 15. References and provenance

Repository sources are pinned to `b1f9ae4158631043314e8a88e5f56549cebd319c`. Dossier Markdown blob: `e8eea73b4cf8b3b124353b155b72a1c24458c908`; reference-fixture blob: `3ceb73d4779c4f3cbd6f0d5896f182d8dc0ca93e`; Powers of Ten planning README blob: `48141a20b2d3648c42e02eb891b276335d36ba49`. Blob IDs identify file content, not repository commits. Original Word/package provenance remains in the repository's `docs/sources/PROVENANCE.md`; it was read, not independently rehashed in this task.

| ID | Source | Use / limit |
| --- | --- | --- |
| R1 | [NHGRI: nanoscale technologies and DNA sequencing](https://www.genome.gov/27550069/2012-release-new-nihnhgri-grants-to-harness-nanoscale-technologies-to-cut-dna-sequencing-costs) | Approximate 2 nm DNA width; not a measurement of a particular displayed image. |
| R2 | [Histology Guide: blood smear](https://histologyguide.com/slideview/MH-033hr-blood-smear/07-slide-1.html) | Red-cell exemplar range and morphology. No medical inference or image reuse permission implied. |
| R3 | [NASA: Earth facts](https://science.nasa.gov/earth/facts/) | Earth diameter and mean distance context; use fixed dossier teaching values, not dynamic page widgets. |
| R4 | [NASA: Moon facts](https://science.nasa.gov/moon/facts/) | Moon dimensions/distance context; radius and diameter must not be confused. |
| R5 | [NASA: Sun facts](https://science.nasa.gov/sun/facts/) | Approximate solar diameter. |
| R6 | [NIST: meter](https://www.nist.gov/si-redefinition/meter) | Exact vacuum speed underlying the rounded classroom value. |
| R7 | [CCSS Grade 8 Expressions & Equations](https://www.thecorestandards.org/Math/Content/8/EE/) | 8.EE.A.3–4 magnitude/operation reference anchors; no claim to assess every clause. The dossier also cites 7.RP.A.2 and course lessons 51, 57, 69, 83, 88, 98; those remain inherited curriculum metadata. |
| R8 | [NGSS MS-ESS1-3](https://www.nextgenscience.org/pe/ms-ess1-3-earths-place-universe) | Partial connection to solar-system data/model scale and scale/proportion/quantity, not a complete performance-expectation assessment. |
| R9 | [MDN: localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) | Browser storage scope/failure/file-URL limitations; portable export remains required. |
| R10 | [GitHub Docs: GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | Static hosting reference; current repository configuration must be checked at deployment. |

Source access and arithmetic verification do not establish application quality, physical measurement truth, classroom timing, or completed deployment.
