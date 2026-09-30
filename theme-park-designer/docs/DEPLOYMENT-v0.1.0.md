# Theme Park Designer v0.1.0 — Deployment Record

**State:** Deployed and hosted workflow verified on 30 September 2026 at 08:27 UTC. Physical classroom acceptance remains pending.

Live application: https://williammcada.github.io/Applied-Math-Projects/theme-park-designer/

Standalone download: https://williammcada.github.io/Applied-Math-Projects/theme-park-designer/ThemeParkDesigner_v0.1.0.html

GitHub Pages uses the repository's existing main/root publication. The tested `index.html` and `ThemeParkDesigner_v0.1.0.html` are byte-identical, 105,803 bytes each, with SHA-256 `c3e9dbe937919751c99925a82be16fe2d45c1797d40e4b13ea8e0e03ce4ed6d9`. Corrected candidate checkpoint: `e1c81fc17a5da727e7bf35feeb4b79770a03f394`.

## Checkpoints and publication

| Stage | Evidence |
| --- | --- |
| DESIGN / CHANGE SPEC | Approved specification and authorization commit `af8a48d83f93e846aa77da61de254a06018096bd` |
| IMPLEMENT / CHECKPOINT | Initial implementation preserved at `39c4981394c28c89f22f7e23d6f040b932edbb61` before testing |
| Corrected candidate | `e1c81fc17a5da727e7bf35feeb4b79770a03f394`, preserved before final verification |
| VERIFY / VERIFIED CHECKPOINT | 189 local assertions; A4/Letter audit; `35ece958a2b309ff580758a26536c4cc40ce1247` |
| RELEASE | `d7f5bba79c0dd104bf80d0ab78ee0a158a31bd02` merged the exact project tree into current main, preserving concurrent project changes |
| DEPLOY | [Pages run 36689353747](https://github.com/williammcada/Applied-Math-Projects/actions/runs/36689353747) completed successfully |
| Hosted observation | [12 passing assertions](verification/hosted-results.json), no failures, at 08:27:12 UTC |

The public index and versioned download both returned HTTP 200 and the exact SHA-256 above. The page displayed v0.1.0 and the embedded park artwork. An isolated browser session created a design, entered aliases and a scale answer, saved, exported a real progress file, reloaded/resumed with the answer intact, and imported the file as an independent copy. Hosted diagnostics passed. No uncaught exceptions or separate runtime asset requests were observed.

The hosted browser used Linux Chromium 153.0.8010.0 and the execution environment's configured outbound proxy. Its temporary test context used a certificate exception for that proxy; a separate curl retrieval used the environment's normal CA validation and independently matched the public hash. No certificate exception or test dependency is part of the delivered application. This verifies the public runtime, not physical iPad/Safari behavior.

Reproduce the hosted workflow with `tests/hosted.test.cjs` after setting `CHROMIUM_PATH` to an installed Chromium executable. `QA_PROXY_TLS_EXCEPTION=1` is only for an isolated test environment whose configured proxy certificate is absent from Chromium's trust store; normal browser use does not require it.

This evidence update changes documentation and test records only. The tested application bytes remain unchanged.

If publication fails, recover the preserved candidate. Do not reconstruct the application during packaging or deployment. Physical iPad/school-network/printer acceptance remains separate and pending.
