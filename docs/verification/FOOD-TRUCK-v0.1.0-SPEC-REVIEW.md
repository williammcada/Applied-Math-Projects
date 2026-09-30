# Food Truck v0.1.0 — specification preparation review

**Date:** 30 September 2026  
**Candidate:** [Implementation specification Draft 1](../change-specs/FOOD-TRUCK-v0.1.0.md)  
**Repository source baseline:** `cf13e7f3111b2291a07c1387707fbb5d8b814ad5`  
**Disposition:** Prepared for owner review. Implementation and deployment have not begun.  
**Scope:** Source integrity, objective/stage coverage, reference arithmetic and branch feasibility.

## Checks actually run

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| Original source manifest | Passed | All 21 files retain exact sizes and SHA-256 values; [source audit](food-truck-source-review-2026-09-30.json) |
| Owner-supplied Word versus archived Word | Passed | Byte-identical; SHA-256 `398716c649a181d50fb201a18a6014a88b3d51b9da1fec93c3b1b52592c6bef5` |
| Current project and handbook identity | Passed | Project source baseline above; handbook `00cbde605ab08203b6b5fd2374d225155608fc29`, v0.1.1, unchanged from Road Trip |
| Original dossier reference checker | Passed | 77/77; [fresh results](food-truck-dossier-checks-2026-09-30.json); original archived report unchanged |
| Food Truck reference checker | Passed | 659/659; [results](food-truck-spec-checks-2026-09-30.json), [fixtures](../../food-truck-business-launch/tests/reference-cases-v0.1.0.json), [checker](../../food-truck-business-launch/tests/verify_spec_reference.py) |
| Fixed constants versus dossier fixtures | Passed | Recipe quantities/prices, batch size, fixed fee, service rate/hours and demand table agree |
| Objective/stage coverage | Passed | Ten explicit C01–C10 contracts, eight S01–S08 stages and twenty planned Q01–Q20 checks |
| Specification outcome table versus literal fixtures | Passed | All 12 price/stock rows agree on sales, revenue, expense, signed profit, waste and ending |
| Implementation assumptions visible | Passed | FT-I01–I06 explicitly draft; no numerical or objective change proposed |
| U-09 saved-work scope | Specified | Session includes both plans/history/reviews; project-only clear-all, confirmation, Cancel, backup/recovery and failure tests required; runtime not tested |
| Food Truck parser, HTML, controls and state | Not run | No application exists; reference Python does not test JavaScript or accepted-input behavior |
| UI help, persistence/import/export/deletion | Not run | Future implementation contracts only |
| Pictures, actual graph interaction and printing | Not run | Asset/representation/print contracts only; source concept art is not finished app artwork |
| Physical iPad, school network and printer | Not run | No classroom acceptance session |
| Food Truck deployment | Not run | No HTML created or hosting configuration changed |

The reference suite runs with Python's standard library and exact Fraction arithmetic. It compares calculations with literal expected quantities and outcomes, uses itemized ingredient purchases to cross-check per-portion expenses, and enumerates integer sales to check break-even rounding rules. The 659 assertions include sold-all identity checks at each count 0–120 for all three prices; they are not 659 distinct classroom scenarios or browser tests.

Boundary fixtures cover zero/negative contribution, zero fixed expense, a threshold outside the displayed domain, exact outcome cutoffs, rounding that must not promote a failing waste fraction, zero-stock percentage handling, tied sales limits, Draft/Provisional precedence and separate transfer data. Non-core scenarios test proposed evaluator behavior only; they do not authorize a scenario editor or relaxed imports.

Run from the repository root:

```sh
python3 food-truck-business-launch/tests/verify_spec_reference.py
python3 docs/sources/dossier-v1.0.0/verify_reference_fixtures.py
```

## Design findings resolved in this draft

- Recipe scaling precedes the later stock screen. An early provisional stock selection, default 100, supplies the needed quantity; the later screen confirms/changes it and marks exactly affected work for recheck.
- Sold-all expense uses x; launch expense uses q. At the baseline, using 90 sold meals instead of 100 prepared overstates profit by $45.
- At $12, 60 meals break even and 61 first earn profit. At $15, the continuous crossing is 300/7; the first whole non-loss and positive-profit quantities are both 43.
- The $9 sold-all break-even at 100 is mathematically correct but unreachable in the three-hour event with capacity 96. Its correctly analyzed launch remains a legitimate rethink outcome.
- Stock changes do not alter v or F, so they must not erase or invalidate the sold-all functions/graphs. Price changes retain recipe and expense-only evidence.
- Plan A is frozen once; Plan B carries unchanged evidence with provenance and rechecks affected fields. Both are retained, and students can recommend either.
- Three cuisine identities share one visibly declared classroom costing model. No real recipe or market-demand inference is made.
- All three narrative endings are reachable. Students are not forced to optimize or to choose the canonical plan; negative profit remains a correct mathematical response when warranted.
- Prose and paper/oral transfer remain teacher-reviewed. Bypass and imported/carried-forward histories are distinguishable from current ordinary checks and independent work.

## Outcome feasibility

Counts assume required mathematics is current, no active bypass and all required submissions present.

| Business ending | Core price/stock combinations |
| --- | ---: |
| Festival success | 3 |
| Viable first launch | 4 |
| Business rethink | 5 |

Top-ending examples are $12/80 portions ($150 profit, no waste), $12/100 ($180, 10% waste) and $15/60 ($180, no waste). The permitted comparison can expose a genuine tradeoff instead of rewarding stock increases by default.

## Review and handoff

No material source conflict requires an immediate clarification. Draft decisions FT-I01–I06 are concrete and ready for owner review. Approval should identify this specification revision and its preserved commit before implementation begins. No handbook change is proposed.

This packet contains a specification, project brief, fixtures/checker and preparation evidence. It does not deliver a Food Truck application or claim that Road Trip's outstanding physical acceptance has been completed. Preserve the packet in GitHub; after approval, build the complete application, checkpoint it before extended verification, and report actual runtime results against its exact bytes.
