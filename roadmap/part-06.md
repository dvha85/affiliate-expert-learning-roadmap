# Phần 6 — Vòng production Hybrid khép kín

- Timeline: **Evidence-gated; includes a production observation window**.
- **Chapters:** C18–C20
- **Core:** 9 micro-lessons
- **Mission:** M11
- **Outcome:** Hybrid Affiliate Intelligence Bot chạy qua một observation window thật với Go core, orchestration runtime và Agent intelligence có recovery/security controls, end-to-end trace và reviewed improvement từ outcome.

## Production ownership

```text
Go
= canonical evidence/state + Decision/Policy contracts + authorization + audit semantics

n8n
= production orchestration reference
= triggers + integrations + workflow state/routing + bounded execution

AgentRuntime
= production intelligence worker
= research/reasoning/tools chỉ trong permission + data-scope ceiling

Human
= consequential approval/review + incident override + reviewed improvement release
```

M11 không biến n8n/Agent thành source of truth. Production maturity là khả năng **phối hợp nhiều runtime nhưng vẫn giữ một authority chain audit được**.

## Attempt trước knowledge pull

Deploy capability nhỏ nhất an toàn, chạy qua declared observation window, chủ động tạo failure/restart cases ở từng runtime và thực hiện kill-switch drill.

Không đợi “production hoàn hảo” mới quan sát operational evidence.

Tối thiểu thử:

1. Go core restart/unavailable case;
2. n8n workflow failure/retry/duplicate case;
3. Agent unavailable/invalid/tool failure case;
4. stale/expired approval case;
5. một data-scope/minimisation failure khi integration/tool có privacy relevance;
6. kill-switch case;
7. recovery rồi replay một end-to-end trace.

## Core checklist

### Chương 18 — Deploy và operate hybrid runtime

- [ ] **18.1** — Configuration, packaging, migration và environment boundary
- [ ] **18.2** — Health check, structured logs, metrics và operational alerts
- [ ] **18.3** — Backup/restore, recovery verification, cost và SLO

Operational view phải tách được ít nhất:

```text
Go core health
n8n orchestration health
AgentRuntime health
external dependency health
```

Một dashboard xanh của orchestrator không được che việc Go policy/Agent/external source đang fail.

### Chương 19 — Security và incident containment

- [ ] **19.1** — Secrets, authentication, authorization và data boundary
- [ ] **19.2** — Prompt injection/tool misuse test và least-privilege containment
- [ ] **19.3** — Incident drill, kill switch, replay và recovery evidence

Cross-runtime security/data rule:

- secrets chỉ tồn tại ở runtime cần chúng;
- Agent không mặc định nhận orchestration/platform credentials;
- n8n không nhận quyền sửa Go policy/business truth;
- Go core không cần giữ mọi integration credential nếu orchestrator sở hữu adapter đó;
- personal/customer/account data chỉ đi tới runtime/provider thật sự cần cho declared purpose;
- ưu tiên aggregate/reference/redacted data khi đủ cho Mission outcome;
- retention/downstream sharing phải theo `DataAccessContext` khi relevant;
- log/traces phải redact sensitive values nhưng giữ correlation và đủ metadata để audit purpose/data scope.

Invariant:

```text
permission to access
≠ permission to collect/store/share without purpose boundary
```

### Chương 20 — Closed-loop learning

- [ ] **20.1** — Weekly business/decision review từ real outcomes
- [ ] **20.2** — Calibration, drift và reviewed proposed improvement
- [ ] **20.3** — End-to-end trace, capstone demo, retrospective và next cycle

Learning loop:

```text
production outcome
→ evaluation
→ proposed change
→ offline/replay tests
→ human review
→ versioned release/reject
```

Không cho Agent/n8n tự sửa production prompt, policy, formula, workflow authority, data-access scope hoặc weights dựa chỉ trên một outcome.

## Cross-runtime fail-safe invariants

```text
Agent unavailable
≠ core deterministic decision unavailable
```

Nếu Agent fail:

- reject/fallback/abstain theo Decision contract;
- không dùng stale Agent output như fresh analysis;
- no silent permission/data-scope expansion.

```text
n8n unavailable
≠ canonical evidence/history corrupted
```

Nếu orchestration fail:

- no fake success;
- retry/idempotency/recovery rõ;
- canonical persisted state vẫn audit được;
- consequential side effect không được lặp khi replay;
- không replay raw sensitive payload sang downstream ngoài retention/scope chỉ để “khôi phục workflow”.

```text
Go Policy unavailable
→ no consequential execution
```

Không fallback sang workflow IF node hoặc Agent judgment để “giữ hệ thống chạy”.

## End-to-end trace contract

Production trace phải nối được:

```text
Trigger
→ WorkflowExecution
→ Evidence refs
→ DataAccessContext/ref khi relevant
→ SignalPacket
→ Agent Analysis/tool trace nếu có
→ DecisionPacket
→ ActionIntent
→ PolicyDecision
→ Approval nếu required
→ ExecutionRecord
→ Outcome
→ Evaluation
```

Correlation ID phải survive cross-runtime boundaries. Trace phải chứng minh được access/action flow mà không cần lưu raw secret/full personal payload.

## Recovery matrix

| Failure | Expected safe behavior |
|---|---|
| Go core unavailable | stop dependent decisions/actions; no policy bypass |
| n8n unavailable | orchestration delayed/degraded; no history corruption |
| Agent unavailable | deterministic fallback/abstain |
| Agent malformed/unsupported output | reject/fallback |
| read-only tool returns excess personal data | minimise/redact/reject outside purpose; no silent retention |
| downstream provider receives data outside declared scope | block/contain + incident evidence |
| duplicate workflow replay | idempotent; no duplicate side effect |
| stale/expired approval | deny/revalidate |
| external API timeout | explicit retry/backoff/failure state |
| context changed after approval | revalidation fails; no execute |
| kill switch ON | all governed external execution blocked |

## Production kill switch

Kill switch phải được kiểm ở execution boundary, không chỉ UI/orchestration layer.

```text
approved ActionIntent
+ Agent confident
+ n8n ready
+ kill switch ON
→ NO EXECUTION
```

Learner phải drill ít nhất một case đang có pending/approved work rồi bật kill switch và chứng minh executor từ chối.

Kill switch external action không phải privacy override: collection/analysis chỉ tiếp tục trong permission/data purpose hiện hành.

## Framework replaceability check

M11 capstone phải giải thích:

- phần nào là Go/domain contract;
- phần nào là n8n implementation detail;
- phần nào là AgentRuntime implementation detail;
- phần nào là permission/data-governance contract phải giữ bất kể runtime;
- nếu thay n8n/Hermes bằng runtime khác thì contracts/evidence nào phải giữ nguyên.

Production PASS không phụ thuộc vào vendor name; nó phụ thuộc behavior, evidence, authority, data boundary và recovery.

## Part PASS

- [ ] M11 có Capability PASS, Reality verified cấp E6 và Operated
- [ ] Bot chạy qua declared observation window với operational evidence
- [ ] Go/n8n/Agent/external health/failure boundaries quan sát được
- [ ] Recovery và kill-switch drill có artifact
- [ ] Duplicate/retry/restart không tạo consequential side effect trùng
- [ ] Agent unavailable/invalid vẫn có deterministic fallback/abstention
- [ ] n8n unavailable không corrupt canonical evidence/history
- [ ] Go Policy unavailable không có consequential execution
- [ ] Production data flow giữ purpose/minimisation/retention/downstream-sharing boundary khi relevant
- [ ] Trace nối được trigger → evidence/data context → analysis → decision → policy/approval → action → outcome → evaluation
- [ ] Trace/audit không mặc định lưu raw secret/full personal data
- [ ] Outcome learning tạo proposed change qua test/review, không tự sửa production behavior/data scope
- [ ] Runtime implementations có thể thay mà không đổi canonical domain/authority/data-governance contracts

[← Part trước](part-05.md) · [Roadmap tổng](../ROADMAP.md)
