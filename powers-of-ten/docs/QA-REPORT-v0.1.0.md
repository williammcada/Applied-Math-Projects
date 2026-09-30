# Powers of Ten v0.1.0 — QA report

**A WILLIAM MCADA PRODUCT** · 30 September 2026

Status: automated verification of the development release candidate. Physical classroom acceptance remains pending. This report does not label the application a fully verified physical-device release.

## Candidate identity and provenance

- Approved specification: `docs/change-specs/POWERS-OF-TEN-v0.1.0.md`, revision 1; user authorized production.
- Implementation baseline: `d728dff8f8553f7db5cd26304d9bc403ad790ad9`.
- Approval checkpoint: `21d5573d4ec69bdb59f92800e725498d43d9808a`.
- Initial implementation checkpoint: `9c107bb283cee735d99f5472fadb316e4ad32a6d`.
- Corrected candidate checkpoint tested after preservation: `db069a8c487cd7f6e263ed8068925df8b7102855`.
- Candidate tree: `7020c4ec4a01a77d3dc2f5342a2b13136ab6f7e1`.
- App 0.1.0; content/schema 1.0.0; each HTML 106,044 bytes.
- Both HTML files SHA-256: `d9a042236b8968cc172f17fb64cfeb564967b77434259a06192ffbbf4de0a7ac`.

The remote checkpoint was fetched and its HTML bytes compared with the local candidate before the final automated run. Packaging and documentation must reuse these bytes. The original dossier and other projects' application files are unchanged by this release.

## Observed verification

Linux, Node, Playwright and headless Chromium 153.0.8010.0. A local HTTP server and direct `file://` opening were both used. Viewports were emulated, not physical devices. All reviewer names and dimensions in fixtures were synthetic and explicitly labeled. Independent expected literals live in `tests/fixtures.cjs`; they are not generated from the app's answer table.

| Suite | Result | Evidence |
| --- | --- | --- |
| Exact evaluators, evidence, save/import/delete | Passed: 221; Failed: 0 | `tests/core-results.json`, `core.test.cjs` |
| Browser journey, layouts, print modes, offline | Passed: 98; Failed: 0 | `tests/browser-results.json`, `browser.test.cjs` |
| Denied storage, recovery, injection, long print, keyboard, conflict | Passed: 7; Failed: 0 | `tests/edges-results.json`, `edges.test.cjs` |
| HTML identity | Passed | `tests/candidate-identity.json`; byte comparison with remote candidate |
| PDF geometry/layout | Passed within digital rounding | `tests/print-results.json`; visual review described below |
| Hosted deployment | See deployment record | `docs/DEPLOYMENT-v0.1.0.md`, `tests/hosted-results.json` |

The browser suite traversed Track B from a blank session through incorrect answers, all common mathematics, scale planning, build confirmation, a correctly reported physical mismatch, correction, gallery, separate transfers, pending review and synthetic accepted reviews. It also rendered a complete Track A fixture. Pure tests cover both tracks, tolerance endpoints and just-outside values, equivalent ratios, alternative common powers, stale dependencies, track restoration, outcome predicates, and first-response preservation.

Recovery tests exercised denied/quota-style storage failures, atomic rollback on index failure, invalid imports, newer-tab conflict, per-session and app-scoped deletion, cancellation, backup/export and new work. Imported HTML text remained inert. Actual download/upload paths were used. Local classroom review controls are deliberately not authentication or anti-tamper security.

## Specification acceptance map

“Passed” below applies only to the stated automated/read-through scope. Unrun physical requirements are separated below.

| IDs | Status | Evidence / scope |
| --- | --- | --- |
| SN-Q01–Q05 | Passed | Twelve objectives/eight stages represented; eight operations on both tracks; literal reference answers, intermediate steps, normalization, tiny quantities, notation parsing, units and ratio direction checked |
| SN-Q06–Q08 | Passed | Inclusive exact tolerances; correct mismatch reports; build/plan invalidation; retained sibling and transfer evidence; original attempts preserved |
| SN-Q09–Q10 | Passed | All five outcome predicates; pending/accepted/repair review records; paper transfers; teacher/peer role restrictions; bypass replaced by genuine recheck with history retained |
| SN-Q11–Q13 | Passed | Save/reload/resume/copy, import/export validation, conflict/rollback, confirmed deletion and preservation of another app's storage |
| SN-Q14 | Passed | Desktop DOM journey, keyboard help/Escape/minus, calculator, review, all active help paths; physical touch testing remains Not run |
| SN-Q15, emulated portion | Passed | All eight stages at 768×1024, 1024×768 and 390×844; 200% zoom reachability check; visual inspection of title, operations, plan and outcome |
| SN-Q16, digital portion | Passed | 28 PDFs across seven modes, both tracks and A4/Letter; selectable text, source/credit, no teacher-reference leakage; long response continuation; digital dimensional checks |
| SN-Q17–Q19 | Passed | Embedded SVG, no runtime external requests, standalone opening, no observed browser exceptions, inert imported strings, pure diagnostics, byte/version agreement |
| SN-Q20 | See deployment record | Actual Pages subpath, served HTML hashes and hosted browser operations are recorded separately |

## Print inspection

Standard reports are four pages on both A4 and Letter. A bounded long interpretation/visitor/review fixture creates a fifth page with a repeated gallery continuation label. Build sheet, placard and visitor passport are each one page; transfer slips two; teacher reference three; cell template one; Earth–Moon templates four. The browser test produced all 28 combinations.

Rendered pages were visually inspected for readable exponents, table wrapping, page breaks, intact cell guide, distance strip and calibration fit, source labels and continuation text. Grayscale remains understandable through text and outlines, not status color alone. The 50 mm PDF line measured approximately 49.988 mm, and a 200 mm distance segment approximately 199.986 mm. Those measurements establish digital geometry only, not output on paper. Exact reproducible values and page counts are in the print-results file.

## Required physical acceptance — Not run

- Physical iPad Safari in portrait/landscape, touch targets and on-screen keyboard reachability.
- Actual school-network availability and any managed-browser restrictions.
- Real A4/Letter printer settings, grayscale output, 50 mm calibration and assembled 600 mm strip measured by ruler.
- Real student-built models, independent human inspection and learner work.
- Classroom pacing, accessibility with learners and assistive-technology use.

No observed automated failures remain in the preserved candidate. These unrun checks limit the release claim; headless/emulated/PDF results do not substitute for them.

## Reproduce and recover

See README commands. Playwright and a compatible Chromium are test-only dependencies. The temporary test artifacts are regenerated under `SN_ARTIFACT_DIR`; the source, result summaries and synthetic saved scenarios are preserved in Git. `tests/export-fixtures.cjs` generates twelve labeled valid scenarios and an intentionally malformed import file. Never represent fixture measurements or review notes as real observations.

Restore the candidate commit to recover exact runtime bytes. Do not rebuild merely because packaging or download delivery failed. After a runtime change, create a new checkpoint and rerun affected verification before carrying forward any pass claim.
