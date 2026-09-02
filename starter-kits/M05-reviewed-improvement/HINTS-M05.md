# M05 hint ladder

1. Freeze one variable and a stop rule before outcome. If there are two changes,
   split the experiment rather than comparing ambiguous results.
2. Link IDs in order: Decision → ActionRecord → Outcome → Evaluation.
3. Mark insufficient traffic `INCONCLUSIVE`; write its limitation and next read.
4. Generate a ChangeProposal, then ask a human to release/reject with a rollback
   target. Never let the proposal edit production directly.
