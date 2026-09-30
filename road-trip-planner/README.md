# Road Trip Planner v0.1.0

**A WILLIAM MCADA PRODUCT · William McAda**

A self-contained applied-mathematics activity for advanced Grade 5 / Introduction to Pre-Algebra. Pairs plan a seven-day trip, build and interpret a linear cost model, respond to a changed hotel quote, and complete separate transfer tasks.

## Candidate status

The complete application is implemented and verified in the environments listed in [QA-REPORT-v0.1.0.md](docs/QA-REPORT-v0.1.0.md). This is a development candidate, not a claim of physical iPad or school-network acceptance. GitHub Pages is not enabled yet.

- Application: **0.1.0**
- Content and initial save schema: **1.0.0**
- Approved specification: [revision 1](../docs/change-specs/ROAD-TRIP-PLANNER-v0.1.0.md)
- First implementation checkpoint: `04e5c7ec88b9ccdf9abc4f0ff48191ea241b694c`
- Verified application candidate: `c73bc879faa065a4d51f91c75d68e4157abecbce`

## Open the application

Download [RoadTripPlanner_v0.1.0.html](RoadTripPlanner_v0.1.0.html) and open it in a modern desktop browser. No installation, network, accounts, external fonts, or other files are needed. [index.html](index.html) is byte-identical and is the intended hosted entry point.

For an iPad, use the hosted page after deployment. Physical Safari and the actual school network must still be checked. The intended Pages path is `/Applied-Math-Projects/road-trip-planner/`; it is not currently a verified live URL.

Start with an alias, assign Planner/Checker roles, and work through the eight named stages. Use a teacher-supplied calculator on fields marked “Calculator allowed.” Help uses different-number examples. Incorrect mathematics can be revised without erasing earlier attempts; correct mathematics can describe a weak or over-budget plan.

## Save and move work

Save writes to this browser's Road Trip storage. Export progress after each lesson and before changing devices. The JSON file includes answers, attempts, event snapshots, help, overrides, and reviews. Import previews a whole file before applying it; importing as new copies is the default.

Saved work provides Resume, Duplicate, Import, Export backup, Delete and Clear all Road Trip sessions. Deletion names its scope and includes Cancel and a backup option. Downloaded files and other applications are not deleted. If storage is unavailable, keep the page open and export. A newer session in another tab offers Reload or Save as copy.

Teacher mode is a local classroom control, not secure authentication. Arithmetic checks, reasoning reviews, paper/oral submissions, and logged bypasses remain distinct. Imported history is labeled and does not certify independent mastery.

## Print

Preview / print proposal produces four student pages. Teacher mode provides a separate two-page reference; transfer slips are separate, one learner per page. Use A4 or Letter portrait, 100% scale, with browser headers/footers disabled. The app prints native text and vector mathematics/graphs.

See the [teacher guide](docs/TEACHER-GUIDE.md), [asset manifest](docs/ASSET-MANIFEST.md), [release notes](CHANGELOG.md), and [QA report](docs/QA-REPORT-v0.1.0.md).

## Development

`src/core.js` contains exact rational arithmetic, the safe linear-expression parser, dependency checks, state validation and local storage. `src/ui.js`, `src/style.css`, `src/art.js`, and `src/template.html` contain the experience. None are separate runtime dependencies of the built HTML.

```sh
python3 build.py
node tests/core.test.cjs
python3 tests/verify_spec_reference.py
```

Browser tests require Playwright and Chromium in the development environment only:

```sh
PLAYWRIGHT_MODULE=/path/to/playwright CHROMIUM_PATH=/path/to/chromium node tests/browser.test.cjs
PLAYWRIGHT_MODULE=/path/to/playwright CHROMIUM_PATH=/path/to/chromium node tests/edge-browser.test.cjs
PLAYWRIGHT_MODULE=/path/to/playwright CHROMIUM_PATH=/path/to/chromium node tests/import-replacement.test.cjs
```

Set `QA_OUTPUT` to choose where test screenshots, PDFs and diagnostic fixtures are written. Tests use synthetic aliases. Runtime assets are original inline SVGs; no map API or tracking runs in the application.
