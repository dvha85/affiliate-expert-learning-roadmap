# Kế hoạch tăng tốc 12 tháng

> **Accelerated track** — không còn là lộ trình mặc định cho nhịp 9 giờ/tuần.

Dùng track này khi có thể duy trì khoảng **11–12 giờ/tuần**; khuyến nghị **12 giờ/tuần** để có buffer cho retry, project integration và tuần bận.

Nếu capacity thực tế khoảng 9 giờ/tuần, dùng [15-month Standard Plan](15-MONTH-PLAN.md).

Track này phải đọc cùng [Hybrid Execution Model](EXECUTION-MODEL.md): bảng tháng mô tả primary knowledge focus, còn execution loops đã mở khóa tiếp tục chạy song song trong cùng weekly capacity.

## 1. Capacity model

Baseline core curriculum cố định:

```text
Phần 0 → 19 → 21
```

Theo Effort Model v0.1:

- lesson + XL integration midpoint: khoảng **509 giờ**;
- 12 tháng ≈ 52 tuần;
- weekly review khoảng 1 giờ/tuần ≈ **52 giờ**.

Tổng planning requirement khoảng:

```text
509 + 52 = 561 giờ
561 / 52 ≈ 10.8 giờ/tuần
```

Vì estimate có uncertainty, track này khuyến nghị **12h/tuần** thay vì lập lịch sát 10.8h.

> Phần 20 — Business & Scale và Phần 22 — Continuous Mastery không nằm trong fixed 12-month core.

## 2. Kế hoạch theo tháng

| Tháng | Trọng tâm | Phần/Chương dự kiến | Content + integration | Review/buffer | Expected total |
|---:|---|---|---:|---:|---:|
| 1 | Orientation, Fundamentals, Economics | Phần 0–2 | ~42h | ~5–7h | **~47–49h** |
| 2 | Tracking, Legal, Platform foundations | Phần 3–5 (một phần) | ~43h | ~5–7h | **~48–50h** |
| 3 | Platform + Niche + Customer | Hoàn tất Phần 5–7 | ~42h | ~5–7h | **~47–49h** |
| 4 | Product Intelligence + Content/Psychology I | Phần 8, đầu Phần 9 | ~43h | ~5–7h | **~48–50h** |
| 5 | Content/Psychology II + Traffic + Funnel | Hoàn tất Phần 9–11 | ~42h | ~5–7h | **~47–49h** |
| 6 | Data Engineering + Analytics | Phần 12–13 | ~43h | ~5–7h | **~48–50h** |
| 7 | Experimentation + Bot Engineering I | Phần 14, đầu Phần 15 | ~42h | ~5–7h | **~47–49h** |
| 8 | Bot Engineering II + Decision Engine | Hoàn tất Phần 15–16 | ~43h | ~5–7h | **~48–50h** |
| 9 | AI Affiliate Bot | Phần 17 | ~42h | ~5–7h | **~47–49h** |
| 10 | Advanced Intelligence + Production I | Phần 18, đầu Phần 19 | ~43h | ~5–7h | **~48–50h** |
| 11 | Production II + Capstone start | Hoàn tất Phần 19, đầu Phần 21 | ~42h | ~5–7h | **~47–49h** |
| 12 | Capstone integration + hardening + catch-up | Hoàn tất Phần 21 | ~42h | ~6–8h | **~48–50h** |

Tổng content + integration envelope khoảng **509 giờ**.

## 3. Hybrid execution trong accelerated track

Accelerated không có nghĩa học nhiều Part độc lập cùng lúc. Vẫn giữ:

```text
ONE primary knowledge focus
+
ONLY unlocked execution loops
+
ALL within ~12h/tuần
```

Ví dụ:

```text
Month 4: Part 9 mở Content Production
Month 5: thêm Traffic + Funnel → Content vẫn chạy
Month 7: Part 14 mở Formal Experiment loop
Month 7–8: Bot loop mở ở Part 15, dùng data/artifact tích lũy trước đó
```

Các loop không cộng thêm ngoài capacity; chúng chiếm phần practice/data/evidence trong envelope tháng.

## 4. Điều kiện dùng accelerated track

Nên chọn track này khi:

- có thể duy trì gần 12h/tuần trong phần lớn năm;
- chấp nhận một số tháng 48–50h;
- có nền tảng engineering/data đủ tốt để các lesson kỹ thuật không thường xuyên vượt estimate;
- vẫn giữ đủ 5 PASS criteria;
- có khả năng duy trì execution loops đã unlock mà không làm primary knowledge bị phân tán.

Không nên chọn track này nếu để kịp lịch phải:

- bỏ practice;
- bỏ explain-back;
- giảm quiz/evidence;
- tick bài chỉ vì đã đọc;
- bỏ project integration;
- chạy quá nhiều execution loop nhưng không có learning focus.

Khi đó phải chuyển về Standard 15 tháng.

## 5. Monthly review và reforecast

Mỗi tháng kiểm tra:

- actual hours;
- số lesson PASS/RETRY;
- active execution loops;
- XL gate còn tồn;
- rolling 4-week capacity;
- backlog spillover.

Nếu rolling capacity < 11h/tuần trong 4 tuần liên tiếp, cân nhắc chuyển sang Standard Plan thay vì tăng áp lực bằng cách giảm chất lượng học.

## 6. Nhịp tuần gợi ý 12 giờ

| Hoạt động | Thời lượng gợi ý |
|---|---:|
| Learn + case | 2.5h |
| Research thực tế | 1.5h |
| Affiliate practice | 2.5h |
| Coding/Data/Artifact | 4.5h |
| Weekly review | 1h |

Khi execution loops mở, có thể dùng heuristic:

```text
50–70%: current knowledge / primary Part
30–50%: execution loops + evidence + review
```

Tỷ lệ thay đổi theo Part; đây chỉ là capacity envelope.

## 7. Nguyên tắc

```text
Timeline là forecast.
Execution loops là hoạt động duy trì.
PASS evidence là gate.
```

Không coi hoàn thành 12 tháng là bằng chứng đạt Expert.