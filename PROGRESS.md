# Bảng tiến độ

> Review cố định: **12:00 Chủ nhật**. Build-First theo dõi **product progress (tiến độ sản phẩm)** và **knowledge progress (tiến độ kiến thức)** độc lập.

## Tiến độ Build

| Trường | Giá trị |
|---|---|
| Curriculum revision (phiên bản curriculum) | `v2026.09` active canonical |
| Learning mode (cách học) | Build-First v1 |
| Primary engineering track (nhánh kỹ thuật chính) | Go-first Bot Engineering |
| Current Mission (Mission hiện tại) | **M00 — Khởi động Affiliate Bot** |
| Mission authoring status | `ready` |
| Learner Mission status | ⬜ Chưa PASS |
| Learner Bot version | `pre-v0.0` — chưa có evidence M00 của learner |
| Learner workspace | `lab/learner/affiliate-bot/` |
| Reference implementation | `lab/affiliate-bot/` — reference v0.3, không phải starting state |
| Current build state | Chưa bắt đầu learner execution |
| Latest learner working commit | — |
| Current blocker | — |
| Weekly capacity | 0 / 9 giờ |
| Next build action | Mở `missions/M00-bot-boots.md`, chạy learner Bot, tự sửa một behavior nhỏ và lưu evidence đầu tiên |

> Reference implementation tồn tại để review/gỡ blocker. Nó **không** có nghĩa learner đã PASS M00–M03 và không được dùng làm starting state của learner.

## Tiến độ kiến thức

| Trường | Giá trị |
|---|---|
| Knowledge Part context | Part 0 |
| Current required knowledge slices | `0.1`, `0.2` cho M00 — chỉ phần cần để hiểu business/Bot boundary |
| 0.1 — Affiliate Expert là gì? | ⬜ Chưa PASS |
| 0.2 — Affiliate Bot Engineer là gì? | ⬜ Chưa PASS |
| Knowledge artifacts/evidence | — |

Mission chỉ yêu cầu knowledge slice đủ cho implementation. Full Lesson PASS vẫn theo [`docs/PASS-CRITERIA.md`](docs/PASS-CRITERIA.md). Mission PASS không tự động tick Lesson checkbox.

## Tiến độ Mission

| Mission | Target version | Learner status |
|---|---:|---|
| M00 — Khởi động Affiliate Bot | v0.0 | ⬜ |
| M01 — Product Ingest (Đọc dữ liệu sản phẩm) | v0.1 | ⬜ |
| M02 — Product Store & History (Lưu trữ + lịch sử) | v0.2 | ⬜ |
| M03 — First Product Ranking (Xếp hạng đầu tiên) | v0.3 | ⬜ |
| M04 — Product Watcher (Theo dõi sản phẩm) | v0.4 | ⬜ |
| M05 — Reliable Alerts (Cảnh báo đáng tin cậy) | v0.5 | ⬜ |
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

M04–M15 hiện là roadmap targets; chỉ M00–M03 đã được author `ready` trong `missions/`.

## Review Build-First hằng tuần

Trả lời theo evidence, không theo cảm giác:

1. **Đã ship gì?** Bot/feature/version nào thực sự chạy được?
2. **Đã chạy gì?** Command/workflow nào đã execute?
3. **Đã lỗi gì?** Failure case, bug hoặc assumption nào lộ ra?
4. **Đã đo gì?** Output/metric/log nào inspect được?
5. **Lỗi làm lộ kiến thức thiếu nào?** Lesson/concept nào cần pull?
6. **Đã cải tiến gì?** Code, logic, data model hoặc decision rule nào thay đổi?
7. **Bước nhỏ nhất tiếp theo có thể ship là gì?**

Checklist:

- [ ] cập nhật learner Mission status;
- [ ] chỉ cập nhật Lesson checkbox khi đạt Lesson PASS evidence;
- [ ] liên kết Mission evidence dưới `artifacts/missions/`;
- [ ] ghi latest learner working commit nếu có;
- [ ] cập nhật blocker;
- [ ] cập nhật calibration actual hours cho Mission hiện tại;
- [ ] review experiment/revenue/knowledge logs khi liên quan;
- [ ] giữ tổng effort trong weekly capacity;
- [ ] không copy reference implementation để thay thế learner evidence.

## Calibration (hiệu chỉnh) — M00 đến M05

M00–M05 là calibration cohort (nhóm hiệu chỉnh) đầu tiên. Mỗi Mission ghi:

```text
planned_hours                 giờ kế hoạch
actual_build_hours            giờ build
actual_debug_hours            giờ debug
actual_operate_hours          giờ vận hành
actual_knowledge_hours        giờ học kiến thức cần thiết
actual_retry_hours            giờ làm lại/review lại
result                        PASS / RETRY / BLOCKED / IN_PROGRESS
```

Dùng [`docs/BUILD-FIRST-CALIBRATION.md`](docs/BUILD-FIRST-CALIBRATION.md). Chưa thay planning baseline ~520h nếu chưa có actual learner data.

## Templates / Evidence (mẫu / bằng chứng)

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

| Tuần | Giờ | Mission | Learner Bot version | Lesson PASS | Kết quả chính | Next build |
|---|---:|---|---|---:|---|---|
| 1 | 0 | M00 ⬜ | pre-v0.0 | 0 | — | Run learner M00 Bot, tự sửa behavior nhỏ, test và lưu evidence |
