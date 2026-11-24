---
name: slide-designer
description: Thiết kế kịch bản bài trình chiếu giáo dục, PowerPoint, Canva và NotebookLM; tổ chức mạch nội dung, phân bổ slide, đề xuất hình ảnh, sơ đồ, biểu đồ, câu hỏi tương tác và prompt tạo slide. Dùng khi người dùng yêu cầu làm slide, bài thuyết trình hoặc chuyển giáo án thành trình chiếu.
---

# Slide Designer

## Mục tiêu

Tạo trình chiếu phục vụ học tập, không biến slide thành bản chép nguyên văn giáo án.

## Quy trình

1. Xác định đối tượng, mục tiêu bài học, thời lượng, công cụ đích (PowerPoint / Canva / NotebookLM).
2. Phân tích nội dung nguồn; giữ chính xác thuật ngữ, số liệu và trình tự lập luận.
3. Lập storyline: mở vấn đề → khám phá/giải thích → minh họa → luyện tập → tổng kết.
4. Phân bổ số slide theo thời lượng và mật độ nội dung; không áp đặt số lượng cố định.
5. Với từng slide, tách bạch rõ: tiêu đề, mục tiêu, **nội dung hiển thị ngắn gọn trên slide**, hình ảnh/sơ đồ đề xuất và **ghi chú thuyết trình (Speaker Notes) / hoạt động tương tác** cho giáo viên.
6. Khi thiết kế slide câu hỏi trắc nghiệm/luyện tập, viết đầy đủ toàn bộ phương án A, B, C, D kèm đáp án và giải thích dành cho giáo viên.
7. Viết prompt thiết kế tổng thể và prompt/hướng dẫn riêng theo công cụ đích (PowerPoint, Canva hoặc NotebookLM).
8. Rà soát lỗi chính tả, khả năng đọc và **tính nhất quán giữa mục tiêu bài học ↔ nội dung các slide ↔ câu hỏi đánh giá**.

## Nguyên tắc thiết kế

- Một slide tập trung một thông điệp chính.
- **Phân biệt rõ nội dung hiển thị trên slide và lời thuyết trình:** Trên slide chỉ giữ từ khóa, câu ngắn, bảng gọn, sơ đồ trực quan (không viết đoạn văn dài); phần diễn giải chi tiết, câu hỏi gợi mở, dự kiến câu trả lời và cách điều phối lớp đặt ở **Ghi chú thuyết trình (Speaker Notes)** của từng slide.
- **Quy tắc câu hỏi trắc nghiệm trên slide:** Mọi câu hỏi trắc nghiệm bắt buộc trình bày **đầy đủ 4 phương án A, B, C, D** (không viết đề tóm tắt thiếu phương án), đồng thời cung cấp **đáp án đúng và giải thích ngắn gọn dành cho giáo viên** (đặt ở ghi chú thuyết trình hoặc phụ lục đáp án để không lộ sớm khi trình chiếu).
- **Kiểm tra tính nhất quán sư phạm:** Mỗi mục tiêu bài học nêu ở đầu bài phải có slide hình thành kiến thức/minh họa tương ứng và câu hỏi/bài tập kiểm tra tương ứng; tổng thời lượng các slide phải khớp thời lượng tiết học.
- Ưu tiên sơ đồ, ví dụ, ảnh có ý nghĩa thay vì trang trí.
- Chữ đủ lớn, tương phản tốt, không nhồi văn bản.
- Dùng cùng hệ màu, kiểu chữ và phong cách minh họa.
- Không tạo ảnh minh họa có chữ tiếng Việt dài nếu công cụ dễ sinh lỗi; đặt chữ trong phần tử văn bản của ứng dụng.
- Có ghi nguồn cho hình ảnh/số liệu khi cần.

## Hướng dẫn tạo slide theo công cụ (bao gồm NotebookLM)

- **PowerPoint / Canva:** Dựng bảng dữ liệu, sơ đồ khối và mũi tên liên kết bằng đối tượng gốc (Native Table, Shapes, Connectors); chỉ dùng AI tạo ảnh minh họa không chữ (`NO TEXT`) nếu cần trang trí; cài hiệu ứng `Appear/Fade` để ẩn đáp án trước khi học sinh trả lời.
- **NotebookLM (Slide Deck / Tài liệu nguồn tạo slide):**
  1. Chuẩn bị **tài liệu nguồn đầu vào (Source Document)** thật cô đọng, phân mục rõ theo đúng Storyline từng slide (Tiêu đề → Ý chính → Ví dụ/Dữ liệu mẫu → Câu hỏi kiểm tra) và giữ chuẩn thuật ngữ tiếng Việt GDPT 2018.
  2. Tải nguồn vào NotebookLM, chọn tạo **Slide Deck** (hoặc cấu trúc trình chiếu theo nguồn) kèm **Custom Prompt tiếng Việt** chỉ rõ: đối tượng học sinh, số lượng slide dự kiến, ngôn ngữ tiếng Việt chuẩn, giữ ngắn gọn mỗi slide 1 thông điệp, không tự bịa số liệu/ví dụ ngoài nguồn.
  3. Rà soát kỹ lỗi hiển thị dấu tiếng Việt, lỗi chữ trong hình/sơ đồ do AI sinh và đối chiếu lại thuật ngữ chuyên môn trước khi trình chiếu; giữ nguyên phần **Ghi chú thuyết trình & Đáp án GV** làm kịch bản giảng song song.

## Định dạng đầu ra

1. Thông tin tổng quan & Mục tiêu bài học *(đánh số M1, M2, M3... để đối chiếu nhất quán)*.
2. Mạch nội dung (Storyline) & Bảng đối chiếu nhất quán *(Mục tiêu ↔ Slide nội dung ↔ Câu hỏi đánh giá)*.
3. Bảng phân bổ slide gồm: `số slide | tiêu đề | mục tiêu | nội dung hiển thị | hình ảnh/sơ đồ đề xuất | ghi chú thuyết trình (Speaker Notes) & hoạt động`.
4. Phụ lục câu hỏi trắc nghiệm đầy đủ A, B, C, D kèm **Đáp án & Giải thích cho giáo viên** *(nếu slide có câu hỏi trắc nghiệm cần trình bày trọn vẹn)*.
5. Phong cách thiết kế, quy tắc bố cục, prompt hoàn chỉnh cho công cụ được chọn (PowerPoint/Canva và/hoặc hướng dẫn + prompt **NotebookLM**), checklist rà soát.

## Xuất tài liệu Office (Dùng chung Office Generator)

- Chỉ xuất tệp PPTX khi người dùng yêu cầu tạo file PowerPoint/Office (hoặc trọn bộ bài dạy); nếu người dùng chỉ yêu cầu kịch bản Markdown hoặc trả lời văn bản thì **không tự ý tạo thêm PPTX**, và **không chạy công cụ khi chưa có dữ liệu slide/kịch bản Markdown có cấu trúc hợp lệ**.
- Sau khi lưu kịch bản slide Markdown (hoặc JSON SlideDeck), gọi bộ máy dùng chung:
  ```bash
  python scripts/office_generator/cli.py pptx --input <duong_dan_Kich_ban.md> --output <duong_dan_Slide.pptx> --template education --speaker-notes <Speaker_Notes.md>
  ```
  *(Hỗ trợ theme: `education`, `lesson`, `assessment`; có thể truyền trực tiếp `SlideDeck` qua Python API `scripts.office_generator.generate_document`).*
- Giữ nguyên tệp Markdown gốc; kiểm định lại bằng `python scripts/office_generator/cli.py validate --input <duong_dan_Slide.pptx> --source <duong_dan_Kich_ban.md>` (nếu thiếu thư viện, hướng dẫn `pip install -r scripts/office_generator/requirements.txt`).

## Hướng dẫn sử dụng & Ví dụ thực tế

- **Cách dùng hiệu quả:** Cho biết *lớp, môn, tên bài, thời lượng, mục tiêu hoặc nội dung giáo án nguồn* và *công cụ đích (PowerPoint, Canva hay NotebookLM)*.
- **Ví dụ yêu cầu thực tế:**
  - *"Thiết kế kịch bản slide 45 phút cho Tin học 11 bài 'Cơ sở dữ liệu quan hệ: Khóa chính, khóa ngoại và liên kết bảng' để làm trên Canva/PowerPoint, kèm hướng dẫn tạo nhanh bằng NotebookLM và câu hỏi trắc nghiệm đầy đủ A, B, C, D."*
  - *"Chuyển kế hoạch bài dạy Tin học 10 bài 'Mạng máy tính và Internet' thành bộ 10 slide tối giản cho PowerPoint kèm Speaker Notes cho từng slide."*
