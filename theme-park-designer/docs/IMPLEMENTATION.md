# Theme Park Designer — Implementation Notes

## Authority and version identity

App 0.1.0, content 1.0.0, schema 1.0.0, scenario `TP-BASE`, project ID `theme-park`. The approved specification and approval record are under the repository's `docs/` directory. Source dossier and handbook identities are recorded in the project brief. No global handbook changes or other-project assessment rules were introduced.

## Runtime

The static build concatenates CSS and three JavaScript modules into a single HTML file. It uses DOM APIs, SVG, localStorage, Blob download, File input, and browser printing. BigInt rational arithmetic avoids floating-point threshold errors. The model computes disjoint cell areas, connected paths, door segments, costs, and outcome predicates; the display reads that model.

Geometry mutations validate a proposed clone before replacing the working plan. Land operations use unique 2 m cell IDs. Doors rotate with facilities. Rooted access uses four-neighbor traversal and positive-length door-edge contact. Expansion is a designation within unused land and carries no duplicate area or cost.

Checkpoint fingerprints track mathematical dependencies. Stale raw answers and previous attempts remain available. Optional expansion answers can remain dormant after removing the expansion designation; this is valid saved history, not an unknown-field import. Snapshots copy the plan and evidence. Report outcomes use the chosen immutable snapshot and current comparison/transfer evidence.

## Portable and local records

Portable JSON uses `schema: mcada-project-progress`, the version/project headers, `currentStage: TP-S01` through `TP-S08`, and `inputs`, `attempts`, `checkpoints`, `teacherOverrides`. `inputs` contains the working plan, snapshots, response/settings metadata, transfer records, and reviews. Plan-level attempts/evidence are nested with their plan; comparison/transfer attempts and evidence occupy the top-level arrays/object. The internal local record uses a numeric stage and `history`, `evidence`, `overrides`; export/import maps the two representations explicitly.

One localStorage record holds each complete session at `mcada:theme-park:session:<id>`. No global `localStorage.clear()` is used. A revision counter rejects stale writes after a newer local revision. Storage denial is reported and the in-memory work remains exportable. Import validates into a temporary value, presents a review, and duplicates session identity on commit.

Input limits: 5 MiB per import file, 100 sessions per backup, 30 snapshots per session, 10,000 records per bounded history collection, 600 unique cells per land layer, 80 characters per alias/name, 2,000 per reflection/response string. Attempt and snapshot limits show explicit errors rather than discarding evidence. These are validation bounds, not a promise that browser storage can hold every maximal combination. Normal lesson exports and backups were round-tripped; large combined backups should be kept below the import size limit.

Imported markup is escaped before rendering. Current claimed-correct answers are re-evaluated. This is a local educational tool: public source and editable files make it unsuitable for authenticated or tamper-proof assessment.

## Print and evidence

The map SVG uses a 68 × 48 viewBox including coordinate margins and prints at 170 × 120 mm, making the 60 × 40 site 150 × 100 mm. Its 2 m grid cells are 5 mm. A separate CSS calibration line is 50 mm. A4/Letter PDF sizes were inspected; physical print measurements remain pending.

`tests/` contains model checks, geometric threshold fixtures, complete ending examples, and browser workflows. `docs/verification/` retains assertion results and a PDF audit; generated PDFs are reproducible test outputs rather than runtime assets. QA examples contain invented aliases only.
