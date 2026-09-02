## Curriculum change checklist

- [ ] Tôi đã nêu rõ authority docs bị thay đổi và nếu cần đã thêm/cập nhật ADR.
- [ ] Mission metadata có `curriculum_version`, `release_kind` và `delivery` hợp lệ.
- [ ] Tôi phân biệt `authoring status` với starter/eval/pilot readiness; không gọi Mission là delivered khi delivery bundle chưa đủ.
- [ ] Tôi đã kiểm tra authority ceiling, external side effects, human approval và evidence level.
- [ ] Tôi đã ghi mapping/migration khi đổi Mission, lesson ID hoặc đường dẫn cũ.
- [ ] Tôi đã cập nhật docs/roadmap/status projection liên quan.
- [ ] Tôi đã chạy các validator và test phù hợp, gồm `python scripts/validate_readiness.py`.
