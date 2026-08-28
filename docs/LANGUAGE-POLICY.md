# Quy chuẩn ngôn ngữ của repository

## 1. Ngôn ngữ chính thức

**Tiếng Việt là ngôn ngữ chính thức của repository.**

Tài liệu học, Mission, hướng dẫn vận hành, tiêu chí PASS, tài liệu kiến trúc và ghi chú tiến độ phải ưu tiên viết bằng tiếng Việt để người học có thể đọc liên tục mà không phải tự dịch toàn bộ nội dung.

## 2. Khi nào dùng tiếng Anh

Tiếng Anh được giữ nguyên khi cần độ chính xác kỹ thuật hoặc khả năng đối chiếu nguồn ngoài, ví dụ:

- tên công nghệ, sản phẩm, protocol (giao thức) và chuẩn;
- tên API, field, function, package, type, command, identifier và schema;
- thuật ngữ chuyên ngành phổ biến trong Affiliate, Data, Engineering và AI;
- tên riêng của tài liệu/chuẩn bên ngoài.

Ở lần xuất hiện quan trọng, ưu tiên dạng:

```text
English term (giải thích tiếng Việt)
```

Ví dụ:

```text
Expected Value (Giá trị kỳ vọng)
Repository (lớp trừu tượng truy cập dữ liệu)
Idempotency (tính lặp an toàn)
Human Approval (phê duyệt của con người)
```

Không cần dịch identifier trong code hoặc tên chuẩn đã được cộng đồng sử dụng ổn định.

## 3. Quy tắc cho file Markdown

Một file Markdown mới hoặc được sửa đáng kể phải:

1. dùng tiêu đề và phần giải thích chính bằng tiếng Việt;
2. không chuyển nguyên đoạn hướng dẫn sang tiếng Anh nếu không có lý do kỹ thuật;
3. giữ English term khi việc dịch làm mất nghĩa hoặc khó tra cứu;
4. bổ sung nghĩa tiếng Việt ở lần xuất hiện quan trọng;
5. có thể dùng code block tiếng Anh khi đó là output, command, schema hoặc identifier thực tế.

Các tên ổn định như `Build-First`, `Mission`, `Project`, `Bot Version`, `PASS`, `Go`, `PostgreSQL`, `MCP`, `LLM`, `OpenTelemetry` có thể giữ nguyên; phần giải thích xung quanh vẫn phải bằng tiếng Việt.

## 4. Không áp dụng máy móc

Quy chuẩn này không nhằm dịch toàn bộ thuật ngữ kỹ thuật sang tiếng Việt. Mục tiêu là:

```text
ĐỌC HIỂU BẰNG TIẾNG VIỆT
+
GIỮ ĐƯỢC TỪ KHÓA TIẾNG ANH ĐỂ LÀM VIỆC THỰC TẾ
```

Do đó không đổi tên code/API chỉ để đạt tỷ lệ tiếng Việt và không dịch sai tên chuẩn của công nghệ.

## 5. Kiểm tra khi review

Khi review PR tài liệu, kiểm tra:

- phần giải thích chính có bằng tiếng Việt không;
- English term quan trọng đã có nghĩa Việt khi cần chưa;
- code/schema/identifier có bị dịch sai không;
- có đoạn nào bị chuyển thành English-only mà người học không được giải thích không.

Quy chuẩn này áp dụng cho tài liệu learner-facing và maintainer-facing của curriculum kể từ Build-First hardening sau Issue #37.