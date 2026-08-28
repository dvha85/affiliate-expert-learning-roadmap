# Bot Evolution Roadmap — M00 to M15

This roadmap defines the **product/evidence spine** of Build-First Learning Architecture v1. It does not replace the canonical 23/89/671 knowledge inventory or 14 main Projects.

| Mission | Bot version | Ship target | Main knowledge themes |
|---|---:|---|---|
| M00 | v0.0 | Bot boots and produces visible output | Affiliate/Bot orientation, minimal Go |
| M01 | v0.1 | Product ingest + validation | Product basics, structs, JSON, errors |
| M02 | v0.2 | Product persistence + snapshots/history | data model, SQL, repository, history |
| M03 | v0.3 | First product ranking + before/after scoring | economics, EV, product intelligence |
| M04 | v0.4 | Product watcher detects change | scheduler, context, delta, concurrency |
| M05 | v0.5 | Reliable alerts | rules, timeout, retry, idempotency |
| M06 | v1.0 | Product Intelligence v1 | market, customer, product, economics, risk |
| M07 | v2.0 | Content Intelligence | content, CTR/CVR, psychology, funnel signals |
| M08 | v3.0 | Revenue & Attribution Intelligence | tracking, orders, validation, commission, reconciliation |
| M09 | v4.0 | Experiment Engine | hypothesis, statistics, experiment logging |
| M10 | v5.0 | Decision & Policy Engine | score/rank/recommendation, confidence, RiskLevel, PolicyDecision |
| M11 | v6.0 | AI Analysis Assistant | grounded LLM, evaluation, state separation |
| M12 | v7.0 | Tool-Using Bot | explicit tool contracts, MCP where useful, tool validation |
| M13 | v8.0 | Governed Automation | ActionIntent, RISK 0/1/2, Human Approval, audit |
| M14 | v9.0 | Production Bot | recovery, observability, security, kill switch, cost |
| M15 | v10.0 | Affiliate Intelligence Platform | end-to-end governed feedback loop |

## Mission dependencies

```text
M00 → M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
    → M09 → M10 → M11 → M12 → M13 → M14 → M15
```

The sequence is intentionally simple for a single learner. Later versions may introduce optional side missions without changing the M00–M15 main spine.

## Pedagogy pattern

M03 is the reference Build-First teaching pattern:

```text
Build naive ranking
→ observe that commission-rate-only ranking is weak
→ pull economics/product knowledge
→ improve formula
→ compare before/after
→ explain why ranking changed
```

## Canonical Project contributions

Mission evidence can contribute to canonical projects without creating new Project IDs:

- M02 + M08 → Project 7 Affiliate Data Warehouse
- M04 + M05 → Project 10 Product Tracker Bot
- M06 → Project 4 Product Intelligence
- M07 → Project 5 Real Content Portfolio
- M09 → Project 9 Experiment System
- M10 → Project 11 Opportunity Engine
- M11 + M12 → Project 12 AI Content Assistant
- M14 → Project 13 Production Affiliate Bot
- M15 → Project 14 Affiliate Intelligence Platform

Mission contribution is reusable evidence, not automatic Project PASS.

## Safety progression

```text
M00–M09: mostly internal/read-only/sample side effects
M10: deterministic decision/policy boundary
M11–M12: AI/tool capability with validation
M13: governed external action model
M14–M15: production reliability/security/governance
```

Do not bring consequential auto-execution forward merely to make an early mission feel more advanced.