# Kế hoạch chuẩn 15 tháng

> **Standard track** dành cho nhịp khoảng **9 giờ/tuần**. Đây là lộ trình mặc định của repo sau Issue #2.

Kế hoạch được xây từ [Effort Model S/M/L/XL](EFFORT-MODEL.md), không chia đều 671 checkbox theo tháng.

## 1. Capacity model

Giả định planning:

```text
9 giờ/tuần
× ~65 tuần trong 15 tháng
≈ 585 giờ capacity
```

Core curriculum cố định dùng trong timeline này:

```text
Phần 0 → 19 → 21
```

Baseline v0.1:

- lesson + integration workload: khoảng **509 giờ**;
- weekly review: khoảng **65 giờ**;
- còn khoảng **10–12 giờ buffer** cho retry/catch-up ở baseline midpoint.

Đây là forecast, không phải deadline cứng. Nếu lesson thực tế vượt estimate, ưu tiên PASS evidence và reforecast timeline.

> **Không tính vào fixed 15-month core:** Phần 20 — Business & Scale bắt đầu khi có tín hiệu doanh thu; Phần 22 — Continuous Mastery chạy liên tục sau core.

## 2. Kế hoạch theo tháng

`Content + integration` là planning envelope ở midpoint; sẽ được hiệu chỉnh khi Step 5 gán effort cho từng lesson thật.

| Tháng | Trọng tâm | Phần/Chương dự kiến | Content + integration | Review/buffer | Expected total |
|---:|---|---|---:|---:|---:|
| 1 | Orientation + Affiliate Fundamentals + Economics mở đầu | Phần 0–1, bắt đầu Phần 2 | ~34h | ~4–5h | **~38–39h** |
| 2 | Economics + Tracking & Attribution | Hoàn tất Phần 2–3 | ~35h | ~4h | **~39h** |
| 3 | Legal/Tax/Compliance + Platform foundations | Phần 4, đầu Phần 5 | ~34h | ~4–5h | **~38–39h** |
| 4 | Platform Expert + Niche Intelligence | Hoàn tất Phần 5–6 | ~34h | ~4–5h | **~38–39h** |
| 5 | Customer Intelligence + Product Intelligence I | Phần 7, Chương 23–25 | ~34h | ~4–5h | **~38–39h** |
| 6 | Product Intelligence II + Content/Psychology I | Hoàn tất Phần 8, bắt đầu Phần 9 | ~35h | ~4h | **~39h** |
| 7 | Content/Psychology II + Traffic + Funnel mở đầu | Hoàn tất Phần 9, Phần 10, bắt đầu Phần 11 | ~34h | ~4–5h | **~38–39h** |
| 8 | Funnel/Conversion + Data Engineering + Analytics mở đầu | Hoàn tất Phần 11–12, bắt đầu Phần 13 | ~34h | ~4–5h | **~38–39h** |
| 9 | Analytics + Experimentation + Bot Architecture mở đầu | Hoàn tất Phần 13–14, đầu Phần 15 | ~34h | ~4–5h | **~38–39h** |
| 10 | Affiliate Bot Engineering | Phần 15 | ~35h | ~4h | **~39h** |
| 11 | Decision/Recommendation + AI foundations | Phần 16, đầu Phần 17 | ~34h | ~4–5h | **~38–39h** |
| 12 | AI Affiliate Bot + Advanced Intelligence mở đầu | Hoàn tất Phần 17, đầu Phần 18 | ~34h | ~4–5h | **~38–39h** |
| 13 | Time-series/ML + Production foundations | Hoàn tất Phần 18, đầu Phần 19 | ~34h | ~4–5h | **~38–39h** |
| 14 | Production/Security/Automation + Capstone start | Hoàn tất Phần 19, bắt đầu Phần 21 | ~34h | ~4–5h | **~38–39h** |
| 15 | Capstone integration + hardening + retry/catch-up | Hoàn tất Phần 21 | ~31h | ~7–8h | **~38–39h** |

Tổng content + integration envelope: khoảng **510 giờ**, khớp baseline khoảng 509 giờ ở mức làm tròn.

## 3. Vì sao tháng 1–2 được giảm tải

Lịch cũ dồn:

```text
Tháng 1: Phần 0–3 = 113 lesson
Tháng 2: Phần 4–6 = 104 lesson
```

Standard plan không còn yêu cầu hoàn tất 217 lesson trong 2 tháng đầu.

Thay vào đó:

- Tháng 1 tập trung orientation + fundamentals và chỉ bắt đầu economics.
- Tháng 2 hoàn thiện economics/tracking ở pace dựa trên effort.
- Legal/platform/niche được đẩy sang tháng 3–4.

Mục tiêu là cho người mới đủ thời gian để thực hiện cả quiz, practice, explain-back và artifact thay vì chỉ đọc checkbox.

## 4. Nhịp tuần 9 giờ

Khung mặc định:

| Hoạt động | Thời lượng gợi ý |
|---|---:|
| Learn + case | 2h |
| Research thực tế | 1h |
| Affiliate practice | 2h |
| Coding/Data/Artifact | 3h |
| Weekly review | 1h |

Không cần giữ đúng tỷ lệ từng tuần. Khi ở phần engineering, Coding/Data có thể tăng; khi ở content/platform/legal, research/practice có thể tăng.

## 5. Monthly gate

Không chuyển tháng chỉ vì hết lịch nếu thiếu evidence quan trọng.

Cuối mỗi tháng review:

- lesson nào PASS / RETRY;
- actual hours so với effort estimate;
- project/lab integration còn thiếu;
- blocker;
- forecast tháng kế tiếp.

Nếu actual workload cao hơn baseline, ưu tiên dời scope sang tháng tiếp theo thay vì giảm PASS criteria.

## 6. Prerequisite ở mức timeline

Ở Step 2 chỉ chốt dependency lớn:

```text
Foundation/Economics/Tracking
→ Market/Customer/Product
→ Content/Traffic/Funnel
→ Data/Analytics/Experiments
→ Bot/Recommendation/AI
→ Advanced Intelligence/Production
→ Capstone
```

Cách kết hợp knowledge tuần tự với execution track song song sẽ được chuẩn hóa chi tiết ở **Issue #3 — EXECUTION-MODEL**.

## 7. Standard vs Accelerated

Chọn Standard nếu capacity thực tế khoảng **9h/tuần**.

Chỉ chọn [12-month Accelerated](12-MONTH-PLAN.md) nếu có thể duy trì khoảng **11–12h/tuần**, khuyến nghị **12h/tuần** để có buffer.

Không dùng thời gian hoàn thành làm định nghĩa Expert. PASS evidence và năng lực thực tế vẫn là tiêu chuẩn.