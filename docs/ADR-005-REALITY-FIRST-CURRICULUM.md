# ADR-005 — Reality-First Curriculum

**Status:** Accepted — 2026-09-02  
**Supersedes:** thứ tự Mission v1 được mô tả tại baseline `curriculum-v1-pre-reality-first`; không thay thế các rule safety/authority của ADR-004.

## Context

V1 bắt đầu bằng starter Go, history và AI advisory trước khi learner có một
hành động thị trường. Cấu trúc kỹ thuật có ích, nhưng feedback từ audience,
channel, offer và tracking xuất hiện quá muộn đối với một người mới.

## Decision

Curriculum v2 dùng thứ tự sau làm canonical execution spine:

```text
O00 safe synthetic walkthrough (không phải PASS)
→ M00 first safe market loop, human-only manual publish
→ M01 first outcome snapshot
  └→ M02 smallest deterministic Bot
      (M01 + M02) → M03 trustworthy history & measurement
      → M04 grounded AI advisor
      → M05 first reviewed improvement
      → M06 … M11 governed automation / production loop
```

- O00 chỉ tạo E0 synthetic evidence và không có external side effect.
- M00 đưa human vào E1→E2: tự quan sát, tự tạo/review/publish một artifact
  nhỏ có disclosure/tracking; Bot/AI không publish.
- M01 và M02 có thể học song song sau M00. M01 ghi outcome thật/snapshot;
  M02 tạo deterministic baseline nhỏ nhất có thể audit.
- AI chỉ xuất hiện ở M04, advisory A1, không tool/write/execute.
- M05 mới cho phép đề xuất improvement từ outcome, qua test/review/rollback.

`authoring status` không phải release claim. Mission chỉ được gọi delivered khi
metadata delivery có starter, eval pack, verification commands và knowledge
links có thể kiểm trong repository.

## Consequences

- Tài liệu v2 là authority; các Mission/lesson v1 vẫn giữ để provenance và
  migration, không phải entrypoint cho learner mới.
- Go vẫn có thể là reference/fallback hoặc implementation profile; v2 không
  ép người mới cài Go trước M00.
- Mốc thời gian v2 là hypothesis cần personal actuals, không phải hứa hẹn.
  Target ban đầu là E2 sớm, khoảng không quá 8 giờ focused work nếu
  account/channel sẵn sàng.
- Chỉ chuyển một Mission v2 sang `ready` khi strict authoring-bundle check qua.
  Không dùng sample để thay E1/E2/E3/E4 market evidence cho live activation.

## Non-goals

ADR này không đổi policy/approval architecture, không trao execution authority
cho AI/workflow, không xóa v1 artifacts, và không tự động migrate learner state.
