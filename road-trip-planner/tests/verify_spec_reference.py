#!/usr/bin/env python3
"""Check Road Trip Draft 1 reference mathematics, not an HTML application.

Uses a direct itemized-cost sum to independently check coefficient-form totals.
The proposed selected-hotel event is labeled P-01; its tests do not approve it.
"""
import argparse
import itertools
import json
from fractions import Fraction as F
from pathlib import Path


def rounded_cents(value):
    """Exact half-up rounding for a rational dollar or percentage value."""
    sign = -1 if value < 0 else 1
    n = abs(value) * 100
    cents = (2 * n.numerator + n.denominator) // (2 * n.denominator)
    return F(sign * cents, 100)


def verify(data):
    checks = []

    def check(name, actual, expected):
        checks.append({"id": name, "passed": actual == expected,
                       "actual": str(actual), "expected": str(expected)})

    base = data["base"]
    party, days = base["party"], base["desiredDays"]
    budget, fixed = F(base["budget"]), F(base["oneOff"])
    liters = F(base["distanceKm"]) / F(base["kmPerLiter"])
    fuel = rounded_cents(liters * F(base["fuelPrice"]))
    order = ("vehicle", "hotel", "food", "activities")
    catalog = {kind: {row["id"]: row for row in data["choices"][kind]} for kind in order}

    def affordable(m, b, cap):
        # Enumeration is independent of the algebraic floor used by the spec.
        valid = [d for d in range(1, 15) if m * d + b <= cap]
        return max(valid) if valid else None

    def scenario(selection, event):
        rows = [catalog[k][name] for k, name in zip(order, selection)]
        r, h, f, a = [F(row["price"]) for row in rows]
        if event:
            h += F(base["hotelEventDelta"])
        m, b = r + h + party * f + a, fixed + fuel - h
        # Itemized travel costs, without using m or b.
        def direct(d):
            return fixed + fuel + r*d + h*(d-1) + party*f*d + a*d
        total = direct(days)
        reserve = budget - total
        fit = sum(row["fit"] for row in rows)
        outcome = "revision" if total > budget or fit < 65 else "approved" if fit < 85 else "delighted"
        result = {"liters": liters, "fuelCost": fuel, "m": m, "b": b,
                  "table": [direct(d) for d in base["tableDays"]],
                  "total": total, "reserve": reserve,
                  "percentSpent": rounded_cents(100 * total / budget),
                  "continuousBound": (budget-b)/m,
                  "maxDays": affordable(m, b, budget), "fit": fit,
                  "outcome": outcome, "reserveStatementRequired": not (0 <= reserve/budget <= F(1,20))}
        return result, direct

    for case in data["cases"]:
        actual, direct = scenario(case["selection"], case["event"])
        for key, expected in case["expected"].items():
            if key == "table":
                expected = [F(x) for x in expected]
            elif key not in ("fit", "outcome", "reserveStatementRequired", "maxDays"):
                expected = F(expected)
            check(case["id"] + "." + key, actual[key], expected)
        check(case["id"] + ".model_matches_itemized_all_days",
              all(actual["m"]*d + actual["b"] == direct(d) for d in range(1,15)), True)

    combinations = list(itertools.product(*(catalog[k] for k in order)))
    check("choice_count", len(combinations), 81)
    enumeration = []
    for event in (False, True):
        summaries = [scenario(selection, event)[0] for selection in combinations]
        outcomes = {k: sum(x["outcome"] == k for x in summaries) for k in ("delighted", "approved", "revision")}
        check(f"event_{event}.all_outcomes_reachable", all(outcomes.values()), True)
        check(f"event_{event}.at_least_three_affordable_plans", sum(x["total"] <= budget for x in summaries) >= 3, True)
        for selection in combinations:
            calculated, direct = scenario(selection, event)
            check(f"event_{event}.{'-'.join(selection)}.model",
                  all(calculated["m"]*d+calculated["b"] == direct(d) for d in range(1,15)), True)
        enumeration.append({"eventApplied": event, "combinations": len(summaries), "outcomes": outcomes,
                            "affordable": sum(x["total"] <= budget for x in summaries)})

    check("every_choice.event_delta",
          all(scenario(s, True)[0]["total"]-scenario(s, False)[0]["total"] == 120 for s in combinations), True)
    for case in data["affordabilityBoundaries"]:
        check("affordability."+case["id"], affordable(F(case["m"]), F(case["b"]), F(case["budget"])), case["expected"])
    for i, case in enumerate(data["reserveBoundaries"]):
        check("reserve_boundary."+str(i), not (0 <= F(case["reserve"])/F(case["budget"]) <= F(1,20)), case["required"])
    for case in data["transfer"]:
        check(case["id"], F(case["m"])*case["days"] + F(case["b"]), F(case["total"]))

    check("wrong_model.same_seven_day_total", 200*7+370, 1770)
    check("wrong_model.different_slope", 200 == 220, False)
    check("rounding.fuel_subtotal_100km", rounded_cents(F(100,12)*F("1.60")), F("13.33"))
    check("rounding.positive_half_cent", rounded_cents(F("1.005")), F("1.01"))
    check("rounding.negative_half_cent", rounded_cents(F("-1.005")), F("-1.01"))
    return {"scope": "Specification arithmetic, 81 choices before/after proposed P-01, and mathematical outcome feasibility only. No app, parser, UI, save, print, device, or deployment tested.",
            "specRevision": data["specRevision"], "eventPolicy": data["eventPolicy"],
            "passed": all(c["passed"] for c in checks), "count": len(checks),
            "choiceEnumeration": enumeration, "checks": checks}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report")
    args = parser.parse_args()
    source = Path(__file__).with_name("reference-cases-v0.1.0.json")
    result = verify(json.loads(source.read_text()))
    if args.report:
        Path(args.report).write_text(json.dumps(result, indent=2)+"\n")
    print(f"{sum(c['passed'] for c in result['checks'])}/{result['count']} specification reference checks passed.")
    print(json.dumps(result["choiceEnumeration"], indent=2))
    for item in result["checks"]:
        if not item["passed"]:
            print("FAIL", item)
    print(result["scope"])
    raise SystemExit(0 if result["passed"] else 1)
