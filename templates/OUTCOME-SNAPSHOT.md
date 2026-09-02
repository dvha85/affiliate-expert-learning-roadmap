# Outcome Snapshot — copy to local/private first

- outcome_id:
- origin: real
- action_record_id:
- measurement_context_id:
- measurement_source/reference:
- observed_at:
- outcome_status: zero | pending | partial | final | inconclusive
- observed_value: 0 | not_yet_observable | <redacted aggregate>
- value_state: observed | missing | unknown | not_yet_observable
- attribution limitation:
- next_read_at:

`observed_value: 0` requires `outcome_status: zero` and `value_state: observed`.
`pending`, missing and `not_yet_observable` must never be converted to zero.
