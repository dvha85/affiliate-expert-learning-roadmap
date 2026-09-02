# M01 hint ladder

1. Declare ActionRecord, MeasurementContext and window before checking data.
2. Query the actual permitted analytics/export source once; write its limitation.
3. If the source says zero, use `zero + observed`; if not yet visible, use
   `pending/not_yet_observable`, never zero.
4. Schedule `next_read_at` instead of inventing attribution or outcome.
