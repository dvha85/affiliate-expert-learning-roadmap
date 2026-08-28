# Roadmap tổng — Knowledge Inventory

> **Vai trò từ Build-First v1:** file này là canonical normalized **knowledge inventory**, không còn là default learner execution sequence. Đường học mặc định nằm ở [`BUILD-FIRST.md`](BUILD-FIRST.md). Mission có thể pull lesson từ nhiều Part theo đúng prerequisite cần thiết.

> Checkbox bài học nằm trong file từng phần. Đây là nguồn trạng thái learner PASS duy nhất để tránh tick trùng.

Tổng cộng: **23 phần · 89 chương · 671 bài học**.

> **Planning note:** 671 bài không có trọng lượng bằng nhau. Workload phải được lập theo [Effort Model S/M/L/XL](docs/EFFORT-MODEL.md), dựa trên **thời gian để PASS**, không dựa riêng vào số checkbox.

## Timeline chính

- **Standard:** [15 tháng](docs/15-MONTH-PLAN.md) ở khoảng **9 giờ/tuần** — planning envelope.
- **Accelerated:** [12 tháng](docs/12-MONTH-PLAN.md) ở khoảng **11–12 giờ/tuần**, khuyến nghị 12 giờ/tuần.
- Fixed core knowledge spine: **Phần 0 → 19 → 21**.
- Phần 20 bắt đầu khi có tín hiệu doanh thu; Phần 22 là Continuous Mastery sau core.

Bảng dưới là **curriculum index**. Build-First Mission system quyết định learner build gì tiếp theo; bảng này xác định knowledge nào tồn tại và trạng thái PASS của learner.

| Phần | Trọng tâm | Chương | Bài | Trạng thái |
|---|---|---:|---:|---|
| [Phần 0](roadmap/part-00.md) | ORIENTATION & AFFILIATE LAB | 0 | 12 | ⬜ |
| [Phần 1](roadmap/part-01.md) | AFFILIATE FUNDAMENTALS | 1–3 | 34 | ⬜ |
| [Phần 2](roadmap/part-02.md) | AFFILIATE ECONOMICS | 4–6 | 34 | ⬜ |
| [Phần 3](roadmap/part-03.md) | TRACKING & ATTRIBUTION | 7–9 | 33 | ⬜ |
| [Phần 4](roadmap/part-04.md) | VIETNAM LEGAL, TAX & COMPLIANCE | 10–12 | 28 | ⬜ |
| [Phần 5](roadmap/part-05.md) | AFFILIATE PLATFORM EXPERT | 13–16 | 50 | ⬜ |
| [Phần 6](roadmap/part-06.md) | MARKET & NICHE INTELLIGENCE | 17–19 | 26 | ⬜ |
| [Phần 7](roadmap/part-07.md) | CUSTOMER INTELLIGENCE | 20–22 | 21 | ⬜ |
| [Phần 8](roadmap/part-08.md) | PRODUCT INTELLIGENCE | 23–27 | 40 | ⬜ |
| [Phần 9](roadmap/part-09.md) | CONTENT & CONSUMER PSYCHOLOGY | 28–32 | 44 | ⬜ |
| [Phần 10](roadmap/part-10.md) | TRAFFIC & DISTRIBUTION | 33–35 | 24 | ⬜ |
| [Phần 11](roadmap/part-11.md) | FUNNEL & CONVERSION | 36–37 | 14 | ⬜ |
| [Phần 12](roadmap/part-12.md) | DATA ENGINEERING FOR AFFILIATE | 38–41 | 23 | ⬜ |
| [Phần 13](roadmap/part-13.md) | AFFILIATE ANALYTICS | 42–45 | 23 | ⬜ |
| [Phần 14](roadmap/part-14.md) | EXPERIMENTATION & STATISTICS | 46–49 | 28 | ⬜ |
| [Phần 15](roadmap/part-15.md) | AFFILIATE BOT ENGINEERING | 50–56 | 42 | ⬜ |
| [Phần 16](roadmap/part-16.md) | DECISION & RECOMMENDATION ENGINE | 57–60 | 23 | ⬜ |
| [Phần 17](roadmap/part-17.md) | AI AFFILIATE BOT | 61–66 | 36 | ⬜ |
| [Phần 18](roadmap/part-18.md) | ADVANCED AFFILIATE INTELLIGENCE | 67–72 | 35 | ⬜ |
| [Phần 19](roadmap/part-19.md) | PRODUCTION, SECURITY & AUTOMATION | 73–77 | 32 | ⬜ |
| [Phần 20](roadmap/part-20.md) | AFFILIATE BUSINESS & SCALE | 78–82 | 32 | ⬜ |
| [Phần 21](roadmap/part-21.md) | CAPSTONE | 83–84 | 17 | ⬜ |
| [Phần 22](roadmap/part-22.md) | CONTINUOUS MASTERY | 85–88 | 20 | ⬜ |

## Authoring status vs learner status

```text
Authoring: planned → draft → ready
Learner:   chưa PASS → PASS / RETRY
```

- `planned` scaffold có thể tồn tại trong `lessons/` nhưng chưa được link từ part roadmap;
- `draft` hoặc `ready` phải được link từ part roadmap;
- link không có nghĩa learner đã PASS;
- checkbox `[x]` chỉ dùng sau khi đủ PASS criteria.

Bài 0.1 và 0.2 là authored references; learner status vẫn `[ ]` cho tới khi evidence thực tế đạt PASS.

## Build-First execution

Knowledge spine vẫn mô tả prerequisite/mastery coverage, nhưng learner execution mặc định là:

```text
ONE current Mission
+
small working Bot slice
+
required/on-demand Knowledge Pulls
+
active operating loops
+
ALL within weekly capacity
+
PASS evidence before mastery
```

Go có thể được **dùng** từ Mission đầu tiên; Part 15 vẫn là formal Bot Engineering mastery scope.

Các execution loops và governed action model nằm trong [docs/EXECUTION-MODEL.md](docs/EXECUTION-MODEL.md).

## Quy ước trạng thái learner

- ⬜ Chưa PASS
- 🟨 Đang học
- 🟦 Chờ review / chưa đủ evidence
- ✅ PASS
- ⛔ Blocked

## Quy ước effort

- **S — Small:** 15–30 phút để PASS.
- **M — Medium:** 45–75 phút để PASS.
- **L — Large:** 1.5–3 giờ để PASS.
- **XL — Integration Gate:** LAB/PROJECT/PASS Gate, thường nhiều giờ hoặc nhiều buổi.

Xem [docs/EFFORT-MODEL.md](docs/EFFORT-MODEL.md).

## Authority rule

```text
BUILD-FIRST tells learner WHAT TO BUILD NEXT.
ROADMAP tells the system WHAT KNOWLEDGE EXISTS and WHAT HAS PASSED.
```

Build-first changes sequencing, not canonical IDs, project inventory or learner evidence history.