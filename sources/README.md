# Tài liệu nguồn

Roadmap được tổng hợp từ ba tài liệu do chủ repo cung cấp:

1. `SYLLABUS-v2026.08.md` — cấu trúc chuẩn theo phần, chương, bài, project, LAB và PASS gate.
2. `Noi-dung-dao-tao.txt` — lộ trình 50 tuần, nhịp học, project evolution và phương pháp thực hành.
3. `Nghien-cuu.txt` — nghiên cứu, ví dụ Affiliate Bot, Product Intelligence, feedback loop, architecture và định hướng triển khai.

## Source precedence

- **Structure:** `SYLLABUS-v2026.08.md` là nguồn chuẩn.
- **Current pacing:** dùng `docs/15-MONTH-PLAN.md` hoặc `docs/12-MONTH-PLAN.md`; lịch 50 tuần chỉ giữ vai trò provenance/context.
- **Execution order:** dùng `docs/EXECUTION-MODEL.md` để phân biệt knowledge prerequisites và parallel execution loops.
- **Examples/practice/rationale:** `Noi-dung-dao-tao.txt` và `Nghien-cuu.txt` bổ sung syllabus.
- Nếu nguồn supplement không có counterpart trực tiếp, không tự suy diễn mapping.

## Current knowledge overlay

Ba file nguồn trên **không bị âm thầm sửa bằng web research**. Các dữ kiện hiện hành có thể thay đổi theo platform, luật, thuế, privacy, API, search hoặc AI được quản lý ở lớp riêng:

- [Freshness Policy](../docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](../docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)

Quy tắc:

```text
canonical structure = source files trong sources/
current operating facts = external source register + verified date
```

Nếu current fact làm một thuật ngữ canonical trở nên cũ, giữ lesson ID/title để bảo toàn provenance và dùng **current-state override** trong lesson/roadmap. Ví dụ: syllabus giữ `14.2 — Promotion Quality Points`, nhưng TikTok Shop Vietnam dùng `Promotion Performance Score (PPS)` làm active score từ 2026-08-27.

Xem [Source-to-Roadmap Traceability Map](../docs/SOURCE-MAPPING.md) để tra mapping toàn bộ 23 Part / 89 Chapter, source ref convention và conflict rules.
