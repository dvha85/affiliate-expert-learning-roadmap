# M05 Reviewed Improvement Contract

M05 turns an outcome into a **proposal**, never an automatic change:

```text
Decision → ActionRecord → Outcome → Evaluation
→ ChangeProposal(PENDING_REVIEW)
→ human release | reject | rollback
```

## Freeze before outcome

An Experiment declares exactly one main variable, hypothesis, primary metric,
MeasurementContext, window and stop rule before outcome is observed. Low traffic
defaults to `INCONCLUSIVE`; no conclusion is better than invented lift.

## Cost and authority

Record content-production time, model/tool cost (or not-applicable) and net
value limitation. Offline champion–challenger/replay can inform a proposal but
does not release it. `ChangeProposal.production_mutation` is always false until
a human makes an auditable release/reject decision with a rollback plan.
