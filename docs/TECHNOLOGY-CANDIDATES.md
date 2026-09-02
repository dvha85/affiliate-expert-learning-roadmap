# Technology References — Runtime, rule engine và Development Agent cho kiến trúc Hybrid

- **Status:** Reference only — không phải Core/PASS shortcut
- **Last reviewed:** 2026-09-02
- **Primary architecture authority:** [`ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md`](ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md)
- **Runtime-separation baseline:** [`ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md)

Tài liệu này không quyết định learner sequence. Nó ghi reference implementation, visual/no-code candidate, code fallback, Development Agent và adoption gate.

Nguyên tắc chung:

```text
Tool available
≠ tool adopted

Tool adopted
≠ tool owns truth

No-code
≠ no governance

AI generated code/rule
≠ reviewed production change

Framework capability
≠ Bot authority
```

Mọi candidate chỉ được adopt khi giải quyết bottleneck đã quan sát được và không làm thay đổi Mission authority ceiling.

## 1. Canonical ownership

```text
Deterministic Domain / Governance Core
= evidence / history / deterministic decision / policy / audit CONTRACTS

Go
= deterministic core reference/fallback implementation

DecisionRules
= visual deterministic rule-engine candidate

n8n
= primary orchestration reference
= visual-first AgentRuntime candidate khi Agent tool-use bắt đầu

AgentRuntime
= intelligence role, không phải authority role

Hermes Agent / OpenAI Agents SDK
= AgentRuntime comparison candidates khi cần runtime chuyên biệt hơn

Development Agent
= repository engineering worker
= GitHub Copilot cloud agent / OpenAI Codex / Anthropic Claude candidates

OpenTelemetry
= telemetry/trace protocol candidate

Langfuse
= optional AI/Agent observability + evaluation backend

MCP
= tool/context interoperability protocol candidate

Playwright
= controlled browser acquisition candidate

Temporal
= durable execution candidate cho long-running workflow/HITL

OPA
= policy-as-code candidate khi visual/simple policy không còn đủ rõ
```

Không candidate nào tự trở thành canonical owner chỉ vì framework có feature tương ứng.

## 2. Go — deterministic reference/fallback, không phải coding quota

M00 Go starter được giữ làm **golden oracle/reference implementation** cho deterministic evidence decision đầu tiên.

Go phù hợp khi:

- visual rule graph khó review hơn code;
- performance/latency trở thành bottleneck thật;
- cần offline/local deterministic execution;
- cần vendor independence;
- custom invariant/protocol khó biểu diễn bằng visual rule;
- fail-closed enforcement cần process boundary riêng.

Go không mặc định sở hữu:

- scheduler;
- webhook/integration plumbing;
- notification;
- approval UI/routing;
- browser acquisition;
- Agent reasoning;
- mọi future policy chỉ vì code đã tồn tại.

### Timing

| Mission | Go role |
|---|---|
| M00 | **Golden oracle/reference**; learner path hiện tại giữ nguyên |
| M01–M06 | dùng khi đó là implementation nhỏ nhất rõ/audit được |
| M07 | oracle cho visual-rule parity comparison |
| M09–M11 | fallback/reference nếu visual policy hoặc external rule engine không đạt gate |

## 3. DecisionRules — visual deterministic rule-engine candidate

DecisionRules phù hợp với logic dạng decision table/tree/rule flow và có API để evaluate JSON input. Product docs hiện có test/debug/versioning capabilities và AI Assistant có thể hỗ trợ tạo/chỉnh rule; AI Assistant vẫn chỉ là authoring aid, không được auto-publish policy.

Potential role:

```text
canonical deterministic input
→ reviewed/versioned DecisionRules rule
→ deterministic result + reason/trace
→ canonical Decision/Policy contract
```

### Candidate timing

- M00: **optional comparison sau khi M00 Go baseline đã PASS**; không thay learner checkpoint và không reset Bài 0.1.
- M01–M06: không cần cho Core.
- M07: **first meaningful Core comparison** cho DecisionPacket/abstention/risk table.
- M09–M10: có thể implement deterministic risk/authorization nếu parity/fail-closed/version gate đã PASS.
- M11: production candidate nếu active rule version, rollback, audit và SLO đủ rõ.

### Adoption gate

```text
same canonical input/output contract
+ parity tests with Go/reference oracle
+ same input + same version = same result
+ explicit missing/unknown behavior
+ decision reason/trace available
+ versioned/reviewable rule artifact
+ API/runtime error fails closed
+ rollback/export path documented
+ AI-generated rule cannot auto-publish
+ n8n cannot silently override rule result
```

Không adopt nếu visual graph khó review hơn code hoặc vendor/runtime failure làm authority ambiguous.

**Official refs:**
- https://docs.decisionrules.io/doc/api/rule-solver-api
- https://docs.decisionrules.io/doc/product-updates/release-notes/public-cloud

## 4. n8n — primary orchestration reference

### Role phù hợp

- trigger / schedule / webhook;
- API/integration glue;
- fetch/import/map/transform;
- analytics/import workflow;
- notification/alert routing;
- retry/backoff;
- approval routing;
- calling deterministic rule/service/API;
- bounded execution sau deterministic policy gate.

Không đặt canonical authority của các phần sau trực tiếp vào workflow branch:

- Product/evidence truth;
- unreviewed scoring semantics;
- final risk/policy chỉ bằng IF/Switch;
- canonical business state nếu không có explicit persistence/audit contract.

### Roadmap learning progression

| Mission | n8n role |
|---|---|
| M00–M03 | Không cần cho Core |
| M04 | **First read-only learning slice**: manual trigger → import/map → deterministic validate/reconcile → failure handling |
| M05 | Optional reporting/orchestration |
| M06 | **Primary watcher/orchestration reference**: trigger/integration/retry/alert |
| M07 | Route DecisionPacket/rule calls nhưng không thay deterministic authority |
| M08 | Có thể host **visual-first AI Agent** + approved read-only tools nếu Safe Profile map được |
| M09 | **Shadow + durable approval routing reference** |
| M10 | **Bounded governed execution reference** sau deterministic policy gate |
| M11 | Production orchestration candidate/reference |

### Adoption gate

```text
canonical contract giữ nguyên
+ failure/retry behavior rõ
+ idempotency
+ audit/correlation
+ secret handling
+ workflow artifact reviewable/versioned
+ no authority bypass
```

Nếu một manual step hoặc deterministic service đơn giản hơn và ít failure surface hơn, không bắt buộc dùng n8n.

## 5. n8n AI Agent — visual-first AgentRuntime candidate

Khi M08 bắt đầu read-only tool-use, **first comparison nên ưu tiên runtime đã có** thay vì lập tức thêm một framework code-heavy khác.

Potential role:

```text
GET_MORE_DATA
→ n8n Agent receives bounded task
→ explicit read-only tools / MCP client
→ CandidateEvidence
→ Deterministic Core validation
→ DecisionPacket
```

n8n hiện có AI Agent/tool workflow và human-in-the-loop support cho tool calls; capability đó là implementation aid, không thay Safe Profile/policy.

### Candidate timing

- M00–M07: không dùng tool-agent cho Core.
- M08: **visual-first AgentRuntime spike** nếu explicit Tool Registry/allowlist/audit map được.
- M09+: Agent chỉ propose/pause xin approval trong authority ceiling hiện hành.

### Adoption gate

- explicit tool allowlist;
- M08 read-only ceiling;
- least-privilege credentials;
- tool output `UNTRUSTED UNTIL DETERMINISTIC VALIDATION`;
- prompt-injection/tool misuse cases;
- trace/correlation;
- deterministic/manual fallback khi Agent unavailable;
- no workflow branch can convert Agent confidence into authorization.

**Official ref:**
- https://docs.n8n.io/advanced-ai/human-in-the-loop-tools/

## 6. Hermes Agent — specialized AgentRuntime comparison candidate

Hermes Agent không còn là mandatory/first Agent implementation. Spike khi n8n AI Agent hoặc simpler runtime đã lộ bottleneck thật, ví dụ:

- cần tool runtime isolation/permission model tốt hơn;
- agent loop/research capability vượt visual workflow;
- portability/operational profile tốt hơn có thể đo được.

Comparison phải dùng cùng M08 fixture/eval set và Safe Profile.

### Adoption gate

```text
same AgentRuntime contract
+ same M08 eval set
+ explicit allowlist / least privilege
+ prompt-injection resistance
+ auditability
+ deterministic fallback
+ measured benefit over n8n AI Agent baseline
```

Nếu benefit không đo được, không thêm runtime mới.

## 7. OpenAI Agents SDK — AgentRuntime comparison candidate

OpenAI Agents SDK cung cấp agent runner, tools, guardrails, handoffs, sessions, tracing, MCP integration và human-in-the-loop capabilities. Đây là code-oriented comparison candidate, không phải reason để bắt learner viết Python/SDK integration.

### Timing

- M02: không dùng tool loop để vượt A1 advisory.
- M03–M07: optional reference, không Core dependency.
- M08+: compare khi n8n AI Agent/Hermes baseline đã cho thấy bottleneck cần SDK.

### Adoption gate

```text
same Safe Profile/eval set
+ explicit tool filters
+ least-privilege credentials
+ HITL/guardrails tested
+ all tool output untrusted until deterministic validation
+ deterministic fallback survives provider/runtime failure
+ trace maps về canonical correlation/audit
+ measured benefit > added code/ops burden
```

**Official refs:**
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/mcp/

## 8. Flowise — watchlist/comparison only

Flowise visual Agentflow/HITL có thể đáng spike nếu n8n Agent graph trở nên khó maintain hoặc Agent-specific visual tooling tạo measured benefit.

Default hiện tại:

```text
DO NOT ADD YET
```

Adopt chỉ khi một bounded M08/M09 use case chứng minh:

- ít code/ops burden hơn;
- Safe Profile map rõ;
- durable pause/resume/audit đạt;
- không tạo duplicate orchestration layer vô ích.

**Official docs:** https://docs.flowiseai.com/

## 9. Development Agent — coding mà learner không phải tự gõ mọi dòng

Development Agent là lớp **repository engineering**, tách khỏi production AgentRuntime.

Candidate hiện hành trên GitHub:

- GitHub Copilot cloud agent;
- OpenAI Codex coding agent;
- Anthropic Claude coding agent.

GitHub hiện hỗ trợ giao issue/prompt cho coding agent để thực hiện thay đổi và mở PR; third-party coding agents Codex/Claude có thể làm việc cùng Copilot cloud agent khi feature/policy của account cho phép.

### Role phù hợp

```text
issue/spec
→ research/plan
→ implement/refactor/tests
→ pull request
→ CI/security checks
→ human review
→ merge/reject
```

### Timing

- Có thể dùng từ M00 nếu task là repository engineering.
- Không phải Mission authority và không unlock A1/A2/A3.
- Đặc biệt hữu ích khi code cần thiết nhưng learning goal là domain/evidence/review thay vì syntax.

### Adoption gate cho mỗi PR

- acceptance criteria rõ;
- diff reviewable;
- tests/regression evidence;
- CI PASS;
- dependency/security review khi relevant;
- human review required cho behavior/policy/runtime changes;
- không auto-merge consequential policy changes;
- learner explain-back được behavior quan trọng.

**Official refs:**
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents
- https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents

## 10. MCP — candidate protocol cho Tool Registry boundary

```text
AgentRuntime
→ MCP client
→ approved MCP server/tool
→ result
→ Deterministic Core validate / ground
```

Invariant:

```text
MCP tool visible
≠ tool permitted

MCP call succeeded
≠ result is trusted evidence

MCP auth succeeded
≠ consequential action authorized
```

### Timing

- M00–M07: không cần cho Core.
- M08: first candidate protocol cho read-only Agent tool boundary.
- M09+: write/action tool vẫn chịu Mission authority + deterministic policy + approval.

### Gate

- explicit server/tool allowlist;
- least privilege;
- M08 read-only;
- secret/token không model-visible;
- correlation/audit metadata;
- timeout/retry semantics;
- tool result untrusted;
- sensitive/write tools separate policy gate.

**Official refs:**
- https://modelcontextprotocol.io/specification/2026-07-28
- https://blog.modelcontextprotocol.io/posts/2026-07-28/

## 11. Playwright — controlled browser acquisition candidate

Playwright dùng khi public source cần browser rendering/interaction mà HTTP/API fetch đơn giản không đủ.

```text
public dynamic page
→ controlled browser session
→ raw observation/snapshot
→ provenance
→ Deterministic Core validation/normalization
```

### Timing/gate

- M06 read-only watcher candidate; M08 có thể expose như approved read-only Agent tool.
- Chỉ sau khi HTTP/API baseline proven insufficient.
- domain/URL allowlist;
- bounded navigation/timeout/rate limit;
- no arbitrary form submit/upload/account mutation;
- provenance source URL + observed_at;
- platform terms/compliance reviewed.

**Official ref:** https://playwright.dev/docs/browsers

## 12. OpenTelemetry — observability protocol candidate ưu tiên

OpenTelemetry phù hợp để mang correlation xuyên:

```text
Observation
→ Deterministic DecisionPacket
→ orchestrator
→ Agent/MCP tool
→ policy/approval
→ execution
```

### Timing

- M04 optional minimal trace spike.
- M06 recommended khi watcher/orchestration thành runtime thật.
- M08+ propagate trace/correlation qua Agent/tool boundaries.

### Gate

- canonical `correlation_id` mapping trước;
- core result không phụ thuộc exporter availability;
- redaction;
- sampling không làm mất mandatory audit;
- telemetry != canonical audit/business state.

**Official refs:**
- https://opentelemetry.io/docs/languages/go/
- https://opentelemetry.io/docs/languages/

## 13. Langfuse — optional AI/Agent observability + evaluation backend

Langfuse có thể làm optional backend cho M02+ eval và M08+ Agent traces.

Không đặt vào Langfuse:

- canonical Product/evidence/history;
- final grounded/not-grounded truth;
- authorization;
- mandatory audit record duy nhất.

### Gate

```text
manual/repo eval baseline exists first
+ datasets/labels versioned outside vendor-only state
+ secrets/private data redacted
+ Langfuse score cannot become evidence/policy input by default
+ backend outage does not break deterministic core
+ measured debugging/eval value > operational cost
```

**Official refs:**
- https://langfuse.com/self-hosting
- https://langfuse.com/docs/evaluation/experiments/experiments-via-opentelemetry

## 14. Windmill — orchestration comparison candidate

Windmill có thể spike trên cùng M04 read-only workflow khi cần code-friendly scripts/Git sync hoặc operational model khác.

Adopt thay n8n chỉ khi cùng use case chứng minh:

```text
same deterministic input/output contract
+ same authority ceiling
+ Git-reviewable artifacts
+ retry/idempotency rõ
+ secret handling đạt
+ correlation/audit không kém
+ measured operational burden thấp hơn
```

**Official refs:**
- https://www.windmill.dev/docs/getting_started/scripts_quickstart/go
- https://www.windmill.dev/docs/advanced/git_sync

## 15. Temporal — durable execution candidate cho M09+

Temporal chỉ spike khi có **real long-running durability pain** vượt simple n8n/persisted-state baseline.

```text
ActionIntent
→ persist / wait approval
→ restart/delay
→ resume
→ revalidate deterministic policy + approval freshness + kill switch
→ bounded execution
```

Gate:

- documented durability/recovery need;
- idempotent/dedup activities;
- canonical business state external to workflow history;
- resume revalidates approval/policy/kill switch;
- operational complexity justified.

**Official ref:** https://docs.temporal.io/

## 16. OPA — complex policy-as-code candidate cho M09+

OPA phù hợp khi policy complexity vượt visual/simple rule và policy-as-code giúp review/test tốt hơn.

```text
canonical deterministic inputs
→ OPA evaluation
→ canonical authorization mapping/enforcement
→ ALLOW | DENY | WAIT | GET_MORE_DATA | HUMAN_REVIEW
```

OPA không bắt buộc phải nằm “bên trong Go”; Go có thể là adapter/reference implementation. Canonical contract mới là authority.

Gate:

- policy complexity chứng minh được;
- parity tests với current deterministic baseline;
- Rego bundle versioned/reviewed;
- evaluation error/timeout fail closed;
- decision reason/trace audit được;
- no direct canonical state mutation.

**Official ref:** https://www.openpolicyagent.org/docs/integration

## 17. Adoption matrix — default hiện tại

| Capability | Primary/reference hiện tại | Candidate/comparison | Earliest meaningful spike | Default decision |
|---|---|---|---|---|
| Deterministic Domain/Governance | contracts + Go golden oracle | DecisionRules; OPA later | M07 / M09 | no-code visual nếu parity/audit/fail-closed tốt; Go fallback |
| Orchestration | n8n | Windmill | M04 | n8n primary |
| AgentRuntime | **n8n AI Agent visual-first candidate** | Hermes; OpenAI Agents SDK; Flowise watchlist | M08 | reuse n8n trước; thêm runtime khi có measured bottleneck |
| Development Agent | human-reviewed GitHub PR workflow | Copilot cloud agent; Codex; Claude | anytime | delegate code, never delegate merge authority |
| Tool boundary | explicit Tool Registry | MCP | M08 | MCP preferred protocol candidate |
| Browser acquisition | HTTP/API/manual | Playwright | M06 | browser only when needed |
| Observability | correlation/audit contract | OpenTelemetry | M04/M06 | adopt cross-runtime when useful |
| AI eval backend | repo fixtures/reports | Langfuse | M02 optional | only after baseline |
| Durable workflow | n8n + persisted canonical state | Temporal | M09 | only on real durability pain |

## 18. Reference architecture

```text
                  Deterministic Core CONTRACTS
             evidence + history + decision + policy
                         /              \
             Go reference              DecisionRules
              / fallback               visual candidate
                         \              /
                          canonical result
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
       Orchestration       Intelligence      Observability
           n8n          n8n AI Agent first   OpenTelemetry
              │          Hermes / OpenAI           │
              │                 │               Langfuse
              │                MCP
              │                 │
              └──────── External/read tools ───────┘
                                │
                            Playwright

Development plane (outside runtime authority):
Issue/spec → Copilot/Codex/Claude → PR → CI → Human Review

Later only when justified:
Temporal = durable workflow/HITL
OPA      = complex policy-as-code
Flowise  = Agent visual runtime comparison
```

Required consequential path:

```text
Agent/tool candidate evidence/proposal
→ Deterministic Core validation/grounding
→ deterministic Decision/Policy
→ ActionIntent
→ orchestration/durable routing
→ approval/revalidation khi required
→ bounded execution
→ ExecutionRecord
```
