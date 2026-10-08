# Mars Colony v0.1.0 — verification record

Date: 9 October 2026 (Asia/Shanghai). Source implementation checkpoint: `39bba7c`. Verified checkpoint: `9e7c69b`. The later integration merge preserves the exact tested application bytes and incorporates the unrelated Powers of Ten planning commits through `9562101`.

SHA-256 for both `index.html` and `MarsColony_v0.1.0.html`: `68a5c22ed59e007edfa3380162300c198c714d2261e2e412e0a080280e1d1854`.

## Actual results

115 automated assertions passed: 59 core, 39 browser, 17 edge. Raw results, screenshots, print PDFs and synthetic saved fixtures are in `verification/`. Tests are in `../tests/`. Environment: Linux, Node 24, Playwright with Chromium executable `/tmp/mars-chromium` (browser version recorded in JSON). This is desktop automation/tablet viewport emulation, not a physical iPad claim.

| Check | Result / evidence |
| --- | --- |
| Canonical numbers and equations | Passed: independent baseline, lean, extra-solar, weak housing/power fixtures; cost/cargo; battery recharge/caps; all field answer contracts |
| Exact/invalid responses | Passed: fractions, Unicode minus, separators; blanks/nonfinite/units/malformed values rejected; incorrect demand blocked, correct sibling retained |
| Learning path | Passed: all eight stages through both transfers and resilient report; narrative and task panels inspected |
| Weak designs/outcomes | Passed: Mission ready, Resilient outpost and Deployment delayed saved fixtures rendered; five arrays/no battery accepted |
| Dependencies/history | Passed: solar edit invalidates cost/storm/battery, preserves water forecast and original answer; first incorrect response survives export |
| Resources/graph | Passed: water, oxygen and food equations/tables/graphs; labeled units and stock caps |
| Save/reload/export/import | Passed: full workflow and copy import, backup recovery; wrong-project/schema/malformed rejection; same-schema earlier app version acceptance |
| Safe data/storage | Passed: imported HTML/script text inert; denied storage keeps memory work and export reminder; concurrent write detected, copy preserves newer stored record |
| U-09 deletion | Passed: Cancel, individual pair grouping, clear-all, persistence after reload, fresh creation, backup restore; unrelated Road Trip key survives |
| Offline/assets/help | Passed: no runtime network requests, no page exceptions; contextual help and Escape; no drag-only controls |
| Layout | Passed: screenshots inspected; no page overflow at 768×1024 and 1024×768; desktop 1365×1000 journey |
| Print | Passed: A4 and Letter PDFs generated, 8 pages each; A4 contact sheet inspected for visible content/units/graph/manifest/patch/evidence; physical output not tested |
| Launcher | Passed: Mars card generates QR offline pointing to the existing Netlify classroom URL; launcher version v0.1.1 |
| Package parity | Passed: versioned and hosted HTML byte-identical; visible title/version/credit consistent |
| U-10 | Not applicable: form-based project has no held/gameplay controls |
| Physical devices/network | Not run: iPad/Edge software keyboard, school-network reachability, physical QR scan, printer and classroom timing/participation |

Run: `node mars-colony/tests/core.test.cjs`; `CHROMIUM_PATH=/path/to/chromium node mars-colony/tests/browser.test.cjs`; corresponding `edges.test.cjs`. Browser executable must be available in the testing environment. The initial runtime's empty Chromium stub could not launch; a locally available packaged Chromium was extracted to a separate path, after which tests passed. No unrun check is counted as a pass.

Limitations: all model quantities are invented; daily energy accounting does not prove continuous operation. Prose and independent participation are teacher reviewed. Device-local saves have no cloud sync or protected teacher authentication. Hosted offline reopening after closing a tab is not promised. Exact installed-device acceptance remains pending.

GitHub persistence: CLI push lacked credentials, so connected GitHub Git Data API saved the identical trees. Canonical implementation checkpoint `39bba7c978c9e855221686ae508e17e399233662`; canonical verified checkpoint `9e7c69be705043ea3c41a78d178be41214dbcc94`. These preserve the tested source/artifacts from local checkpoints 1fca9b3/0a0c918; application hashes did not change.
