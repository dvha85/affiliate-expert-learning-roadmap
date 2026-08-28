# Autonomy and Approval Model

> Governance standard for bots that act automatically while the human operator approves consequential actions.

## 1. Goal

The target system is not fully manual and not unconstrained autonomy.

```text
observe
→ analyze
→ create ActionIntent
→ classify risk
→ policy decision
→ execute automatically OR request approval
→ audit
→ measure result
```

## 2. Core entities

### ActionIntent

Describes the proposed action before execution.

Minimum fields:

```text
id
intent_type
requested_by
reason
inputs
expected_effect
risk_level
created_at
expires_at
idempotency_key
```

### RiskLevel

```text
RISK 0 — routine/reversible/internal
RISK 1 — controlled side effect with mandatory audit
RISK 2 — consequential; human approval required
```

### PolicyDecision

```text
ALLOW
ALLOW_WITH_AUDIT
REQUIRE_APPROVAL
DENY
```

Include policy version and explanation.

### ApprovalRequest

Must include enough context for a fast human decision:

- what will happen;
- why the bot proposes it;
- evidence/source provenance;
- expected benefit;
- risk/downside;
- expiry;
- exact side effect;
- rollback/compensation path when available.

### ApprovalDecision

```text
APPROVE
REJECT
EXPIRE
CANCEL
```

Store decision time, actor and reason.

### ExecutionRecord

Record:

- action intent;
- policy decision;
- approval decision if any;
- execution attempt(s);
- external request/result IDs;
- idempotency key;
- final state;
- error/compensation;
- measured result.

## 3. Risk examples

### RISK 0

Usually internal/read-only actions:

- collect product data;
- refresh a snapshot;
- calculate metrics;
- update ranking cache;
- generate internal report;
- detect anomaly;
- create an alert.

### RISK 1

Potential controlled examples:

- change internal product priority;
- enable/disable a watcher;
- create a draft;
- adjust a bounded experiment configuration;
- update an internal recommendation state.

These require audit and bounded policy constraints.

### RISK 2

Usually approval-required:

- publish external content;
- spend money;
- change account/platform settings;
- delete important data;
- send consequential external communication;
- modify production/security configuration;
- execute actions with material legal/compliance impact.

Exact classification is policy-specific and may change with scope.

## 4. Approval workflow

```text
ActionIntent
→ Policy Engine
→ REQUIRE_APPROVAL
→ persist workflow state
→ create ApprovalRequest
→ notify human
→ wait durably
   ├── APPROVE → resume → revalidate → execute
   ├── REJECT  → terminate
   ├── EXPIRE  → terminate/re-plan
   └── CANCEL  → terminate
→ audit final state
```

## 5. Revalidation before execution

Approval does not mean “execute forever”. Before execution, re-check:

- approval not expired;
- product/price/commission still current;
- policy version still valid;
- action not already executed;
- credentials/permissions still valid;
- external target still exists;
- risk has not increased.

If material context changed, create a new approval request.

## 6. Idempotency

Every side-effecting action should have an idempotency strategy.

Examples:

```text
publish:<content-id>:<version>
alert:<event-id>:<channel>
workflow:<workflow-id>:<step>
```

Retry must not silently create duplicate external effects.

## 7. Kill switch

Production autonomous systems need at least:

- global execution disable;
- action-type disable;
- platform/tool disable;
- emergency credential revocation path;
- ability to keep collection/analysis running while side effects are disabled.

Preferred behavior:

```text
ANALYZE may continue
ACT can be disabled independently
```

## 8. Human experience principle

The operator should review **decisions**, not babysit every mechanical step.

A useful approval should be answerable from a concise decision packet, not require reading raw logs.

## 9. Metrics

Track:

- auto-execution rate;
- approval-required rate;
- approval acceptance/rejection rate;
- approval latency;
- expired requests;
- duplicate-prevention events;
- policy blocks;
- rollback/compensation rate;
- human intervention rate;
- outcome after approved vs auto actions.

## 10. Anti-patterns

Do not:

- let the LLM assign and approve its own high-risk action;
- use a chat message as the only approval record;
- hold approval state only in process memory;
- execute after approval when critical facts changed materially;
- retry side effects without idempotency;
- make the kill switch depend on the same failing agent workflow;
- classify everything RISK 2 and turn the human into a bottleneck.
