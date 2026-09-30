# Theme Park Designer v0.1.0

**A WILLIAM MCADA PRODUCT**

Design a 60 × 40 m theme park, justify the mathematics, compare two plans, and test each partner's understanding. This self-contained application supports advanced Grade 5 / Saxon 8/7 work across scale, area, rotation, land allocation, fractions, percentages, and budgeting.

[Open Theme Park Designer](https://williammcada.github.io/Applied-Math-Projects/theme-park-designer/) · [Standalone HTML](ThemeParkDesigner_v0.1.0.html) · [Teacher guide](docs/TEACHER-GUIDE.md) · [Approved specification](../docs/change-specs/THEME-PARK-DESIGNER-v0.1.0.md)

## Start a project

1. Open the live application or download the HTML and open it in a desktop browser.
2. Choose **Start designing**, enter aliases and a park name, and follow the eight stages.
3. Use the field Help buttons when needed. Corrections are unlimited; first attempts, current answers, and assistance remain separate.
4. Place facilities by tap, drag, or coordinates. Paint land by cell or rectangle. Save inspected Plan A, revise, save Plan B, and explain a numerical tradeoff.
5. Complete separate A/B transfer tasks. Export progress at lesson boundaries and print the final report or scale map.

**Saved work** offers resume, JSON import/export, backup, snapshot/session deletion, and clear-all for this project. Browser storage belongs to the current device, browser profile, and origin. Exported JSON is the portable backup. No account, analytics, or student-data transmission is used.

The **Teacher** workspace includes answers, reference layout, diagnostics, reflection review, paper/oral transfer records, and logged bypasses. Teacher mode is a classroom convenience; it is not authenticated or tamper-proof. Bypassed work remains provisional.

## Print and device scope

Choose A4 or Letter. Print the scale map at **100%**, then measure its 5 cm calibration line. The site should measure 15 × 10 cm and each grid cell 5 mm. The student report, brochure, separate transfer slips, and teacher reference have dedicated print layouts.

The downloaded desktop application works offline. Reopening the hosted page offline is not guaranteed. Desktop Chromium and tablet portrait/landscape emulation were checked; physical iPad/Safari, software keyboard, school network, and measured printer acceptance remain pending. See the [QA report](docs/QA-REPORT-v0.1.0.md) and [deployment record](docs/DEPLOYMENT-v0.1.0.md).

## Source and reproduction

`src/core.js` contains exact rational arithmetic, geometry, evidence, and storage validation. `src/art.js` holds original SVG artwork. `src/ui.js` and `src/style.css` supply the interface and print layouts. `build.py` concatenates these into two byte-identical standalone HTML files; there are no runtime dependencies or external assets.

From the repository root:

```sh
python theme-park-designer/build.py
node theme-park-designer/tests/core.test.cjs
node theme-park-designer/tests/edges.test.cjs
# Browser tests require a separately installed Playwright and Chromium:
CHROMIUM_PATH=/path/to/chromium node theme-park-designer/tests/browser.test.cjs
CHROMIUM_PATH=/path/to/chromium node theme-park-designer/tests/edge-browser.test.cjs
```

The browser suites create local PDF/screenshot evidence under `docs/verification/`. The five `tests/ending-*.json` files are generated QA examples, not student records. Test dependencies are not shipped to learners.

[Project brief](docs/PROJECT-BRIEF.md) · [Release notes](CHANGELOG.md) · [Asset manifest](docs/ASSET-MANIFEST.md) · [Implementation notes](docs/IMPLEMENTATION.md)
