# Mô hình khối lượng học v2 — Reality-First

Curriculum v2 không dùng nominal hours của v1 để hứa hẹn lịch. Những estimate
M00→M03 ~48h thuộc baseline v1 và không mô tả thứ tự v2.

## Hypothesis cần pilot

Mục tiêu thiết kế là đưa một beginner tới **E2 human-only market action** ở M00
sớm, với target `≤ 8` focused hours khi account/channel/disclosure path đã sẵn
sàng. Đây là hypothesis, không phải PASS criterion hay SLA. Setup, platform
review, account eligibility và outcome window được ghi riêng.

| Giai đoạn v2 | Cần đo trong pilot |
|---|---|
| O00 → M00 | setup friction, time-to-first-E1/E2, blocker, publish/review safety |
| M01 + M02 | snapshot/measurement time và baseline implementation time riêng |
| M03–M05 | history/AI/evaluation time, waiting time và quality of improvement |
| M06–M11 | reliability, governance, recovery và production overhead |

## Actuals cần lưu

```text
focused_setup
focused_attempt/build
focused_debug
focused_knowledge_pull
focused_review
external_waiting
blocked_external_reason
evidence level achieved
```

Không double-count waiting như focused work, và không kéo dài market action chỉ
để “học đủ lý thuyết”. Forecast chỉ được recalibrate sau pilot evidence; ưu
tiên median/dispersion theo cohort thay vì một learner duy nhất.
