# Road Trip Planner v0.1.0 implementation specification

**Specification revision:** Draft 1, 30 September 2026  
**Owner:** William McAda  
**Product credit:** A WILLIAM MCADA PRODUCT  
**Status:** Specification preparation and source preservation authorized. Existing dossier requirements are carried forward. P-01 below is a proposed content adjustment awaiting a decision. This is not an implemented or verified application release.  
**Canonical repository:** [williammcada/Applied-Math-Projects](https://github.com/williammcada/Applied-Math-Projects)  
**Planning baseline:** ec7753842c8321f5e2a9192529cb60da1e44d1b1  
**Application target:** 0.1.0. No previous executable release exists.  
**Handbook baseline:** 00cbde605ab08203b6b5fd2374d225155608fc29, v0.1.1.

## 1 Purpose and source authority

Build a complete classroom project in which a pair plans a trip, constructs a linear cost model, connects it to a table and graph, evaluates affordability, responds to a price change, and presents an evidence-based recommendation. The first release must cover the entire student journey and all three client outcomes.

The [original dossier](../sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md) supplies the design baseline. Read sections 01–12, 13–17, and 39–42. The Word dossier, original reference fixtures, checker, and concept art are preserved unchanged beside it. [Source provenance](../sources/PROVENANCE.md) records the hashes and retrieval. This specification makes the Road Trip implementation explicit; it does not replace the other four project chapters.

Current user instructions govern. The approved U-09 saved-work rule applies. U-01–U-08 and conditional modules S-02, S-04, and S-05 are applicable guidance already selected by the project brief; their handbook status remains seeded/draft rather than newly ratified universal rules. Consulted files: AI-START-HERE.md, UNIVERSAL-RULES.md, CONDITIONAL-STANDARDS.md, RELEASE-CHECKLIST.md. No assessment quotas, game penalties, music requirements, or shared backend are inherited from other products.

The repository change template predates this handbook revision. This document uses the current revision above. The attached Word file and the original package Word file have identical SHA-256 hashes. No conflict was found between those source copies.

## 2 Scope and retained requirements

Audience: advanced Grade 5 Introduction to Pre-Algebra, Saxon 8/7 context. Default: two students sharing an iPad, with full desktop keyboard/mouse support. English prompts are brief and ELL-friendly. Plan for three 45-minute lessons; this is an estimate, not a classroom-tested duration. Students alternate Planner and Checker after the first and second lesson chapters. Individual transfer evidence is separate from the shared plan.

Deliver one independent HTML application with inline CSS, plain JavaScript, system fonts, embedded artwork, and no required runtime network request. The versioned HTML and deployable index.html must be byte-identical. Primary iPad delivery is the hosted page; desktop users may open the downloaded HTML offline. Closing and reopening a hosted page offline is not promised.

Required: eight stages; nine objectives; contextual help; explicit academic validation; unlimited revision; first-attempt and final evidence; three client outcomes; teacher review/override records; local sessions; portable JSON; individual and all-session deletion; student print report; teacher reference; embedded pictures and an evolving itinerary scene. Save, Back, Help, and export remain available when an answer is wrong. No music, audio files, timers, or speed score.

Outside this release: the other four applications, a suite launcher, a reusable lesson engine, authoring UI, live AI, cloud accounts/sync, multiplayer, automatic GradeCam submission, real booking or payment, maps APIs, dynamic route drawing, live prices, advanced vehicle-efficiency comparisons, and currency conversion. Optional route research is a manually entered source record, not an online service integration.

## 3 Decisions and implementation assumptions

The numerical defaults and client ratings below come from the dossier and remain clearly labeled classroom assumptions. They are not market quotations or a scientifically validated measure of travel quality.

| ID | Decision or clarification | Status |
| --- | --- | --- |
| P-01 | Apply the $20/night disruption to the selected hotel category. On entry to the alert stage, all three hotel quotes receive the same $20 uplift; switching hotels afterward uses the revised quote. This guarantees that every pair revises a model and prevents changing categories from undoing the event. | Proposed change to the dossier's standard-hotel-only wording. Owner decision required before implementation. |
| I-01 | Core scenario keeps three travelers, a desired seven-day trip, and the $1,800 budget. All listed vehicle, hotel, food, and activity choices remain selectable. The stated 1–6 traveler and 1–14 day boundaries guide data validation and future teacher scenarios; no general scenario editor is added. | Concrete implementation of dossier defaults. |
| I-02 | Offer guided term construction and an equivalent-expression entry alternative. Both require independent slope/constant responses and interpretation; the app never accepts a right total as proof of a right model. | Implementation detail preserving C04. |
| I-03 | Digital individual transfer is the default. A teacher may record a separate paper/oral response, which stays pending review until checked. Device sharing alone is not evidence of independent work. | Implements dossier evidence and teacher-review rules. |
| I-04 | Do not add school-year/class folders. A session is the complete saved-work group: inputs, attempts, reviews, and reports. Provide Delete session and Clear all Road Trip sessions. | U-09 applied without an unnecessary management layer. |
| I-05 | For noncanonical research distances, keep exact rational fuel calculations, round the fuel-cost subtotal once to cents, then use that disclosed subtotal throughout the cost model. Do not round liters early. | Explicit precision policy needed for recurring decimal results; canonical figures are unchanged. |

If P-01 is declined, revise this specification before coding: retain the standard-only rate change and add a required standard-hotel comparison for pairs that selected another category. Do not silently skip RT-C08 or force all initial plans to choose the standard hotel. Do not build a user-facing switch between these two designs.

## 4 Scenario data and mathematical model

Use stable source IDs. Values shown here are in dollars; store monetary source values as integer cents. Preserve rational intermediate arithmetic where required.

| Source ID | Given data | Choices and meaning |
| --- | --- | --- |
| RT-D01 | Three travelers; seven desired days; budget $1,800 | Fixed core brief; Harbor City to Lakeview and back |
| RT-D02 | Total route 900 km; efficiency 12 km/L; fuel $1.60/L | Fixed route regardless of number of days; all core cars use 12 km/L |
| RT-D03 | One-off expenses $200 | Booking $40, luggage $80, supplies $80 |
| RT-D04 | Vehicle $30 / $40 / $60 per group per day | Basic / standard / touring; all fit the party; suitability 15 each |
| RT-D05 | Hotel $60 / $90 / $130 per group per night | Basic / standard / premium; client ratings 15 / 30 / 30 |
| RT-D06 | Food $10 / $15 / $20 per person per day | Client ratings 10 / 20 / 25 |
| RT-D07 | Activities $10 / $20 / $30 per group per day | Client ratings 10 / 20 / 30 |
| RT-D08 | Price event +$20 per night | Canonical standard rate becomes $110; extension to other categories depends on P-01 |

Publish all client ratings before selection. Lodging and activities are the two highest-weight priorities. Expensive cars and premium hotels do not earn additional ratings. The four component ratings form U, the disclosed client-fit indicator; U is not a mathematics grade.

Let p be party size, D total route distance, e efficiency, g fuel price, F one-off expenses, r daily vehicle price, h nightly lodging price, f per-person daily food, a group daily activities, B budget, and d whole travel days. Fixed core p=3; valid project duration 1≤d≤14.

- Liters = D/e; fuel subtotal K = gD/e, rounded once to cents only when needed.
- C(d) = F + K + rd + h(d−1) + pfd + ad.
- m = r+h+pf+a; b = F+K−h; C(d)=md+b.
- Reserve R = B−C(7), signed dollars. Spending percentage = 100C(7)/B, nearest 0.01%.
- Affordability: md+b≤B, continuous upper bound (B−b)/m, then interpret whole days in 1–14. If C(1)>B, answer is “No affordable trip.” If C(14)≤B, answer is 14 within this project domain; do not falsely say day 15 is unaffordable.

The model's intercept is an algebraic constant containing the −h adjustment, not actual spending on a zero-day holiday. The cost line may illustrate a continuous model, but only whole days in the valid domain represent available trips. Negative b is legitimate when a sufficiently expensive hotel creates it; do not impose a nonnegative-constant rule.

| Canonical phase | m | b | C(1), C(3), C(5), C(7) | Reserve at seven days | Maximum whole days |
| --- | ---: | ---: | --- | ---: | ---: |
| RT-BASE | 220 | 230 | 450, 890, 1330, 1770 | 30 | 7 |
| RT-HOTEL | 240 | 210 | 450, 930, 1410, 1890 | −90 | 6 |
| RT-REVISION | 225 | 210 | 435, 885, 1335, 1785 | 15 | 7 |

RT-HOTEL changes h from 90 to 110. RT-REVISION then changes f from 20 to 15. The event changes m by +20, b by −20, and the seven-day total by +120. Base spending is 98.33%; event spending 105.00%; revised spending 99.17%. Base continuous crossing is 157/22; event crossing 53/8; revised crossing 106/15. Base day 8 costs $1,990; revised day 8 costs $2,010.

## 5 Student journey

Persistent controls show project/version, team alias, current stage, save status, Back, Save, Export progress, and relevant Help. On desktop use a main working area and a restrained itinerary panel; on iPad stack them as needed. No nested scrolling or fixed panel may hide the focused input, error, or navigation. Do not reveal calculated answers in the itinerary panel before the corresponding check passes.

| Stage | Required screen and action | Completion condition |
| --- | --- | --- |
| RT-S01 Commission | Title scene, short client brief, alias, Planner/Checker roles. “Which two priorities matter most to these clients?” Show the four disclosed ratings. | Alias and role selection; confirm lodging and activities. This is a supported briefing task, not scored mastery. |
| RT-S02 Route desk | Schematic route, 900 km total round trip, efficiency and fuel-price cards. “Enter the total distance this vehicle will travel.” Optional manually entered teacher-approved source. | Valid distance and source status. Research stays marked pending until reviewed. |
| RT-S03 Build the itinerary | Select car, lodging, food, activities. Classify six cost cards; calculate liters, fuel cost, group food, and nights. The scene reflects selections without displaying unearned totals. | RT-C01–C03 current or an explicit logged teacher override. End lesson one; export and swap roles. |
| RT-S04 Modeling studio | Construct the full cost rule, enter m and b, label their units and interpretation. | RT-C04 current; neither a displayed answer nor a single substituted total satisfies this gate. |
| RT-S05 Forecast wall | Complete table for d=1,3,5,7; label graph; place four points; add the horizontal budget line; interpret the daily rise. | RT-C05 current. Verified model line appears only after plotting checks. |
| RT-S06 Budget review | Solve inequality; distinguish continuous crossing and whole days; calculate reserve and percentage; recommend a plan with one numerical reason. | RT-C06 and numeric/structural parts of RT-C07 current. Weak designs continue. End lesson two; export and swap roles. |
| RT-S07 Hotel alert | Freeze a before-event snapshot, show the changed quote, and require updated model, table, graph, affordability, and reserve. Then revise a choice or deliberately keep a weak plan. | RT-C08 verified for the event; final active plan's affected checkpoints current. No repeated event application after Back/reload. |
| RT-S08 Client presentation | Preview proposal, complete separate transfer responses, reveal client postcard, print/export, or duplicate for another revision. | Apply ending precedence in section 10. Draft and provisional reports remain available. |

Progress uses named stages and evidence status rather than a fabricated mastery percentage. A future stage identifies its missing prerequisite. A failed Check moves keyboard focus to a linked error summary; correct fields remain intact. Check on request or blur, not on every partially typed keystroke.

Calculator policy: allow a teacher-supplied calculator for numeric arithmetic in C02, the group rate in C03, table values in C05, numerical checks in C06, percentages in C07, revised numbers in C08, and the total in C09. Label those fields “Calculator allowed.” Model construction, cost classification, graph placement, interpretation, and inequality setup still require student input. No built-in symbolic solver or auto-fill button is added.

Route-source fields are sourceMode (provided/researched), sourceTitle, providerOrLink, accessDate, routeType (roundTrip/oneWay/segmentTotal), originalDistance, originalUnit, totalDistanceKm, and reviewStatus. Core mode prepopulates the authored source card. Research can directly enter km or m (1 km=1,000 m); a one-way figure must be explicitly doubled for a return trip, and segment totals must show their components. Other source units require a teacher-recorded conversion before entry. Positive research distances outside 100–2,400 km require teacher review, not a claim that the route is geographically impossible. Link text is inert until the user explicitly opens a valid http/https link; no background fetch. Format/internal-consistency validation cannot establish source truth.

## 6 Checkpoint contracts

Each implementation record has id, objectiveId, sourceIds, prompt, fieldIds, allowed range, action, quantity dimensions, representation, accepted form, evaluator, units/precision, prerequisites, help, errors, evidence, and review policy. These are fixed Road Trip records, not a generic lesson-authoring system. IDs below are permanent; source IDs refer to section 4.

Common evidence: preserve first checked response and final response separately, timestamp, scenario revision, attempt count, help used, dependencies, and any teacher override. Typing, opening Help, and a failed prerequisite check do not count as mathematical attempts. Record responses actually submitted to an evaluator. An error in one field does not erase accepted siblings.

### RT-C01 Classify costs

Objective RT-01; sources RT-D02–D07; prerequisite valid route and all four choices. Fields RT-F01.costClass.{oneOff,fuel,vehicle,hotel,food,activities}. Prompt: “Sort each cost: once for this route, every day, or every night.” Representation: six selectable cards with tap and keyboard alternatives. Exact key: oneOff/fuel → once; vehicle/food/activities → day; hotel → night. Food also retains its per-person label. Domain: six known IDs and three category enums; no numeric rounding. Pass only when all six match. Feedback names the incorrect card: “This route stays the same when the trip lasts longer. Fuel is a once-per-route cost.” Store each classification and result; no prose review.

### RT-C02 Calculate fuel

Objective RT-02; source RT-D02; prerequisite valid route/efficiency/price. Fields RT-F02.liters and RT-F02.fuelCost. Prompts: “How many liters will this route use?” and “What will that fuel cost?” Dimensions: km÷(km/L)=L, then L×USD/L=USD. Require numerical calculation with displayed unit labels, not a unitless guess. Canonical accepted values: 75 L and $120; equivalent exact decimals/fractions accepted. Noncanonical recurring liters may be entered as an exact fraction; explain this before checking. Fuel money uses the declared cents rule in section 4. Reject negative/zero input when it cannot satisfy the positive data. Evaluate each quantity independently. Wrong fuel must not pass because it follows an incorrect student liters value. Error: “Divide the route distance by kilometers per liter.” Preserve both responses and used source revision; research truth is separately teacher-reviewed.

### RT-C03 Scale daily and nightly costs

Objective RT-03; sources RT-D01, RT-D05, RT-D06; prerequisites valid choices. Fields RT-F03.partyFood, RT-F03.nights, RT-F03.hotelExpression. Prompts: “Find the food cost for the whole group each day.” “How many nights are in this seven-day trip?” “Write the hotel cost for d days.” Dimensions: USD/person/day×people=USD/day; d days entails d−1 nights. Canonical key: 60, 6, and 90(d−1). Accept equivalent hotel expressions such as 90d−90; compare both coefficients. Counts are exact integers; rates exact to cents; expression uses only d. Common errors: “That price is for one traveler. There are three travelers.” and “Seven travel days include six overnight stays.” Store rate, count, expression, and normalized model coefficients; no prose review.

### RT-C04 Construct and interpret the model

Objective RT-04; sources RT-D01–D07; prerequisites C01–C03 current. Fields RT-F04.expression, RT-F04.slope, RT-F04.constant, RT-F04.slopeMeaning, RT-F04.constantMeaning, RT-F04.domain. Prompt: “Write a rule for the total cost of d days on this fixed route.” Guided mode contains the six labeled terms F, K, rd, h(d−1), pfd, ad. Typed mode accepts any equivalent linear expression. In either mode independently enter m and b; do not fill them from the expression preview. Canonical key is (220,230), slope USD/day, constant USD, whole days 1–14. Required interpretations: m is cost of one additional day under the model; b combines route/one-off cost and the lodging subtraction and is not literal zero-day spending. Use selected statements with a brief optional explanation. Compare exact coefficients for the full expression and separately for m,b. A right seven-day total paired with 220d+200 fails. Error: “Expanding h(d−1) adds hd and subtracts h. Recheck the constant.” Record expression, normalized coefficients, interpretations, and domain. Optional free prose is not automatically graded.

### RT-C05 Connect table and graph

Objective RT-05; sources current verified C04 plus RT-D01; prerequisite C04 current. Fields RT-F05.table.{1,3,5,7}, RT-F05.xAxis, RT-F05.yAxis, RT-F05.xStep, RT-F05.yStep, RT-F05.points, RT-F05.budgetLine, RT-F05.rise. Prompt sequence: “Complete the table.” “Label the axes and plot the four points.” “Show the budget.” “How much does cost rise for one extra day?” Exact key is C(d) for each listed d, x=days, y=USD, horizontal y=B, rise=m. The graph defaults to one-day x ticks, 0–14 displayed with day-zero labeled outside the trip domain. Offer uniform y tick steps of $50, $100, $200, $500, or $1,000; compute a readable range covering budget and all required points. Selecting any uniform supported scale that covers the data is valid; tick spacing need not equal a point's coordinates. Place points by taps/drags with visible ordered-pair inputs; exact coordinate entry is always available. Check model coordinates, never raw pixel proximity. No arbitrary grid rounding: retain exact cents. Reject reversed axes or a sloped budget line with specific feedback. Record table values, axis/scale choices, four coordinates, budget line, and rise. Render a vector SVG and accessible data equivalent. Reveal the verified line after student construction; preserve discrete markers.

### RT-C06 Solve affordability

Objective RT-06; sources RT-D01 and current C04; prerequisite C05 current. Fields RT-F06.inequality, RT-F06.continuousBound, RT-F06.maxDays, RT-F06.costAtMax, RT-F06.nextDayCost. Prompt: “Find the longest affordable whole-day trip. Check your answer.” Accept an equivalent linear inequality with ≤ or correctly reversed ≥; normalize both sides and direction using exact arithmetic. Base key: d≤157/22, 7 whole days, C(7)=1770, C(8)=1990>B. An approximate bound to two decimals is display-only; the exact fraction or a guided (B−b)/m quotient establishes the bound. The student may enter the quotient using supplied budget/model values. Numeric entry accepts exact fractions and terminating decimals. The maxDays field is an integer 1–14 or the explicit “No affordable trip” response. If no day is affordable, require C(1)>B; if the domain cap is affordable, require C(14)≤B and show why a next-day failure check does not apply. Errors distinguish incorrect algebra from taking a fraction of a day. No prose review. Save the full inequality and verification evidence.

### RT-C07 Evaluate and recommend

Objective RT-07; sources RT-D01, RT-D04–D07 and current C04/C06; prerequisite C06 current. Fields RT-F07.total, RT-F07.reserve, RT-F07.percentSpent, RT-F07.priorityChecklist, RT-F07.recommendation, RT-F07.evidenceQuantity, RT-F07.reason, RT-F07.reserveStatement. Prompts: “How much is left after seven days?” “What percent of the budget is spent?” “Recommend this plan or a revision. Use one number to support your choice.” Evaluate total/reserve exactly to cents and percentage rounded half-up to 0.01%. Allow a negative reserve and percentage above 100; those can be correct mathematics. Confirm priority checklist against selected choices and published ratings. Require a known recommendation enum, a verified quantity selected from the student's results, and a short sentence or teacher-recorded oral response. Numeric and structural validation is automatic; reasoning quality is pending teacher review. If reserve/B is outside 0–0.05, request an allocation/revision statement. Exact 0% and 5% need no extra statement. Do not penalize a well-justified underspend. Error: “Reserve is budget minus trip cost. An overspend gives a negative reserve.” Store automatic checks and prose review separately.

### RT-C08 Revise the model

Objective RT-08; sources RT-D08 plus a preserved pre-event scenario; prerequisite C01–C07 current or logged overrides. Fields RT-F08.deltaSlope, RT-F08.deltaConstant, RT-F08.deltaTotal, RT-F08.explanation, and the phase-specific C04–C07 response records. Prompt: “The hotel quote rose by $20 per night. Update your model and compare the seven-day cost.” Mandatory event comparison before another choice can be used to bypass it. Key for a selected-hotel +20 event: +20 USD/day, −20 USD, +120 USD over six nights; structured explanation identifies the six nights and the h(d−1) term. Require updated equation, all four table values/points, inequality, reserve, and percentage. Reuse the existing evaluator functions with the new scenario revision. Then allow revising one or more choices, rechecking only affected work, or explicitly keeping the analyzed plan. An unchanged choice alone is not a revision task; an event calculation is still required. Common error: “There are six nights, so the increase is 6×$20.” Record before/event/final snapshots, each response's original context, and the choice-change log. Historical before/event evidence remains valid for its snapshot; final reports identify it as historical. Free explanation is teacher-reviewed; numeric delta/structured reason checks are automatic.

### RT-C09 Individual transfer

Objective RT-09; source RT-T01/T02 below; prerequisite RT-S08 and completed shared-plan calculations. Use learner labels A/B rather than names. Fields RT-F09.{A,B}.expression and RT-F09.{A,B}.total, plus response mode/reviewer status. Prompt A: “A different trip costs $160 each day and $240 once. Write T(d). Find the cost for four days.” Key: 160d+240 and $880. Prompt B: “Another trip costs $145 each day and $310 once. Write T(d). Find the cost for six days.” Key: 145d+310 and $1,180. Each is two parts, separate from the pair's itinerary; exact equivalent linear forms and money accepted. Show one learner's task at a time, do not reveal the other's response or a worked key, and offer separate printable slips. No claim of proctored independence. A teacher-recorded oral/paper submission stores mode and pending/verified/revise status; it does not invent digital attempts. Digital wrong answers allow unlimited revision and retain the first checked answer. These figures are new authored transfer fixtures, not added curriculum objectives. Store evidence by learner label; teacher can mark a suspected shared response as requiring follow-up.

### Help content required beside the fields

Every substantive field/group has a visible keyboard/touch “?” control. The panel contains meaning, unit/format, procedure, and an example with different numbers. Use Escape, Close, and outside-tap dismissal; return focus to the initiating button. Examples are support rather than penalties. At minimum use these reviewed examples; never inject the active answer into Help.

| Checkpoint | Help meaning and format | Procedure and different-number example |
| --- | --- | --- |
| C01 | A cost can occur once, every day, or every night. | Ask what changes when only the duration changes. A $25 booking charge is paid once; a $12/day rental is daily. |
| C02 | km/L means kilometers traveled using one liter. | Divide km by km/L, then multiply liters by price/L. 240 km ÷ 12 km/L = 20 L; at $1.50/L, fuel costs $30. |
| C03 | Per-person prices must cover the whole party; nights are one fewer than days. | Four travelers at $8 each cost $32/day. Five days have four nights; a $50 hotel gives 50(d−1). |
| C04 | m is the daily change; b is the constant after simplifying. | Expand nightly cost before combining terms: 50d+70(d−1)+100 = 120d+30. |
| C05 | An ordered pair is (days,cost); equal distances on an axis mean equal changes. | For C(d)=100d+50, three days gives (3,350). A $600 budget is horizontal at y=600. |
| C06 | A continuous bound can fall between whole-day choices. | If 100d+50≤600, then d≤5.5. Five whole days fit; six cost $650 and do not. |
| C07 | Reserve is signed money left; percent compares spending with the budget. | $1,000−$850=$150; 850/1000×100=85%. A $1,050 cost instead gives −$50 reserve. |
| C08 | A nightly increase changes both coefficients in a days-based model. | A $10 increase over four nights adds $40. The term +10(d−1) changes m by +10 and b by −10. |
| C09 | Combine a daily part and a once-only part for a new situation. | $90/day plus $120 once gives T(d)=90d+120; at three days, cost is $390. |

## 7 Answer parsing and mathematical display

Keep pure evaluation separate from UI and persistence. Suggested function boundaries: parseRational, parseLinear, compareLinear, normalizeInequality, modelForScenario, validateCheckpoint, affectedFields, and determineOutcome. These are small Road Trip functions, not a new framework.

Normalize whitespace, Unicode minus, ×/· and ÷, and valid thousands separators. Accept an optional matching $ prefix or declared unit suffix, while rejecting conflicting units. Numeric fields accept finite signed decimals, integers, and simple fractions a/b with nonzero denominator; malformed comma decimals receive a format explanation. Counts remain integers. Do not accept empty strings as zero, Infinity, NaN, hexadecimal literals, markup, functions, or executable input.

Expression grammar permits numbers, d, parentheses, +, −, multiplication and division. Support common implicit multiplication such as 220d, 90(d−1), and 3×20d. Division must be by a constant nonzero expression. This project does not need powers. Reject nonlinear terms and unsupported variables explicitly. Parse into exact coefficient pairs; never use eval, string matching, or agreement at one input. The inequality parser compares the difference of both linear sides and handles reversed direction; equality alone is not an inequality response.

Display fractions vertically, exponents where needed as true superscripts, and negative signs to the left of a fraction. Use native HTML/CSS or inline mathematical markup with an accessible verbal form, without remote fonts or renderers. Graphs and exact diagrams are application-rendered SVG. Print the same mathematical content rather than screenshotting a canvas. Money inputs carry visible USD labels; rates state per person/group and per day/night.

Suggested input limits: 256 characters per expression, 32 numeric-token digits, 16 nesting levels, 64-character alias, 280-character reasoning field, 512-character source link, and 2 MiB per imported session. These are proposed implementation limits for this release, not cross-project rules. Enforce a known safe text/type/range schema before evaluating. Display a useful export/recovery option rather than silently truncating existing work.

## 8 Dependency and revision behavior

Use one explicit dependency map. A fingerprint covers the values and content/evaluator revision a response actually depends on. Derive it from canonical serialized inputs; a raw session-wide edit counter is not enough. Touching an alias must not invalidate arithmetic. Editing upstream data changes relevant records to Needs recheck while retaining previous entries. Do not automatically regrade them against the new scenario or overwrite old attempts.

| Changed input | Required rechecks | Evidence retained without recheck |
| --- | --- | --- |
| Distance, efficiency, fuel price | C02; C04; C05; C06; C07; affected C08 active-plan work and outcome | Cost-category classifications, nights/group food, transfer |
| Hotel quote/category | Hotel term in C03; C04–C07; affected C08 and outcome | Route/fuel, category classifications, group food; nights if duration unchanged |
| Food price or party size | Group food in C03; C04–C07; affected C08 and outcome | Route/fuel and unchanged lodging inputs |
| Vehicle or activity price | C04–C07; affected C08 and outcome | C01–C03 when efficiency/party remain unchanged |
| Budget | C05 budget line, C06, C07, outcome | Model and plotted cost points |
| Desired duration in a future supported scenario | Nights for that duration, selected total/reserve, event-total comparison, outcome | The symbolic cost model and fixed-day table if their source values are unchanged |
| Alias, roles, prose wording, review status | Report text/review label only | Mathematical results |

The default UI does not expose a general budget/party editor, but imported supported state must still be internally coherent. A new choice may invalidate only part of a checkpoint; aggregate status is current only when every required field is current.

Freeze the before-event plan when RT-E01 first runs. Persist an eventApplied flag and event identity. Revised prices come from the base price plus the event delta exactly once, not from incrementing the previous displayed value on each render. Later choices use that phase's catalog. To explore a fresh event from a different baseline, duplicate or create a session; preserve the previous event evidence. C08 needs a valid recorded event comparison, while the latest final-plan answers must reference the active snapshot.

## 9 State and saved work

Use the dossier's progress envelope: schema=mcada-project-progress, schemaVersion=1.0.0, projectId=road-trip, appVersion=0.1.0, contentVersion=1.0.0, sessionId, scenarioId, teamAlias, currentStage, inputs, attempts, checkpoints, teacherOverrides, completedAt. Add scenarioRevision, localRevision, updatedAt, eventApplied, scenarioSnapshots, choiceHistory, reviews, and per-learner transfer records as the explicit initial schema. This specification has no prior real app save to migrate; do not claim compatibility with invented earlier releases.

Each checkpoint record stores field responses, state (unstarted/inProgress/verified/needsRecheck/overridden), dependency values/fingerprint, first attempt reference per scenario revision, final attempt reference, support events, and teacher-review status. Review status (notRequired/pending/verified/revise) is separate from arithmetic state. Snapshots hold the actual source values and event catalog so exported history does not depend on current app defaults. Attempts are append-only within a session until the owner explicitly deletes that session. Store decimal or rational values in lossless JSON forms; never serialize binary rounding as instructional truth.

Use project-specific keys such as mcada:road-trip:session:<id> and mcada:road-trip:index. Test storage with a guarded write/read/delete at startup. Show Saved only after a successful write. Autosave confirmed edits and transitions; on quota/denial/corruption keep usable in-memory work, show a persistent export reminder, and do not claim success. A second tab with a newer revision prompts Reload or Save as copy; do not silently merge or overwrite it.

New session, Resume, Duplicate for revision, Export, Import, Delete session, and Clear all Road Trip sessions are visible ordinary controls. Duplication creates a new identity and records the source session; editing it cannot modify the original. A single-session JSON export is portable between devices. A clear-all backup is a bundle with schema mcada-project-backup, schemaVersion 1.0.0, projectId road-trip, exportedAt, and an array of validated session envelopes. Both import forms are supported; bound a bundle to 20 MiB and 100 sessions and offer smaller batches if needed.

Import into temporary state, validate the entire file, preview alias/stage/version and collision handling, then commit atomically from the user's perspective. Detect known IDs, compatible schema/content, finite values, allowed keys/types, valid references, event consistency, and text limits. Reject wrong-project, unknown future schema/content, corrupt or oversized files without changing current work. Imported “verified” flags are not trusted: recompute mathematical/dependency validity; preserve reported history with an imported marker rather than certifying independent mastery. Reject unsupported content rather than silently substituting current values.

On identity collision, offer Import as copy by default; replacing an existing session requires a named confirmation and backup option. Stage all bundle records and keep originals until the new index write succeeds. Roll back newly created keys on failure; never announce an atomic success after a partial write. Do not switch the active session until commit succeeds. Existing reference libraries/scenario catalogs are never imported as executable code.

U-09 deletion: name the selected session or all Road Trip sessions, show the count, list the associated history/reviews included, and offer Cancel plus Export backup. Require explicit confirmation; explain that downloaded files are not removed and recovery needs the backup. Clear-all removes only this project's session/index data, including complete groups of related records, leaving other apps and fixed content intact. Never call localStorage.clear(). Treat backup cancellation/failure as unresolved and allow the user to return; do not pretend a backup exists. Report partial deletion failures accurately and retry safely. Verify cancellation, reload persistence, selection/empty state, new-session creation, and backup restoration.

Teacher mode shows solutions, review actions, local diagnostics, and logged bypass with checkpoint, reason, time, and reviewer alias. It cannot securely conceal client-side answers or produce tamper-proof records. Bypassed work is not ordinary verified work.

## 10 Endings and printable evidence

Apply this order to prevent misleading approval:

1. Missing/stale required active-plan work → Draft — finish checks. C09 must have both valid digital responses or recorded paper/oral submissions; a mere blank is not a submission.
2. Any academic bypass used for required completion → Provisional — teacher review, with the mathematical/design analysis shown. A completed independent recheck can retire an override from active completion while preserving its historical record.
3. Current analyzed plan above budget or U<65 → Revision requested.
4. Current plan within budget and 65≤U<85 → Trip approved.
5. Current plan within budget and U≥85 → Client delighted, with any required reserve statement submitted.

Show pending interpretation/research/transfer review separately in every outcome and report. Structural receipt of a sentence cannot become an automatic quality judgment. Submitted paper/oral transfer may allow a client outcome but its individual evidence remains explicitly pending. A missing required reserve/recommendation response prevents completion; an honestly analyzed overspend does not.

The postcard must identify actual selected choices and two or three numerical consequences. A large justified reserve can still receive Client delighted. Correct arithmetic paired with a poor plan is acknowledged; no red arithmetic error is invented to force financial success. Offer Back to revise, Duplicate, Export, and Print from every state. completedAt records the first complete analyzed submission, including a revision-requested plan; subsequent revisions have separate timestamps.

Student proposal target: three to four pages, A4 and Letter. Page 1 brief, source/route and itemized choices; page 2 annotated equation, table, SVG graph, affordability and interpretation; page 3 before/event/final comparison, recommendation, outcome and review status; page 4 individual transfer/evidence summary when needed. Use explicit report page sections and printed page labels. Include alias, app/content versions, date, units, first-attempt versus corrected status, help/overrides, and any pending review. Draft printing is allowed and marked. Do not truncate long source fields; constrain or wrap them.

Teacher reference is a separate print view/file containing canonical answers, legitimate equivalents, misconceptions, client-rating table, all outcome examples, and checkpoint review guidance. Student reports contain the students' work; never append hidden teacher keys through shared print CSS. Individual paper transfer slips must not print their answers. Provide a local diagnostic export with app/content versions, nonidentifying errors and checkpoint status; no telemetry or automatic submission.

## 11 Artwork and accessibility contract

Visual direction: travel journal/planning desk, warm paper, teal route lines, coral accents, navy readable text, and illustrated postcards. The evolving scene visibly changes vehicle, hotel, food, and activity selections. It is explanatory decoration, not a geographically accurate map. Do not encode figures or answer text inside generated raster art.

| Asset | Required content and behavior |
| --- | --- |
| RT-A01 | Wide illustrated travel desk title; no baked-in labels; responsive crop |
| RT-A02 | Schematic Harbor City–Lakeview return route, labeled total distance in code; “not to scale” |
| RT-A03, RT-A04, RT-A05 | Distinct basic, standard, and touring car illustrations |
| RT-A06 | Lodging illustration with distinguishable basic/standard/premium variants |
| RT-A07 | Food illustration with three readable choice variants |
| RT-A08 | Activity illustration with three readable choice variants |
| RT-A09 | Calm changed-hotel-quotation illustration; old and new numbers supplied by code |
| RT-A10, RT-A11, RT-A12 | Distinguishable delighted/approved/revision postcard states with actual itinerary overlays |

This register supplies the route plus at least six distinct concept/choice illustrations. The preserved road.svg/road.png are concept references, not a finished asset set. Keep an asset manifest with purpose, stage, dimensions, alt text, source/credit or original-art status, and whether scale is meaningful. Narrative art may be original SVG or optimized embedded raster. All required math/graphs are exact code-rendered graphics. Target ≤8 MiB HTML; review before exceeding 12 MiB.

All controls have visible focus, descriptive labels, and at least 44×44 CSS-pixel targets. Body and inputs are at least 16 px. Help works without hover; every drag has a tap/keyboard alternative. Reduced motion is respected; any reveal is skippable. Status/errors have text and appropriate live announcements. Test actual touch/keyboard navigation, portrait/landscape reflow, zoom, on-screen keyboard visibility, and grayscale printing. Do not claim physical iPad or school-network verification from emulation.

## 12 Verification contract

The accompanying [reference cases](../../road-trip-planner/tests/reference-cases-v0.1.0.json) and [checker](../../road-trip-planner/tests/verify_spec_reference.py) verify the specified mathematics and branch feasibility. They do not test an HTML application. Original dossier checks are also preserved. Use independent expected values when testing the eventual JavaScript; do not make the app its own answer oracle.

| Test | Required check and expected result | Current application status |
| --- | --- | --- |
| RT-Q01 | Nine objectives map to required evidence; eight stages reachable; extensions do not block core. | Not run |
| RT-Q02 | Base, event, and revision values reproduce section 4; fuel stays fixed; seven days means six nights. | Not run |
| RT-Q03 | Expanded/factored equivalent models pass; right total/wrong model, malformed expressions, nonlinear terms, zero divisors, conflicting units fail usefully. | Not run |
| RT-Q04 | Negative reserve and >100% spending can be correct; rounding to 0.01% is stated; no cent/float drift. | Not run |
| RT-Q05 | Students supply four table cells and four plotted points; reversed axes and sloped budget line fail; ordered-pair entry works on touch/keyboard. | Not run |
| RT-Q06 | Affordability tests include between-day crossing, exact boundary, no affordable day, and the 14-day domain cap. | Not run |
| RT-Q07 | Hotel/food/route/budget/alias edits invalidate only their dependencies; historical before/event answers retain context; no answer leakage. | Not run |
| RT-Q08 | Price event is exactly once after reload/Back; all choices follow the approved P-01 resolution; C08 cannot be skipped. | Not run |
| RT-Q09 | Saved fixture journeys reach all three client endings, Draft, and Provisional; underspending can earn top outcome; pending prose/transfer review stays visible. | Not run |
| RT-Q10 | Both independent transfer variants and paper/oral review path work; first attempts and corrected answers remain distinct. | Not run |
| RT-Q11 | Reload/session isolation, multiple-tab conflict, storage denial/quota/corruption, and save-status accuracy work. | Not run |
| RT-Q12 | Export/import single session and backup bundle preserve stage, inputs, attempts, event, review/override status; malformed/future/wrong-project import leaves work unchanged. | Not run |
| RT-Q13 | Deletion Cancel, single/all-project scope, backup recovery, partial failure, reload, new session, and unrelated app protection satisfy U-09. | Not run |
| RT-Q14 | Complete success and weak-design/revision journeys; every Help; every visible control; teacher review and bypass. | Not run |
| RT-Q15 | Desktop keyboard/mouse and emulated iPad portrait/landscape; separately physical Safari iPad with on-screen keyboard and actual school network. | Not run |
| RT-Q16 | A4 and Letter student/teacher print views: equations, stacked fractions, SVG, wrapped labels, page count/labels, no key leakage, no overlapping content. | Not run |
| RT-Q17 | Offline desktop full journey with network disabled; no required external asset/font request; import markup renders as inert text. | Not run |
| RT-Q18 | All art present, coherent and embedded; actual file size measured; every ending reports the actual plan. | Not run |
| RT-Q19 | Version/README/teacher guide/release notes agree; versioned HTML equals index.html byte-for-byte. | Not run |
| RT-Q20 | Actual GitHub Pages subpath opens the verified candidate; entry/assets, save/export/import and print spot-check; stale version ruled out. | Not run |

RT-Q01–20 collectively cover dossier QA-01–20 plus the Road Trip-specific checks. Record Passed/Failed/Not run/Not applicable with environment and evidence against the exact candidate. A static reference check is not a pass for RT-Q02 in the application column. Physical-device/network checks can remain explicitly pending in a development candidate but must not be hidden in a classroom-ready claim.

## 13 Build and release sequence

1. DESIGN / CHANGE SPEC: resolve P-01, record the decision and approved spec revision in the project brief, and preserve this packet as the source baseline.
2. IMPLEMENT: write pure evaluators and targeted tests, then the full journey, fixed checkpoint content, state/dependencies, help, reporting, embedded art, and responsive interactions. Complete these as parts of one application, not separate student products.
3. CHECKPOINT: commit the complete candidate with a meaningful message such as “Road Trip Planner v0.1.0 implementation checkpoint” before extended verification.
4. VERIFY: run reference and actual app tests, full success/revision paths, imports/deletion, prints, layout/input checks, and inspect all assets/endings. Fix defects and create a new candidate checkpoint when bytes change.
5. VERIFIED CHECKPOINT: preserve the exact candidate and evidence that passed the declared checks. Do not transfer results from an earlier commit to changed bytes.
6. RELEASE: generate the versioned HTML, byte-identical index.html, README, teacher guide/answer reference, release notes, and QA report from that candidate. Add no new features while packaging.
7. DEPLOY: use the existing repository's GitHub Pages delivery. Inspect current Pages settings before selecting a source; proposed URL path is /Applied-Math-Projects/road-trip-planner/. Enable/configure hosting only as part of the authorized build/deploy task. Verify the actual hosted bytes/version and running workflow. No deployment is part of this specification commit.

Suggested project paths: road-trip-planner/index.html; road-trip-planner/RoadTripPlanner_v0.1.0.html; road-trip-planner/README.md; road-trip-planner/docs/PROJECT-BRIEF.md; road-trip-planner/docs/TEACHER-GUIDE.md; road-trip-planner/CHANGELOG.md; road-trip-planner/tests/; road-trip-planner/docs/QA-REPORT-v0.1.0.md. Development support files do not become runtime dependencies.

If packaging/upload/deployment fails, recover the preserved candidate. Do not rebuild a verified implementation to fix a delivery problem. A later change to math, defaults, or prompts increments the appropriate content/app version and explicitly addresses existing saves.

## 14 Completion of this preparation task

This task supplies the preserved dossier/handoff, this implementation contract, a project-specific brief, reference cases and checker, and an honest preparation-verification record. It adds no executable app and does not claim app tests or deployment passed. The next concrete decision is P-01; the next development deliverable after specification approval is the complete Road Trip Planner v0.1.0 implementation candidate.
