# Chiến lược implementation — deterministic core trước, không mặc định code trước

- **Status:** Active reference
- **Last reviewed:** 2026-09-02
- **Architecture authority:** [`ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md`](ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md)

## Nguyên tắc

```text
DETERMINISTIC CORE FIRST
≠ CODE FIRST

NO-CODE WHEN IT IS AUDITABLE
REUSE AN EXISTING VISUAL RUNTIME BEFORE ADDING A NEW ONE
AGENT-WRITTEN CODE WHEN CODE IS NECESSARY
HUMAN WRITES CODE ONLY WHEN IT ADDS LEARNING OR REVIEW VALUE
```

Canonical curriculum khóa **contract/behavior**, không khóa mọi behavior vào Go hoặc một Agent framework cụ thể.

Deterministic Domain/Governance Core vẫn phải giữ:

- evidence schema/validation;
- canonical identity/history contracts;
- deterministic ranking/decision;
- confidence/uncertainty/risk semantics;
- authorization states;
- audit/correlation contracts;
- invariants như `missing != 0`, `Decision != Execution`.

## Ba deterministic implementation profile

### Profile A — Visual/no-code deterministic core

```text
n8n
→ acquire / map / orchestrate
→ deterministic rule engine
→ canonical persistence
→ n8n route / approval / bounded execution
```

Candidate hiện tại cho visual rule engine: **DecisionRules**. Chỉ adopt sau parity/eval/fail-closed gate.

### Profile B — Go deterministic core

```text
n8n
→ Go service/CLI/API
→ canonical persistence
→ n8n route / approval / bounded execution
```

Go vẫn là reference implementation ưu tiên khi:

- visual rule graph bắt đầu khó review hơn code;
- performance/latency là bottleneck thật;
- cần offline/local execution;
- cần vendor independence;
- custom protocol/invariant khó biểu diễn rõ bằng rule engine;
- fail-closed enforcement cần process boundary riêng.

### Profile C — Agent-maintained code

Runtime có thể giống Profile B, nhưng learner không nhất thiết tự viết mọi dòng Go:

```text
Issue/spec
→ Development Agent
→ code + tests + PR
→ CI/security checks
→ human review
→ merge
```

Development Agent là **engineering worker**, không phải Bot runtime authority. Code do agent viết không được merge nếu thiếu test/evidence/review tương ứng.

## Quy tắc lựa chọn

Chọn implementation có **failure surface nhỏ nhất nhưng vẫn audit/test được**.

```text
visual rule đủ rõ + parity test PASS
→ không cần viết Go chỉ để chứng minh đã code

visual rule trở nên opaque / hard-to-test
→ chuyển deterministic contract sang Go hoặc policy engine phù hợp

coding cần thiết nhưng giá trị học nằm ở domain/review
→ giao implementation cho Development Agent, learner review contract/test/diff
```

## V1 M00 reference

V1 M00 starter hiện tại tiếp tục dùng Go và là **golden oracle/reference implementation** cho deterministic behavior đầu tiên. In v2, this reference maps to M02 after M00 human market loop and M01 outcome snapshot.

Điều này có ba lý do:

1. Bài 0.1 đã PASS và không có evidence cho thấy rewrite M00 tạo learning value;
2. baseline nhỏ, dễ hiểu và đã có regression tests;
3. nó tạo oracle để sau này so một visual rule implementation trên đúng fixtures.

Do đó:

```text
Bài 0.1 PASS
→ giữ nguyên
→ không học lại
→ không rewrite M00 chỉ vì có no-code tool
```

## M04+ — giảm code plumbing

Khi orchestration xuất hiện, ưu tiên n8n cho:

- trigger/schedule/webhook;
- HTTP/API integration;
- import/map/transform;
- retry/backoff;
- notifications;
- approval routing;
- bounded execution;
- calling deterministic rule/service.

Không tự viết Go scheduler/integration nếu n8n giải quyết use case rõ hơn và failure behavior vẫn audit được.

## M07+ — rule engine candidate

DecisionRules hoặc rule engine tương đương có thể spike trên một contract đã có oracle/tests:

```text
canonical fixtures
→ Go/reference result
→ visual rule result
→ parity comparison
```

Chỉ adopt khi:

- same input/version → same deterministic result;
- missing/unknown behavior explicit;
- decision reason traceable;
- rule version reviewable;
- runtime failure fail closed;
- rollback/export path có thật.

## M08+ — visual-first AgentRuntime

AgentRuntime là abstraction. Khi read-only tool use bắt đầu, ưu tiên dùng runtime đã có trước:

```text
M08
n8n AI Agent + explicit read-only tools
→ CandidateEvidence
→ deterministic validation
```

Chỉ thêm Hermes Agent hoặc OpenAI Agents SDK khi cùng fixture/eval set chứng minh n8n AI Agent có bottleneck thật như permission isolation, specialized tool runtime, auditability hoặc capability cần thiết.

Flowise là watchlist/comparison only nếu n8n Agent graph thực sự khó maintain; không thêm một visual runtime thứ hai chỉ để giảm vài node.

## Development Agent candidate

Ưu tiên workflow:

```text
human writes problem/acceptance criteria
→ Development Agent implements
→ CI + tests
→ human reviews behavior/security/diff
→ merge
```

Candidate hiện hành:

- GitHub Copilot cloud agent;
- OpenAI Codex coding agent;
- Anthropic Claude coding agent.

Việc agent có thể tạo PR không thay review requirement.

## Authority invariant

```text
visual workflow can evaluate a condition
≠ workflow owns authority

AI can generate a rule
≠ generated rule is approved policy

coding agent can open a PR
≠ code is trusted/merged

AgentRuntime can call a tool
≠ AgentRuntime can authorize the result/action
```

Final authority vẫn phải đến từ deterministic contract đã được version/review/test và Mission gate hiện hành.
