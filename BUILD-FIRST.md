# Build-First, Reality-First v2

> Canonical sequence: [CURRICULUM.md](CURRICULUM.md). This execution model
> follows [ADR-005](docs/ADR-005-REALITY-FIRST-CURRICULUM.md), while retaining
> deterministic-core and governed-action boundaries from ADR-004.

## The learner loop

```text
DO A SMALL THING A REAL PERSON CAN VERIFY
→ observe the gap
→ pull the smallest knowledge slice
→ improve and test
→ save evidence
→ decide the next measurement
```

O00 is a safe synthetic walkthrough only. M00 is the first PASS candidate: a
human observes, makes/reviews a small affiliate artifact, adds disclosure and
tracking as applicable, and manually publishes. Bot/AI has no publish authority.
M01 gets an outcome snapshot and M02 supplies the smallest deterministic
baseline in parallel after M00. AI appears only at M04 as grounded, no-tool
advisory.

## Evidence taxonomy

- origin / eligibility: real | synthetic
- use context khi relevant: test | replay
- `evidence_kind: real | synthetic` khi contract M00 áp dụng
- Không ép `real | synthetic | test | replay` thành bốn giá trị loại trừ trên cùng một enum.

Synthetic data is useful for O00 and tests, but never proves market reality.
Missing, zero, pending and inconclusive must remain distinct.

## Authority progression

```text
M00 human_only manual publish
→ M01 manual/read-only outcome
→ M02–M03 A0 deterministic
→ M04–M05 A1 advisory/propose-only
→ M08 A2 read-only tools
→ M09–M11 governed action only through policy/risk/approval/audit
```

```text
DETERMINISTIC CORE FIRST
≠ CODE FIRST

NO-CODE WHEN IT IS AUDITABLE
AGENT-WRITTEN CODE WHEN CODE IS NECESSARY
```

Every Mission declares `delivery` separately from authoring status. A `ready`
file is not a beginner-ready delivery until starter/eval/verification/pilot
metadata supports the claim.
