# Curriculum CI — Hệ thống kiểm tra curriculum

Curriculum CI bảo vệ đồng thời **canonical curriculum**, provenance/freshness (nguồn gốc/độ mới), Build-First execution semantics, Agentic Decision Intelligence, learner/reference code và các invariant quan trọng.

Tiếng Việt là ngôn ngữ chính thức của tài liệu. English term được giữ cho tên code, error code, công nghệ và thuật ngữ kỹ thuật khi cần. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md).

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

## 2. Layer 1 — Canonical curriculum validator

`scripts/validate_curriculum.py` bảo vệ:

- active canonical v2026.09 + historical v2026.08;
- 23 Parts / 89 Chapters / 671 Lessons;
- Go-first Part 15 direction;
- timeline metadata;
- Lesson ID, metadata, lifecycle và headings;
- relative links;
- freshness metadata contract.

## 3. Layer 2 — Curriculum integrity hardening validator

`scripts/validate_hardening.py` bảo vệ:

- external source IDs đối chiếu Affiliate + Bot source registers;
- normalized provenance authority;
- đúng 671 Lesson / 89 Chapter;
- canonical Project 1–14 và vị trí Part;
- authority-document consistency.

Khi freshness register chi tiết hóa source ID, source ID đã được Lesson tham chiếu phải được giữ compatibility/migration path; không làm provenance cũ tự nhiên mất resolve.

## 4. Layer 3 — Build-First semantic validator

`scripts/validate_build_first.py` bảo vệ execution architecture mà không định nghĩa lại canonical syllabus.

### BUILD001–BUILD003 — Authority, Mission identity và sequence

- Build-First authority files bắt buộc tồn tại;
- Mission ID unique, filename đúng ID;
- Bot roadmap đúng M00→M15;
- authored Mission files là contiguous prefix từ M00.

### BUILD004–BUILD006 — Knowledge, dependency và Bot Version

- explicit Lesson refs phải resolve trong 671 inventory;
- Mission `ready` phải có required canonical knowledge mapping;
- dependency phải trỏ ngược, tồn tại và không cycle;
- Bot Version tăng đúng sequence và khớp roadmap.

### BUILD007–BUILD009 — Ready contract, learner state, Projects

- Mission `ready` có đủ required sections;
- Mission không được auto-mark Lesson PASS;
- `projects.contributes_to` chỉ dùng canonical Project 1–14.

### BUILD010–BUILD014 — Workspace/semantics hardening

- learner + reference bootstrap files tồn tại;
- learner/reference separation + capability ceiling theo Current Mission;
- `bot_version_from` nối đúng Mission trước;
- Project frontmatter khớp central mapping;
- learner/reference Go runtime line đồng bộ.

### LANG001 — Language Policy

- tiếng Việt là ngôn ngữ chính thức;
- authority docs tham chiếu Language Policy;
- guard không dùng tỷ lệ từ máy móc vì code/API/protocol cần giữ English chính xác.

## 5. Layer 4 — Agentic Decision Intelligence validator

`scripts/validate_agentic_architecture.py` bảo vệ kiến trúc AI/Agent mà không khóa repo vào provider/model cụ thể.

### AI001 — Agentic authority files

Bắt buộc tồn tại các authority docs về:

- AI/Agent architecture;
- A0–A4 capability levels;
- Decision contracts;
- provider capability matrix;
- A1 advisory patterns;
- Decision Intelligence/confidence/freshness/model routing;
- Tool Registry/Agent Runtime/programmatic orchestration/MCP notes;
- Agent Evaluation/Durable HITL/Decision-Outcome Memory.

### AI002 — Capability progression

Central Bot Evolution map phải giữ:

```text
M00–M04 → A0
M05–M10 → A1
M11–M12 → A2
M13–M14 → A3
M15     → A4 optional
```

AI được xuất hiện sớm nhưng không được tăng execution authority sớm.

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

Confidence không phải execution permission.

### AI004–AI005 — Tool governance

External side-effect tool phải đi qua `ActionIntent → Policy/Risk → approval khi cần`; Tool Registry phải khai báo `permission`, `risk_ceiling`, `requires_approval` và audit fields.

### AI006 — Untrusted model boundary

Authority architecture phải giữ:

```text
MODEL OUTPUT = UNTRUSTED INPUT
AI ADVICE ≠ EXECUTION AUTHORITY
POLICY BEFORE CONSEQUENTIAL ACTION
```

### AI007 — Agent evaluation

Evaluation standard phải bao phủ output, trajectory/tool behavior, policy/safety, confidence calibration, latency/cost và human intervention.

### AI008 — Freshness cho kỹ thuật Agent biến động

MCP/provider-runtime current facts phải có source, URL, verified date và volatility. Exact feature/version không trở thành permanent canonical truth.

### AI009 — Provider-neutral core

Domain Decision/Policy core phải đi qua `AI Provider Interface → Provider Adapter`; exact provider/model mapping thuộc config/freshness layer.

### AI010 — Multi-agent boundary

A4/multi-agent chỉ optional ở M15. A2A không được trở thành dependency mặc định trước khi có independent remote-agent/service use case thật.

### AI011 — Outcome learning không tự sửa production

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

Agent không được tự rewrite production policy/prompt/weights từ outcome history.

### AI012 — Programmatic tool orchestration boundary

Bounded programmatic orchestration ưu tiên READ_ONLY/internal-safe tools. External actions như publish/spend/account-security change/destructive delete không được free-orchestrate ngoài explicit policy.

## 6. Executable Go gates

GitHub Actions chạy cho **cả reference và learner modules**:

```text
gofmt check
→ go vet ./...
→ go test ./...
```

Reference Bot chứng minh curriculum có implementation chạy/test được để đối chiếu. Learner Bot chứng minh active learner workspace không bị hỏng khi tiến hóa qua Mission.

Fast CI hiện không bắt buộc PostgreSQL service; integration infrastructure chỉ thêm khi operational value đủ lớn.

## 7. Regression / mutation tests

`tests/test_build_first_validator.py` tiếp tục bảo vệ Build-First semantic invariants.

`tests/test_agentic_architecture_validator.py` cố tình phá và phải bắt được ít nhất:

- thiếu Agentic authority file;
- sai AI level ở Mission;
- DecisionPacket thiếu confidence/evidence field bắt buộc;
- external tool thiếu Policy/Risk boundary;
- tool contract thiếu risk ceiling;
- mất `MODEL OUTPUT = UNTRUSTED INPUT`;
- Agent Evaluation thiếu metric quan trọng;
- volatile Agent/MCP fact thiếu freshness metadata;
- mất provider-neutrality marker;
- multi-agent bị đưa trước M15;
- outcome learning mất guard chống tự sửa policy;
- programmatic orchestration mất guard cấm free external actions.

Các regression tests của curriculum/hardening/scaffolder trước đó tiếp tục chạy.

## 8. GitHub Actions merge rule

Workflow `.github/workflows/curriculum-ci.yml` chạy với mọi Pull Request và mọi push vào `main`.

```text
canonical validator
→ hardening validator
→ Build-First semantic validator
→ Agentic Architecture validator
→ Python regression tests
→ reference: gofmt + vet + test
→ learner:   gofmt + vet + test
```

**Quy tắc quy trình:** không merge khi bất kỳ gate nào fail.

Để GitHub tự cưỡng chế quy tắc này ở cấp repository, branch protection/ruleset của `main` vẫn cần cấu hình theo [`REPOSITORY-GOVERNANCE.md`](REPOSITORY-GOVERNANCE.md) / Issue #41.

## 9. State rule — CI không phải learner PASS

CI chỉ xác minh cấu trúc/code/invariant của repository.

```text
CI PASS
≠
Mission PASS
≠
Lesson PASS
≠
Project PASS
```

Không dùng GitHub Actions run xanh để tự cập nhật learner achievement.