# Kế hoạch chuẩn 15 tháng

> **Standard track** dành cho nhịp khoảng **9 giờ/tuần**. Đây là lộ trình mặc định của repo.

Đọc cùng:

- [Effort Model](EFFORT-MODEL.md)
- [Effort Recalibration v2026.09](EFFORT-RECALIBRATION-v2026.09.md)
- [Hybrid Execution Model](EXECUTION-MODEL.md)

## 1. Capacity model

```text
9 giờ/tuần
× ~65 tuần trong 15 tháng
≈ 585 giờ capacity
```

Core curriculum cố định:

```text
Phần 0 → 19 → 21
```

Recalibrated v2026.09 planning envelope:

- content + lesson evidence + incremental integration: khoảng **520 giờ**;
- weekly review: khoảng **65 giờ**;
- tổng midpoint requirement: khoảng **585 giờ**.

Khác baseline cũ, Standard 15 tháng giờ gần như **không còn planning buffer ở midpoint**. Đây vẫn là forecast hợp lý cho 9h/tuần nếu artifact được reuse đúng và không double-count project work, nhưng không phải deadline cứng.

Nếu rolling actual workload vượt model, ưu tiên kéo dài finish date thay vì giảm PASS criteria. **16 tháng là fallback chấp nhận được**, không phải failure.

> Phần 20 — Business & Scale bắt đầu khi có tín hiệu doanh thu; Phần 22 — Continuous Mastery không nằm trong fixed 15-month core.

## 2. Kế hoạch theo tháng

| Tháng | Trọng tâm | Phần/Chương dự kiến | Planning envelope |
|---:|---|---|---:|
| 1 | Orientation + Fundamentals + Economics mở đầu | Phần 0–1, bắt đầu Phần 2 | ~39h |
| 2 | Economics + Tracking & Attribution | Hoàn tất Phần 2–3 | ~39h |
| 3 | Legal/Tax/Compliance + Platform foundations | Phần 4, đầu Phần 5 | ~39h |
| 4 | Platform Expert + Niche Intelligence | Hoàn tất Phần 5–6 | ~39h |
| 5 | Customer + Product Intelligence I | Phần 7, Chương 23–25 | ~39h |
| 6 | Product Intelligence II + Content I | Hoàn tất Phần 8, bắt đầu Phần 9 | ~39h |
| 7 | Content II + Traffic + Funnel mở đầu | Hoàn tất Phần 9–10, bắt đầu 11 | ~39h |
| 8 | Funnel + Data Engineering + Analytics mở đầu | Hoàn tất Phần 11–12, bắt đầu 13 | ~39h |
| 9 | Analytics + Experimentation + Bot Architecture mở đầu | Hoàn tất 13–14, đầu 15 | ~39h |
| 10 | Go-first Affiliate Bot Engineering | Phần 15 | ~39h |
| 11 | Decision/Policy + AI foundations | Phần 16, đầu 17 | ~39h |
| 12 | AI Affiliate Bot + Advanced Intelligence mở đầu | Hoàn tất 17, đầu 18 | ~39h |
| 13 | Advanced Intelligence + Production foundations | Hoàn tất 18, đầu 19 | ~39h |
| 14 | Production/Security/Governance + Capstone start | Hoàn tất 19, bắt đầu 21 | ~39h |
| 15 | Capstone integration + hardening + retry/catch-up | Hoàn tất 21 | ~39h |

Bảng là **capacity envelope**, không phải quota checkbox.

## 3. Hybrid execution

Khi loop đã mở, nó tiếp tục chạy trong cùng quỹ 9h/tuần:

```text
50–70%: primary knowledge/current Part
30–50%: active execution loops + evidence + review
```

Đặc biệt từ Part 15 trở đi:

```text
Go Bot
→ Decision/Policy
→ AI Tools
→ Governed Action/Approval
→ Production
```

là một progression liên tục; không coi từng Part là project tách biệt.

## 4. Weekly rhythm gợi ý

| Hoạt động | Thời lượng |
|---|---:|
| Learn + case | 2h |
| Research thực tế | 1h |
| Affiliate practice | 2h |
| Coding/Data/Artifact | 3h |
| Weekly review | 1h |

Engineering-heavy weeks có thể dồn nhiều hơn vào coding/artifact nhưng tổng capacity vẫn giữ.

## 5. Monthly gate

Cuối tháng review:

- lesson PASS/RETRY;
- actual hours vs estimate;
- active execution loops;
- project/lab integration còn thiếu;
- blocker;
- forecast tháng sau.

Nếu actual workload cao hơn baseline, dời scope thay vì giảm evidence quality.

## 6. Nguyên tắc

```text
Timeline = forecast
PASS evidence = gate
Actual data > planning assumption
```

Không dùng “hoàn thành 15 tháng” làm định nghĩa Expert.
