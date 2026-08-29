# Profile 12 tháng — focused-hours forecast

> Evidence là gate; calendar không phải PASS criterion. Profile này chỉ là planning envelope và phải được reforecast từ learner actuals.

## Nguyên tắc planning

Không khóa Mission vào một tháng cố định. Dùng **focused-hour envelope + external waiting tách riêng**:

- khoảng 5–8 focused hours/tuần;
- waiting for account/platform/outcome được ghi riêng, không tính như giờ học;
- safety/evidence gate không bị nén để giữ lịch;
- learner có thể tiếp tục phần engineering được Mission cho phép trong lúc Reality gate đang chờ;
- sau M00–M05 phải reforecast từ actual build/debug/business/review time.

## Early-loop target

Mục tiêu pedagogical là đưa learner tới **first tracked human market action (M03)** đủ sớm để curriculum nhận reality feedback, thay vì để nhiều tháng trôi qua chỉ với infrastructure.

Nominal drafted Mission effort hiện tại:

| Mission | Nominal focused effort | Outcome |
|---|---:|---|
| M00 | ~10h | first evidence-backed decision |
| M01 | ~12h | trustworthy history |
| M02 | ~12h | grounded AI advisor |
| M03 | ~14h | first tracked human publish |
| **M00→M03** | **~48h** | first real tracked market action |

Với 5–8 focused hours/tuần, ~48h tương đương khoảng **6–10 tuần focused work**, chưa tính external blockers/waiting. Vì vậy “M03 vào tháng 5” không còn là default target.

Nếu learner bị block bởi account/platform/reality access, ghi `BLOCKED_EXTERNAL` và reforecast; không dùng sample thay cho E2.

## Planning bands

| Band | Missions | Planning intent |
|---|---|---|
| B1 | M00 | boot + real public evidence + first decision |
| B2 | M01–M02 | trustworthy data + grounded AI, giữ deterministic fallback |
| B3 | M03 | first human tracked publish càng sớm càng hợp lý sau prerequisites |
| B4 | M04–M05 | real outcome analytics + first reviewed improvement |
| B5 | M06–M07 | reliable watcher + DecisionPacket/memory |
| B6 | M08 | read-only evidence agent |
| B7 | M09–M10 | shadow approval → bounded governed automation |
| B8 | M11 | production closed loop + recovery drill |

Calendar 12 tháng là **upper planning container**, không phải lý do kéo dài một Mission đã PASS hoặc trì hoãn reality action khi prerequisites đã đủ.

## Suggested reforecast checkpoints

Reforecast sau:

1. M00 — vì đây là first absolute-beginner setup/build/evidence actual;
2. M03 — vì learner đã có first public tracked action;
3. M05 — vì đã có first closed market learning loop;
4. M07 — vì reliability/decision workload đã quan sát;
5. M10 — trước production closed loop.

Mỗi reforecast phải tách:

```text
focused build/debug/business/review hours
+
external waiting/blocker days
```

Không cộng hai loại trên thành một con số “giờ học”.

Xem thêm [`EFFORT-MODEL.md`](EFFORT-MODEL.md) và [`AFFILIATE-METRIC-REVENUE-SPINE.md`](AFFILIATE-METRIC-REVENUE-SPINE.md).
