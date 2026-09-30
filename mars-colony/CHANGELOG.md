# Changelog

## 0.1.0 — Implementation candidate, 2026-09-30

First Mars Colony application, built under approved specification revision 1. Content and progress schema are both 1.0.0.

- Eight stages and ten objective/checkpoint groups covering rates, units, capacity, housing, resource functions/graphs, electrical energy, battery storage, cargo/budget, comparison and individual transfer.
- Exact numeric/fraction and linear-rule validation; bounded configuration model with shortages, capped stocks, curtailment and both solar/battery strategies.
- Draft, Provisional, Resilient outpost, Mission ready and Deployment delayed states; retained first attempts, corrections, help, revisions and separate teacher review.
- Alias-based local missions, JSON export/import, duplication/fresh revision, conflict handling, confirmed per-session deletion and Mars-only clear-all.
- Original inline vector art; student report, teacher reference, transfer slips and personalized mission patch.
- Readable source with deterministic single-file build; independent model tests, in-process DOM workflow checks and a prepared browser suite.

Verification corrections included hiding unchecked revised totals in draft reports, applying individual-transfer bypasses to Provisional status, preventing deleted active work from being autosaved again, keeping unsaved work when starting another mission fails, and completing field metadata/system diagrams.

This is **not a verified release or deployment**. Core and in-process DOM evidence is recorded in [QA](docs/QA-REPORT-v0.1.0.md). Real browser layout, offline/download behavior, PDF output, touch/keyboard and hosted-route checks remain pending. Physical iPad, school-network and printer checks remain pending separately. No earlier Mars schema exists to migrate.
