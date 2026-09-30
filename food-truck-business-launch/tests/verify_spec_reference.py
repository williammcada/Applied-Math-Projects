#!/usr/bin/env python3
"""Independent arithmetic check of Food Truck specification Draft 1.

Standard library only. No HTML, JS parser, persistence, UI or deployment is tested.
Literal expected fixtures are compared with exact Fraction calculations; threshold
counts are also checked by enumerating sales, independently of floor/ceil formulas.
"""
import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path


def rounded_tenth(value):
    sign = -1 if value < 0 else 1
    n = abs(value) * 10
    return F(sign * ((2 * n.numerator + n.denominator) // (2 * n.denominator)), 10)


def percentages(stock, sales):
    if stock == 0:
        return None, None
    return F(100 * (stock-sales), stock), F(100 * sales, stock)


def outcome(profit, waste, stock, current=True, bypass=False):
    if not current:
        return "Draft"
    if bypass:
        return "Provisional"
    if profit < 0:
        return "Business rethink"
    if stock > 0 and profit >= 150 and 10 * waste <= stock:
        return "Festival success"
    return "Viable first launch"


def verify(data):
    checks = []

    def check(name, actual, expected):
        checks.append({"id": name, "passed": actual == expected,
                       "actual": str(actual), "expected": str(expected)})

    base = data["base"]
    ingredients = base["ingredients"]
    lines = [F(row["quantity"]) * F(row["unitPrice"]) for row in ingredients]
    for row, line in zip(ingredients, lines):
        check("recipe.base." + row["id"], line, F(row["expectedLineCost"]))
    batch = sum(lines)
    variable = batch / base["batchPortions"]
    fixed = F(base["fixedCost"])
    capacity = base["serviceRate"] * base["hours"]
    check("recipe.batch", batch, F(90))
    check("recipe.unit", variable, F("4.5"))
    check("service.capacity", capacity, 96)
    for row in data["recipes"]:
        q = row["stock"]
        k = F(q, base["batchPortions"])
        amounts = [F(item["quantity"]) * k for item in ingredients]
        costs = [a * F(item["unitPrice"]) for a, item in zip(amounts, ingredients)]
        prefix = "recipe." + str(q)
        check(prefix + ".factor", k, row["factor"])
        for index, item in enumerate(ingredients):
            check(prefix + ".quantity." + item["id"], amounts[index], F(row["quantities"][index]))
            check(prefix + ".cost." + item["id"], costs[index], F(row["lineCosts"][index]))
        check(prefix + ".total", sum(costs), F(row["total"]))
        check(prefix + ".unitInvariant", sum(costs) / q, variable)

    prices = {row["price"]: row for row in data["prices"]}
    for price_string, row in prices.items():
        p = F(price_string)
        c = p - variable
        crossing = fixed / c
        profit = lambda x: p * x - (fixed + variable * x)
        prefix = "price." + price_string
        check(prefix + ".contribution", c, F(row["contribution"]))
        check(prefix + ".markup", rounded_tenth(100 * c / variable), F(row["markup"]))
        check(prefix + ".crossing", crossing, F(row["crossing"]))
        check(prefix + ".crossingEquality", p * crossing, fixed + variable * crossing)
        check(prefix + ".crossingRevenue", p * crossing, F(row["crossingRevenue"]))
        # Enumerating integer sales is a separate method from algebraic rounding.
        first_nonloss = next(x for x in range(1000) if profit(x) >= 0)
        first_profit = next(x for x in range(1000) if profit(x) > 0)
        check(prefix + ".firstNonLoss", first_nonloss, row["firstNonLoss"])
        check(prefix + ".firstProfit", first_profit, row["firstProfit"])
        check(prefix + ".ceilRule", -(-crossing.numerator // crossing.denominator), first_nonloss)
        check(prefix + ".strictRule", crossing.numerator // crossing.denominator + 1, first_profit)
        check(prefix + ".profitBefore", profit(first_profit - 1), F(row["profitBefore"]))
        check(prefix + ".profitAt", profit(first_profit), F(row["profitAt"]))
        check(prefix + ".revenueTable", [p*x for x in (0, 60, 100)], list(map(F, row["revenueTable"])))
        check(prefix + ".expenseTable", [fixed+variable*x for x in (0, 60, 100)], list(map(F, (450, 720, 900))))
        check(prefix + ".lossAt30", profit(30), F(row["profitAt30"]))
        check(prefix + ".negativeProfitAtOrigin", profit(0), F(-450))
        for x in range(121):
            check(prefix + ".directVsLinear." + str(x), profit(x), c*x-fixed)
    check("lowPrice.thresholdExceedsCapacity", prices["9"]["firstNonLoss"] > capacity, True)
    check("wrongModel.sameRoot", 8*60-480, F("7.5")*60-450)
    check("wrongModel.coefficientsDiffer", (F(8), F(-480)) != (F("7.5"), F(-450)), True)

    check("catalog.completeGrid", {(r["price"], r["stock"]) for r in data["launches"]},
          {(p, q) for p in prices for q in (60, 80, 100, 120)})
    check("catalog.noDuplicateRows", len(data["launches"]), 12)
    results = {}
    for row in data["launches"]:
        p, q = F(row["price"]), row["stock"]
        demand = prices[row["price"]]["demand"]
        s = min(q, demand, capacity)
        # Itemized prepared ingredient purchases, independent of v*q expression.
        purchase = sum(F(item["quantity"])*F(q,20)*F(item["unitPrice"]) for item in ingredients)
        revenue, expense = p*s, fixed+purchase
        profit, waste = revenue-expense, q-s
        waste_percent, sell_through = percentages(q, s)
        actual = {"sales":s,"revenue":revenue,"expense":expense,"profit":profit,
                  "waste":waste,"wastePercent":waste_percent,"sellThrough":sell_through}
        for field, value in actual.items():
            check(row["id"] + "." + field, value, F(row[field]))
        limits = [name for name,value in (("stock",q),("demand",demand),("capacity",capacity)) if value==s]
        check(row["id"] + ".limits", limits, row["limits"])
        ending = outcome(profit,waste,q)
        check(row["id"] + ".ending", ending, row["ending"])
        check(row["id"] + ".expenseForms", expense, fixed+variable*q)
        check(row["id"] + ".percentComplement", actual["wastePercent"]+actual["sellThrough"], F(100))
        check(row["id"] + ".overstatement", (p-variable)*s-fixed-profit, variable*waste)
        results[row["id"]] = actual | {"ending":ending}
    check("endings.counts", dict(Counter(r["ending"] for r in results.values())),
          {"Festival success":3,"Viable first launch":4,"Business rethink":5})
    for revision in ("FT-LOW-WASTE", "FT-PREMIUM"):
        check(revision + ".deltaProfit", results[revision]["profit"]-results["FT-BASE"]["profit"], F(-30 if revision=="FT-LOW-WASTE" else 0))
        check(revision + ".deltaWaste", results[revision]["waste"]-results["FT-BASE"]["waste"], -10)
    check("baseline.naiveSoldAllProfit", (F(12)-variable)*90-fixed, F(225))
    check("baseline.overstatementLiteral", variable*10, F(45))

    for row in data["boundaryThresholds"]:
        fee, c = F(row["fixed"]), F(row["price"])-F(row["variable"])
        crossing = fee/c if c > 0 else None
        nonloss = next((x for x in range(1001) if c*x-fee >= 0), None)
        positive = next((x for x in range(1001) if c*x-fee > 0), None)
        check(row["id"] + ".crossing", crossing, None if row["crossing"] is None else F(row["crossing"]))
        check(row["id"] + ".nonloss", nonloss, row["firstNonLoss"])
        check(row["id"] + ".positive", positive, row["firstProfit"])
    for i,row in enumerate(data["endingBoundaries"]):
        check("ending.boundary."+str(i), outcome(F(row["profit"]),row["waste"],row["stock"]), row["ending"])
    check("rounding.halfUp", rounded_tenth(F("166.65")), F("166.7"))
    check("rounding.noThresholdFromDisplay", rounded_tenth(F(10100,1009)), F("10.0"))
    check("ending.draftBeforeBypass", outcome(180,10,100,current=False,bypass=True), "Draft")
    check("ending.bypassBeforeSuccess", outcome(180,10,100,bypass=True), "Provisional")
    check("zeroStock.profit", F(12)*0-fixed-variable*0, F(-450))
    check("zeroStock.wastePercent", percentages(0,0)[0], None)
    check("zeroStock.sellThrough", percentages(0,0)[1], None)
    check("ties.threeWay", [name for name,value in (("stock",96),("demand",96),("capacity",96)) if value==min(96,96,96)], ["stock","demand","capacity"])

    a = data["transfers"]["A"]
    c = F(a["price"])-F(a["variable"])
    check("transfer.A.slope", c, F(a["profitSlope"]))
    check("transfer.A.constant", -F(a["fixed"]), F(a["profitConstant"]))
    check("transfer.A.crossing", F(a["fixed"])/c, F(a["crossing"]))
    check("transfer.A.firstProfit", next(x for x in range(1000) if c*x-F(a["fixed"])>0), a["firstProfit"])
    b = data["transfers"]["B"]
    revenue, expense = F(b["price"])*b["sales"], F(b["fixed"])+F(b["variable"])*b["stock"]
    for field,value in {"revenue":revenue,"expense":expense,"profit":revenue-expense,
                        "waste":b["stock"]-b["sales"],"sellThrough":F(100*b["sales"],b["stock"])}.items():
        check("transfer.B."+field,value,F(b[field]))
    return {"scope":"Specification reference mathematics only; no Food Truck runtime exists",
            "checks":checks,"passed":sum(c["passed"] for c in checks),
            "failed":sum(not c["passed"] for c in checks),"total":len(checks),
            "endingCounts":dict(Counter(r["ending"] for r in results.values()))}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report",type=Path)
    args = parser.parse_args()
    source = Path(__file__).with_name("reference-cases-v0.1.0.json")
    report = verify(json.loads(source.read_text()))
    report["fixtureSha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    report["checkerSha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["checkedAtUtc"] = datetime.now(timezone.utc).isoformat()
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k!="checks"},indent=2))
    for result in report["checks"]:
        if not result["passed"]:
            print(result)
    raise SystemExit(1 if report["failed"] else 0)
