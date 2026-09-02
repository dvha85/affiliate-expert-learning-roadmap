# M03 checkpoints

- **Attempt:** overwrite t1 with t2 and record the lost evidence before reading
  the history contract.
- **Failure:** run duplicate/identity/out-of-order fixtures and predict whether
  the state is idempotent, conflict or append.
- **Improve:** append the four linked record types, restart/query and record a
  correction/reconciliation as a new immutable record.
