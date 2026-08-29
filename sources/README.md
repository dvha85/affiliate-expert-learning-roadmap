# Tài liệu nguồn

Thư mục `sources/` là **historical/research archive**, không phải active curriculum authority.

## Active authority hiện tại

Nguồn chuẩn đang vận hành của chương trình là:

1. [`../CURRICULUM.md`](../CURRICULUM.md) — active canonical curriculum;
2. [`../ROADMAP.md`](../ROADMAP.md) và các file `../roadmap/part-*.md` — execution inventory của active curriculum;
3. [`../docs/SOURCE-MAPPING.md`](../docs/SOURCE-MAPPING.md) — traceability từ active curriculum về historical/training/research sources.

Nếu nội dung trong `sources/` mâu thuẫn với active authority ở trên, **active authority thắng**. Không sửa historical file để làm nó trông giống trạng thái hiện tại.

## Historical syllabus

- `SYLLABUS-v2026.08.md` — historical baseline ban đầu.
- `SYLLABUS-v2026.09.md` — historical revision trước outcome-driven redesign.
- `CURRICULUM-INDEX-v2026.09.md` — historical normalized index của revision v2026.09.

Các file này vẫn quan trọng để truy provenance, rationale và các ý tưởng domain đã sinh ra curriculum hiện tại, nhưng chúng **không còn là manifest active**.

Các count như **23 Part / 89 Chapter / 671 lesson / 14 main projects** thuộc revision lịch sử và không được dùng để mô tả curriculum đang vận hành.

## Supplementary source material

- `Noi-dung-dao-tao.txt` — nguồn đào tạo về nhịp học, project evolution và thực hành.
- `Nghien-cuu.txt` — nguồn nghiên cứu về Affiliate Bot, Product Intelligence, feedback loop, architecture và triển khai.

Các supplement cung cấp evidence/rationale cho thiết kế bài học. Chúng không tự động override active curriculum.

## Source precedence

```text
ACTIVE CANONICAL CURRICULUM:
CURRICULUM.md

ACTIVE EXECUTION INVENTORY:
ROADMAP.md + roadmap/part-*.md

TRACEABILITY / CONFLICT RESOLUTION:
docs/SOURCE-MAPPING.md

HISTORICAL SYLLABUS / INDEX:
sources/SYLLABUS-v2026.08.md
sources/SYLLABUS-v2026.09.md
sources/CURRICULUM-INDEX-v2026.09.md

SUPPLEMENTARY TRAINING / RESEARCH:
sources/Noi-dung-dao-tao.txt
sources/Nghien-cuu.txt

CURRENT-FACT OVERLAYS:
docs/FRESHNESS-POLICY.md
và các knowledge refresh docs
```

Quy tắc resolution:

```text
active lesson / mission question
→ CURRICULUM.md
→ ROADMAP + active part/mission docs
→ docs/SOURCE-MAPPING.md để truy provenance
→ historical/training/research source khi cần rationale
→ external verification cho current facts
```

Một historical identifier như `S:P/C/L` là provenance locator, **không phải active lesson ID mặc định**.

## Go-first engineering decision

Go vẫn là primary implementation language của active Bot track. Xem:

- [`../docs/ADR-001-GO-FIRST-BOT-STACK.md`](../docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`../CURRICULUM.md`](../CURRICULUM.md)

Các quyết định C#/.NET-first trong historical syllabus được giữ để truy lịch sử thiết kế, không phải current implementation instruction.

## Current knowledge overlay

Historical source không bị âm thầm sửa bằng web research. Các dữ kiện có thể thay đổi theo platform, luật, privacy, API, search, Go runtime hoặc AI/agent protocols được quản lý ở lớp current-state riêng.

Xem:

- [Freshness Policy](../docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](../docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [Bot Engineering Refresh 2026.08](../docs/BOT-ENGINEERING-REFRESH-2026.08.md)
- [Source-to-Roadmap Traceability Map](../docs/SOURCE-MAPPING.md)

Nguyên tắc cuối cùng:

> **History stays history. Active authority stays singular. Current facts stay verifiable.**
