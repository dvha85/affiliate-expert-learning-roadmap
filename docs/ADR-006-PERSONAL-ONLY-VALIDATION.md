# ADR-006 — Personal-only validation và activation

**Status:** Accepted — 2026-09-02
**Decision owner:** repository owner
**Supersedes:** các điều kiện group/public curriculum validation trong ADR-002,
ADR-005 và migration guide đối với repository này; không thay evidence ladder,
Mission PASS hay authority ceiling của ADR-004/ADR-005.

## Context

Repository này phục vụ một owner tự học, tự xây và tự vận hành Affiliate
Intelligence Bot. Việc tuyển hoặc quản lý một nhóm learner không thuộc product
scope và không được dùng làm điều kiện để author hay kích hoạt M06–M11.

Bỏ điều kiện nhóm không có nghĩa fixture/replay, `BLOCKED_EXTERNAL` hay test
xanh được coi là real evidence. Personal progression vẫn phải phân biệt rõ code
có thể được viết với capability có thể được kích hoạt trên account/source thật.

## Decision

Chỉ giữ hai gate vận hành:

```text
AUTHORING_OPEN
= code / contract / fixture / replay / dry-run only

LIVE_ACTIVATION
= real evidence level + permission + safety controls của Mission
```

Quy tắc:

1. Repository không tuyển participant, không thu consent cho nghiên cứu learner,
   không duy trì aggregate group report và không có public-validation gate.
2. `BLOCKED_EXTERNAL` là truthful blocker, không phải E1–E6 và chỉ có thể mở
   authoring/replay phù hợp.
3. Live M06 cần E3 thật; live M10 canary cần E4 thật và chỉ tạo E5 sau operated
   bounded canary; live M11 cần E5 thật và chỉ tạo E6 sau production/recovery
   window.
4. RISK0/RISK1 chỉ auto-execute sau deterministic policy trong exact allowlist
   và declared caps. RISK2 luôn cần durable human approval + revalidation.
5. Personal actuals chỉ chứng minh Bot hoạt động trong bối cảnh của owner. Repo
   không suy rộng chúng thành timeline, độ dễ hay hiệu quả cho người khác.
6. Delivery metadata chỉ phản ánh artifact có thể kiểm bằng repository như
   starter, eval, verification và learner path. Personal execution/evidence nằm
   trong workspace ignored, không được giả lập trong tracked metadata.

## Migration boundary

Framework group-validation cũ được gỡ theo H1.3 trong
[Reality-First implementation plan](REALITY-FIRST-IMPLEMENTATION-PLAN.md), gồm
dedicated assets, Mission metadata, validator/report/test/CI và active prose.

Các trường hợp sau không thuộc migration này:

- “compliant micro-experiment” trong market loop là thử nghiệm affiliate nhỏ của
  chính owner;
- “5–10 eval cases” là số lượng test case, không phải số người;
- cohort trong attribution/analytics là khái niệm phân tích dữ liệu;
- `sources/` là historical input, không phải active curriculum authority.

## Consequences

- Owner có thể author M06–M11 sau trust repair mà không có external learner
  dependency.
- Live authority vẫn chỉ tăng theo E1–E6, permission và safety control thật.
- Readiness tooling phải bỏ mọi field hoặc claim dành cho participant/group.
- Ước lượng thời gian được hiệu chỉnh bằng actuals cá nhân và phải ghi rõ
  `n=1`; repository không đưa ra beginner-wide claim.

## Operational authority

Checklist và thứ tự thực thi nằm trong
[Reality-First implementation plan](REALITY-FIRST-IMPLEMENTATION-PLAN.md).
`CURRICULUM.md` tiếp tục là authority cho outcome, evidence và PASS; ADR này
chỉ xác định repository là personal-only và phân tách authoring với live
activation.
