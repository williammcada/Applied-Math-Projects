# Powers of Ten v0.1.0 — Deployment record

**A WILLIAM MCADA PRODUCT**

[Open Powers of Ten](https://williammcada.github.io/Applied-Math-Projects/powers-of-ten/) · [Versioned standalone HTML](https://williammcada.github.io/Applied-Math-Projects/powers-of-ten/PowersOfTen_v0.1.0.html)

Status: deployed development release candidate; actual hosted bytes and browser operations verified. Physical classroom acceptance remains pending.

| Item | Recorded identity |
| --- | --- |
| App / content / schema | 0.1.0 / 1.0.0 / 1.0.0 |
| Corrected candidate | `db069a8c487cd7f6e263ed8068925df8b7102855` |
| Automated verification checkpoint | `5506401f906c11bfab6e750251c81893dec86d28` |
| Release commit | `dcbf2d71b7084ab221162015f432846408a61f12` |
| Main baseline used by release | `ba66eef6840363451b4c815ac7eb20795806200c` |
| Each hosted HTML | 106,044 bytes |
| Both HTML SHA-256 | `d9a042236b8968cc172f17fb64cfeb564967b77434259a06192ffbbf4de0a7ac` |
| Hosted checks completed, UTC | 2026-09-30T08:24:30.040Z |

## Observed deployment

The existing repository Pages workflow publishes the main branch. The release added the `powers-of-ten/` application and its records, with additive family-document links. A Git diff against the release parent confirmed that only Powers of Ten paths and the four intended specification/index documents changed. No other project's application file was modified.

The initial Pages run [36689221287](https://github.com/williammcada/Applied-Math-Projects/actions/runs/36689221287) was superseded/cancelled as a concurrent Theme Park release advanced main to `d7f5bba79c0dd104bf80d0ab78ee0a158a31bd02`. That commit retains the exact Powers of Ten candidate. Successful publication is established here by the actual HTTPS responses and browser checks, not by treating the cancelled workflow as successful. Later evidence-only commits leave the app bytes unchanged.

## Hosted verification — Passed 10, Failed 0

- Both live HTML routes returned HTTP 200 and the exact candidate length/SHA-256.
- App title/version and embedded SVG were present.
- A fresh synthetic session saved, reloaded and resumed at the expected stage.
- Actual JSON export downloaded the synthetic record; actual file import created a separate copy.
- The selected build-sheet preview rendered and invoked print; a hosted Letter PDF was produced.
- Built-in diagnostics passed, no page errors were observed, and no unexpected runtime requests were made.
- Existing Road Trip and Food Truck hosted entry points still returned HTTP 200.

See `tests/hosted-results.json` and `tests/hosted.test.cjs`. Runtime behavior was exercised in headless Chromium 153.0.8010.0 with a fresh browser context. The workspace requires an HTTPS proxy; the test browser accepted that proxy certificate. Separate Python HTTPS reads using the environment's normal certificate trust also verified both lengths and hashes. This test setup does not change the application or the public site's TLS configuration.

## Release limits and recovery

Physical iPad Safari/keyboard, managed school network, actual printer calibration, assembled 600 mm paper strip, real student models and classroom pacing are **Not run**. Reports of synthetic reviews are test fixtures, not physical inspection evidence. See the QA report and teacher guide before classroom acceptance.

Recover the exact candidate from its checkpoint and compare the SHA-256 above. The downloadable ZIP contains the same HTML plus source, test fixtures, specification, answers and release records. Only the HTML is required to run the app. Repack preserved bytes after any delivery failure; do not rebuild the application merely to recreate a download.
