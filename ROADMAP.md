# Roadmap — Core Hybrid hướng outcome

> **Active canonical:** [`CURRICULUM.md`](CURRICULUM.md).
> **Architecture authority hiện hành:** [`docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md`](docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md).
> Runtime separation nền: [`docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md).
> File này là normalized index/checklist cho **7 Parts · 21 Chapters · 63 Core micro-lessons · 12 Missions · 1 evolving Affiliate Intelligence Bot**.

Hai syllabus trong `sources/` là historical research input. Chúng không còn quyết định learner sequence hiện hành.

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

## Cách người học thực thi

```text
Open current Mission
→ attempt before reading
→ run and observe a concrete gap
→ pull at most three micro-lessons
→ improve and test
→ collect technical + business evidence
→ explain back
→ ship the next Bot capability
```

Roadmap không phải reading order. Framework capability cũng không tự nâng Bot authority. **Số dòng code không phải thước đo PASS.**

## Trục kiến trúc Hybrid

Ba capability lane runtime trưởng thành song song:

```text
DOMAIN / GOVERNANCE
= Deterministic Domain/Governance Core
= evidence + history + deterministic decision + policy + audit contracts
= Go reference/fallback; visual rule engine có thể implement sau parity gate

AUTOMATION / ORCHESTRATION
= n8n primary reference khi Mission justify
= trigger + integration + routing + approval + bounded execution

INTELLIGENCE / AGENT
= AgentRuntime abstraction
= analysis + research + tool-use theo permission
= n8n AI Agent là visual-first candidate ở M08
= Hermes Agent / OpenAI Agents SDK là comparison khi có measured bottleneck
```

Development automation là lớp hỗ trợ ngang, **không phải runtime authority lane**:

```text
DEVELOPMENT AGENT
= Codex / GitHub Copilot cloud agent / Claude coding agent candidate
= issue/spec → code/tests/PR → CI → human review
= không tự cấp authority cho production Bot
```

Rule bắt buộc:

```text
Deterministic Core decides what is true / allowed.
Agent investigates / reasons / proposes.
n8n coordinates when / where / how workflows run.
Development Agent implements changes under PR/CI/review.
```

Implementation principle:

```text
DETERMINISTIC CORE FIRST
≠ CODE FIRST

NO-CODE WHEN IT IS AUDITABLE
AGENT-WRITTEN CODE WHEN CODE IS NECESSARY
```

Chiến lược implementation chi tiết: [`docs/IMPLEMENTATION-STRATEGY.md`](docs/IMPLEMENTATION-STRATEGY.md).

## Chỉ mục Core

| Phần | Trọng tâm | Chương | Bài | Missions | Trạng thái |
|---|---|---:|---:|---|---|
| [Phần 0](roadmap/part-00.md) | Quyết định đầu tiên dựa trên bằng chứng | 0–2 | 9 | M00 | ⬜ |
| [Phần 1](roadmap/part-01.md) | Dữ liệu đáng tin và AI có grounding | 3–5 | 9 | M01–M02 | ⬜ |
| [Phần 2](roadmap/part-02.md) | Vòng thị trường có tracking đầu tiên | 6–8 | 9 | M03–M04 | ⬜ |
| [Phần 3](roadmap/part-03.md) | Cải tiến dựa trên outcome | 9–11 | 9 | M05 | ⬜ |
| [Phần 4](roadmap/part-04.md) | Intelligence đáng tin và orchestration | 12–14 | 9 | M06–M07 | ⬜ |
| [Phần 5](roadmap/part-05.md) | Tool Agent và tự động hóa có quản trị | 15–17 | 9 | M08–M10 | ⬜ |
| [Phần 6](roadmap/part-06.md) | Vòng production Hybrid khép kín | 18–20 | 9 | M11 | ⬜ |

## Trục Mission và mức trưởng thành Hybrid

| Mission | Domain / Governance | Automation / Orchestration | Intelligence / Agent | Evidence |
|---|---|---|---|---|
| M00 | **Go starter = golden oracle** cho first deterministic evidence decision | manual/local | none | E1 |
| M01 | validated history/freshness; implementation nhỏ nhất audit được | manual/local | none | E1 |
| M02 | grounded AI contract + deterministic fallback | none required | advisory, no tools | E1 |
| M03 | tracked Decision→Action boundary | human-only publish | optional advisory | E2 |
| M04 | analytics validation/reconciliation contract | **first read-only n8n learning slice** | optional advisory | E3 |
| M05 | experiment/evaluation/release decision | optional reporting/orchestration | advisory | E4 |
| M06 | signal/reliability contracts; không tự viết scheduler nếu n8n đủ | **n8n primary watcher/orchestration reference** | optional triage | E4 |
| M07 | DecisionPacket + deterministic policy; **first meaningful visual-rule comparison** | route decisions | advisory | E4 |
| M08 | Tool Registry/policy/audit contracts | invoke/route read-only tools | **read-only AgentRuntime; n8n AI Agent visual-first candidate** | E4 |
| M09 | ActionIntent + deterministic risk; visual rule engine có thể adopt nếu parity/fail-closed PASS | **shadow + durable approval routing** | propose only | E4 |
| M10 | deterministic authorization implementation-flexible | **bounded governed execution** | governed reasoning within permission | E5 |
| M11 | canonical state/policy/audit contracts; vendor/language replaceable | production orchestration | production intelligence within authority ceiling | E6 |

Chi tiết mapping Mission↔Lesson và evidence gate nằm trong [`CURRICULUM.md`](CURRICULUM.md).

## Tiến triển implementation và framework

### Deterministic Core

```text
M00 Go golden oracle/reference
→ M01–M06 giữ implementation đơn giản nhất audit được
→ M07 compare visual rule engine trên cùng fixtures/contracts
→ M09–M10 adopt rule engine nếu parity + versioning + fail-closed PASS
→ Go vẫn là reference/fallback khi visual rule không còn rõ hoặc đủ an toàn
```

DecisionRules là visual deterministic rule-engine candidate hiện tại; **không mandatory** và không rewrite M00 chỉ vì tool tồn tại.

### n8n

```text
M04 read-only import learning slice
→ M06 reliable orchestration
→ M08 visual-first AI Agent candidate for read-only tool use
→ M09 approval/shadow workflow
→ M10 bounded execution
→ M11 production orchestration
```

n8n không giữ Product truth hoặc tự nâng workflow branch thành final policy authority. Nó có thể gọi **deterministic authority implementation hiện hành** thay vì bắt buộc gọi Go.

### AgentRuntime

```text
M02 advisory / no tools
→ M08 n8n AI Agent visual-first comparison
→ Hermes/OpenAI Agents SDK only if a measured bottleneck justifies another runtime
→ M09 propose ActionIntent
→ M10 governed participation
→ M11 production intelligence within policy
```

Agent confidence không thay evidence và không thay execution permission. Flowise chỉ ở watchlist/comparison khi n8n Agent graph thật sự khó maintain; không thêm runtime thứ hai chỉ vì feature list hấp dẫn.

### Development Agent

```text
issue/spec
→ coding agent implements/refactors/tests
→ pull request
→ repository CI/security checks
→ human review
→ merge/reject
```

Candidate hiện hành: GitHub Copilot cloud agent, OpenAI Codex coding agent, Anthropic Claude coding agent. Development Agent có thể xuất hiện sớm hơn runtime Agent vì nó **không phải Bot authority**.

## Quy tắc checkbox và PASS

- `[ ]` nghĩa là learner chưa chứng minh knowledge slice trong Mission context.
- `[x]` chỉ dùng khi có artifact/evidence và explain-back liên quan; chỉ đọc xong không đủ.
- Lesson file `planned` không được link như active authored lesson.
- Mission theo dõi riêng **Capability PASS**, **Reality verified** và **Operated**.
- Mission chỉ `DONE` khi cả ba chiều bắt buộc đạt.
- `0`, `missing`, `inconclusive` và `not_yet_observable` là bốn trạng thái khác nhau.
- n8n/Hermes/DecisionRules/Development Agent không phải PASS shortcut.
- learner phải review/giải thích behavior quan trọng dù implementation do visual tool hoặc coding agent tạo.

## Các cổng milestone

| Gate | Missions | Demo outcome |
|---|---|---|
| G1 — First Evidence-Backed Decision | M00 | First running Bot + real observations + explainable decision |
| G2 — Trustworthy Intelligence | M01–M02 | History/provenance + deterministic baseline + grounded AI |
| G3 — First Market Learning Loop | M03–M05 | Tracked publication + real outcome + reviewed improvement + first safe orchestration exposure |
| G4 — Governed Hybrid Production Loop | M06–M11 | Reliable orchestration + deterministic governance + governed Agent/tools/actions + production outcome loop |

## Tài liệu tham chiếu công nghệ — không phải dependency cứng

- `Go` — **deterministic core reference/fallback implementation**, đặc biệt là M00 golden oracle.
- `DecisionRules` — **visual deterministic rule-engine candidate**; comparison từ M07, adopt chỉ sau parity/fail-closed gate.
- `n8n` — **primary orchestration reference** và **visual-first AgentRuntime candidate ở M08**; production relevance tăng từ M06.
- `Hermes Agent / OpenAI Agents SDK` — **AgentRuntime comparison candidates** khi n8n AI Agent baseline lộ bottleneck đo được.
- `Flowise` — watchlist/comparison only, không thêm trước khi cần.
- `GitHub Copilot cloud agent / OpenAI Codex / Anthropic Claude` — **Development Agent candidates** cho issue→PR workflow; không phải runtime authority.

Chi tiết adoption/fallback/replaceability: [`docs/TECHNOLOGY-CANDIDATES.md`](docs/TECHNOLOGY-CANDIDATES.md).

## Module nâng cao — ngoài Core/PASS

| ID | Module |
|---|---|
| A01 | Platform-specific APIs và production adapters |
| A02 | Server-side tracking, webhook và identity resolution |
| A03 | Data warehouse, dashboard và BI nâng cao |
| A04 | Advanced experimentation và statistical power |
| A05 | Time-series, anomaly detection và forecasting |
| A06 | Machine Learning và Learning-to-Rank |
| A07 | Explore–Exploit và Multi-Armed Bandit |
| A08 | RAG, embeddings và vector retrieval |
| A09 | MCP, A2A và multi-agent orchestration |
| A10 | Distributed workflows và high-scale operations |
| A11 | Paid traffic và multi-channel portfolio optimization |
| A12 | SaaS productization, multi-tenancy và billing |

Advanced module chỉ được mở sau khi có Core evidence và một use case/bottleneck thật.

## Tài liệu tham chiếu — không có PASS

Platform/legal/tax current facts, glossary, provider matrix, deployment recipes, security, technology references và troubleshooting checklists là reference. Nội dung biến động phải có source/freshness metadata.

## Quy ước trạng thái

- ⬜ Chưa bắt đầu
- 🟨 Đang attempt/build
- 🟦 Capability PASS, chờ Reality/Operate hoặc review
- ✅ Mission/Part PASS
- ⛔ Blocked, có blocker evidence

## Thứ tự authority

```text
CURRICULUM.md
→ ROADMAP.md + roadmap/part-00..06.md
→ active Missions / Lessons
→ ADR-004 + operating standards
→ ADR-003 runtime-separation history
→ historical/research sources
```

Curriculum migration: [`docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md`](docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md).
Current architecture: [`docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md`](docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md).
Runtime separation baseline: [`docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md).
