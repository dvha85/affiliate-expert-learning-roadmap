# M04 starter — grounded advisory replay gate

`grounding_gate.py` accepts explicit evidence plus an untrusted replay
candidate. It validates only factual field/value claims, preserves the baseline
and always returns `action: null`. It has no provider, network, tool or write
capability.

```bash
python scripts/validate_m04_grounded_advisory_pack.py
```

The eval pack is replay/synthetic; it is not live AI or learner E3 evidence.
