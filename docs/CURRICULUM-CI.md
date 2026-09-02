# Curriculum CI — Hệ thống kiểm tra curriculum

## V2 readiness metadata

`python scripts/validate_readiness.py` validates the distinction between
authoring and delivery. Every Mission file declares `curriculum_version`,
`release_kind`, `starter_paths`, `eval_pack`, `verification_commands`,
knowledge links.

Normal CI verifies schema and declared paths while preserving v1 baseline files.
It reports `DELIVERY_INCOMPLETE` transparently without turning historical
authoring status into a failing release claim. A new v2 Mission may be promoted
to `ready` only after its delivery bundle is real and:

```bash
python scripts/validate_readiness.py --strict
```

passes alongside its evaluator and relevant curriculum tests. See
[`CURRICULUM-MIGRATION-v2.md`](CURRICULUM-MIGRATION-v2.md) for the mapping.

Curriculum CI bảo vệ [`../CURRICULUM.md`](../CURRICULUM.md), Mission-first/Real Evidence semantics, provenance/freshness, Agentic Decision Intelligence, learner/reference code và safety invariants. CI không bảo vệ một inventory legacy hoặc biến số lượng hiện tại thành mục tiêu vĩnh viễn.

Tiếng Việt là ngôn ngữ chính thức. English term được giữ cho code, error code, công nghệ và thuật ngữ kỹ thuật khi cần; xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md).

## 1. Chạy kiểm tra local

Từ root repository:

```bash
python scripts/validate_curriculum.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python scripts/validate_agentic_architecture.py
python -m unittest discover -s tests -v
```

Reference Bot:

```bash
cd lab/affiliate-bot
test -z "$(gofmt -l .)"
go vet ./...
go test ./...
```

Learner Bot:

```bash
cd lab/learner/affiliate-bot
test -z "$(gofmt -l .)"
go vet ./...
go test ./...
```

Exit code `0` nghĩa là gate tương ứng PASS.

## 2. Layer 1 — Active curriculum validator

`scripts/validate_curriculum.py` phải bảo vệ:

- root authority là `CURRICULUM.md`;
- current normalized inventory khớp 7 Parts / 21 Chapters / 63 Core micro-lessons;
- inventory được derive từ active roadmap, không hard-code làm invariant vĩnh viễn;
- chỉ `roadmap/part-00.md` đến `part-06.md` thuộc active Core;
- ID/Part/Chapter/lesson path unique và nhất quán;
- lesson metadata, lifecycle, headings và relative links;
- Mission refs nằm trong `M00–M11`;
- freshness metadata contract;
- Core, Advanced và Reference không bị trộn PASS semantics.

Khi `CURRICULUM.md` được thay qua accepted ADR và roadmap đồng bộ, validator được cập nhật cùng PR. Validator không được dùng historical `sources/` để phủ quyết active structure.

## 3. Layer 2 — Authority và provenance hardening

`scripts/validate_hardening.py` phải bảo vệ:

- `CURRICULUM.md` tồn tại và có Mission-first, Real Evidence Ladder, Core / Advanced / Reference;
- README, ROADMAP, BUILD-FIRST, CONTRIBUTING và active authority docs trỏ về cùng root authority;
- external source IDs resolve trong Affiliate + Bot freshness registers;
- active lesson/chapter IDs không trùng;
- active docs không tuyên bố syllabus lịch sử là canonical;
- các số liệu legacy chỉ tồn tại trong historical context rõ ràng;
- file trong `sources/` được bỏ qua bởi active-authority guard nhưng vẫn giữ provenance.

`S:` ref trong metadata cũ có thể được giữ làm lineage. Nó không trao authority cho historical syllabus và không được dùng để tạo lại lesson ngoài active roadmap.

## 4. Layer 3 — Build-First semantic validator

`scripts/validate_build_first.py` bảo vệ execution architecture.

### BUILD001–BUILD003 — Authority, Mission identity và sequence

- Build-First authority files bắt buộc tồn tại và link `CURRICULUM.md`;
- Mission ID unique, filename đúng ID;
- active Mission spine đúng `M00→M11`;
- authored Mission files là contiguous prefix từ M00 hoặc có explicit authoring-state rule.

### BUILD004–BUILD006 — Knowledge pull, dependency và Bot Version

- explicit Core lesson ref phải resolve trong active 63-lesson inventory;
- Mission `ready` chỉ pull knowledge cần cho attempt hiện tại;
- dependency trỏ ngược, tồn tại và không cycle;
- Bot Version tăng đúng sequence và capability/authority ceiling.

### BUILD007–BUILD010 — Ready contract và workspace

- Mission `ready` có Attempt First, Capability/Reality/Operated, failure cases, explain-back và evidence artifacts;
- không quá ba micro-lessons liên tiếp trước khi learner quay lại build/run/observe;
- learner/reference separation được giữ;
- reference solution không được coi là learner evidence;
- learner/reference Go runtime line đồng bộ.

### BUILD011–BUILD014 — Real Evidence Ladder

- sample/synthetic được gắn E0 và không thỏa business gate;
- M00 có E1 public observations + human judgment trước Bot;
- M03–M05 có manual tracked publish, analytics/outcome và reviewed improvement boundary;
- M10/M11 chỉ tăng authority khi policy/approval/revalidation/audit/kill-switch evidence đủ.

### LANG001 — Language Policy

- tiếng Việt là ngôn ngữ chính thức;
- authority docs tham chiếu Language Policy;
- không dùng tỷ lệ từ máy móc vì code/API/protocol cần giữ English chính xác.

## 5. Layer 4 — Agentic Decision Intelligence validator

`scripts/validate_agentic_architecture.py` bảo vệ kiến trúc AI/Agent mà không khóa repo vào provider/model cụ thể.

### AI001 — Authority files

Bắt buộc có docs về:

- AI/Agent architecture;
- Decision contracts, confidence/uncertainty và freshness;
- Tool Registry, provider boundary và Agent Runtime;
- Agent Evaluation, durable HITL và Decision-Outcome Memory;
- autonomy/approval, security, idempotency và kill switch.

### AI002 — Capability progression

Active mapping phải giữ:

```text
M00–M01 → A0 deterministic
M02–M07 → A1 grounded advisory
M08     → A2 read-only tool agent
M09     → A3-S shadow + durable approval
M10–M11 → A3-G bounded governed automation
```

Deterministic baseline tiếp tục tồn tại sau khi AI xuất hiện. MCP/A2A/multi-agent là Advanced/Reference, không phải Core dependency.

### AI003 — DecisionPacket contract

Decision contract phải giữ ít nhất:

```text
evidence
confidence
uncertainty
missing evidence
freshness
expiry
risk level
policy decision
```

Confidence không phải execution permission; `WAIT`, `GET_MORE_DATA`, `HUMAN_REVIEW` và `ABSTAIN` là output hợp lệ.

### AI004–AI006 — Tool và model boundaries

- external side-effect tool đi qua `ActionIntent → Policy/Risk → approval khi cần`;
- Tool Registry khai báo `permission`, `risk_ceiling`, `requires_approval`, validation và audit fields;
- authority architecture giữ `MODEL OUTPUT = UNTRUSTED INPUT`, `AI ADVICE ≠ EXECUTION AUTHORITY` và `POLICY BEFORE CONSEQUENTIAL ACTION`.

### AI007–AI010 — Evaluation, freshness và provider neutrality

- evaluation bao phủ output, grounding, trajectory/tool behavior, policy/safety, confidence calibration, latency/cost và human intervention;
- volatile provider/MCP facts có source, URL, verified date và volatility;
- domain core đi qua provider-neutral interface/adapter;
- multi-agent/A2A không được biến thành prerequisite Core.

### AI011–AI012 — Controlled outcome learning

Learning loop phải là:

```text
Decision
→ Action
→ Outcome
→ Evaluation
→ Proposed Improvement
→ Offline Test / Experiment
→ Review
→ Deploy
```

Agent không tự rewrite production policy/prompt/weights/code. Programmatic orchestration ưu tiên read-only/internal-safe tools; external actions không được free-orchestrate.

## 6. Four Milestone Gates trong CI

CI kiểm cấu trúc/rule để Mission có thể thu evidence cho bốn gate:

| Gate | Mission | Structural checks |
|---|---|---|
| G1 — First Evidence-Backed Decision | M00 | real observation schema, human-before-Bot, decision evidence |
| G2 — Trustworthy Intelligence | M01–M02 | immutable history, grounding, eval và fallback |
| G3 — First Market Learning Loop | M03–M05 | manual publish, tracked outcome, missing-vs-zero, reviewed change |
| G4 — Governed Production Loop | M06–M11 | reliability, contracts, tool permissions, approval, recovery và outcome memory |

CI chỉ kiểm rằng contract/gate tồn tại và code behavior được test. Human/market evidence phải được review riêng.

## 7. Executable Go gates

GitHub Actions chạy cho cả reference và learner modules:

```text
gofmt check
→ go vet ./...
→ go test ./...
```

Reference Bot chứng minh implementation mẫu chạy/test được để đối chiếu sau attempt. Learner Bot chứng minh workspace active không hỏng khi tiến hóa qua Mission.

Fast CI không bắt buộc dịch vụ production bên ngoài. Database/provider/platform integrations dùng fake/local contract tests trước; integration infrastructure chỉ thêm khi Mission cần operational evidence tương ứng.

## 8. Regression / mutation tests

Regression tests phải cố tình phá và xác nhận validator bắt được tối thiểu:

- root authority bị đổi về historical syllabus;
- inventory/ID active không khớp `CURRICULUM.md` và roadmap;
- Mission ngoài `M00–M11` bị đưa vào active spine;
- sample được dùng để thỏa real-evidence gate;
- Mission thiếu Capability PASS, Reality verified hoặc Operated;
- AI capability được tăng quá sớm;
- DecisionPacket thiếu evidence/confidence/uncertainty;
- model output đi thẳng vào execution;
- tool thiếu permission/risk/approval boundary;
- source volatile thiếu freshness metadata;
- missing outcome bị đổi thành zero;
- outcome learning mất guard chống silent self-modification;
- multi-agent bị biến thành Core dependency.

Scaffolder tests phải tạo lesson/Mission đúng active authority và không đọc historical inventory như nguồn scope.

## 9. GitHub Actions merge rule

Workflow `.github/workflows/curriculum-ci.yml` chạy với mọi Pull Request và push vào `main`:

```text
active curriculum validator
→ authority/provenance hardening
→ Build-First semantics
→ Agentic Architecture
→ Python regression tests
→ reference: gofmt + vet + test
→ learner:   gofmt + vet + test
```

Không merge khi bất kỳ gate nào fail. Branch protection/ruleset của `main` cần require workflow này theo [`REPOSITORY-GOVERNANCE.md`](REPOSITORY-GOVERNANCE.md).

## 10. State rule — CI không phải learner PASS

CI chỉ xác minh cấu trúc, code và invariant của repository.

```text
CI PASS
≠ Capability PASS
≠ Reality verified
≠ Operated
≠ Mission DONE
≠ Milestone Gate PASS
```

Không dùng một run xanh để tự cập nhật learner achievement hoặc tuyên bố business validation. Outcome dương cũng không được dùng để bỏ qua test, provenance hay safety boundary.
