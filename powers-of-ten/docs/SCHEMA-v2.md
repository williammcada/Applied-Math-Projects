# Powers of Ten progress 2.0.0

Frozen implementation contract, 2026-10-08. App 0.2.0 / content 2.0.0.

The v1 identity, inputs, attempts, checkpoint, review and build fields remain. Root adds `lesson` (dashboard/science/math), `scienceStep` (1–4), `science` (A/B), `handoff` (exported/verified) and `legacy` (null or validated original v1 session). All fields and bounds are validated on load/import.

Each Science track has strings `label` (40), `property` (60), `source` (30), `prediction` (100), `preserved` (180), `omitted` (180), `other` (140), `peer` (120); `route` (measured/paper/teacher-example/legacy), and `measuredBuild` (−1 or build revision 0–100). C09 measurements, units, tool and resolution remain the single source of truth. Science restricts tool to 60 characters; longer legacy text remains preserved and must be shortened in the new copy for completion.

Each handoff marker is null or `{fingerprint, revision, at}`. Fingerprints include session identity, pair aliases, selected track, build confirmation/revision, Science claims and measurements. Test saved copy compares a separately parsed export; it does not replace answers. Export click alone is not verification. Editing handoff evidence makes verification stale.

C13A/B add exact observed factors. Measurements/build/claims invalidate dependent measurement/scale/interpretation fingerprints; fixed C04–C07 remain current. Optional methods are retained in raw attempt responses and checked separately from required final answers.

A validated v1 save migrates to a new session ID with `duplicateOf` and an entire original `legacy` record. Original storage keys are never overwritten by migration. Existing reviews retain their original fingerprints and become historical. New Science completeness never derives from old stage numbers. v1 and v2 bundle imports are supported, each session validated.
