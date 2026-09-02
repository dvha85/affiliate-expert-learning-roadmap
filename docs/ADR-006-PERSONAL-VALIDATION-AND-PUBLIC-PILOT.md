# ADR-006 — Personal Validation và Public Pilot là hai gate khác nhau

**Status:** Accepted — 2026-09-02
**Decision owner:** repository owner
**Amends:** ADR-002 authoring-wave pilot requirement cho personal development;
không thay evidence ladder, Mission PASS hoặc authority ceiling của ADR-004/
ADR-005.

## Context

Repository hiện được một owner dùng để vừa học vừa xây Affiliate Intelligence
Bot. Yêu cầu cohort 5–10 absolute beginners trước khi author M06–M11 tạo một
external dependency không cần thiết cho personal development. Tuy nhiên bỏ
cohort gate mà không thay bằng boundary rõ có thể khiến synthetic/replay hoặc
`BLOCKED_EXTERNAL` bị dùng để mở live automation.

## Decision

Tách ba gate độc lập:

```text
AUTHORING_OPEN
= code / contract / fixture / replay / dry-run only

LIVE_ACTIVATION
= real evidence level + permission + safety controls của Mission

PUBLIC_VALIDATION
= independent beginner pilot + aggregate/redacted evidence
```

Quy tắc:

1. Personal authoring không cần cohort pilot nếu workflow inactive, không chứa
   credential và không tạo external side effect.
2. `BLOCKED_EXTERNAL` là truthful blocker, không phải E1–E6 và chỉ có thể mở
   authoring/replay phù hợp.
3. Live M06 cần E3 thật; live M10 canary cần E4 thật và chỉ tạo E5 sau operated
   bounded canary; live M11 cần E5 thật và chỉ tạo E6 sau production/recovery
   window.
4. RISK0/RISK1 chỉ auto-execute sau deterministic policy trong exact allowlist
   và declared caps. RISK2 luôn cần durable human approval + revalidation.
5. Personal evidence không đổi `pilot_status: validated`, không chứng minh
   beginner readiness và không dùng để công bố cohort timeline.
6. Nếu repository sau này phục vụ learner khác, public promotion vẫn tuân
   independent pilot requirements trong migration/authoring standards.

## Consequences

- Owner có thể tiếp tục author M06–M11 mà không fake cohort.
- Authoring progress và operational authority được báo riêng.
- Fixture/replay vẫn hữu ích cho Capability nhưng không mở live runtime.
- Tài liệu quản lý phải nêu rõ gate nào đang đạt; từ `open` không được dùng nếu
  không nói rõ `AUTHORING_OPEN` hay `LIVE_ACTIVATION`.

## Operational authority

Checklist và thứ tự thực thi nằm trong
[Reality-First implementation plan](REALITY-FIRST-IMPLEMENTATION-PLAN.md).
`CURRICULUM.md` tiếp tục là authority cho outcome, evidence và PASS; ADR này
chỉ thay cách owner quyết định khi nào được author và khi nào được activate.
