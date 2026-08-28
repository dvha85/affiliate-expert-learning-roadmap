---
mission_id: "M01"
title: "Product Ingest"
status: ready
requires_missions: ["M00"]
bot_version_from: "v0.0"
bot_version_to: "v0.1"
estimated_hours: 3
knowledge:
  required: []
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
---

# Mission M01 — Product Ingest

## Ship Target

Đọc product JSON thành validated `[]Product` và trả lỗi rõ ràng cho input invalid.

## Starting Bot State

v0.0 chạy được nhưng product handling còn rất mỏng.

## Build First

Đọc `internal/product` và `internal/ingest`; chạy sample data trước rồi sửa một field.

## Run

```bash
cd lab/affiliate-bot
go run ./cmd/bot
```

## Observe

Raw JSON không phải business data đáng tin ngay. Bot cần schema/validation trước khi scoring hoặc automation.

## Knowledge Pull

### Required

- Product fields tối thiểu: ID, name, price, commission rate.
- Go struct, JSON decode, error handling, validation.

### On-demand

- Platform-specific fields chỉ thêm khi có adapter thật.

### Reference

- Part 12 data model đầy đủ để sau.

## Improve

Thêm validation phù hợp business semantics; tránh để price âm, empty ID/name hoặc commission ngoài range.

## Tests

```bash
go test ./...
```

Phải cover valid JSON, malformed JSON và invalid product.

## Operate

Chạy với sample file và một file chỉnh sửa thủ công để quan sát validation behavior.

## Failure Case

Malformed JSON hoặc product invalid phải trả lỗi, không silently drop data.

## Evidence

Lưu test output, sample input/output và note validation nào bảo vệ decision downstream.

## Explain-back

1. Vì sao decode thành công chưa đủ?
2. Validation nào là business validation, validation nào chỉ là syntax?
3. Vì sao không đưa platform-specific field vào core model quá sớm?

## Mission PASS

- [ ] ingest works
- [ ] tests pass
- [ ] valid data flows
- [ ] invalid data fails explicitly
- [ ] output inspectable
- [ ] required knowledge understood
- [ ] explain-back passes
- [ ] evidence saved

## Bot Version Result

```text
v0.0 → v0.1 validated product ingest
```

## Next Mission

M02 — Product Store & History.