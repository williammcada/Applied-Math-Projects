# Mars Colony · Red Horizon

**A WILLIAM MCADA PRODUCT** · app 0.1.0 · content/schema 1.0.0

An applied-mathematics mission for 24 settlers over ten Earth days. Plan resources, housing, cargo and cost; model a stock; compare batteries and extra solar during a disclosed three-day disruption.

**Status:** Complete implementation candidate; core and in-process DOM checks pass. Real browser/print verification and deployment are pending. The complete approved scope is in [the specification](../docs/change-specs/MARS-COLONY-v0.1.0.md), with [approval](../docs/decisions/MARS-COLONY-v0.1.0-APPROVAL.md) and [project brief](docs/PROJECT-BRIEF.md).

Open `MarsColony_v0.1.0.html` in a desktop browser. `index.html` contains identical bytes for GitHub Pages. No installation, account, CDN or network service is required for core work. iPad delivery uses the hosted page; physical-device and school-network checks must be recorded separately.

Use aliases. Save locally and Export progress before changing devices or clearing browser data. JSON import creates a new copy; current answers are revalidated. Saved work supports session deletion and clear-all for Mars only. Export a backup before deletion; downloaded files and other apps are preserved.

Build from readable source with `python3 build.py`. Arithmetic and browser verification live in `tests/`. Do not rebuild an already verified candidate merely to recover from packaging or upload failure.

All equipment values and rates are invented classroom data. One day is 24 Earth hours. The model does not establish real life-support or continuous electrical operation. Correct mathematics can produce a weak design; the app accepts that analysis and names the failed criteria.

[Teacher guide](docs/TEACHER-GUIDE.md) · [Asset manifest](docs/ASSET-MANIFEST.md) · [Changelog](CHANGELOG.md) · [QA report](docs/QA-REPORT-v0.1.0.md) · [Deployment status](docs/DEPLOYMENT-v0.1.0.md) · [Verification commands](tests/README.md)
