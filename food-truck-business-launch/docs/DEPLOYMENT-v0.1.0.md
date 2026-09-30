# Food Truck v0.1.0 — deployment verification

Verified 30 September 2026, 07:29–07:32 UTC. Deployed development candidate; physical classroom acceptance remains pending.

[Live application](https://williammcada.github.io/Applied-Math-Projects/food-truck-business-launch/)

| Record | Identity |
| --- | --- |
| Implementation PR | [#5](https://github.com/williammcada/Applied-Math-Projects/pull/5), merged |
| Verified implementation/evidence head | `b7cebb9976b57db84df9702d2ccdca761d347842` |
| Deployment merge commit | `d728dff8f8553f7db5cd26304d9bc403ad790ad9` |
| Source tree | `92a5f1d3ada2dc0517448522b56b463c87b4a218` |
| Pages workflow | [36683900312](https://github.com/williammcada/Applied-Math-Projects/actions/runs/36683900312), completed successfully |
| Hosting | Existing GitHub Pages, main branch/root; no hosting-provider change |
| App / content / schema | 0.1.0 / 1.0.0 / 1.0.0 |

## Served identity

Both the directory URL and `FoodTruck_v0.1.0.html` returned HTTP 200 and exactly **101,711 bytes**, SHA-256 `93d0fde0e125fb68b96eeef14816ac51d2bc0ce2b03670bc005c767dbd26aae0`, matching the locally verified release. The initial request while Pages was building still returned the old directory landing page; the verification recorded here occurred after workflow success.

Road Trip remained HTTP 200, 120,755 bytes, SHA-256 `19afbe79565f1bda8739b0c2d5856005e6138832f39871213eda09b2de893dc8`, unchanged. Raw response measurements are in `verification/hosted-bytes.json`.

## Actual hosted browser

Cloud Chrome loaded the app/version and embedded artwork. Using synthetic alias Deployment QA, started a session, entered truck identity/brief, reached Recipe bench and checked all six scaling answers. Reloaded and resumed the same checked work. Exported the live JSON and imported that same downloaded file as a new copy; the UI validated it, preserved checked answers and labeled imported history. Opened the four-page draft report preview with checked/missing states and separate report content. Captured the live homepage in `verification/live-home.jpg`.

The browser tool's download-event waiter timed out, but the actual nonempty downloaded JSON was present in the shared download directory and was successfully reimported through the live file chooser. This is recorded as a tool-event limitation, not a failed app export. `verification/live-export.json` preserves that synthetic export.

These targeted hosted observations are additional to the 216 core and 80 browser assertions in the QA report. They do not establish physical iPad/Safari, on-screen keyboard, school-network or physical-printer acceptance. No Road Trip content was changed.
