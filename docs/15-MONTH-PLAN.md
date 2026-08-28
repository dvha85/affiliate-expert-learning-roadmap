# Kế hoạch chuẩn 15 tháng — Build-First capacity envelope

> **Standard track** dành cho khoảng **9 giờ/tuần**. Đây là capacity/coverage forecast, **không phải execution sequence**. Learner execution mặc định đi theo [`../BUILD-FIRST.md`](../BUILD-FIRST.md) và Mission hiện tại.

Đọc cùng:

- [Build-First Learning Model](BUILD-FIRST-LEARNING-MODEL.md)
- [Bot Evolution Roadmap](BOT-EVOLUTION-ROADMAP.md)
- [Build-First Calibration](BUILD-FIRST-CALIBRATION.md)
- [Effort Model](EFFORT-MODEL.md)
- [Effort Recalibration v2026.09](EFFORT-RECALIBRATION-v2026.09.md)

## 1. Capacity model

```text
9 giờ/tuần
× ~65 tuần trong 15 tháng
≈ 585 giờ capacity
```

Canonical fixed core knowledge coverage vẫn là:

```text
Phần 0 → 19 → 21
```

Current v2026.09 planning envelope:

- content + lesson evidence + incremental integration: khoảng **520 giờ**;
- weekly review: khoảng **65 giờ**;
- tổng midpoint requirement: khoảng **585 giờ**.

Không tự giảm 520h vì Build-First có vẻ hiệu quả hơn. Build-First có thể giảm double-work nhờ reuse code/evidence, nhưng cũng thêm debugging/operation. **M00–M05 là calibration cohort** để đo net effect.

Standard 15 tháng gần như không có planning buffer ở midpoint. Nếu rolling actual workload vượt model, kéo dài finish date thay vì giảm PASS criteria; **16 tháng là fallback chấp nhận được**.

> Part 20 bắt đầu khi có revenue signal; Part 22 là continuous mastery sau fixed core.

## 2. Execution vs coverage

```text
BUILD-FIRST MISSION SPINE
= thứ tự learner build/operate bot

MONTHLY PART ENVELOPE
= knowledge coverage forecast
```

Một Mission có thể pull lesson từ nhiều Part trước khi formal mastery của Part đó hoàn tất. Dùng sớm không đồng nghĩa mastery sớm.

## 3. Kế hoạch coverage theo tháng

| Tháng | Knowledge coverage forecast | Planning envelope |
|---:|---|---:|
| 1 | Orientation + Fundamentals + Economics mở đầu; bootstrap M00–M03/M04 khi phù hợp | ~39h |
| 2 | Economics + Tracking & Attribution; tiếp tục early bot iteration | ~39h |
| 3 | Legal/Tax/Compliance + Platform foundations | ~39h |
| 4 | Platform Expert + Niche Intelligence | ~39h |
| 5 | Customer + Product Intelligence I | ~39h |
| 6 | Product Intelligence II + Content I | ~39h |
| 7 | Content II + Traffic + Funnel mở đầu | ~39h |
| 8 | Funnel + Data Engineering + Analytics mở đầu | ~39h |
| 9 | Analytics + Experimentation + formal Bot Engineering mở đầu | ~39h |
| 10 | Formal Go-first Affiliate Bot Engineering mastery | ~39h |
| 11 | Decision/Policy + AI foundations | ~39h |
| 12 | AI Affiliate Bot + Advanced Intelligence mở đầu | ~39h |
| 13 | Advanced Intelligence + Production foundations | ~39h |
| 14 | Production/Security/Governance + Capstone start | ~39h |
| 15 | Capstone integration + hardening + retry/catch-up | ~39h |

Bảng không có nghĩa learner phải chờ tháng 10 mới code Go. Go được **dùng từ M00**; tháng 9–10 là formal mastery coverage.

## 4. Weekly rhythm Build-First

Heuristic, không phải quota cứng:

| Hoạt động | Tỷ lệ/giờ gợi ý |
|---|---:|
| Build / run / debug / operate | 4.5–6h |
| Required knowledge pulls | 1.5–2.5h |
| Evidence / review / calibration | 1–1.5h |

Compliance/research work được tính vào bucket phù hợp với Mission đang chạy.

## 5. Monthly gate

Review:

- Mission PASS/RETRY/BLOCKED;
- Bot Version đã ship;
- lesson PASS/RETRY thực tế;
- actual hours vs mission estimates;
- build/debug/operate/knowledge/retry split;
- evidence reused giữa Mission/Lesson/Project;
- active operating loops;
- blockers và forecast tháng sau.

## 6. Recalibration rule

Không sửa global workload từ vài ngày đầu. Sau M00–M05, dùng [`BUILD-FIRST-CALIBRATION.md`](BUILD-FIRST-CALIBRATION.md) để xem actual median, nguồn overrun và reuse benefit trước khi re-estimate remaining scope.

## 7. Nguyên tắc

```text
Timeline = forecast
Mission = execution unit
Knowledge coverage = mastery inventory
PASS evidence = gate
Actual data > planning assumption
```

Không dùng “hoàn thành 15 tháng” làm định nghĩa Expert.