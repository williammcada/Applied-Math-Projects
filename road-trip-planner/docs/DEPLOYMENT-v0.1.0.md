# Road Trip Planner v0.1.0 — deployment verification

**Verified:** 30 September 2026, approximately 04:15–04:21 UTC  
**Disposition:** Deployed development candidate; physical classroom acceptance remains pending.  
**Live application:** https://williammcada.github.io/Applied-Math-Projects/road-trip-planner/

## Authorization and source

The owner approved enabling GitHub Pages through the browser after the repository connector was found unable to configure Pages. Settings were saved with “Deploy from a branch,” branch `main`, folder `/ (root)`. HTTPS is enforced for the default GitHub Pages domain.

| Record | Identity |
| --- | --- |
| Deployed repository | `williammcada/Applied-Math-Projects` |
| Initial deployment commit | `32c3500d43a8e1e497b2dd214ab45772b6b4e184` (merged PR #2) |
| Initial deployment tree | `b1f70c1a12aad4c0591869f78b2a8a36a646080f` |
| Verified application checkpoint | `7927f457c1d977c8c3bcb2a435fc38f641aea7de` |
| Evidence/package checkpoint | `e404b138b90775c1ba139deb6499a8296d28fdc7` |
| Pages workflow | [36667795884](https://github.com/williammcada/Applied-Math-Projects/actions/runs/36667795884), completed successfully at 04:13:24 UTC |
| Handbook rechecked | `00cbde605ab08203b6b5fd2374d225155608fc29`, v0.1.1; release checklist unchanged |
| Application / content / schema | 0.1.0 / 1.0.0 / 1.0.0 |

This deployment reused the preserved candidate. No application source, built HTML or schema changed. Documentation and deployment evidence are recorded separately after verification.

## Served artifact identity

Direct HTTPS retrieval returned HTTP 200 for each endpoint. Each response was 120,755 bytes with SHA-256 `19afbe79565f1bda8739b0c2d5856005e6138832f39871213eda09b2de893dc8`, exactly matching the locally verified artifact.

| Endpoint | Result |
| --- | --- |
| `/Applied-Math-Projects/road-trip-planner/` | Exact byte match |
| `/Applied-Math-Projects/road-trip-planner/RoadTripPlanner_v0.1.0.html` | Exact byte match |

## Hosted browser observations

Checks used the live HTTPS subpath in the dedicated cloud Chrome browser. Synthetic alias: `Deployment QA 2026-09-30`. These are targeted deployment observations, separate from the 749 local application assertions and 259 specification checks in the [QA report](QA-REPORT-v0.1.0.md).

| Check | Observed result |
| --- | --- |
| Welcome page, artwork and footer | Rendered; footer reports App 0.1.0 and Content 1.0.0 |
| Start, priorities and progression | Alias entered; comfortable lodging/full activities selected; advanced to Route desk |
| Save, reload and resume | Saved session remained at Stage 2 with its alias and choices after reload |
| Export progress | Downloaded JSON is 1,305 bytes, schema/app/content versions correct, Stage 2 and original alias/priorities preserved |
| Import actual exported file | Preview validated one session and recognized matching identity; “Import as new copies” created a separately labeled copy at Stage 2; imported evidence label shown |
| Proposal preview | Four student page sections rendered; alias, version, draft and imported-evidence labels correct; Print / save PDF control present |
| Print command | Invoked from hosted preview; native dialog/output was not observable through this cloud browser. No new hosted PDF-output pass is claimed |

The browser download-event observer timed out twice, but the exported files were present in the synchronized download directory. The first actual file was parsed, preserved and successfully selected through the hosted import chooser. Export success is based on those bytes and the successful import, not solely the app's “download requested” message.

## Preserved evidence

- [Live welcome screenshot](verification/live-20260930.jpg)
- [Synthetic exported progress](verification/hosted-progress-20260930.json), SHA-256 `b45eca4b57d541852132e185d63b5e40edfeff2d71a04c5387c0bcaa79a910f6`
- [Local candidate QA and print PDFs](QA-REPORT-v0.1.0.md)

## Remaining acceptance and recovery

Still required on the actual school iPad/network: Safari portrait/landscape, on-screen keyboard, graph/input/help touch workflows, resume/export/import and backup/replacement. Verify the actual printer and grayscale output. Local Chromium A4/Letter PDFs have been inspected, but neither browser emulation nor this deployment establishes physical acceptance.

To recover application delivery, restore the two HTML entry files from the preserved verified candidate and compare the recorded SHA-256 before redeploying. Keep the same hosted origin/path to avoid unexpectedly separating users from browser-local saves. Export progress before changing devices or clearing browser data. Preserve the accepted candidate rather than rebuilding it to repair packaging or hosting.
