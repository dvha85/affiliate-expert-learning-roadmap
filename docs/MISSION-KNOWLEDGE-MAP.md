# Mission ↔ Knowledge Map

This file is the central just-in-time mapping layer. It intentionally avoids bulk-editing 671 lesson front matters.

## Semantics

- **REQUIRED** — required for Mission PASS.
- **ON-DEMAND** — pull when a concrete implementation/business trigger appears.
- **REFERENCE** — useful deeper context, not a Mission PASS gate.

Explicit lesson IDs below must resolve in the canonical 671 inventory. Part/chapter themes identify future pulls to refine as missions/lessons are authored.

## M00 — Bot Boots

**REQUIRED**
- `0.1` — Affiliate Expert là gì?
- `0.2` — Affiliate Bot Engineer là gì?

**ON-DEMAND**
- Minimal Go syntax needed to run the bootstrap app.

## M01 — Product Ingest

**REQUIRED themes**
- Affiliate product/business vocabulary.
- Go struct, JSON, error handling and validation.

**ON-DEMAND**
- Platform-specific product fields only when a real adapter is introduced.

## M02 — Product Store & History

**REQUIRED themes**
- Part 12 data model/history concepts.
- SQL, repository boundary, migration and snapshot semantics.

## M03 — First Product Ranking

**REQUIRED**
- `5.11` — Expected Value.
- `27.3` — Ranking.

**ON-DEMAND themes**
- Demand, Product–Audience Fit, price, CVR, valid-order/refund risk, seller/product quality.

**REFERENCE**
- Advanced statistical ranking and AI scoring are intentionally deferred.

## M04 — Product Watcher

**REQUIRED themes**
- snapshot/delta semantics, scheduler, context/cancellation.

**ON-DEMAND**
- bounded concurrency when sequential collection becomes a real bottleneck.

## M05 — Reliable Alerts

**REQUIRED themes**
- rules/thresholds, timeout, retry/backoff, idempotency/deduplication.

## M06 — Product Intelligence v1

**REQUIRED themes**
- Parts 2, 6, 7 and 8: economics + market + customer + product intelligence.

## M07 — Content Intelligence

**REQUIRED themes**
- Parts 9–11: content/psychology + traffic context + funnel/conversion.

## M08 — Revenue & Attribution Intelligence

**REQUIRED themes**
- Parts 2, 3, 11–13: economics, tracking/attribution, funnel, data, analytics.

## M09 — Experiment Engine

**REQUIRED themes**
- Part 14 experimentation/statistics.

## M10 — Decision & Policy Engine

**REQUIRED themes**
- Parts 8, 13, 15 and 16: product/analytics/bot/recommendation.
- Decision ≠ Execution.
- RiskLevel + PolicyDecision.

## M11 — AI Analysis Assistant

**REQUIRED themes**
- Part 17: grounding, LLM workflow, evaluation and state separation.

## M12 — Tool-Using Bot

**REQUIRED themes**
- explicit tool contracts, validation, permissions; MCP where useful.

## M13 — Governed Automation

**REQUIRED themes**
- ActionIntent, RISK 0/1/2, Human Approval, revalidation and audit.

## M14 — Production Bot

**REQUIRED themes**
- Part 19: recovery, observability, security, least privilege, kill switch and cost.

## M15 — Affiliate Intelligence Platform

**REQUIRED themes**
- Part 21 capstone integration and all evidence needed for a governed closed loop.

## Refinement rule

As a mission is authored, replace vague theme-level pulls with the smallest set of explicit canonical lesson IDs that truly gate Mission PASS. Do not add hundreds of speculative mappings in advance.