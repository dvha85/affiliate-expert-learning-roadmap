# Tài liệu nguồn

Roadmap được xây từ các tài liệu do chủ repo cung cấp và các revision canonical có versioning rõ ràng.

## Active canonical source

**`SYLLABUS-v2026.09.md`** là active canonical manifest hiện tại.

Revision v2026.09 dùng mô hình:

```text
v2026.09 active canonical
=
v2026.08 historical source baseline
+
explicit v2026.09 overrides
+
validated normalized roadmap inventory
```

Active curriculum vẫn giữ **23 Part / 89 Chapter / 671 lesson / 14 main projects**, nhưng không giả định rằng mọi lesson ID/title trong normalized roadmap đã xuất hiện verbatim trong historical source.

Đọc [`CURRICULUM-INDEX-v2026.09.md`](CURRICULUM-INDEX-v2026.09.md) để hiểu provenance classes và cách resolve đủ 671 active lesson IDs.

## Historical source baseline

`SYLLABUS-v2026.08.md` được giữ nguyên làm historical provenance/base source.

Nó chứa:

- Part và Chapter structure;
- nhiều lesson ID/title được ghi explicit;
- một số chapter/design block được roadmap sau đó normalize thành lesson-sized units;
- Project, LAB, PASS Gate và mục tiêu chương trình ban đầu.

Vì vậy **không được tuyên bố rằng mọi normalized lesson ID hiện tại đều đã tồn tại verbatim trong v2026.08**.

Provenance của active lesson được phân loại:

```text
source_explicit
normalized_from_chapter
normalized_then_overridden
```

C#/.NET-first trong v2026.08 là quyết định lịch sử và **không còn là active primary implementation path**.

## Normalized active lesson inventory

Inventory lesson đang vận hành nằm ở:

```text
ROADMAP.md
+
roadmap/part-00.md ... roadmap/part-22.md
```

Curriculum CI bảo vệ count, chapter placement, lesson IDs và lifecycle. `CURRICULUM-INDEX-v2026.09.md` định nghĩa cách inventory này truy ngược về historical source + active override mà không tạo thêm một bản copy 671-row dễ drift.

## Các nguồn supplement

- `Noi-dung-dao-tao.txt` — lộ trình 50 tuần, nhịp học, project evolution và phương pháp thực hành.
- `Nghien-cuu.txt` — nghiên cứu, ví dụ Affiliate Bot, Product Intelligence, feedback loop, architecture và định hướng triển khai.

## Source precedence

```text
ACTIVE NORMATIVE OVERRIDES:
SYLLABUS-v2026.09

HISTORICAL SOURCE EVIDENCE:
SYLLABUS-v2026.08

NORMALIZED ACTIVE LESSON INVENTORY:
ROADMAP.md + roadmap/part-00..22.md

PACING CURRENT:
docs/15-MONTH-PLAN.md hoặc docs/12-MONTH-PLAN.md

EXECUTION ORDER:
docs/EXECUTION-MODEL.md

SUPPLEMENTS:
Noi-dung-dao-tao.txt + Nghien-cuu.txt
```

Quy tắc resolution:

```text
roadmap lesson ID/title
→ v2026.09 explicit override nếu có
→ v2026.08 lesson-level evidence nếu source-explicit
→ nếu không explicit, dùng chapter/block-level provenance
→ external verification cho current facts
```

`S:P/C/L` là normalized canonical identifier, **không phải lời khẳng định rằng exact lesson token luôn tồn tại trong historical file**.

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
- [Bot Engineering Refresh 2026.08](../docs/BOT-ENGINEERING-REFRESH-2026.08.md)

Quy tắc:

```text
canonical concepts/structure = normalized inventory + active overrides + historical provenance
current operating facts = external source register + verified date
```

Nếu current fact làm một thuật ngữ canonical trở nên cũ, dùng current-state override trong lesson/roadmap thay vì âm thầm sửa history.

Xem [Source-to-Roadmap Traceability Map](../docs/SOURCE-MAPPING.md) để tra source ref convention và conflict rules.