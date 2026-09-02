# M02 starter — deterministic baseline

`baseline.py` deliberately uses only the Python standard library and receives
data as an explicit JSON file. It does not fetch, call AI, use tools, publish
or write history. It returns a scenario or `GET_MORE_DATA` with `action: null`.

```bash
python starter-kits/M02-deterministic-baseline/run_baseline.py \
  evals/M02-deterministic-baseline/rankable-observations.json
```

The provided inputs are synthetic evaluator fixtures (E0). Replace only with
permitted, redacted evidence references and preserve `real`/`synthetic` truth.
