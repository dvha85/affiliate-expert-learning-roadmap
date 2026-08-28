# Hệ thống Mission

Mission là đơn vị **build + run + observe + improve + operate + evidence (xây + chạy + quan sát + cải tiến + vận hành + bằng chứng)** của Build-First curriculum.

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

## ID

Mission dùng `M00`, `M01`, ... và filename `missions/MXX-slug.md`.

## Hai state (trạng thái) độc lập

```text
Authoring (trạng thái nội dung): planned → draft → ready
Learner (trạng thái người học):  ⬜ Chưa bắt đầu → 🟨 Đang làm → 🟦 Chờ review → ✅ PASS
                                                        └────────────→ ⛔ Blocked
```

`status: ready` chỉ nói Mission đã được author đủ để học. Nó không có nghĩa learner đã PASS.

## Metadata của Mission

```yaml
mission_id: "M00"
title: "Khởi động Affiliate Bot"
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

## Content contract (hợp đồng nội dung)

Mission `ready` phải có các section sau; English term được giữ để tương thích validator và luôn có nghĩa Việt trong Mission:

1. Ship Target — Mục tiêu bàn giao
2. Starting Bot State — Trạng thái Bot ban đầu
3. Build First — Xây trước
4. Run — Chạy
5. Observe — Quan sát
6. Knowledge Pull — Lấy kiến thức đúng lúc
7. Improve — Cải tiến
8. Tests — Kiểm thử
9. Operate — Vận hành
10. Failure Case — Tình huống lỗi
11. Evidence — Bằng chứng
12. Explain-back — Giải thích lại
13. Mission PASS — Tiêu chí PASS
14. Bot Version Result — Kết quả phiên bản Bot
15. Next Mission — Mission tiếp theo

Chi tiết: [`../docs/MISSION-AUTHORING-STANDARD.md`](../docs/MISSION-AUTHORING-STANDARD.md).

## Learner workspace và reference implementation

Bootstrap M00–M03 dùng:

```text
learner workspace: lab/learner/affiliate-bot/
reference:         lab/affiliate-bot/
```

Learner phải tự phát triển capability theo Mission. Reference (bản tham chiếu) chỉ dùng để đối chiếu/gỡ blocker và không phải starting state của learner.

## State separation (tách trạng thái)

Mission không được chứa cơ chế tự tick Lesson PASS. Lesson PASS chỉ thay đổi khi learner đạt evidence theo `docs/PASS-CRITERIA.md`.

## Knowledge rule (quy tắc kiến thức)

`knowledge.required` nghĩa là learner phải hiểu **phần kiến thức cần cho Mission**, không có nghĩa phải full PASS toàn bộ Lesson trước khi code.

```text
required knowledge for Mission
≠
full Lesson PASS
```

## Quy chuẩn ngôn ngữ

Tiếng Việt là ngôn ngữ chính thức. English term chỉ giữ khi cần đối chiếu kỹ thuật và có giải thích tiếng Việt khi quan trọng. Xem [`../docs/LANGUAGE-POLICY.md`](../docs/LANGUAGE-POLICY.md).