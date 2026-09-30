# Road Trip Planner v0.1.0 — candidate verification

**Date:** 30 September 2026  
**Disposition:** Locally verified development candidate. Physical classroom acceptance and deployment remain pending.  
**App / content / save schema:** 0.1.0 / 1.0.0 / 1.0.0

## Exact candidate

| Record | Identity |
| --- | --- |
| Approved specification baseline | `c13f297e38552a241f9d9643cbeb0918003975ba` |
| Handbook consulted | `00cbde605ab08203b6b5fd2374d225155608fc29`, v0.1.1 |
| First implementation checkpoint, before extended tests | `04e5c7ec88b9ccdf9abc4f0ff48191ea241b694c` |
| Corrected application candidate, preserved before final verification | `c73bc879faa065a4d51f91c75d68e4157abecbce` |
| Candidate source tree | `b7c1265a92cf1efc7bf675acbd9252bdda82e6c1` |
| HTML SHA-256, both entry files | `fe3c5cbd3e0a5be5c67fd061e9302ef9c48c9d410e63395ef7987df2be1e9664` |
| HTML size, each | 120,686 bytes (about 118 KiB; below the 8 MiB target) |

Packaging adds documentation, a supplemental verification script, and preserved evidence only. It does not change the verified HTML or application source. The manifest records artifact hashes. The immutable specification/preparation reports remain historical rather than being overwritten with application-test claims.

## Environment and results

Linux x86_64; Node 24.19.0; Playwright 1.62.1; Chromium 153.0.8010.0. The application ran through the local file entry point with the browser context offline. Browser code reported zero uncaught page errors and zero external HTTP(S) asset requests.

| Suite | Result | Evidence |
| --- | --- | --- |
| Pure application engine, parser, state and storage | **662/662 passed** | [core results](verification/core-results.json), `tests/core.test.cjs` |
| Eight-stage browser journey, revision, transfer, saves, imports, deletion, conflicts and print | **55/55 passed** | [browser results](verification/browser-results.json), `tests/browser.test.cjs` |
| Teacher review/bypass, paper transfer, guided rule, weak endings, touch and storage failure | **16/16 passed** | [edge results](verification/edge-results.json), `tests/edge-browser.test.cjs` |
| Explicit replacement/cancel/backup, research conversion, fresh-session recovery and remaining controls | **12/12 passed** | [replacement results](verification/replacement-results.json), `tests/import-replacement.test.cjs`; unchanged application hash |
| Approved specification mathematics and all catalog outcomes | **259/259 passed** | `tests/verify_spec_reference.py`; historical reference fixtures retained |
| HTML identity | **Passed** | Same SHA-256 and bytes for `index.html` and `RoadTripPlanner_v0.1.0.html` |
| Student A4 / Letter print | **4 / 4 pages** | PDFs below; rendered pages inspected |
| Teacher A4 / Letter print | **2 / 2 pages** | PDFs below; rendered pages inspected |
| Separate A4 transfer slips | **2 pages** | One learner per page; no answers |

These are test assertions, not mastery scores or a statement that every device/browser has been tested. Test aliases and saved data are synthetic. The browser suites exercise rendered controls and downloads; they do not simply call the mathematical engine and call that a UI pass.

## Acceptance mapping

| ID | Result and concrete scope |
| --- | --- |
| RT-Q01 | Passed: all eight stages traversed; C01–C09 evidenced; optional researched-route mode does not block the provided route. |
| RT-Q02 | Passed: base, event, food revision and all 81 choices in both phases; route fuel and six-night convention preserved. |
| RT-Q03 | Passed: factored/expanded/reversed equivalents; wrong intercept/right single total, nonlinear terms, malformed separators, unsupported input and zero divisors rejected. |
| RT-Q04 | Passed: negative reserve and >100% spending accepted; half-up rounding and exact rational values checked. |
| RT-Q05 | Passed: four entered table values and four exact coordinate pairs, axes/scale/budget/rise checks, checked-line reveal. Responsive graph inspected; ordered-pair keyboard/touch entry remains the exact alternative to tap placement. |
| RT-Q06 | Passed in engine and ordinary browser path: between-day crossing, exact boundary, no affordable day and domain cap. The cap branch is directly tested; current fixed catalog/budget cannot reach 14 days. |
| RT-Q07 | Passed for exposed changes: hotel, food, route, alias, transfer and preserved event snapshots; unchanged siblings retain evidence. General budget/party/efficiency editing is not exposed in this release. |
| RT-Q08 | Passed: event applies once, survives resume, uses revised category prices, and blocks another choice until event comparison. |
| RT-Q09 | Passed: real rendered delighted/approved/revision/draft/provisional states; numerical preference cases and large-reserve feasibility checked. Prose review stays separate. |
| RT-Q10 | Passed: learner A/B responses separated; first incorrect versus corrected fuel evidence retained; paper submission requires a reviewer record and review remains pending until recorded. |
| RT-Q11 | Passed: reload, separate copy, newer-tab conflict/copy, denied storage, injected quota rollback, corrupt-record recovery and truthful save status. |
| RT-Q12 | Passed: single export, bundle backup/restore, import preview/default copies, malformed/wrong-project/future-version rejection, current “verified” re-evaluation, markup escaping, duplicate-ID rejection and atomic-write rollback. Named replacement, backup before replacement, cancellation with byte preservation, identity preservation and confirmed replacement also passed in the supplemental browser check. |
| RT-Q13 | Passed: deletion Cancel, scoped clear-all, backup restoration, corrupted-record deletion, unrelated app preservation and injected partial-deletion reporting. |
| RT-Q14 | Passed for the automated full journey and targeted controls: Help C01–C09/route, Escape/focus return, guided inputs, teacher review and bypass, export/duplicate/import/delete, proposal/reference/slips. This is not an exhaustive physical-device audit of every control. |
| RT-Q15 | **Partial:** desktop browser journey and 768×1024 / 1024×768 / 390×844 layouts passed without horizontal overflow. Touch-emulated teacher workflows, ≥44 px primary controls and 200% text reflow passed. **Physical Safari iPad, on-screen keyboard and school network not run.** |
| RT-Q16 | Passed for Chromium PDF: four-page student and two-page teacher A4/Letter views, two transfer slips, native text, stacked fractions, vector graph, labels and separate keys. Rendered pages inspected after fixes. **Physical printer/grayscale acceptance not run.** |
| RT-Q17 | Passed: full offline file journey, no external requests, imported markup inert in preview and app, no runtime assets outside HTML. |
| RT-Q18 | Passed: original inline assets registered and home/choices/outcome layouts inspected; actual itinerary data supplies outcomes; size measured above. |
| RT-Q19 | Passed: app/content versions agree, guide/notes/briefs updated, both HTML files identical; reproducible build retained. |
| RT-Q20 | **Not run / delivery blocked:** repository metadata reports `has_pages: false`; the connector rejects the Pages settings endpoint and exposes no Pages configuration tool. No live URL, hosted-version match or deployed save/print check is claimed. |

## Defects found and corrected before the final pass

1. A control refresh could discard another field's partially typed value. Raw input is now retained in memory immediately, while checking remains explicit.
2. A default SVG fill produced a black triangular graph area in print. Axes/grid paths are unfilled. Unique clip references isolate the print graph from its preview copy, and the printed page background is white.
3. Incomplete route text could be classified as an unreadable save. It remains resumable at the route desk, with downstream navigation blocked until consistent.
4. Paper/oral mode alone could appear complete. An actual reviewer submission record is now required.
5. Local resume previously set the imported marker. Only an actual import adds that marker.

The corrected checkpoint was preserved, then the final suites were run. No known failing automated checks remain. The explicit not-run items above prevent a classroom-ready or deployed-release claim.

## Preserved visual evidence

- [Welcome screenshot](verification/home.png)
- [Student A4 proposal](verification/student-A4.pdf)
- [Student Letter proposal](verification/student-Letter.pdf)
- [Teacher A4 reference](verification/teacher-A4.pdf)
- [Teacher Letter reference](verification/teacher-Letter.pdf)
- [Individual transfer slips](verification/transfer-slips.pdf)
- [Verification manifest](verification/verification-manifest.json)

## Next delivery / acceptance steps

Enable GitHub Pages only after inspecting the repository settings, using the intended repository root source and `/road-trip-planner/` entry path. The repository connector cannot perform that settings operation; browser fallback requires user approval. After publishing, fetch and compare the actual served HTML hash/version and spot-check save/export/import and print at the real subpath. Preserve this candidate rather than rebuilding it to solve a delivery problem.

On a physical iPad at school, verify Safari portrait/landscape, on-screen keyboard visibility, touch graph/input/help, resume/export/import, and the printer workflow. Repeat the backup/replacement drill on that device. Record observed results separately; browser emulation does not establish those facts.
