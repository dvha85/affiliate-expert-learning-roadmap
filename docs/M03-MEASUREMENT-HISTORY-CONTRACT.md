# M03 Measurement History Contract

M03 biến M01 snapshot và M02 baseline context thành history có thể audit,
không phải database architecture exercise.

```text
append-only snapshot
+ observation/provenance/time
+ explicit missing semantics
→ query/reconcile/freshness decision
```

## Invariants

- `observation_id` định danh một snapshot; duplicate cùng canonical content là
  idempotent, cùng ID nhưng content khác là `CONFLICT`/human review;
- `subject_id` ổn định khác `observation_id` và khác arrival time;
- `observed_at` là world-time evidence, `ingested_at` là arrival time; evidence
  đến muộn vẫn được lưu, query sort theo `observed_at`;
- history append-only: correction tạo record mới, không silently overwrite;
- freshness cần `observed_at + as_of + explicit max_age/policy`; thiếu policy
  là `UNKNOWN`, không áp TTL toàn cục.

Raw export/history có personal/account data phải ở private local storage; commit
chỉ fixture synthetic hoặc redacted summary/reference.
