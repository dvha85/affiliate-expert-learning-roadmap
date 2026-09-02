# M04 Grounded Advisory Contract

M04 introduces A1 advisory **after** M03 trustworthy history. Provider/model
output is untrusted input; a replay fixture proves the gate, not a live model.

```text
evidence set + deterministic baseline
→ candidate advisory
→ ref exists + field/value support check
→ grounded advisory OR rejected/unavailable/skipped fallback
→ baseline preserved; no action
```

## Required boundaries

- every factual claim has an evidence ref and exact support for field/value;
- unsupported claim, malformed schema, unavailable provider or injection-like
  text yields `rejected`/`unavailable` and deterministic fallback;
- hypotheses remain hypotheses, not observed facts/scoring inputs;
- no tool, write, publish, execution, credential or external side effect;
- input/evidence/prompt/provider/model version and fallback reason are logged as
  redacted references, never raw secret/private payloads.

`grounded` does not mean correct business outcome; it means the claim is tied
to supplied evidence under this limited contract.
