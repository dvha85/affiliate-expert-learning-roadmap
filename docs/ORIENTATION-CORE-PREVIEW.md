# Orientation Core vs Preview — Bài 0.1 và 0.2

> Tài liệu này là **reading contract** cho hai lesson orientation đã author đầy đủ. Nó không xóa, thay thế hoặc làm giảm PASS criteria của lesson 0.1/0.2.

## Vì sao cần reading contract?

Bài 0.1 và 0.2 cố ý cho learner nhìn thấy toàn bộ hệ thống từ đầu. Depth đó hữu ích để định hướng, nhưng người mới **không cần mastery mọi thuật ngữ production ngay trong lần đọc đầu**.

Quy tắc:

```text
CORE NOW
= phải hiểu đủ để làm Mission hiện tại và explain-back

PREVIEW / MASTER LATER
= phải nhận diện được ý nghĩa và biết nó sẽ quay lại ở đâu;
  chưa cần implementation-level mastery trong orientation
```

Không dùng nhãn `Preview` để bỏ qua quiz, practice artifact hoặc evidence mà lesson PASS contract yêu cầu. Nhãn này chỉ điều chỉnh **độ sâu kỳ vọng ở lần học orientation đầu tiên**.

---

## Bài 0.1 — Affiliate Expert là gì?

### CORE NOW — cần hiểu ngay

Learner phải giải thích được bằng lời của mình:

1. Affiliate Expert không chỉ là người lấy link và đăng content.
2. Affiliate là một business system:

```text
Content → Audience → Click → Platform → Order → Validation → Commission → Payment
```

3. Funnel phải được nhìn bằng dữ liệu, không bằng cảm giác.
4. Hai nguyên tắc:

```text
DATA > OPINION
EXPECTED VALUE > COMMISSION RATE
```

5. Commission Rate cao không tự động đồng nghĩa opportunity tốt.
6. Cần hiểu/manual-observe workflow trước khi automate.
7. `Decision ≠ Execution` — recommendation tốt chưa phải permission để hành động.
8. Affiliate Expert cần phối hợp Business + Marketing + Data + Engineering + AI + Experimentation, nhưng chưa cần mastery toàn bộ stack trong bài mở đầu.

### PREVIEW — nhận diện bây giờ, mastery sau

Các concept sau cần **biết chúng tồn tại và vì sao quan trọng**, nhưng implementation-level mastery sẽ đến ở Parts/Missions sau:

- attribution/reconciliation sâu;
- statistical sample size và experiment design;
- production data quality architecture;
- Action Intent / approval workflow chi tiết;
- governance implementation;
- advanced recommendation/decision system;
- production automation boundaries.

Khi gặp phần sâu trong lesson 0.1, learner nên tự hỏi:

> “Tôi cần hiểu concept này để giải thích Affiliate system hôm nay, hay cần mastery implementation của nó ngay?”

Nếu câu trả lời là implementation mastery, đánh dấu note và quay lại ở canonical Part tương ứng.

---

## Bài 0.2 — Affiliate Bot Engineer là gì?

### CORE NOW — cần hiểu ngay

Learner phải giải thích được:

1. Affiliate Bot Engineer xây **system**, không chỉ viết một script chạy được một lần.
2. Progression:

```text
Manual workflow
→ Deterministic automation
→ Reliable Bot
→ AI-assisted Bot
→ Tool-Using Agent
→ Governed Autonomous System
```

3. Deterministic logic đi trước LLM autonomy.
4. Vì sao Go là primary implementation language của curriculum mà không cần tuyên bố “Go luôn nhanh hơn C#”.
5. `Decision ≠ Execution`.
6. RISK 0 / RISK 1 / RISK 2 và vai trò Human Approval.
7. Boundary tối thiểu:

```text
Data → Decision → Policy → Approval → Action → Audit
```

8. `MODEL OUTPUT = UNTRUSTED INPUT`.

### PREVIEW — nhận diện bây giờ, mastery sau

Trong orientation, learner chỉ cần biết **vai trò** của các concept sau; chưa cần tự triển khai production-grade:

- Tool Contract / MCP;
- durable workflow/execution;
- retry/backoff/idempotency/compensation ở quy mô production;
- OpenTelemetry/trace/production observability;
- least privilege cho tool agents;
- prompt injection defense architecture;
- kill switch implementation;
- provider routing/evaluation;
- multi-agent coordination.

Các nội dung này vẫn ở lesson để learner có system map, nhưng mastery được kéo đúng lúc qua Build-First Missions và canonical Parts.

---

## Cách học hai bài orientation

### Pass 1 — Map

Đọc để hiểu system map. Không dừng quá lâu ở thuật ngữ Preview.

### Pass 2 — Core explain-back

Không nhìn tài liệu, tự giải thích CORE NOW bằng lời của mình.

### Pass 3 — Practice / Quiz / Evidence

Làm đầy đủ artifact và quiz theo lesson PASS contract.

### Pass 4 — Preview bookmark

Ghi 3–5 concept Preview mà bạn muốn quay lại khi Mission thực sự cần.

## Anti-pattern

```text
SAI:
“Tôi chưa hiểu MCP/Temporal/OpenTelemetry sâu nên chưa được phép bắt đầu M00.”

ĐÚNG:
“Tôi hiểu chúng là production capabilities sẽ học đúng lúc;
M00 hiện chỉ cần mental model và capability slice được Mission yêu cầu.”
```

Orientation phải tạo **direction**, không tạo prerequisite giả.