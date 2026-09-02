# ADR-004 — Deterministic Core + Implementation Flexibility

- **Status:** Accepted
- **Decision date:** 2026-09-02
- **Last reviewed:** 2026-09-02
- **Applies from:** roadmap rebaseline v2026.09-deterministic-core
- **Supersedes:** phần implementation-language ownership trong ADR-003 cho rằng Go phải là canonical owner của mọi domain/governance semantics
- **Keeps from ADR-003:** separation giữa deterministic governance, orchestration và Agent intelligence; authority progression; fail-safe boundaries
- **Related:** [`ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md), [`IMPLEMENTATION-STRATEGY.md`](IMPLEMENTATION-STRATEGY.md), [`TECHNOLOGY-CANDIDATES.md`](TECHNOLOGY-CANDIDATES.md)

## 1. Bối cảnh

Mục tiêu chương trình không phải biến learner thành Go developer. Mục tiêu là xây một Affiliate Intelligence Bot có evidence, deterministic decision, policy, audit và controlled automation.

ADR-003 đã sửa đúng lỗi `Go-everything` bằng cách giao orchestration cho n8n và intelligence cho AgentRuntime. Tuy nhiên sau review tooling 2026-09-02, hai assumption khác cần nới:

```text
deterministic governance semantics
≠ bắt buộc phải được người học tự viết bằng Go

AgentRuntime
≠ bắt buộc phải bắt đầu bằng một framework code-heavy riêng
```

Visual rule engine hiện có thể biểu diễn decision table/tree/flow, test input/output và version rule; coding agents trên GitHub có thể nhận issue, sửa code, chạy test và mở PR để người học review; n8n hiện đã có visual AI Agent/tool workflow + human-in-the-loop support. Vì vậy khóa Core vào một implementation language hoặc thêm Agent framework riêng quá sớm có thể tạo learning/ops burden không trực tiếp cải thiện Affiliate judgment hoặc governance quality.

## 2. Quyết định

Canonical architecture từ nay là:

```text
Deterministic Domain / Governance Core
+ n8n Orchestration Reference
+ AgentRuntime Intelligence Layer
```

Mental model bắt buộc:

```text
Deterministic Core decides what is true / allowed.
Agent investigates / reasons / proposes.
n8n coordinates when / where / how workflows run.
```

Implementation principle:

```text
DETERMINISTIC CORE FIRST
≠ CODE FIRST

NO-CODE WHEN IT IS AUDITABLE
REUSE AN EXISTING VISUAL RUNTIME BEFORE ADDING A NEW ONE
AGENT-WRITTEN CODE WHEN CODE IS NECESSARY
HUMAN WRITES CODE ONLY WHEN IT ADDS LEARNING OR REVIEW VALUE
```

## 3. Canonical ownership không phụ thuộc vendor/language

Deterministic Domain/Governance Core owns the **contract/behavior** của:

- evidence schema/validation;
- subject/observation identity;
- canonical history/state contracts;
- deterministic ranking/decision logic;
- confidence/uncertainty semantics khi machine-readable;
- `DecisionPacket` / `ActionIntent` contracts;
- deterministic risk/policy classification;
- authorization result như `ALLOW | DENY | WAIT | GET_MORE_DATA | HUMAN_REVIEW`;
- audit/correlation contracts;
- invariants như `missing != 0`, `Decision != Execution`.

Canonical ownership ở đây là ownership của **semantics và tests**, không phải ownership của một ngôn ngữ.

AgentRuntime owns unstructured reasoning/research/proposal capability, nhưng không sở hữu final evidence truth hoặc authorization.

## 4. Implementation profiles

### 4.1. Visual deterministic core

Candidate hiện tại: **DecisionRules** hoặc rule engine tương đương.

Phù hợp khi:

- logic là decision table/tree/rule flow rõ;
- input/output schema cố định;
- test bench/parity test đủ mạnh;
- rule version/review/audit trace rõ;
- failure/timeout có thể fail closed;
- export/API boundary không làm mất canonical state.

Không adopt chỉ vì có giao diện đẹp.

### 4.2. Go deterministic core

Go tiếp tục là **reference implementation và code fallback ưu tiên**.

Dùng Go khi:

- rule graph trở nên khó đọc/review hơn code;
- performance/latency là bottleneck thật;
- cần offline/local deterministic execution;
- cần vendor independence;
- custom protocol/invariant khó biểu diễn bằng rule engine;
- security/fail-closed enforcement cần process boundary riêng.

M00 Go starter hiện tại được giữ làm **golden oracle/reference implementation**. Bài 0.1 đã PASS không bị reset.

### 4.3. Agent-maintained code

Khi code cần thiết nhưng learner không cần tự gõ từng dòng:

```text
Issue/spec
→ Development Agent
→ code + tests + PR
→ CI/security checks
→ human review
→ merge
```

Development Agent có thể là GitHub Copilot cloud agent, OpenAI Codex hoặc Anthropic Claude coding agent nếu account/repo cho phép.

Agent development capability không tạo runtime authority:

```text
coding agent can open a PR
≠ code is trusted
≠ code is merged
≠ production policy changed
```

### 4.4. Visual-first AgentRuntime

Khi M08 bắt đầu read-only tool use, ưu tiên thử **n8n AI Agent** trên cùng orchestration/runtime đã có trước khi thêm Hermes/OpenAI Agents SDK hoặc một Agent framework riêng.

```text
M08 first Agent spike
→ n8n AI Agent + explicit read-only tools
→ same Safe Profile/eval set
→ measure limitation
→ only then compare Hermes/OpenAI Agents SDK if needed
```

Lý do:

- giảm số runtime phải vận hành;
- giảm code integration;
- reuse credential/routing/audit surface đã học ở n8n;
- vẫn giữ AgentRuntime abstraction để không vendor-lock curriculum.

n8n AI Agent không nhận policy authority; tool output vẫn là untrusted input tới khi deterministic validation PASS.

Flowise chỉ ở watchlist/comparison khi n8n Agent graph thực sự khó maintain hoặc thiếu Agent-specific capability đo được.

## 5. No-code/low-code boundary

n8n được phép sở hữu implementation plumbing như:

- trigger/schedule/webhook;
- fetch/import/map/transform;
- retry/backoff;
- notification;
- approval routing;
- bounded execution;
- calling deterministic rule/API/service;
- hosting/routing visual Agent workflow trong authority ceiling.

Nhưng n8n canvas không tự trở thành canonical authority chỉ vì có IF/Switch/Code/AI Agent node.

Một visual deterministic rule engine **có thể** implement canonical deterministic decision/policy khi parity/audit/fail-closed gate PASS; n8n workflow routing không được âm thầm thay rule engine hoặc reviewed policy contract.

## 6. DecisionRules candidate gate

Earliest meaningful spike:

- M00: **optional comparison only sau khi Go baseline đã PASS**, để so cùng fixtures và output states; không thay learner checkpoint hiện tại.
- M07: meaningful candidate cho `DecisionPacket`/abstention/risk tables.
- M09+: meaningful candidate cho deterministic risk/authorization nếu fail-closed + parity + version review đạt.

Adoption gate:

```text
same canonical input/output contract
+ parity tests with golden Go/reference fixtures
+ explicit unknown/missing behavior
+ versioned/reviewable rule artifact
+ deterministic result for same input/version
+ decision reason/trace available
+ API/runtime error fails closed
+ no Agent-generated rule auto-publish
+ rollback/export path documented
```

## 7. Development Agent gate

Development Agent có thể dùng từ bất kỳ Mission nào khi cần sửa code/repo, nhưng không phải PASS shortcut.

Mỗi agent-authored PR phải có:

- issue/spec rõ;
- changed behavior được mô tả;
- tests/regression evidence;
- CI PASS;
- dependency/security review khi relevant;
- human review của diff và contract;
- không auto-merge consequential policy/runtime changes chỉ vì agent confidence cao.

Learner phải hiểu **behavior và reason**, không bắt buộc tự viết mọi implementation detail.

## 8. AgentRuntime candidate gate

n8n AI Agent là visual-first candidate ở M08. Hermes/OpenAI Agents SDK chỉ được thêm khi cùng test set chứng minh measured benefit như:

- permission isolation tốt hơn;
- tool/runtime capability cần thiết hơn;
- prompt-injection containment tốt hơn;
- auditability/portability tốt hơn;
- latency/cost/human intervention tốt hơn đáng kể.

Không thêm runtime chỉ vì demo thông minh hơn.

## 9. Authority progression giữ nguyên

```text
A0 deterministic/manual
→ A1 grounded advisory
→ A2-RO read-only tools
→ A3-shadow proposed/dry-run actions
→ A3-limited governed bounded execution
→ production closed loop
```

No-code, low-code hoặc coding agent không làm tăng authority level.

```text
visual rule exists
≠ rule approved

AI generated the rule
≠ rule is policy

workflow can execute
≠ workflow is authorized

Agent can call a tool
≠ Agent can authorize the result/action
```

## 10. Fail-safe invariant mới

Thay vì khóa invariant vào một process cụ thể:

```text
Go Policy unavailable
→ no consequential execution
```

canonical invariant là:

```text
Deterministic Policy Authority unavailable / invalid / unverified
→ no consequential execution
```

Nếu implementation đang là Go thì Go failure kích hoạt invariant. Nếu implementation là DecisionRules/rule engine thì rule runtime/version/parity failure cũng phải fail closed.

## 11. Hệ quả cho learner roadmap

- M00 hiện tại: giữ Go starter/golden oracle, không học lại Bài 0.1.
- M01–M03: không thêm tool chỉ để tránh vài dòng code; giữ implementation đơn giản nhất.
- M04: n8n read-only orchestration có thể map/import và gọi deterministic validator implementation hiện hành.
- M06: plumbing watcher/retry/alert ưu tiên n8n, không tự viết Go scheduler nếu không cần.
- M07: first meaningful visual-rule comparison cho deterministic DecisionPacket/policy.
- M08: n8n AI Agent là visual-first read-only AgentRuntime candidate; Hermes/OpenAI Agents SDK chỉ compare khi có bottleneck đo được.
- M09–M10: visual policy/rule engine có thể được adopt nếu parity/fail-closed/audit gate PASS; Go vẫn fallback.
- M11: production PASS dựa trên contract/evidence/recovery, không dựa vào số dòng Go hay số framework dùng.

## 12. Non-goals

ADR này không có nghĩa:

- bỏ Go khỏi repo;
- n8n trở thành final policy authority;
- Agent/LLM được tự quyết `ALLOW/DENY`;
- DecisionRules mandatory;
- n8n AI Agent mandatory;
- Hermes/OpenAI SDK bị cấm;
- coding agent được auto-merge;
- learner không cần hiểu deterministic logic;
- visual rule không cần tests;
- workflow success đồng nghĩa evidence/policy đúng.

## 13. Nguồn ngoài được kiểm tại review

- DecisionRules Rule Solver API và product docs: https://docs.decisionrules.io/doc/api/rule-solver-api
- DecisionRules public-cloud release notes/AI Assistant: https://docs.decisionrules.io/doc/product-updates/release-notes/public-cloud
- GitHub Copilot cloud agent: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents
- GitHub third-party coding agents (Codex/Claude): https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents
- n8n human-in-the-loop for AI tool calls: https://docs.n8n.io/advanced-ai/human-in-the-loop-tools/
