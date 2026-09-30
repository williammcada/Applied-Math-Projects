# Theme Park Designer v0.1.0 — QA Record

**Date:** 30 September 2026  
**Result:** 189 automated assertions passed, 0 failed, on the preserved candidate below. Local verification is complete for the exercised cases. Physical classroom acceptance remains pending. This is not a claim that every device or all possible input combinations have been tested.

## Exact candidate

| Record | Identity |
| --- | --- |
| Approval checkpoint | `af8a48d83f93e846aa77da61de254a06018096bd` |
| Implementation checkpoint before testing | `39c4981394c28c89f22f7e23d6f040b932edbb61` |
| Corrected candidate preserved before final run | `e1c81fc17a5da727e7bf35feeb4b79770a03f394` |
| App / content / schema | 0.1.0 / 1.0.0 / 1.0.0 |
| `index.html` and `ThemeParkDesigner_v0.1.0.html` | Byte-identical, 105,803 bytes each |
| HTML SHA-256 | `c3e9dbe937919751c99925a82be16fe2d45c1797d40e4b13ea8e0e03ce4ed6d9` |
| Git HTML blob | `78bfbbf5d015bf1fa9eb8301645d6426eb871314` |

The final full run occurred after the corrected candidate was committed. Release documentation and evidence do not alter these application bytes. Recover this candidate if packaging or deployment fails.

## Automated evidence

| Suite | Passed | Evidence |
| --- | ---: | --- |
| Core mathematics, geometry, state, parser, storage | 91 | [core-results.json](verification/core-results.json) |
| Exact constraint boundaries and complete ending fixtures | 29 | [edge-core-results.json](verification/edge-core-results.json) |
| Complete student browser workflow | 50 | [browser-results.json](verification/browser-results.json) |
| Saved endings, touch, deletion, denied storage, injection/import | 19 | [edge-browser-results.json](verification/edge-browser-results.json) |
| **Total distinct assertions in the final run** | **189** | Repeated development runs are not added to this total. |

Environment: Linux, Node (exact version in core results), headless Chromium 153.0.8010.0 via Playwright. Desktop 1440 × 1050 and tablet viewport emulation at 768 × 1024 / 1024 × 768; touch emulation in the edge browser suite. Browser suites opened the actual standalone file; the complete student run used offline mode. It recorded zero runtime HTTP(S) requests and zero uncaught exceptions.

The workflow creates a new design, deliberately enters the diameter/radius misconception, retains the first failed response, corrects it with a fraction, places six facilities, constructs paths/green/expansion, corrects a double-counted union, calculates the budget, saves different A/B designs, compares and recommends, records separate transfer responses, reaches distinction, downloads real JSON, reloads, imports copies, cancels deletion, backs up, clears Theme Park records, preserves another project's sentinel, restores the backup, and exercises all ten help panels.

## Specification traceability

“Exercised” identifies the available evidence, not exhaustive combinatorial coverage. The approved specification's original “Not run” column is historical; this record supplies implementation results.

| Spec | Local evidence / result | Scope limits or remaining acceptance |
| --- | --- | --- |
| TP-Q01 | Complete workflow traverses eight stages and required checks for all nine objectives. | Classroom observation pending. |
| TP-Q02 | Baseline 704/432/480/784 m², 79,600 cr, 10,400 cr, 140 m² independently asserted. | None for baseline fixtures. |
| TP-Q03 | Scale ratio, squared area factor, radius, triangle half, footprint and embedded shape misconceptions asserted. | None for exercised examples. |
| TP-Q04 | Decimals/fractions, Unicode minus, commas, invalid/blank inputs, units, and exact rounding exercised. | Not every numeric string enumerated. |
| TP-Q05 | Bounds, grid rejection, boundary touch, atomic collisions, rotated dimensions and door segments exercised. | Physical drag gestures not device-certified. |
| TP-Q06 | Rooted baseline, missing connector, diagonal and corner-only contact, rotated entrance segment exercised. | Arbitrary network topologies not exhaustively enumerated. |
| TP-Q07 | Cell union, repeated paint, disjoint land, expansion accounting exercised in model and UI. | None for exercised fixtures. |
| TP-Q08 | Full boundary, baseline quote, signed overrun and dynamic land costs asserted. | None for exercised fixtures. |
| TP-Q09 | 600/604 paths, 480/476 green, 4,500/4,460 reserve, 100/96 expansion, 90,000/90,040 cost thresholds exercised. | Fixed main spines make the path minimum unreachable through ordinary editing. |
| TP-Q10 | Correct low-green and over-budget designs produce revision; wrong arithmetic blocks its field/checkpoint. | Complete distinction flow and saved revision fixture exercised. |
| TP-Q11 | Green/expansion changes selectively invalidate affected evidence and retain raw/first responses; chosen snapshot stays frozen. | Dependency combinations beyond recorded assertions remain unenumerated. |
| TP-Q12 | Distinct A/B, equal-cost numerical tradeoff, selected snapshot and recommendation exercised. | Reflection quality requires a teacher. |
| TP-Q13 | Both digital variants, response covering, separate records and printed slips exercised. | Actual paper/oral teaching observation pending. |
| TP-Q14 | Five complete portable fixtures imported through UI; visible outcome headings and model status match. | None for saved fixtures. |
| TP-Q15 | Actual downloaded export, resume, copy import, backup restore and malformed import preservation pass. | None for normal lesson workflow. |
| TP-Q16 | Denied storage UI/export, stale revision rejection, wrong project/future schema, invalid cells/fields tested. | Quota exhaustion, corrupt-storage recovery UI and multiple real browser-tab race scenarios not fully automated. |
| TP-Q17 | Snapshot deletion/reload, session cancellation, group storage deletion, clear-all/backup recovery and unrelated project retention exercised. | Browser-specific storage failures remain device checks. |
| TP-Q18 | Markup alias is not injected; malformed, oversize, unknown-field/cell inputs rejected. | Maximum combinations of all bounded collections not stress-tested. |
| TP-Q19 | All Help dialogs, focus restoration, modal keyboard containment, coordinate placement and touch painting pass; reduced-motion CSS present. | Screen-reader audit and physical assistive-technology use pending. |
| TP-Q20 | Desktop plus portrait/landscape tablet emulation have reachable layout and no page overflow. | Physical iPad/Safari and software keyboard pending. |
| TP-Q21 | Ten A4/Letter PDFs generated; expected pages and all numbered footers audited; map/comparison/teacher rendering visually inspected. | Physical grayscale output remains printer acceptance. |
| TP-Q22 | PDF vector site measures approximately 149.996 × 99.997 mm; CSS calibration and grid dimensions match intended scale. | Physical 150 × 100 mm site / 5 mm grid / 50 mm line measurement pending. |
| TP-Q23 | Embedded assets; original SVG manifest; complete local offline journey; zero runtime network requests. | Hosted offline reopening not promised. |
| TP-Q24 | Full real browser journey with error/correction, plans, transfer, ending, save/import and print passed. | Actual classroom timing pending. |
| TP-Q25 | Index/versioned HTML hashes match; exact release identity retained. | Hosted observation recorded in [deployment record](DEPLOYMENT-v0.1.0.md). |

## Print audit

| Output | A4 pages | Letter pages |
| --- | ---: | ---: |
| Student report | 9 | 9 |
| Scale map | 1 | 1 |
| Brochure | 1 | 1 |
| Transfer slips | 1 | 1 |
| Teacher reference | 6 | 6 |

[print-audit.json](verification/print-audit.json) records PDF identities, page counts, every page footer, and the measured PDF site rectangle. PDFs are generated by the browser test scripts; they are not app dependencies. Unique pattern IDs preserve the grid/green hatch when previews and multiple maps coexist. The comparison fits one report page. Teacher and student outputs remain separate.

## Corrections before the final checkpoint

Resolved stale optional expansion import, overly broad layout-evidence invalidation, rotation of the triangle diagram, comparison input rerendering on blur, premature answer exposure in draft outputs, SVG pattern collisions in PDF, comparison page overflow, and print background color. Portable progress export uses the approved named envelope. A teacher-PDF test initially inherited screen media; the harness now explicitly enables print media. No application changes followed the final successful run.

## Remaining classroom acceptance

1. Open on the intended school network and physical iPad/Safari, in both orientations and with the software keyboard.
2. Perform touch placement, rotation, save/export/import and classroom role swaps on that device.
3. Measure a 100% A4/Letter print, check grayscale labels/hatching, and confirm the available printer workflow.
4. Observe lesson pacing, independent transfer and paper/oral accommodations with learners.

These checks require the actual environment and are intentionally pending. Emulation and PDF inspection must not be renamed as physical-device or measured-paper evidence.
