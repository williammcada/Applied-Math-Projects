# Theme Park Designer v0.1.0 — Implementation Specification

**Specification revision:** Approved revision 1 · 30 September 2026 (Asia/Shanghai)  
**Status:** Approved for implementation by William McAda on 30 September 2026 with “Proceed with production.” Approval includes TP-I01–TP-I07. Application verification remains a separate stage.  
**Owner:** William McAda · **Credit:** A WILLIAM MCADA PRODUCT  
**Student-facing title:** Theme Park Designer · **Working subtitle:** ParkWorks  
**Project ID:** `theme-park`  
**Canonical repository:** [williammcada/Applied-Math-Projects](https://github.com/williammcada/Applied-Math-Projects)  
**Application directory:** `theme-park-designer/`  
**Suggested canonical specification path:** `docs/change-specs/THEME-PARK-DESIGNER-v0.1.0.md`  
**Source baseline:** `b1f9ae4158631043314e8a88e5f56549cebd319c`  
**Target versions:** application `0.1.0`; content `1.0.0`; progress schema `1.0.0`  
**Handbook baseline consulted:** `00cbde605ab08203b6b5fd2374d225155608fc29`

## 1. Purpose, source authority, and current state

Students act as a design team commissioned to build a compact theme park. They convert between real and drawing dimensions, calculate areas, place facilities, connect entrances, allocate land, calculate construction costs, and revise their design after inspection. The final product is a scale plan and an opening-day brochure or a report explaining why the park needs revision.

**Driving question:** How do scale and area turn an attractive sketch into a buildable plan?

The authoritative project source is the preserved **Applied Mathematics Project Series Dossier v1.0.0**, common sections 01–12, Theme Park sections 23–27, and release/reference sections 39–42. Its exact geometry, costs, objectives, and outcome thresholds are carried forward below. The dossier supplies proposed classroom defaults as well as binding product directions; this specification does not relabel every default as a separately approved preference.

At the consulted repository commit, Theme Park Designer contains a planning README and the shared dossier, with no Theme Park application or project-specific approved change specification. The source baseline is therefore a design baseline, not an existing verified software release. Road Trip and Food Truck specifications provide a documentation precedent. Their tasks, durations, scoring, and numerical rules do not become Theme Park requirements.

### Source register

All repository links in this register point to the exact revisions read for this preparation.

| Source | Purpose |
| --- | --- |
| [Series README](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/README.md) | Canonical repository, independent applications, build/release process |
| [Series PROJECT-BRIEF.md, version 0.8](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/PROJECT-BRIEF.md) | Audience, devices, family requirements, handbook selection |
| [Theme Park planning README](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/theme-park-designer/README.md) | Existing subproject identity and spatial-design scope |
| [Dossier v1.0.0](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md) | Full common and Theme Park contracts; blob `e8eea73b4cf8b3b124353b155b72a1c24458c908` |
| [Dossier START_HERE.md](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/START_HERE.md) | Delivery requirements and default/extension distinctions |
| [Reference fixtures](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/reference_fixtures.json) and [reference checker](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/verify_reference_fixtures.py) | Independently check supplied arithmetic and geometry; not application tests |
| [Change-spec template](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/change-specs/CHANGE-SPEC-TEMPLATE.md) and [series foundation](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/change-specs/SERIES-FOUNDATION.md) | Versioned decisions, preservation, evidence, recovery |
| [Road Trip v0.1.0 specification](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/change-specs/ROAD-TRIP-PLANNER-v0.1.0.md) and [Food Truck v0.1.0 specification](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/change-specs/FOOD-TRUCK-v0.1.0.md) | Process and specification structure only |

The original course-outline and external standards references are preserved in the dossier. They were not independently retrieved in this task. Curriculum references below describe the dossier's alignment; they are not a new curriculum audit or a claim of complete coverage of each standard.

### Handbook files and applicability

The following files were read at [handbook commit `00cbde6`](https://github.com/williammcada/mcada-project-handbook/tree/00cbde605ab08203b6b5fd2374d225155608fc29):

| File | Application to this specification |
| --- | --- |
| `AI-START-HERE.md` | Use actual source, identify conflicts, separate proposals from saved/approved decisions |
| `UNIVERSAL-RULES.md` | U-01–U-08 selected as project guidance; approved U-09 governs saved-work deletion |
| `CONDITIONAL-STANDARDS.md` | Select S-02 learning evidence, S-04 distribution, and S-05 Applied Mathematics Project Series |
| `PROJECT-TEMPLATE.md` | Local brief, source identity, must-retain requirements, saved-work scope |
| `RELEASE-CHECKLIST.md` | Required evidence and honest Passed / Failed / Not run / Not applicable reporting |

U-01–U-08 remain seeded rules in the handbook; the conditional modules remain draft modules selected for this family. U-09 is explicitly approved. No universal rule is added or changed. S-01 external AI generation and S-03 live games are not selected: this application has neither an AI roundtrip nor networked multiplayer. Portable progress import is still fully validated.

## 2. Scope and decisions proposed for v0.1.0

### Inherited requirements and classroom defaults

| Area | v0.1.0 scope |
| --- | --- |
| Audience | Advanced Grade 5 Introduction to Pre-Algebra / Saxon 8/7 context |
| Working arrangement | Default: pairs sharing an iPad; full desktop keyboard/mouse support; alternate Planner/Checker at major chapter boundaries |
| Time | Four proposed 45-minute lessons; not yet classroom-tested |
| Mathematical identity | Scale, linear versus area scale, rectangle/triangle/circle area, footprint allocation, coordinate placement, perimeter, percentages, and cost constraints |
| Language | ELL-friendly English; short prompts, numerical responses, structured labels, brief evidence-based reflections |
| Site | 60 m × 40 m; 2 m grid; coordinates measured from the lower-left |
| Currency | Credits (`cr`); authored classroom costs |
| Product | One bespoke, self-contained HTML application; embedded visuals; no shared runtime |
| Delivery | Downloaded desktop HTML works offline; intended hosted path uses GitHub Pages; iPad primarily uses the hosted page |
| Evidence | Nine required checkpoints; first attempts, corrections, support, review, and individual transfer separated |
| Feedback | Unlimited revisions; no hint penalty, countdown, speed score, or automatic gradebook mark |
| Sound | No music, audio files, autoplay audio, or sound-dependent information |
| Output | Portable progress, printable scale map, student report, brochure/inspection report, teacher reference |

No new repository is needed. The existing canonical repository and `theme-park-designer/` directory establish the project home. Before implementation, add `theme-park-designer/docs/PROJECT-BRIEF.md` and record the approved specification in `docs/change-specs/`. Keep shared repository documents intact and preserve other subprojects.

### Proposed implementation decisions

These decisions resolve details the dossier leaves open. TP-I01–TP-I07 were approved for v0.1.0 by the owner with “Proceed with production” on 30 September 2026. Descriptions of their proposal rationale remain as provenance.

| ID | Proposed decision | Reason and boundary |
| --- | --- | --- |
| TP-I01 | Start with an empty site and six facility tiles. Require the two main path rectangles at their published positions; students add connector cells and any additional paths. Main rectangles cannot be resized or removed in core. | Gives every student the required overlapping-rectangle calculation while preserving meaningful facility placement, connectors, landscape, and expansion choices. The dossier specifies mandatory connected paths but does not explicitly lock the example spines; locking these is a proposed scope choice. |
| TP-I02 | Treat each published door coordinate as the center of a 4 m entrance segment on its footprint edge. Rotate the segment with the facility. Connection requires positive-length shared edge with an exterior path cell, not a corner touch. | The dossier names entrance edges but its legacy fixture checker only tests inclusive point contact. This closes that implementation gap without changing the baseline map. |
| TP-I03 | The entrance facility has a distinct street-facing edge and park-facing door. Its street-facing edge must lie on the site boundary; all path cells must be reachable from its park-facing door. | Makes the entrance the access root and prevents an isolated network from receiving approval. This is a classroom rule, not a building-code simulation. |
| TP-I04 | Require an inspected Plan A and a materially different Plan B, changing at least one facility position/orientation, editable path cell, green cell, or expansion designation. Students may recommend either plan. | Makes TP-08 observable even when the first plan already satisfies all opening criteria. Improvement is discussed, not assumed from any arbitrary change. |
| TP-I05 | Use two authored individual transfer variants, one per partner, with fresh pavilion dimensions. Record them separately and withhold their keys from the shared student screen until both are submitted. | Creates individual evidence without accounts or a separate assessment engine. |
| TP-I06 | One saved session groups its working design, named plan snapshots, attempts, reviews, and transfer responses. Provide snapshot deletion, session deletion, and clear-all for Theme Park only. | Implements approved U-09 with the project's own terminology; no class/year administration. |
| TP-I07 | Keep site size, scale, costs, required facilities, and ending thresholds fixed in core. Teacher Mode offers reference answers, review, diagnostics, calculator control, and recorded bypasses, not a scenario generator. | Keeps the first release bounded and makes its fixtures reproducible. |

There is no conflict between the current request and the handbook. The principal source ambiguity is point-based door checking versus an entrance-edge access rule; TP-I02 resolves it explicitly. Numerical defaults and ending thresholds remain unchanged.

### Out of scope

- CAD tools, arbitrary-angle rotation, freehand geometry recognition, ride physics, crowd simulation, demand forecasts, or real accessibility/fire-code approval.
- Accounts, cloud storage, live multiplayer, teacher dashboards, AI generation, paid services, telemetry, or automatic submission.
- Volume, surface covering, capacity rates, a second drawing scale, and a separate Tiny House project. The food pavilion retains the spatial-design connection; those extensions do not block core completion.
- Unrelated assessment quotas, AAC formats, Road Trip events, Food Truck business scoring, and other games' reward systems.
- iPhone support or guaranteed offline reopening of a closed hosted page. Neither follows automatically from a self-contained file.

## 3. Fixed content and mathematical model

### Site and scale

| Quantity | Contract and reference result |
| --- | --- |
| Actual site | Width 60 m; height 40 m; area 2,400 m²; perimeter 200 m |
| Drawing scale | 1 cm represents 4 m; same-unit ratio 1:400 |
| Printed mathematical plan | Exactly 15 cm × 10 cm at 100% print scale |
| Grid | 30 columns × 20 rows; each cell 2 m × 2 m = 4 m² |
| Printed grid cell | 0.5 cm × 0.5 cm; 5 mm per edge |
| Coordinate origin | Lower-left site corner; mathematical y increases upward |
| Permitted rotation | 0° or 90° counterclockwise; no arbitrary-angle rotations |
| Circular calculation | Use π = 3.14, explicitly stated on the task |
| Budget | 90,000 cr |

Use two unit-aware scale operations: `drawingCm = actualM / 4` and `actualM = drawingCm × 4`. Do not describe 1:4 as the scale ratio after ignoring the centimeter/meter conversion. Doubling all lengths multiplies area by four; a 2 m square becomes a 4 m square, with area changing from 4 m² to 16 m².

### Six required facilities

Every design contains exactly one of each facility. Students may move or rotate them within the geometric rules; dimensions and costs remain fixed. The coordinates below define teacher/reference fixture `TP-BASE`, not a layout that all students must copy.

| ID | Facility | Baseline lower-left (m) | Baseline width × height (m) | Reserved area (m²) | Cost (cr) | Baseline door center (m) |
| --- | --- | --- | --- | --- | --- | --- |
| `coaster` | Coaster | (2, 4) | 20 × 12 | 240 | 24,000 | (12, 16) |
| `carousel` | Carousel | (42, 4) | 12 × 12 | 144 | 12,000 | (48, 16) |
| `theater` | Theater | (2, 26) | 16 × 10 | 160 | 10,000 | (10, 26) |
| `food` | Food pavilion | (42, 26) | 10 × 8 | 80 | 8,000 | (48, 26) |
| `services` | Services | (22, 8) | 6 × 8 | 48 | 4,000 | (28, 12) |
| `entrance` | Entrance | (24, 0) | 4 × 8 | 32 | 2,000 | (28, 4) |
| **Total** | | | | **704** | **60,000** | |

The circular carousel platform has diameter 10 m, radius 5 m, and area `3.14 × 5² = 78.5 m²`. Its reserved square is 144 m². The remaining reserved clearance is `144 − 78.5 = 65.5 m²`. Reserve the full square in the land ledger; do not add the circle again or count its clearance as public green space.

The food pavilion contains a triangular shade-roof subfeature with base 8 m and perpendicular height 6 m. Its area is `8 × 6 ÷ 2 = 24 m²`. It is already inside the pavilion's allocated footprint and cost. No additional land or unquoted roof charge is added.

### Paths, green space, and expansion reference

Rectangles use `[x, y, width, height]` in actual meters.

| Component | Rectangle(s) | Area |
| --- | --- | --- |
| Horizontal main path | `[0,18,60,4]` | 240 m² |
| Vertical main path | `[28,0,4,40]` | 160 m² |
| Main-path overlap | `[28,18,4,4]` | 16 m² |
| Main-path union | Both main paths counted once | `240 + 160 − 16 = 384 m²` |
| Baseline connectors | `[10,16,4,2]`; `[46,16,4,2]`; `[8,22,4,4]`; `[46,22,4,4]` | 48 m² total |
| All baseline paths | Main-path union plus connectors | **432 m² = 108 cells = 18% of site** |
| Green rectangles | `[0,0,24,4]`; `[32,0,28,4]`; `[0,36,28,4]`; `[32,36,28,4]`; `[20,26,6,8]` | **480 m² = 120 cells = 20% of site** |
| Undeveloped land | Site minus facilities, path union, and green union | **784 m²** |
| Designated expansion zone | `[32,4,10,14]` | **140 m²**, already part of undeveloped land |

For any valid design, calculate from disjoint occupied-cell sets:

```text
facilityArea = 4 × number of facility cells
pathArea     = 4 × number of distinct path cells
greenArea    = 4 × number of distinct green cells
unusedArea   = 2400 − facilityArea − pathArea − greenArea
fractionOfSite(area) = area / 2400
percentOfSite(area)  = 100 × area / 2400
```

The expansion rectangle is a tagged subset of unused land, not a fifth additive category. Unused land outside the designated baseline expansion zone is `784 − 140 = 644 m²`. Empty land is not automatically landscaped, accessible path, or designated expansion space.

### Budget

| Line | Rule | TP-BASE amount |
| --- | --- | --- |
| Facilities | Sum of six fixed prices | 60,000 cr |
| Paths | 25 cr/m² × path union area | 10,800 cr |
| Landscaping | 10 cr/m² × green area | 4,800 cr |
| Boundary treatment | 20 cr/m × full 200 m perimeter | 4,000 cr |
| Total | Facilities + paths + landscaping + boundary | **79,600 cr** |
| Signed balance | 90,000 − total | **+10,400 cr** |
| Reserve percentage | Balance ÷ 90,000 × 100 | Exact `104/9%`; **11.6%** to nearest 0.1 percentage point |

The boundary quotation **includes the entry gate segment**. Do not subtract the gate width. Negative budget balances are legitimate answers when a student correctly calculates an overrun.

All geometry uses exact integer meters/cell counts. Use rational/decimal arithmetic for answers and percentages; π is the exact supplied decimal `3.14` for this model. Core cost totals are whole credits. Compare thresholds with exact quantities, never rounded display values.

### Opening criteria

All critical conditions must be true:

1. Six required facilities are present exactly once, within the site, with valid non-overlapping reserved footprints.
2. Both main paths remain present under TP-I01; path/building/green allocations do not overlap.
3. The entrance's street edge meets the site boundary, every facility door is connected, and all path cells belong to the entrance-rooted network.
4. Path area is between **10% and 25%, inclusive**: 240–600 m². Fixed main spines already occupy 384 m², so the 10% floor is automatically met by structurally valid core plans. Do not claim a lower-bound failure is student-reachable under TP-I01.
5. Green area is **at least 20%**, or 480 m².
6. Total cost is **no more than 90,000 cr**.

Distinction additionally requires budget balance **at least 4,500 cr** (5% of the original budget) and a valid student-designated unoccupied rectangle **at least 100 m²**. It must be one qualifying rectangle, not scattered cells whose total reaches 100 m².

## 4. Student journey and pacing

| Stage | Student action and visual | Completion/evidence |
| --- | --- | --- |
| TP-S01 · Land offer | Meet the town's planning inspector; name the park; read the illustrated site brief, facility list, budget, and published opening rules. | Confirm the six facilities and key constraints. Create a session with two aliases and current Planner/Checker. |
| TP-S02 · Survey desk | Label real and drawing dimensions; calculate grid area, site area/perimeter, and area-scale change. | TP-C01 and TP-C02; site calculations used again by TP-C03/07. |
| TP-S03 · Attraction studio | Inspect six illustrated tiles; calculate footprints, carousel platform/clearance, and shade triangle. | TP-C03 and TP-C04; correct classification of area used for land allocation. |
| TP-S04 · Design table | Place and rotate all six facilities on the exact top-down map. Use drag, tap placement, or coordinate entry. | TP-C05; structural layout valid. Connections may remain unfinished until TP-S05. |
| TP-S05 · Paths and landscape | Construct the required main paths; add connectors; paint green cells; optionally designate expansion. Calculate union, allocations, and percentages. | TP-C06; disconnected or strategically weak plans remain eligible for analysis once their mathematics is correct. |
| TP-S06 · Quantity surveyor | Build a cost ledger with rates, units, total, and signed balance. | TP-C07; correct overspend is accepted as mathematics and flagged as a design problem. |
| TP-S07 · Inspection | Inspect Plan A, revise to Plan B, recheck affected work, and make a recommendation with one numerical tradeoff. | TP-C08; preserve both plans and their evidence. Highlight actual conflicts and constraint failures. |
| TP-S08 · Opening day | Reveal the selected verified map; show its exact outcome; print the map/report/brochure; complete individual transfer. | TP-C09 for each partner. Final academic report requires both transfer records or explicit teacher override. |

Suggested pacing: lesson 1 covers the land offer and survey; lesson 2 covers attractions and placement; lesson 3 covers paths, landscape, and costs; lesson 4 covers inspection, revision, transfer, and the reveal. Prompt a role swap at each lesson boundary and a progress export at each stopping point. Save, Back, Help, and teacher assistance remain available at every gate.

The opening scene may be previewed after current pair mathematics and the two-plan comparison are complete. Label the report **Individual transfer pending** until both students submit the required evidence. A preview is not a completed academic report.

## 5. Checkpoint, answer, and evidence contracts

Use stable IDs `TP-C01` through `TP-C09`, linked to dossier objectives `TP-01` through `TP-09`. These nine objectives are retained in full. The dossier's reference anchors are 7.G.A.1, 7.G.B.4/6, 7.RP.A.2–3, and 7.EE.B.3; they are alignment references rather than a complete standards assessment.

Every implemented field record must include ID, objective, prompt, source/given data, permitted range, mathematical action, quantity/unit, required representation, answer format, evaluator, precision, prerequisite IDs, help, misconception messages, and evidence/review status. The contracts below are the build requirements; the developer must instantiate their field IDs and dependencies explicitly.

For every deliberate Check, record the first checked response, later attempts, current response, current input fingerprint, scenario/design revision, support used, result, and timestamp. Do not count typing as an attempt. Preserve the distinction between unassisted first response, final corrected work, teacher override, and teacher-reviewed prose.

### TP-C01 — Convert scale dimensions / TP-01

- **Given:** 60 m × 40 m site; 1 cm represents 4 m.
- **Required action:** Enter drawing width/height, reverse-convert a 3.5 cm model length, and express the drawing-to-real ratio in common units.
- **Representation:** Dimensioned real/drawing diagrams and a labeled conversion table; student entries create their dimension labels after checking.
- **Fields and keys:** `scale.drawingWidthCm = 15`; `scale.drawingHeightCm = 10`; `scale.actualFrom3_5Cm = 14 m`; `scale.ratio = 1:400` or an equivalent positive ratio in the declared drawing:actual order.
- **Acceptance:** Exact decimals/fractions for lengths; positive numerator/denominator for ratio. Reject 1:4 with a unit-conversion explanation. No hidden rounding.
- **Prerequisite:** Land-offer setup. Later coordinate and print work must use this scale, not a separate display constant.
- **Help:** “A scale links a drawing length and a real length. For example, at 1 cm:5 m, a 20 m wall is 4 cm on paper.”
- **Evidence:** Both conversion directions and ratio interpretation; not merely recognition of a prefilled 15 × 10 label.

### TP-C02 — Separate length and area scale / TP-02

- **Given:** 2 m grid-cell side; a comparison square with 4 m side.
- **Required action:** Calculate both square areas, linear factor, area factor, and grid dimensions.
- **Fields and keys:** `grid.cellAreaM2 = 4`; `grid.doubledAreaM2 = 16`; `grid.lengthFactor = 2`; `grid.areaFactor = 4`; `grid.columns = 30`; `grid.rows = 20`.
- **Representation:** Two dimensioned squares subdivided into equal cells; students identify four small squares in the enlarged square.
- **Acceptance:** Exact nonnegative quantities; rows/columns positive integers. Area has square units, not meters.
- **Prerequisite:** TP-C01. Evidence must show that the area factor is squared, rather than accepting a single unexplained answer.
- **Help:** Use 3 m and 6 m squares: 9 m² and 36 m². Explain that both width and height double.
- **Error example:** “You doubled one length. Area changes in two directions.”

### TP-C03 — Calculate the site's and facilities' areas / TP-03

- **Given:** Dimensions from section 3; π = 3.14; triangle base 8 m and perpendicular height 6 m.
- **Required action:** Calculate site area, each of six reserved footprint areas, carousel radius/platform area, and shade area. Any previously checked site-area field is reused as evidence, not silently prefilled and newly counted as a student response.
- **Fields and keys:** `geometry.siteAreaM2 = 2400`; six footprint areas `240,144,160,80,48,32`; `carousel.radiusM = 5`; `carousel.platformAreaM2 = 78.5`; `shade.areaM2 = 24`.
- **Representation:** Exact rectangles, a circle with diameter/radius labels, and a triangle with perpendicular-height marker. Use structured formula fields for the circle and triangle; a correct total cannot compensate for using diameter as radius or omitting one-half.
- **Acceptance:** Exact numeric/rational forms under the stated π convention. Formula selection and substituted quantities must agree. No need for a general symbolic algebra engine.
- **Prerequisite:** TP-C02. Calculator can support arithmetic; selecting the relevant dimensions/formula remains student work.
- **Help:** Different-number rectangle, circle, and triangle examples. Diagnose 314 m² as likely diameter/radius confusion and 48 m² as omission of the triangle's one-half.
- **Evidence:** Calculations, selected formula, substitutions, units, and final responses.

### TP-C04 — Distinguish occupied area and reserved footprint / TP-04

- **Given:** Verified carousel platform 78.5 m²; 12 × 12 m reserved square; shade roof within the food pavilion.
- **Required action:** Classify the platform, clearance, reserved footprint, and roof feature; calculate clearance; select which area enters the land ledger.
- **Fields and keys:** `carousel.clearanceM2 = 65.5`; `carousel.ledgerAreaM2 = 144`; `shade.additionalLandM2 = 0`; categories must identify the platform/clearance as contained within the reservation.
- **Representation:** Toggle between exact nested shapes and decorated ride. The same outer square remains visible as the reservation.
- **Acceptance:** Exact values plus correct structured labels. Do not count an occupied-area total as a valid reserved-footprint answer.
- **Prerequisite:** TP-C03. Teacher-reviewed optional oral explanation can supplement, not replace, required numerical evidence unless a bypass is recorded.
- **Help:** A 6 × 6 m equipment zone containing a 20 m² platform still reserves 36 m²; the remaining 16 m² is clearance, not extra land.

### TP-C05 — Place and rotate without changing area / TP-05

- **Given:** Fixed facility dimensions, 2 m grid, site boundaries, and main-path reservations.
- **Required action:** Place all six facilities; record coordinates; perform at least one 90° rotation of a non-square facility and compare its dimensions/area before and after. Rotation evidence can be collected in an unobstructed preview before placement. Retaining 0° in the final plan is allowed.
- **Fields:** `layout.facilities[id].xM`, `yM`, `rotation`; `rotationEvidence.facilityId`, `beforeDimensions`, `afterDimensions`, `beforeArea`, `afterArea`.
- **Representation:** Exact SVG map plus a coordinate/dimension table. Dragging and numerical placement modify the same state.
- **Acceptance:** Multiples of 2 m; fixed dimensions; only 0°/90°; no out-of-bounds or overlapping interiors. The entrance's street edge must meet the boundary. Touching boundaries is permitted. A non-square facility's width and height swap while its area remains equal.
- **Prerequisite:** TP-C04. Connection is checked after paths are constructed, not prematurely during facility placement.
- **Help:** A 6 × 10 m rectangle becomes 10 × 6 m, but remains 60 m². Explain the lower-left anchor and upward mathematical y-axis.
- **Evidence:** Accepted positions, attempted invalid moves, a genuine rotation comparison, and before/after geometry fingerprints.

### TP-C06 — Calculate land use without double counting / TP-06

- **Given:** Current valid facility layout; mandatory main paths; editable connectors/green cells; optional expansion rectangle.
- **Required action:** Calculate the two main-path areas, their overlap and union; total path area; green area as fraction/percent; full allocation including undeveloped land. Calculate a designated expansion rectangle when present.
- **Fields and keys:** `land.mainHorizontalM2 = 240`; `mainVerticalM2 = 160`; `mainOverlapM2 = 16`; `mainUnionM2 = 384`. Remaining fields use current cell sets. TP-BASE keys: path 432 m² and 18%; green 480 m², fraction 1/5 and 20%; facilities 704 m²; unused 784 m²; expansion 140 m² if designated.
- **Representation:** Student-completed ledger and color/pattern-coded plan. Highlight the crossroads once. Display exact area totals only after those answers pass.
- **Acceptance:** Areas/fractions exact; accept equivalent fractions, including 480/2400. Required percent fields state “nearest 0.1 percentage point”; apply that instruction consistently to nonterminating values. Also retain exact fractions internally for thresholds. Accept 20 as the percent field's value, not 0.2 unless explicitly entered in a separately labeled decimal-proportion field.
- **Prerequisite:** TP-C05 and current path/green geometry. Positive-area overlaps are structural errors; low landscape percentage or disconnected access is a design finding, not an arithmetic failure.
- **Help:** Two paths with areas 80 m² and 50 m², overlapping by 10 m², occupy 120 m². Explain that painting a cell twice does not create two parcels of land.
- **Evidence:** Union reasoning, current allocation, fraction/percentage, and explicit classification of expansion inside undeveloped land.

### TP-C07 — Calculate construction costs and signed balance / TP-07

- **Given:** Checked land quantities, quoted rates, fixed prices, budget, and the rule including the gate segment in boundary treatment.
- **Required action:** Enter site perimeter and one cost per ledger line, total, signed balance, and reserve percentage.
- **Fields and keys for TP-BASE:** `budget.perimeterM = 200`; `facilitiesCr = 60000`; `pathsCr = 10800`; `landscapeCr = 4800`; `boundaryCr = 4000`; `totalCr = 79600`; `balanceCr = 10400`; `reservePercent = 11.6` to nearest 0.1 percentage point.
- **Representation:** Quantity × rate = cost rows with explicit units; total and balance entered by students before the verified summary appears.
- **Acceptance:** Whole-credit amounts exactly; signed balance may be negative. Format separators are allowed. Compare reserve threshold as `balanceCr ≥ 4500`, not using the rounded percentage.
- **Prerequisite:** Current TP-C06 quantities. Position-only changes that preserve quantities do not invalidate unaffected arithmetic.
- **Help:** At 12 cr/m², an 80 m² zone costs 960 cr. A 1,000 cr budget minus a 1,100 cr cost has balance −100 cr, meaning an overrun.
- **Evidence:** Each line's quantity/rate, total, signed interpretation, rounding policy, and input fingerprint.

### TP-C08 — Inspect, revise, and justify / TP-08

- **Given:** Current mathematically checked Plan A and its exact inspection results.
- **Required action:** Save Plan A, make a material Plan B change under TP-I04, recheck affected work, inspect Plan B, and select the recommended plan. Complete a short stem such as “We changed ___. This changed ___ from ___ to ___. We recommend ___ because ___.”
- **Representation:** Before/after maps and ledgers with changed values highlighted; actual inspector findings linked to map objects or ledger rows.
- **Acceptance:** Both snapshots must be structurally valid and mathematically current. They must have different design fingerprints. The selected numerical comparison must match the two snapshots. Valid equal-cost changes can demonstrate better access or preserved area, but a cosmetic rename alone is not a revision. Do not require a forced improvement or mark a weaker but correctly analyzed alternative as bad arithmetic.
- **Prerequisite:** TP-C01–07 for the relevant plan. Structural errors can be viewed in a draft inspection but must be repaired before this checkpoint is automatically verified.
- **Reflection review:** Check that a choice and numerical evidence are supplied. Free prose/oral reasoning is “Submitted — teacher review”; do not claim automatic semantic evaluation.
- **Help:** Demonstrate adding a 12 m² landscape zone at 10 cr/m², increasing landscape by 12 m² and cost by 120 cr. Explain that one constraint may improve while another becomes harder to meet.
- **Evidence:** Immutable Plan A/Plan B snapshots, affected rechecks, inspection findings, selected plan, tradeoff, and review status. Deliberate deletion of a required snapshot returns this checkpoint to Needs recheck.

### TP-C09 — Individual transfer / TP-09

Two independent variants use the same 1 cm:4 m scale and 2,400 m² site. Each student calculates a fresh pavilion's drawing dimensions, actual area, and percent of site, then gives its drawing dimensions after a 90° rotation. They work away from the shared design; use separate digital turns or printed slips. This records independent response conditions without claiming secure examination software.

| Variant | Actual pavilion | Drawing dimensions | Actual area | Percent of site | Drawing after 90° |
| --- | --- | --- | --- | --- | --- |
| TP-T01 · Partner A | 12 m × 8 m | 3 cm × 2 cm | 96 m² | 4% | 2 cm × 3 cm |
| TP-T02 · Partner B | 16 m × 6 m | 4 cm × 1.5 cm | 96 m² | 4% | 1.5 cm × 4 cm |

Exact values and equivalent fractions pass. Keep dimensions in their labeled width/height order. Area is unchanged by rotation. An optional explanation is teacher-reviewed; no paragraph or grammar score is required. Help and retries remain available but are recorded separately from the first response. Paper evidence stays “Awaiting teacher entry/review” until actually reviewed; merely printing a slip does not complete the checkpoint.

Calculator is available by default for arithmetic checkpoints. Formula setup, classifications, coordinates, and decisions always require student input. In independent transfer, default to scratch paper without the in-app calculator; Teacher Mode may allow it and records that support. Do not claim control over external calculators.

## 6. Geometry and interaction implementation contract

### One authoritative geometry model

Store facility positions as actual-meter integers and rotation enums; derive occupied cells, current dimensions, doors, collision checks, SVG, and printed map from that state. Do not independently store editable pixel coordinates or trust imported derived totals.

Cell `(c,r)` covers `[2c,2c+2] × [2r,2r+2]`, with `c = 0…29`, `r = 0…19`. Use positive-area interior intersection for collisions: shared edges/corners are permitted for objects that otherwise satisfy their rules. For occupancy, half-open cell indexing avoids counting shared boundaries twice.

For a rectangle `(x,y,w,h)`, screen rendering uses `screenX = x × scale` and `screenY = (40 − y − h) × scale`. For a point, use `screenY = (40 − y) × scale`. The visible y labels must always increase upward.

### Rotation and doors

Local coordinates are measured from the unrotated footprint's lower-left. A 90° counterclockwise rotation maps `(u,v)` to `(h−v,u)` and changes dimensions from `w×h` to `h×w`. The current lower-left anchor remains `(x,y)`; the user then repositions if needed. Rotate artwork, door segment, and entrance street edge together. Check the whole proposed result before committing it.

| Facility | Unrotated local door segment endpoints (m) |
| --- | --- |
| Coaster | (8,12) to (12,12) |
| Carousel | (4,12) to (8,12) |
| Theater | (6,0) to (10,0) |
| Food pavilion | (4,0) to (8,0) |
| Services | (6,2) to (6,6) |
| Entrance | Park door: (4,2) to (4,6); street edge: (0,0) to (4,0) |

These segments are TP-I02's proposed interpretation of the source points. At baseline positions their centers reproduce every published door coordinate. A square carousel's rotation keeps the same footprint but changes its door orientation, so it can change connectivity.

For the entrance, orientation 0° places its street edge along the site's south boundary (`y=0`). Under the specified 90° transformation, its street edge lies on its east edge, which must coincide with `x=60`. Those are the two available street-edge orientations in the 0°/90° core model. No invisible access through a building is implied.

### Path connectivity

Build a four-neighbor graph of path cells. Root it at path cells sharing a **positive-length edge** with the entrance facility's park-facing door segment. Flood-fill from those roots. Require at least one root, every path cell reached, and every other facility door touching at least one reached exterior path cell.

Corner contact alone does not connect a door or two path cells. A diagonal chain is disconnected. The minimum walkway width is one 2 m cell; mandatory main paths are 4 m wide. These are simplified classroom access rules, not real engineering approval.

The inherited checker confirms the original baseline but uses inclusive point contact for doors. Its success cannot establish the stronger edge-contact contract. Add dedicated corner-only, rotated-door, disconnected-island, and entrance-root fixtures to the application tests.

### Placement, painting, and undo

- Select a facility and drag, tap a lower-left grid intersection, or enter `(x,y)`; provide a Rotate button and keyboard placement controls. Numerical entry must permit every legal position available by dragging.
- Keep an invalid move as a labeled preview or reject that transaction with a precise explanation; retain the last committed valid placement. Identify the conflicting facility/cell/boundary and offer Undo.
- Main paths reserve their cells even before they are decorated. New facilities cannot cover them.
- Add path/green cells idempotently. Painting an existing path cell again leaves both area and cost unchanged. Require an explicit erase action; do not silently recolor green to path or path to green.
- A rectangle-fill tool and coordinate-range entry must offer non-drag alternatives to painting many cells. Provide named layers and selected-cell details for keyboard users.
- Undo the last accepted geometric edit and restore its associated prior checkpoint state when the input fingerprint is identical. Retain attempt history; undo is not a way to erase recorded mistakes.
- Adding/removing landscape or paths may invalidate expansion designation. Preserve the prior rectangle as a visibly stale draft until repaired or removed; never count an occupied rectangle toward distinction.

Use an exact SVG mathematical-plan mode showing site border, meter axes, scale legend, reserved footprints, doors, grid, dimensions, paths, and pattern-coded land categories. Decorative mode overlays rides/roofs/visitors without changing geometry or collision footprints. Include an accessible coordinate and allocation table.

## 7. Validation, help, and dependency integrity

### Three distinct result classes

| Class | Examples | Behavior |
| --- | --- | --- |
| Academic or structural error | Wrong area, missing required number, invalid unit, off-grid placement, overlap, impossible footprint, incorrect cost | Block affected Check & Continue; identify the cause and preserve valid work. Save, Back, Help, draft inspection, and teacher assistance remain available. |
| Correctly analyzed weak design | Too little green space, disconnected access, excessive path allocation, negative budget balance, no expansion reserve | Accept correct mathematics; show design findings; allow revision and a revision-required report. Do not mislabel the calculated answer as wrong. |
| Teacher-reviewed evidence | Brief design justification, paper transfer, teacher-recorded oral response | Check completeness/format, retain evidence, and report review status honestly. |

An overlap cannot earn a completed academic checkpoint simply by showing a red inspector badge. Conversely, an exactly calculated overrun must not trap the student at the cost-entry step. Draft printing is always allowed, with missing/stale/invalid sections marked.

### Input contract

Accept trimmed whitespace, Unicode minus, valid thousands separators, and exact decimal/fraction equivalents for declared numeric fields. Fractions require a nonzero denominator. Allow mixed numbers only where explicitly documented; the core tasks do not require them. Reject ambiguous decimal commas, nonfinite values, expressions outside the permitted format, and extra text with actionable messages. Do not use `eval()`.

Use fixed unit labels or explicit unit selectors. Lengths use m or cm as requested; areas use m²; currency uses cr. A correct number with the wrong quantity unit does not automatically pass. Coordinate inputs are actual meters, not cell indices. Budget balances are signed; dimensions, areas, and prices are not.

For percentages rounded to 0.1 percentage point, use round-half-up on the exact rational value and display that instruction beside the field. Do not accept arbitrary nearby numbers through a broad floating-point tolerance. Store exact values for opening predicates. The proposed TP-BASE reserve display is 11.6%, while the exact underlying percentage is 104/9%.

Validate on deliberate Check and appropriate blur, not during each incomplete keystroke. Focus an accessible error summary after a failed Check and link to each field. Never clear unrelated correct answers.

### Help and answer visibility

Every substantive field/group has a visible `?` button with a meaningful accessible name. Its panel contains meaning, unit/format, method, and a worked example using different numbers. Close by button, Escape, or tapping outside; no hover-only guidance. Provide a short illustrated glossary for scale, footprint, clearance, union/overlap, perimeter, reserve, and expansion.

The student dashboard can show chosen dimensions, posted rates, and geometric selections. It must not display unchecked requested totals or percentages. Reveal computed totals after the student's relevant entries pass; hide them again when their dependencies become stale. Teacher Reference may show the full keys. Exact geometry is necessarily visible, but automatically answering the current area or cost question is not required to render it.

### Dependency matrix

Keep pure calculations separate from validation and UI. Fingerprint the smallest meaningful input set; do not invalidate the entire session after every edit.

| Edit | Needs recheck | Remains current when unaffected |
| --- | --- | --- |
| Move or rotate a facility | Bounds/collision, door connectivity, expansion validity, plan comparison and outcome | Fixed footprint/circle/triangle areas and costs; unchanged path/green quantities |
| Add/remove editable path cells | Path union total/percent, connectivity, unused area, expansion validity, path cost, total/balance, comparison/outcome | Fixed main-cross overlap calculation; facilities and unchanged landscape calculations |
| Add/remove green cells | Green area/fraction/percent, unused area, expansion validity, landscaping cost, total/balance, comparison/outcome | Facility geometry; path connectivity and path costs |
| Change only expansion rectangle | Its geometry/area, comparison and distinction predicate | Other land quantities and all costs |
| Change park name, alias, or decorative preference | Report labels only | Mathematics and opening eligibility |
| Change a submitted numerical answer | That field and dependent verification/report status | Unrelated answers and their history |
| Change recommendation from A to B | Report's selected-plan link and outcome | Both frozen snapshots and their current evidence |

Each historical response retains the inputs against which it was checked. A later design change never regrades an old answer against new quantities. “Needs recheck” retains the old entry and says what changed. If the exact prior fingerprint is restored, an earlier verified result may be reused with its original evidence intact.

Inspection snapshots are immutable once recorded. Editing one creates a new working revision; it must not silently change the map labeled Plan A. The final report refers to an exact selected snapshot and its content version.

## 8. State, persistence, import, and deletion

### Portable progress contract

Use the shared envelope with project-local content:

```json
{
  "schema": "mcada-project-progress",
  "schemaVersion": "1.0.0",
  "projectId": "theme-park",
  "appVersion": "0.1.0",
  "contentVersion": "1.0.0",
  "sessionId": "locally-generated-id",
  "scenarioId": "TP-BASE",
  "teamAlias": "Pair-04",
  "currentStage": "TP-S04",
  "inputs": {},
  "attempts": [],
  "checkpoints": {},
  "teacherOverrides": [],
  "completedAt": null
}
```

This is an envelope example, not a completed-session fixture. `TP-BASE` identifies the supplied scenario data; it does not mean the student must adopt the teacher's baseline layout. Instantiate the full schema before implementation tests.

Inside versioned inputs, retain partner aliases/roles, park name, facility transforms, sorted path/green cell sets, optional expansion rectangle, numerical field responses, current design revision, named snapshots, recommended snapshot ID, tradeoff evidence, and two transfer records. Checkpoints and attempts store the evidence defined in section 5. Teacher review and override records carry scope, reason, timestamp, and relevant design fingerprint.

Derived areas, costs, connected components, and opening results are recalculated from validated source state on load/import. Never trust imported `approved: true` or a cached cost. An import that changes or omits required evidence cannot silently retain completed status.

### Save behavior

Use namespaced keys such as `mcada:theme-park:session:<id>`, plus a Theme Park session index. Do not call `localStorage.clear()`: other applications share the GitHub Pages origin. Autosave confirmed edits and stage transitions, and show a saved timestamp only after successful persistence.

Provide New Session, Resume, Duplicate for Revision, Export Progress, Import Progress, Delete, and Clear All Theme Park Work. New work receives a new session ID. A duplicate retains provenance but has its own identity and independent future edits.

Test storage with a guarded write/read/delete. If unavailable or full, keep the working session in memory, show “Not saved on this device,” and keep Export available. Detect newer revisions from another tab; offer reload or save-as-copy instead of overwriting silently.

### Import and recovery

Proposed input bound: one UTF-8 JSON file up to 5 MiB, bounded strings and collections, exactly six known facility identities, at most 600 cells per layer, and no duplicate/unknown checkpoint IDs. Document collection limits before coding; at a limit, warn and offer export instead of silently discarding attempts or snapshots. Alias/name fields are capped at 80 characters; reflection/reason fields at 2,000 characters. No imported scripts or markup execute.

Parse into a temporary object; validate schema, project, scenario/content version, ranges, shape types, references, and strings; recompute derived state; then preview and commit atomically. Default to import-as-copy. Replacing an existing session requires an explicit choice and recovery export. Wrong-project, unknown-future-schema, oversized, corrupt, or unsupported-content files leave existing work untouched. Structural validity and academic correctness remain distinct; legitimate unfinished drafts can import with their incomplete/stale status.

Accept compatible application patch versions when schema/content permit. Only implement migrations that are explicitly defined and tested; preserve the original export before migrating. Since this is a new application, do not claim that any historical Theme Park save format has already been migrated.

### U-09 saved-work controls

| Control | Scope and required behavior |
| --- | --- |
| Delete named plan snapshot | Delete the selected user-created snapshot and its exclusively associated evidence/review records. Explain if it is used by the comparison or recommendation; clear dangling references and return those sections to Needs recheck. Preserve unrelated plans. |
| Delete session | Delete its working plan, all snapshots, attempts, transfer evidence, reviews, overrides, and generated-report records. Show the session alias and record counts. |
| Clear all Theme Park work | Remove every Theme Park session and its children from this browser's storage and in-memory selection. Show affected counts. Preserve other projects and fixed curriculum/scenario data. |

Every destructive dialog names the scope, offers Cancel and Export Backup, and requires explicit confirmation. State that deletion cannot be undone without an exported backup; previously downloaded files remain outside the app's control. Never claim success if a required storage operation fails. Reconcile selection/empty state after deletion, and permit a new session immediately. A session's intentional deletion includes all its grouped content; no orphaned history is retained secretly.

Teacher Mode exposes answers, review, diagnostics, support settings, and logged bypasses. It is a classroom convenience, not secure authentication. A bypass yields provisional academic status and cannot turn impossible geometry into a mathematically valid park.

## 9. Outcomes, reports, and printing

### Outcome precedence

1. Missing, stale, or structurally invalid required evidence: **Draft — finish checks**. A diagnostic report is available; do not issue a clean approval.
2. Required gates completed through teacher bypass: **Provisional — review required**. Show the calculated design findings but do not assert unqualified academic completion.
3. Current required mathematics and transfer evidence: apply the critical and stretch predicates below. Append pending prose/oral review and recorded assistance honestly; no automatic mastery claim.

| Design outcome | Predicate | Required narrative |
| --- | --- | --- |
| Opening-day distinction | All critical criteria; balance ≥4,500 cr; one valid designated expansion rectangle ≥100 m² | State actual green percentage, reserve, and expansion area. Decorate the selected map without relocating objects. |
| Park approved | All critical criteria; one or both stretch conditions absent | Identify a successful design feature and the specific unmet stretch condition. |
| Return to the design table | At least one critical criterion fails after correct analysis | Name the actual access/landscape/path/budget failure and its numerical or geometric consequence. Preserve the analysis and offer revision. |

For example, the verified TP-BASE plan opens with 20% green space, 10,400 cr reserve, and a designated 140 m² expansion zone. It is not enough to paste those figures into every ending. Build text from the selected snapshot's data.

### Required saved ending fixtures

All completed ending fixtures must also contain current checkpoint responses, the required Plan A/Plan B comparison, both transfer submissions, and appropriate review status. Geometry alone is not a completed journey.

| Fixture | Layout/data difference from TP-BASE | Expected result |
| --- | --- | --- |
| TP-END-DISTINCTION | Exact supplied baseline; designated expansion `[32,4,10,14]` | Distinction; cost 79,600 cr; balance 10,400 cr |
| TP-END-APPROVED | Same map and calculations; no expansion designation | Approved; same cost/balance; explicitly lacks a designated qualifying rectangle |
| TP-END-REVISION | Remove the green cells in `[0,0,8,2]`; keep other geometry and recalculate | Green 464 m² = 19⅓%; cost 79,440 cr; balance 10,560 cr; revision required for 16 m² green shortfall |
| TP-END-DRAFT | Baseline then edit a relevant input without rechecking | Draft; names stale sections |
| TP-END-PROVISIONAL | Complete a required checkpoint using a recorded teacher bypass | Provisional review; no unqualified approval badge |

The low-green fixture's lower cost must not compensate for failing the landscape requirement. Omitting expansion changes the stretch result without changing costs or unused land. A fully checked low-green plan is a legitimate completed revision-required report.

### Print surfaces

1. **Student Report:** Alias, version, selected plan, student calculations, all land categories, budget, inspections, before/after comparison, first/final attempts, support, transfer, and review status.
2. **Scale Map / Build Sheet:** Exact 150 mm × 100 mm site, 5 mm grid, labeled dimensions, scale legend, footprint/door/path/green/expansion distinction, and coordinate table. Optional paper tiles are an extension, not a release blocker.
3. **Opening Brochure or Inspection Report:** Park name and designed visual; actual outcome with two or three numerical facts. A revision-required design receives an inspection report, not a fictitious opening certificate.
4. **Teacher Reference:** All fixed answers, formulas, source baseline layout, dynamic answer values for the selected plan, ending predicates, common misconceptions, transfer keys, and a concise classroom guide.
5. **Individual Transfer Slips:** Two separately labeled variants; teacher key printed separately.

Use browser print styles for both A4 and Letter, white backgrounds, legible equations/units, page numbering in the paginated report layout, product/version, aliases, and William McAda credit. Include a **5 cm calibration line** and “Print at 100%, not Fit to page.” At the specified scale, this line represents 20 m. Do not resize the mathematical plan to fill a page or equate responsive screen centimeters with real physical centimeters.

Avoid clipped maps, split ledgers, missing SVG layers, or answer leakage into student transfer slips. Test print output in the actual release environment. Paper calibration remains unverified until a physical print is measured; a correct PDF dimension is necessary but not sufficient. If manual print-dialog settings are required, explain them in the teacher guide.

## 10. Visual, accessibility, and runtime requirements

Use an illustrated architect's sketchbook: indigo blueprint lines, controlled bright attraction colors, green landscape zones, and clear white calculation cards. The map is the main workspace. Avoid a grid of tiny dashboard cards that makes the design itself difficult to use.

| Asset ID | Required asset and behavior |
| --- | --- |
| TP-A01 | Title scene with park, design board, and original non-franchise imagery |
| TP-A02–A07 | Six distinct facility illustrations, each with a consistent top-down version |
| TP-A08 | Editable exact grid/site, mathematical-plan toggle, dimensions and coordinates |
| TP-A09 | Inspector overlay showing the actual offending region, access break, or constraint |
| TP-A10 | Opening-day distinction visual |
| TP-A11 | Ordinary approved-plan visual |
| TP-A12 | Revision-required visual |

Ending variations may reuse base artwork but must look and read distinctly. Emoji-only cards, blank gradients, and placeholder boxes do not satisfy the visual contract. Mathematical boundaries, numbers, labels, and scale bars are generated from code, not baked into decorative images. Maintain an asset manifest with ID, purpose, stage, dimensions, alt text, original/source/license status, and whether scale is meaningful.

Use semantic HTML, inline CSS, bundled plain JavaScript, system fonts, and embedded SVG/optimized images. No required CDN, external fonts, math service, live AI, API key, or backend. Source may be organized into local modules for development, then deterministically bundled into the single application. The app must not import another project's file at runtime.

Separate fixed content, exact math, geometry, validation, state/persistence, UI events, reporting, and self-tests. Copy a shared helper only after inspecting its real source and verifying its use here; similarity to Road Trip is not evidence it already meets Theme Park's geometry requirements.

Target at least 44 × 44 CSS-pixel control hit areas, 16 px or larger body/input text, visible focus, readable projection contrast, reduced motion, and no hover-only functions. Required input, error message, Continue, and save state remain reachable with the iPad keyboard open. Use labeled controls, accessible SVG descriptions, a data-table alternative, textual validation, and non-color cues. The map may zoom/pan within its workspace; page controls must not disappear offscreen.

Target standalone HTML size ≤8 MB; review above 12 MB. Embed an asset once and reuse it. These are implementation targets, not current measurements. Privacy is alias-only, local by default, with no analytics, location data, roster collection, automatic submission, or transmitted student work. Public source necessarily exposes the answer logic; do not claim tamper-proof assessment records.

## 11. Verification and acceptance

This is a specification deliverable. Application, browser, physical-device, classroom, and deployment verification are **Not run** because Theme Park Designer has not been implemented in this task.

### Preparation checks actually completed

| Check | Result | Scope and limits |
| --- | --- | --- |
| Retrieve canonical repository, exact source commit, project brief, dossier, fixtures, and applicable handbook | Passed | GitHub reads at the revisions recorded in section 1 |
| Rerun the preserved dossier reference checker | Passed — 77/77 checks | All five projects' supplied reference arithmetic; no application inference |
| Independently check Theme Park specification examples | Passed — 37/37 checks | Baseline rooted paths and positive-edge doors, corner/diagonal rejection, path union/idempotence, scale/print dimensions, area fractions, clearance, reserve/thresholds, expansion accounting, local rotation examples, three mathematical ending cases, and transfer answers |
| Core objective coverage review | Passed | Nine dossier objectives mapped to nine required checkpoint contracts |
| Source conflict review | Passed with clarification | Legacy point-contact check is weaker than entrance-edge rule; TP-I02 is explicitly proposed |
| Build, UI, full saved-session fixtures, printing, physical iPad, network, hosted version | Not run | Future implementation acceptance work |

The 37 checks cover the specification's examples, not exhaustive geometry correctness. The ending checks establish mathematical feasibility, not functioning student journeys or complete progress files.

### Application acceptance matrix

Each Passed result must name the exact candidate commit/hash, test environment, inputs, and evidence. A failed required test must be resolved before the corresponding acceptance claim. Use **Passed / Failed / Not run / Not applicable**, with a reason for Not applicable.

| ID | Required check | Expected evidence | Current result |
| --- | --- | --- | --- |
| TP-Q01 | All nine objectives require observable student action | Objective-to-field map; completed student workflow | Not run |
| TP-Q02 | Source fixtures and dynamic quantities | Independently reproduce 704/432/480/784 m², 79,600 cr, 10,400 cr, and 140 m² expansion | Not run |
| TP-Q03 | Scale and shape misconceptions | 1:400 versus 1:4; area factor 4 versus 2; diameter/radius; triangle half; footprint versus circle | Not run |
| TP-Q04 | Numeric parser and rounding | Blank, malformed, fraction, zero denominator, Unicode minus, thousands separator, wrong units, signed balance, exact percent thresholds | Not run |
| TP-Q05 | Bounds, collisions, grid, and rotation | Edge/corner touching allowed; crossing blocked; correct 90° dimensions and doors; off-grid values rejected | Not run |
| TP-Q06 | Connectivity | Baseline all connected; diagonal/corner-only and isolated-island failures; moved/rotated entrances; correct rooted network | Not run |
| TP-Q07 | Land accounting | Idempotent paint; arbitrary overlapping path additions counted once; green/path/building disjoint; expansion not double-counted | Not run |
| TP-Q08 | Boundary quotation and budgets | Full 200 m charged; exact signed overrun accepted; cost updates follow current cells | Not run |
| TP-Q09 | Constraint boundaries | Path 600 m² passes and 604 fails; green 480 passes and 476 fails; reserve 4,500 passes and below fails; expansion 100 passes and smaller fails; equality at budget passes | Not run |
| TP-Q10 | Feasibility versus academic correctness | Correct low-green, disconnected, over-path, and over-budget designs reach inspection/revision; wrong arithmetic blocks only its gate | Not run |
| TP-Q11 | Selective invalidation | Each edit in dependency matrix changes only appropriate fields; stale work retained; report never presents stale approval | Not run |
| TP-Q12 | Two-plan revision and evidence | Required material edit, immutable snapshots, numerical tradeoff, either recommendation, honest teacher review | Not run |
| TP-Q13 | Individual transfer | Two independent records/slips, withheld shared keys, first/final/support distinctions, paper review status | Not run |
| TP-Q14 | All five report statuses | Complete saved-session fixtures for distinction, approved, revision, draft, provisional; narratives match selected data | Not run |
| TP-Q15 | Save/resume/import/export | Full roundtrip includes geometry, attempts, scene, stage, snapshots, transfer, review; malformed import preserves current work | Not run |
| TP-Q16 | Storage/version conflicts | Denied/full/corrupt storage, cross-tab edits, supported patch versions, future schemas, wrong project/content, recovery export | Not run |
| TP-Q17 | Deletion | Cancel, individual snapshot, session group, clear-all, backup recovery, reload persistence, new-session creation, unrelated projects retained | Not run |
| TP-Q18 | Injection and bounded import | Imported names/reflections never execute HTML/JS; oversize and excessive collections rejected atomically | Not run |
| TP-Q19 | Touch/keyboard/access | All help controls, coordinate placement, painting alternatives, rotation, undo, modal focus, reduced motion | Not run |
| TP-Q20 | Screen layouts | Desktop; iPad portrait/landscape and software keyboard; readable map and reachable controls; physical results named separately | Not run |
| TP-Q21 | A4/Letter exports | Maps, labels, math, ledgers, review/attempt distinctions, page numbers, student/teacher separation, SVG grayscale legibility | Not run |
| TP-Q22 | Print calibration | 150 × 100 mm site, 5 mm cells, 50 mm calibration line; PDF inspection plus measured physical print | Not run |
| TP-Q23 | Visual completeness/offline boundary | All assets embedded; meaningful inspection/ending art; no audio/CDN/runtime network requests; downloaded desktop offline journey | Not run |
| TP-Q24 | Real workflow | Start → deliberate error → correction → design → Plan A/B → transfer → ending → export/import → print | Not run |
| TP-Q25 | Distribution and hosted candidate | Byte-identical versioned HTML/index; actual GitHub Pages path, visible version and assets; exact candidate identification | Not run |

For constraints made unreachable by fixed core settings, use pure-evaluator boundary tests and report that distinction. In particular, the 10% path minimum is covered in the evaluator but cannot be failed by a student who retains the mandatory 384 m² spines. Do not invent UI evidence for an unreachable branch.

Retain the dossier QA-01–20 mapping in the implementation QA report. Scientific-notation-specific QA-05 is Not applicable to this project's construct; applicable general input validation remains required. No classroom concurrency test is required because there is no live multiplayer system. Physical iPad, school-network, and printer checks must be listed as pending until actually performed.

## 12. Implementation, checkpoint, release, and recovery

Use the existing repository. Before coding, retrieve its then-current head, the current handbook, the project brief, and the approved revision of this specification. Do not assume this draft's source commit is still the repository head. Other subprojects may be changing concurrently; limit commits to the intended project and documentation.

**DESIGN → CHANGE SPEC → IMPLEMENT → CHECKPOINT → VERIFY → VERIFIED CHECKPOINT → RELEASE → DEPLOY**

| Stage | Required work and durable record |
| --- | --- |
| DESIGN | Resolve TP-I01–TP-I07 and any amendments; preserve the dossier objectives and constants. |
| CHANGE SPEC | Save the approved revision at the canonical spec path; record approval; create the local PROJECT-BRIEF.md with source, devices, delivery, must-retain requirements, and rule selection. |
| IMPLEMENT | Build pure math/geometry and content contracts first; complete the entire eight-stage journey, evidence, persistence, deletion, artwork, reports, and help. |
| CHECKPOINT | Commit the full source as `Theme Park Designer v0.1.0 implementation checkpoint` before extended verification. Preserve candidate HTML and its hash. |
| VERIFY | Run the required matrix against that candidate; fix failures in identifiable commits; record automated, desktop, physical-device, and classroom evidence separately. |
| VERIFIED CHECKPOINT | Preserve the exact candidate that passed the required checks. State any outstanding physical acceptance; do not transfer old test results to changed executable bytes. |
| RELEASE | Finalize README, release notes, teacher guide, QA record, asset manifest, package identities, and deployment instructions. Introduce no new features here. |
| DEPLOY | Publish the exact checked candidate at the intended GitHub Pages path; verify running version, assets, and a real save/export/import path. A repository commit alone is not deployment. |

Expected project package:

```text
theme-park-designer/README.md
theme-park-designer/CHANGELOG.md
theme-park-designer/ThemeParkDesigner_v0.1.0.html
theme-park-designer/index.html
theme-park-designer/docs/PROJECT-BRIEF.md
theme-park-designer/docs/TEACHER-GUIDE.md
theme-park-designer/docs/ASSET-MANIFEST.md
theme-park-designer/docs/QA-REPORT-v0.1.0.md
theme-park-designer/docs/DEPLOYMENT-v0.1.0.md
theme-park-designer/tests/ [reference cases, geometry, state, UI, and ending fixtures]
docs/change-specs/THEME-PARK-DESIGNER-v0.1.0.md
docs/decisions/THEME-PARK-DESIGNER-v0.1.0-APPROVAL.md
```

Development modules/build scripts may be added locally within the project. There must be no build step for the student to play the delivered HTML. `ThemeParkDesigner_v0.1.0.html` and `index.html` must be byte-identical.

**Intended hosted address:** `https://williammcada.github.io/Applied-Math-Projects/theme-park-designer/`. This is a deployment target, not a verified live Theme Park website.

A packaging, upload, ZIP, final-response, or deployment failure must not trigger reconstruction of the application. Recover the last preserved candidate and its exact evidence. Rebuild only when the source genuinely needs correction, then rerun the checks affected by that correction. Use “implementation checkpoint” or “release candidate” before verification; reserve “verified release” for the exact candidate and scope actually verified.

## 13. Handoff and completion of this specification task

The implementation handoff requires this approved specification, the exact source/handbook revisions, the preserved dossier and fixtures, the project brief, and the actual current source if implementation has started. Historical chat summaries do not replace any of those sources.

**Must retain:** all nine objectives; six facilities; exact top-down mathematics; the occupied-area/footprint distinction; the source scale/geometry/costs; three design outcomes; meaningful revision; individual transfer; narrative visuals; field help; device/input access; local and portable saves; scoped deletion; scale-calibrated reports; branding/version; no audio or runtime service dependency.

**This task produced:** a standalone Markdown specification, with source-grounded requirements, explicitly proposed implementation decisions, exact examples, and future verification criteria. The source arithmetic and stated additional examples were checked as recorded in section 11.

**Not done in this task:** application implementation, application verification, approval of the new decisions, repository modification, handbook modification, or deployment. This document has not been committed to GitHub. Its suggested repository path identifies where the approved specification should be recorded.

**Next decision:** Approve this v0.1.0 specification, including TP-I01–TP-I07, or amend those choices before implementation. No missing essential source prevents that review.


## 14. Production authorization — 30 September 2026

The owner instructed “Proceed with production” after receiving Draft 1. This approves its seven implementation choices and authorizes implementation and the specified GitHub Pages release workflow. Production starts from repository commit `d728dff8f8553f7db5cd26304d9bc403ad790ad9`; handbook remains `00cbde605ab08203b6b5fd2374d225155608fc29`. Section 13 records the completed earlier specification-only task; its no-repository-change statement is historical. This approved revision is now being saved to the canonical repository.
