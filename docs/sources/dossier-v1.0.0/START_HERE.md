# Start here — Applied Mathematics Project Series

**A WILLIAM MCADA PRODUCT**  
**Dossier version 1.0.0 · September 15, 2026**

## What this package contains

This is a build-ready design and implementation dossier for five independent classroom projects. It does not contain the five playable applications. Each future application must be delivered as its own self-contained HTML file, with a matching GitHub-ready `index.html`.

Open `William_McAda_Applied_Math_Projects_Dossier_v1.0.0.docx` for the formatted, editable 44-page dossier. The matching `.md` file supplies searchable/copyable content for an AI coding handoff. Both represent the same version; use one chosen master when revising them, rather than allowing competing versions to drift.

`ASTRA_BUILD_PROMPT.txt` is ready to paste when requesting the first build, Road Trip Planner. Attach the dossier and the reference files, or attach this whole ZIP. For later builds, change the project name and its chapter range. Do not ask for a generic engine first.

## Project order and chapter map

| Build | Project | Dossier sections | Proposed core time |
|---|---|---|---|
| 1 | Road Trip Planner | 13–17 | 3 × 45 minutes |
| 2 | Food Truck | 18–22 | 3 × 45 minutes |
| 3 | Theme Park Designer | 23–27 | 4 × 45 minutes |
| 4 | Mars Colony | 28–32 | 3 × 45 minutes |
| 5 | Powers of Ten | 33–38 | 2 × 45 minutes |

Sections 01–12 apply to every project. Sections 39–42 define acceptance, handoff, reference cases, and sources. Powers of Ten can move earlier to fit the cross-curricular calendar. These timings are proposed defaults, not classroom-tested results.

## Included implementation aids

- `reference_fixtures.json`: baseline data and expected mathematical/geometry results.
- `verify_reference_fixtures.py`: independent Python checks, using the standard library only.
- `reference_check_report.json`: result of the supplied reference check run: **77 of 77 passed**.
- `figures/`: editable SVG and PNG concept/reference diagrams. These are not a complete final artwork library and do not replace the asset requirements inside each project chapter.
- `dossier_validation_report.json`: document/layout and reference-check status; explicitly separates these from application testing.
- `CHANGELOG.md`: initial dossier release record.
- `MANIFEST.json`: file hashes for this release.

To rerun the reference checks with Python 3:

```bash
python verify_reference_fixtures.py --report reference_check_report.json
```

Run this command from the extracted package folder. The checks verify reference arithmetic and geometry only. Astra must also implement tests against the actual HTML: correct and incorrect student paths, dependency rechecking, saving/importing, keyboard/touch alternatives, print layout, and every ending. Physical iPads and the school network remain untested until checked there.

## Defaults that remain adjustable

Pairs sharing one device; English with ELL scaffolding; metric units; fictional USD classroom prices for Road Trip and Food Truck; credits for Theme Park and Mars; formative reporting rather than automatic gradebook marks. An optional teacher-applied 20-point rubric is specified. Students receive unlimited revisions; asking for help is not penalized.

The scientific-notation project assumes the operations have been taught. Add a bridge lesson or a third session rather than deleting an operation, the small-number contexts, or the physical build to force the two-day schedule.

## Non-negotiable product identity

Five bespoke flows—not a generator. Visible version numbers and William McAda branding. Embedded pictures, meaningful `?` help, explanatory blocking of academic errors, reliable local/portable saving, printable work, narrative endings, and no music. Correctly calculated poor designs receive a revision outcome, not a false arithmetic error.

## Authorship and source status

The requirements and project concepts are William McAda's project series. Scientific and technical source references appear in dossier section 42. The included visual references are original explanatory diagrams, not photographs, microscopy, or measured observations. No font files or third-party image files are distributed in this package.
