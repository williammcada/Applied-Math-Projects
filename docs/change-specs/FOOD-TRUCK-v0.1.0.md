# Food Truck / Business Launch v0.1.0 implementation specification

**Specification revision:** Approved revision 1, 30 September 2026  
**Status:** Approved by William McAda on 30 September 2026 with “Proceed to build.” FT-I01–FT-I06 are approved. See [approval record](../decisions/FOOD-TRUCK-v0.1.0-APPROVAL.md). Implementation is now authorized; no application verification is inferred from specification approval.  
**Owner:** William McAda · **Credit:** A WILLIAM MCADA PRODUCT  
**Student-facing title:** Food Truck · **Subtitle:** Street Food Startup  
**Repository:** `williammcada/Applied-Math-Projects`  
**Source baseline:** `cf13e7f3111b2291a07c1387707fbb5d8b814ad5`  
**Targets:** app 0.1.0, content 1.0.0, save schema 1.0.0  
**Handbook:** `00cbde605ab08203b6b5fd2374d225155608fc29`, v0.1.1

## 1. Purpose and authority

Build the second independent application in the Applied Mathematics Project Series. Students plan a three-hour food-festival launch, scale a recipe, price a meal, construct and compare business functions, calculate a deterministic launch, then compare an alternative plan. The central distinction is between a sold-all model and realized profit when prepared food remains unsold.

The [preserved dossier](../sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md), sections 01–12, 18–22 and 39–42, supplies the requirements and numerical defaults. The Word source supplied by the owner matches the preserved package; [provenance](../sources/PROVENANCE.md) records its identity. Preserve the source files unchanged.

Use the same specification → approval → implementation checkpoint → verification → release → deployment process used for Road Trip. Its [approved specification](ROAD-TRIP-PLANNER-v0.1.0.md) supplies a process and engineering precedent, not Food Truck content. Road Trip remains unchanged. Copy suitable tested arithmetic, input, save, graph and print helpers into this project after review; no shared runtime or dependency on the Road Trip HTML is permitted.

Apply U-01–U-08 as the selected project guidance, approved U-09, and conditional S-02/S-04/S-05. Their handbook statuses remain seeded/draft/approved as recorded there; this task does not ratify new universal rules. AI-START-HERE, UNIVERSAL-RULES, CONDITIONAL-STANDARDS and RELEASE-CHECKLIST were read at the exact revision above. No missing essential source or numerical conflict was found. The clarifications below make unspecified implementation details reviewable without altering the source prices, demand or outcome thresholds.

## 2. Scope and implementation decisions

Audience: advanced Grade 5 Introduction to Pre-Algebra / Saxon 8/7. Default grouping: two students sharing an iPad, with complete desktop keyboard/mouse support. Three proposed 45-minute lessons, brief ELL-friendly English, no countdown, speed score, music or audio. Alternate Planner and Checker after lessons one and two; obtain separate individual transfer responses.

Deliver a bespoke self-contained HTML, byte-identical hosted `index.html`, teacher guide/reference, release notes and evidence-based QA report. Inline CSS/JavaScript, system fonts and embedded pictures only; no runtime network service, CDN, account, analytics, backend or shared suite loader. Downloaded desktop HTML works offline; hosted offline reopening is not promised. iPad delivery uses the hosted page.

Core contains one menu item, three illustrated cuisine identities, three prices, four stock quantities, eight stages and ten required checkpoints. Concert-promotion ideas appear through the festival pitch, stall fee and audience forecast. There is no concert module, business generator, tax/discount exercise, interest, payroll, depreciation, second menu item, student survey or general scenario editor in v0.1.0. No cooking or food handling is required.

| ID | Draft implementation decision | Rationale and scope |
| --- | --- | --- |
| FT-I01 | Select provisional stock in Recipe bench; default 100 portions. Stock and service later confirms or changes that same selection. Changing it returns affected recipe/ledger fields to Needs recheck. | Recipe scaling needs a quantity before the dossier's later stock stage; no new production values are introduced. |
| FT-I02 | Rice bowl, wrap and noodle identities use one explicitly labeled classroom ingredient/cost model. Cuisine changes artwork and naming only. | All are fictional menu concepts; do not imply that changing cuisine changes cost or supplies a real cooking recipe. No silent ingredient substitutions. |
| FT-I03 | Default price is $12; the full demand table is disclosed before selection. All $9/$12/$15 options remain available. | Preserves the canonical example and viable weak-design paths. |
| FT-I04 | Freeze the first checked launch as Plan A. Require a distinct Plan B changing price, stock, or both, with affected mathematics checked. Students may recommend either plan. | Makes the required revision observable without requiring financial improvement or erasing the first attempt. The dossier's business Versions A/B are labeled Plan A/B to distinguish them from app versions. |
| FT-I05 | Teacher mode has solutions, review, diagnostics and logged bypass, but no editable fixed fee, prices, demand, recipe or service-rate settings. | Keeps the three-lesson scope bounded. Zero stock/nonpositive contribution are evaluator boundary fixtures, not selectable core plans. |
| FT-I06 | One saved session is the complete work group, including both plans, histories, reviews and reports. | U-09 requires session deletion and clear-all, not an invented school-year manager. |

These implementation details were approved with revision 1. There is no proposed change to the mathematical objectives or ending predicates.

## 3. Fixed data and exact mathematics

All money is USD, labeled “Classroom prices—not live quotations.” Source money uses integer cents; evaluation uses exact decimal/rational arithmetic. Counts and production options are discrete. Keep unit meaning alongside every value.

| Source ID | Given data | Unit / constraint |
| --- | --- | --- |
| FT-D01 | One batch makes 20 portions | Whole batches; q ∈ {60,80,100,120} |
| FT-D02.grain | 2 kg at $5/kg per batch | Line cost $10 |
| FT-D02.vegetables | 3 kg at $6/kg | Line cost $18 |
| FT-D02.protein | 2 kg at $20/kg | Line cost $40 |
| FT-D02.sauce | 0.5 L at $20/L | Line cost $10 |
| FT-D02.packaging | 20 units at $0.60/unit | Line cost $12; all prepared meals incur packaging expense |
| FT-D03 | Stall $200 + truck hire $150 + signs/setup $100 = F=$450 | Once per launch, not per portion |
| FT-D04 | p=$9 → demand 120; p=$12 → demand 90; p=$15 → demand 60 | Authored event forecasts, not real market claims |
| FT-D05 | 32 meals/hour for 3 hours | Service capacity K=96; does not cap advance preparation |
| FT-D06 | Profit at least $150 and waste at most 10% of prepared stock | Disclosed sponsor targets; equality passes |

For stock q, scale factor k=q/20. Scale each ingredient and packaging quantity by k. A base batch costs $90. Prepared variable expense V(q)=$4.50q; per-portion cost v=$4.50. Fixed expense is excluded from v; prepared total expense is F+V(q).

Sold-all model: x denotes portions both prepared and sold, in a separate theoretical comparison. R(x)=px, C(x)=F+vx, P(x)=R(x)−C(x)=(p−v)x−F. Use 0≤x≤120 with whole portions for feasible counts; continuous lines help locate crossings. Do not impose demand/capacity on this hypothetical graph or describe a sold-all 100-meal point as an achievable launch when K=96. Explain the assumption beside the graph and on print.

Contribution c=p−v is USD per portion; markup is 100c/v percent, not c/p (margin). For c>0, continuous break-even x*=F/c; smallest whole count with nonnegative profit is ceil(x*); first positive profit is floor(x*)+1. A fractional crossing is valid in the model, not a fractional sale. Exact equality may have no whole-number solution. At c≤0 and F>0 there is no nonnegative or positive-profit threshold; report no break-even under this model without dividing by zero. Such prices are outside the core catalog.

| Price | Contribution | Markup, nearest 0.1% | Continuous crossing | First whole non-loss | First whole positive profit |
| --- | ---: | ---: | ---: | ---: | ---: |
| $9 | $4.50 | 100.0% | 100 | 100 | 101 |
| $12 | $7.50 | 166.7% | 60 | 60 | 61 |
| $15 | $10.50 | 233.3% | 300/7 | 43 | 43 |

Launch uses separate variables: q prepared, D forecast demand, K service capacity, s modeled sales. s=min(q,D,K); revenue=ps; expense=F+vq; realized profit=ps−F−vq; waste=q−s; waste percent=100(q−s)/q; sell-through=100s/q. Report every tied limiting factor, not just the first minimum. Demand and capacity are distinct constraints. q=120 is allowed even though at most 96 meals can be served.

The sold-all profit evaluated at actual sales overstates realized profit by v(q−s). At q=100,p=$12: P(90)=$225, actual profit=$180, overstatement=$45. Preparing extra food is not free. In a zero-stock boundary fixture, sales and waste are zero, profit=−F, waste/sell-through percentages are null with “Not applicable”; zero is not a core selectable stock value.

### All 12 core plan outcomes

Results assume current academic gates, no active bypass and required submissions. Waste percentages below are exact; display to nearest 0.1%. Financial success is not academic mastery.

| p | q | Sales | Revenue | Expense | Profit | Waste | Waste % | Ending |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 9 | 60 | 60 | 540 | 720 | −180 | 0 | 0 | Business rethink |
| 9 | 80 | 80 | 720 | 810 | −90 | 0 | 0 | Business rethink |
| 9 | 100 | 96 | 864 | 900 | −36 | 4 | 4 | Business rethink |
| 9 | 120 | 96 | 864 | 990 | −126 | 24 | 20 | Business rethink |
| 12 | 60 | 60 | 720 | 720 | 0 | 0 | 0 | Viable first launch |
| 12 | 80 | 80 | 960 | 810 | 150 | 0 | 0 | Festival success |
| 12 | 100 | 90 | 1080 | 900 | 180 | 10 | 10 | Festival success |
| 12 | 120 | 90 | 1080 | 990 | 90 | 30 | 25 | Viable first launch |
| 15 | 60 | 60 | 900 | 720 | 180 | 0 | 0 | Festival success |
| 15 | 80 | 60 | 900 | 810 | 90 | 20 | 25 | Viable first launch |
| 15 | 100 | 60 | 900 | 900 | 0 | 40 | 40 | Viable first launch |
| 15 | 120 | 60 | 900 | 990 | −90 | 60 | 50 | Business rethink |

The $9 sold-all threshold is mathematically valid but cannot be reached during this festival because K=96. Do not mark its correct model wrong; the launch analysis explains the loss. Three plans meet the top ending; the app must not privilege only the default one.

## 4. Student journey

Persistent controls: alias/truck name, named stage, project/version, save state, Back, Save, Export progress and relevant Help. Future stages name missing prerequisites. Incorrect required mathematics blocks the affected check; valid weak business plans continue. Save, Back, Help and draft printing stay available. No dashboard or decorative scene reveals answers before the relevant check.

| Stage | Task and interaction | Gate / chapter boundary |
| --- | --- | --- |
| FT-S01 Festival invitation | Illustrated festival; alias, truck name, cuisine, Planner/Checker. Read three-hour event and sponsor targets. Confirm that profit and waste both matter. | Valid selections and briefing confirmation; not a mastery score |
| FT-S02 Recipe bench | Select provisional stock, initially 100; scale five recipe/packaging quantities. Ratio strip and quantity fields; drag is optional. | C01 current |
| FT-S03 Purchasing ledger | Base-batch and prepared-stock columns; compute line costs, batch/prepared totals and cost per portion. Classify variable versus fixed expense. | C02 current; end lesson one, export and swap roles |
| FT-S04 Pricing desk | Show demand table, select price, calculate contribution and markup. Distinguish markup from margin. | C03 current |
| FT-S05 Investor pitch | Construct R,C,P; solve equality versus strict profit threshold; complete and plot revenue/cost values; identify loss. | C04–C06 current; end lesson two, export and swap roles |
| FT-S06 Stock and service | Confirm/change stock; show affected work requiring recheck; calculate capacity, read demand, enter sales and all limiting factors. | C01–C07 current; weak forecasts remain allowed |
| FT-S07 Launch weekend | Deterministic illustrated launch; calculate revenue from sales and expense from prepared stock, profit, waste and sell-through. | C08 current or explicit bypass; freeze Plan A once. No random customer roll |
| FT-S08 Business review | Create Plan B, recheck only affected C01–C08 work, compare both plans, recommend A or B, complete each learner's transfer. Reveal outcome; print report/menu/display card and export. | C09–C10 plus current required plan evidence; Draft/Provisional available |

Plan B uses the same calculation screens with a visible plan label and “Return to business review.” It must change price or stock from Plan A; alias/cuisine changes alone do not satisfy revision. Once both are checked, recommending either plan is valid. Both plans must use permitted inputs and correct mathematics; “feasible comparison” does not mean both must be profitable. Students may complete a rethink outcome rather than being forced to hunt for a top ending.

## 5. Checkpoint and help contracts

Each checkpoint is a fixed Food Truck record with id, objectiveId, sourceIds, prompt, fieldIds, number range, mathematical action, dimensions, representation, accepted forms, evaluator, units/precision, prerequisite field IDs, help/error content, evidence and review status. The field paths below are stable relative to a plan unless explicitly session-level. This is not a generic lesson engine.

Common evidence: first checked and latest response per field/context; exact normalized values/coefficients; result, timestamp, scenario/plan revision, attempt count, dependency fingerprint, support opened and overrides. Raw typing and blocked prerequisites do not count as mathematical attempts. Check only submitted/changed fields, preserving accepted siblings. Each attempt retains its original input context; no retroactive regrading of historical answers against a different plan.

Provide a short illustrated glossary for batch, portion, fixed cost, variable cost, revenue, contribution, markup, profit, break-even, demand, capacity, waste and sell-through. Essential meanings also appear beside the task; the glossary is not a substitute for field help.

Help beside every substantive field/group contains meaning, units/format, action and a different-number example. Every popup supports touch, keyboard, Escape, outside-tap and Close with focus return. Examples below define the mathematical content; concise final wording may improve without changing answers or revealing the current item. Required definitions also appear in ordinary screen text.

### FT-C01 — Scale the recipe (FT-01)

Sources D01–D02; prerequisite valid `stock`. Fields `recipe.factor` and `recipe.quantity.{grain,vegetables,protein,sauce,packaging}`. Prompt: “Scale the 20-portion recipe for your prepared stock.” Enter q/20 and all five amounts. Accept exact equivalent fractions/decimals for kg/L and exact integer-valued packaging counts. At q=100: factor 5; 10 kg,15 kg,10 kg,2.5 L,100 packages. Valid scales are 3,4,5,6; ingredients remain proportional. Compare each against the source recipe, not against a potentially wrong student factor. Evidence includes the quantities and selected q.

Help: a 10-portion recipe with 1.5 kg of base needs 4.5 kg for 30 portions. Error: “Multiply every ingredient by the same batch factor; do not add the number of extra portions.” No semantic teacher review required.

### FT-C02 — Purchase and cost the stock (FT-02)

Sources D01–D03; prerequisite current C01 for this q. Fields `ledger.baseLine.<item>`, `ledger.baseTotal`, `ledger.preparedLine.<item>`, `ledger.preparedTotal`, `ledger.unitCost`, `ledger.fixedTotal`, `ledger.costClass.<item>`. Five items use D02 IDs. Enter quantity×unit price for each base and prepared line, sum totals and divide prepared total by q for v. Classify each ingredient/packaging line variable, stall/hire/setup fixed. Include packaging exactly once; fixed fees do not enter v.

Keys: base lines 10,18,40,10,12; total 90; at q100 prepared lines 50,90,200,50,60; prepared total 450; v=4.50; fixed total=450. Two $450 totals represent different things and require separate labels. Accept exact money equivalents with field-compatible units; current recipe plus q sets expected answers, independently of student subtotals. Preserve base-batch/fixed/unit-cost evidence on a stock-only edit; prepared fields become stale. No prose review.

Help: 6 kg at $3/kg costs $18; a $72 batch of 24 portions costs $3/portion. Error: “Packaging is paid for every prepared meal, including meals left unsold.”

### FT-C03 — Price, contribution and markup (FT-03)

Sources D02/D04; prerequisite C02 unit cost current and valid price. Fields `pricing.contribution`, `pricing.markupPercent`, `pricing.markupBase`, `pricing.contributionMeaning`. Enter p−v in USD/portion and 100(p−v)/v, rounded half-up to nearest 0.1%. Select cost as the markup denominator and “available per sale to cover fixed costs, then profit” as contribution meaning. Do not confuse contribution with final profit. Keys for each price are in section 3; all four fields are required. Accept a percent sign or a bare number in a visibly percent-labeled field. No margin field is required.

Help: cost $8, price $10 gives $2 contribution and 25% markup. Error: “Markup compares the increase with cost, not with selling price.” No prose grading.

### FT-C04 — Construct three functions (FT-04)

Sources D02–D04; prerequisites C02/C03 current. Fields `models.revenue`, `models.expense`, `models.profit`, `models.profitSlope`, `models.profitConstant`, `models.domain`, `models.assumption`. Enter rules in x; canonical p12 keys (m,b): R=(12,0), C=(4.5,450), P=(7.5,−450). Independently enter profit slope and constant with units USD/portion and USD; select whole portions 0–120 and “x portions prepared and all x sold.” Both expression and coefficient fields must pass. Compare exact coefficient pairs for each rule, not one substituted total. Guided labeled-term entry may replace typing but must not autofill the independent coefficients.

Accept `12x-(450+4.5x)`, `7.5x-450` and equivalent linear forms for P; labels such as `P(x)=` are optional when matching the field. `8x-480` also gives zero at 60 and must fail. Unknown variables/function references are rejected; either expand R−C or use the guided form. Evidence stores raw rules, normalized coefficients and interpretations. No free-prose model grading.

Help: price 11, variable cost 3 and fixed fee 160 give R=11x, C=160+3x and P=8x−160. Error: “Fixed launch expense is subtracted once, not once per meal.”

### FT-C05 — Break-even and the first profit (FT-05)

Sources current C04 and D03/D04; prerequisite C04 current. Fields `breakEven.equation`, `breakEven.crossing`, `breakEven.firstNonLoss`, `breakEven.firstProfit`, `breakEven.profitBefore`, `breakEven.profitAt`, `breakEven.interpretation`. Enter an equality equivalent to (p−v)x−F=0; normalize both sides and permit nonzero scalar multiples of that equation. Require the exact continuous crossing, the two whole-count thresholds, and profit at firstProfit−1 and firstProfit. Negative profit is valid. Select the statement distinguishing zero profit from positive profit.

At p12: crossing60, non-loss60, first profit61, P(60)=0 and P(61)=7.50. At p15: crossing300/7, non-loss43, first profit43, P(42)=−9 and P(43)=1.50. The fraction is required exactly; 42.86 is not an exact crossing. Help states the accepted fraction format. Report a threshold outside 0–120 as beyond the displayed model domain rather than claiming it attainable; no current core price requires that branch. Zero/negative contribution gets a useful design warning and no division; it must never trap a valid negative-profit core plan.

Help: fixed fee150 and contribution6 give equality25 and first profit26. Error: “At equality the profit is zero. For positive profit, revenue must be greater than expense.” Store both thresholds and boundary checks; no prose review.

### FT-C06 — Connect tables, graphs and loss (FT-06)

Sources current C04/C05; prerequisites both current. Fields `graph.table.{revenue,expense}.{0,60,100}`, `graph.points.{revenue,expense}`, `graph.xAxis`, `graph.yAxis`, `graph.xStep`, `graph.yStep`, `graph.crossingX`, `graph.crossingY`, `graph.lossAt30`, `graph.lossMeaning`. Students enter six table values and independently plot the corresponding six points. At p12, R values 0,720,1200; C values450,720,900. Crossing=(60, 720). At p9 crossing=(100,900); at p15 crossing=(300/7,4500/7), accepted via exact coordinate fields with a correctly positioned visual marker.

SVG axes: x portions, displayed 0–120; y USD, displayed 0–1800; default uniform ticks 20 and 200. Permit x tick 10/20/30 and y tick 100/200/300, all evenly spaced with sufficient range. Points use exact coordinate fields as the authoritative accessible alternative; touch snapping must permit the required table points. Correct points are shown after checking; complete lines appear only after the table/plot gate, not while students are being asked to construct them. Mark continuous crossing as theoretical; sale counts are whole numbers.

Calculate profit at x=30 (−315/−225/−135 for p9/12/15) and select “expense exceeds revenue.” After this check, a separate derived profit view may show the same model with signed y axis −600 to1200, uniform ticks, and accessible values; it must display negative values, not clip losses. Do not confuse a revenue/cost chart's nonnegative y range with a claim that profit cannot be negative.

Help: at 20 sales, revenue200 and expense 250 imply profit−50; revenue is below cost. Error: “The horizontal axis counts portions; the vertical axis measures dollars.” Preserve coordinates, axes and scales; no automatic semantic interpretation of prose.

### FT-C07 — Stock, demand and service (FT-07)

Sources D01/D04/D05; prerequisites current C01–C06. Fields `service.capacity`, `service.demand`, `service.sales`, `service.limits` (set of stock/demand/capacity IDs). Enter 32×3=96, the selected demand-table value, min(q,D,K), and every limit tied at the minimum. Baseline q100,p12: sales90, demand alone limits. q60,p15: both stock and demand. q120,p9: capacity alone. Counts are nonnegative integers; core capacity/source inputs are fixed. A correct forecast of low sales or loss is accepted.

Help: stock 50, demand 70, capacity 60 gives 50 sales, limited by stock. Error: “Advance preparation may exceed service capacity; sales may not exceed any of the three limits.” Record the source triple and all tied limits.

### FT-C08 — Realized profit and waste (FT-08)

Sources D02–D05 and current C07; prerequisite C07 current. Fields `launch.revenue`, `launch.expense`, `launch.profit`, `launch.waste`, `launch.wastePercent`, `launch.sellThroughPercent`, `launch.variableCostBasis`, `launch.soldAllOverstatement`. Require ps, F+vq, signed profit, q−s, both percentages, selection “prepared portions” for expense, and v(q−s). Money is exact here; percentages use half-up to nearest 0.1%. Compare all fields independently against current inputs, never propagate a wrong prior answer as the key.

Baseline keys: 1080,900,180,10,10.0%,90.0%,prepared,45. The result scene may reveal verified quantities progressively; avoid displaying unchecked totals. Help: prepare 50 at variable cost 3, sell 40 at price 9, fixed fee 100 → revenue 360, expense 250, profit 110 and waste 10. Error: “You prepared 100 meals. Expense includes all 100 even though only 90 sold.” Adapt counts to the current plan.

After the initial plan's C08 gate, freeze an immutable Plan A record containing inputs, evidence, calculation context and checks. Refresh/Back must not create another first launch or silently alter that record. No prose review needed.

### FT-C09 — Compare and recommend (FT-09)

Sources checked A/B, D06; prerequisite both plans' required calculation evidence current, and B differs in p or q. Session fields `comparison.deltaProfit`, `comparison.deltaWaste`, `comparison.chosenPlan`, `comparison.evidenceMetric`, `comparison.evidenceValue`, `comparison.reason`, `comparison.review`. Enter B−A profit and waste differences; select a plan and a supported metric (its profit, waste count, waste percent, sales or the declared B−A differences), then enter the corresponding quantity. Require a short sentence or recorded oral submission. Check metric/value exactly under that metric's precision; verify structural submission only for prose. Teacher marks the reasoning pending/reviewed/revise; grammar is not scored.

Canonical A=(12,100),B=(12,80): profit−30, waste−10, with B profit150 and zero waste. B=(15,60) instead: profit change0, waste−10. Students may prefer A or B with evidence; no rule forces maximum profit, minimum waste, or a particular cuisine. Both plans' service/cost implications appear side by side without rewarding a wrong expense model.

Help: two plans earn 120/140 and waste 8/2; the second changes profit by +20 and waste by −6. Error: “Use Plan B minus Plan A; keep the sign to show an increase or decrease.” Prose submission stays explicitly teacher-reviewed, not automatically certified.

### FT-C10 — Separate transfer (FT-10)

Sources FT-T01/FT-T02 (new fixed transfer data below); prerequisite C09 structurally submitted. Session fields `transfer.A` and `transfer.B`, each with mode digital/paper/oral, raw responses, attempts, submittedAt and review. Do not display the shared model or the other learner's answer as a solution. Mark pair-device independence as a classroom procedure, not secure verification. Answer feedback appears only after the individual submits; never copy one learner's evidence to the other.

- FT-T01, learner A: fixed fee 360, selling price 14, variable cost 5. Enter profit rule 9x−360, break-even 40 and first positive-profit count 41. Assumption: sold all. New values distinguish transfer from the group task.
- FT-T02, learner B: prepare 70 portions at variable cost 4, sell 56 at price 10, fixed fee 200. Enter revenue 560, expense 480, profit 80, waste 14 and sell-through 80.0%. Explain the expense basis through a prepared/sold choice. Given sales are valid; no demand forecast is inferred.

Numeric/equation rules match their corresponding shared checkpoint, but fixed transfer values never change with a plan edit. Help uses a generic example distinct from these values. A teacher may record a paper/oral submission with reviewer alias and note; selecting paper alone does not count as submission. Such work remains pending review until checked. Imported history is labeled; it cannot prove independent mastery.

## 6. Input, precision and feedback

Normalize whitespace, Unicode minus, ×/÷ and unambiguous thousands separators; reject malformed grouping and comma decimals. Accept equivalent decimals/fractions unless an integer or rounded response is requested. Exact integer-valued decimals/fractions can represent a count; fractional counts cannot. Money labels permit compatible $/USD; rates must keep their denominator (USD/portion is not USD). Accept kg, L and packaging units only in the matching fields. A wrong unit must not disappear during parsing.

Money is exact rational/cents with no floating epsilon. If a future supported fixture needs cents, use decimal half-up at the stated final step, not intermediate rounding. For requested percentages, compare the submitted value with the exact rational rounded half-up to one decimal place; allow omitted trailing zero. Thus166.7% passes while an unrounded500/3% does not meet that prompt. Never use rounded percentages for ending thresholds: compare10×waste≤q exactly. Negative money/profit and percentages above100 in appropriate generic fixtures are not intrinsically malformed; field meaning controls bounds. Waste/sell-through here remain0–100 by the launch model.

Expression parser: numeric literals, variable x, parentheses, +,−,×,÷ and implicit numeric multiplication; optional field-appropriate function prefix. Linear expressions only, no eval, unknown variables, exponent syntax or division by a variable; constant division allowed and zero rejected. Bound expressions to200 characters, nesting12,100 tokens; numeric entries64 characters and12 significant digits. Reject nonlinear intermediates rather than approximating sampled values. Fraction input must reject zero denominator. The complete actual parser requires implementation tests; reference arithmetic is not parser verification.

Every error identifies the field, explains a corrective action and keeps valid work. Failed Check focuses a linked summary. No alert boxes, hidden red-only states or per-keystroke wrong-answer warnings. Price/stock catalog errors are structural; correct negative profit is a weak design. Review status is a third distinct condition.

Calculator allowed for arithmetic C01/C02, numeric contribution/percent C03, boundary arithmetic C05, table values C06, C07/C08, comparison differences C09 and transfer numeric totals. Symbolic rules, classification, graph construction, interpretation and inequality/equality setup still require student responses. No built-in symbolic answer filler.

## 7. State, dependency and revision integrity

State separates fixed content, session identity/roles, active plan inputs, checked fields, attempts, immutable Plan A, mutable Plan B revisions, comparison/recommendation, individual transfers, reviews, overrides and print views. Each field records only dependencies that can change its answer; teacher solutions are derived separately.

| Edit | Must become Needs recheck | Must remain intact |
| --- | --- | --- |
| Stock q | C01 quantities/factor; C02 prepared lines/total; C07 sales/limits; C08 amounts/percentages; comparison and ending | Base recipe/costs, unit cost, fixed total, price/contribution/markup, sold-all models and graphs, fixed capacity and demand |
| Price p | C03; C04 revenue/profit coefficients; C05; C06 revenue points/crossing/loss; C07 demand/sales/limits; C08 revenue/profit/overstatement as affected; comparison/ending | Recipe/ledger, expense function/expense graph, capacity; preserve any mathematically independent C08 field |
| Cuisine, truck name, alias | Display/print labels only | Academic evidence and both historical plan contexts |
| Graph scale | Graph presentation/scale check only | Correct numeric table and ordered pairs |
| Reason/reviewer decision | Recommendation receipt/review status only | Calculations and transfer responses |

Use value-level fingerprints where an edit leaves a derived value unchanged: e.g. overstatement depends on v,q,s, not directly p. Do not mark unchanged siblings stale merely because an entire stage rerendered. Dependencies of a checkpoint's gate may require returning to that stage, but this does not erase its independent field evidence.

Plan A snapshots remain immutable. To change the original launch after freezing, offer Duplicate for a fresh comparison; preserve the existing session. Initialize B from A with explicit carried-forward provenance for unchanged checked fields; these are not new attempts or independent evidence. Changing B invalidates only affected fields. Editing B increments its scenario revision, retains previous attempts and invalidates C09/ending as needed. Recommending A does not skip B checks. Resume restores whether A is frozen and the active A/B context. A valid freeze is idempotent across Back/reload/import. No fabricated price disruption is added; the comparison is the required revision event.

Draft reports label stale/missing sections. Teacher bypass stores checkpoint/field, reason, reviewer alias, timestamp and context; it never becomes ordinary verified evidence. A later real successful recheck may retire an active bypass while retaining its history. Current summaries show the active plan; history retains original values and provenance.

## 8. Save, import, deletion and teacher controls

Project ID `food-truck`. Storage namespace `mcada:food-truck:session:<id>` and `mcada:food-truck:index`; no reuse of Road Trip keys and never localStorage.clear(). Autosave confirmed edits/transitions; announce Saved only after successful storage write. Retain raw partially entered values in memory immediately. Guard initial storage probing and quota/corruption errors; fall back to in-memory work with a persistent export reminder. No fictitious assurance of durable `file:` storage. Detect newer revisions in another tab; offer Reload or Save as copy, not silent merging.

Visible controls: New session, Resume, Duplicate, Export progress, Import progress, Export all as backup, Delete session and Clear all Food Truck sessions. Duplicating creates new IDs and a link to its origin without changing the original. A new session never overwrites a prior pair.

Use the dossier envelope: schema `mcada-project-progress`, schemaVersion 1.0.0, projectId, appVersion, contentVersion, sessionId, scenarioId `FT-BASE`, teamAlias, currentStage `FT-S01`…`FT-S08`, inputs, attempts, checkpoints, teacherOverrides and completedAt. Add explicitly validated fields for truckName, cuisineId, roles, localRevision, plan revisions/snapshots, comparison, transfers, support, reviews and imported provenance. Serialize rational values as bounded strings/decimal pairs, never Infinity/NaN. Preserve both plans and original contexts; rehydration must not substitute current p/q into Plan A.

Draft limits: UTF-8 JSON file≤5MiB; backup≤25 sessions; alias/truck/reviewer≤64 characters each; reasoning≤600; reviewer/override note≤400;≤10,000 attempts and≤100 retained plan snapshots per session. On reaching a storage/evidence limit, preserve existing history, explain the limit and offer export/new session; never silently drop first attempts. Confirm limits in implementation diagnostics and test their boundaries. Diagnostic export contains app/content versions, nonidentifying error information and status, with no telemetry.

Single export uses the session envelope; backup uses a separately discriminated `mcada-project-progress-bundle` schema with version 1.0.0, projectId, exportedAt and sessions array. Validate the whole file in temporary state: allowed fields/types/IDs, lengths, numeric/catalog bounds, plan references, distinct session IDs, supported versions, snapshot consistency and known checkpoints. Reject wrong-project/future-schema/unsupported-content/malformed state with current work untouched. A non-core q0 or edited fixed fee is not a legitimate core import merely because the pure evaluator supports it.

Preview session count, aliases, stage/version and identity collisions. Default Import as new copies; replacement requires named confirmation and an export-backup option. Recompute current mathematics and dependency statuses; never trust imported “verified” flags. Preserve reported history labeled imported; do not certify independent evidence. Stage writes and retain originals until index commit succeeds; rollback on failure and report any recovery failure honestly. No raw HTML or executable imported strings.

U-09: Delete session removes its complete associated A/B work, attempts, reviews and report state; Clear all applies only to Food Truck records. Show affected count/scope, Cancel, explicit confirmation and Export backup. Explain permanent local deletion and backup-based recovery; downloaded files, fixed content and other projects remain. Backup failure/cancel cannot be reported as success. Report partial deletion failures and selection/empty state truthfully. Test cancellation, reload, recovery and new-session creation.

Teacher mode exposes separate answers, review/oral submission recording, bypass and a built-in deterministic diagnostic with no mutation of student work. Any PIN is only a classroom deterrent; client-side answers/history are not securely hidden or tamper-proof. No real names, roster, location, password, automatic submission or student-network request is needed.

## 9. Endings and print artifacts

Apply precedence to the recommended plan, with comparison evidence from both:

1. Missing/stale required A/B calculation evidence, absent comparison/reason, or either individual submission absent → **Draft — finish checks**.
2. Active academic bypass used for any required completion → **Provisional — teacher review**, with an explicitly provisional business analysis.
3. Current recommended plan profit<0 → **Business rethink**.
4. Profit≥150 and10×waste≤q → **Festival success**.
5. Otherwise profit≥0 → **Viable first launch**.

Required C10 paper/oral work means an actual recorded submission; its pending review remains visible. Pending reasoning/transfer review does not falsely become an automatic academic approval. Each ending names two or three actual decisions and consequences, all applicable sales limits and the financial tradeoff. Negative-profit completion is legitimate. No hidden quality score, ranking or preferred cuisine. completedAt records first complete analyzed submission; later revisions keep their own timestamps.

Student business report target: four explicitly paginated A4/Letter pages, white background, page labels, alias, product credit, app/content version and date. Page1 menu/brief plus scaled recipe and itemized ledger; page2 sold-all models, table, revenue/cost graph and break-even interpretation; page3 Plan A/B launch comparison, limits, waste and recommendation; page4 individual submissions, first-versus-final evidence, help/override/review summary. Use the recommended plan on pages1–2 and identify it. Exact historical input values remain available on page3/export. Mark Draft and Provisional conspicuously.

Separate one-page printable menu/truck display card: chosen cuisine/name, price, selected plan and meaningful illustration, with no teacher key or invented successful sales. Separate teacher reference includes all three models, 12 outcome rows, accepted equivalent forms, transfer answers, misconceptions and review guidance. Separate learner transfer slips omit answers. Use native text/math, stacked fractions and exact SVG graphs; no full-page screenshot exports. Check A4/Letter at 100% portrait without browser headers/footers, wrapping and grayscale. Control flow must select one print view so hidden teacher content never leaks into student output.

## 10. Artwork and access

Visual direction: street-market posters, tomato red, mustard, cream and charcoal, a prominent original truck and clean recipe/ledger cards. The truck's name/cuisine/menu and stock/sales/waste overlays reflect actual saved choices. The three-hour clock is a label, not a timer. Any animation is optional, reduced-motion aware and skippable.

| Asset ID | Required illustration / behavior |
| --- | --- |
| FT-A01 | Festival street/title scene with live truck-name text |
| FT-A02–A04 | Distinct rice bowl, wrap and noodle menu illustrations |
| FT-A05 | Ingredient baskets with distinguishable grain/vegetable/protein forms |
| FT-A06 | Sauce/measurement concept illustration |
| FT-A07 | Packaging concept illustration |
| FT-A08 | Recipe tray/ratio strip and purchasing-ledger visual; quantity input alternative to drag |
| FT-A09 | Service-hatch capacity/inspection notice; 3-hour label drawn in code |
| FT-A10–A12 | Festival success, viable trial and rethink scenes, sharing a base if useful but visibly distinct and numerically faithful |

This meets the common title/evolving-scene/six-concept/inspection/three-ending asset floor. Dossier food.svg/png are references, not a complete final asset library. Maintain an asset manifest with purpose, stage, dimensions, alt text, source/license or original status, and whether scale is meaningful. Mathematical labels/graphs are code-rendered; decorative art must not encode uncertain numbers. Aim≤8MiB HTML; review before exceeding12MiB.

Minimum 44×44 CSS-pixel controls/help, 16px body/input text, keyboard focus, sufficient contrast and text error messages. SVGs have titles/descriptions and data equivalents; decorative art has empty alt. Every drag has touch/keyboard field alternatives. Inspect iPad portrait/landscape, narrow screens, 200% text and on-screen keyboard without hiding inputs, errors or Next. No nested scroll traps or hover-only help. Physical-device/network results remain separate from emulation.

## 11. Verification contract

The [reference fixtures](../../food-truck-business-launch/tests/reference-cases-v0.1.0.json) and [independent checker](../../food-truck-business-launch/tests/verify_spec_reference.py) validate this draft's mathematics, not an application. The [preparation review](../verification/FOOD-TRUCK-v0.1.0-SPEC-REVIEW.md) records the checks actually run. Use independent expected literals when later testing the JavaScript; do not make the app its own answer oracle.

| ID | Required implementation evidence | Current app result |
| --- | --- | --- |
| FT-Q01 | Ten objectives/C01–C10 and all eight stages; three lesson boundaries; extensions excluded | Not run |
| FT-Q02 | Recipe line costs, all four scales and packaging; fixed versus variable separation | Not run |
| FT-Q03 | All 12 price/stock outcomes, three model coefficient sets and markup values | Not run |
| FT-Q04 | Equivalent numeric/model/equality forms pass; wrong-model/right-total, malformed units/grouping, nonlinear and zero-divisor forms fail | Not run |
| FT-Q05 | Break-even exact/noninteger/strict thresholds; c≤0 and domain-boundary defensive cases; $9 capacity infeasibility explained | Not run |
| FT-Q06 | Six entered table cells and independently plotted points, exact fractional crossing, axes/scales and negative profit display | Not run |
| FT-Q07 | min(stock,demand,capacity), every tied limiter, capacity distinct from preparation | Not run |
| FT-Q08 | Expense uses q, not s; signed profit; v×waste overstatement; zero-stock null percentages in evaluator only | Not run |
| FT-Q09 | Exact ≥150 and ≤10% boundaries; all three business endings plus Draft/Provisional; choose A or B without forced optimization | Not run |
| FT-Q10 | Exactly dependent fields stale; retained siblings/history; Plan A freeze once; Plan B edit/reload/import; no answer leakage | Not run |
| FT-Q11 | Both transfer variants; paper/oral submission/review; first versus corrected/imported evidence | Not run |
| FT-Q12 | Save/reload/duplicate; separate sessions; storage denial/quota/corruption and newer-tab conflict | Not run |
| FT-Q13 | Single/bundle export-import, default copies, named replacement/cancel/backup, rollback; malformed/future/wrong-project rejection | Not run |
| FT-Q14 | U-09 individual/whole-session/clear-all scope, cancellation, reload, partial failure, recovery and fresh session; Road Trip data preserved | Not run |
| FT-Q15 | Every Help/visible control, full success/rethink/revision journeys, teacher diagnostics/review/bypass | Not run |
| FT-Q16 | Desktop keyboard/mouse and emulated layouts; separately physical Safari iPad/on-screen keyboard and school network | Not run |
| FT-Q17 | A4/Letter report/reference/menu/slips, exact math/SVG, four student pages, wrapping/grayscale, no teacher-key leakage | Not run |
| FT-Q18 | All registered art embedded, runtime offline, no network/font/audio requests; import strings inert; bounded errors recover | Not run |
| FT-Q19 | HTML byte identity, app/content/schema/README/guide/release-note consistency, measured artifact size | Not run |
| FT-Q20 | Actual Food Truck Pages subpath, served HTML hash/version, live save/export/import/print preview; Road Trip still works | Not run |

This covers dossier QA-01–20 plus project/U-09/deployment specifics. QA-05 scientific notation and dimensional-template calibration are Not applicable to Food Truck; fractions, signed values and exact graph coordinates remain required. Distinguish arithmetic references, implementation/browser tests, physical checks and hosting verification. A passing preparation suite cannot be labeled a passing app test.

## 12. Build and release sequence

1. Specification and FT-I01–I06 approved on 30 September 2026. Preserve this approved source baseline and its approval record before implementation.
2. Implement pure Food Truck evaluators and meaningful tests, then complete all screens, fixed content/help, state, reports and embedded art. Copy helpers as appropriate; no cross-project runtime.
3. Commit the complete implementation candidate before extended verification. Preserve its exact identity.
4. Verify the real workflows in FT-Q01–20. Fix defects, checkpoint changed bytes and rerun affected evidence. Never transfer old pass claims to changed artifacts.
5. Preserve a verified checkpoint and package the versioned HTML, identical index, guide/reference, asset manifest, README, CHANGELOG and QA report. No new feature work during packaging.
6. Deploy through the existing GitHub Pages `main`/root arrangement when implementation/release is authorized. Intended path `/Applied-Math-Projects/food-truck-business-launch/`; no live Food Truck URL is claimed now. Verify the actual served bytes and subpath, and preserve Road Trip's files/storage. No Netlify/Render/Cloudflare step is required by this plan.

Paths: `food-truck-business-launch/FoodTruck_v0.1.0.html`, `index.html`, `README.md`, `CHANGELOG.md`, `docs/PROJECT-BRIEF.md`, `docs/TEACHER-GUIDE.md`, `docs/ASSET-MANIFEST.md`, `docs/QA-REPORT-v0.1.0.md`, `tests/` and optional development `src/`/build script. Only HTML is needed to play.

If packaging or publishing fails, recover the preserved candidate rather than rebuild it. Future changes to mathematical content, prompts or schema require the corresponding version and explicit compatibility handling. Keep physical classroom acceptance pending until actual tests establish it.
