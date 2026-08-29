# Effort Recalibration — v2026.09 Go-first hardening (superseded)

> **Historical planning record.** Tài liệu này áp dụng cho inventory cũ. Active planning nằm tại [EFFORT-MODEL.md](EFFORT-MODEL.md); không dùng baseline bên dưới để ước lượng Core hiện hành.

> Recalibrates planning after the Go-first Bot Engineering migration without changing 23/89/671/14.

## 1. Why recalibrate

The original baseline predated the expanded Go/durable-workflow/tool-security/approval scope. Most new concepts were absorbed into existing lesson IDs, so workload should increase only where the PASS artifact/testing burden materially increased.

## 2. Impacted Parts

| Part | Previous midpoint | v2026.09 planning midpoint | Delta | Main reason |
|---:|---:|---:|---:|---|
| 0 | 7.6h | 8.0h | +0.4h | Go-first/autonomy orientation in 0.2 |
| 15 | 38.2h | 40.5h | +2.3h | Go/concurrency + durable workflow + approval-aware bot design |
| 16 | 22.4h | 23.5h | +1.1h | deterministic policy/risk boundary |
| 17 | 32.2h | 34.5h | +2.3h | tool engineering/MCP, state separation, agent eval/HITL |
| 19 | 32.0h | 34.5h | +2.5h | agent observability/security/governed automation |
| 21 | 20.1h | 22.0h | +1.9h | durable/governed capstone integration |
| **Total delta** |  |  | **+10.5h** |  |

All other Part baseline midpoints remain unchanged until actual learner data justifies recalibration.

## 3. Updated capacity envelope

Previous lesson midpoint: approximately **478.5h**.  
Go-first hardening adjustment: **+10.5h**.  
Updated lesson midpoint: approximately **489h**.

Retain approximately **30–31h** incremental XL integration/hardening budget after anti-double-counting.

```text
content + lesson evidence + incremental integration
≈ 520h
```

### Standard 15-month

```text
~65 weeks × 9h/week ≈ 585h capacity
~520h content/integration
~65h weekly review
≈ 585h planned requirement
```

Interpretation: **15 months at 9h/week is feasible but now has effectively zero planning buffer at midpoint**. It must be treated as a forecast, not a promise.

Operational rule:

- keep 9h/week as the default capacity;
- reuse lesson artifacts in projects to avoid double-counting;
- reforecast monthly;
- if rolling actual workload exceeds the model, extend the finish date instead of reducing PASS criteria.

A 16-month finish is an acceptable fallback when retries/real-world blockers accumulate.

### Accelerated 12-month

```text
~52 weeks
~520h content/integration
~52h weekly review
≈ 572h
≈ 11h/week average
```

Keep the recommendation at **~12h/week** to provide retry/project buffer.

## 4. What was not added

Do not create workload inflation by counting each new engineering term as a new lesson. MCP, durable workflow, prompt injection, policy/risk and approval are integrated into existing lesson/project scope.

Do not double-count:

```text
lesson implementation artifact
+
project reuse of the same artifact
```

Project effort only adds integration, validation, failure testing, hardening, demo and retrospective work not already counted.

## 5. Calibration rule

After 8–12 completed lessons of a comparable class, prefer actual median time over planning midpoint. Re-estimate the remaining similar lessons if actual time repeatedly exceeds the expected range.

## 6. Timeline implication

No Part/month labels are renumbered in v2026.09. Standard M1–M15 and Accelerated M1–M12 remain **planning envelopes**. The finish date may move if PASS evidence requires more time.
