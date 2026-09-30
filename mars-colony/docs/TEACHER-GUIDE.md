# Mars Colony — Teacher Guide

**A WILLIAM MCADA PRODUCT** · App 0.1.0 · Content/schema 1.0.0

Implementation candidate, 30 September 2026. Browser, PDF and classroom-device acceptance is pending; consult the [QA report](QA-REPORT-v0.1.0.md) before classroom deployment.

## Prepare

Use this applied-mathematics project with advanced Grade 5 learners working around Saxon 8/7. Plan three 45-minute lessons, then adjust from classroom observation. Pairs share a device; each learner completes a separate transfer task. There is no countdown, speed score, audio, account or online submission.

Open `MarsColony_v0.1.0.html` in a desktop browser. The final GitHub Pages route is the intended iPad entry point; it is not yet verified or deployed for this candidate. Use aliases, prepare a place to keep exported JSON files, and allow calculators. Print the reference and transfer slips through **Teacher**. The teacher desk is a local classroom aid, not secure access control.

The mission is fictional: 24 settlers, ten **24-hour Earth days**, 26,000 credits and 3,400 kg cargo. These are authored classroom values, not real engineering specifications. Days 4–6 reduce solar output by 25%. Food is delivered before arrival; batteries start full; daily accounting omits efficiency losses and nighttime operation. Water and oxygen production assume full module power, while electrical readiness is checked separately.

## Lesson sequence

| Lesson | Stages | Pair work and evidence |
| --- | --- | --- |
| 1 | 1 Arrival request; 2 Demand console; 3 Module bay | Set aliases and acknowledge assumptions; distinguish daily/per-person/mission quantities; convert units; calculate minimum whole modules and housing. Export progress and swap roles. |
| 2 | 4 Supply manifest; 5 Resource forecast | Calculate mass/cost and separate reserves; select water, oxygen or food; enter a linear rule, capped daily table and graph points. Freeze the initial plan, export and swap roles. |
| 3 | 6 Storm briefing; 7 Resilience test; 8 Mission control | Calculate reduced generation and daily battery states; compare two fixed strategies; revise and explain the final plan; complete individual transfer. Export the final mission and print its report. |

The Planner enters and explains; the Checker independently checks units and reasoning. The app swaps roles after stages 3 and 5. Repeated help and corrections carry no penalty. A `?` provides the field's units/format, an approach and a worked example using different values.

**Check & continue** requires current valid mathematics. A correctly calculated unsuccessful design can continue and receive **Deployment delayed**. Changing equipment or supplies retains answers and earlier attempts, marks dependent evidence **Needs recheck**, and changes a completed report to **Draft** until the affected pair checkpoints are current.

## Fixed data

| Resource | Per settler/day | Daily demand, 24 settlers | Ten-day demand |
| --- | ---: | ---: | ---: |
| Water | 3 L | 72 L | 720 L |
| Oxygen | 0.8 kg | 19.2 kg | 192 kg |
| Food | 0.6 kg | 14.4 kg | 144 kg |

| Equipment | Capacity/output | Daily energy use | Cargo | Cost |
| --- | --- | ---: | ---: | ---: |
| Oxygen module | 8 kg/day | 12 kWh | 200 kg | 2,000 cr |
| Water module | 30 L/day | 8 kWh | 150 kg | 1,500 cr |
| Habitat | 8 places; 24 m² | 10 kWh | 400 kg | 3,000 cr |
| Solar array | 36 kWh/day normally; 27 during storm | — | 100 kg | 1,000 cr |
| Battery | 36 kWh usable stored energy; initially full | — | 80 kg | 800 cr |

Fixed electrical load is 24 kWh/day. Each settler needs at least 3 m² of floor area. Maximum counts are 6 each for oxygen, water and habitats, 8 solar arrays and 4 batteries.

| Supply crate | Water | Oxygen | Food | Other/crate | Total cargo | Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Standard | 144 L | 38.4 kg | 172.8 kg | 100 kg | 455.2 kg | 1,000 cr |
| Lean | 144 L | 38.4 kg | 158.4 kg | 100 kg | 440.8 kg | 800 cr |

Use the supplied cargo convention **1 L water = 1 kg**. Storage caps are 400 L water, 100 kg oxygen and 200 kg food. Calculate daily net change first, then cap retained stock; record shortages and discarded surplus separately. Zero retained stock does not prove every demand was met.

## Baseline answers

The standard baseline has **3 oxygen modules, 3 water modules, 3 habitats, 4 arrays and 1 battery**. Water/oxygen capacity ratios are each 2.4; round upward to three whole modules. Two water modules supply only 60 L/day; two oxygen modules supply only 16 kg/day. Three habitats provide 24 places and 72 m², or 3 m²/person.

- Cargo **3,185.2 kg**; cost **25,300 cr**; spare cargo **214.8 kg** and spare budget **700 cr**.
- Load **114 kWh/day**; normal solar **144**, storm solar **108**; balances **+30** and **−6 kWh/day**.
- Uncapped rules: **W(t) = 144 + 18t**, **O(t) = 38.4 + 4.8t**, **F(t) = 172.8 − 14.4t**. Here `t` counts completed Earth days.
- Day-10 stocks: **324 L**, **86.4 kg**, **28.8 kg**. Final stock-only reserves: **4.5, 4.5 and 2 days**. Outcome: **Resilient outpost**.

| Day | Water L | Oxygen kg | Food kg | Battery kWh | Unserved kWh | Curtailed kWh |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 144 | 38.4 | 172.8 | 36 | — | — |
| 1 | 162 | 43.2 | 158.4 | 36 | 0 | 30 |
| 2 | 180 | 48 | 144 | 36 | 0 | 30 |
| 3 | 198 | 52.8 | 129.6 | 36 | 0 | 30 |
| 4 | 216 | 57.6 | 115.2 | 30 | 0 | 0 |
| 5 | 234 | 62.4 | 100.8 | 24 | 0 | 0 |
| 6 | 252 | 67.2 | 86.4 | 18 | 0 | 0 |
| 7 | 270 | 72 | 72 | 36 | 0 | 12 |
| 8 | 288 | 76.8 | 57.6 | 36 | 0 | 30 |
| 9 | 306 | 81.6 | 43.2 | 36 | 0 | 30 |
| 10 | 324 | 86.4 | 28.8 | 36 | 0 | 30 |

The Teacher answer reference contains all active baseline field answers and the full resource/energy tables. Exact equivalent fractions and equivalent linear expressions are accepted. A correct final stock with an incorrect linear rule does not pass the rule checkpoint. Units may be included where the field supports the displayed unit; no hidden rounding or tolerance band changes the answer.

## Compare and revise

The comparison fixes 3 oxygen, 3 water and 3 habitat modules and uses the currently selected crate. Strategy A is 4 arrays + 1 battery; B is 5 arrays + no battery. Students may keep a different personal configuration after explaining their choice.

| Plan | Cost cr | Cargo kg | Normal/storm generation | Day-6 battery | Final food reserve | Outcome |
| --- | ---: | ---: | --- | ---: | ---: | --- |
| Standard A | 25,300 | 3,185.2 | 144 / 108 kWh/day | 18 kWh | 2 days | Resilient outpost |
| Standard B | 25,500 | 3,205.2 | 180 / 135 kWh/day | 0 kWh | 2 days | Resilient outpost |
| Lean A | 25,100 | 3,170.8 | 144 / 108 kWh/day | 18 kWh | 1 day | Mission ready |
| Lean B | 25,300 | 3,190.8 | 180 / 135 kWh/day | 0 kWh | 1 day | Mission ready |
| Lean, 4 arrays + 2 batteries | 25,900 | 3,250.8 | 144 / 108 kWh/day | 54 kWh | 1 day | Mission ready |

A uses 200 cr and 20 kg less than B. B has a positive daily energy balance during the disruption without batteries. That conclusion is valid only within this daily model; it does not establish continuous nighttime power. Require a supported benefit/tradeoff and a model limitation, rather than a preferred strategy.

| Diagnostic design | Correct conclusion |
| --- | --- |
| Baseline with no battery | Days 4–6 each leave 6 kWh unserved. Deployment delayed. |
| Three arrays and no battery | Day 1 already leaves 6 kWh unserved; each storm day leaves 33. |
| Two habitats | 16 places and 48 m², or 2 m²/person; housing fails. |
| Two water modules | Final water remains 24 L, but 60 L/day fails the required 72 L/day production. |
| Four water modules | Net +48 L/day; day 5 stock 384; day 6 raw stock 432, retained 400, discarded 32 L. |
| No water/oxygen modules | Initial stocks reach zero at day 2; day 3 leaves 72 L water and 19.2 kg oxygen unmet. |

## Interpret evidence and endings

All critical criteria must pass: housing, daily water/oxygen production, food, no unmet material demand, no unserved energy on any day, budget and cargo. **Resilient outpost** also requires at least two final reserve days in each material resource. Passing all critical criteria with a smaller reserve earns **Mission ready**. Otherwise the model gives **Deployment delayed**.

Missing or stale pair evidence produces **Draft**. An active teacher bypass produces **Provisional**. The teacher desk requires a teacher alias and reason, preserves the bypass, and does not silently mark the mathematics correct. A bypass ceases to govern a field after a later valid check. Free responses and paper work retain their separate review status. The pair's design ending is not an assessment of either learner's independent mastery.

Review recommendations, model limitations and revision explanations in **Teacher**. For an oral response, choose a prose field, enter the response and review note, then use **Record oral response**. Changing a reviewed response invalidates its previous review context.

## Individual transfer

Keep each learner's work separate, using on-device entries or the printable slips. Paper mode remains pending until the teacher records the review.

| Learner | Task | Answers |
| --- | --- | --- |
| A | 30 settlers; 3 L water/person/day; 30 L/day per module | 90 L/day; 900 L over ten days; ratio 3; 3 modules. Three modules supply exactly 90 L/day. |
| B | 28 settlers; 0.8 kg oxygen/person/day; 8 kg/day per module | 22.4 kg/day; 224 kg over ten days; ratio 2.8; 3 modules. Two supply 16; three supply 24 kg/day. |

Common misconceptions include treating per-person rates as whole-colony demand, multiplying a rate without changing the unit, rounding capacity ratios down, adding battery capacity as daily production, subtracting 25% as 25 kWh, and using a clipped zero to conceal unmet demand. Ask learners to state what each number and unit describes.

## Save, recover and delete

**Save** stores a complete mission in this browser. Autosave follows edits. **Export progress** downloads portable JSON; use it at lesson boundaries and before device changes. Browser data can be cleared by the device or browser, so local saving alone is not a durable classroom backup.

**Saved work** supports resume, duplicate, fresh revision, import, per-mission deletion and clear-all for Mars. Duplicate keeps evidence; Fresh revision keeps work as a starting point with a fresh evidence history. Import validates first and creates independent copies. Wrong-project, future-schema or malformed files are rejected without replacing existing missions. Schema 1.0.0 is the first Mars schema; there is no legacy Mars migration. A newer tab is never silently overwritten; choose reload, export or save as a copy.

Delete requires confirmation and offers Cancel and backup. It removes the selected complete mission, including learner responses and evidence. It does not remove downloaded JSON or another project's data. Recovery requires an exported backup. If local storage is unavailable, keep the page open and export before leaving; multi-mission backup/import requires available storage.

## Print and accessibility

The report includes the final plan, resources/graph, energy ledger, recommendations, initial/final configuration and first/current response evidence. The teacher reference contains solutions; transfer slips omit answers. The patch includes the team alias, configuration and version. Use the preview's **Print / Save PDF** control and choose A4 or Letter. Actual layout/PDF/printer acceptance remains pending in this candidate.

All mathematical graph points have typed-entry controls; no dragging is required. Controls use explicit labels, feedback, focus outlines and native dialog semantics. Real keyboard/touch, screen-reader, open-software-keyboard and physical iPad checks remain to be observed. Do not infer accessibility conformance from source markup or in-process tests alone.
