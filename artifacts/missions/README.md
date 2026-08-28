# Bằng chứng Mission

Mission evidence (bằng chứng Mission) phải chứng minh người học đã **build, run, observe, test và learn (xây, chạy, quan sát, kiểm thử và học)** những gì, nhưng không copy lại toàn bộ codebase.

Cấu trúc khuyến nghị:

```text
artifacts/missions/MXX/
├── README.md
├── test-output.md
├── result-before.md
├── result-after.md
└── decision-notes.md
```

Source code thật vẫn nằm trong learner bot workspace. Artifact nên reference (tham chiếu) code path và commit SHA khi hữu ích.

Với bootstrap M00–M03, learner workspace mặc định là:

```text
lab/learner/affiliate-bot/
```

`lab/affiliate-bot/` là reference implementation (bản triển khai tham chiếu), không phải evidence rằng learner đã tự build capability.

## Evidence nên trả lời được

- Bạn đã build gì?
- Bạn đã chạy command nào?
- Output trước/sau khác nhau thế nào?
- Failure case nào đã được thử?
- Test nào bảo vệ behavior?
- Knowledge slice nào làm thay đổi implementation/quyết định?
- Commit nào đại diện cho learner work?

## An toàn dữ liệu

Không commit:

- secret, API key, token, password;
- credential;
- raw production data không cần thiết;
- dữ liệu cá nhân/sensitive data;
- nội dung không có quyền phân phối.

Mission evidence có thể được reuse (tái sử dụng) cho canonical Lesson/Project khi nó thực sự chứng minh cùng requirement. Reuse không tự động đánh dấu Mission, Lesson hay Project PASS.