# Kế hoạch tăng tốc 12 tháng — Build-First capacity envelope

> **Accelerated track** dành cho khoảng **11–12 giờ/tuần**; khuyến nghị **12 giờ/tuần**. Đây là capacity/coverage forecast, không phải default execution sequence. Learner build theo [`../BUILD-FIRST.md`](../BUILD-FIRST.md).

Đọc cùng:

- [Build-First Learning Model](BUILD-FIRST-LEARNING-MODEL.md)
- [Bot Evolution Roadmap](BOT-EVOLUTION-ROADMAP.md)
- [Build-First Calibration](BUILD-FIRST-CALIBRATION.md)
- [Effort Recalibration v2026.09](EFFORT-RECALIBRATION-v2026.09.md)

## 1. Capacity model

Canonical fixed core knowledge coverage vẫn là:

```text
Phần 0 → 19 → 21
```

Current v2026.09 model:

```text
content + lesson evidence + incremental integration ≈ 520h
weekly review ≈ 52h
planned total ≈ 572h
572 / 52 ≈ 11h/tuần
```

Vẫn khuyến nghị **12h/tuần** để có retry/project/debug buffer. Không tự giảm 520h chỉ vì Build-First reuse được artifacts; phải đo M00–M05 trước.

Nếu rolling capacity <11h/tuần trong 4 tuần liên tiếp, chuyển về Standard thay vì giảm PASS criteria.

> Part 20 và Part 22 không nằm trong fixed 12-month core.

## 2. Execution vs coverage

```text
Mission M00 → ... → M15
= product/evidence execution spine

Part/month table
= expected knowledge coverage envelope
```

Go được dùng ngay M00. Formal Part 15 mastery vẫn được coverage sâu ở giai đoạn engineering sau.

## 3. Coverage theo tháng

| Tháng | Knowledge coverage forecast | Planning envelope |
|---:|---|---:|
| 1 | Orientation + Fundamentals + Economics; bootstrap Build-First missions | ~48h |
| 2 | Tracking + Legal + Platform foundations | ~48h |
| 3 | Platform + Niche + Customer | ~48h |
| 4 | Product Intelligence + Content I | ~48h |
| 5 | Content II + Traffic + Funnel | ~48h |
| 6 | Data Engineering + Analytics | ~48h |
| 7 | Experimentation + formal Go Bot Engineering I | ~48h |
| 8 | formal Go Bot Engineering II + Decision/Policy | ~48h |
| 9 | AI Affiliate Bot + governed workflow | ~48h |
| 10 | Advanced Intelligence + Production I | ~48h |
| 11 | Production II + Capstone start | ~48h |
| 12 | Capstone integration + hardening + catch-up | ~48h |

Bảng không phải quota lesson và không cấm Mission pull knowledge sớm hơn khi có prerequisite phù hợp.

## 4. Weekly rhythm Build-First

Gợi ý:

| Hoạt động | Thời lượng |
|---|---:|
| Build / run / debug / operate | 6–8h |
| Required knowledge pulls | 2–3h |
| Evidence / review / calibration | 1–2h |

## 5. Điều kiện dùng Accelerated

Nên dùng khi:

- duy trì gần 12h/tuần;
- vẫn ship/test/operate/evidence đầy đủ;
- vẫn hoàn thành required knowledge pulls và formal lesson PASS khi cần;
- không dùng tốc độ để bỏ security/compliance/approval controls;
- chấp nhận reforecast dựa trên actual mission data.

## 6. Calibration

M00–M05 ghi planned vs actual theo `build/debug/operate/knowledge/retry`. Sau cohort này mới đánh giá Build-First có giảm double-work đủ để thay planning model hay không.

## 7. Nguyên tắc

```text
Timeline = forecast
Mission = execution
Knowledge inventory = mastery coverage
PASS evidence = gate
Actual data > original estimate
```