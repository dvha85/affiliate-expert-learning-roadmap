# Affiliate Expert Learning Roadmap

**Structured, evidence-based curriculum for becoming an Affiliate Expert + Affiliate Bot Engineer → Affiliate Intelligence Expert.**

```text
Affiliate Expert
+
Affiliate Bot Engineer
=
Affiliate Intelligence Expert
```

## Trạng thái hiện tại

- **Active canonical:** `sources/SYLLABUS-v2026.09.md`
- **Historical structural baseline:** `sources/SYLLABUS-v2026.08.md`
- **Primary Bot Engineering language:** **Go**
- **Default timeline:** 15 tháng, khoảng 9 giờ/tuần
- **Accelerated:** 12 tháng, khoảng 11–12 giờ/tuần
- **Structure:** 23 Parts · 89 Chapters · 671 lessons · 14 main projects
- **0.1 — Affiliate Expert là gì?**: `ready`, general lesson reference
- **0.2 — Affiliate Bot Engineer là gì?**: `ready`, Go-first Bot Engineer/autonomy reference
- **0.3 trở đi:** chưa được coi là authored nếu chưa có file `draft|ready` đúng lifecycle

`ready` là trạng thái biên soạn, **không phải learner PASS**. Checkbox `[x]` chỉ dùng khi người học đạt đủ PASS evidence.

## Go-first Bot Engineering

Từ v2026.09, active engineering spine là:

```text
Go
→ Services / Workers
→ Collectors & Adapters
→ PostgreSQL / optional Redis
→ Queue / Workflow
→ Durable Execution when required
→ Analytics / Decision Engine
→ Tool Boundary / MCP
→ AI Agent where justified
→ Policy & Risk Engine
→ Human Approval Queue
→ Action Executor
→ Audit / Tracing / Feedback
```

C#/.NET vẫn tồn tại trong historical v2026.08 và có thể dùng làm comparison/reference stack, nhưng không còn là primary implementation path.

Đọc:

- [ADR — Go-first Bot Stack](docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [Go Bot Engineering Stack](docs/GO-BOT-ENGINEERING-STACK.md)
- [Autonomy & Approval Model](docs/AUTONOMY-AND-APPROVAL-MODEL.md)
- [Agent Security & Tool Governance](docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md)
- [Bot Engineering Refresh 2026.08](docs/BOT-ENGINEERING-REFRESH-2026.08.md)

### Autonomy model

```text
RISK 0
→ auto execute

RISK 1
→ auto execute + mandatory audit

RISK 2
→ persist state
→ pause
→ human approve/reject
→ revalidate
→ resume or terminate
```

Mục tiêu là để người vận hành **duyệt quyết định consequential**, không babysit từng bước cơ học của bot.

## Architecture principles

```text
modular monolith first
+ deterministic logic before LLM autonomy
+ context/cancellation
+ bounded concurrency
+ retry + idempotency
+ durable state for long waits
+ explicit tool contracts
+ least privilege
+ policy/risk boundary
+ human approval
+ audit/tracing/evaluation
+ kill switch
```

Không chọn Go chỉ vì benchmark CPU. Affiliate Bot chủ yếu bị chi phối bởi API/network/database/LLM/rate limits; Go được chọn vì concurrency, deployment simplicity, resource footprint và operational simplicity phù hợp hệ thống chạy lâu dài.

## Current-knowledge layer

Canonical curriculum và current operating facts được tách riêng:

```text
STABLE/VERSIONED CANONICAL
+
VERIFIED CURRENT FACTS
+
CONTINUOUS WATCH
=
AFFILIATE INTELLIGENCE CURRICULUM
```

Current source registers:

- [Freshness Policy](docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [Bot Engineering Refresh 2026.08](docs/BOT-ENGINEERING-REFRESH-2026.08.md)

Exact Go/runtime/SDK/protocol/platform/legal facts phải được re-verify theo freshness policy; không biến version hiện tại thành permanent curriculum truth.

## Source model

```text
ACTIVE CANONICAL:
sources/SYLLABUS-v2026.09.md

INHERITED STRUCTURAL BASELINE:
sources/SYLLABUS-v2026.08.md

PACING:
docs/15-MONTH-PLAN.md / docs/12-MONTH-PLAN.md

EXECUTION:
docs/EXECUTION-MODEL.md

SUPPLEMENTS:
sources/Noi-dung-dao-tao.txt
sources/Nghien-cuu.txt

CURRENT FACTS:
external source registers + last_verified
```

`S:P/C/L` source refs remain version-neutral identifiers. `sources/README.md` resolves which canonical revision is active.

Đọc:

- [Source README](sources/README.md)
- [Source Mapping](docs/SOURCE-MAPPING.md)
- [Freshness Policy](docs/FRESHNESS-POLICY.md)

## Bắt đầu học

1. Mở [ROADMAP.md](ROADMAP.md).
2. Chọn [15-month Standard](docs/15-MONTH-PLAN.md) hoặc [12-month Accelerated](docs/12-MONTH-PLAN.md).
3. Đọc [Hybrid Execution Model](docs/EXECUTION-MODEL.md).
4. Học [`0.1 — Affiliate Expert là gì?`](lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md).
5. Học [`0.2 — Affiliate Bot Engineer là gì?`](lessons/part-00/chapter-00/0.2-affiliate-bot-engineer-la-gi.md) và làm boundary-map artifact.
6. Chỉ tick `[x]` sau khi đạt đủ [5 tiêu chí PASS](docs/PASS-CRITERIA.md).
7. Lưu evidence theo [Artifact conventions](artifacts/README.md).
8. Review và cập nhật [PROGRESS.md](PROGRESS.md).

## Learning operating system

Mỗi lesson `ready` phải hỗ trợ:

```text
Concept
+
Example / Case
+
Quiz ≥80%
+
Practice Artifact
+
Explain-back
```

Authoring/evidence resources:

- [Lesson Template](templates/LESSON.md)
- [Lesson Notes](templates/LESSON-NOTES.md)
- [Lesson Authoring Standard](docs/LESSON-AUTHORING-STANDARD.md)
- [Experiment Log](templates/EXPERIMENT-LOG.md)
- [Revenue Journal](templates/REVENUE-JOURNAL.md)
- [Knowledge Entry](templates/KNOWLEDGE-ENTRY.md)
- [Project README Template](templates/PROJECT-README.md)
- [Retrospective](templates/RETROSPECTIVE.md)

## Lesson lifecycle

```text
scaffold
→ planned
→ draft
→ ready
→ learner evidence
→ PASS / RETRY
```

- `planned`: file có thể tồn tại nhưng chưa link từ roadmap;
- `draft|ready`: phải link từ roadmap;
- `[x]`: learner PASS only.

Reference implementations:

- [0.1 — Affiliate Expert là gì?](lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md) — general Affiliate Expert reference.
- [0.2 — Affiliate Bot Engineer là gì?](lessons/part-00/chapter-00/0.2-affiliate-bot-engineer-la-gi.md) — Go-first Bot Engineer/governed-autonomy reference.

## Lesson scaffolding

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --effort M --minutes 75 --prerequisite 0.1 --dry-run
```

0.2 đã tồn tại và `ready`, nên dry-run chỉ báo `EXISTS ... would not overwrite`; actual write vẫn từ chối overwrite.

Xem [Lesson Scaffolding Guide](docs/LESSON-SCAFFOLDING.md).

## Curriculum CI

```bash
python scripts/validate_curriculum.py
python -m unittest discover -s tests -v
```

CI bảo vệ:

- active canonical v2026.09 + historical v2026.08;
- Go-first primary Part 15;
- 23/89/671 structural counts;
- Part/Chapter/Lesson IDs;
- timeline contract;
- links;
- lesson metadata;
- freshness refs ↔ `last_verified`;
- lifecycle `planned|draft|ready`;
- heading hierarchy;
- scaffolder overwrite behavior.

Xem [Curriculum CI](docs/CURRICULUM-CI.md).

## Timeline contract

Per-Part files dùng:

```text
- Timeline: **Standard ... · Accelerated ...** — forecast; PASS evidence mới là gate.
```

Part 20 là conditional; Part 22 là post-core continuous.

Timeline là forecast, không phải định nghĩa Expert.

## Core principles

```text
LEARN → EXPLAIN → APPLY → TEST → PASS
UNDERSTAND → DECIDE → EXECUTE → MEASURE → LEARN → IMPROVE
```

- DATA > OPINION.
- EXPECTED VALUE > COMMISSION RATE.
- Không automate thứ chưa hiểu bằng tay.
- Không optimize trước khi đo.
- Deterministic logic trước LLM autonomy.
- Decision ≠ Execution.
- Model output là untrusted input.
- High-risk action cần deterministic policy + human approval.
- AI/agent capability không loại bỏ accountability/compliance.

## Contributing

Repo dùng mô hình **issue-first**. Đọc [CONTRIBUTING.md](CONTRIBUTING.md) trước thay đổi curriculum hoặc engineering direction.

## Licensing

Repository public nhưng **không phát hành theo open-source license**. Xem [Licensing Status](docs/LICENSING.md).

## Tài liệu chính

- [Roadmap](ROADMAP.md)
- [Active Canonical v2026.09](sources/SYLLABUS-v2026.09.md)
- [ADR Go-first](docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [Go Bot Engineering Stack](docs/GO-BOT-ENGINEERING-STACK.md)
- [Autonomy & Approval](docs/AUTONOMY-AND-APPROVAL-MODEL.md)
- [Agent Security & Tool Governance](docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md)
- [Bot Engineering Refresh](docs/BOT-ENGINEERING-REFRESH-2026.08.md)
- [15-Month Standard](docs/15-MONTH-PLAN.md)
- [12-Month Accelerated](docs/12-MONTH-PLAN.md)
- [Execution Model](docs/EXECUTION-MODEL.md)
- [Source Mapping](docs/SOURCE-MAPPING.md)
- [Freshness Policy](docs/FRESHNESS-POLICY.md)
- [Curriculum CI](docs/CURRICULUM-CI.md)
- [PASS Criteria](docs/PASS-CRITERIA.md)
- [Projects](docs/PROJECTS.md)
