---
mission_id: "M02"
title: "Lưu trữ và lịch sử sản phẩm"
status: ready
requires_missions: ["M01"]
bot_version_from: "v0.1"
bot_version_to: "v0.2"
estimated_hours: 4
knowledge:
  required: ["38.2", "39.1", "51.3"]
  on_demand: []
  reference: []
projects:
  contributes_to: [7]
risk_scope:
  external_side_effects: false
---

# Mission M02 — Product Store & History (Lưu trữ và lịch sử sản phẩm)

## Ship Target — Mục tiêu bàn giao

Từ learner Bot v0.1, tự xây storage boundary (ranh giới lưu trữ), lưu được ProductSnapshot (ảnh chụp trạng thái sản phẩm) vào in-memory repository dùng cho unit test, định nghĩa PostgreSQL migration/schema path và **nối storage vào executable flow**.

Sau M02, Bot phải có history foundation (nền tảng lịch sử) thật, không chỉ có package tồn tại rời rạc.

## Starting Bot State — Trạng thái Bot ban đầu

Starting state là learner commit đã PASS M01:

```text
v0.1
Product model
→ JSON ingest
→ validation
→ visible product count
```

Chưa có storage/history.

Workspace:

```text
lab/learner/affiliate-bot/
```

## Build First — Xây trước

Build theo lát nhỏ:

```text
Snapshot type
→ Repository interface
→ MemoryRepository
→ save/list unit test
→ gọi Repository từ cmd/bot
→ migration SQL cho PostgreSQL
```

Đừng bắt đầu bằng ORM/framework nặng. Mục tiêu là hiểu data boundary trước.

## Run — Chạy

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Expected capability:

```text
load validated products
→ create snapshots
→ save snapshots
→ report snapshot count/history state
→ exit cleanly
```

## Observe — Quan sát

Current Product state (trạng thái hiện tại) không đủ để trả lời:

- giá hôm nay khác hôm qua không;
- commission vừa tăng hay giảm;
- watcher phát hiện delta dựa trên đâu;
- decision sau này có truy lại dữ liệu đã thấy tại thời điểm ra quyết định không.

History là prerequisite (điều kiện nền) cho watcher, analytics và decision audit.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Required — Bắt buộc cho Mission

- `38.2` — ProductSnapshot và dữ liệu lịch sử.
  - slice: Product identity khác snapshot state theo thời gian.
- `39.1` — Snapshot.
  - slice: mỗi quan sát có timestamp và không được mutate history cũ.
- `51.3` — PostgreSQL, Redis và data access.
  - slice: Repository (lớp trừu tượng truy cập dữ liệu), migration/schema và persistence contract; **chưa cần Redis**.

> Không yêu cầu full PASS ba Lesson trước khi build. Required ở đây là knowledge slice đủ để giải thích design M02.

### On-demand — Khi phát sinh nhu cầu

- PostgreSQL driver/integration wiring khi bạn muốn chạy local DB thật;
- transaction/index khi workload thật làm xuất hiện nhu cầu;
- provenance/data lineage sâu hơn khi dữ liệu đến từ platform thật.

### Reference — Tham khảo

- Project 7 — Affiliate Data Warehouse là scope lớn hơn;
- `lab/affiliate-bot/` chỉ dùng để review sau learner attempt.

## Improve — Cải tiến

Giữ domain model độc lập khỏi DB driver để:

- unit test nhanh;
- có thể thay storage implementation;
- business logic không bị khóa vào một thư viện persistence.

Quan trọng: `cmd/bot` phải thực sự gọi Repository để M02 là capability của Bot, không phải dead code (code không được sử dụng).

## Tests — Kiểm thử

Unit tests phải chứng minh tối thiểu:

- save/list snapshots hoạt động;
- history cũ không bị mutate khi object input bị thay đổi;
- invalid Product/Snapshot bị reject;
- executable path có thể lưu snapshot sau ingest.

## Operate — Vận hành

Chạy Bot nhiều lần với sample data. Ở M02 chưa yêu cầu durable database giữa hai process run nếu chưa bật PostgreSQL; mục tiêu là chứng minh storage boundary + snapshot semantics + executable integration.

Khi bật local PostgreSQL, migration là contract (hợp đồng schema) cho integration path.

## Failure Case — Tình huống lỗi

Empty Product ID, zero timestamp hoặc Snapshot invalid phải bị chặn trước persistence.

## Evidence — Bằng chứng

Lưu:

- Repository interface;
- MemoryRepository implementation;
- migration SQL;
- code path nơi `cmd/bot` gọi Repository;
- unit test output;
- learner commit;
- note giải thích Product row khác ProductSnapshot như thế nào.

## Explain-back — Giải thích lại

1. Vì sao Bot cần history trước khi Product Watcher có ý nghĩa?
2. Repository boundary giúp gì cho testing và thay database?
3. Vì sao current Product và ProductSnapshot không nên là cùng một khái niệm?
4. Vì sao M02 chưa bắt buộc PostgreSQL integration test trong fast learning loop?

## Mission PASS — Tiêu chí PASS

- [ ] learner tự build storage boundary
- [ ] in-memory history chạy đúng
- [ ] executable thực sự gọi storage
- [ ] migration/schema path tồn tại
- [ ] tests PASS
- [ ] failure case đã được thử
- [ ] hiểu required knowledge slices
- [ ] explain-back đạt
- [ ] evidence đã lưu

## Bot Version Result — Kết quả phiên bản Bot

```text
v0.1 → v0.2 Product state + snapshot/history foundation
```

## Next Mission — Mission tiếp theo

M03 — First Product Ranking (Xếp hạng sản phẩm đầu tiên).