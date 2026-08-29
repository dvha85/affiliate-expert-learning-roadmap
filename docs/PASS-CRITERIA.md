# Tiêu chí áp dụng micro-lesson

Curriculum mới là **Mission-first**. Lesson là knowledge slice được kéo vào để giải quyết một gap vừa xuất hiện; đọc hết Lesson không phải mục tiêu tiến độ độc lập.

## Applied khác Read

Một micro-lesson chỉ được đánh dấu `applied` khi đủ năm điều kiện:

| # | Điều kiện | Evidence tối thiểu |
|---:|---|---|
| 1 | Try first | Có attempt/output trước phần giải thích |
| 2 | Observe | Ghi expected, observed và evidence kind |
| 3 | Apply | Concept được dùng ngay để sửa Bot/data/decision |
| 4 | Test | Có happy path và ít nhất một failure case |
| 5 | Explain-back | Giải thích được vì sao, giới hạn và bước đo tiếp theo |

```text
TRY → OBSERVE → PULL KNOWLEDGE → APPLY → TEST → EVIDENCE → EXPLAIN
```

Nếu thiếu một điều kiện, ghi `RETRY`. Không đánh dấu chỉ vì đã đọc, xem video hoặc trả lời câu hỏi nhớ thuật ngữ.

## Mission mới là progress gate

```text
Lesson applied
≠ Mission PASS
≠ Reality verified
≠ Bot operated
```

Mission có thể dùng nhiều knowledge slice. Mission chỉ PASS khi ship target, test, evidence và safety gate đều đạt theo [Mission PASS](MISSION-PASS-CRITERIA.md).

## Phân biệt bằng chứng

Mọi artifact dùng dữ liệu phải ghi một trong bốn loại:

- `real`: quan sát/hành động/outcome thật;
- `test`: dữ liệu dùng để kiểm plumbing hoặc failure;
- `synthetic`: dữ liệu dựng để học/test;
- `replay`: dữ liệu thật cũ được phát lại.

Sample/test/synthetic giúp PASS kỹ thuật nhưng không thay thế Reality gate của Mission.
