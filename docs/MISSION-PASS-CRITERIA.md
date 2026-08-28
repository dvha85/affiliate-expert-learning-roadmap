# Mission PASS Criteria

Mission PASS is product/evidence progress, separate from canonical lesson PASS.

## Base criteria

A Mission is PASS only when all relevant base criteria are satisfied:

- [ ] **Feature works** — ship target behavior is demonstrable.
- [ ] **Bot runs** — documented run path works for the mission scope.
- [ ] **Tests pass** — required automated/manual checks pass.
- [ ] **Data flows** — sample/real data reaches the intended output.
- [ ] **Output is inspectable** — learner can show result, not merely claim completion.
- [ ] **Failure case tested** — at least one explicit failure/invalid-input scenario is exercised.
- [ ] **Required knowledge understood** — required mission knowledge is understood enough to justify the implementation/decision.
- [ ] **Explain-back passes** — learner can explain why the solution works and key trade-offs.
- [ ] **Evidence saved** — code/result/test evidence is linked or stored.

## Scope-dependent engineering criteria

Add when the mission actually introduces them:

- [ ] timeout/cancellation;
- [ ] retry/backoff;
- [ ] idempotency/deduplication;
- [ ] persistence/recovery;
- [ ] observability;
- [ ] least privilege/secrets handling;
- [ ] deterministic policy/risk;
- [ ] Human Approval;
- [ ] rollback/compensation/kill switch;
- [ ] cost/resource checks.

Do not force advanced controls onto M00 simply to satisfy a checklist. Criteria scale with actual side effects and failure modes.

## Knowledge PASS remains independent

Mission PASS never writes canonical lesson PASS automatically.

```text
Mission PASS
≠
Lesson PASS
```

A Mission may require enough knowledge to ship safely, while the learner may still need a deeper canonical lesson PASS cycle later. Conversely, lesson artifacts can be reused as mission evidence when they genuinely prove the same behavior.

## Review decision

Possible learner states:

- `✅ PASS` — all required criteria satisfied.
- `🟦 Awaiting Review` — implementation exists but evidence/explain-back still needs review.
- `⛔ Blocked` — external prerequisite or unresolved technical/business blocker.
- `🟨 In Progress` — active work remains.

Do not lower PASS quality merely to hit a planned date.