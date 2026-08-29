# Tiêu chí Mission PASS

Mission là progress gate của curriculum. Mỗi Mission mở rộng cùng một evidence chain:

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

Không phải Mission nào cũng có đủ mọi record ngay từ đầu; field chưa xuất hiện phải được ghi rõ là chưa nằm trong scope, không được giả lập rồi gọi là reality.

## Ba chiều trạng thái

- **Capability PASS:** Bot/learner làm được behavior kỹ thuật.
- **Reality verified:** có đúng evidence level mà Mission yêu cầu.
- **Operated:** capability đã chạy đủ cycle/window để quan sát failure/outcome.

Mission chỉ được đánh dấu DONE khi ba chiều bắt buộc của Mission đều đạt. Fixture có thể giúp Capability PASS nhưng không thay Reality verified.

## Tiêu chí chung

- [ ] learner đã TRY trước khi kéo knowledge;
- [ ] Bot có behavior/output quan sát được;
- [ ] learner tự thay đổi phần có ý nghĩa;
- [ ] human prediction/judgment được ghi trước Bot output khi Mission có decision;
- [ ] happy path và failure case đạt;
- [ ] evidence kind được ghi đúng: real, test, synthetic hoặc replay;
- [ ] trước/sau hoặc baseline comparison được lưu;
- [ ] safety gate tương ứng đạt;
- [ ] uncertainty, limitation và bước đo tiếp theo được giải thích;
- [ ] không trình bày test/synthetic/replay như reality;
- [ ] Bot version và evidence record có thể truy lại.

## Reality gate

- M00–M02 yêu cầu public evidence E1; sample chỉ là fallback cho Capability.
- M03 yêu cầu public artifact do learner tự review/thực hiện, không yêu cầu bot publish.
- M04 yêu cầu analytics/export thật; observed zero hợp lệ, missing phải giữ là missing.
- M05 yêu cầu một real improvement cycle; negative/inconclusive vẫn PASS nếu measurement trung thực.
- M06–M11 tăng dần từ automatic read-only tới governed action và production loop.

Order, valid order và paid commission là maturity milestone, không phải PASS gate.

## Safety gate

Mỗi Mission phải khai báo S0–S6:

- S0 evidence/data;
- S1 AI advisory;
- S2 manual publish;
- S3 automatic collection;
- S4 read-only tool agent;
- S5 shadow/durable approval;
- S6 limited governed automation.

Prohibited actions như fake clicks/orders, spam, policy bypass, credential sharing và unbounded spend không thể được human approval để hợp thức hóa.

## Review record

Review phải lưu:

- reviewer hoặc self-review stage;
- timestamp;
- Capability/Reality/Operated result;
- evidence links;
- blocking misconception hoặc safety failure;
- PASS/RETRY/BLOCKED;
- next action.

CI xanh không tự tạo Mission PASS.
