# Affiliate Bot — deterministic learner runtime

> Workspace này thuộc **M01 — Smallest Deterministic Bot v0.1** trong curriculum mới. Nó không còn là M00 entrypoint.

M00 tạo real evidence + Human DecisionPacket trước. M01 dùng evidence/context đó để xây baseline deterministic có thể audit.

## Chạy baseline

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Fixture mặc định là synthetic/test và chỉ chứng minh behavior kỹ thuật.

## Contract M01

```text
known evidence fields
→ deterministic formula + stable tie-break
→ RANK_SCENARIO | GET_MORE_DATA | HUMAN_REVIEW
→ reason + missing evidence
→ NO external action
```

### Invariant bắt buộc

```text
real evidence
!= RECOMMEND

RANK_SCENARIO
!= Approval
!= Execution permission
```

Baseline hiện dùng `price × commission_rate` để tạo một weak scenario có chủ đích. Nó chưa xét conversion potential, audience fit, refund/cancel risk và nhiều business factors khác.

## Evidence semantics

- synthetic fixture: E0 engineering evidence;
- public observation thật: hỗ trợ E1 market context;
- `null`/missing không được đổi thành observed `0`;
- mixed real/synthetic hoặc identity/currency conflict phải `HUMAN_REVIEW`;
- missing/invalid evidence phải `GET_MORE_DATA`.

## Tại sao không có `RECOMMEND`?

M01 chỉ chứng minh deterministic ranking/abstention behavior. Một source là real không có nghĩa weak formula đã đủ business evidence để đưa recommendation.

Recommendation semantics, grounded AI và execution authority được mở ở các Mission sau với gate riêng.

## Bản đồ file

```text
cmd/bot/main.go
cmd/bot/main_test.go
internal/decision/
internal/observation/
data/
```

Không cần refactor sang database, Agent, n8n hay tool-calling trong M01.

## Reference implementation

`lab/affiliate-bot/` vẫn là reference workspace cũ trong thời gian cleanup. Learner runtime này là nơi contract M01 được kiểm trực tiếp; repo hardening sau sẽ giảm duplication giữa hai workspace.
