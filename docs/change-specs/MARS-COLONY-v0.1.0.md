# Mars Colony v0.1.0 — finalized implementation specification

Authorized by William McAda on 9 October 2026: finalize plans, update GitHub and deploy to Netlify. The implementation scope is approved by that instruction. Baseline: `811dfc383c70861dcc6ccdcfa80df8a7b3f56e9d`; Mars has only a placeholder README and no prior app or Mars specification. This specification adopts the original dossier sections 28–32 below, together with its common sections 2–12 and QA-01–20.

Handbook revision `fd4330863f4cc0812180fbf1de122970a42c7885`: AI-START-HERE.md, UNIVERSAL-RULES.md, CONDITIONAL-STANDARDS.md and RELEASE-CHECKLIST.md consulted. U-01–09/U-11 and S-02/S-04/S-05 apply. U-10 is not applicable (ordinary forms, no held controls/gameplay). No handbook changes.

## Final implementation decisions

- Preserve all ten objectives and eight stages. Three estimated 45-minute lessons. Each field has a stable ID, objective/stage mapping, unit, exact evaluator, dependency list and contextual example in `src/core.js`. Demand: six daily/ten-day quantities. Units: six stock/rate classifications plus kg→g and L→mL. Modules: integer minima and capacity checks, selected habitat area/occupancy/area per person. Manifest: cost/cargo and signed reserves. Forecast: select one resource; enter structured initial/net coefficients, table and graph points for days 0/5/10 with axis labels. Storm: remaining percent, per-array output, load, total output and signed balance. Battery: end-of-day 3–7 storage and unserved storm energy. Comparison: baseline against five arrays/no battery, numerical differences plus teacher-reviewed reasoning. Independent transfer: partner A 30 people, B 28 people; daily water and minimum 30 L/day modules.
- Numeric answers accept exact decimals, equivalent fractions, Unicode minus and valid thousands separators. Units are fixed labels or validated selections. Structured equation coefficients avoid an unnecessary free-text algebra parser. Core model uses bounded small integer counts (0–12) and exact tenths for authored decimal quantities; field checking uses only a tiny floating-representation allowance.
- Capacity caps discard surplus. Negative stock/energy is prevented while unmet demand is separately recorded and causes delayed deployment. Battery starts full. Correct calculations for strategically weak plans can finish; readiness is separate from academic correctness. No claim of real engineering viability.
- First/current responses, help use and attempt scenario retained. Per-field dependency fingerprints preserve unaffected evidence and flag stale responses. Required reflection is submitted—teacher review. Numeric automatic checks are not a claim of prose/independent-work verification.
- Multi-session namespaced storage, save/export/import, duplicate for revision, individual pair-session deletion and clear-all with scope/count/Cancel/backup guidance. Import atomically as new copies after validation/preview; 2 MB maximum. Same schema patch versions accepted; wrong-project/future schema rejected. No historical Mars schema exists. Detect concurrent edits and offer reload or copy; storage failure retains memory work with export fallback.
- Embedded SVG horizon, equipment icons, storm and three ending scenes; unit-labeled resource/energy diagram; accessible table accompanying SVG graph. Story and instructions physically separated. Field help is keyboard/touch usable and contains different-number examples. Four-operation calculator. Alias-only; no backend, audio, telemetry or remote assets.
- Mission report includes configuration, manifest, checked responses, model/graph, daily balances, attempts, reflections and personalized mission patch. Teacher guide includes answer/reference plans. Offline standalone desktop and hosted iPad are target delivery modes; physical device/printer/school-network evidence must be reported separately.
- Generate byte-identical `index.html` and `MarsColony_v0.1.0.html`. Update root launcher to v0.1.1, add Mars project card/QR and retain other four links unchanged. Existing Netlify root/no-build configuration remains.
- Preserve implementation checkpoint; verify arithmetic fixtures, outcomes, stale dependencies, browser journey, save roundtrip, malformed imports, deletion, offline/layout/print; preserve verified checkpoint before release/deploy. Verify hosted HTML hashes and interaction. Exact test results go in QA/DEPLOYMENT records.

## Canonical Mars dossier adopted for this release

# 28 / MARS COLONY
## Narrative and experience brief
**Working subtitle:** Red Horizon · **Project ID:** `mars-colony` · **Initial release:** v0.1.0

**Premise:** Twenty-four settlers are waiting for approval to occupy an initial research outpost. The pair is the mission-planning team. Their job is to assemble a working resource system, protect reserves, and show what happens during a three-day reduction in solar output. The reward is a colony that visibly functions because its underlying quantities balance.

![Mars design reference](figures/mars.png)

*Design reference: concept and mathematical visual, not a screenshot of a completed application.*

**Central question:** How do rates, stocks, and capacities interact—and how much reserve makes a system resilient?

## Scope and pacing
Three 45-minute lessons. Lesson 1: people, daily demand, unit conversions, and module counts. Lesson 2: habitat area, cargo, cost, and resource graphs. Lesson 3: reduced solar output, battery balance, revision, and mission report.

All core time steps are **24-hour Earth days**, not Martian sols. Equipment capacities, consumption values, prices, masses, and the 25% event are explicitly invented classroom simulation inputs. They are not engineering recommendations or factual claims about astronaut needs. The science contribution is systems thinking and the distinction between a real setting and a simplified mathematical model.

## Product-specific aesthetic
A credible but inviting illustrated mission console: rust landscapes, slate backgrounds, ivory work panels, cyan system lines, and amber caution accents. Distinct water, oxygen, food, habitat, power, and storage icons. Use a visible network of modules, not combat units or a base-building action game.

The colony illustration becomes populated as requirements are met. Failure means deployment is postponed or the plan needs revision; no deaths, gore, or humiliating narration. The payoff is an operational outpost, a resource timeline, and a personalized mission patch.

## Tangible artifact
Mission readiness report, labeled system diagram, cargo manifest, daily resource balances, storm revision, and a printed mission patch. Optional resource tokens support a tabletop demonstration but are not needed for the core build.

<!-- PAGE: 29 -->
# 29 / Mars Colony—exact learning objectives

Reference anchors: 7.RP.A.1–3; 7.EE.B.3–4; 8.F.B.4–5; geometry as supporting application [S1–S5].

| ID / checkpoint | By completion, the learner will… | Required evidence and success condition |
|---|---|---|
| MC-01 / C01 | Convert per-person rates into group demand over time. | Correct daily and ten-day water, oxygen, and food needs with L, kg, and day units. |
| MC-02 / C02 | Choose units consistently and distinguish stock from rate. | Classify L versus L/day, kg versus kg/day, kWh versus kWh/day; convert stated kg/g or L/mL values. |
| MC-03 / C03 | Determine the minimum number of indivisible modules. | Calculate demand/capacity and deliberately round upward; justify the integer choice through a capacity check. |
| MC-04 / C04 | Use area-per-person and capacity constraints for habitats. | Correct total area, area per settler, and occupancy; do not equate volume with floor area. |
| MC-05 / C05 | Represent a stock as initial amount plus net daily change. | Write and tabulate a stock rule; distinguish production from stored reserve and cap where declared. |
| MC-06 / C06 | Calculate percent reduction and signed surplus/deficit. | Apply 75% of normal solar yield during the storm; calculate daily energy difference. |
| MC-07 / C07 | Track a finite energy store over several days. | Correct battery change during the three-day deficit; respect maximum usable capacity and prevent negative stored energy. |
| MC-08 / C08 | Balance cargo and cost against explicit caps. | Add masses in kg, equipment costs, and supplies; show budget and cargo reserves separately. |
| MC-09 / C09 | Defend a resilient design using calculated evidence. | Compare a battery-based and extra-panel design; identify a benefit, cost, and remaining model limitation. |
| MC-10 / C10 | Transfer a rate/capacity calculation independently. | Each student calculates a new population or one changed module capacity without copied totals. |

## Scope boundary
Counts are small nonnegative integers; rates are simple decimals. Core requires water, oxygen, food, habitat, solar production, one battery type, cost, and cargo—no chemical reaction simulation, biological farming model, orbital mechanics, real thermal control, or hourly electrical engineering.

**Theoretical simplifications must be visible:** constant per-person demand; pre-delivered food; idealized daily energy accounting; quoted usable battery capacity; no efficiency loss unless explicitly introduced; no claim that the model addresses all conditions for living on Mars. Questions ask students to name a limitation rather than mistake the simulation for a real mission design.

<!-- PAGE: 30 -->
# 30 / Mars Colony—screen and interaction flow

| Stage | Student task, prompt intention, and gate |
|---|---|
| MC-S01 / Arrival request | Confirm 24 settlers, 10 Earth days, budget, cargo cap, and system criteria. Distinguish fictional mission from scientific fact. |
| MC-S02 / Demand console | Calculate daily/group demands, then ten-day totals. “What is consumed per day, and what must be stored?” C01–C02. |
| MC-S03 / Module bay | Determine minimum oxygen/water/habitat counts, then choose a plan. “Will your full modules meet the demand?” C03–C04. |
| MC-S04 / Supply manifest | Choose standard or lean supply crate; account for equipment mass, budget, and reserves. “Which cap is tighter in your plan?” C08. |
| MC-S05 / Resource forecast | Build one stock equation and a table/graph. Select a resource so unlike units are not plotted on one unlabeled axis. C05. |
| MC-S06 / Storm briefing | Days 4–6 receive 25% less solar energy. “How much energy does each panel provide now?” C06. The event is disclosed in the brief and occurs once. |
| MC-S07 / Resilience test | Track energy, choose additional solar or battery capacity, and update dependencies. “How much stored energy is needed to cover this deficit?” C07–C09. |
| MC-S08 / Mission control | Summarize system readiness and limits, reveal the outpost, print report/patch, and complete C10. |

## System visual behavior
Each resource has a separate unit-labeled production arrow, consumption arrow, and storage box. Animated flow is optional and skippable. A bar labeled “water” must not alternate between liters and liters/day. Solar output is energy per day in this simplified model; it must never be casually relabeled kW.

**Feedback—module count:** “2.4 modules is the calculated ratio, not a purchasable quantity. Three modules provide enough capacity; two do not.”

**Feedback—percent loss:** “A 25% reduction leaves 75% of the original energy, not 25%.”

**Feedback—battery:** “A battery stores energy. It does not add a new daily production rate. Subtract the uncovered daily deficit from what is stored.”

## Physical optionality
A tray of labeled counters can represent one day’s supply and use, but digital completion does not require tokens. Do not use actual gases, pressurized containers, biological experiments, or chemical production. The hands-on scientific modeling requirement belongs primarily to Powers of Ten.

<!-- PAGE: 31 -->
# 31 / Mars Colony—canonical system and data

## MC-BASE: authored simulation constants
Population n=24; mission 10 Earth days. Per person/day: net water 3 L, oxygen 0.8 kg, food 0.6 kg. Daily demand: 72 L water, 19.2 kg oxygen, 14.4 kg food. Habitat criterion: capacity for all settlers and ≥3 m² floor area/person.

| Equipment | Capacity | Energy use | Mass | Cost |
|---|---|---|---|---|
| Oxygen module | 8 kg/day | 12 kWh/day | 200 kg | 2,000 cr |
| Water module | 30 L/day | 8 kWh/day | 150 kg | 1,500 cr |
| Habitat | 8 settlers; 24 m² | 10 kWh/day | 400 kg | 3,000 cr |
| Solar array | 36 kWh/day normally | — | 100 kg | 1,000 cr |
| Battery | 36 kWh usable storage | — | 80 kg | 800 cr |

Other fixed daily electrical demand=24 kWh. Standard supply crate: 1,000 cr; water 144 L, oxygen 38.4 kg, food 172.8 kg; plus 100 kg crate/other supplies. A lean crate costs 800 cr and contains 158.4 kg food, with all other contents unchanged. For cargo, use the declared classroom convention 1 L water=1 kg. Tank capacities: water 400 L, oxygen 100 kg, food 200 kg. These two fixed packs are the only core supply choices.

## Baseline plan and balances
Choose 3 oxygen modules, 3 water modules, 3 habitats, 4 arrays, 1 full battery. Daily production: oxygen 24 kg, water 90 L. Habitat area 72 m², 3 m²/person. Daily load=24+36+24+30=114 kWh. Normal solar=144 kWh/day; surplus=30 kWh/day.

Before storage caps are reached: `W(t)=144+18t` L; `O(t)=38.4+4.8t` kg; `F(t)=172.8−14.4t` kg. At day 10: 324 L water, 86.4 kg oxygen, 28.8 kg food. Initial reserves for water/oxygen cover two days; final food covers two days. All stated tank capacities are respected.

Storm days 4–6: each array gives 27 kWh/day, four arrays 108, daily deficit 6. Full battery 36→30→24→18 kWh. After normal production resumes, storage is capped at 36; no impossible accumulation above capacity.

Cost=25,300 cr against 26,000. Cargo mass=3,185.2 kg against 3,400; reserves 700 cr and 214.8 kg. Baseline assumptions—not current scientific consumption data.

<!-- PAGE: 32 -->
# 32 / Mars Colony—outcomes, artwork, and tests

## Resilience comparison and ending rules
An alternative uses five solar arrays and no battery. Normal generation=180 kWh/day; storm generation=135; load remains 114. Cost=25,500 cr; cargo=3,205.2 kg. It costs 200 cr and 20 kg more than the baseline, but avoids the modeled storm deficit. This is a second feasible strategy, not a prescribed best answer.

Critical readiness criteria: sufficient habitat; daily water/oxygen production meets demand; adequate food for ten days; resource stores within capacity and never below zero; energy demand covered during all modeled days; cost≤26,000; cargo≤3,400. Use daily balance only; no claim that this proves continuous 24-hour electrical operation.

| Ending | Exact predicate and response |
|---|---|
| Resilient outpost | Critical criteria met and final water/oxygen/food stores each cover ≥2 days’ demand. “Your four arrays and battery cover the storm. Eighteen kWh remain when normal output returns, and food retains a two-day reserve.” |
| Mission ready | Critical criteria met, but at least one final reserve is under two days. Identify which reserve would limit an extension. |
| Deployment delayed | Any critical criterion fails. Name the exact shortage, overload, housing gap, or overrun. Students can revise without restarting. |

A lean-crate variant of the baseline ends with 14.4 kg food (one day), cost 25,100 cr, and cargo 3,170.8 kg: it reaches Mission ready rather than Resilient outpost. A battery-free plan with adequate daily generation must not be rejected. Battery storage is not counted as production.

## Asset brief
MC-A01: horizon scene with a small research outpost, not a mature city. MC-A02–A07: water, oxygen, food, habitat, solar, battery illustrations. MC-A08: authoritative unit-labeled system diagram. MC-A09: dust-reduced solar scene. MC-A10–A12: operational, limited-reserve, delayed-deployment scenes. No dramatic casualty imagery; the mission patch includes the selected configuration and project/version.

## Project acceptance tests
Demand=72/19.2/14.4 in the appropriate daily units. Minimum self-sufficient counts are 3 oxygen, 3 water, 3 habitats. Power load is 114, not a sum that includes stored kWh as kWh/day. Storm loss is 25%, leaving 108 from four arrays. Three deficits consume 18 kWh. Day-10 food is 28.8 kg. Cargo and cost match the fixture. Five arrays/no battery is accepted. Two habitats fail occupancy. Three arrays plus no battery fail the storm criterion even if other resources are sufficient. Stale module changes invalidate power, cargo, cost, and verdict together.

<!-- PAGE: 33 -->
