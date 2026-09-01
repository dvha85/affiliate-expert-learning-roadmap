# Roadmap — Outcome-Driven Hybrid Core

> **Active canonical:** [`CURRICULUM.md`](CURRICULUM.md).
> Runtime architecture authority: [`docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md).
> File này là normalized index/checklist cho **7 Parts · 21 Chapters · 63 Core micro-lessons · 12 Missions · 1 evolving Affiliate Intelligence Bot**.

Hai syllabus trong `sources/` là historical research input. Chúng không còn quyết định learner sequence hiện hành.

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

## Learner execution

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

Roadmap không phải reading order. Framework capability cũng không tự nâng Bot authority.

## Hybrid architecture spine

Ba capability lane trưởng thành song song:

```text
DOMAIN / GOVERNANCE
= Go core
= evidence + history + deterministic decision + policy + audit

AUTOMATION / ORCHESTRATION
= n8n primary reference khi Mission justify
= trigger + integration + routing + approval + bounded execution

INTELLIGENCE / AGENT
= AgentRuntime
= analysis + research + tool-use theo permission
= Hermes Agent là primary reference/candidate từ tool-use stage
```

Rule bắt buộc:

```text
Go decides what is true / allowed.
Agent investigates / reasons / proposes.
n8n coordinates when / where / how workflows run.
```

## Core index

| Phần | Trọng tâm | Chương | Bài | Missions | Trạng thái |
|---|---|---:|---:|---|---|
| [Phần 0](roadmap/part-00.md) | First Evidence-Backed Decision | 0–2 | 9 | M00 | ⬜ |
| [Phần 1](roadmap/part-01.md) | Trustworthy Data & Grounded AI | 3–5 | 9 | M01–M02 | ⬜ |
| [Phần 2](roadmap/part-02.md) | First Tracked Market Loop | 6–8 | 9 | M03–M04 | ⬜ |
| [Phần 3](roadmap/part-03.md) | Outcome-Driven Improvement | 9–11 | 9 | M05 | ⬜ |
| [Phần 4](roadmap/part-04.md) | Reliable Intelligence & Orchestration | 12–14 | 9 | M06–M07 | ⬜ |
| [Phần 5](roadmap/part-05.md) | Tool Agent & Governed Automation | 15–17 | 9 | M08–M10 | ⬜ |
| [Phần 6](roadmap/part-06.md) | Hybrid Production Closed Loop | 18–20 | 9 | M11 | ⬜ |

## Mission spine + hybrid maturity

| Mission | Domain / Governance | Automation / Orchestration | Intelligence / Agent | Evidence |
|---|---|---|---|---|
| M00 | first deterministic evidence decision | manual/local | none | E1 |
| M01 | validated history/freshness | manual/local | none | E1 |
| M02 | grounded AI contract + fallback | none required | advisory, no tools | E1 |
| M03 | tracked Decision→Action boundary | human-only publish | optional advisory | E2 |
| M04 | analytics validation/reconciliation | **first read-only n8n learning slice** | optional advisory | E3 |
| M05 | experiment/evaluation/release decision | optional reporting/orchestration | advisory | E4 |
| M06 | signal/reliability contracts | **n8n primary watcher/orchestration reference** | optional triage | E4 |
| M07 | DecisionPacket + deterministic policy | route decisions | advisory | E4 |
| M08 | Tool Registry/policy/audit | invoke/route read-only tools | **read-only AgentRuntime** | E4 |
| M09 | ActionIntent + risk | **shadow + durable approval routing** | propose only | E4 |
| M10 | deterministic authorization | **bounded governed execution** | governed reasoning within permission | E5 |
| M11 | canonical state/policy/audit | production orchestration | production intelligence within authority ceiling | E6 |

Chi tiết mapping Mission↔Lesson và evidence gate nằm trong [`CURRICULUM.md`](CURRICULUM.md).

## Framework progression

### n8n

```text
M04 read-only import learning slice
→ M06 reliable orchestration
→ M09 approval/shadow workflow
→ M10 bounded execution
→ M11 production orchestration
```

n8n không giữ Product truth, scoring authority hay final policy authority.

### AgentRuntime

```text
M02 advisory / no tools
→ M08 read-only tools
→ M09 propose ActionIntent
→ M10 governed participation
→ M11 production intelligence within policy
```

Agent confidence không thay evidence và không thay execution permission.

## Quy tắc checkbox và PASS

- `[ ]` nghĩa là learner chưa chứng minh knowledge slice trong Mission context.
- `[x]` chỉ dùng khi có artifact/evidence và explain-back liên quan; chỉ đọc xong không đủ.
- Lesson file `planned` không được link như active authored lesson.
- Mission theo dõi riêng **Capability PASS**, **Reality verified** và **Operated**.
- Mission chỉ `DONE` khi cả ba chiều bắt buộc đạt.
- `0`, `missing`, `inconclusive` và `not_yet_observable` là bốn trạng thái khác nhau.
- n8n/Hermes/Agent framework không phải PASS shortcut.

## Milestone gates

| Gate | Missions | Demo outcome |
|---|---|---|
| G1 — First Evidence-Backed Decision | M00 | First running Bot + real observations + explainable decision |
| G2 — Trustworthy Intelligence | M01–M02 | History/provenance + deterministic baseline + grounded AI |
| G3 — First Market Learning Loop | M03–M05 | Tracked publication + real outcome + reviewed improvement + first safe orchestration exposure |
| G4 — Governed Hybrid Production Loop | M06–M11 | Reliable orchestration + governed Agent/tools/actions + production outcome loop |

## Technology references — không phải dependency cứng

- `n8n` — **primary orchestration reference**; first learning slice ở M04, production relevance tăng từ M06.
- `Hermes Agent` — **primary Agent runtime reference/candidate** cho read-only tool-use từ M08.

Chi tiết adoption/fallback/replaceability: [`docs/TECHNOLOGY-CANDIDATES.md`](docs/TECHNOLOGY-CANDIDATES.md).

## Advanced modules — ngoài Core/PASS

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

## Reference — không có PASS

Platform/legal/tax current facts, glossary, provider matrix, deployment recipes, security, technology references và troubleshooting checklists là reference. Nội dung biến động phải có source/freshness metadata.

## Quy ước trạng thái

- ⬜ Chưa bắt đầu
- 🟨 Đang attempt/build
- 🟦 Capability PASS, chờ Reality/Operate hoặc review
- ✅ Mission/Part PASS
- ⛔ Blocked, có blocker evidence

## Authority

```text
CURRICULUM.md
→ ROADMAP.md + roadmap/part-00..06.md
→ active Missions / Lessons
→ ADR/operating standards
→ historical/research sources
```

Curriculum migration: [`docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md`](docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md).
Runtime ownership: [`docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md).
