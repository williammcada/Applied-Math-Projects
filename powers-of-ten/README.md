# Powers of Ten v0.2.0

**A WILLIAM MCADA PRODUCT** · Content and save schema 1.0.0

[Open the application](https://mcada-applied-math.netlify.app/powers-of-ten/) · [Standalone HTML](PowersOfTen_v0.2.0.html) · [Teacher guide and answers](docs/TEACHER-GUIDE.md) · [QA evidence](docs/QA-REPORT-v0.1.0.md) · [Deployment record](docs/DEPLOYMENT-v0.1.0.md)

One 40-minute Science lesson builds a model and produces a saved Science Evidence Passport. A second Mathematics lesson reuses those observations for notation, all four operations, intended and observed scale, deviations, limitations and individual exits. Classroom timing and physical iPad checks remain unverified.

[Science guide](docs/SCIENCE-GUIDE-v0.2.0.md) · [Mathematics guide](docs/MATHEMATICS-GUIDE-v0.2.0.md) · [Coordination sheet](docs/COORDINATION-v0.2.0.md) · [v0.2 QA](docs/QA-REPORT-v0.2.0.md)

Use the hosted link on an iPad. On a desktop, download and open `PowersOfTen_v0.2.0.html` in a current browser. The HTML includes every script, style and illustration; no installation or runtime network is required. Optional science-reference links open external sources.

Enter a team alias and two different learner aliases, then follow the stages. Choose the 160 mm cell enlargement or the 600 mm Earth–Moon desktop model. Both tracks require the same eight scientific calculations. Measure a real model: the application never fills in an invented measurement. A teacher or peer inspects the model; a teacher reviews the interpretation. Software checks arithmetic and recorded evidence, not whether a physical measurement is truthful.

Use **Save**, **Sessions** and **Export progress**. Browser storage is specific to the browser and location; private mode or device cleanup can remove it. JSON exports are the portable backup. Imports default to new copies; replacing records requires confirmation. Deletion applies only to this app. Use aliases, since exports contain responses, assistance and review histories. There is no server, account, telemetry, gradebook integration or automatic submission. Teacher controls are local and are not secure assessment authentication.

The print menu includes student reports, build sheets, calibrated templates, exhibit placards, visitor passports and separate answer-free transfers. Teacher reference pages are available from the teacher desk. Print templates at **100% / actual size**, with browser headers/footers off. Measure the 50 mm calibration line before use, then measure the completed model. Do not use a responsive on-screen drawing as a ruler.

This is a deployed development release candidate with automated verification. Physical iPad Safari/keyboard, the school network, actual printer calibration and classroom use remain unverified. See the QA report for exact scope.

## Maintenance

`src/core.js` contains exact rational evaluators and evidence/storage rules; `src/ui.js` contains the interface and print views; `src/art.js` contains original SVG illustrations. Build without dependencies:

```sh
python3 powers-of-ten/build.py
node powers-of-ten/tests/core.test.cjs
```

The build writes byte-identical versioned HTML and `index.html`. Browser tests use Node and Playwright; set `SN_CHROMIUM_PATH` when using a separately installed compatible Chromium. `SN_ARTIFACT_DIR` optionally selects the temporary PDF/screenshot directory.

```sh
node powers-of-ten/tests/browser.test.cjs
node powers-of-ten/tests/edges.test.cjs
node powers-of-ten/tests/export-fixtures.cjs
```

Synthetic fixtures are explicitly labeled and are not physical observations or learner records. Test answer literals are independent of the application's expected-answer table. Build dependencies are never required by a learner's HTML.

Source authority: [approved specification](../docs/change-specs/POWERS-OF-TEN-v0.1.0.md), [approval](../docs/decisions/POWERS-OF-TEN-v0.1.0-APPROVAL.md), and [project brief](docs/PROJECT-BRIEF.md). Preserve the original dossier and other subprojects when updating this app.


Current checks: `node tests/v2-core.test.cjs` and `node tests/v2-browser.test.cjs` (from powers-of-ten). Older v0.1 tests/results and standalone HTML remain historical evidence. See [schema](docs/SCHEMA-v2.md) for migration and handoff contracts.
