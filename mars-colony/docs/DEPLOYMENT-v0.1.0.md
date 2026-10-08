# Mars Colony v0.1.0 — deployment record

Target: https://mcada-applied-math.netlify.app/mars-colony/

GitHub canonical source: williammcada/Applied-Math-Projects main. Existing Netlify connection publishes repository root; no build command. `mars-colony/index.html` is the entry point; standalone artifact is byte-identical. Root launcher v0.1.1 adds Mars card/QR; other four app links retained.

Verified source checkpoint: 9e7c69b (115 local assertions). Artifact SHA-256: 68a5c22ed59e007edfa3380162300c198c714d2261e2e412e0a080280e1d1854.

## Successful deployment

Release commit: `8b4f3b9b008813cc295cef2fc4bcf3fcaf93b8fb`, saved through the connected GitHub Git Data API after CLI push found no credentials. Implementation checkpoint `39bba7c978c9e855221686ae508e17e399233662`; verified checkpoint `9e7c69be705043ea3c41a78d178be41214dbcc94`.

Netlify automatically published the GitHub main update. Both application URLs returned HTTP 200. A direct Python HTTP fetch returned the exact raw 48,157-byte application and SHA-256 above. Netlify serves some clients an additional platform marketing comment and public HUD script. The browser HTTP check removes only those two identified host additions and confirms all application bytes match the verified candidate; the live browser test runs against the actual hosted page, including host additions. No application code was changed to accommodate this host behavior.

12 hosted assertions passed in Linux Chromium 153: both artifacts and content identity, launcher v0.1.1, generated Mars QR/destination, live app v0.1.0, new mission→demand, save→reload→resume, contextual help and zero page exceptions. See `verification/hosted-results.json` and `../tests/hosted.test.cjs`. The browser uses the environment HTTP proxy; an initial unconfigured request failed DNS, and raw byte comparison exposed the identified Netlify additions before the final successful check.

Physical iPad/Edge, camera scan, school-network access and printer acceptance remain not run. Local save/import data is device/origin specific. Browser automated checks are not a substitute for those classroom checks.

