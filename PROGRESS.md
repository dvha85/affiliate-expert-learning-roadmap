# Progress Dashboard

> Review cố định: **12:00 Chủ nhật**. Build-First theo dõi **product progress** và **knowledge progress** riêng biệt.

## Build Progress

| Trường | Giá trị |
|---|---|
| Curriculum revision | `v2026.09` active canonical |
| Learning mode | Build-First v1 |
| Primary engineering track | Go-first Bot Engineering |
| Current Mission | **M00 — Bot Boots** |
| Mission authoring status | `ready` |
| Learner Mission status | ⬜ Chưa PASS |
| Bot version | `pre-v0.0` — repo có reference implementation; learner chưa ship M00 evidence |
| Current build state | Chưa bắt đầu learner execution |
| Latest learner working commit | — |
| Current blocker | — |
| Weekly capacity | 0 / 9 giờ |
| Next build action | Mở `missions/M00-bot-boots.md`, chạy bot và lưu evidence đầu tiên |

> Repo đã có bootstrap implementation để học và sửa. Điều đó **không** có nghĩa learner đã PASS M00. Bot version trong bảng là learner product state, không phải repository reference state.

## Knowledge Progress

| Trường | Giá trị |
|---|---|
| Knowledge Part context | Part 0 |
| Current required knowledge | `0.1`, `0.2` cho M00 |
| 0.1 — Affiliate Expert là gì? | ⬜ Chưa PASS |
| 0.2 — Affiliate Bot Engineer là gì? | ⬜ Chưa PASS |
| Knowledge artifacts/evidence | — |

Lesson PASS vẫn theo [`docs/PASS-CRITERIA.md`](docs/PASS-CRITERIA.md). Mission PASS không tự động tick lesson checkbox.

## Mission Progress

| Mission | Target version | Learner status |
|---|---:|---|
| M00 — Bot Boots | v0.0 | ⬜ |
| M01 — Product Ingest | v0.1 | ⬜ |
| M02 — Product Store & History | v0.2 | ⬜ |
| M03 — First Product Ranking | v0.3 | ⬜ |
| M04 — Product Watcher | v0.4 | ⬜ |
| M05 — Reliable Alerts | v0.5 | ⬜ |
| M06 — Product Intelligence | v1.0 | ⬜ |
| M07 — Content Intelligence | v2.0 | ⬜ |
| M08 — Revenue & Attribution Intelligence | v3.0 | ⬜ |
| M09 — Experiment Engine | v4.0 | ⬜ |
| M10 — Decision & Policy Engine | v5.0 | ⬜ |
| M11 — AI Analysis Assistant | v6.0 | ⬜ |
| M12 — Tool-Using Bot | v7.0 | ⬜ |
| M13 — Governed Automation | v8.0 | ⬜ |
| M14 — Production Bot | v9.0 | ⬜ |
| M15 — Affiliate Intelligence Platform | v10.0 | ⬜ |

M04–M15 hiện là roadmap targets; chỉ M00–M03 đã được author `ready` ở `missions/`.

## Weekly Build-First Review

Trả lời theo evidence, không theo cảm giác:

1. **What shipped?** Bot/feature/version nào thực sự chạy được?
2. **What ran?** Command/workflow nào đã execute?
3. **What failed?** Failure case, bug hoặc assumption nào lộ ra?
4. **What was measured?** Output/metric/log nào có thể inspect?
5. **What knowledge did the failure reveal?** Lesson/concept nào cần pull?
6. **What improved?** Code, logic, data model hoặc decision rule nào đã thay đổi?
7. **What is the next smallest shippable action?**

Checklist:

- [ ] cập nhật learner Mission status;
- [ ] chỉ cập nhật lesson checkbox khi đạt lesson PASS evidence;
- [ ] liên kết Mission evidence dưới `artifacts/missions/`;
- [ ] ghi latest learner working commit nếu có;
- [ ] cập nhật blocker;
- [ ] cập nhật calibration actual hours cho active Mission;
- [ ] review experiment/revenue/knowledge logs nếu relevant;
- [ ] giữ tổng effort trong weekly capacity.

## Calibration — M00 to M05

M00–M05 là calibration cohort đầu tiên. Mỗi mission ghi:

```text
planned_hours
actual_build_hours
actual_debug_hours
actual_operate_hours
actual_knowledge_hours
actual_retry_hours
result
```

Dùng [`docs/BUILD-FIRST-CALIBRATION.md`](docs/BUILD-FIRST-CALIBRATION.md). Chưa thay planning baseline ~520h nếu chưa có actual learner data.

## Templates / evidence

- [Mission Template](templates/MISSION.md)
- [Mission PASS](docs/MISSION-PASS-CRITERIA.md)
- [Mission Evidence](artifacts/missions/README.md)
- [Lesson Notes](templates/LESSON-NOTES.md)
- [Experiment Log](templates/EXPERIMENT-LOG.md)
- [Revenue Journal](templates/REVENUE-JOURNAL.md)
- [Knowledge Entry](templates/KNOWLEDGE-ENTRY.md)
- [Project README](templates/PROJECT-README.md)
- [Retrospective](templates/RETROSPECTIVE.md)

## Nhật ký tuần

| Tuần | Giờ | Mission | Bot version | Lesson PASS | Kết quả chính | Next build |
|---|---:|---|---|---:|---|---|
| 1 | 0 | M00 ⬜ | pre-v0.0 | 0 | — | Run M00 bootstrap bot |
