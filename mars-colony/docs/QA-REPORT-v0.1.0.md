# Mars Colony v0.1.0 — QA Report

**Implementation candidate; verification incomplete. Not a verified release.**

App 0.1.0 · content/schema 1.0.0 · 30 September 2026.

## Candidate and source

- Approved specification revision 1: `docs/change-specs/MARS-COLONY-v0.1.0.md`; approval commit `4b7134293e4596ff9eb9edfd7857c7cf9afd7407`.
- Source intake: `d728dff8f8553f7db5cd26304d9bc403ad790ad9`.
- Initial complete implementation checkpoint: `87a7f7b1097d1d1cf7b2a24877827ee1dd021d21`.
- Corrected implementation checkpoint: **779b0b1f551d23c54eedca6eec7d04e5218dc70d**. This is not a verified checkpoint.
- Concurrent main preserved through `ba66eef6840363451b4c815ac7eb20795806200c`; other applications are unchanged by the Mars work.
- Artifact identity: [SHA-256 and structural checks](verification/artifact-checks.json).

## Performed checks

Core verification uses Node.js v24.19.0, the actual engine, an independently authored integer-tenths reference model, explicit approved fixtures and manually calculated field answers. It compares all 30,870 permitted configurations. DOM integration executes the actual built HTML in jsdom 30.1.1 with synthetic aliases.

Current runs: **257 named core checks**, **30,870 configuration comparisons**, **72 in-process DOM checks** passed. Enumerated outcomes: 2 Resilient outpost, 3 Mission ready, 30,865 Deployment delayed. [Core results](verification/core-results.json), [DOM results](verification/dom-results.json), [independent fixtures](../tests/reference-cases-v0.1.0.json) and test source retain the assertions and expected values.

The DOM harness substitutes dialog open/close, scrolling, printing, object-URL downloads and file selection. It copies serialized storage between isolated instances. Export/import checks inspect Blob contents and actual UI handlers. This does **not** establish real downloads, browser storage behavior, layout, keyboard/touch, accessibility-tree behavior, PDF output or offline browser operation.

| Requirement | Result for recorded scope | Evidence and remaining work |
| --- | --- | --- |
| QA-01 objectives/gates | Passed in core/DOM | All ten groups; eight-stage standard journey, lean revision, separate transfer and incorrect-answer blocking. |
| QA-02 numeric fixtures | Passed | MC-F01–13 explicit values plus MC-F14 state cases; independent exhaustive configuration comparison. |
| QA-03 input boundaries | Passed for listed core/DOM cases | Blank/malformed/nonfinite/huge input, invalid counts, incorrect daily demand and blocking feedback. Device input methods remain Not run. |
| QA-04 equivalent forms | Passed | Exact decimals/fractions and equivalent linear expressions; incorrect model does not pass with a correct total. |
| QA-05 scientific notation | Not applicable | Outside Mars core. |
| QA-06 weak designs | Passed in core/DOM | Correct no-battery design reaches delayed and identifies day-4 6 kWh shortage. Other failures checked mathematically. |
| QA-07 dependencies | Passed for recorded cases | Solar invalidates power/battery/manifest; lean invalidates manifest/comparison but retains water. Full browser dependency matrix remains Not run. |
| QA-08 first/corrected work | Passed in core/DOM | Initial 0.8 oxygen error and later 19.2 correction retained; initial plan and role swaps retained. |
| QA-09 persistence | Passed for core/DOM scope | Revision conflict, copied-storage resume, multiple sessions; real browser reload/storage denial/quota remain Not run. |
| QA-10 progress round trip | Passed in core/DOM | All three resource selections; UI serialization/import preview and backup recovery. Actual chooser/download remains Not run. |
| QA-11 compatibility | Passed for listed cases | Compatible app patch accepted; wrong project/future schema/hostile/invalid state rejected atomically. First Mars schema; legacy migration Not applicable. |
| QA-12 artwork/offline | Passed for source/artifact inspection | Required inline SVGs and embedded scripts/styles, no external runtime resource tags. Actual offline browser journey Not run. |
| QA-13 help/access | Passed in DOM; device checks Not run | All ten help groups respond; graph points are typed. Real focus/keyboard/touch still requires observation. |
| QA-14 responsive layout | Not run | Prepared suite covers 768, 1024 and 1440 px. No browser screenshots exist. Physical iPad and software keyboard are separate. |
| QA-15 print | Content checks passed; layout Not run | Report/reference/patch/slips generated; slips omit answers; print handler invoked. A4/Letter PDF, clipping, page numbers and physical printer remain Not run. Calibration templates Not applicable. |
| QA-16 endings | Passed in core/DOM | Both resilient strategies, lean ready cases, delayed, stale Draft and transfer-bypass Provisional. |
| QA-17 teacher evidence | Passed in core/DOM | Paper review, oral response, logged bypass and separate mastery language. |
| QA-18 hostile/corrupt data | Passed for listed core/DOM cases | Hostile/unknown fields rejected, rendering escapes text, wrong-project import atomic. Full browser recovery matrix remains Not run. |
| QA-19 privacy | Passed in source/content inspection | Aliases, local state, no telemetry/service and explicit nonsecure teacher controls. |
| QA-20 artifact/version | Passed for candidate | Byte-identical HTML/index; version agreement; actual changes and gaps documented. Not release approval. |
| U-09 deletion | Passed in core/DOM | Cancel, clear-all, no unload resurrection, cross-tab deletion/export, backup restore, other-project data retained. Real browser event/reload behavior remains Not run. |
| Hosted route | Not run | No Mars merge to main, release tag or deployment. |
| Physical iPad/network/printer | Not run | Actual intended equipment required; emulation is separate evidence. |

## Browser blocker

Chromium failed before opening a page with `socket() failed: Operation not permitted`. A request to launch outside the restrictive sandbox was rejected by automatic approval policy (`sandbox_approval: false`). No browser screenshots, PDFs or passing browser-results file were produced. No sandbox bypass was attempted after rejection.

`tests/browser.test.cjs` is prepared but unexecuted. DOM evidence must not be relabeled as browser verification. Completing browser checks requires a permitted environment; cloud-browser fallback requires approval under the tool's fallback rules.

## Verified corrections within available scope

Draft reports hide unchecked revised totals. Active C10 bypasses make the outcome Provisional. Deleting active work clears autosave state, including partial-delete handling. New-mission save failures preserve/export-prompt existing work. Fresh revision starts a new evidence history. Malformed cross-tab state shows recovery guidance. System diagrams distinguish production, consumption and stored quantities; field metadata identifies objective/source/evaluator/representation/precision/review policy.

## Release gate

Preserve the candidate. Run browser workflows in a permitted environment and inspect screenshots and every A4/Letter PDF, including the long response record. Check keyboard/focus, touch emulation, storage failure/corruption and remaining dependency variants. Fix failures, checkpoint and rerun affected tests. Only then record a verified checkpoint, merge/package exact bytes and verify the actual GitHub Pages route. Keep physical iPad, school network and printer gaps separate until observed.
