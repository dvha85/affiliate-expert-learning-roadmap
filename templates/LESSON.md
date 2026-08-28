---
lesson_id: "X.Y"
title: "Tên bài"
part: X
chapter: Y
effort: M # S | M | L
estimated_minutes: 60
status: planned # planned | draft | ready
prerequisites: []
source_refs:
  canonical:
    - "S:PX/CY/LX.Y"
  training: []
  research: []
  external: []
last_verified: null
---

# Bài X.Y — Tên bài

> **Phần X — TÊN PHẦN**  
> **Chương Y — Tên chương**  
> **Effort:** M · ~60 phút  
> **Authoring status:** `planned`

> `status` mô tả trạng thái biên soạn của lesson, **không phải trạng thái học tập của người học**. Một lesson `ready` vẫn chưa được coi là PASS cho tới khi người học đủ 5 tiêu chí PASS.

## 1. Mục tiêu bài học

Sau bài này, người học phải có khả năng:

1. ...
2. ...
3. ...

Mục tiêu phải dùng động từ quan sát/đánh giá được như: giải thích, phân biệt, tính, phân tích, thiết kế, kiểm chứng, triển khai, chẩn đoán, ra quyết định.

## 2. Prerequisites

- Kiến thức/bài bắt buộc trước: ...
- Execution loop đã nên mở: ...
- Nếu không có prerequisite: ghi `Không có`.

Không yêu cầu prerequisite chỉ vì lesson đứng trước trong file roadmap. Chỉ ghi dependency thực sự cần cho việc hiểu hoặc làm bài.

## 3. Source refs và phạm vi nguồn

### 3.1. Canonical

- `S:PX/CY/LX.Y`

### 3.2. Training supplement

- `T:...` hoặc `Không có counterpart trực tiếp`.

### 3.3. Research supplement

- `R:...` hoặc `Không có supplement trực tiếp`.

### 3.4. External verification

- Chỉ thêm khi lesson có claim hiện hành cần kiểm chứng.
- Với platform policy, legal, tax, privacy, pricing, attribution window, API/rule hiện hành: **bắt buộc kiểm chứng nguồn ngoài chính thức hoặc đáng tin cậy tại thời điểm authoring**.
- Ghi ngày kiểm chứng trong `last_verified`.

Tuân theo [`docs/SOURCE-MAPPING.md`](../docs/SOURCE-MAPPING.md). Không gắn `T`/`R` nếu nguồn không thật sự hỗ trợ nội dung.

## 4. Concept cốt lõi

Định nghĩa khái niệm bằng ngôn ngữ rõ, ngắn, đúng scope syllabus.

Nên trả lời:

- Nó là gì?
- Nó giải quyết câu hỏi nào?
- Nó nằm ở đâu trong affiliate system?
- Nó **không** phải là gì?

## 5. Giải thích sâu

Triển khai logic của concept.

Có thể dùng:

- mental model;
- flow;
- công thức;
- bảng so sánh;
- failure mode;
- trade-off;
- dữ liệu cần có;
- decision rule.

Không tăng độ dài chỉ để lesson “trông đầy đủ”. Nội dung phải phục vụ trực tiếp mục tiêu và PASS criteria.

## 6. Ví dụ minh họa

Tạo ít nhất một ví dụ đủ cụ thể để người học thấy concept vận hành.

Nếu có số liệu, công thức hoặc code:

- cho input;
- chỉ rõ cách suy luận;
- cho output;
- giải thích vì sao output hợp lý.

## 7. Case thực tế / tình huống quyết định

Đưa một case gần với affiliate thực tế.

Yêu cầu người học phải:

1. nhận diện vấn đề;
2. chọn dữ liệu/metric phù hợp;
3. phân tích;
4. đưa ra quyết định;
5. giải thích trade-off/risk.

Nếu lesson là policy/legal/current-platform, case phải dựa trên dữ kiện đã external-verify.

## 8. Misconceptions / failure modes

Liệt kê các cách hiểu sai phổ biến hoặc failure mode chính.

Ví dụ format:

- Sai: “...”
- Vì sao sai/chưa đủ: “...”
- Cách nghĩ đúng hơn: “...”

## 9. Exercise — artifact bắt buộc

Tạo artifact tại:

```text
artifacts/part-XX/<lesson-id>-<artifact-slug>.md
```

### Yêu cầu

- ...
- ...
- ...

### Definition of Done cho artifact

- [ ] Có output hữu hình, không chỉ ghi “đã hiểu”.
- [ ] Có reasoning/decision/evidence cần thiết.
- [ ] Có link ngược về lesson hoặc lesson note khi phù hợp.

Với lesson S, artifact có thể rất nhỏ. Với M/L, artifact phải phản ánh đúng effort thực tế.

## 10. Quiz

**PASS quiz: ≥ 80%.**

Tối thiểu:

- S: 3–5 câu
- M: 5–10 câu
- L: 8–15 câu hoặc assessment tương đương

Quiz phải kiểm tra hiểu biết/ứng dụng, không chỉ recall thuật ngữ.

### Câu 1

...

### Câu 2

...

### Câu 3

...

## 11. Answer key / scoring rubric

> **Bắt buộc.** Lesson không được chuyển sang `ready` nếu thiếu answer key hoặc scoring rubric.

<details>
<summary><strong>Mở đáp án/rubric sau khi đã làm xong</strong></summary>

### Answer key

1. ...
2. ...
3. ...

### Scoring

- Tổng điểm: ...
- PASS: ≥ 80%
- Với câu tự luận/case: ghi rõ tiêu chí chấm đạt/chưa đạt.

Nếu người học sai, yêu cầu ghi lại **vì sao sai** hoặc misconception tương ứng.

</details>

## 12. Explain-back

Không nhìn tài liệu, trả lời:

> “Tại sao ...?”

Câu trả lời đạt phải chạm được các ý:

- ...
- ...
- ...

Explain-back phải kiểm tra causal understanding, không chỉ định nghĩa.

## 13. Tiêu chí PASS bài X.Y

Chỉ tick lesson trong roadmap khi đủ **cả 5**:

- [ ] **Concept:** tự giải thích concept bằng ngôn ngữ của mình.
- [ ] **Example:** tự xử lý được example/case tương đương.
- [ ] **Quiz:** đạt ít nhất 80%.
- [ ] **Practice:** hoàn thành artifact bắt buộc.
- [ ] **Explain-back:** giải thích được “tại sao”, trade-off hoặc causal logic chính.

Nếu thiếu một mục:

```text
RETRY
```

Không tick `[x]` chỉ vì đã đọc xong.

## 14. Knowledge Base update

Sau khi PASS, lưu tối thiểu:

```text
Concept:
...

Decision rule / formula / mental model:
...

Biggest misconception fixed:
...

Evidence:
- artifact: ...
- quiz: ...
- explain-back: ...

Open question:
...
```

## 15. Tóm tắt một trang

Tóm tắt lesson bằng 5–10 bullet hoặc một mental model ngắn.

Mục tiêu: sau này có thể ôn lại trong 1–2 phút.

## 16. Tài liệu nguồn của bài

Liệt kê đúng các nguồn đã dùng:

1. Canonical syllabus: ...
2. Training supplement: ...
3. Research supplement: ...
4. External/current verification: ...
5. Repo standards: [`PASS-CRITERIA.md`](../docs/PASS-CRITERIA.md), [`SOURCE-MAPPING.md`](../docs/SOURCE-MAPPING.md), [`EFFORT-MODEL.md`](../docs/EFFORT-MODEL.md), [`EXECUTION-MODEL.md`](../docs/EXECUTION-MODEL.md)

Không liệt kê nguồn chỉ vì “có liên quan”; chỉ ghi nguồn thực sự được dùng.

## 17. Next action

Sau khi hoàn thành exercise + quiz + explain-back:

```text
PASS X.Y
hoặc
RETRY X.Y
```

Nếu PASS, chuyển sang lesson kế tiếp theo prerequisite của roadmap.