# Artifact & Evidence conventions

`artifacts/` lưu bằng chứng learner tạo trong Mission. Artifact phải inspect/reproduce được; “đã đọc/đã hiểu” không phải evidence.

## Cấu trúc

~~~text
artifacts/missions/M00/
artifacts/missions/M01/
...
artifacts/milestones/G1/
artifacts/experiments/
artifacts/knowledge/
~~~

Một artifact có thể chứng minh đồng thời micro-lesson, Mission và Milestone khi đúng requirement; link/reuse, không copy để tăng số lượng.

## Evidence kind bắt buộc

- `real`: observation/action/outcome thật;
- `test`: kiểm plumbing/failure;
- `synthetic`: dữ liệu dựng;
- `replay`: dữ liệu thật cũ phát lại.

Mọi business record phải có source, observed_at, access method và kind. Synthetic/test/replay không được trình bày như market validation.

## Evidence chain

Tùy Mission, lưu dần:

~~~text
Observation
→ HumanPrediction
→ BotDecision
→ Action hoặc ActionIntent
→ Outcome
→ Evaluation
→ ChangeProposal
→ BotVersion
~~~

Record chưa có phải là missing/pending/not-in-scope; không dựng record giả để “đủ chain”.

## Ba trạng thái

- Capability PASS;
- Reality verified;
- Operated.

Artifact tồn tại không tự tạo bất kỳ trạng thái nào. Review phải trỏ evidence, ghi blocking issue và PASS/RETRY/BLOCKED.

## Zero, missing và outcome

- zero chỉ dùng khi source thật báo 0;
- missing là chưa có/không đọc được;
- pending là observation window chưa kết thúc;
- inconclusive là đã đo nhưng evidence chưa phân biệt được giả thuyết.

Order/revenue là maturity milestone, không phải điều kiện may rủi để learner PASS.

## Dữ liệu nhạy cảm

Không commit secret, token, credential, API key, raw personal/sensitive export. Dùng redacted sample hoặc secure external storage và chỉ lưu reference/checksum khi cần.
