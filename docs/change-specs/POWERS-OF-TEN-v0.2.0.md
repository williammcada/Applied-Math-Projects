# Powers of Ten v0.2.0 — Science-to-Mathematics handoff

**Status: implementation specification, Draft 1. Planning only.**
**Owner:** William McAda. **Credit:** A WILLIAM MCADA PRODUCT.
**Date:** 9 October 2026 (Asia/Shanghai).

The owner requested one science lesson and one mathematics lesson, with Day 1 complete within 40 minutes and a tangible saved output used in the other class. After reviewing the proposed science-first design, the owner said “proceed.” This authorizes recording this plan. The high-level science-first direction is accepted; detailed implementation choices below are proposed. This document does not claim application implementation or classroom timing verification.

## 1. Canonical source and scope

Repository: williammcada/Applied-Math-Projects. Inspected main baseline: `811dfc383c70861dcc6ccdcfa80df8a7b3f56e9d`. Powers of Ten remains app 0.1.0, content/schema 1.0.0; its HTML SHA-256 is `d9a042236b8968cc172f17fb64cfeb564967b77434259a06192ffbbf4de0a7ac`.

Read the existing v0.1.0 change specification, project brief, teacher guide and core implementation. Handbook consulted: `fd4330863f4cc0812180fbf1de122970a42c7885`, AI-START-HERE.md, UNIVERSAL-RULES.md, CONDITIONAL-STANDARDS.md and RELEASE-CHECKLIST.md. Relevant: U-01–U-09, U-11 and S-02/S-04/S-05. U-10 held-game-control requirements are not applicable. No shared handbook rule changes.

Primary classroom host: https://mcada-applied-math.netlify.app/powers-of-ten/ . GitHub remains canonical. Preserve standalone/offline desktop delivery, iPad/desktop controls, original artwork, embedded scientific references, exact mathematics, saved-work deletion, source labeling and honest review status. No new accounts, backend, telemetry, remote QR service or automatic submission.

## 2. Learning design

Central question: **How can we represent something too small or too large to experience directly—and how trustworthy is our model?**

Day 1 is Science: build, observe, measure, distinguish evidence from representation, explain limitations. Day 2 is Mathematics: interpret quantities, calculate with scientific notation, determine scale and evaluate the actual measurements from Day 1.

One pair, one physical model, one portable evidence record. Each pair builds either a cell or an Earth–Moon model. Both tracks remain available; students compare an example of the other track. Do not require both builds from one pair.

Prerequisites: scientific notation, signed exponent rules, all four operations, metric conversion, ratio direction and basic ruler use have already been taught. These are application lessons, not introductory instruction. Teacher preparation and material distribution occur before the 40-minute clock. No homework is required to produce the Day 1 handoff.

Science completion is independent of mathematics correctness. Day 1 does not require eight operation checks, a scale-factor derivation, a deviation calculation, a finished exhibit placard or individual math transfers.

## 3. Science lesson — 40 minutes

| Minutes | Student work | Required evidence |
|---|---|---|
| 0–4 | Read the short museum brief; compare a source image and a model; record a prediction. | Object and property; brief prediction |
| 4–8 | Select/confirm the assigned track; read the source and supplied construction dimensions; assign Builder/Verifier. | Track, aliases, source and labeled construction brief |
| 8–22 | Construct from prepared materials. Swap practical roles at midpoint. | One physical model |
| 22–29 | Measure actual dimensions and record tool/resolution; another pair checks one dimension where practical. | Actual measurements, units, tool and any disagreement |
| 29–34 | State one preserved feature and one omitted/distorted feature; briefly inspect the other-track example. | Scientific interpretation and other-track observation |
| 34–40 | Label, pack and save. Check the passport, export and reopen the progress copy. | Model plus completed Science Evidence Passport |

### Track A: cell

Supply the existing rounded actual diameter, 8 micrometers, and target model diameter, 160 mm. Preserve the biconcave disc concept; an intact shallow depression, not a hole or nucleus. Use reusable modeling material and/or a quick paper/card representation; no drying, elaborate sculpture or decorative grading. A flat representation must explicitly state that it omits three-dimensional form. The scale claim applies to diameter only, never to an invented thickness.

Students measure diameter and record the actual value. They explain that this is a representation based on supplied scientific references, not their own observation of a living cell. The intended 20,000:1 scale is derived on Day 2; do not require that answer for Science completion.

### Track B: Earth–Moon

Supply target Earth diameter 20 mm, Moon construction diameter 5.5 mm and center-to-center separation 600 mm. Prepare card discs or rapidly usable templates and a strip/string with separate center marks. Students assemble and measure the model; cutting a tiny accurate circle is not the learning objective. Diameter and separation must share the intended scale; Moon rounding is disclosed on Day 2. Explain that the model does not show orbital motion or the full three-dimensional system.

### Science teacher preparation

Prepare rulers with millimeter marks, tape, pencils, pair labels, paper/card, reusable modeling material if chosen, and 600 mm workspace/measure for cosmic teams. Preprint one blank passport per pair and calibrated templates when used; verify the 50 mm calibration line within 0.5 mm. Provide a teacher example of the other track, so a gallery visit never waits for another pair to finish. Test the site and chosen file-transfer route on the actual iPads beforehand. Reserve six minutes for handoff; begin packing at minute 34.

If construction runs slowly, simplify finishing, use prepared components, and omit decoration. A rough or out-of-tolerance model is usable scientific evidence. Never enter ideal measurements or certify a missing build to meet time. A pair lacking required evidence exports an honest incomplete passport; the teacher can provide a labeled example dataset on Day 2, which must remain distinguishable from the pair's measurements. Such a case fails the completed-Day-1 timing target and is recorded for redesign.

## 4. The Science Evidence Passport

A one-page A4/Letter student record, readable in grayscale. Also show the same record in a touch-friendly screen preview. It contains:

1. Project/version, pair aliases, short human-readable model label and session reference.
2. Track, object, property, supplied real-world values and source identifiers.
3. Intended model dimensions, visibly separate from actual observations.
4. Actual measurement table with dimension, value, unit, tool and resolution/estimate.
5. Prediction; one feature preserved; one feature omitted/distorted; short other-track observation.
6. Peer-check result or explicitly “not checked,” without inventing acceptance.
7. Next-class question: **What scale did we intend, and what scale did we actually produce?**
8. Science status, record revision and save/export time; no false claim of teacher approval.

Prompts use short fields or sentence starters. Suggested bounds: prediction 100 characters, each science claim 180, other-track observation 140, tool 60, peer note 120. Tell students the limits before entry; never silently truncate. Print must fit the stated bounds at readable type. Longer legacy responses use a labeled continuation page rather than being cut off.

### Day 1 completion contract

Require two aliases, track/source/property identification, build confirmation, all selected-track measurements with valid units, tool/resolution and the short science responses. Reported out-of-tolerance dimensions do not block completion. Peer/teacher acceptance is not a mandatory Day 1 bottleneck; human-review status remains separate. “Ready for mathematics” means the evidence record is usable, not that the science interpretation has been approved or independent mastery established.

### Saving and transport

Provide a prominent **Finish Science Day** workflow: validate missing fields together, preview passport, Save, Download progress, and Test saved copy. Test saved copy imports the downloaded file into a temporary preview and compares its session/revision and handoff fields without replacing the original. Report what was tested; a download click alone does not prove durable storage.

Keep **Export draft** available for interrupted work. The complete record is portable JSON plus a human-readable passport. Support print/save-as-PDF through the browser, but do not assume every iPad has a printer or PDF route. The preprinted blank passport is the guaranteed physical fallback; pairs fill it from the displayed record and label the model. Teachers collect passports/models together at the end of Science.

On Day 2, offer **Continue on this device**, **Import Science progress**, and **Use my paper passport**. Paper recovery asks only for the handoff data, records the recovery route, and does not force repetition of Science. It cannot award review status from a copied checkbox. No shared folder, email, AirDrop or LMS integration is assumed; teachers select an available transfer route beforehand. QR links open the app, not the pair's private progress; do not promise cloud synchronization.

## 5. Mathematics lesson — target 40 minutes

| Minutes | Student work |
|---|---|
| 0–3 | Resume/import and match the passport to the labeled model. |
| 3–7 | Apply existing notation, magnitude and conversion checkpoints in a compact review. |
| 7–23 | Eight calculations: all four operations in both microscopic and astronomical contexts. |
| 23–31 | Intended scale; actual observed scale; deviations from construction targets. |
| 31–36 | Quantitative limitation, shared-scale comparison and final scientific interpretation. |
| 36–40 | Separate individual transfer responses; save/export the final exhibit record. |

The 40-minute second lesson is a design target, not an additional user-imposed hard constraint. Day 1's 40-minute completion requirement remains the primary timing gate. Do not silently remove content if pilot timing fails; simplify interaction first, then report remaining workload and propose a change.

### Retained mathematics

Retain C01–C03, all eight C04–C07 expressions and exact answer contracts, C08 scale calculations, C09 signed deviations, C10 one selected numerical limitation plus museum-ratio comparison, C11 source/property interpretation and C12's two individual variants. Retain both micro/macro ranges and negative exponents. The existing 12 objectives remain traceable.

Proposed interface change: final scientific result and correct unit remain required for each operation; the repeated coefficient/exponent/common-power entry grids become optional **Show my method** scaffolding. When submitted, method responses are checked and preserved, but hidden empty scaffolding cannot block core completion. This explicitly supersedes the v0.1.0 requirement that every intermediate cell be correct before progress. Reports distinguish final-answer evidence from checked-method evidence; never infer an unobserved method.

Pairs alternate Calculator/Checker roles across the eight tasks. Each learner completes their own final transfer without the partner's response displayed. Existing first-versus-corrected evidence and human-review modes remain.

### Use the actual science evidence

Use exact unit conversions before division. For each dimension, observed scale factor = measured model length / supplied actual length. Keep intended factor, rounded construction target and observed factor distinct.

- Cell: actual 0.008 mm; target 160 mm; intended factor 20,000. A measurement of 159 mm implies observed factor 19,875 and deviation −1 mm. It does not prove a uniform thickness scale.
- Earth: actual 12,800,000,000 mm; target 20 mm; intended factor 1/640,000,000.
- Moon: actual 3,500,000,000 mm. At the intended factor, exact diameter is 5.46875 mm; construction target 5.5 mm. An ideal 5.5 mm construction therefore does not produce numerically identical inferred scale to Earth. Label this as disclosed rounding, not contradiction.
- Earth–Moon center separation: actual 384,000,000,000 mm; target 600 mm. A measurement of 598 mm gives observed factor 598/384,000,000,000 and deviation −2 mm.

Observed-scale response fields accept exact equivalent fractions or ratios; do not force long recurring decimal quotients. Render an optional approximate ratio clearly marked with its rounding. Scale checks have exact answer contracts; physical tolerance never becomes tolerance for academic arithmetic.

Retain original fit intervals: cell 158–162 mm; Earth 19–21 mm; Moon 4.5–6.5 mm; separation 595–605 mm, inclusive. For cosmic consistency, ask whether dimensions fit the stated targets/tolerances at the intended scale; do not invent a second arbitrary percentage threshold or require identical observed ratios. Claims of exact equality are inappropriate after rounding and measurement.

## 6. Proposed application and state design

Replace continuous stage gating with a subject dashboard: **Science Day**, **Mathematics Day**, **My evidence and exports**, **Teacher guides**. Science has Brief → Build → Observe → Passport. Mathematics has Resume evidence → Quantities → Calculations → Scale audit → Exhibit and individual response. Narrative and procedural instructions occupy separate labeled panels under U-11.

Maintain separate indicators: science record completeness; handoff-copy verification; math checkpoint status; physical model fit; human review; final museum outcome. No single completion flag can represent all six.

Proposed target versions: app 0.2.0, content 2.0.0, progress schema 2.0.0. Keep projectId `powers-of-ten`. Freeze exact schema field definitions before coding; preserve bounded strings, exact numeric text and strict validation. Add a science evidence object with track/build revision, supplied-target identifiers, measurements/tool, claims, source IDs and status. Store handoff verification separately from academic correctness. Track paper recovery and teacher-example provenance explicitly.

Science measurements must not require C08 or C09 arithmetic first. Math consumes the same recorded values, not duplicate editable copies. Changing science measurements retains prior responses while marking only dependent observed scales, deviations, interpretation and reviews stale. Standard C04–C07 tasks remain valid if their fixed givens did not change. Track switching preserves inactive work and clears no evidence. A rebuilt model has a new build revision and requires fresh measurements.

### Existing work

Never overwrite a 0.1.x session in place. Offer export first, then a migrated copy preserving the original identity link, raw inputs, history and original reviews. Map available measurements and source statements; flag missing new science fields. Keep old approval records as historical unless they cover unchanged evidence and still meet the new contract. New fields cannot be marked complete from old stage numbers. Reject malformed/unsupported files with useful errors while preserving valid current work. Test both individual and bundle imports, copy/replace conflicts, corrupted storage and blocked storage. Preserve U-09 deletion scope, confirmation and backup behavior.

## 7. Teacher deliverables

Produce separate Science and Mathematics guides, each with purpose, preparation, a timed sequence, student prompts, expected evidence, common misconceptions, accessible alternatives and a clear finish point. Science guide includes packing/collection and transfer checks; Math guide begins with resume/recovery and includes exact keys. A shared one-page coordination sheet records pair continuity, model location, chosen transfer method and prerequisites.

Student outputs: Science Passport, physical model label, final exhibit placard, full report and independent exit slips. Preserve existing build templates and downloadable standalone HTML; update visible/title/download version consistently. Update the launcher summary to explicitly say “Science + Math · 2 lessons”; because launcher HTML changes, increment its own version separately. Other project applications are outside this revision.

## 8. Verification and release gates

| Check | Acceptance | Current result |
|---|---|---|
| Separate subjects | Science completes without math prerequisite gates; Math opens matching Science evidence. | Not run |
| Both tracks | Complete a normal journey for cell and Earth–Moon. | Not run |
| 40-minute handoff | Representative students finish build, evidence, packing and a usable saved/physical handoff within 40 minutes under documented preparation conditions. | Not run — classroom timing required |
| Different iPad | Export on device A; import on B; match every handoff field and resume correct next task. Also test paper recovery. | Not run |
| Honest completion | Wrong shape/poor fit and pending review remain distinguishable from incomplete record or incorrect mathematics. | Not run |
| Mathematics | Retained eight expressions and 12-objective map; exact/equivalent responses; observed-scale fixtures; rounding/tolerance boundaries. | Not run |
| Dependencies | Science edits invalidate only dependent evidence; earlier work/history remains. | Not run |
| Existing saves | Migration copies, legacy data retention, invalid files, bundle and conflict paths. | Not run |
| Recovery | Cancelled downloads, denied storage, lost file, paper passport and interruption before save. No false success. | Not run |
| Printed output | One-page bounded passport; A4/Letter/grayscale/long text; calibration lines physically measured. | Not run |
| Devices | Desktop keyboard and physical iPad touch/software keyboard, Files import/export, camera QR, school network. | Not run |
| Hosted release | Netlify exact bytes match preserved candidate and both subject workflows operate at live URL. | Not run |

Preserve an implementation checkpoint before extended verification. Fixes get new identifiable checkpoints. Preserve the exact passed candidate before release packaging. Never call classroom duration or physical-device behavior verified based solely on automation. If the timed trial is unavailable, publish only with that limitation explicit.

## 9. Execution sequence after plan review

1. Finalize schema and checkpoint mapping against the actual 0.1.0 source; preserve fixtures and export examples.
2. Implement subject flow and portable Science handoff, then the Math scale audit and migration.
3. Produce subject-specific guides and print outputs, checkpoint, and verify.
4. Preserve verified candidate, update release materials and launcher, deploy on Netlify and verify the actual hosted paths.

No application changes are included in this planning checkpoint. Implementation awaits the next instruction.
