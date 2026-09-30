# Food Truck / Business Launch v0.1.0

**A WILLIAM MCADA PRODUCT · William McAda**

[Open the app](https://williammcada.github.io/Applied-Math-Projects/food-truck-business-launch/) · [Standalone HTML](FoodTruck_v0.1.0.html) · [Teacher guide](docs/TEACHER-GUIDE.md) · [QA report](docs/QA-REPORT-v0.1.0.md)

An independent classroom project for pairs: scale a recipe, set a price, build business functions, forecast a festival launch, account for unsold stock, and compare a revision. Eight stages, ten checkpoints, three menu identities and all twelve price/stock combinations. A correctly analyzed loss is valid work.

Open `index.html` or the byte-identical `FoodTruck_v0.1.0.html` in a modern browser. No installation, account or external asset is required. Use aliases. Save locally and export JSON before changing devices or clearing browser data. Each session preserves both plans and its evidence history. Teacher controls provide paper/oral review, provisional bypasses, references and transfer slips.

## Development and verification

```sh
python3 food-truck-business-launch/build.py
node food-truck-business-launch/tests/core.test.cjs
python3 food-truck-business-launch/tests/verify_spec_reference.py
```

Browser suites `tests/browser.test.cjs` and `tests/edges.test.cjs` require Playwright and Chromium; set `PLAYWRIGHT_MODULE` and `CHROMIUM_PATH` for the installation. The app itself has no dependencies. Sources live in `src/`; run the builder after editing. Do not independently edit one generated HTML file.

- [Approved implementation specification](../docs/change-specs/FOOD-TRUCK-v0.1.0.md)
- [Approval record](../docs/decisions/FOOD-TRUCK-v0.1.0-APPROVAL.md)
- [Project brief](docs/PROJECT-BRIEF.md)
- [Asset manifest](docs/ASSET-MANIFEST.md)
- [Original dossier](../docs/sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md), sections 18–22

Physical iPad/Safari, school-network and printer acceptance remain pending. Local Chromium emulation and PDFs are separate evidence.
