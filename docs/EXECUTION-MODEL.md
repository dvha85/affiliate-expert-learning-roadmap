# Execution model v2

This is a v2 companion to [CURRICULUM.md](../CURRICULUM.md) and ADR-005. It
preserves governed-action safety while moving real human action before Bot/AI.

## Execution lanes

```text
human market lane: observe → create/review → manual publish → measure
deterministic lane: validate → record → decide/abstain → audit
AI lane: grounded analysis/proposal only; never fact or permission
automation lane: read/watch/orchestrate only after policy contracts exist
```

M00 has no Bot/AI publish capability. M04 advice is no-tool/no-write. Later
runtime choice remains implementation-flexible under ADR-004.

## Governed Action / Approval

Consequential automation starts only after the later Mission contracts:

```text
DecisionPacket / ActionIntent
→ deterministic Policy + Risk
   ├── RISK 0 → explicitly allowlisted execution + audit
   ├── RISK 1 → bounded execution + mandatory audit
   └── RISK 2 → persist → human approval → revalidate → execute/reject
→ ExecutionRecord → outcome/evaluation
```

ActionIntent is not permission. Any unavailable/invalid policy, stale evidence,
unknown version or kill switch must fail closed. Workflow and agent runtime do
not own canonical truth, risk or authorization.
