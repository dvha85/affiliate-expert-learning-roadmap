---
mission_id: "MXX"
title: "Mission title"
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

# Mission MXX — Mission title

## Ship Target

Mô tả một output/behavior có thể quan sát được.

## Starting Bot State

Bot đang có gì trước mission này?

## Build First

Build smallest working slice trước khi đi sâu theory.

## Run

```bash
# exact command(s)
```

Expected output/behavior:

```text
...
```

## Observe

Điều gì còn sai, thiếu, brittle hoặc chưa hiểu?

## Knowledge Pull

### Required

- Lesson X.Y — vì sao cần ngay bây giờ?

### On-demand

- ...

### Reference

- ...

## Improve

Áp dụng knowledge pull để cải thiện code/logic/architecture.

## Tests

- happy path;
- boundary/invalid input;
- additional scope-dependent tests.

## Operate

Bot phải được chạy/quan sát như thế nào để chứng minh feature hữu ích?

## Failure Case

Một failure case bắt buộc và expected handling.

## Evidence

- code path / commit:
- test output:
- data/output:
- notes:

## Explain-back

1. Vì sao implementation này đúng với ship target?
2. Knowledge nào làm thay đổi quyết định/implementation?
3. Failure mode quan trọng nhất là gì?

## Mission PASS

Dùng [`../docs/MISSION-PASS-CRITERIA.md`](../docs/MISSION-PASS-CRITERIA.md).

- [ ] feature works
- [ ] bot runs
- [ ] tests pass
- [ ] data flows
- [ ] output inspectable
- [ ] failure case tested
- [ ] required knowledge understood
- [ ] explain-back passes
- [ ] evidence saved

## Bot Version Result

```text
before → after
```

## Next Mission

MXX — ...