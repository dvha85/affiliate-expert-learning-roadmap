# n8n Orchestration Standard — Chuẩn workflow, versioning và security

## 1. Mục tiêu

n8n là primary orchestration reference từ các Mission phù hợp, nhưng không phải domain truth/policy authority.

```text
n8n execution state/history
≠ canonical business state
```

Workflow capability không tự cấp quyền.

## 2. Adoption theo Mission

- M00–M03: không dùng n8n cho Core.
- M04: read-only/import learning slice; manual trigger, mapping, call Go, failure handling; không external mutation.
- M06+: reliable watcher/orchestration; security review trở thành Operated gate.
- M09+: shadow/approval routing.
- M10+: bounded execution chỉ sau deterministic authorization.

## 3. Workflow-as-code baseline

Khi n8n được dùng trong Core/learner artifact, workflow export phải được version trong repo thay vì chỉ tồn tại trên canvas/runtime.

Portable layout tham chiếu:

```text
lab/orchestration/n8n/
  workflows/
    m04-import-analytics.json
    m06-product-watcher.json
  metadata/
    m04-import-analytics.yaml
    m06-product-watcher.yaml
  fixtures/
  expected/
  README.md
```

Không yêu cầu paid source-control feature của n8n; Git repo là portable baseline.

## 4. Metadata contract

Mỗi workflow cần metadata machine/human-readable gồm tối thiểu:

- workflow name/version;
- Mission;
- authority ceiling;
- allowed side effects;
- required Go/domain contract/API version;
- expected inputs/outputs;
- idempotency strategy;
- retry/failure policy;
- correlation ID strategy;
- credential **names/scopes**, không chứa secret values;
- rollback/import instructions.

## 5. Review và rollback

Workflow change phải review như code:

```text
export
→ inspect diff
→ validate metadata/authority
→ test fixture + failure path
→ review secrets/credentials
→ merge
→ deploy/import
```

Rollback phải xác định được workflow artifact/version trước đó. Runtime canvas không được là bản duy nhất có thể khôi phục.

## 6. Secrets

Không commit:

- API keys/tokens;
- passwords;
- credential payloads;
- production webhook secrets;
- personal/account identifiers không cần thiết.

Exported workflow phải tham chiếu credential logical name/scope. Log/fixture phải sanitize secrets.

## 7. Operational security gate từ M06

Khi n8n trở thành runtime thực sự, Mission Operated/PASS yêu cầu security evidence phù hợp deployment.

Checklist tối thiểu:

- chạy n8n security audit (`n8n audit`) khi deployment hỗ trợ CLI đó, hoặc equivalent documented review;
- credential least privilege;
- inventory/review risky, community và custom nodes;
- webhook exposure/authentication review;
- consequential/write endpoint không bypass Go policy/authorization;
- secret leakage review trong workflow export, log và fixture;
- runtime/version freshness recorded;
- kill switch/execution-disable path được test ở Mission có external action authority.

Security audit PASS không tự chứng minh business policy đúng; đây là operational gate bổ sung.

## 8. Webhook boundary

Read-only webhook vẫn phải validate schema/provenance.

Write/consequential path bắt buộc:

```text
request/event
→ authenticated/integrity-checked boundary
→ canonical Decision/ActionIntent
→ deterministic Go PolicyDecision
→ required approval/revalidation
→ bounded executor
```

Không cho phép:

```text
public webhook
→ n8n IF/Switch
→ consequential action
```

nếu thiếu canonical policy/authorization gate.

## 9. Runtime failure

- duplicate execution không tạo duplicate canonical record/side effect;
- retry chỉ khi operation safe/idempotent;
- n8n unavailable không corrupt canonical evidence/history/action state;
- execution history loss không xóa canonical approval/execution evidence;
- `workflow succeeded` không đồng nghĩa business action authorized/succeeded.

## 10. Canonical rule

```text
Go/domain store owns truth, policy and canonical action state.
n8n owns orchestration execution.
Git owns reviewable workflow artifacts.
Security gate grows with authority.
```
