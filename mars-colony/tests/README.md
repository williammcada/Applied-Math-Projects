# Verification commands

Run from `mars-colony/` with Node.js 24+ and Python 3. The delivered HTML needs no installed packages. Development-only tools are `jsdom` 30.1.1 for in-process integration and Playwright with Chromium for browser testing. Install those in a separate test-tools directory and set `NODE_PATH` to its `node_modules` if they are not already available. Do not vendor dependencies into the standalone application.

```sh
python3 build.py
node tests/core.test.cjs
NODE_PATH=/path/to/test-tools/node_modules node tests/dom.test.cjs
NODE_PATH=/path/to/test-tools/node_modules node tests/browser.test.cjs
```

The browser suite uses Playwright's installed Chromium, or an explicitly provided `CHROMIUM_PATH`. A browser-launch permission failure is **Not run**, never a passing browser result. It was blocked in this execution environment; escalation was denied by policy. Run it only in an environment that permits browser processes.

`core.test.cjs` imports the actual mathematical engine. Its reference model independently uses integer tenths and manually authored field answers; it compares all 30,870 configurations and the required canonical scenarios. `reference-cases-v0.1.0.json` records the approved fixture values separately from the implementation.

`dom.test.cjs` executes the built HTML and real UI event handlers inside jsdom. Dialog, print, scroll, URL/download and file-chooser APIs are shimmed; storage is copied between separate instances. This checks workflow integration and serialization, **not** rendering, real browser storage/downloads, keyboard/touch, PDF layout, accessibility or device behavior.

`browser.test.cjs` is prepared for the actual file-based offline journey, variants, imports, deletions, responsive screenshots and A4/Letter PDF output. A passing run still requires visual inspection of screenshots and PDFs; emulated sizes do not substitute for a physical iPad.

Evidence goes in `docs/verification/`. Generated JSON fixtures use synthetic aliases only. Preserve a candidate checkpoint before extended testing, record its commit and SHA-256, and rerun affected checks after a source change. Do not mark the candidate verified until the required browser/print checks pass.
