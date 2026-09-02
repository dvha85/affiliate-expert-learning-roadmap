# M03 hint ladder

1. Save one Observation, then deliberately try to overwrite it: what audit
   question becomes impossible?
2. Append ActionRecord, MeasurementContext and Outcome with linked IDs. Query
   after restart; preserve arrival time separately from observed time.
3. Trigger duplicate/conflict/out-of-order fixtures. A correction must append a
   new record, never mutate the old JSONL line.
4. Pass explicit `as_of` and max age to freshness; missing policy is `UNKNOWN`.
