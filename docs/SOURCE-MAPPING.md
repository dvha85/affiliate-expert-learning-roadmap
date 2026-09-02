# Source-to-Curriculum Traceability Map

> Mục tiêu: mọi active Core micro-lesson truy ngược được về curriculum outcome, Mission cần nó, historical research đã tham khảo và current external fact đã kiểm chứng — mà không biến nguồn lịch sử thành authority.

## 1. Authority precedence

Khi tài liệu mâu thuẫn, resolve theo thứ tự:

1. [`../CURRICULUM.md`](../CURRICULUM.md) — active canonical outcome, Core structure, Mission spine và PASS boundary;
2. [`../ROADMAP.md`](../ROADMAP.md) cùng `roadmap/part-00.md` đến `part-06.md` — normalized checklist/index;
3. active Mission và lesson files — execution detail;
4. operating standards trong `docs/` — safety, evidence và engineering contracts;
5. `sources/` — historical/research input, không phải active implementation authority;
6. external primary sources — current facts, luôn đi qua [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md).

```text
ACTIVE SCOPE: CURRICULUM > ROADMAP > MISSION/LESSON
OPERATING BOUNDARY: active docs, không được override curriculum outcome
HISTORICAL CONTEXT: S / T / R, chỉ supplement/provenance
CURRENT FACTS: EXT refs + verified date + volatility
```

Current Core gồm 7 Parts, 21 Chapters và 63 micro-lessons trên Mission spine `M00–M11`. Đây là inventory hiện tại, không phải số lượng phải bảo vệ trước learner evidence.

## V2 sequence overlay

The detailed Part/Mission tables below preserve v1 source lineage. They are not
the active sequence. V2 routes existing knowledge inventory through:

```text
M00 human safe market loop
→ M01 outcome snapshot ∥ M02 deterministic baseline
→ M03 history/measurement → M04 grounded AI → M05 reviewed improvement
→ M06–M11 governed production
```

Mapping is explicit in [`CURRICULUM-MIGRATION-v2.md`](CURRICULUM-MIGRATION-v2.md).
When authoring a v2 Mission, cite active outcome/evidence need first, then add
historical IDs only as provenance; do not inherit v1 sequence from a lesson ID.

## 2. Source roles

### Active curriculum

- **`CUR`** — `CURRICULUM.md`: mục tiêu và boundary có authority.
- **`RM`** — active roadmap Part/Chapter/Lesson index.
- **`M`** — Mission attempt, artifact, Capability PASS, Reality verified và Operated.

Active lesson identity được xác định bằng lesson ID trong active roadmap và file path tương ứng. Một historical source ref không thể tự làm một lesson trở thành Core.

### Historical research

- **`S`** — `sources/SYLLABUS-v2026.08.md` và `sources/SYLLABUS-v2026.09.md`.
- **`T`** — `sources/Noi-dung-dao-tao.txt`.
- **`R`** — `sources/Nghien-cuu.txt`.

Các nguồn này bảo toàn provenance, terminology và coverage ideas. Chúng không quyết định active count, sequence, technology stack hay PASS gate.

Historical IDs vẫn dùng dạng:

```text
S:P{part}/C{chapter}/L{lesson}
T:G{giai_doan}/W{week}
R:{named section}
```

Active lesson dùng `source_refs.active` với namespace `CUR:`. Historical lineage nếu thật sự có đóng góp dùng `source_refs.historical` hoặc các nhóm `training`/`research`; không được đặt `S:` dưới nhãn canonical.

### External/current sources

Current facts dùng stable `EXT:` ID và verified date, ví dụ:

```text
EXT:TIKTOK:PPS
EXT:GO:RELEASES
EXT:MCP:SDK
EXT:TEMPORAL:GO-SDK
```

Registers:

- [Affiliate Knowledge Refresh](AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [Bot Engineering Refresh](BOT-ENGINEERING-REFRESH-2026.08.md)

## 3. Conflict rules

- Active scope/title/sequence/PASS: `CUR` và active roadmap thắng mọi historical source.
- Mission execution: Mission file phải tuân `CUR`; docs không được nới Reality gate hoặc authority ceiling.
- Historical sources khác nhau: ghi rõ nguồn nào nói gì; không dùng inheritance để tạo active requirement mới.
- Timeline/effort: dùng learner actuals và current plan; historical week/month chỉ là context.
- Platform/legal/tax/API/runtime/provider fact: external primary source + freshness thắng historical wording.
- Source không có counterpart: ghi `—`; không suy đoán mapping.
- Mapping tương đồng một phần: ghi `partial` và chỉ dùng phần thực sự hỗ trợ claim.
- Một current vendor capability không tự trở thành Core lesson.

Go-first architecture rationale lịch sử được giữ tại [`ADR-001-GO-FIRST-BOT-STACK.md`](ADR-001-GO-FIRST-BOT-STACK.md). Active learning sequence và outcome-driven redesign nằm tại [`ADR-002-OUTCOME-DRIVEN-CURRICULUM.md`](ADR-002-OUTCOME-DRIVEN-CURRICULUM.md).

## 4. Traceability contract cho active lesson

Một lesson cần resolve được bốn câu hỏi:

1. Lesson phục vụ outcome nào trong `CURRICULUM.md`?
2. Mission nào làm lộ nhu cầu học nó?
3. Learner áp dụng nó vào artifact/evidence nào ngay sau khi pull?
4. Claim volatile nào cần external ref và `last_verified`?

Metadata tối thiểu:

```yaml
lesson_id: "0.1"
part: 0
chapter: 0
track: core
mission_refs: ["M00"]
practice_first: true
source_refs:
  active:
    - "CUR:P0/C0/L0.1"
  historical: [] # chỉ thêm S:/T:/R: khi nội dung thực sự được dùng
  training: []
  research: []
  external: []
last_verified: null
```

Rules:

- `lesson_id`, `part`, `chapter`, `track` và `mission_refs` phải khớp active roadmap/CURRICULUM;
- `practice_first: true` phải thể hiện bằng Try/Observe trước explanation dài;
- historical refs chỉ thêm khi nội dung thực sự được dùng; không cần ép 1:1;
- nếu lesson được thiết kế mới từ learner need, historical refs có thể rỗng theo migration contract tương lai;
- external ref không rỗng thì cần `last_verified` và source-ID resolution;
- source ref không thay citation/evidence cho claim cụ thể;
- không quá ba Core micro-lessons liên tiếp trước khi learner quay lại Mission attempt.

## 5. V1 baseline Part và Mission map

| Part | Chapters | Lessons | Mission | Capability outcome |
|---|---:|---:|---|---|
| P0 — First Evidence-Backed Decision | C0–C2 | 9 | M00 | running Bot + public evidence + human-vs-Bot decision |
| P1 — Trustworthy Data & Grounded AI | C3–C5 | 9 | M01–M02 | immutable history + grounded advisory/fallback |
| P2 — First Tracked Market Loop | C6–C8 | 9 | M03–M04 | manual tracked publish + real outcome comparison |
| P3 — Outcome-Driven Improvement | C9–C11 | 9 | M05 | hypothesis → outcome → reviewed change |
| P4 — Reliable Intelligence & Decisions | C12–C14 | 9 | M06–M07 | reliable watcher + traceable decision/abstention |
| P5 — Tool Agent & Governed Automation | C15–C17 | 9 | M08–M10 | read-only agent → shadow approval → bounded canary |
| P6 — Production Closed Loop | C18–C20 | 9 | M11 | deploy/recover/learn without silent self-modification |

## 6. Chapter-level historical traceability — 21 active Chapters

Historical refs trong bảng là research leads, không phải inherited requirements.

### P0 — First Evidence-Backed Decision

| Chapter | Active scope | Historical leads | Mission / evidence |
|---|---|---|---|
| C0 — Bot đầu tiên và evidence discipline | edit-run-test, sample-vs-real, failure/evidence/explain-back | `S:P0/C0` + `S:P15/C50-51`; `T:G0/W0` | M00 / E0→E1 |
| C1 — Quan sát Affiliate thật đầu tiên | product observation, money flow, provenance/freshness | `S:P1/C1-3` + `S:P8/C23-24`; `T:G1/W1-2` | M00 / E1 |
| C2 — Human-vs-Bot decision đầu tiên | human rank, EV/naive baseline, confidence/abstain | `S:P2/C4-6` + `S:P8/C27` + `S:P16/C57-60`; `R:Opportunity Score` | M00 / G1 |

### P1 — Trustworthy Data & Grounded AI

| Chapter | Active scope | Historical leads | Mission / evidence |
|---|---|---|---|
| C3 — Minimal trustworthy ingest | struct/JSON, validation, adapter/provenance | `S:P12/C38-40` + `S:P15/C52`; `R:Technology stack` | M01 / real snapshot |
| C4 — History và change observation | append-only history, delta, second observation/restart | `S:P12/C39` + `S:P15/C53-55`; `R:Product Intelligence history` | M01 / second snapshot |
| C5 — Grounded AI advisory | deterministic-vs-AI choice, structured grounding, eval/fallback | `S:P17/C61-65`; `T:G8/W34-37` | M02 / G2 |

### P2 — First Tracked Market Loop

| Chapter | Active scope | Historical leads | Mission / evidence |
|---|---|---|---|
| C6 — Compliant micro-content | audience/claim, disclosure, human review/publish | `S:P4/C10-12` + `S:P9/C28-32`; `R:manual publish` | M03 / E2 |
| C7 — Tracking và real outcome import | tracking link, observation window, import/reconcile | `S:P3/C7-9` + `S:P12/C41`; `T:G1/W3` | M03–M04 / E2–E3 |
| C8 — Human-vs-AI outcome comparison | baseline, segmentation, missing-vs-zero, decision linkage | `S:P13/C42-44` + `S:P17/C65`; `R:feedback loop` | M04 / E3 |

### P3 — Outcome-Driven Improvement

| Chapter | Active scope | Historical leads | Mission / evidence |
|---|---|---|---|
| C9 — Hypothesis từ outcome | question, metric, weakest assumption | `S:P14/C46`; `R:feedback loop` | M05 / E4 |
| C10 — Experiment nhỏ và honest inference | variant, window, inconclusive, stopping guard | `S:P14/C47-49`; `T:G9/W39-42` | M05 / E4 |
| C11 — Controlled improvement | Decision/Outcome memory, proposed change, test/review/rollback | `S:P16/C60` + `S:P19/C73-77`; `R:knowledge feedback` | M05 / G3 |

### P4 — Reliable Intelligence & Decisions

| Chapter | Active scope | Historical leads | Mission / evidence |
|---|---|---|---|
| C12 — Reliable automatic watcher | event/change, retry/backoff, idempotency, recovery | `S:P15/C53-56`; `R:Product Intelligence alert` | M06 / operational evidence |
| C13 — Signal-to-decision contracts | Signal/Analysis/Decision packets, fusion, expiry | `S:P16/C57-60` + `S:P17/C65`; `R:Affiliate Intelligence actions` | M07 / trace |
| C14 — Confidence, abstention và evaluation | calibration, stale/missing/conflict, eval dataset | `S:P17/C65-66`; `T:G8/W34` | M07 / decision cases |

### P5 — Tool Agent & Governed Automation

| Chapter | Active scope | Historical leads | Mission / evidence |
|---|---|---|---|
| C15 — Read-only evidence agent | tool schema/registry, least privilege, audit, prompt injection | `S:P17/C61,65` + `S:P19/C75-76`; `R:AI layer` | M08 / read-only trace |
| C16 — ActionIntent, policy và durable approval | decision≠execution, risk, expiry, revalidation | `S:P17/C66` + `S:P19/C74-76`; `R:human review` | M09 / shadow record |
| C17 — Bounded governed canary | idempotent executor, RISK0/1, RISK2 approval, kill switch | `S:P19/C73-77`; `R:automation stages` | M10 / E5 |

### P6 — Production Closed Loop

| Chapter | Active scope | Historical leads | Mission / evidence |
|---|---|---|---|
| C18 — Deploy và observe | config/secrets, release, metrics/traces/logs, cost | `S:P19/C73,77`; `T:G11/W47-48` | M11 / production run |
| C19 — Recover và secure | durable state, restore/replay, incident/kill-switch drill | `S:P19/C74-76`; `R:Technology stack` | M11 / recovery evidence |
| C20 — Outcome learning loop | evaluation, proposed improvement, controlled release | `S:P13/C42-44` + `S:P14/C46-49` + `S:P21/C83-84`; `R:feedback loop` | M11 / E6 + G4 |

## 7. Mission và Real Evidence mapping

| Mission | Required evidence | Milestone |
|---|---|---|
| M00 | E1 public observations + human rank trước Bot | G1 |
| M01 | real snapshots/history, no overwrite | G2 |
| M02 | grounded AI cases + deterministic fallback | G2 |
| M03 | E2 manual compliant tracked publication | G3 |
| M04 | E3 real analytics/export; missing khác zero | G3 |
| M05 | E4 Decision→Action→Outcome→reviewed change | G3 |
| M06 | retry/duplicate/recovery operating evidence | G4 |
| M07 | stale/missing/conflicting decision cases | G4 |
| M08 | read-only tool permission/audit trace | G4 |
| M09 | shadow ActionIntent + durable approval/rejection | G4 |
| M10 | E5 bounded governed canary + kill switch | G4 |
| M11 | E6 production loop + recovery + outcome review | G4 |

Four Milestone Gates là integration checkpoints trên một evolving Bot, không phải nhiều project rời.

## 8. Advanced và Reference mapping

Advanced modules giữ breadth có giá trị từ historical inventory nhưng không trở thành Core prerequisite:

| Advanced | Historical research leads |
|---|---|
| A01 Platform APIs/adapters | `S:P5/C13-16`, `S:P15/C52` |
| A02 Server-side tracking/webhook/identity | `S:P3/C7-9` |
| A03 Warehouse/dashboard/BI | `S:P12/C38-41`, `S:P13/C42-45` |
| A04 Advanced experimentation/statistical power | `S:P14/C46-49` |
| A05 Time-series/anomaly/forecasting | `S:P18/C67-69` |
| A06 ML/Learning-to-Rank | `S:P18/C70-71` |
| A07 Explore–Exploit/Bandit | `S:P18/C72` |
| A08 RAG/embeddings/vector retrieval | `S:P17/C64` |
| A09 MCP/A2A/multi-agent | `S:P17/C61,66`, `S:P22/C87` |
| A10 Distributed/high-scale workflows | `S:P19/C73-74` |
| A11 Paid traffic/portfolio | `S:P10/C33-35`, `S:P20/C79,81` |
| A12 SaaS/multi-tenancy/billing | `S:P20/C82` |

Reference cards/cookbooks có thể dùng historical source để giải thích sâu, nhưng không có lesson checkbox và không tạo Mission gate mới.

## 9. Audit notes

- Active coverage: 7/7 Parts, 21/21 Chapters và 63/63 Core micro-lessons trong roadmap.
- Active Mission coverage: `M00–M11`.
- Milestone coverage: G1–G4.
- Historical mapping là many-to-many và có thể `partial`; không còn rule kế thừa syllabus cũ.
- Source ID compatibility được giữ để lesson đã author không mất provenance.
- `—` nghĩa là không có direct counterpart; đó không phải lỗi nếu active lesson được tạo từ Mission need và có evidence contract rõ.

## 10. Authoring rule

Khi tạo hoặc rewrite lesson:

1. resolve outcome/ID/Mission từ `CURRICULUM.md` và active roadmap;
2. bắt đầu từ Mission attempt và gap learner sẽ quan sát;
3. đọc đúng historical lead trong bảng nếu nó thực sự hỗ trợ scope;
4. chỉ thêm refs đã dùng, ghi `partial` khi cần;
5. external-verify mọi current claim và thêm `last_verified`;
6. đưa learner quay lại build/run/measure trong tối đa ba micro-lessons;
7. yêu cầu artifact/evidence áp dụng ngay và failure path;
8. không nâng sample thành real evidence, không hứa outcome dương;
9. nếu learner pilot cho thấy lesson thừa/quá dài/sai thời điểm, merge/rewrite/remove thay vì giữ inventory.

Traceability tốt trả lời được: **vì sao learner cần knowledge này lúc này, đã dùng nguồn nào, áp dụng vào quyết định nào và evidence nào cho thấy nó giúp hoặc chưa giúp**.
