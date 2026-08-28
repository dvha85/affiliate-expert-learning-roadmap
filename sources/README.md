# Tài liệu nguồn

Roadmap được xây từ các tài liệu do chủ repo cung cấp và các revision canonical có versioning rõ ràng.

## Active canonical source

**`SYLLABUS-v2026.09.md`** là active canonical manifest hiện tại.

Revision v2026.09 dùng mô hình:

```text
v2026.09 active canonical
=
v2026.08 structural baseline
+
explicit v2026.09 overrides
```

Điều này cho phép giữ nguyên provenance của 23 Part / 89 Chapter / 671 lesson trong v2026.08 nhưng thay technology direction sang **Go-first Bot Engineering** mà không sao chép toàn bộ syllabus và tạo hai bản dễ drift.

## Historical structural baseline

`SYLLABUS-v2026.08.md` được giữ nguyên làm historical provenance/base structural source.

Nó chứa cấu trúc đầy đủ:

- Part;
- Chapter;
- Lesson ID/title;
- Project;
- LAB;
- PASS Gate;
- mục tiêu chương trình ban đầu.

C#/.NET-first trong v2026.08 là quyết định lịch sử và **không còn là active primary implementation path**.

## Các nguồn supplement

- `Noi-dung-dao-tao.txt` — lộ trình 50 tuần, nhịp học, project evolution và phương pháp thực hành.
- `Nghien-cuu.txt` — nghiên cứu, ví dụ Affiliate Bot, Product Intelligence, feedback loop, architecture và định hướng triển khai.

## Source precedence

```text
ACTIVE STRUCTURE / NORMATIVE OVERRIDES:
SYLLABUS-v2026.09

INHERITED STRUCTURAL BASELINE:
SYLLABUS-v2026.08

PACING CURRENT:
docs/15-MONTH-PLAN.md hoặc docs/12-MONTH-PLAN.md

EXECUTION ORDER:
docs/EXECUTION-MODEL.md

SUPPLEMENTS:
Noi-dung-dao-tao.txt + Nghien-cuu.txt
```

Quy tắc resolution:

```text
v2026.09 explicit override
→ v2026.09 thắng

v2026.09 không nói tới
→ kế thừa v2026.08

current platform/legal/API/software fact
→ external verification + freshness policy
```

## Go-first engineering decision

Xem:

- [`docs/ADR-001-GO-FIRST-BOT-STACK.md`](../docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`SYLLABUS-v2026.09.md`](SYLLABUS-v2026.09.md)

Active Track C:

```text
Go
→ Services / Workers
→ Collector
→ Database
→ Queue / Durable Workflow
→ Bot
→ Tool Engineering / MCP
→ AI Agent
→ Human Approval / Governance
→ Production
```

C#/.NET vẫn được phép làm comparison/reference stack nhưng không còn là primary implementation language của curriculum.

## Current knowledge overlay

Canonical source không bị âm thầm sửa bằng web research. Các dữ kiện hiện hành có thể thay đổi theo platform, luật, thuế, privacy, API, search, Go runtime hoặc AI/agent protocols được quản lý ở lớp riêng:

- [Freshness Policy](../docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](../docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)

Quy tắc:

```text
canonical concepts/structure = active canonical revision + inherited baseline
current operating facts = external source register + verified date
```

Nếu current fact làm một thuật ngữ canonical trở nên cũ, dùng current-state override trong lesson/roadmap thay vì âm thầm sửa history.

Xem [Source-to-Roadmap Traceability Map](../docs/SOURCE-MAPPING.md) để tra source ref convention và conflict rules.