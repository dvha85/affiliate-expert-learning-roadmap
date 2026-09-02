# M02 hint ladder

1. **Input first:** run `valid.json`, then `missing.json`; compare state and
   `missing_evidence` before editing a rule.
2. **One failure:** make an assertion for duplicate, mixed currency or tie;
   predict `HUMAN_REVIEW`/stable order before seeing the output.
3. **Rule card:** use `../M02-operator-profile/OPERATOR-RULES.md` and explain
   why price × commission is only a weak scenario.
4. **Go oracle:** after Operator output is frozen, run the Go profile and the
   parity validator. Do not use either output as market truth or authority.
