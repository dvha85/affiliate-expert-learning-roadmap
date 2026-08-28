---
mission_id: "M02"
title: "Product Store & History"
status: ready
requires_missions: ["M01"]
bot_version_from: "v0.1"
bot_version_to: "v0.2"
estimated_hours: 4
knowledge:
  required: []
  on_demand: []
  reference: []
projects:
  contributes_to: [7]
risk_scope:
  external_side_effects: false
---

# Mission M02 — Product Store & History

## Ship Target

Bot có storage boundary rõ ràng, lưu được product snapshot trong in-memory implementation dùng cho unit tests và có PostgreSQL migration/schema path để triển khai persistence thật.

## Starting Bot State

v0.1 ingest được product nhưng chưa có history.

## Build First

Dùng `store.Repository` + `MemoryRepository` trước để hiểu behavior. Sau đó đọc migration SQL định nghĩa `products` và `product_snapshots`.

## Run

```bash
cd lab/affiliate-bot
go test ./...
```

## Observe

Current state không đủ để biết price/commission thay đổi thế nào. History là prerequisite cho watcher, analytics và decision audit.

## Knowledge Pull

### Required

- product identity vs snapshot/time-series state;
- repository boundary;
- SQL migration/schema basics;
- history/provenance thinking từ Part 12.

### On-demand

- PostgreSQL driver/integration wiring khi learner triển khai local DB thật.

### Reference

- full Affiliate Data Warehouse scope của Project 7.

## Improve

Giữ domain model độc lập khỏi DB driver để unit tests chạy nhanh và storage implementation có thể thay đổi.

## Tests

Unit tests phải chứng minh save/list snapshots và không mutate history cũ khi object input thay đổi.

## Operate

Chạy test nhiều lần. Khi local PostgreSQL được bật, dùng migration như contract cho integration path.

## Failure Case

Empty product ID hoặc snapshot invalid phải bị chặn trước persistence.

## Evidence

- repository interface;
- migration SQL;
- unit test output;
- note giải thích vì sao snapshot khác current product row.

## Explain-back

1. Vì sao bot cần history trước khi watcher có ý nghĩa?
2. Repository boundary giúp gì cho testing?
3. Vì sao M02 không bắt buộc DB integration test trong fast CI?

## Mission PASS

- [ ] storage boundary exists
- [ ] in-memory history works
- [ ] migration/schema path exists
- [ ] unit tests pass
- [ ] failure case covered
- [ ] required knowledge understood
- [ ] explain-back passes
- [ ] evidence saved

## Bot Version Result

```text
v0.1 → v0.2 product state + history foundation
```

## Next Mission

M03 — First Product Ranking.