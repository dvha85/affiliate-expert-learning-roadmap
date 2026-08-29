# Roadmap — Outcome-Driven Core

> **Active canonical:** [`CURRICULUM.md`](CURRICULUM.md).
> File này là normalized index/checklist cho **7 Parts · 21 Chapters · 63 Core micro-lessons · 12 Missions · 1 evolving Bot**.

Hai syllabus trong `sources/` là historical research input. Chúng không còn quyết định Part, Chapter, Lesson, Project hoặc learner sequence hiện hành.

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

Roadmap không phải reading order. Learner không học hết Part trước khi build và không được dùng sample output để tuyên bố business validation.

## Core index

| Phần | Trọng tâm | Chương | Bài | Missions | Trạng thái |
|---|---|---:|---:|---|---|
| [Phần 0](roadmap/part-00.md) | First Evidence-Backed Decision | 0–2 | 9 | M00 | ⬜ |
| [Phần 1](roadmap/part-01.md) | Trustworthy Data & Grounded AI | 3–5 | 9 | M01–M02 | ⬜ |
| [Phần 2](roadmap/part-02.md) | First Tracked Market Loop | 6–8 | 9 | M03–M04 | ⬜ |
| [Phần 3](roadmap/part-03.md) | Outcome-Driven Improvement | 9–11 | 9 | M05 | ⬜ |
| [Phần 4](roadmap/part-04.md) | Reliable Intelligence & Decisions | 12–14 | 9 | M06–M07 | ⬜ |
| [Phần 5](roadmap/part-05.md) | Tool Agent & Governed Automation | 15–17 | 9 | M08–M10 | ⬜ |
| [Phần 6](roadmap/part-06.md) | Production Closed Loop | 18–20 | 9 | M11 | ⬜ |

## Mission spine

| Mission | Ship target | Required evidence level |
|---|---|---|
| M00 | First running Bot + public evidence + human-vs-Bot decision | E1 |
| M01 | Validated append-only history + freshness | E1 |
| M02 | Grounded AI Product Advisor có deterministic fallback | E1 |
| M03 | Một manual, compliant, tracked publication | E2 |
| M04 | Real outcome import + human-vs-AI comparison | E3 |
| M05 | Experiment + reviewed improvement hoặc documented rejection | E4 |
| M06 | Reliable automatic watcher qua retry/dedup/recovery cases | E4 |
| M07 | DecisionPacket + confidence/freshness/abstention + replay | E4 |
| M08 | Read-only evidence agent có permission/audit | E4 |
| M09 | Shadow ActionIntent + durable approval + dry-run | E4 |
| M10 | Limited governed RISK0/RISK1 canary; RISK2 approval | E5 |
| M11 | Production closed loop qua observation window | E6 |

Chi tiết mapping Mission↔Lesson và gate nằm trong [`CURRICULUM.md`](CURRICULUM.md).

## Quy tắc checkbox và PASS

- `[ ]` nghĩa là learner chưa chứng minh knowledge slice trong Mission context.
- `[x]` chỉ dùng khi có artifact/evidence và explain-back liên quan; chỉ đọc xong không đủ.
- Lesson file `planned` không được link như active authored lesson.
- File legacy tồn tại không tự động trở thành Core.
- Mission theo dõi riêng **Capability PASS**, **Reality verified** và **Operated**.
- Mission chỉ `DONE` khi cả ba chiều bắt buộc đạt.
- `0`, `missing`, `inconclusive` và `not_yet_observable` là bốn trạng thái khác nhau.

## Milestone gates

| Gate | Missions | Demo outcome |
|---|---|---|
| G1 — First Evidence-Backed Decision | M00 | First running Bot + real observations + explainable decision |
| G2 — Trustworthy Intelligence | M01–M02 | History/provenance + deterministic baseline + grounded AI |
| G3 — First Market Learning Loop | M03–M05 | Tracked publication + real outcome + reviewed improvement |
| G4 — Governed Production Loop | M06–M11 | Reliable decisions + governed tools/actions + production outcome loop |

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

Advanced module chỉ được mở sau khi có Core evidence và một use case/bottleneck thật. Advanced không tăng Core completion percentage và không thay Mission PASS.

## Reference — không có PASS

Platform/legal/tax current facts, glossary, cookbooks, schemas, provider matrix, deployment recipes, security và troubleshooting checklists là reference. Nội dung biến động phải có source và freshness metadata; không tạo thêm Core lesson chỉ để lưu current facts.

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
→ operating standards
→ historical/research sources
```

Quyết định migration được ghi tại [`docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md`](docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md).
