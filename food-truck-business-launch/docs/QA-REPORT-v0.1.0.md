# Food Truck v0.1.0 — application verification

30 September 2026. Disposition: development candidate verified in Linux Chromium; physical classroom acceptance pending. App 0.1.0 / content 1.0.0 / schema 1.0.0.

## Authorization and preserved source

Approved specification merged at `b1f9ae4158631043314e8a88e5f56549cebd319c`. First complete implementation preserved remotely at `a44afe23f95dac2126daa9caceb11fe69f5b8ce2`; corrected functional candidate at `3e8a4073c1544b48b60153f4e7721fdb3220d9cf`. Final print-background correction preserved locally at `7498f2c` before final browser verification; released source is the implementation PR head. Handbook v0.1.1 at `00cbde605ab08203b6b5fd2374d225155608fc29`.

Both HTML entry points are **101,711 bytes**, SHA-256 `93d0fde0e125fb68b96eeef14816ac51d2bc0ce2b03670bc005c767dbd26aae0`. The deterministic builder embeds all code, CSS and original SVG art. Road Trip and the dossier source package remain unchanged.

## Executed checks

| Evidence | Result / scope |
| --- | --- |
| Actual core suite | 216 assertions: all 12 plans and evaluators; exact arithmetic, equivalent rules/equalities, units and parser rejection; boundaries; dependent rechecks; A preservation; A or B recommendation; paper review/bypass/import; transactional rollback, conflicts and scoped deletion; history/revision/bundle limits |
| Full browser suite | 54 assertions: all eight stages, intentionally wrong then corrected cost, both plans, distinct revision, individual work, role swaps once, JSON export/reload/import, backup/clear/restore, ten help dialogs, diagnostics, print outputs, offline runtime and responsive widths |
| Browser edge suite | 26 assertions: all three endings plus Draft/Provisional, teacher bypass navigation/final submission, paper review, preserved A, fresh comparison, duplicates, conflict reload/copy, pre-delete backup, deletion, diagnostics export, native print dispatch, denied storage/export, 200% root text, inert imported markup, bounded malformed graph scales and import replacement cancellation |
| Independent preparation fixtures | 659 mathematical reference assertions; separate from the app tests |
| Original dossier fixtures | 77 reference checks; separate from app/device tests |
| Runtime network/errors | No external HTTP runtime requests and no uncaught page exceptions in offline browser suites |

Individual assertion names and outcomes are preserved in `verification/*-results.json`; synthetic exports are included. The main journey uses independently authored literal fixture answers. Edge outcomes use prepared state and actual rendered controls; they are not three separate full manual journeys.

## Print and visual review

Chromium-generated student PDFs: four pages each on A4 and Letter. Teacher reference: two pages each. Menu: one A4 page. Transfer slips: two A4 pages without answers. A near-maximum-length recommendation stays within four Letter pages. Inspectable PDFs and responsive screenshots are preserved. Rendered pages were inspected for graph labels, stacked exact fractions, table alignment, wrapping and page breaks. Student output excludes the separate teacher key. Native print dispatch was exercised with a test spy; PDFs were produced directly from the browser print CSS.

Layouts were checked at 1365×980, 768×1024, 1024×768 and 390×844; root-text enlargement at tablet width had no document overflow. These are Chromium emulations, not physical iPad/Safari or on-screen keyboard acceptance. Keyboard Escape/focus return and touch-capable controls were exercised. No claim of complete assistive-technology audit is made.

## Corrections found during verification

- Teacher bypasses now survive Next/Finish and unchanged Plan B export/import.
- Lesson role swaps occur once rather than again when revisiting a checkpoint.
- Glossary remains available when the tablet sidebar is hidden.
- Untrusted graph tick intervals are bounded to authored choices to prevent runaway rendering.
- Fractional coefficients retain their expression grouping in print; simple exact fractions stack.
- All printed page background is white; reference text spacing was clarified.

An initial browser-test failure was a file-input timing race in the test, corrected by waiting for the visible import-review heading. No history was discarded to pass tests.

## Remaining acceptance and deployment

Physical Safari iPad/on-screen keyboard, school network, physical A4/Letter/grayscale printer and classroom pilot remain pending. Menu/slips Letter and full grayscale output have not received separate visual acceptance. Browser storage remains device/origin-specific and may be cleared by browser settings; export is the portability/backup mechanism. Teacher tools and local evidence are intentionally not secure or tamper-proof.

Hosting is verified after merge using the served bytes, Pages workflow and actual live browser; see [the deployment record](DEPLOYMENT-v0.1.0.md). Passing local checks alone is not a deployment claim.
