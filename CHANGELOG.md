# Changelog

Mọi thay đổi quan trọng của bộ **Vietnamese Teacher AI Skills** được ghi nhận tại tệp này.

---

## [1.2.0] - 2026-11-24

### Nâng cấp kiến trúc cấp hệ thống: Shared Office Document Generator

1. **Xây dựng bộ máy xuất Office dùng chung (`scripts/office_generator/`):**
   - Tách rõ kiến trúc modular: `models.py`, `markdown_parser.py`, `docx_engine.py`, `pptx_engine.py`, `pdf_engine.py`, `validator.py`, `generator.py`, `cli.py`, `__init__.py`, `requirements.txt`, `README.md`.
   - API thống nhất `generate_document(source_file, output_file, format, template, ...)` hỗ trợ `docx`, `pptx` (nhận cả Markdown/JSON hoặc trực tiếp `SlideDeck`/`SlideModel`), `pdf` (mở rộng có kiểm soát qua LibreOffice/`docx2pdf`) và `run_batch()`.
   - CLI tối ưu cho Windows PowerShell / Gemini CLI / Antigravity: `docx`, `pptx`, `pdf`, `validate`, `batch`.
   - Hệ thống kiểm định chất lượng dùng chung (`validator.py`) xác minh tệp mở được bằng `python-docx`/`python-pptx`, đối chiếu nguồn Markdown, kiểm tra dấu tiếng Việt, phát hiện slide rỗng & nguy cơ tràn chữ, phân biệt `file_error` / `content_error` / `format_warning` / `unconvertible`.
   - Chuyển đổi `scripts/document_generator/generate_docx.py` và `generate_pptx.py` thành lớp tương thích mỏng gọi sang `scripts/office_generator/` để loại bỏ trùng lặp mã nguồn mà không xóa tệp cũ.

2. **Tách riêng hệ thống Template (`templates/office/`):**
   - 7 cấu hình DOCX chuẩn giáo dục Việt Nam (A4, Times New Roman 13–14 pt, không hardcode tên trường/giáo viên, hỗ trợ logo & header/footer tùy chỉnh): `khbd`, `assessment`/`exam`, `matrix`, `answer_key`, `study_material`, `teacher_guide`, `general`.
   - 3 theme PPTX 16:9 (`education`, `lesson`, `assessment`) cùng **13 bố cục trình chiếu**: `title_slide`, `section_divider`, `text_image`, `two_columns`, `comparison`, `timeline`, `process`, `diagram`, `table`, `code_example`, `quiz`, `summary`, `closing`, hỗ trợ nhúng Speaker Notes và xuất `Speaker_Notes_*.md`.

3. **Tích hợp dùng chung trên toàn bộ 9 Agent Skills (`.agents/skills/*/SKILL.md`):**
   - Tích hợp chỉ dẫn gọi `scripts/office_generator/cli.py` phù hợp với vai trò của từng Skill (`lesson-planner`, `slide-designer`, `assessment-generator`, `curriculum-analyzer`, `teaching-assistant`, `digital-competency`, `ai-education`, `ai-video-creator`, `informatics-expert`), không sao chép mã nguồn Office vào Skill và giữ nguyên toàn bộ quy tắc chuyên môn hiện có.

4. **Bộ kiểm thử tự động & Kiểm chứng thực tế Bài 16:**
   - Thêm 4 bộ kiểm thử tự động (`tests/office_generator/test_parser.py`, `test_docx.py`, `test_pptx.py`, `test_validator.py`) bao phủ đủ 10 nhóm kiểm thử (14/14 test PASS).
   - Chạy batch xuất thực tế Bài 16 Tin học 10: `KHBD_Bai_16.docx`, `Bai_16_Ngon_ngu_lap_trinh_va_Python.pptx`, `Speaker_Notes_Bai_16.md`, `output/bai-16-tin-hoc-10/OFFICE_GENERATION_REPORT.md` (cả DOCX và PPTX đều `VALIDATE [PASS]` với `0 errors, 0 warnings`).
   - Lập báo cáo tổng hợp triển khai tại `OFFICE_GENERATOR_IMPLEMENTATION_REPORT.md`.

---

## [1.1.0] - 2026-11-24

### Nâng cấp 4 Agent Skills dựa trên kết quả kiểm thử thực tế (`TEST_REPORT.md`)

1. **`lesson-planner`** (`.agents/skills/lesson-planner/SKILL.md`)
   - Bổ sung mục *Tài liệu tham chiếu bắt buộc*: yêu cầu đọc trước `../../../references/lesson-plan-template.md` và đối chiếu `../../../references/vietnam-education-guidance.md` khi soạn kế hoạch bài dạy theo Công văn 5512/2345.
   - Chuẩn hóa cấu trúc và cách đánh số mục theo hướng dẫn tham khảo Công văn 5512 (đặt *Thông tin bài học & Giả định* ở đầu trang không đánh số La Mã; bắt đầu `I. Mục tiêu` → `II. Thiết bị dạy học và học liệu` → `III. Tiến trình dạy học` với đủ 4 bước tổ chức → `IV. Đánh giá` → `V. Điều chỉnh sau bài dạy`).
   - Bổ sung phân biệt yêu cầu giữa cấp THCS/THPT (Công văn 5512) và cấp Tiểu học (Công văn 2345); nhấn mạnh không tự khẳng định bất kỳ biểu mẫu nào là bắt buộc duy nhất nếu tài liệu nguồn không chứng minh.
   - Bổ sung mục *Hướng dẫn sử dụng & Ví dụ thực tế*.

2. **`assessment-generator`** (`.agents/skills/assessment-generator/SKILL.md`)
   - Bổ sung tham chiếu trực tiếp đến `../../../references/vietnam-education-guidance.md` bên cạnh `../../../references/assessment-template.md`.
   - Bổ sung cơ chế xác định rõ lớp, môn, bộ sách, phạm vi kiến thức và kiểm soát độ khớp khối lớp theo Chương trình GDPT 2018 (không đưa kiến thức lớp 11 vào đề lớp 10 nếu không được yêu cầu; cảnh báo rõ tại Mục 1 khi yêu cầu giao thoa giữa lõi Tin học 10 và Tin học 11 định hướng KHMT).
   - Siết chặt quy tắc đối chiếu 1–1 giữa từng câu hỏi với Yêu cầu cần đạt (YCCĐ), phân loại mức độ nhận thức, kiểm soát thời lượng làm bài khả thi (đặc biệt đề 45 phút kết hợp thực hành lập trình) và kiểm chứng đáp án/mã nguồn trước khi bàn giao.
   - Bổ sung mục *Hướng dẫn sử dụng & Ví dụ thực tế*.

3. **`slide-designer`** (`.agents/skills/slide-designer/SKILL.md`)
   - Bổ sung quy tắc bắt buộc cho câu hỏi trắc nghiệm trên slide: trình bày đầy đủ cả 4 phương án A, B, C, D kèm phụ lục đáp án và giải thích dành cho giáo viên.
   - Chuẩn hóa việc tách bạch *Nội dung hiển thị trên slide* với *Ghi chú thuyết trình (Speaker Notes)* cho từng slide.
   - Bổ sung yêu cầu kiểm tra tính nhất quán giữa mục tiêu bài học (`M1, M2...`) ↔ slide nội dung ↔ câu hỏi đánh giá.
   - Bổ sung hướng dẫn và quy trình tạo slide bằng **NotebookLM** (chuẩn bị tài liệu nguồn cô đọng, Custom Prompt tiếng Việt, kiểm tra dấu tiếng Việt và giảng song song với Speaker Notes).
   - Bổ sung mục *Hướng dẫn sử dụng & Ví dụ thực tế*.

4. **`digital-competency`** (`.agents/skills/digital-competency/SKILL.md`)
   - Bổ sung liên kết trực tiếp bắt buộc đến `../../../references/vietnam-education-guidance.md` (yêu cầu đọc trước khi đưa ra kết luận về năng lực số).
   - Làm rõ nguyên tắc phân biệt rạch ròi giữa *mã chỉ báo có trong tài liệu chính thức* với *đề xuất vận dụng của AI*; tuyệt đối không tự tạo mã chỉ báo.
   - Bổ sung cột *Căn cứ gắn năng lực số* trong bảng đầu ra để giải thích rõ lý do sư phạm gắn từng thành tố vào từng hoạt động học tập.
   - Bổ sung mục *Hướng dẫn sử dụng & Ví dụ thực tế* cho cả hai trường hợp (chưa có khung và có văn bản khung chính thức).

### Sửa lỗi đường dẫn tham chiếu & Kiểm chứng
- Sửa đường dẫn tương đối `../../references/` → `../../../references/` trong 3 file `SKILL.md` (`ai-education`, `assessment-generator`, `lesson-planner`) và bổ sung các liên kết tham chiếu mới; xác minh toàn bộ đường dẫn tồn tại (`Exists=True`).
- Giữ nguyên không chỉnh sửa 5 Skill đã đạt toàn diện ở V1.0 (`ai-education` chỉ sửa 1 dòng đường dẫn trước đó, `ai-video-creator`, `curriculum-analyzer`, `informatics-expert`, `teaching-assistant`).
- Chạy lại `scripts/validate_skills.py` (`Validation passed: 9 skills found.`) và kiểm thử độc lập lại cả 4 Skill nâng cấp; ghi nhận kết quả so sánh trước–sau trong `TEST_REPORT.md`.

---

## [1.0.0] - Phát hành ban đầu
- Bộ 9 Agent Skills nền tảng cho giáo viên Việt Nam trong `.agents/skills/`.
- Tài liệu tham chiếu trong `references/` (`ai-literacy-framework.md`, `assessment-template.md`, `lesson-plan-template.md`, `vietnam-education-guidance.md`).
- Script kiểm tra cấu trúc cơ bản `scripts/validate_skills.py`.
