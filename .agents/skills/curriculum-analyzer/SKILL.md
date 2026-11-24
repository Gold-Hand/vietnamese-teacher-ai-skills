---
name: curriculum-analyzer
description: Phân tích chương trình GDPT, yêu cầu cần đạt, sách giáo khoa và tài liệu môn học; xác định trọng tâm, kiến thức tiên quyết, độ khó, hiểu lầm phổ biến và tiến trình dạy học. Dùng khi người dùng tải SGK/tài liệu hoặc yêu cầu phân tích bài, chủ đề, phân phối chương trình.
---

# Curriculum Analyzer

## Mục tiêu

Chuyển chương trình, SGK và tài liệu giáo viên cung cấp thành bản phân tích có thể dùng để lập kế hoạch dạy học.

## Quy trình

1. Xác định nguồn: chương trình, bộ SGK, sách giáo viên, tài liệu địa phương hay tài liệu tự biên soạn.
2. Đọc đúng phần liên quan; ưu tiên tài liệu người dùng tải lên. Nếu tài liệu dài, tìm mục lục/chủ đề rồi đọc phần cần thiết.
3. Trích xuất nguyên văn yêu cầu cần đạt khi cần; phân biệt trích dẫn và diễn giải.
4. Lập bản đồ: kiến thức nền → kiến thức mới → kỹ năng → sản phẩm/minh chứng.
5. Xác định trọng tâm, nội dung khó, khái niệm dễ nhầm, lỗi học sinh có thể mắc.
6. Đề xuất hoạt động, ví dụ gần gũi và phương án kiểm tra hiểu biết.
7. Nêu rõ nội dung chưa có trong tài liệu hoặc cần giáo viên xác nhận.

## Đầu ra

- Tóm tắt bài/chủ đề.
- Yêu cầu cần đạt và nguồn trang/mục nếu xác định được.
- Kiến thức tiên quyết.
- Trọng tâm và nội dung khó.
- Các hiểu lầm/lỗi sai dự kiến.
- Gợi ý dạy học và đánh giá.
- Liên hệ thực tiễn phù hợp lứa tuổi.
- Câu hỏi ôn tập/đánh giá nhanh.

## Kiểm soát chất lượng

Không tự nhận diện bộ SGK từ nội dung mơ hồ. Không trộn nội dung giữa các bộ sách. Không bịa số trang. Nếu chỉ có ảnh mờ hoặc trích đoạn thiếu, thông báo giới hạn và yêu cầu trang rõ hơn.

## Phân biệt chương trình Tin học và chương trình Trí tuệ nhân tạo (AI – V2.0)

- **Phân biệt hai hệ chương trình:** Tách bạch rõ **Chương trình GDPT 2018 môn Tin học** (có SGK/SGV và YCCĐ chính thức theo khối 10, 11, 12) với **chương trình / chuyên đề giáo dục Trí tuệ nhân tạo (AI)** (chuyên đề lựa chọn, khung năng lực AI, kế hoạch giáo dục nhà trường, STEM hoặc câu lạc bộ).
- **Kiểm tra căn cứ trước khi xác định YCCĐ:** Đối chiếu `../../../KNOWLEDGE_INDEX.md`, `../../../KHBD_INDEX.md`, `../../../knowledge-base/02_curriculum/` và `../../../knowledge-base/01_legal/` (kết hợp tài liệu người dùng cung cấp) trước khi kết luận yêu cầu cần đạt và phân bổ thời lượng.
- **Không tự mặc định nội dung AI thuộc chương trình Tin học chính thức:** Chỉ ghi nhận một nội dung AI thuộc chương trình Tin học chính thức khi văn bản chương trình/SGK nguồn chứng minh rõ (ví dụ đúng mạch kiến thức/chuyên đề Tin học theo quy định); nếu không có căn cứ đó, phải ghi rõ thuộc chương trình/chuyên đề AI độc lập hoặc đề nghị giáo viên xác nhận căn cứ áp dụng.

## Xuất tài liệu Office (Dùng chung Office Generator)

- Khi người dùng yêu cầu xuất báo cáo phân tích chương trình/SGK ra tệp Word (`.docx`) và đã có bản phân tích Markdown nguồn hợp lệ (không tự ý tạo khi người dùng chỉ cần Markdown), gọi:
  ```bash
  python scripts/office_generator/cli.py docx --input <phan_tich.md> --output <phan_tich.docx> --template teacher_guide
  ```
- Kiểm định đầu ra bằng `python scripts/office_generator/cli.py validate --input <phan_tich.docx> --source <phan_tich.md>`.
