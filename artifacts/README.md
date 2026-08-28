# Artifact & Evidence Conventions

`artifacts/` lưu evidence hữu hình do người học tạo ra trong lesson, lab, project hoặc review.

## 1. Nguyên tắc

Artifact phải inspect được. Các trạng thái như “đã đọc”, “đã hiểu”, “đã xem video” không phải artifact.

Một artifact tốt trả lời được ít nhất một câu hỏi:

- Người học đã áp dụng concept như thế nào?
- Quyết định nào đã được đưa ra và dựa trên evidence nào?
- Code/schema/dashboard/analysis nào đã được tạo?
- Kết quả có thể review/reproduce ở đâu?

## 2. Naming

Lesson artifact:

```text
artifacts/part-XX/X.Y-<artifact-slug>.<ext>
```

Ví dụ:

```text
artifacts/part-00/0.1-affiliate-expert-self-assessment.md
artifacts/part-08/27.4-opportunity-score-analysis.md
```

Project artifact nên nằm trong:

```text
artifacts/projects/project-XX-<slug>/
```

Lab/Pass Gate:

```text
artifacts/labs/<lab-slug>/
artifacts/pass-gates/<gate-slug>/
```

Experiment/revenue/knowledge records có thể nằm trong:

```text
artifacts/experiments/
artifacts/revenue/
artifacts/knowledge/
```

## 3. Linking

- Lesson phải link tới artifact bắt buộc.
- Lesson note phải link tới artifact đã hoàn thành.
- Project README phải link tới deliverables/evidence.
- Retrospective phải link tới project/lab/experiment được review.
- Không copy cùng một artifact sang nhiều nơi nếu có thể link/reuse.

## 4. Evidence status

Artifact tồn tại **không tự động nghĩa là PASS**. PASS lesson vẫn cần đủ 5 tiêu chí:

```text
Concept + Example + Quiz >=80% + Practice + Explain-back
```

Project/Lab/Pass Gate chỉ hoàn thành khi đạt acceptance criteria riêng.

## 5. Anti-double-counting

Nếu một lesson artifact được dùng lại trong project:

- lesson tính effort để tạo artifact ban đầu;
- project chỉ tính integration, validation, hardening, demo, retrospective tăng thêm.

Không nhân đôi workload chỉ vì cùng artifact xuất hiện ở nhiều milestone.

## 6. Sensitive data

Không commit secret, token, credential, API key, personal data không cần thiết hoặc raw production data nhạy cảm. Dùng sample/anonymized data hoặc external secure storage và chỉ lưu reference khi phù hợp.
