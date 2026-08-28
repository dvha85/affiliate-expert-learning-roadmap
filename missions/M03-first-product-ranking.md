---
mission_id: "M03"
title: "First Product Ranking"
status: ready
requires_missions: ["M02"]
bot_version_from: "v0.2"
bot_version_to: "v0.3"
estimated_hours: 4
knowledge:
  required: ["5.11", "27.3"]
  on_demand: []
  reference: []
projects:
  contributes_to: [4]
risk_scope:
  external_side_effects: false
---

# Mission M03 — First Product Ranking

## Ship Target

Bot rank product bằng hai chiến lược và cho thấy bằng dữ liệu vì sao `commission_rate only` có thể đưa ra thứ tự kém hơn một score có Expected Value.

## Starting Bot State

v0.2 có validated products và history foundation nhưng chưa có decision logic.

## Build First

Chạy naive ranking trước:

```text
score = commission_rate
```

Sau đó mới đọc output và hỏi: sản phẩm commission cao nhất có thật sự tạo expected commission/order tốt nhất không?

## Run

```bash
cd lab/affiliate-bot
go run ./cmd/bot
go test ./...
```

## Observe

Commission rate bỏ qua price và conversion potential. Ranking có thể đảo khi dùng expected commission per opportunity.

## Knowledge Pull

### Required

- `5.11` — Expected Value.
- `27.3` — Ranking.

### On-demand

- Demand, Product–Audience Fit, valid-order/refund risk, quality and seller signals when moving to M06.

### Reference

- advanced statistics/AI ranking intentionally deferred.

## Improve

Baseline implementation uses:

```text
commission-only score = commission rate
expected-value score = price × commission rate × conversion potential
```

Formula is intentionally simple; it creates context for later economics/risk refinement.

## Tests

Tests must show at least one dataset where the two strategies produce a different top product and verify deterministic ordering.

## Operate

Run against `sample-products.json`; inspect `commission-only` and `expected-value` rankings side by side.

## Failure Case

Invalid/zero conversion potential or malformed product data must not create NaN/undefined ranking behavior.

## Evidence

Save before/after ranking output and one paragraph explaining why the order changed.

## Explain-back

1. Vì sao commission rate không phải Expected Value?
2. Tại sao ranking function phải deterministic ở giai đoạn này?
3. Những biến nào còn thiếu trước khi score có thể dùng cho real recommendation?

## Mission PASS

- [ ] both rankings run
- [ ] tests pass
- [ ] same input produces deterministic output
- [ ] at least one before/after ordering difference is explained
- [ ] failure case covered
- [ ] lessons 5.11 and 27.3 understood enough for the implementation
- [ ] explain-back passes
- [ ] evidence saved

## Bot Version Result

```text
v0.2 → v0.3 first decision/ranking behavior
```

## Next Mission

M04 — Product Watcher.