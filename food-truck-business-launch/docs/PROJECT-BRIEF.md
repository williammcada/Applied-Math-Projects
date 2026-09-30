# Food Truck / Business Launch — project brief

**Brief version:** 0.1, 30 September 2026  
**Owner:** William McAda · **Credit:** A WILLIAM MCADA PRODUCT  
**Project ID:** `food-truck` · **Directory:** `food-truck-business-launch`  
**Status:** Implementation specification Draft 1 prepared for review. No executable application exists.  
**Target:** app 0.1.0 / content 1.0.0 / initial save schema 1.0.0  
**Repository baseline:** `cf13e7f3111b2291a07c1387707fbb5d8b814ad5`

## Purpose and source

The second project in the dossier's Road Trip → Food Truck → Theme Park → Mars Colony → Powers of Ten sequence. Pairs plan a three-hour festival launch, connect proportional recipe scaling to linear business models, distinguish break-even from positive profit, and account for unsold prepared stock before defending a revision.

Use [dossier v1.0.0](../../docs/sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md), common sections 01–12, Food Truck 18–22 and release/source 39–42. The source package and attached Word identity are preserved in [provenance](../../docs/sources/PROVENANCE.md). The [implementation specification](../../docs/change-specs/FOOD-TRUCK-v0.1.0.md) is Draft 1, pending owner review. Preparation authorization is not recorded as approval of its implementation details.

Audience: advanced Grade 5 pre-algebra / Saxon 8/7; pairs sharing an iPad, desktop keyboard/mouse supported. Three proposed 45-minute lessons, role swaps after lessons one and two, separate learner transfer. English is brief and ELL-friendly. Classroom prices/forecasts are authored, not live or empirical market data.

## Must retain

- Eight stages and all ten objectives FT-01–FT-10 with required field-level evidence.
- Recipe for 20 portions: 2 kg grain at $5/kg, 3 kg vegetables at $6/kg, 2 kg protein at $20/kg, 0.5 L sauce at $20/L, 20 packages at $0.60; batch $90, portion $4.50.
- Fixed launch expense $450; prices $9/$12/$15 with demand 120/90/60; service 32/hour for 3 hours; stock 60/80/100/120.
- Sold-all R(x)=px, C(x)=F+vx, P(x)=(p−v)x−F; coefficient validation and learner-built tables/graphs; exact crossing versus strict positive-profit threshold.
- Realized sales=min(stock,demand,capacity); revenue from sold meals and expense from all prepared meals; signed profit, waste and sell-through.
- Sponsor targets profit≥$150 and waste≤10%; three transparent business endings plus Draft/Provisional. Correct loss-making analysis remains valid mathematics.
- First launch preserved as Plan A, distinct checked Plan B, recommendation of either with a numerical reason; individual transfer evidence and teacher-reviewed prose/oral work.
- Local alias-only sessions, export/import, recovery, session/group deletion and Food Truck-only clear-all; Road Trip storage remains separate.
- Independent self-contained HTML, embedded art, visible credit/version, touch/keyboard help, non-drag alternatives, student report/menu/display card, separate teacher reference and transfer slips. No audio.

## Reviewable implementation decisions

FT-I01 introduces an early provisional stock selection so recipe scaling can happen before the later stock confirmation. FT-I02 makes the cuisine skins explicitly share one classroom costing model. FT-I03 selects the canonical $12/100-portion starting plan. FT-I04 requires a different comparison plan while allowing either recommendation. FT-I05 excludes a general teacher scenario editor. FT-I06 treats the complete A/B session as the saved-work group. These preserve the dossier's numbers and objectives; all remain draft until specification approval.

The stock-only edit must not invalidate the sold-all cost model, since v and F remain unchanged. Price edits retain recipe and expense-only evidence. Historical Plan A never silently changes when B is edited. No random launch, hidden optimum, gradebook score, tax extension, second item or concert module enters core.

## Handbook and delivery

Handbook v0.1.1 at `00cbde605ab08203b6b5fd2374d225155608fc29`; AI-START-HERE, UNIVERSAL-RULES, CONDITIONAL-STANDARDS and RELEASE-CHECKLIST consulted. Apply U-01–U-08 project guidance, approved U-09 and S-02/S-04/S-05. Seeded/draft handbook sections are not newly promoted; no handbook amendment is proposed.

Use DESIGN → CHANGE SPEC → APPROVAL → IMPLEMENT → CHECKPOINT → VERIFY → VERIFIED CHECKPOINT → RELEASE → DEPLOY. GitHub is canonical. Runtime files will be `FoodTruck_v0.1.0.html` and identical `index.html`; development files may be separate, but play needs only HTML. Intended GitHub Pages subpath: `/Applied-Math-Projects/food-truck-business-launch/`, using the existing main/root configuration. No Food Truck live URL or runtime is claimed during preparation.

## Evidence and next step

[Preparation review](../../docs/verification/FOOD-TRUCK-v0.1.0-SPEC-REVIEW.md): 659/659 Food Truck reference assertions and 77/77 original dossier checks passed. These establish arithmetic and branch feasibility only. Parser/UI/save/import/print/artwork/device/deployment checks are Not run. Three of 12 stock/price plans meet Festival success; four are Viable first launch; five are Business rethink, conditional on completed academic gates.

Next: owner reviews Draft 1. After approval, preserve its exact source commit and build the complete v0.1.0 candidate. Road Trip remains deployed at 0.1.0 with physical iPad/network/printer acceptance still pending; Food Truck preparation does not certify that acceptance or modify Road Trip.
