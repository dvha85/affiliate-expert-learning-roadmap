# Optional public pilot kit — do not fabricate results

PR9 hiện là personal validation theo
[`ADR-006`](../docs/ADR-006-PERSONAL-VALIDATION-AND-PUBLIC-PILOT.md). Kit này
được giữ cho public curriculum validation nếu owner sau này recruit 5–10
consenting beginners. Nó không chặn personal authoring/live gates và personal
evidence không được ghi thành participant/cohort evidence.

There is no hidden telemetry: use the redacted session and aggregate templates,
keep identifying/raw material in ignored `pilot/raw/`, and commit an aggregate
only after review.

Track focused time separately from waiting time. `not_started` is the only
truthful status until real sessions exist.
