# Road Trip Planner specification review

**Date:** 30 September 2026  
**Candidate:** Road Trip Planner v0.1.0 implementation specification, Draft 1  
**Repository starting commit:** ec7753842c8321f5e2a9192529cb60da1e44d1b1  
**Scope:** Source preservation, specification completeness and mathematical feasibility. No application exists.

**Historical report:** The results and pending-decision wording below describe Draft 1 at checkpoint 393f2e1. William McAda subsequently approved the specification and P-01 on 30 September 2026. See the [approval record](../decisions/ROAD-TRIP-v0.1.0-APPROVAL.md) and the fresh approved-revision reference report linked there. The original review findings are retained without being relabeled as application verification.

## Results

| Check | Result | Evidence and limitation |
| --- | --- | --- |
| Attached Word dossier versus handoff copy | Passed | Identical SHA-256; source is not reconstructed from conversation history |
| Original manifest's 21 file sizes and hashes | Passed | source-preservation-2026-09-30.json; all files preserved unchanged |
| Original dossier reference checker | Passed | 77/77 reference checks; fresh output in dossier-reference-checks-2026-09-30.json |
| Expanded Road Trip reference checker | Passed | 259/259; canonical phases, outcome fixtures, boundaries, transfers, and 81 choices before/after proposed event |
| Objective and stage coverage | Passed | Nine explicit checkpoint contracts, eight stages, same source objective identities |
| Proposed changes distinguished | Passed | P-01 labeled pending; numerical defaults and implementation details distinguishable from universal approvals |
| Saved-work rule included | Passed | Delete session, complete associated records, clear all Road Trip sessions, confirmation/cancel, backup/recovery, isolation/failure tests specified |
| Runtime implementation and mathematical parser | Not run | No HTML or JavaScript application produced |
| UI, help, persistence, import/export, deletion | Not run | Written contracts and future test matrix only |
| Artwork, browser print, desktop/iPad input | Not run | Concept sources preserved; final asset work and runtime verification belong to implementation |
| Physical iPad and school network | Not run | No classroom/device session performed |
| Deployment | Not run | No GitHub Pages settings or live application changed |

Run reference checks from the repository root:

    python3 docs/sources/dossier-v1.0.0/verify_reference_fixtures.py
    python3 road-trip-planner/tests/verify_spec_reference.py

The new checker computes itemized trip totals independently of the coefficient-form model, then compares both across all 14 allowed day values for all 81 choices in each phase. It verifies literal expected values in the JSON fixtures. It does not implement the future JavaScript parser or certify student-save schema behavior.

## Outcome feasibility

These counts assume required mathematics is current, no active bypass, and required statements are submitted. They describe the authored scenario, not learner outcomes or mastery.

| Scenario phase | Choice combinations | Within budget | Client delighted | Trip approved | Revision requested |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original prices | 81 | 62 | 18 | 35 | 28 |
| Proposed P-01 event applied | 81 | 47 | 9 | 29 | 43 |

All three endings are reachable. A plan with a reserve greater than 5% can still reach the top ending when its stated priorities are met and its reserve statement is submitted. The event always changes a seven-day plan by $120 under P-01, including plans that initially selected basic or premium lodging.

## Review findings resolved in Draft 1

- Seven travel days means six nights; the hotel event changes slope and constant in opposite directions.
- A wrong model can match the correct total at one duration. The fixture 200d+370 equals $1,770 at seven days but must fail C04.
- Distinguish the project domain cap of 14 days from the mathematical affordability bound; no fabricated day-15 failure is required.
- Preserve before/event/final snapshots and first attempts with their original scenario; an upstream edit does not destroy historical evidence.
- Separate automatic arithmetic/structural checks from teacher review of prose, research and individual paper/oral work.
- The original artwork is a reference set, not evidence that the complete required illustrations already exist.
- Preserve the original dossier checker/report; do not overwrite historical evidence with a new run.

## Remaining content decision

P-01: extend the dossier's standard-hotel +$20/night event to whichever hotel category students selected. This is recommended to give every pair the required C08 revision experience. It remains a proposed change, not an approved alteration. If declined, revise the specification to retain the standard-only event and require a separate standard-hotel comparison for other pairs.

The completed preparation is a specification checkpoint. It must not be named a verified application release.
