# Food Truck / Business Launch

**A WILLIAM MCADA PRODUCT · William McAda**

The next independent Applied Mathematics project after Road Trip Planner. Students scale a recipe, set a price, build business functions, forecast a festival launch, account for unsold stock and compare a revision.

**Current status:** v0.1.0 implementation specification Draft 1 is prepared for review. No Food Truck HTML application has been built or deployed.

- [Implementation specification — Draft 1](../docs/change-specs/FOOD-TRUCK-v0.1.0.md)
- [Project brief](docs/PROJECT-BRIEF.md)
- [Preparation review](../docs/verification/FOOD-TRUCK-v0.1.0-SPEC-REVIEW.md)
- [Reference cases](tests/reference-cases-v0.1.0.json)
- [Original dossier](../docs/sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md), sections 18–22

The draft preserves the source's eight stages, ten objectives, three price choices, four stock quantities and three business endings. The first launch and comparison plan remain separate. A correct calculation of a loss is valid work; financial success is not a mastery score.

Run preparation checks from the repository root:

```sh
python3 food-truck-business-launch/tests/verify_spec_reference.py
python3 docs/sources/dossier-v1.0.0/verify_reference_fixtures.py
```

These check reference mathematics, not a working application. Implementation follows specification review/approval, then preserved candidate, actual workflow verification, packaging and GitHub Pages deployment. The future standalone deliverables are `FoodTruck_v0.1.0.html` and a byte-identical `index.html`.
