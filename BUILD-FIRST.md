# Build-First Learning Roadmap

> **START HERE.** Đây là đường học mặc định của curriculum v2026.09.

## Mental model

```text
Build
→ Run
→ Observe
→ Pull Knowledge just-in-time
→ Improve
→ Test
→ Operate
→ Save Evidence
→ Ship next Bot Version
```

`ROADMAP.md` và 23 Part files vẫn là **canonical knowledge inventory** gồm 23 Parts / 89 Chapters / 671 lessons. Build-First không thay, renumber hay xoá lesson; nó thay **thứ tự thực thi việc học**.

## Bốn loại đơn vị

- **Lesson** — một đơn vị kiến thức trong canonical curriculum.
- **Mission** — một đơn vị build/operate có ship target cụ thể.
- **Project** — một trong 14 canonical integration milestones.
- **Bot Version** — trạng thái sản phẩm Affiliate Intelligence Bot sau mỗi mission.

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

## Quy tắc học mặc định

1. Mở mission hiện tại trong `PROGRESS.md`.
2. Build phần nhỏ nhất chạy được trước.
3. Chạy và quan sát failure/gap.
4. Pull đúng lesson cần thiết từ knowledge map.
5. Áp dụng kiến thức vào bot.
6. Test cả happy path và failure case phù hợp scope.
7. Chạy/operate đủ để quan sát output.
8. Lưu evidence và explain-back.
9. Chỉ PASS mission khi ship target thực sự đạt.

## Go từ ngày đầu, mastery đến sau

Build-First dùng Go ngay từ mission bootstrap. Điều đó **không** có nghĩa learner đã mastery Part 15.

```text
USE GO EARLY
≠
CLAIM GO MASTERY EARLY
```

Go concepts được pull đúng lúc: package/function/struct trước; JSON/error/validation khi ingest; database khi persistence; context/concurrency khi scheduler; retry/idempotency khi reliability.

## Safety / autonomy

Build-first không bỏ các boundary hiện có:

```text
Deterministic logic before LLM autonomy
Decision ≠ Execution
Model output = untrusted input
RISK 0 → auto
RISK 1 → auto + audit
RISK 2 → human approval
```

## Knowledge mastery vẫn tồn tại

Lesson PASS vẫn theo `docs/PASS-CRITERIA.md`. Mission PASS sẽ được định nghĩa riêng ở PR2. Một mission hoàn thành **không được tự động tick lesson PASS**.

## Tiếp theo

Mission system, Bot Evolution M00–M15 và first working Go bot sẽ được bổ sung tuần tự theo Issue #30. Trong thời gian migration, learner status hiện tại được giữ nguyên.