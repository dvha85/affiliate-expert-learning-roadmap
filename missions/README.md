# Mission System

Mission là đơn vị **build + run + observe + improve + operate + evidence** của Build-First curriculum.

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

## ID

Mission dùng `M00`, `M01`, ... và filename `missions/MXX-slug.md`.

## Hai state độc lập

```text
Authoring: planned → draft → ready
Learner:   ⬜ Not Started → 🟨 In Progress → 🟦 Awaiting Review → ✅ PASS
                                   └──────────────→ ⛔ Blocked
```

`status: ready` chỉ nói mission đã được author đủ để học. Nó không có nghĩa learner đã PASS.

## Mission metadata

```yaml
mission_id: "M00"
title: "Boot Affiliate Bot"
status: ready
requires_missions: []
bot_version_from: null
bot_version_to: "v0.0"
estimated_hours: 2
knowledge:
  required: []
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
```

## Content contract

Mission `ready` phải có:

1. Ship Target
2. Starting Bot State
3. Build First
4. Run
5. Observe
6. Knowledge Pull
7. Improve
8. Tests
9. Operate
10. Failure Case
11. Evidence
12. Explain-back
13. Mission PASS
14. Bot Version Result
15. Next Mission

Chi tiết: [`../docs/MISSION-AUTHORING-STANDARD.md`](../docs/MISSION-AUTHORING-STANDARD.md).

## State separation

Mission không được chứa cơ chế tự tick lesson PASS. Lesson PASS chỉ thay đổi khi learner đạt evidence theo `docs/PASS-CRITERIA.md`.