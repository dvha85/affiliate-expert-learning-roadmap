# Build-First Calibration

> M00–M05 là calibration cohort đầu tiên. Không giảm/tăng toàn bộ workload model chỉ từ cảm giác rằng Build-First nhanh hơn hay chậm hơn.

## Why

Current v2026.09 planning baseline is approximately:

```text
lesson/evidence midpoint ≈ 489h
incremental integration ≈ 30–31h
total planning envelope ≈ 520h
```

Build-First may reduce double work because code can simultaneously serve as mission evidence, lesson practice evidence and later Project contribution. It may also add real debugging/operation time. Only actual learner data should determine the net effect.

## Per-Mission record

For M00–M05 record:

| Field | Meaning |
|---|---|
| `planned_hours` | mission estimate before execution |
| `actual_build_hours` | coding/configuration/data work |
| `actual_debug_hours` | diagnosing/fixing failures |
| `actual_operate_hours` | running/observing the bot |
| `actual_knowledge_hours` | required knowledge pull and explain-back |
| `actual_retry_hours` | redo/review after failed PASS evidence |
| `result` | PASS / RETRY / BLOCKED / IN_PROGRESS |

Total actual:

```text
build + debug + operate + knowledge + retry
```

Do not double-count the same time in multiple buckets.

## Reforecast rule

After M00–M05:

1. calculate median actual vs planned ratio;
2. identify whether overruns came from learning, engineering setup, debugging or operation;
3. compare mission evidence reused by lessons/projects vs duplicate work avoided;
4. update only the remaining comparable scope;
5. preserve PASS criteria and extend timeline when evidence requires it.

## Timeline decision

Standard remains ~9h/week and Accelerated remains ~11–12h/week until evidence supports a revision.

```text
DATA > OPINION
```

Calendar dates are forecasts; evidence is the gate.