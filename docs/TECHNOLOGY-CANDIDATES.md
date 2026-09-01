# Technology References — n8n và Agent Runtime trong kiến trúc Hybrid

- **Status:** Reference only — không phải Core/PASS shortcut
- **Last reviewed:** 2026-09-02
- **Primary architecture authority:** [`ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md`](ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md)

Tài liệu này không quyết định learner sequence. Nó ghi reference implementation và adoption gate cho hai runtime role ngoài Go core.

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
```

Framework capability không tự tăng Bot authority.

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
+ no authority bypass
```

Nếu một Go script/service đơn giản hơn và ít failure surface hơn, không bắt buộc dùng n8n.

## 3. AgentRuntime — intelligence role

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

## 4. Hermes Agent — primary Agent reference/candidate

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

## 5. Hybrid architecture reference

```text
                     Go Core
        evidence + history + decision + policy
                        │
             ┌──────────┴──────────┐
             │                     │
        n8n runtime           AgentRuntime
      orchestration          intelligence
             │                     │
             └──────────┬──────────┘
                        │
                  External world
```

Required flow cho consequential path:

```text
Agent candidate evidence/proposal
→ Go validation/grounding
→ Go Decision/Policy
→ ActionIntent
→ n8n routing/execution workflow
→ approval/revalidation khi required
→ ExecutionRecord
```

Không cho phép:

```text
Agent confidence → direct execution
```

hoặc:

```text
n8n branch → bypass deterministic RISK policy
```

## 6. Replaceability

| Role | Primary reference | Mandatory? |
|---|---|---|
| Domain/Governance core | Go | Go là primary learner path |
| Orchestration | n8n | Không; contract/behavior mới là gate |
| AgentRuntime | Hermes Agent candidate/reference | Không |

Một runtime khác có thể thay n8n/Hermes nếu đáp ứng tốt hơn permission, audit, retry/recovery, cost, security và operational simplicity mà không đổi Mission outcome.

## 7. Freshness note

Capabilities, license/deployment model, security và tool-permission behavior của n8n/Hermes thay đổi nhanh. Trước mỗi spike/adoption phải kiểm official docs/current version tại thời điểm đó.

Không đóng băng current feature list thành curriculum truth.
