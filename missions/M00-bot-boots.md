---
mission_id: "M00"
title: "Bot Boots"
status: ready
requires_missions: []
bot_version_from: null
bot_version_to: "v0.0"
estimated_hours: 2
knowledge:
  required: ["0.1", "0.2"]
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
---

# Mission M00 — Bot Boots

## Ship Target

Chạy được Affiliate Bot bằng Go và nhận output trạng thái + sample product summary.

## Starting Bot State

Chưa có working bot.

## Build First

Dùng workspace `lab/affiliate-bot/`; đọc code nhỏ nhất trước khi học sâu Go.

## Run

```bash
cd lab/affiliate-bot
go run ./cmd/bot
```

Expected: bot start, load sample products, print count và exit cleanly.

## Observe

Bạn chưa cần hiểu toàn bộ Go. Điều cần hiểu ngay là bot đang phục vụ business flow nào và boundary của Bot Engineer là gì.

## Knowledge Pull

### Required

- `0.1` — Affiliate Expert là gì?
- `0.2` — Affiliate Bot Engineer là gì?

### On-demand

- `package`, `func`, struct/slice ở mức đọc được code hiện tại.

### Reference

- Part 15 formal Go/Bot Engineering mastery để sau.

## Improve

Đổi message/status nhỏ hoặc thêm một sample product, chạy lại và quan sát output.

## Tests

```bash
go test ./...
```

## Operate

Run bot nhiều lần; output phải deterministic với cùng sample data.

## Failure Case

Đổi data path sang file không tồn tại; bot phải trả lỗi rõ ràng và exit non-success thay vì panic mơ hồ.

## Evidence

Lưu command, output, code path/commit và note bạn hiểu bot hiện làm gì/chưa làm gì.

## Explain-back

1. Affiliate Bot hiện tại tự động hóa phần nào?
2. Vì sao M00 chưa cần AI/Agent?
3. Khác nhau giữa dùng Go sớm và mastery Part 15 là gì?

## Mission PASS

- [ ] feature works
- [ ] bot runs
- [ ] tests pass
- [ ] sample data flows
- [ ] output inspectable
- [ ] missing-file failure case understood/tested
- [ ] required knowledge understood
- [ ] explain-back passes
- [ ] evidence saved

## Bot Version Result

```text
no bot → v0.0 runnable Go bot
```

## Next Mission

M01 — Product Ingest.