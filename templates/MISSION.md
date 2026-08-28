---
mission_id: "MXX"
title: "Tên Mission"
status: planned
requires_missions: []
bot_version_from: null
bot_version_to: "vX.Y"
estimated_hours: 0
knowledge:
  required: []
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
---

# Mission MXX — Tên Mission

## Ship Target — Mục tiêu bàn giao

Mô tả một output/behavior (đầu ra/hành vi) có thể quan sát được.

## Starting Bot State — Trạng thái Bot ban đầu

Bot learner đang có gì trước Mission này? Ghi rõ path/previous Mission để starting state có thể tái lập.

## Build First — Xây trước

Build smallest working slice (phần nhỏ nhất chạy được) trước khi đi sâu theory (lý thuyết).

## Run — Chạy

```bash
# command(s) chính xác
```

Expected output/behavior (đầu ra/hành vi mong đợi):

```text
...
```

## Observe — Quan sát

Điều gì còn sai, thiếu, brittle (dễ vỡ) hoặc chưa hiểu?

## Knowledge Pull — Lấy kiến thức đúng lúc

### Required — Bắt buộc cho Mission

- Lesson X.Y — knowledge slice nào cần ngay và vì sao?

> Required for Mission không đồng nghĩa full Lesson PASS.

### On-demand — Khi phát sinh nhu cầu

- ...

### Reference — Tham khảo

- ...

## Improve — Cải tiến

Áp dụng knowledge pull để cải thiện code/logic/architecture.

## Tests — Kiểm thử

- happy path (luồng đúng);
- boundary/invalid input (biên/đầu vào sai);
- additional scope-dependent tests (kiểm thử bổ sung theo scope).

## Operate — Vận hành

Bot phải được chạy/quan sát như thế nào để chứng minh feature hữu ích?

## Failure Case — Tình huống lỗi

Một failure case bắt buộc và expected handling (cách xử lý mong đợi).

## Evidence — Bằng chứng

- code path / commit:
- test output:
- data/output:
- notes (ghi chú):

## Explain-back — Giải thích lại

1. Vì sao implementation này đúng với ship target?
2. Knowledge nào làm thay đổi quyết định/implementation?
3. Failure mode quan trọng nhất là gì?

## Mission PASS — Tiêu chí PASS

Dùng [`../docs/MISSION-PASS-CRITERIA.md`](../docs/MISSION-PASS-CRITERIA.md).

- [ ] feature works — tính năng chạy đúng
- [ ] bot runs — Bot chạy được
- [ ] tests pass — kiểm thử đạt
- [ ] data flows — dữ liệu đi qua đúng luồng khi có data flow
- [ ] output inspectable — đầu ra kiểm tra được
- [ ] failure case tested — đã thử tình huống lỗi
- [ ] required knowledge understood — hiểu knowledge slice bắt buộc
- [ ] explain-back passes — giải thích lại đạt
- [ ] evidence saved — đã lưu bằng chứng

## Bot Version Result — Kết quả phiên bản Bot

```text
before → after
```

## Next Mission — Mission tiếp theo

MXX — ...

> Tiếng Việt là ngôn ngữ chính thức của nội dung; English term chỉ giữ khi cần kỹ thuật và có giải thích tiếng Việt khi quan trọng.