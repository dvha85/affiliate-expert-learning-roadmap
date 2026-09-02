# Roadmap v2 — Reality-First Affiliate Intelligence Bot

> Active canonical: [CURRICULUM.md](CURRICULUM.md). Architecture authority:
> [ADR-004](docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md) and
> [ADR-005](docs/ADR-005-REALITY-FIRST-CURRICULUM.md).

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

`roadmap/part-00..06.md` continues to index the current 63 knowledge IDs. In
v2 those IDs are pulled on demand, not read sequentially. Their v1 wording is
being remapped before any v2 Mission becomes `ready`.

## Cách thực thi

```text
open the current Mission
→ attempt a small real/manual context
→ observe a concrete gap
→ pull at most three knowledge slices
→ improve/test
→ collect evidence and explain limits
```

## Chỉ mục Core

| Phần | Trọng tâm v2 | Chương | Bài | Missions | Trạng thái |
|---|---|---:|---:|---|---|
| [Phần 0](roadmap/part-00.md) | Reality trước: safe market loop | 0–2 | 9 | M00 | migration |
| [Phần 1](roadmap/part-01.md) | Outcome snapshot + deterministic baseline | 3–5 | 9 | M01–M02 | migration |
| [Phần 2](roadmap/part-02.md) | History/measurement + grounded advice | 6–8 | 9 | M03–M04 | migration |
| [Phần 3](roadmap/part-03.md) | Reviewed improvement | 9–11 | 9 | M05 | migration |
| [Phần 4](roadmap/part-04.md) | Reliable decisions | 12–14 | 9 | M06–M07 | planned |
| [Phần 5](roadmap/part-05.md) | Governed tools/actions | 15–17 | 9 | M08–M10 | planned |
| [Phần 6](roadmap/part-06.md) | Production closed loop | 18–20 | 9 | M11 | planned |

## Mission authority and delivery v2

| Mission | Product spine | Evidence | Authority | Delivery |
|---|---|---|---|---|
| M00 | first safe market loop | E2 | human_only; no Bot/AI publish | planned |
| M01 | first outcome snapshot | E3 | manual/read-only | planned |
| M02 | smallest deterministic Bot | E1 | A0 deterministic | planned |
| M03 | trustworthy history & measurement | E3 | A0 deterministic | planned |
| M04 | grounded AI advisor | E3 | A1 advisory, no tools/write | planned |
| M05 | first reviewed improvement | E4 | A1 propose only | planned |
| M06 | reliable watcher | E4 | A0 core + A1 triage | planned |
| M07 | decision + abstention | E4 | A1 advisory | planned |
| M08 | read-only evidence agent | E4 | A2-RO | planned |
| M09 | shadow action + approval | E4 | A3-shadow | planned |
| M10 | bounded governed canary | E5 | A3-limited | planned |
| M11 | production closed loop | E6 | A3-production | planned |

### Implementation profiles

```text
DETERMINISTIC CORE FIRST ≠ CODE FIRST
human/manual market loop first
→ no-code when auditable
→ code/profile only when its behavior needs it
→ AI never overrides evidence/policy/approval
```

Go is a v1 reference and a possible deterministic implementation profile for
M02+, not an M00 prerequisite. n8n/AgentRuntime may coordinate later but do
not own final truth, risk or authorization. Development Agent remains an
implementation helper under PR/CI/human review.

## Status vocabulary

- `planned` — canonical intent exists, no delivered Mission bundle;
- `draft` — authored but incomplete;
- `ready` — authoring complete, **not** a delivery/pilot claim;
- delivered — starter/eval/verification/pilot metadata complete; see
  `python scripts/report_readiness.py`.

The current v1 Mission projection and migration mapping are in
[missions/README.md](missions/README.md).
