# Operator rule card

1. Stop at `GET_MORE_DATA` when any required field is missing or invalid:
   subject/observation ID, source, observed_at, price, currency, commission.
2. Stop at `HUMAN_REVIEW` for duplicate observation ID, conflicting identity or
   a mixed-currency comparison.
3. Otherwise calculate `price × commission_rate`; sort descending score then
   ascending `subject_id` for ties.
4. Label result `RANK_SCENARIO`, not execution permission. It is a weak scenario
   and cannot claim audience fit, conversion, revenue or market outcome.

The rule card is usable in a paper sheet/local spreadsheet. Preserve source,
time and missing values; do not silently insert zero.
