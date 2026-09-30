# Road Trip Planner project brief

**Brief version:** 0.3, 30 September 2026  
**Owner:** William McAda  
**Product credit:** A WILLIAM MCADA PRODUCT  
**Repository:** williammcada/Applied-Math-Projects  
**Application directory:** road-trip-planner  
**Current implementation:** Complete v0.1.0 development candidate; local verification recorded below. Physical iPad/network acceptance and deployment pending.  
**Target release:** v0.1.0  
**Starting repository commit:** ec7753842c8321f5e2a9192529cb60da1e44d1b1

## Purpose and audience

Students plan a fictional trip for three travelers, model its cost as a linear function of days, interpret a table and graph, solve a budget inequality, and respond to a hotel-price change. The audience is advanced Grade 5 Introduction to Pre-Algebra/Saxon 8/7. Default use is pairs on an iPad with separate individual transfer evidence. Desktop keyboard/mouse must also work. Pacing is three proposed 45-minute lessons.

## Source and version contract

The immutable starting content is the [dossier v1.0.0](../../docs/sources/dossier-v1.0.0/William_McAda_Applied_Math_Projects_Dossier_v1.0.0.md), common sections 01–12, Road Trip sections 13–17, and acceptance/source sections 39–42. The attached Word copy matches the archived Word copy exactly. [Provenance](../../docs/sources/PROVENANCE.md) records its identity.

The current [implementation specification](../../docs/change-specs/ROAD-TRIP-PLANNER-v0.1.0.md) is approved revision 1. William McAda approved P-01 and merging the specification into main on 30 September 2026; see the [approval record](../../docs/decisions/ROAD-TRIP-v0.1.0-APPROVAL.md). First implementation checkpoint: `04e5c7ec88b9ccdf9abc4f0ff48191ea241b694c`; verified application candidate: `c73bc879faa065a4d51f91c75d68e4157abecbce`. App, content, and initial save-schema targets are respectively 0.1.0, 1.0.0, and 1.0.0; those numbers do not establish backward compatibility with a nonexistent prior app.

## Must retain

- Eight stages, RT-S01–S08; nine objectives/checkpoints, RT-01–09 and RT-C01–09.
- Fixed, per-day and per-night costs; party rates; fixed-route fuel; correct intercept; a student-constructed model, table, and graph; whole-day affordability; signed reserve and percent; event revision; separate transfer responses.
- Wrong required mathematics blocks the affected check with useful feedback. Correct analysis of a weak plan can reach Revision requested. Help, Back, Save, and export remain available.
- Contextual touch/keyboard help; unlimited revisions; first-attempt and final evidence; exact dependencies; preserved historical scenarios; teacher-reviewed prose/research and logged bypasses.
- Self-contained HTML with embedded art, readable math, vector graph, evolving travel scene, and three distinct outcomes. No music or runtime online service.
- Alias-only local sessions; export/import; printable proposal and teacher reference; no automatic gradebook submission or false claim of secure teacher authentication.

## Saved-work scope

Approved U-09 applies. A session includes its inputs, attempts, snapshots, reviews and derived report. Provide Delete session and Clear all Road Trip sessions with scope/count, explicit confirmation, Cancel, export backup, recovery explanation, reload persistence and fresh-session behavior. Preserve other applications and the fixed scenario catalog. No school-year/class manager is part of this release.

## Delivery and verification

Target files are a versioned RoadTripPlanner_v0.1.0.html and byte-identical index.html, teacher guide/answer reference, release notes and QA report. Development files may be separate; playing requires only the HTML. Intended hosting is GitHub Pages under this repository's road-trip-planner path. GitHub Pages is currently disabled; this candidate has not been deployed. Physical iPad and school-network checks remain explicit release evidence, separate from browser emulation.

Use DESIGN → CHANGE SPEC → IMPLEMENT → CHECKPOINT → VERIFY → VERIFIED CHECKPOINT → RELEASE → DEPLOY. Preserve the candidate before extended tests and package from the exact verified state. Use the twenty specification checks plus the original dossier acceptance contract. Reference arithmetic checks are not application tests.

## Applicable handbook

Consulted revision 00cbde605ab08203b6b5fd2374d225155608fc29, v0.1.1: AI-START-HERE.md, UNIVERSAL-RULES.md, CONDITIONAL-STANDARDS.md (S-02, S-04, S-05), RELEASE-CHECKLIST.md. U-09 is approved. Earlier seeded rules and selected draft modules retain their original status; this project already embodies their relevant principles. No unrelated local restrictions are imported.

## Approved decision

P-01 is approved: apply the $20/night event to whichever hotel the pair selected, including revised quotes for later switching. The resulting nightly rates are basic $80, standard $110, and premium $150. This explicitly supersedes the dossier's standard-only wording for Road Trip. There is no user-facing policy switch or separate standard-only comparison task.

## Preparation evidence

See the [preparation report](../../docs/verification/ROAD-TRIP-v0.1.0-SPEC-REVIEW.md). Original source hashes, 77 dossier reference checks, and 259 expanded Road Trip mathematical checks pass. Those were preparation-only checks. The complete application now has 662 core and 83 browser checks, plus inspected A4/Letter print output; see [QA report](QA-REPORT-v0.1.0.md). Physical device/network checks and actual deployment remain pending.
