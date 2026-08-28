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

## Bot Evolution spine

| Mission | Bot version | Ship target |
|---|---:|---|
| M00 | v0.0 | Bot boots |
| M01 | v0.1 | Product ingest |
| M02 | v0.2 | Product store + history |
| M03 | v0.3 | First product ranking |
| M04 | v0.4 | Product watcher |
| M05 | v0.5 | Reliable alerts |
| M06 | v1.0 | Product Intelligence |
| M07 | v2.0 | Content Intelligence |
| M08 | v3.0 | Revenue & Attribution Intelligence |
| M09 | v4.0 | Experiment Engine |
| M10 | v5.0 | Decision & Policy Engine |
| M11 | v6.0 | AI Analysis Assistant |
| M12 | v7.0 | Tool-Using Bot |
| M13 | v8.0 | Governed Automation |
| M14 | v9.0 | Production Bot |
| M15 | v10.0 | Affiliate Intelligence Platform |

Full product progression: [`docs/BOT-EVOLUTION-ROADMAP.md`](docs/BOT-EVOLUTION-ROADMAP.md). Just-in-time mapping: [`docs/MISSION-KNOWLEDGE-MAP.md`](docs/MISSION-KNOWLEDGE-MAP.md).

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

```text
Deterministic logic before LLM autonomy
Decision ≠ Execution
Model output = untrusted input
RISK 0 → auto
RISK 1 → auto + audit
RISK 2 → human approval
```

## Knowledge mastery vẫn tồn tại

Lesson PASS vẫn theo `docs/PASS-CRITERIA.md`. Mission PASS theo [`docs/MISSION-PASS-CRITERIA.md`](docs/MISSION-PASS-CRITERIA.md). Một mission hoàn thành **không được tự động tick lesson PASS**.

## Bootstrap scope

M00–M03 là bootstrap missions đầu tiên sẽ được author thành `ready` cùng working Go bot ở phase tiếp theo. Không tạo file placeholder cho M04–M15 trước khi author thực sự.