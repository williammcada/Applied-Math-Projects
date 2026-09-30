# Implementation notes — v0.1.0

The approved specification remains the authority. These are concrete representations selected within its initial-save-schema and development-file allowances.

- `src/core.js` is a dependency-free UMD-style module for browser use and Node verification. BigInt rational pairs drive numeric, linear-expression and inequality evaluation; no eval or dynamic code execution is used.
- Fixed checkpoint definitions have permanent `RT-Fxx.<field>` IDs, `RT-xx` objectives, source IDs, prompts/labels, units, evaluator kinds, help groups and review policies. Group gates map C01–C09 to the eight stages. The detailed pedagogical contracts remain in the approved specification.
- `currentStage` and `maxStage` store integers 1–8 corresponding to RT-S01–RT-S08. Field keys are flat stable strings in `inputs`; schema 1.0.0 has no earlier real app save to migrate. `scenarioId` records the base/hotel phase, while actual choice/distance revisions are preserved in snapshots and fingerprints.
- Exact values serialize as integers or reduced `n/d` strings. Numeric/model attempts include normalized values or coefficients when parseable, with the original raw response and dependency fingerprint retained. An unchanged verified sibling does not gain a duplicate attempt.
- Research-source format checks and teacher truth review are separate. A partially typed route can be saved and resumed at the route desk; downstream navigation remains blocked until consistent.
- Imported current verified answers are re-evaluated. Historical imported attempts remain historical reported evidence. Teacher review/bypass records are not cryptographic attestations.
- Storage scans the project session namespace so a missing/stale index does not hide recoverable records. Multi-record writes stage old values and roll back if a write/index operation fails. Partial deletion reports surviving records rather than claiming success.
- The graph uses one-day ticks, uniform selected cost steps, exact ordered-pair inputs and a tap-to-estimate alternative. The input is the exact authority, not pixel proximity. Rendering bounds the number of grid lines for unusually large reviewed research distances.
- HTML build output has no runtime dependency on `src/`. Both entry files are deterministic, byte-identical products of `build.py`. Separate print roots prevent teacher-key leakage into student proposals; graph clip IDs are isolated between preview and print copies.
- The 14-day cap is supported by the affordability evaluator, although no canonical current-catalog route reaches that cap at $1,800. Its boundary is tested directly. General budget, party-size and efficiency editors are not exposed.

The initial checkpoint was preserved before extended verification. All later source changes were checkpointed again before the final verification pass. No application bytes were changed while packaging the verified candidate.
