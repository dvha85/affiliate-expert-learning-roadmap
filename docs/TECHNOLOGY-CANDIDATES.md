# Technology References — Runtime và công cụ hỗ trợ cho kiến trúc Hybrid

- **Status:** Reference only — không phải Core/PASS shortcut
- **Last reviewed:** 2026-09-02
- **Primary architecture authority:** [`ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md)

Tài liệu này không quyết định learner sequence. Nó ghi reference implementation, comparison candidate và adoption gate cho các runtime/công cụ nằm ngoài Go domain/governance core.

Nguyên tắc chung:

```text
Tool available
≠ tool adopted

Tool adopted
≠ tool owns truth

Framework capability
≠ Bot authority
```

Mọi candidate chỉ được adopt khi giải quyết bottleneck đã quan sát được và không làm thay đổi Mission authority ceiling.

## 1. Canonical ownership

```text
Go core
= evidence / history / deterministic decision / policy / audit

n8n
= primary orchestration reference

AgentRuntime
= intelligence role
Hermes Agent
= primary reference/candidate implementation cho tool-use stage

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
= policy implementation candidate dưới Go-owned authorization contract
```

Windmill là **orchestration comparison candidate**; OpenAI Agents SDK là **AgentRuntime comparison candidate**. Không candidate nào tự trở thành canonical owner chỉ vì framework có feature tương ứng.

## 2. n8n — primary orchestration reference

### Role phù hợp

- trigger / schedule / webhook;
- API/integration glue;
- analytics/import workflow;
- notification/alert routing;
- approval routing;
- calling Go service/CLI/API;
- bounded execution sau Go policy gate.

Không đặt canonical authority của các phần sau vào n8n:

- Product ranking truth;
- evidence truth classification;
- deterministic risk policy;
- final `ALLOW | DENY | WAIT | HUMAN_REVIEW`;
- canonical business state nếu không có explicit persistence/audit contract.

### Roadmap learning progression

| Mission | n8n role |
|---|---|
| M00–M03 | Không cần cho Core |
| M04 | **First read-only learning slice**: manual trigger → import/map → call Go → failure handling; không external mutation |
| M05 | Optional reporting/orchestration |
| M06 | **Primary watcher/orchestration reference**: trigger/integration/retry/alert |
| M07–M08 | Route DecisionPacket / Agent requests nhưng không thay policy |
| M09 | **Shadow + durable approval routing reference** |
| M10 | **Bounded governed execution reference** sau deterministic policy gate |
| M11 | Production orchestration candidate/reference |

### Adoption gate

n8n chỉ được đưa vào implementation khi giải quyết bottleneck cụ thể và learner chứng minh:

```text
Go contract giữ nguyên
+ failure/retry behavior rõ
+ idempotency
+ audit/correlation
+ secret handling
+ workflow artifact reviewable/versioned
+ no authority bypass
```

Nếu một Go script/service đơn giản hơn và ít failure surface hơn, không bắt buộc dùng n8n.

## 3. Windmill — orchestration comparison candidate

Windmill đáng spike vì hỗ trợ Go scripts trực tiếp; scripts có thể chạy độc lập, scheduled hoặc ghép thành Flow. Official docs cũng có Git sync/versioning workflow. Đây là lợi thế tiềm năng cho một curriculum lấy Go làm domain language, nhưng **không phải lý do đủ để thay n8n**.

### Candidate timing

- M00–M03: không dùng cho Core.
- M04: có thể làm **comparison spike** trên đúng read-only import workflow của n8n.
- M06: chỉ cân nhắc thay/đồng tồn tại nếu measured operational simplicity tốt hơn.
- M09+: có thể được đánh giá cho approval/execution workflow nếu state/retry/audit contract đáp ứng.

### Adoption gate

Chỉ adopt Windmill thay n8n cho một role khi cùng một bounded use case chứng minh:

```text
same Go input/output contract
+ same authority ceiling
+ Git-reviewable workflow artifacts
+ retry/error semantics rõ
+ idempotency proof
+ secret handling đạt
+ correlation/audit không kém n8n baseline
+ measured operational burden thấp hơn hoặc capability cần thiết tốt hơn
```

Không đổi primary reference trong curriculum chỉ vì code-first UX hợp sở thích hơn.

**Official refs:**
- https://www.windmill.dev/docs/getting_started/scripts_quickstart/go
- https://www.windmill.dev/docs/advanced/git_sync

## 4. AgentRuntime — intelligence role

Canonical abstraction là `AgentRuntime`, không phải vendor name.

Potential role:

- unstructured analysis;
- research;
- read-only missing-evidence acquisition;
- tool use qua explicit Tool Registry;
- decomposition/delegation;
- candidate hypotheses/proposals.

Không cho Agent mặc định:

- biến inference thành measured fact;
- sửa canonical Product/history/scoring input;
- tự quyết định final risk class;
- bypass Go policy;
- publish/send/spend/change account ngoài Mission authority.

### Roadmap progression

| Mission | Agent role |
|---|---|
| M00–M01 | Không dùng |
| M02 | AI advisory, no tools, strict grounding/fallback |
| M03–M07 | Advisory/analysis only; tool-use chưa phải Core |
| M08 | **First read-only AgentRuntime tool-use** |
| M09 | Agent có thể propose `ActionIntent`, không execute |
| M10 | Governed reasoning trong permission/policy ceiling |
| M11 | Production intelligence nhưng vẫn không tự tăng authority |

## 5. Hermes Agent — primary Agent reference/candidate

Hermes Agent được giữ như **reference/candidate implementation** để spike ở M08 khi:

- có missing-evidence case thật;
- manual/deterministic retrieval bắt đầu tốn công;
- Tool Registry/permission/audit có thể map rõ vào runtime.

Spike phải so:

```text
manual/deterministic retrieval baseline
vs
Hermes read-only AgentRuntime
```

Theo:

- evidence correctness/grounding;
- unsupported claim rate;
- tool-call success/failure;
- permission compliance;
- prompt-injection resistance;
- auditability;
- latency/cost;
- human intervention rate.

Nếu framework không enforce được permission/audit/fallback theo contract repo, **không adopt** dù demo trông thông minh.

## 6. OpenAI Agents SDK — AgentRuntime comparison candidate

OpenAI Agents SDK hiện cung cấp agent runner với tools, guardrails, handoffs, sessions, tracing, MCP integration và human-in-the-loop approval. Đây là candidate phù hợp để so với Hermes ở M08+, nhưng SDK capability không thay `AGENT SAFE PROFILE` của repo.

### Candidate timing

- M02: không dùng SDK tool loop để vượt khỏi AI Advisor A1.
- M03–M07: optional research/reference, không Core dependency.
- M08: comparison spike với Hermes cho read-only tool use.
- M09+: chỉ có thể propose hoặc pause xin approval trong authority ceiling hiện tại.

### Adoption gate

```text
same M08 fixture/eval set
+ explicit tool allowlist/filter
+ least-privilege credentials
+ approval/guardrail behavior tested
+ MCP server trust boundary explicit nếu dùng MCP
+ all tool output UNTRUSTED UNTIL GO VALIDATION
+ deterministic fallback survives provider/runtime failure
+ trace/correlation maps về repo audit contract
+ no direct consequential action bypassing Go policy
```

Built-in HITL/guardrails là implementation aid, **không phải bằng chứng rằng policy đã đúng**.

**Official refs:**
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/mcp/

## 7. MCP — chuẩn ứng viên cho Tool Registry boundary

Model Context Protocol (MCP) là protocol để ứng dụng expose context/tools cho AI clients. Bản spec được kiểm tại thời điểm review là `2026-07-28`; revision này tiếp tục harden authorization và chuyển core transport theo hướng stateless hơn.

MCP phù hợp để chuẩn hóa boundary:

```text
AgentRuntime
→ MCP client
→ approved MCP server/tool
→ result
→ Go validate / ground
```

Nhưng invariant bắt buộc:

```text
MCP tool visible
≠ tool permitted

MCP call succeeded
≠ result is trusted evidence

MCP auth succeeded
≠ consequential action authorized
```

### Candidate timing

- M00–M07: không cần cho Core.
- M08: **first candidate protocol** cho read-only Agent tool boundary.
- M09+: có thể expose proposal/supporting tools; write/action tool vẫn chịu Mission authority + Go policy + approval.

### Adoption gate M08

- explicit server allowlist;
- explicit tool allowlist/filter;
- read-only capability ở M08;
- credentials least privilege;
- secret/token không nằm trong URL hoặc model-visible text;
- mỗi call có correlation/audit metadata;
- timeout/retry/failure semantics rõ;
- tool output bị coi là untrusted input;
- Go evidence validator quyết định claim support;
- sensitive/write tools require separate policy/approval gate ở Mission sau.

**Official refs:**
- https://modelcontextprotocol.io/specification/2026-07-28
- https://blog.modelcontextprotocol.io/posts/2026-07-28/

## 8. Playwright — controlled browser acquisition candidate

Playwright phù hợp khi public source cần browser rendering/interaction để quan sát dữ liệu mà HTTP/API fetch đơn giản không đủ. Nó hỗ trợ Chromium, Firefox và WebKit, cùng headless execution cho automation.

Candidate role:

```text
public dynamic page
→ controlled Playwright session
→ raw observation/snapshot
→ provenance
→ Go validation/normalization
```

### Candidate timing

- M06: deterministic watcher candidate cho **public read-only acquisition** khi source thật yêu cầu browser.
- M08: có thể expose như read-only Agent tool qua explicit Tool Registry.
- M09–M10: không tự động biến browser thành publish/purchase/account-change surface.

### Adoption gate

```text
plain HTTP/API baseline proven insufficient
+ domain/URL allowlist
+ public/read-only profile for M06/M08
+ bounded navigation/timeout/rate limit
+ no arbitrary form submit/upload/account mutation
+ provenance captures source URL + observed_at + acquisition method
+ page/tool output remains untrusted until Go validation
+ platform terms/compliance reviewed for target source
+ browser failure does not mutate canonical state
```

Consequential browser action nếu sau này có phải là **separate Action capability**, không phải side effect ẩn của evidence acquisition.

**Official ref:**
- https://playwright.dev/docs/browsers

## 9. OpenTelemetry — observability protocol candidate ưu tiên

OpenTelemetry là candidate chuẩn cho cross-runtime traces/metrics. Tại thời điểm review, official Go status ghi **Traces: Stable, Metrics: Stable, Logs: Beta**.

Phù hợp với repo vì correlation có thể đi xuyên:

```text
Observation
→ Go DecisionPacket
→ orchestrator
→ Agent/MCP tool
→ policy/approval
→ execution
```

mà không giao canonical business truth cho telemetry backend.

### Candidate timing

- M00–M03: không cần cho PASS.
- M04: optional minimal trace spike ở first cross-runtime workflow.
- M06: **recommended adoption point** khi watcher/orchestration trở thành runtime thật.
- M08+: propagate trace/correlation qua Agent/tool boundaries.

### Adoption gate

- canonical `correlation_id`/trace mapping được định nghĩa trước;
- Go domain result không phụ thuộc exporter availability;
- telemetry failure không làm corrupt evidence/history;
- secret/private payload redaction rõ;
- semantic attributes đủ để nối Decision → tool/workflow → outcome;
- sampling không làm mất mandatory audit record;
- audit record và telemetry được phân biệt rõ: **telemetry != canonical audit state**.

**Official refs:**
- https://opentelemetry.io/docs/languages/go/
- https://opentelemetry.io/docs/languages/

## 10. Langfuse — optional AI/Agent observability + evaluation backend

Langfuse là open-source LLM/AI observability platform có self-host option. Current docs hỗ trợ OpenTelemetry ingestion và experiments/evaluation workflows, vì vậy nó phù hợp làm optional backend cho M02+ eval và M08+ Agent traces.

Không đặt vào Langfuse:

- canonical Product/evidence/history;
- final grounded/not-grounded truth;
- authorization;
- mandatory audit record duy nhất.

### Candidate timing

- M02: optional eval spike **sau khi** deterministic baseline + frozen eval fixtures tồn tại.
- M06: optional observability backend qua OpenTelemetry.
- M08+: useful cho Agent/model/tool trace và regression evaluation.

### Adoption gate

```text
manual/repo eval baseline exists first
+ OpenTelemetry-first trace integration when practical
+ dataset/eval labels remain versioned/reviewable outside vendor-only state
+ secrets/private data redacted
+ Langfuse score cannot become evidence or policy input by default
+ export/backend outage does not break deterministic core
+ measured debugging/eval value > operational cost
```

Nếu dashboard đẹp nhưng không cải thiện regression detection, auditability hoặc debugging, không cần adopt.

**Official refs:**
- https://langfuse.com/self-hosting
- https://langfuse.com/docs/evaluation/experiments/experiments-via-opentelemetry
- https://langfuse.com/docs/api-and-data-platform/features/public-api

## 11. Temporal — durable execution candidate cho M09+

Temporal phù hợp cho workflow cần survive process crash, network failure hoặc wait dài rồi resume. Đây là candidate cho **durable execution / long-running HITL**, không phải early orchestration dependency.

Potential future flow:

```text
ActionIntent
→ persist / wait approval
→ process restart or long delay
→ resume
→ revalidate Go policy + approval freshness + kill switch
→ bounded execution
```

### Candidate timing

- M00–M08: **không adopt cho Core**.
- M09: spike chỉ khi shadow/approval flow đã có real durability pain.
- M10–M11: production candidate khi workflows thực sự cần long-lived recovery semantics.

### Adoption gate

- measured need vượt khả năng của simple Go job/n8n workflow hiện tại;
- long-running state/retry/recovery requirement documented;
- every consequential activity idempotent hoặc có dedup key;
- canonical business state vẫn nằm ở Go-owned persistence contract;
- resume luôn revalidate approval expiry, policy và kill switch;
- runtime outage không mất ActionIntent/ExecutionRecord contract;
- operational complexity/cost justified by failure-recovery benefit;
- no workflow history is treated as substitute for canonical evidence/history.

Temporal durability:

```text
durable resume
≠ authorization to continue
```

**Official ref:**
- https://docs.temporal.io/

## 12. OPA — policy-as-code implementation candidate cho M09+

Open Policy Agent (OPA) có thể embed vào Go qua SDK/Rego API và phù hợp khi deterministic policy tăng đủ phức tạp để tách policy-as-code giúp review/test tốt hơn.

OPA không thay ownership contract:

```text
Go-owned canonical inputs
→ OPA policy evaluation candidate
→ Go maps/enforces canonical authorization contract
→ ALLOW | DENY | WAIT | GET_MORE_DATA | HUMAN_REVIEW
```

### Candidate timing

- M00–M08: giữ policy trực tiếp trong Go nếu đơn giản hơn.
- M09: optional spike khi risk/action policy bắt đầu có nhiều actor/platform/environment rule.
- M10–M11: adopt chỉ khi policy-as-code có measured maintainability/audit advantage.

### Adoption gate

- policy complexity/bottleneck được chứng minh, không adopt vì trend;
- parity tests với existing deterministic Go policy trước migration;
- policy bundle/Rego versioned + reviewed trong Git;
- input schema do Go kiểm soát;
- evaluation error/timeout fail closed theo contract;
- decision reason/trace đủ audit;
- OPA không đọc/mutate canonical state ngoài explicit input;
- Go boundary vẫn là nơi phát canonical authorization result.

**Official ref:**
- https://www.openpolicyagent.org/docs/integration

## 13. Adoption matrix — default hiện tại

| Capability | Primary/reference hiện tại | Candidate mới | Earliest meaningful spike | Default decision |
|---|---|---|---|---|
| Domain/Governance | Go | OPA cho complex policy | M09 | Giữ Go; OPA chỉ khi policy complexity có thật |
| Orchestration | n8n | Windmill | M04 | n8n vẫn primary; compare trên cùng read-only slice |
| AgentRuntime | Hermes Agent candidate/reference | OpenAI Agents SDK | M08 | Compare cùng Safe Profile/eval set |
| Tool boundary | explicit Tool Registry contract | MCP | M08 | MCP preferred protocol candidate, permission vẫn ngoài protocol |
| Browser acquisition | HTTP/API/manual baseline | Playwright | M06 | Chỉ khi browser thực sự cần |
| Observability protocol | correlation/audit contract | OpenTelemetry | M04/M06 | Ưu tiên khi bắt đầu cross-runtime |
| AI/Agent eval backend | repo fixtures/reports | Langfuse | M02 optional | Chỉ sau deterministic/manual eval baseline |
| Durable workflow | n8n/Go bounded workflow | Temporal | M09 | Chỉ khi long-running durability là bottleneck |

## 14. Hybrid architecture reference

```text
                         Go Core
          evidence + history + decision + policy
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
   Orchestration       Intelligence      Observability
   n8n / Windmill      AgentRuntime      OpenTelemetry
          │          Hermes / OpenAI           │
          │                 │               Langfuse
          │                MCP
          │                 │
          └──────── External/read tools ───────┘
                            │
                        Playwright

Later, only when justified:
Temporal = durable workflow/HITL
OPA      = complex policy-as-code implementation
```

Required flow cho consequential path vẫn là:

```text
Agent/tool candidate evidence/proposal
→ Go validation/grounding
→ Go Decision/Policy
→ ActionIntent
→ orchestration/durable routing
→ approval/revalidation khi required
→ bounded execution
→ ExecutionRecord
```

Không cho phép:

```text
Agent confidence → direct execution
MCP tool available → permission granted
browser navigation → trusted evidence
Langfuse score → canonical fact
Temporal resume → permission to execute
OPA rule exists → bypass Go authorization contract
```

## 15. Replaceability

| Role | Primary reference | Mandatory? |
|---|---|---|
| Domain/Governance core | Go | Go là primary learner path |
| Orchestration | n8n | Không; contract/behavior mới là gate |
| Orchestration comparison | Windmill | Không |
| AgentRuntime | Hermes Agent candidate/reference | Không |
| AgentRuntime comparison | OpenAI Agents SDK | Không |
| Tool interoperability | MCP candidate | Không |
| Browser acquisition | Playwright candidate | Không |
| Telemetry | OpenTelemetry candidate | Không |
| AI/Agent observability/eval | Langfuse candidate | Không |
| Durable execution | Temporal candidate | Không |
| Policy implementation | OPA candidate | Không |

Một runtime/tool khác có thể thay candidate nếu đáp ứng tốt hơn permission, audit, retry/recovery, cost, security và operational simplicity mà không đổi Mission outcome.

## 16. Freshness note

Các capability, license/deployment model, SDK status, security guidance và tool-permission behavior thay đổi nhanh. Trước mỗi spike/adoption phải kiểm official docs/current version tại thời điểm đó.

Đặc biệt phải re-check trước adoption:

- OpenTelemetry signal/SDK maturity;
- Langfuse ingestion/self-host/version requirements;
- MCP specification + authorization revision;
- Windmill/n8n licensing, Git/versioning và self-host behavior;
- AgentRuntime tool approval/guardrail semantics;
- Playwright/browser/platform compatibility;
- Temporal deployment/durability semantics;
- OPA SDK/Rego compatibility.

Không đóng băng current feature list thành curriculum truth.