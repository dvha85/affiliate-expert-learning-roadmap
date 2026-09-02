# M03 starter — trustworthy history

`history.py` is a small JSONL profile: it validates snapshots, appends rather
than overwrites, identifies duplicate/conflict and queries by `observed_at`.
It has no network, AI, tool or external action capability.

The evaluator uses synthetic records only:

```bash
python scripts/validate_m03_history_pack.py
```

Use private local storage for any real analytics/account history.
