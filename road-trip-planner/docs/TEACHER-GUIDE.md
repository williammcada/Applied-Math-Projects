# Road Trip Planner — teacher guide and answers

**William McAda · A WILLIAM MCADA PRODUCT**  
**App 0.1.0 · Content 1.0.0 · Candidate dated 30 September 2026**

Use the in-app Teacher desk to print the formatted reference separately from student proposals. This document contains answers.

## Set up the lesson

The audience is advanced Grade 5 Introduction to Pre-Algebra / Saxon 8/7. Prior knowledge includes rational-number arithmetic, linear expressions, coordinates and simple inequalities. Plan for three 45-minute lessons; adjust to the class.

Pairs use learner labels A/B and a team alias. The Planner enters and explains; the Checker checks calculations and units. Swap roles at the end of stages 3 and 6. Export progress at those stops. Calculator permission is marked on arithmetic fields; students still construct the expressions, inequality, points and interpretation.

| Lesson | Stages | Evidence |
| --- | --- | --- |
| 1 | Commission, Route desk, Build the itinerary | Classifications, liters/fuel, party food, nights and hotel term |
| 2 | Modeling studio, Forecast wall, Budget review | Full model and coefficients, table/points, inequality, affordability, reserve and recommendation |
| 3 | Hotel alert, Client presentation | Frozen before/event/final comparison, revised work, separate individual transfer, proposal |

## Scenario and mathematical key

Three travelers request seven days with a $1,800 budget. The authored return route is 900 km, vehicle efficiency 12 km/L, and fuel $1.60/L. One-off costs total $200: booking $40, luggage $80 and supplies $80. Fuel is 75 L and $120 once per route. Seven days has six nights.

For vehicle rate r, hotel rate h, per-person food f, group activities a, and whole days 1–14:

`C(d) = 200 + 120 + rd + h(d−1) + 3fd + ad`

`m = r + h + 3f + a` and `b = 320 − h`.

m is the USD/day change. b is the adjusted constant in USD, not literal spending on a zero-day trip. Research routes may change fuel; the UI records source title, provider/link, access date, original distance/unit and return/one-way/segment interpretation. Source truth remains a teacher review.

| Scenario | Rule | C(1), C(3), C(5), C(7) | Reserve | Spent | Exact bound | Whole-day maximum |
| --- | --- | --- | --- | --- | --- | --- |
| Base: r40, h90, f20, a30 | 220d + 230 | 450, 890, 1330, 1770 | $30 | 98.33% | 157/22 | 7 |
| Hotel event: h110 | 240d + 210 | 450, 930, 1410, 1890 | −$90 | 105.00% | 53/8 | 6 |
| Food revision: f15 | 225d + 210 | 435, 885, 1335, 1785 | $15 | 99.17% | 106/15 | 7 |

Base C(8) is $1,990; revised C(8) is $2,010. The event adds 20 to m, subtracts 20 from b, and adds $120 over six nights. It applies exactly once to every hotel category: $80, $110, $150 after the event. Students must record this comparison before another choice revision. Reopening a saved session does not apply the increase again.

Fuel rounds only at the money subtotal. Percent spent rounds half up to 0.01%. Recurring bounds and liters accept exact fractions or equivalent quotients. The parser accepts factored/expanded linear expressions, Unicode arithmetic operators and correctly reversed inequalities. A correct seven-day total does not establish a correct full model.

## Choices and client fit

| Category | Choices and original USD rates | Fit points |
| --- | --- | --- |
| Vehicle, per group/day | City compact 30; Coastal wagon 40; Touring van 60 | 15 / 15 / 15 |
| Lodging, per group/night | Trail cabin 60; Lakeview lodge 90; Grand hotel 130 | 15 / 30 / 30 |
| Food, per person/day | Picnic plan 10; Local cafés 15; Food explorer 20 | 10 / 20 / 25 |
| Activities, per group/day | Quiet days 10; A little of both 20; Adventure pass 30 | 10 / 20 / 30 |

Client fit is a disclosed design preference, not an academic grade. Comfortable lodging and full activities are the primary priorities.

Apply outcome precedence: missing/stale work or missing hotel comparison → Draft; active teacher bypass → Provisional; over budget or fit below 65 → Revision requested; within budget and fit 65–84 → Trip approved; within budget and fit at least 85 → Client delighted.

The standard hotel/full food/full activities event plan correctly reaches Revision requested at $1,890. The balanced-food revision reaches Client delighted at $1,785 / 95 fit. Basic vehicle, standard hotel, balanced food and quiet activities reaches Trip approved at $1,575 / 75. Basic vehicle, standard hotel, balanced food and varied activities reaches Client delighted at $1,645 / 85, with a reserve statement. Underspending can earn the top outcome.

A reserve outside 0–5% of budget requires a statement. A negative reserve or percent above 100 can be the correct arithmetic. Do not invent an arithmetic error to force a better design.

## Individual evidence and review

Learner A: a new trip costs $160/day and $240 once; `T(d)=160d+240`, `T(4)=$880`.

Learner B: a new trip costs $145/day and $310 once; `T(d)=145d+310`, `T(6)=$1,180`.

Only one learner's task is displayed at a time. The separate print slips omit keys. Ask the other learner to look away; the app does not claim proctored independence. Teacher mode can record an actual paper/oral submission, initially pending, then mark it verified or requiring follow-up. No digital attempts are fabricated.

Automatic checks assess mathematics and structural completion. A received sentence is not a verified justification. Review recommendation quality, reserve reasoning, research truth and oral/paper work separately. A logged bypass requires checkpoint, reviewer alias and reason. It makes active completion provisional until a correct recheck retires the bypass; history remains.

Exported JSON retains first/final field submissions, timestamps, scenario revision, normalized mathematical values, dependency fingerprints, help and overrides. The proposal summarizes first-check versus current evidence without claiming a mastery percentage. Imported history is labeled and cannot certify independence. Teacher mode is not secure authentication.

## Recovery and delivery

Use aliases. Save locally and export after every lesson. Browser storage is not cross-device synchronization. A denied/quota failure retains in-memory work and asks for export. A newer tab's revision offers reload or a separate copy.

Import validates a complete file before applying it. Copies are the default; replacements name matching records and offer backup. Deletion names the session count and associated history, offers Cancel and backup, preserves other apps, and does not remove downloaded files. Verify the downloaded backup exists before deletion. Corrupt saved records offer raw-file recovery.

Print student proposals separately from teacher keys. A4 and Letter PDF output were checked; physical printer behavior is still a classroom acceptance item. Physical Safari iPad and school-network testing are also pending. See the [QA report](QA-REPORT-v0.1.0.md) before treating the candidate as classroom-ready.
