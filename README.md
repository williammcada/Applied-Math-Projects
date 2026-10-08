# Applied Mathematics Project Series

**A WILLIAM MCADA PRODUCT**

A family of five interactive applied-mathematics projects: Road Trip Planner, Food Truck / Business Launch, Theme Park Designer, Mars Colony, and Powers of Ten / Scale of Reality.

[Open the project homepage](https://mcada-applied-math.netlify.app/) — choose a project, then **Share with students** to display its QR code.

## Canonical project record

**Repository:** `williammcada/Applied-Math-Projects`  
**Current state:** All five projects have runnable implementations. Mars Colony v0.1.0 is deployed to Netlify and verified (115 local + 12 hosted checks); see its deployment record. Netlify is the primary classroom host. Original dossier/handoff v1.0.0 and project-specific release histories are preserved. Physical iPad/school-network/printer acceptance remains pending.  
**Handbook:** `williammcada/mcada-project-handbook`

The repository is the canonical home for the current source, permanent project brief, and approved version-specific change specifications. Chat history is working context rather than the permanent project record.

## Road Trip Planner

[Open the live application](https://mcada-applied-math.netlify.app/road-trip-planner/) · [Download the self-contained application](road-trip-planner/RoadTripPlanner_v0.1.0.html) · [Getting started](road-trip-planner/README.md) · [Teacher guide](road-trip-planner/docs/TEACHER-GUIDE.md) · [QA report](road-trip-planner/docs/QA-REPORT-v0.1.0.md) · [Deployment record](road-trip-planner/docs/DEPLOYMENT-v0.1.0.md)

## Food Truck / Business Launch

[Open the application](https://mcada-applied-math.netlify.app/food-truck-business-launch/) · [Standalone HTML](food-truck-business-launch/FoodTruck_v0.1.0.html) · [Getting started](food-truck-business-launch/README.md) · [QA report](food-truck-business-launch/docs/QA-REPORT-v0.1.0.md)

## Powers of Ten

[Open the application](https://mcada-applied-math.netlify.app/powers-of-ten/) · [Standalone HTML](powers-of-ten/PowersOfTen_v0.1.0.html) · [Teacher guide](powers-of-ten/docs/TEACHER-GUIDE.md) · [QA report](powers-of-ten/docs/QA-REPORT-v0.1.0.md) · [Deployment record](powers-of-ten/docs/DEPLOYMENT-v0.1.0.md)

Powers of Ten v0.1.0 is implemented from its [approved specification](docs/change-specs/POWERS-OF-TEN-v0.1.0.md). Automated verification is complete; physical classroom acceptance remains pending.

## Theme Park Designer

[Open the application](https://mcada-applied-math.netlify.app/theme-park-designer/) · [Standalone HTML](theme-park-designer/ThemeParkDesigner_v0.1.0.html) · [Getting started](theme-park-designer/README.md) · [Teacher guide](theme-park-designer/docs/TEACHER-GUIDE.md) · [QA report](theme-park-designer/docs/QA-REPORT-v0.1.0.md) · [Deployment record](theme-park-designer/docs/DEPLOYMENT-v0.1.0.md)

Theme Park v0.1.0 is deployed and verified: 189 local assertions and 12 hosted assertions passed. Public HTML bytes match the preserved candidate. Physical classroom acceptance remains pending.

## Mars Colony

[Open Mars Colony](https://mcada-applied-math.netlify.app/mars-colony/) · [Standalone HTML](mars-colony/MarsColony_v0.1.0.html) · [Teacher guide](mars-colony/docs/TEACHER-GUIDE.md) · [Finalized specification](docs/change-specs/MARS-COLONY-v0.1.0.md) · [QA record](mars-colony/docs/QA-REPORT-v0.1.0.md) · [Deployment record](mars-colony/docs/DEPLOYMENT-v0.1.0.md)

Mars Colony v0.1.0 implements the dossier's ten learning objectives across three estimated lessons. Students calculate demand, module capacity, resource models, cargo/budget, storm energy and battery reserves; compare designs; complete individual transfer; and print a mission report. Verified checkpoint `9e7c69b`: 115 automated checks passed. Physical iPad, school-network and printer acceptance remains pending. Launcher v0.1.1 includes all five projects and Mars QR sharing.

## Documentation

- [Theme Park Designer v0.1.0 approved specification](docs/change-specs/THEME-PARK-DESIGNER-v0.1.0.md).

- [Food Truck v0.1.0 approved implementation specification](docs/change-specs/FOOD-TRUCK-v0.1.0.md).
- [`docs/PROJECT-BRIEF.md`](docs/PROJECT-BRIEF.md)
- [`docs/change-specs/`](docs/change-specs/)
- [Road Trip Planner v0.1.0 specification](docs/change-specs/ROAD-TRIP-PLANNER-v0.1.0.md)
- [Original dossier and handoff](docs/sources/dossier-v1.0.0/START_HERE.md)
- [Source provenance](docs/sources/PROVENANCE.md)
- [Specification preparation review](docs/verification/ROAD-TRIP-v0.1.0-SPEC-REVIEW.md)
- [McAda Project Handbook](https://github.com/williammcada/mcada-project-handbook)

Use the project brief for permanent project-local rules and the change-spec directory for version-specific approved decisions.

Build order remains Road Trip → Food Truck → Theme Park → Mars Colony → Powers of Ten. Each is a separate self-contained HTML application. Road Trip's selected-hotel event adjustment P-01 and specification revision 1 were approved on 30 September 2026. See the [approval record](docs/decisions/ROAD-TRIP-v0.1.0-APPROVAL.md).

## Release workflow

**DESIGN → CHANGE SPEC → IMPLEMENT → CHECKPOINT → VERIFY → VERIFIED CHECKPOINT → RELEASE → DEPLOY (when applicable)**

Do not treat a renamed file, README update, successful build, or packaging attempt as proof that the intended release is actually running. Preserve accepted behavior unless the approved change specification deliberately changes it.



## Ownership

**William McAda**  
**A WILLIAM MCADA PRODUCT**
