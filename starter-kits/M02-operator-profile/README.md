# M02 Operator / no-code profile

This profile is a manual spreadsheet/table workflow, not a paid SaaS or API.
Use the rule card in `OPERATOR-RULES.md` against the shared JSON fixtures or a
local redacted evidence export. The small Python helper exists only to compare
the worksheet result with the Go golden oracle in CI; it makes no network, AI,
tool, write or external call.

```bash
python starter-kits/M02-operator-profile/run_operator.py evals/cases/m02/valid.json
```
