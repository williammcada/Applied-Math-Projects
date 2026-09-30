# Mars Colony v0.1.0 — Implementation Specification

**Working subtitle:** Red Horizon  
**Specification revision:** Approved revision 1 · 30 September 2026 (Asia/Shanghai)  
**Status:** Approved by William McAda on 30 September 2026 with “Proceed with production.” MC-I01–MC-I08 and the detailed contracts are approved for implementation. Approval does not establish a verified application.  
**Owner:** William McAda  
**Credit:** A WILLIAM MCADA PRODUCT  
**Project ID:** `mars-colony`  
**Target versions:** application `0.1.0`; content `1.0.0`; progress schema `1.0.0`  
**Canonical repository:** [williammcada/Applied-Math-Projects](https://github.com/williammcada/Applied-Math-Projects)  
**Inspected source commit:** `b1f9ae4158631043314e8a88e5f56549cebd319c`  
**Canonical specification path:** `docs/change-specs/MARS-COLONY-v0.1.0.md`  
**Handbook baseline:** v0.1.1, commit `00cbde605ab08203b6b5fd2374d225155608fc29`


> Approval addendum: The owner authorized production on 30 September 2026. The Draft 1 text below is retained as the design record; its statements that repository changes had not yet occurred describe the specification-only delivery. Current implementation baseline: `d728dff8f8553f7db5cd26304d9bc403ad790ad9`. The approved choices apply despite historical “proposed” labels. See `docs/decisions/MARS-COLONY-v0.1.0-APPROVAL.md`.

## 1. Purpose and source authority

Build a complete, independent applied-mathematics experience in which students design an initial research outpost for 24 settlers over ten Earth days. They calculate demand, choose equipment, account for cargo and cost, construct a resource model, and compare ways to withstand three days of reduced solar output.

The central question is: **How do rates, stocks, and capacities interact—and how much reserve makes a system resilient?**

The application must distinguish correct mathematics from a successful design. A student who correctly calculates a shortage has completed valid mathematical work. That shortage delays fictional deployment and invites revision; it must not be mislabeled an arithmetic error.

### 1.1 Sources actually consulted

All project links below identify the inspected commit, rather than an assumed future state of `main`.

| Source | Identity and role |
| --- | --- |
| [Repository README](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/README.md) | Canonical repository, independent applications, release workflow |
| [Family PROJECT-BRIEF.md](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/PROJECT-BRIEF.md) | Brief v0.8; audience, devices, required experience, selected standards and scope boundaries |
| [Original dossier v1.0.0](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md) | Sections 01–12, 28–32 and 39–41 read; Mars objectives, fixed data, screen flow, outcomes, shared delivery requirements. File blob: `e8eea73b4cf8b3b124353b155b72a1c24458c908` |
| [Mars planning README](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/mars-colony/README.md) | Planning placeholder; no Mars application or verified Mars release at this baseline |
| [Change-spec template](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/change-specs/CHANGE-SPEC-TEMPLATE.md) | Specification, checkpoint, verification and recovery structure; its older handbook reference is superseded here by the current baseline |
| [Food Truck specification](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/change-specs/FOOD-TRUCK-v0.1.0.md) | Opening sections consulted for the current specification/approval process; Food Truck mechanics are not Mars requirements |
| [Reference fixtures](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/reference_fixtures.json) and [reference checker](https://github.com/williammcada/Applied-Math-Projects/blob/b1f9ae4158631043314e8a88e5f56549cebd319c/docs/sources/dossier-v1.0.0/verify_reference_fixtures.py) | Original numerical reference data/checks; not application tests |

The handbook files consulted at the exact revision above were [AI-START-HERE.md](https://github.com/williammcada/mcada-project-handbook/blob/00cbde605ab08203b6b5fd2374d225155608fc29/AI-START-HERE.md), [UNIVERSAL-RULES.md](https://github.com/williammcada/mcada-project-handbook/blob/00cbde605ab08203b6b5fd2374d225155608fc29/UNIVERSAL-RULES.md), [CONDITIONAL-STANDARDS.md](https://github.com/williammcada/mcada-project-handbook/blob/00cbde605ab08203b6b5fd2374d225155608fc29/CONDITIONAL-STANDARDS.md), [RELEASE-CHECKLIST.md](https://github.com/williammcada/mcada-project-handbook/blob/00cbde605ab08203b6b5fd2374d225155608fc29/RELEASE-CHECKLIST.md), and its versioned README.

Apply U-01–U-08 as selected project guidance, approved U-09 for saved-work deletion, and S-02/S-04/S-05. Their handbook status remains seeded/draft/approved as recorded there. This specification does not ratify new universal rules. S-01 is not applicable: there is no AI generation/import workflow. S-03 live-game machinery is not required for this paired, locally saved project.

### 1.2 Baseline, decisions and limits

The dossier is the design baseline. Its specified objectives, values, units, representations and outcomes are retained. Classroom defaults and the implementation clarifications below remain proposals until this specification is approved. No essential Mars source was missing. No numerical conflict was found in the inspected Mars examples.

This request is for a Markdown specification. It does not establish a built application, authorize a claim of deployment, or change the series build order. Preparing this document ahead of implementation does not move Mars ahead of the other projects.

**Repository status for this delivery:** the source repository and handbook were read, not modified. This file is the proposed versioned change specification. On approval, save the accepted revision at the destination above, create `mars-colony/docs/PROJECT-BRIEF.md` from the permanent decisions, and record the approval and exact implementation baseline. Do not create a second canonical repository.

## 2. Scope, audience and must-retain requirements

The intended audience is Will’s advanced Grade 5 Introduction to Pre-Algebra / Saxon 8/7 class. Default grouping is two students sharing one iPad, with full desktop keyboard/mouse support. Use ELL-friendly English, metric units, and credits (`cr`). These are authored classroom quantities, not live prices or engineering specifications.

Proposed pacing is three 45-minute lessons:

1. **Demand and capacity:** people, daily/ten-day demand, units, module counts and habitats.
2. **Mission plan:** equipment, supply crate, cargo, cost and resource models.
3. **Resilience:** storm energy, battery balance, comparison, revision and mission report.

Actual timing requires classroom observation. Provide Save/Export throughout; no countdown or speed score. Prompt Planner/Checker role swaps at the lesson boundaries. Pair work and individual evidence remain separate.

### 2.1 Required in v0.1.0

- One fixed mission, eight stages, ten core objectives/checkpoints, five equipment types and two supply packs.
- Water, oxygen, food, habitat, solar energy, battery storage, cargo and cost.
- Student-created equation, numerical table and graph for one selected material resource; a separate daily energy ledger.
- A disclosed, deterministic 25% solar reduction on days 4–6.
- Comparison of a battery strategy with an extra-solar strategy; supported revision and three reachable endings.
- Illustrated introduction, evolving system diagram, useful field help, final outpost reveal and printable mission patch.
- Exact mathematical validation, dependency rechecking, first-attempt and corrected evidence, teacher review and logged bypass.
- Multiple local sessions, JSON export/import, duplicate for revision, deletion and clear-all.
- Student report, teacher reference, versioned standalone HTML and identical deployable `index.html`.

### 2.2 Excluded from v0.1.0

No chemistry, food-growing model, orbital mechanics, real life-support engineering, hourly power model, Martian-sol conversion, scientific-notation strand, action combat, resource-clicking game, multiplayer, student accounts, live teacher dashboard, AI calls, curriculum generator, scenario authoring system, telemetry or automatic submission. Optional physical tokens are not required evidence. No music, audio files or sound-dependent information.

Do not import AAC item counts, benchmark scoring, other-game retry penalties, or another project’s duration. Retain all ten Mars objectives; do not replace them with generic math gates.

## 3. Proposed implementation decisions

These decisions close gaps left open in the dossier. They are local to Mars Colony and included for review; they are not claims of prior approval.

| ID | Proposed decision | Reason |
| --- | --- | --- |
| MC-I01 | Equipment selections allow oxygen/water/habitat counts 0–6, solar arrays 0–8, batteries 0–4; whole numbers only. Mission population, duration, caps and rates are fixed. | Defines small bounded inputs while retaining weak plans and both source strategies. No general editor. |
| MC-I02 | Compute all timelines at the end of each 24-hour Earth day. Day 0 is the initial loaded state; all selected batteries start full. Apply storage caps after that day’s net balance. Track shortages and discarded surplus separately. | Makes the source’s stock and battery examples reproducible without implying hourly engineering. |
| MC-I03 | Resource production is modeled at each selected module’s quoted rate. An electrical shortfall independently fails readiness; resource projections then carry a visible “assumes modules receive full power” warning. Do not invent partial-production or shutdown rules. | Avoids an unspecified cascade model and false scientific precision. |
| MC-I04 | Require a full equation/table/graph for one selected resource: water, oxygen or food. All three resource timelines still appear in the verified report. | Preserves meaningful representation work within three lessons. All three types must be supported. |
| MC-I05 | In the resilience comparison, hold oxygen/water/habitat at 3 each and use the selected crate for both alternatives. Compare 4 arrays + 1 battery against 5 arrays + 0 batteries. The final personal plan may use any permitted configuration. | Makes the battery-versus-solar comparison fair and consistent, even if a student’s own plan is weak. |
| MC-I06 | Freeze the first fully checked personal forecast as the initial plan; retain later revisions and reasons. Require the two-strategy comparison, but permit students to retain their initial configuration after considering it. | Comparison is required evidence; an arbitrary equipment change is not a learning goal. |
| MC-I07 | Teacher mode exposes solutions, reviews, diagnostics and logged bypass. It does not edit fixed mission constants. Offer on-device or printed individual transfer tasks. | Keeps the release bounded and accommodates paired-device classroom practice. |
| MC-I08 | Each saved mission/session is one complete work group. Delete a selected session with all its internal history; provide clear-all for this application. | Implements approved U-09 without creating class/year administration. |

No source prices, consumption rates, capacity limits, storm dates or ending thresholds are changed.

## 4. Fixed content and units

Place this notice in the arrival briefing, teacher reference and report: **“Classroom simulation: these equipment capacities, consumption rates, costs and masses are invented for mathematical modeling. One day means 24 Earth hours.”**

### 4.1 Mission constants

| Source ID | Quantity | Value |
| --- | --- | ---: |
| MC-D01.population | Settlers | 24 |
| MC-D01.days | Mission length | 10 Earth days |
| MC-D01.budget | Budget | 26,000 cr |
| MC-D01.cargo | Cargo limit | 3,400 kg |
| MC-D02.water | Net water use per person | 3 L/day |
| MC-D02.oxygen | Oxygen use per person | 0.8 kg/day |
| MC-D02.food | Food use per person | 0.6 kg/day |
| MC-D03.floor | Required floor area per person | At least 3 m² |
| MC-D04.fixed-load | Other electrical demand | 24 kWh/day |
| MC-D05.storm | Reduced-output days | Days 4, 5 and 6 |
| MC-D05.loss | Reduction from normal solar yield | 25% |
| MC-D06.water-tank | Water storage limit | 400 L |
| MC-D06.oxygen-tank | Oxygen storage limit | 100 kg |
| MC-D06.food-store | Food storage limit | 200 kg |
| MC-D07.cargo-convention | Water mass for this model | 1 L = 1 kg |

The water-mass convention is supplied classroom data. All unit conversion prompts provide the needed relationship: `1 L = 1,000 mL` and `1 kg = 1,000 g`. Students apply the conversion, rather than recall an unstated fact.

### 4.2 Equipment catalog

| Stable ID | Equipment | Production / usable capacity | Electrical demand | Cargo mass | Cost |
| --- | --- | --- | ---: | ---: | ---: |
| MC-EQ-O | Oxygen module | 8 kg/day | 12 kWh/day | 200 kg | 2,000 cr |
| MC-EQ-W | Water module | 30 L/day | 8 kWh/day | 150 kg | 1,500 cr |
| MC-EQ-H | Habitat | 8 settlers; 24 m² floor area | 10 kWh/day | 400 kg | 3,000 cr |
| MC-EQ-S | Solar array | 36 kWh/day normally; 27 during storm | No added load in this model | 100 kg | 1,000 cr |
| MC-EQ-B | Battery | 36 kWh usable storage | No added loss/load in this model | 80 kg | 800 cr |

Use `kWh` for stored energy and `kWh/day` for daily production/consumption. Do not relabel either quantity as `kW`. Battery storage never enters the daily-generation sum.

### 4.3 Exactly two supply crates

| Pack ID | Water | Oxygen | Food | Crate/other supplies mass | Total cargo mass | Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| MC-PACK-STANDARD | 144 L | 38.4 kg | 172.8 kg | 100 kg | 455.2 kg | 1,000 cr |
| MC-PACK-LEAN | 144 L | 38.4 kg | 158.4 kg | 100 kg | 440.8 kg | 800 cr |

Charge the pack once. Count its water, oxygen, food and 100 kg packaging/other supplies once in cargo. Do not multiply the crate by population or days. No custom food amount, extra crate, tank purchase or tank mass is added to this fixed classroom model.

## 5. Mathematical engine

Use pure, independently testable evaluators. Preserve exact decimal/rational values internally. Decimal input must not be graded with a broad floating-point tolerance. Derived quantities, answer keys, UI, report, endings and fixtures use the same declared model.

### 5.1 Demand, module counts and habitat

For population `n=24`:

```text
Daily water demand Dw = 3n = 72 L/day
Daily oxygen demand Do = 0.8n = 19.2 kg/day
Daily food demand Df = 0.6n = 14.4 kg/day
Ten-day totals = 720 L, 192 kg, 144 kg

Minimum oxygen modules = ceil(19.2 / 8) = 3
Minimum water modules = ceil(72 / 30) = 3
Minimum habitats = max(ceil(24 / 8), ceil((3 × 24) / 24)) = 3
```

The intermediate ratios for oxygen and water are both `2.4`; do not round these to 2. Three oxygen modules supply 24 kg/day; two supply 16. Three water modules supply 90 L/day; two supply 60.

For selected habitat count `h`, occupancy capacity is `8h`, floor area is `24h` m², and floor area per person is `24h/24` m²/person. Both occupancy and area requirements apply. Never grade volume as floor area. A mathematically correct analysis of two habitats passes the calculation check but fails housing readiness.

### 5.2 Material stocks

Let selected oxygen/water/habitat/solar/battery counts be `o,w,h,a,b`. Initial stores are supplied by the chosen pack. Daily production is `Pw=30w` L/day, `Po=8o` kg/day, `Pf=0` kg/day.

Before a storage boundary is encountered, the student’s linear rule is:

```text
Rlinear(t) = R0 + (P − D)t
t = number of completed Earth days; 0 ≤ t ≤ 10
```

Interpret the coefficient as net daily change and the intercept as initial stock. It is not enough to type the correct day-10 value. Compare the exact coefficient and intercept of the student expression, not one sampled value.

The authoritative end-of-day ledger is:

```text
raw[t]       = stock[t−1] + production − demand
unmet[t]     = max(0, −raw[t])
discarded[t] = max(0, raw[t] − storageCapacity)
stock[t]     = min(storageCapacity, max(0, raw[t]))
```

Any positive unmet demand fails readiness. A displayed zero after a shortage must retain the unmet quantity; clipping must not hide failure. Surplus above a tank cap is discarded in the model and is not stored reserve. The app must distinguish the unrestricted linear forecast from the capped ledger. Do not draw the unbounded line above a tank cap and label it actual stock.

These are daily net balances. The model does not simulate within-day tank filling, hourly consumption or physical production timing. Resource projections after an energy failure remain conditional as specified in MC-I03.

For `o=w=h=3`, standard supplies:

```text
W(t) = 144 + 18t L
O(t) = 38.4 + 4.8t kg
F(t) = 172.8 − 14.4t kg
```

These three lines remain within their storage bounds through day 10. Final stores are 324 L, 86.4 kg and 28.8 kg. Lean food instead follows `F(t)=158.4−14.4t`, ending at 14.4 kg.

Final reserve days are `stock[10]/dailyDemand`. These ratios describe how long that final stock alone could cover demand with no new production. Compare exact values with the two-day threshold; an optionally rounded display must not change an ending.

### 5.3 Electrical load and storm

```text
Daily load L = 24 + 12o + 8w + 10h        kWh/day
Normal generation Gn = 36a               kWh/day
Storm yield per array = 36(1 − 0.25) = 27 kWh/day
Storm generation Gs = 27a                kWh/day
Daily balance Δ[t] = G[t] − L             kWh/day
```

Negative balance is a deficit. A 25% reduction leaves 75%, not 25%, of normal generation. The three storm days replace normal generation on days 4–6; they are not extra mission days. The event occurs once and does not reroll on reload or revision.

### 5.4 Battery ledger

Total usable capacity is `Bmax=36b` kWh. Initial stored energy is `B[0]=Bmax`. Each daily step is exactly one day, so the numerical daily balance in kWh/day contributes the same numerical amount of kWh during that step.

```text
rawBattery[t] = B[t−1] + Δ[t] × 1 day
unserved[t]   = max(0, −rawBattery[t])
curtailed[t]  = max(0, rawBattery[t] − Bmax)
B[t]          = min(Bmax, max(0, rawBattery[t]))
```

Every modeled day must have zero unserved energy. A battery cannot become negative, exceed usable capacity, create energy, or contribute a recurring daily production rate. With no batteries, `Bmax=B[t]=0`; nonnegative daily generation-minus-load is sufficient. Extra generation is curtailed rather than accumulated invisibly.

For the baseline, load is 114 kWh/day. Four arrays produce 144 normally and 108 during the storm. A full battery remains at 36 through day 3, then ends days 4–6 at 30, 24 and 18. On day 7 the +30 balance restores it to 36 and curtails 12 kWh. Days 8–10 remain capped at 36.

For five arrays and no battery, generation is 180 normally and 135 during the storm, so all modeled days meet the 114 load. The model does not establish continuous nighttime power or real 24-hour operational safety; that limitation is visible in the comparison and report.

### 5.5 Cost and cargo

```text
Cost = 2,000o + 1,500w + 3,000h + 1,000a + 800b + packCost     cr
Mass = 200o + 150w + 400h + 100a + 80b + packMass             kg
Budget reserve = 26,000 − Cost                               cr
Cargo reserve = 3,400 − Mass                                 kg
```

Zero reserve is allowed. Negative reserve is an overrun, not incorrect arithmetic. Keep the two reserves separate; do not subtract or rank raw kilograms against raw credits. If asking which cap is tighter, compare the used fractions `Cost/26000` and `Mass/3400`, with displayed percentages rounded to the nearest 0.1 percentage point only after the exact calculation. Exact ratios determine any comparison and tie.

## 6. Student journey and stage gates

Persistent controls show the project/version, stage/progress, alias, current plan label, save status, Back, Save, Export progress and Help. Each screen has one clear task. Future stages identify their prerequisites. Mathematical errors block only the affected progression; valid weak plans can reach analysis and the delayed-deployment report.

Do not reveal expected totals in a dashboard, tooltip, diagram, example or preview before the corresponding student calculation is checked. Given rates, capacities and initial stocks remain visible. Teacher mode may reveal answers explicitly.

| Stage | Required experience | Completion condition |
| --- | --- | --- |
| MC-S01 Arrival request | Illustrated outpost; mission/team alias, two learner aliases, Planner/Checker roles. Confirm population, ten Earth days, both caps, the disclosed storm and fictional-model notice. | Valid setup and acknowledgments; no academic score for reading the brief |
| MC-S02 Demand console | Calculate three daily and ten-day demands. Classify stock/rate units and convert supplied quantities. Reveal labeled demand arrows after checking. | C01–C02 current |
| MC-S03 Module bay | Calculate minimum water/oxygen counts; check habitat occupancy and area. Then select a complete provisional equipment plan, including arrays/batteries. No correct-count answer is prefilled before the minimum-count task. | C03–C04 current; selections structurally valid even if strategically weak. End lesson 1: export and swap roles |
| MC-S04 Supply manifest | Select standard/lean pack. Calculate equipment line costs/masses, pack mass, total cost/mass and signed reserves. | C08 current; correct overspending/overloading does not block analysis |
| MC-S05 Resource forecast | Select water, oxygen or food. Build a rule, fill day 0–10 values, plot required points and identify boundaries/shortages. Reveal verified timelines and first checked plan snapshot. | C05 current. End lesson 2: export and swap roles |
| MC-S06 Storm briefing | Display the one scheduled dust event. Calculate current electrical load, remaining solar percentage, per-array output, total generation and signed normal/storm balances. | C06 current |
| MC-S07 Resilience test | Complete battery/energy ledger; compare both strategies; return to earlier selections for a revised final plan. Recheck only affected work. Record recommendation and one model limitation. | C07–C09 current and all affected prior work current |
| MC-S08 Mission control | Show critical criteria, actual plan-specific ending, system reveal and patch. Obtain individual transfer evidence, then print/export. | Final report status follows section 11; missing/stale work permits Draft, and bypass permits Provisional |

The two strategy cards in S07 are comparison tasks, not a hidden rule that the personal plan must equal one of them. Students may finish a correctly analyzed delayed mission and later revise it without starting over.

## 7. Checkpoint contracts

### 7.1 Shared field contract

Every substantive field/group is declared in a fixed content registry with:

```text
id, checkpointId, objectiveId, stageId, prompt, sourceIds,
allowedRange, operation, inputDimension, outputDimension,
representation, acceptedForms, evaluatorId, unitPolicy,
precisionPolicy, prerequisiteFieldIds, help, errors, evidence,
teacherReviewPolicy
```

The tables below define the required content. During implementation, expand repeating table/graph/day fields using stable suffixes, such as `C05.table.day04` and `C07.battery.day06`. Do not generate IDs from display order or localized labels.

Common rules apply unless a row specifies otherwise:

- Exact finite numbers; whole counts within MC-I01; blanks are not zero. Permit exact equivalent decimals/fractions for instructional quantities unless a count or representation specifically requires otherwise.
- Each numeric quantity has a visible unit or explicit unit selection. Required unit classification is checked separately from numerical equivalence.
- Normalize spaces, Unicode minus, multiplication signs and valid thousands separators. Reject ambiguous decimal commas, malformed fractions, division by zero and nonfinite values with useful messages.
- No `eval`, substring marking or checking a linear expression at just one input. Restrict the expression parser to numbers, `t`, parentheses and arithmetic needed to reduce an expression to exact coefficients `(m,b)`. Reject nonlinear expressions and undeclared variables.
- Do not require trailing zeros, a particular term order, or a particular equivalent fraction unless that representation is the stated target.
- Exact fractions are accepted for repeating results. Optional display rounding never changes a threshold. Area/count/resource answers in the base mission need no hidden rounding.
- All submitted checks record original raw entry, normalized answer, result, context, support and timestamp. Editing without pressing Check is not an academic attempt.
- Free prose receives completeness/review status, not automated claims of semantic correctness. An oral response can be recorded by the teacher.

### 7.2 C01–C04: demand and physical capacity

| Checkpoint / objective | Required fields and response | Evaluator, dependencies and evidence |
| --- | --- | --- |
| C01 / MC-01 | `daily.water`, `daily.oxygen`, `daily.food`; `total.water`, `total.oxygen`, `total.food`. Prompt: “Calculate what 24 settlers need each day and over ten Earth days.” | MC-D01/02. Answers: daily 72 L, 19.2 kg, 14.4 kg; ten-day 720 L, 192 kg, 144 kg. Daily fields are labeled per day. Record all six answers and units. |
| C02 / MC-02 | Classify the six units L, L/day, kg, kg/day, kWh, kWh/day as stock or rate. Convert 0.8 kg to g, 3 L to mL, and 19,200 g to kg. | Supplied unit relationships; answers 800 g, 3,000 mL, 19.2 kg. Record each classification and conversion; no dependence on selected equipment. |
| C03 / MC-03 | For both water and oxygen: `ratio`, `minimumCount`, `capacityAtMinimum`, `capacityOneFewer`; explain the need for a whole module using a structured comparison. | Uses checked C01 daily needs and catalog. Ratios 2.4; counts 3; water capacities 90/60 L/day and oxygen 24/16 kg/day. Correct minimum calculation is separate from later selected count. |
| C04 / MC-04 | `minimumHabitats`, `selectedCapacity`, `selectedArea`, `areaPerPerson`, `occupancyMet`, `areaMet`. | Uses population, MC-D03 and selected `h`. Minimum 3; capacity `8h`; area `24h`; area/person `h`. Both classifications must agree with the chosen count. Record true/false even when housing fails. |

C03 help uses different numbers: demand 50 L/day and capacity 20 L/day give ratio 2.5, so three whole modules are needed. Feedback distinguishes “minimum required” from “number currently selected.” C04 help explicitly contrasts m² floor area with m³ volume.

### 7.3 C05: resource equation, table and graph

**Objective:** MC-05. **Sources:** initial pack stock, selected production modules, C01 demand, fixed storage limits. **Fields:** `resourceId`, `initialStock`, `production`, `consumption`, `netChange`, `rule`, `firstBoundaryDay`, `table.day00…day10`, `graph.axisX`, `graph.axisY`, `graph.points`, and `limitation`.

Require the unrestricted rule `R0+(P−D)t` and the interpretation “valid as actual stock only until a boundary is reached.” Students also identify whether the selected trajectory encounters a cap or shortage during days 1–10, with the first affected day or “none.” The exact evaluator calculates that day from the recurrence in section 5.2. No typed piecewise-expression parser is required.

The table covers day 0 and all ten end-of-day values. For days with discarded material or unmet demand, the table includes the affected quantity, not only a clipped stock. Students calculate the selected resource; the remaining two resource tables can be revealed after the selected model is checked.

The student labels the horizontal axis “Completed Earth days” and the vertical axis with the selected resource and stock unit. Require ordered pairs at days 0, 1, 3, 6 and 10, plus the first storage-boundary day if it is a different day. Use exact snapped coordinates or typed pairs. Render a verified SVG plot only after the required points and labels pass. Fixed horizontal ticks run 0–10. The vertical range covers 0 to the selected tank/storage capacity, with readable major ticks and an accessible value table. A line between daily points is illustrative; the authoritative model is discrete daily accounting.

Record the student expression, coefficient/intercept, table, plotted points, cap/shortage interpretation and current dependency fingerprint. Graph/table correctness is required evidence, not a decorative chart automatically completed on behalf of the student.

### 7.4 C06–C07: power and finite storage

| Checkpoint / objective | Required fields and response | Evaluator, dependencies and evidence |
| --- | --- | --- |
| C06 / MC-06 | Load contributions from fixed demand, oxygen, water and habitats; `totalLoad`, `remainingPercent`, `normalGeneration`, `stormPerArray`, `stormGeneration`, `normalBalance`, `stormBalance`. | Equipment selections and MC-D04/05. Remaining 75%; storm 27 per array. Full baseline: 114 load, 144/108 generation and +30/−6 balances. Persist signed quantities with kWh/day. |
| C07 / MC-07 | `batteryCapacity`, `initialEnergy`, `totalStormDeficit`; daily ledger for days 1–10 with generation, load, balance, starting energy, ending energy, unserved and curtailed energy; `allDaysCovered`. | Current C06 plus selected batteries. Exact capped recurrence. Initial energy is full capacity. Three-day deficit is `3×max(0,L−27a)`; a plan can also fail on normal days, so that subtotal does not replace the ten-day test. |

Prefill immutable given columns and previously checked quantities, not the new battery answers. Students enter each daily ending energy and any nonzero unserved/curtailed amount; unchanged runs may be entered through an explicitly labeled “same value for these days” control. They must still see every daily row.

Helpful feedback includes “A battery stores kWh; it does not produce kWh each day” and “The calculated balance is negative. Record the uncovered amount; stored energy cannot go below zero.” A correct zero with an omitted shortage fails the ledger check.

### 7.5 C08–C10: limits, comparison and transfer

| Checkpoint / objective | Required fields and response | Evaluator, dependencies and evidence |
| --- | --- | --- |
| C08 / MC-08 | Every equipment line’s cost/mass, pack mass, total cost/mass, budget/cargo reserves, both cap classifications. | Selected `o,w,h,a,b,pack`; section 5.5. Negative reserves accepted when correct. Require the reasoning distinction between budget and cargo; no unitless combined score. |
| C09 / MC-09 | Complete the two comparison configurations: normal/storm output, load, end-storm battery, cost, cargo, reserve status. Select recommendation; cite one numerical tradeoff, one benefit and one remaining model limitation. Retain/revise the personal plan with a reason. | Fixed comparison resource modules plus current pack. Exact numerical comparison; prose submitted for teacher review. Both strategies valid; no compulsory preference for batteries or extra solar. |
| C10 / MC-10 | Separate transfer response for each learner. Retain first checked answer, corrections, help and review status independently of pair work. | Transfer tasks below; either on-device checking or printed responses reviewed by teacher. Pair outcome does not certify individual mastery. |

**C09 comparison:** With standard supplies, 4 arrays/1 battery cost 25,300 cr and weigh 3,185.2 kg; 5 arrays/0 batteries cost 25,500 cr and weigh 3,205.2 kg. The extra-array design adds 200 cr and 20 kg, produces 27 kWh/day more during the storm, and avoids the modeled deficit. The battery design ends the storm with 18 kWh stored. With lean supplies, subtract 200 cr and 14.4 kg from both plans; both then have only one day of final food reserve.

Numerical evidence is checked against the actual comparison snapshot. The limitation may address constant demands, ideal daily timing, omitted losses, preloaded batteries or omitted real life-support conditions. A generic sentence is not automatically graded as a scientifically sound explanation.

**C10 proposed transfer tasks:** Give the relevant rate and module capacity in each prompt.

- Learner A: 30 settlers use 3 L/person/day; each water module produces 30 L/day. Find daily demand, ten-day demand, demand/capacity ratio and minimum module count. Answers: 90 L/day, 900 L, 3, 3.
- Learner B: 28 settlers use 0.8 kg/person/day; each oxygen module produces 8 kg/day. Find the same four quantities. Answers: 22.4 kg/day, 224 kg, 2.8, 3.

Both learners give a short capacity justification. These tasks are formative evidence, not psychometrically equivalent test forms. Sequential device screens reduce answer exposure but do not prove independent work; the teacher supervises or uses the printed slips. Printed mode records “assigned/pending review” until the teacher enters a result. It must not falsely mark an unreviewed paper answer correct. An assigned but unfinished transfer leaves academic completion pending while the pair’s modeled design outcome remains visible.

## 8. Validation, help and accessibility

Each substantive field or coherent field group has a visible `?` button, with an accessible name such as “Help: battery capacity.” Its four parts are meaning, unit/format, what to do, and an example with different values. It works by touch and keyboard; Close, Escape and outside tap dismiss it. Help carries no score penalty.

| Condition | Required response |
| --- | --- |
| Blank, malformed, impossible count or wrong calculation | Block affected Check & Continue; identify the field and correction; preserve other entries |
| Correctly calculated shortage, overrun or inadequate capacity | Accept mathematics; show the exact failed design criterion and allow analysis/revision |
| Stale dependent work | Keep entered answers; show Needs recheck with the changed parent named |
| Prose/oral interpretation | Submitted/pending teacher review; no automatic semantic score |
| Storage/import failure | Preserve current in-memory work; explain recovery/export route without claiming success |

Validate on deliberate Check or appropriate blur, not on every partial keystroke. Focus the error summary after an unsuccessful check; link to each affected field and announce status accessibly. Color supplements text, symbols and labels. Avoid disruptive browser alerts.

Use at least 16 px body/input text and 44×44 CSS-pixel targets for primary controls and help. Support visible focus, semantic labels, accessible tables, SVG titles/descriptions, reduced motion and non-drag alternatives. On-screen keyboards must not hide the focused answer, its unit, error or primary action. Test iPad portrait/landscape and desktop without horizontal overflow or nested-scroll traps. Phone support is not a release claim for this project.

Keep instructional prompts short—normally one action per sentence and under 45 words excluding data. Use a small illustrated glossary for habitat, stock, rate, reserve, demand, production, surplus, deficit, capacity and model. Do not score grammar or require paragraphs.

Calculator support is field-specific: allow numerical arithmetic after students choose an operation; students must still provide units, a model, classifications and capacity reasoning. No “solve current task” button. Show when help or teacher assistance was used.

## 9. Dependency and revision rules

Store a dependency fingerprint with every checked field/checkpoint, containing the relevant input values, content revision and plan identity. Editing a parent marks only affected downstream evidence Needs recheck. Keep previous answers and attempts with their original context; never compare a historical response against a newly changed plan.

| Change | Evidence requiring recheck | Evidence retained as current |
| --- | --- | --- |
| Selected oxygen count | Oxygen stock model if selected; oxygen projection; load/energy; manifest; final criteria/outcome | Fixed demands/units, minimum-count calculation, unrelated water/food academic model |
| Selected water count | Water stock model if selected; water projection; load/energy; manifest; final criteria/outcome | Fixed demands/units, minimum-count calculation, unrelated oxygen/food academic model |
| Selected habitats | Selected habitat calculations; load/energy; manifest; final criteria/outcome | Demands, material-stock equations/tables unless other inputs changed |
| Selected arrays | Normal/storm output and balances, battery ledger, manifest, final criteria/outcome | Demands, habitat, water/oxygen/food models |
| Selected batteries | Battery capacity/ledger, manifest, final criteria/outcome | Module demand/load, solar generation, material-stock models |
| Supply pack | Food model if selected; manifest; food reserves; comparison costs/cargo/reserve interpretation; final criteria/outcome | Water/oxygen initial stock and models, electrical load/generation |
| Selected graph resource | C05 model/table/graph for that resource | Completed other objectives; retain prior model as history |
| Alias or display name | Report/patch display metadata | All academic calculations |

The fixed strategy comparison has its own fingerprint. A personal array/battery change does not invalidate its numeric results when its fixed comparison inputs are unchanged, but a recommendation relying on the old personal plan needs review. A crate change affects both comparison packs.

An upstream edit cannot silently keep an approved report current. Print previews show stale fields. Any previously downloaded report remains an external historical snapshot; the app cannot revoke or erase it.

## 10. State, saving, import and deletion

### 10.1 Architecture and save envelope

Use semantic HTML, inline CSS and bundled plain JavaScript, with embedded SVG or optimized data-URI art and system fonts. Organize fixed data, state, mathematical evaluation, answer parsing, validation, rendering, persistence and reporting separately within the project. Copy suitable reviewed helpers if useful; no dependency on another project’s HTML or a shared service.

Use the dossier envelope with Mars identities:

```json
{
  "schema": "mcada-project-progress",
  "schemaVersion": "1.0.0",
  "projectId": "mars-colony",
  "appVersion": "0.1.0",
  "contentVersion": "1.0.0",
  "sessionId": "locally-generated-id",
  "scenarioId": "MC-BASE",
  "teamAlias": "Pair-04",
  "currentStage": "MC-S01",
  "inputs": {},
  "attempts": [],
  "checkpoints": {},
  "teacherOverrides": [],
  "completedAt": null
}
```

The full schema must additionally declare learner aliases, selected equipment/pack/resource, initial and revision snapshots, comparison evidence, transfer evidence, teacher reviews, save revision, creation/update times and per-checkpoint fingerprints. Use integer counts and exact numeric strings for instructional quantities. Internal field IDs are stable across compatible patches.

A checkpoint stores status, current response, first checked response, attempt count, help/support used, dependency fingerprint and evidence references. Attempts identify the field/checkpoint, plan/scenario revision, response, result and timestamp. Imported “correct” flags are not authority: recompute current validators/fingerprints and derived totals before trusting completion.

### 10.2 Persistence behavior

Use `mcada:mars-colony:session:<id>` and a namespaced session index. Multiple apps may share a GitHub Pages origin. Never call `localStorage.clear()` or delete another project’s keys.

Autosave confirmed edits and transitions. Display “Saved on this device” and a timestamp only after success. Test storage availability with a guarded write/read/delete. On denial/quota/corruption, retain work in memory, display a persistent export reminder and keep JSON export functional. Do not promise that desktop `file:` storage behaves identically across browsers.

Provide New Session, Resume, Duplicate for Revision, Export Progress, Import Progress, Delete Session and Clear All Mars Colony Work. New Session creates a distinct ID. Duplicate retains the chosen starting work but receives a new ID and creation metadata; it does not overwrite the original. Detect a newer saved revision from another tab and offer reload or save-as-copy instead of silently merging.

### 10.3 Import contract

Proposed limits: 5 MiB per JSON file; aliases up to 40 characters; comments/reflections up to 1,000 characters each; at most 10,000 attempt records per session. Enforce bounded arrays/strings/depth and known keys/types. Never silently truncate history. If the session approaches an attempt limit, offer export and an explicitly identified new revision session with the previous one preserved.

Parse into a temporary object, validate and preview before committing. Check schema, project/content identity, bounded equipment counts, allowed pack/resource/stage IDs, finite values, known checkpoint IDs and structurally consistent histories. Reject future/unsupported schemas or content, wrong-project files, malformed JSON, HTML/script payloads and impossible states without changing the current session. Render imported text as text, never executable HTML.

Default import creates a copy if its session ID already exists. Replacing a known session requires an explicit preview/confirmation and backup opportunity. Supported older-schema migration preserves a raw backup. App patch differences alone do not justify rejection; v0.1.0 need not invent migration from a nonexistent earlier Mars schema.

### 10.4 Approved U-09 deletion behavior

A saved session is the record and complete grouping: inputs, attempts, both learner responses, initial/final plans, comparison, reviews, overrides and report metadata belong to it. There are no separately managed school years or classes.

Delete Session names the alias/session and explains that its complete stored history will be removed. Clear All lists the number of Mars sessions affected. Both offer Export/Backup, Cancel and explicit confirmation; explain that recovery requires an exported file when no undo is offered. Remove associated state/index entries and update the active selection/empty state. Deleting the active session cancels pending autosaves so it cannot reappear accidentally.

Preserve unrelated sessions on individual deletion, other projects, fixed curriculum and already downloaded files. In-memory-only sessions also have a clear/reset path. Verify cancellation, successful persistence after reload, failure reporting, fresh creation and backup import. These implementation tests use disposable test data, not the user’s actual saved work.

## 11. Readiness, endings and evidence

### 11.1 Critical design criteria

Every criterion uses the final current configuration, not the reference example.

| ID | Passing condition |
| --- | --- |
| MC-R01 Housing | `8h ≥ 24` and `24h/24 ≥ 3 m²/person` |
| MC-R02 Water production | `30w ≥ 72 L/day` |
| MC-R03 Oxygen production | `8o ≥ 19.2 kg/day` |
| MC-R04 Food | Initial food ≥144 kg; no daily food shortage |
| MC-R05 Material storage | Initial stores within stated caps; no modeled unmet water/oxygen/food demand; all retained stocks remain within caps |
| MC-R06 Energy | Zero unserved energy on every day 1–10, with battery capacity respected |
| MC-R07 Budget | Total cost ≤26,000 cr |
| MC-R08 Cargo | Total mass ≤3,400 kg |

Daily self-sufficient water/oxygen production is a separate source requirement. A plan with two water modules still has 24 L at day 10, but fails MC-R02 because it produces 60 against demand 72. Remaining initial stock does not excuse that criterion.

### 11.2 Outcome precedence

1. Missing or stale required pair calculations: **Draft — finish checks**. Show diagnostic design projections without presenting them as an approved final plan.
2. Any active bypass of a required academic gate: **Provisional — teacher review**. The modeled outcome may be shown with that qualifier, never as independently verified academic evidence.
3. Otherwise determine the story outcome below. Pending prose review or paper transfer is separately labeled; it does not turn an unreviewed statement into correctness.

| Story outcome | Exact predicate | Required feedback |
| --- | --- | --- |
| Resilient outpost | All critical criteria pass and each final water/oxygen/food store covers at least two days of its demand | Identify actual configuration and reserve evidence; include storm performance |
| Mission ready | All critical criteria pass but at least one final material reserve is under two days | Identify every sub-two-day reserve and its exact/clearly rounded duration |
| Deployment delayed | One or more critical criteria fail | Name each shortage, housing gap, production shortfall, cap overrun or unserved-energy day; allow revision |

Equality at the cost/cargo limit and exactly two reserve days passes. Stored battery energy is not one of the three material-reserve thresholds. A battery-free plan can reach Resilient outpost.

Outcome copy must be generated from the selected configuration. Do not reuse “your four arrays and battery” for the five-array/no-battery alternative. Failure means approval is postponed, never deaths, gore or ridicule. The reveal includes two or three actual decisions and their numerical consequences.

### 11.3 Learning report

Keep three panels distinct: **mathematical evidence**, **design readiness**, and **teacher review/individual transfer**. Final corrected answers do not by themselves prove independent mastery. Report first-attempt results, corrections, support and overrides. No automatic gradebook mark, speed reward, hidden weighted score or leaderboard. The dossier’s optional 20-point rubric remains optional teacher guidance, not an implemented default score.

## 12. Visual and print requirements

The visual direction is an inviting mission console: rust-colored landscapes, slate backgrounds, ivory work panels, cyan system lines and amber caution. Use large math workspaces and a small research outpost. Avoid dense game HUDs and corporate-dashboard styling.

| Asset ID | Required artwork / function |
| --- | --- |
| MC-A01 | Illustrated Mars horizon/title scene |
| MC-A02–MC-A07 | Six distinct water, oxygen, food, habitat, solar and battery illustrations |
| MC-A08 | Evolving authoritative system diagram with separate production arrows, demand arrows and storage boxes; each value labeled with its own unit |
| MC-A09 | Dust-reduced solar scene used in storm briefing |
| MC-A10 | Operational/resilient outpost ending |
| MC-A11 | Operational outpost with limited-reserve ending |
| MC-A12 | Delayed-deployment ending with specific readiness concerns |
| MC-A13 | Personalized mission patch with alias, selected configuration and project/version |

Narrative art can be original SVG or embedded raster art. Mathematical labels, numbers, axes and scale information must be code-rendered. Do not bake uncertain values into generated images. Record each asset’s purpose, stage, dimensions, alternative text, source/license or original-art status and whether it represents scale. The source concept image is a design reference, not evidence of a working app.

Graph and system diagram are SVG with accessible data equivalents. No mixed-unit unlabeled resource axis; energy has its own display. Animations are optional, reduced-motion aware and skippable. Pictures cannot be replaced by emoji cards or placeholders.

Aim for ≤8 MiB per standalone HTML and require review above 12 MiB. Embed required assets once where possible. No runtime font/CDN/art/audio fetch is needed.

### 12.1 Required printable outputs

**Student Mission Readiness Report:** project/version/content revision, alias, mission assumptions, equipment and crate, labeled system diagram, demands, habitat evidence, itemized cargo/cost and signed reserves, student resource equation/table/graph, all three verified material timelines, storm/battery ledger, comparison, initial/final revisions, outcome criteria, teacher-review status and separate individual evidence. Include the classroom-model notice and daily-time limitation.

**Teacher Reference:** fixed data, accepted forms, complete baseline/comparison/lean answers, all outcome predicates, misconception guidance, transfer answers, bypass meanings and model limitations.

**Mission Patch and Transfer Slips:** a printable commemorative patch and the two individual tasks. The patch is not a mathematically scaled construction template; no physical-size calibration requirement is introduced. Optional token sheets are outside the core release.

Use white backgrounds, readable grayscale, page numbers, units and visible product credit. Test A4 and Letter. Keep table headers with rows, prevent clipped equations/figures, and ensure SVGs print. Draft and Provisional reports are permitted and clearly labeled. Screenshots of the UI do not satisfy the report contract. DOCX export is not required.

## 13. Reference cases and preparation checks

### 13.1 Required numerical fixtures

Tuple order below is `(oxygen, water, habitat, solar, battery)`.

| Fixture ID | Configuration / condition | Expected result |
| --- | --- | --- |
| MC-F01 | Daily and ten-day demands | Daily 72 L / 19.2 kg / 14.4 kg; mission 720 L / 192 kg / 144 kg |
| MC-F02 | Standard, `(3,3,3,4,1)` | Load 114; cost 25,300; cargo 3,185.2; reserves 700 cr and 214.8 kg; end stocks 324 L / 86.4 kg / 28.8 kg; Resilient outpost |
| MC-F03 | Baseline battery | Day 0–3: 36 kWh; day 4:30; day 5:24; day 6:18; day 7–10:36. Day 7 curtailment 12 kWh |
| MC-F04 | Standard, `(3,3,3,5,0)` | Normal/storm generation 180/135; cost 25,500; cargo 3,205.2; zero unserved energy; Resilient outpost |
| MC-F05 | Lean, `(3,3,3,4,1)` | Cost 25,100; cargo 3,170.8; final food 14.4 kg, one day; Mission ready |
| MC-F06 | Lean, `(3,3,3,5,0)` | Cost 25,300; cargo 3,190.8; Mission ready |
| MC-F07 | Lean, `(3,3,3,4,2)` | Cost 25,900; cargo 3,250.8; battery 72 initially and 54 at day 6; Mission ready |
| MC-F08 | Standard, `(3,3,3,4,0)` | Normal surplus 30; storm shortage 6 kWh on each of days 4–6, total 18; Deployment delayed |
| MC-F09 | Standard, `(3,3,3,3,0)` | Shortage already 6 kWh on day 1; storm shortage 33/day; Deployment delayed |
| MC-F10 | Standard, `(3,3,2,4,1)` | Occupancy 16; floor area 48 m²; 2 m²/person; Deployment delayed |
| MC-F11 | Standard, `(3,2,3,4,1)` | Water production 60 L/day; final stock 24 L; fails production readiness despite nonnegative stores |
| MC-F12 | Four water modules with standard initial stock | Net +48 L/day; day 5 stock 384 L; day 6 raw 432, retained 400, discarded 32; later stock remains capped |
| MC-F13 | No water/oxygen production | Initial reserves exhausted at end of day 2; day 3 unmet water 72 L and oxygen 19.2 kg, with zero retained stock |
| MC-F14 | Teacher/academic status | Missing/stale required pair work gives Draft; active required-gate override gives Provisional; free-prose or paper review remains explicitly pending |

Final reserve days for the standard baseline are 4.5 water, 4.5 oxygen and 2 food. The alternative solar plan has the same material stores because production/consumption/pack are unchanged.

### 13.2 Feasible configuration audit

A preparation-only enumeration examined all 30,870 configurations in the proposed bounded catalog: `7 × 7 × 7 × 9 × 5 × 2`. Under the stated model, exactly five meet critical readiness: MC-F02, F04, F05, F06 and F07. Two achieve Resilient outpost and three Mission ready. The remaining configurations produce Deployment delayed if their academic work is complete and current.

This is a teacher/developer feasibility audit, not student-facing answer disclosure. It confirms that the intended endings and both strategies are reachable, and that the lean two-battery alternative must not be rejected merely because it differs from the baseline. The narrow feasible set is a consequence of the supplied budget/data; do not quietly change the budget or enforce a single preferred configuration.

### 13.3 Checks actually run while preparing this document

| Check | Result | Evidence / limit |
| --- | --- | --- |
| Current repository, Mars design and applicable handbook read | Passed | Exact source and handbook identities recorded in section 1 |
| Original dossier reference checker rerun | Passed | 77/77 arithmetic/geometry reference checks; includes the source Mars examples. This is a source-data check across the dossier, not an application test |
| New Mars reference/boundary arithmetic | Passed | 34 exact-arithmetic assertions using Python rational numbers; demand, baseline, extra solar, lean, storm, recharge, caps, shortages and transfer calculations |
| Proposed bounded-catalog feasibility | Passed | 30,870 configurations evaluated using a separate integer-scaled calculation; all three story branches reachable |
| Actual Mars HTML, browser, save, import, print and deployment | Not run | No Mars application was built in this task |
| Physical iPad, school network and printer | Not run | Requires the later implementation and real classroom equipment |

Specification checks do not establish software correctness. The implementation must reproduce these cases using its own evaluator and UI. Preserve test inputs/expected results in the canonical repository during implementation; do not transfer a Passed label from this specification to an untested candidate.

## 14. Application verification and acceptance

Use the dossier QA-01–20 and handbook release checklist, with the following Mars-specific coverage. Record the exact candidate commit/file hash, environment, inputs, expected/actual result and **Passed / Failed / Not run / Not applicable**. All application rows below begin **Not run**.

| Area | Required checks |
| --- | --- |
| Objectives and gates | All MC-01–MC-10 represented; complete standard and lean journeys; both learner transfers; help and bypass; no answer leakage |
| Numeric correctness | All section 13 fixtures, independent expected values, every ending; exact threshold equality; no resource/energy-unit confusion |
| Input boundaries | Blank, zero, negative, fractions, decimals, malformed thousands separators, Unicode minus, huge input, nonfinite, out-of-range counts and wrong units |
| Equivalent answers | Equivalent decimals/fractions; reordered equivalent linear rules; correct day-10 total with wrong model must fail the model check |
| Graph/storage | All three selectable resources; positive/negative slopes; exact cap day; shortage clipping with unmet values; labeled SVG and typed-point alternative |
| Energy | Full/no batteries, zero arrays, normal-day failure, three-day storm, recharge cap, surplus curtailment; extra-solar strategy accepted |
| Weak design | Correctly analyzed housing/production/energy/cargo/budget failures reach Deployment delayed without false math errors |
| Revision | Every dependency row; historical context retained; selected crate change; obsolete report invalidated; unrelated work kept current |
| Persistence | Reload/resume, two sessions, duplicate, unavailable storage/quota, corrupted stored state and simultaneous tabs |
| Import/export | Full round trip of stage/answers/history/review/scene; wrong project/content/schema, malformed/oversized/hostile JSON; atomic failure; duplicate-ID handling |
| U-09 deletion | Cancel; active/inactive session delete; clear-all; no late autosave resurrection; reload; fresh work; backup recovery; other-app keys preserved |
| Access and device | Desktop keyboard/mouse, touch emulation, real iPad portrait/landscape, open software keyboard, help focus and non-drag input |
| Assets/runtime | All MC-A01–A13 present; no placeholder art; no runtime network dependency; no audio; downloaded desktop HTML completes offline |
| Print | Student/teacher/patch/transfer outputs on A4 and Letter; equations, units, SVGs, page numbers, no clipping and truthful Draft/Provisional/review labels |
| Privacy/teacher | Alias-only data, no telemetry or external submission; imported strings cannot execute; teacher mode explicitly not secure authentication |
| Packaging/host | Visible version matches notes/package; HTML and index byte-identical; actual `/Applied-Math-Projects/mars-colony/` entry/assets/state/export/print verified after deployment |

Scientific-notation checks and calibrated physical-model templates are **Not applicable** to the Mars core. This does not excuse stock/rate unit conversion or graph testing. Physical iPad/network/printer rows remain Not run until actually performed; emulation is separate evidence.

The practical acceptance path is that Will can complete the mission, deliberately make calculation errors, finish a valid weak design, revise it, resume a saved session, export/import, delete disposable work, print the report and see an ending that agrees with the mathematics.

## 15. Implementation, release and recovery plan

Follow **DESIGN → CHANGE SPEC → IMPLEMENT → CHECKPOINT → VERIFY → VERIFIED CHECKPOINT → RELEASE → DEPLOY**. Approval of this specification is separate from proof of a working release.

1. **CHANGE SPEC:** record the accepted revision, MC-I01–I08 decisions and source commit in GitHub. Add the Mars project brief and link the approved spec. Retain the original dossier unchanged.
2. **IMPLEMENT, content/math:** declare fixed data, all checkpoint field contracts, exact parsers/evaluators, capped resource/energy ledgers, outcome predicates and independent reference fixtures.
3. **IMPLEMENT, full journey:** build all eight stages, help, validation, graph entry, revision, local sessions, import/export, U-09 controls, teacher review and reporting.
4. **IMPLEMENT, visual completion:** add embedded scenes/icons/system diagram, three endings, mission patch and responsive/print layouts. These are part of the first complete application.
5. **CHECKPOINT:** preserve an identifiable source state before extended testing, using a message such as `Mars Colony v0.1.0 implementation checkpoint`.
6. **VERIFY:** run affected numerical, browser, persistence, security, print and device checks. Fix failures, preserve a new candidate when code changes, and rerun the affected checks.
7. **VERIFIED CHECKPOINT:** preserve the exact candidate that passed the recorded checks. A code change after verification requires corresponding re-verification. State physical-device/network/printer gaps honestly.
8. **RELEASE:** generate the self-contained file and identical deployable index from preserved source; update versions, release notes, teacher guide, asset manifest and QA materials without adding features.
9. **DEPLOY:** publish through the existing GitHub Pages project structure when authorized as part of implementation/release. Verify the actual hosted path, visible version, assets and workflow. An upload or README edit alone is not deployment verification.

### 15.1 Required repository/package structure

```text
README.md
docs/PROJECT-BRIEF.md
docs/change-specs/MARS-COLONY-v0.1.0.md
docs/decisions/MARS-COLONY-v0.1.0-APPROVAL.md
mars-colony/
  README.md
  CHANGELOG.md
  MarsColony_v0.1.0.html
  index.html
  docs/
    PROJECT-BRIEF.md
    TEACHER-GUIDE.md
    ASSET-MANIFEST.md
    QA-REPORT-v0.1.0.md
    DEPLOYMENT-v0.1.0.md
  tests/
    reference-cases-v0.1.0.json
    [math, workflow and persistence verification]
```

The root README/brief already exist and must be updated narrowly after re-reading the then-current repository. Other projects may be changing concurrently; do not overwrite their work using this older snapshot. Source may be organized in readable local files with a deterministic bundling step, but students receive a standalone HTML requiring no build tools to play.

The intended hosted route is `https://williammcada.github.io/Applied-Math-Projects/mars-colony/`. It is a target, not a claim that a Mars page is live. Downloaded desktop HTML must run offline; an already-hosted page’s ability to reopen after closing the tab without a network is not promised. iPad delivery is primarily the hosted application, not an HTML preview in a file-sharing app.

### 15.2 Recovery rule

Preserve source checkpoints, test results and exact candidate bytes before packaging or upload. A ZIP, export, upload, final-response or deployment failure must recover from the preserved candidate. Do not rebuild a verified implementation from chat history. Use “implementation checkpoint” or “release candidate” before the candidate has passed its required checks; do not call an untested commit a verified release.

## 16. Review summary

This draft preserves the original Mars curriculum, fixed simulation data, two resilience strategies, three endings and complete standalone-application requirements. The reviewable new choices are MC-I01–I08, detailed checkpoint/input contracts, individual transfer prompts, save/import bounds and the explicit daily shortage/overflow interpretation.

No handbook amendment is proposed. No Mars code was implemented, no application test was represented as passed, and no repository or deployment was changed by this specification-only delivery.
