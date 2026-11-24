# BÁO CÁO TRIỂN KHAI SHARED OFFICE DOCUMENT GENERATOR (V1.2)
**Dự án:** Vietnamese Teacher AI Skills  
**Thời điểm hoàn thành:** 24/11/2026  
**Phạm vi:** Nâng cấp kiến trúc cấp hệ thống giúp toàn bộ 9 Agent Skills dùng chung một bộ máy xuất và kiểm định tài liệu Microsoft Office (DOCX, PPTX, mở rộng PDF).

---

## 1. Kiến trúc mới

Hệ thống tách biệt hoàn toàn 4 tầng trách nhiệm: **Parsing (Phân tích nguồn)** → **Templates (Cấu hình mẫu/theme tách biệt)** → **Format Engines (DOCX / PPTX / PDF độc lập)** → **Shared Validator & CLI/API**:

```text
scripts/
├── __init__.py
├── validate_skills.py
├── document_generator/            # Lớp tương thích ngược mỏng ủy quyền về office_generator
│   ├── generate_docx.py           # Wrapper -> scripts.office_generator.generate_document
│   └── generate_pptx.py           # Wrapper -> scripts.office_generator.generate_document
└── office_generator/              # Thành phần dùng chung cốt lõi (V1.2)
    ├── __init__.py                # Xuất khẩu API công khai
    ├── models.py                  # SlideModel, SlideDeck, DocxTemplateConfig, PptxTemplateConfig, ValidationReport...
    ├── markdown_parser.py         # Parser Markdown + Parser SlideDeck (bảng 6 cột / ## Slide N: / JSON)
    ├── docx_engine.py             # Bộ máy python-docx (A4, Times New Roman, bảng, ảnh, ngắt trang/section, header/footer)
    ├── pptx_engine.py             # Bộ máy python-pptx (16:9, 13 bố cục, auto font-size, ảnh, code, Speaker Notes)
    ├── pdf_engine.py              # Mở rộng PDF có kiểm soát (LibreOffice soffice / docx2pdf)
    ├── validator.py               # Bộ kiểm định dùng chung DOCX/PPTX & đối chiếu nguồn
    ├── generator.py               # API thống nhất generate_document() & run_batch()
    ├── cli.py                     # CLI đa lệnh cho Windows PowerShell / Gemini CLI / Antigravity
    ├── requirements.txt
    └── README.md

templates/
└── office/
    ├── docx/
    │   ├── __init__.py            # Registry: khbd, exam/assessment, matrix, answer_key, study_material, teacher_guide, general
    │   ├── khbd_template.py
    │   ├── assessment_template.py
    │   └── general_document_template.py
    └── pptx/
        ├── __init__.py            # Registry: education, lesson, assessment/quiz
        ├── education_template.py
        ├── lesson_template.py
        └── assessment_template.py

tests/
└── office_generator/
    ├── __init__.py
    ├── test_parser.py
    ├── test_docx.py
    ├── test_pptx.py
    └── test_validator.py
```

---

## 2. Danh sách file mới đã tạo

- **Bộ máy dùng chung (`scripts/office_generator/`):**
  - `scripts/__init__.py`
  - `scripts/office_generator/__init__.py`
  - `scripts/office_generator/models.py`
  - `scripts/office_generator/markdown_parser.py`
  - `scripts/office_generator/docx_engine.py`
  - `scripts/office_generator/pptx_engine.py`
  - `scripts/office_generator/pdf_engine.py`
  - `scripts/office_generator/validator.py`
  - `scripts/office_generator/generator.py`
  - `scripts/office_generator/cli.py`
  - `scripts/office_generator/requirements.txt`
  - `scripts/office_generator/README.md`
- **Hệ thống Template tách biệt (`templates/office/`):**
  - `templates/__init__.py`, `templates/office/__init__.py`
  - `templates/office/docx/__init__.py`, `khbd_template.py`, `assessment_template.py`, `general_document_template.py`
  - `templates/office/pptx/__init__.py`, `education_template.py`, `lesson_template.py`, `assessment_template.py`
- **Bộ kiểm thử tự động (`tests/office_generator/`):**
  - `tests/office_generator/__init__.py`, `test_parser.py`, `test_docx.py`, `test_pptx.py`, `test_validator.py`
- **Sản phẩm kiểm thử thực tế Bài 16 & Báo cáo:**
  - `output/bai-16-tin-hoc-10/Speaker_Notes_Bai_16.md`
  - `output/bai-16-tin-hoc-10/OFFICE_GENERATION_REPORT.md`
  - `OFFICE_GENERATOR_IMPLEMENTATION_REPORT.md`

---

## 3. Danh sách file đã chỉnh sửa

- **9 file `SKILL.md`** (chỉ bổ sung mục *Xuất tài liệu Office* trỏ tới `scripts/office_generator/cli.py`, không thay đổi nội dung chuyên môn và không ảnh hưởng frontmatter kích hoạt):
  - `.agents/skills/lesson-planner/SKILL.md`
  - `.agents/skills/slide-designer/SKILL.md`
  - `.agents/skills/assessment-generator/SKILL.md`
  - `.agents/skills/curriculum-analyzer/SKILL.md`
  - `.agents/skills/teaching-assistant/SKILL.md`
  - `.agents/skills/digital-competency/SKILL.md`
  - `.agents/skills/ai-education/SKILL.md`
  - `.agents/skills/ai-video-creator/SKILL.md`
  - `.agents/skills/informatics-expert/SKILL.md`
- **Chống trùng lặp mã nguồn (giữ tương thích ngược, không xóa tệp cũ):**
  - `scripts/document_generator/generate_docx.py` (chuyển sang wrapper gọi `scripts.office_generator`)
  - `scripts/document_generator/generate_pptx.py` (chuyển sang wrapper gọi `scripts.office_generator`)
- **Cập nhật tệp xuất Bài 16 bằng engine V1.2 mới & Lịch sử phiên bản:**
  - `output/bai-16-tin-hoc-10/KHBD_Bai_16.docx`
  - `output/bai-16-tin-hoc-10/Bai_16_Ngon_ngu_lap_trinh_va_Python.pptx`
  - `CHANGELOG.md` (bổ sung mục `[1.2.0]`, giữ nguyên `[1.1.0]` và `[1.0.0]`)

---

## 4. Các thư viện sử dụng và phiên bản thực tế

| Thư viện / Môi trường | Phiên bản thực tế | Vai trò |
|---|---|---|
| Python | `3.12.3` | Ngôn ngữ thực thi (chuẩn `unittest`, `pathlib`, `dataclasses`, `argparse`) |
| `python-docx` | `1.2.0` | Tạo, định dạng và kiểm định tệp Word (`.docx`) không cần Microsoft Word |
| `python-pptx` | `1.0.2` | Tạo, định dạng, nhúng Speaker Notes và kiểm định PowerPoint (`.pptx`) không cần PowerPoint |
| `Pillow` (`pillow`) | `13.0.0` | Xử lý hình ảnh khi chèn ảnh vào DOCX/PPTX và tạo ảnh kiểm thử |
| `lxml` | `6.1.3` | Xử lý OpenXML (`tblHeader`, `cantSplit`, trường `PAGE`/`NUMPAGES`, viền/nền bảng) |
| LibreOffice (`soffice`) / `docx2pdf` | *Chưa cài trên máy hiện tại* | Backend mở rộng tùy chọn cho `pdf_engine.py` |

---

## 5. Cách cài đặt

Không yêu cầu cài Microsoft Word hay PowerPoint, không chỉnh sửa PATH hệ thống:

```powershell
pip install -r scripts/office_generator/requirements.txt
```

---

## 6. Cách gọi Python API

```python
from scripts.office_generator import SlideDeck, SlideModel, generate_document

# 1. Xuất KHBD Word từ Markdown với tùy biến trường/giáo viên
res_docx = generate_document(
    source_file="output/bai-16-tin-hoc-10/01_KHBD_Bai_16.md",
    output_file="output/bai-16-tin-hoc-10/KHBD_Bai_16.docx",
    format="docx",
    template="khbd",
    overrides={"school_name": "Trường THPT Mẫu", "teacher_name": "Nguyễn Văn A"},
)

# 2. Xuất PowerPoint từ kịch bản Markdown (hoặc truyền trực tiếp SlideDeck)
res_pptx = generate_document(
    source_file="output/bai-16-tin-hoc-10/02_Kich_ban_PowerPoint.md",
    output_file="output/bai-16-tin-hoc-10/Bai_16_Ngon_ngu_lap_trinh_va_Python.pptx",
    format="pptx",
    template="education",
    speaker_notes_file="output/bai-16-tin-hoc-10/Speaker_Notes_Bai_16.md",
)
```

---

## 7. Cách sử dụng CLI (Windows PowerShell / Gemini CLI / Antigravity)

```powershell
# Xuất DOCX theo mẫu giáo dục Việt Nam
python scripts/office_generator/cli.py docx --input input.md --output output.docx --template khbd

# Xuất PPTX 16:9 theo theme & xuất kèm Speaker Notes
python scripts/office_generator/cli.py pptx --input slides.md --output slides.pptx --template education --speaker-notes Speaker_Notes.md

# Kiểm định độc lập tệp DOCX hoặc PPTX đối chiếu với nguồn
python scripts/office_generator/cli.py validate --input output.docx --source input.md

# Xuất hàng loạt nhiều tài liệu trong một lần chạy
python scripts/office_generator/cli.py batch --config batch.json
```

---

## 8. Các Agent Skills đã tích hợp (9/9 Skill)

| STT | Skill | Định dạng tích hợp | Template mặc định | Nguyên tắc kích hoạt xuất Office |
|---:|---|---|---|---|
| 1 | `lesson-planner` | DOCX | `khbd` | Chỉ xuất khi người dùng yêu cầu tạo file Office/trọn bộ bài dạy |
| 2 | `slide-designer` | PPTX (+ Speaker Notes) | `education`, `lesson`, `assessment` | Chỉ xuất khi có kịch bản cấu trúc hợp lệ và người dùng yêu cầu PPTX |
| 3 | `assessment-generator` | DOCX + PPTX *(tùy chọn)* | `exam`, `matrix`, `answer_key`, `assessment` | Xuất đề/ma trận/đáp án DOCX; slide câu hỏi PPTX khi được yêu cầu |
| 4 | `curriculum-analyzer` | DOCX | `teacher_guide` | Xuất báo cáo phân tích chương trình/SGK khi được yêu cầu |
| 5 | `teaching-assistant` | DOCX | `teacher_guide`, `study_material` | Xuất tài liệu chủ nhiệm, hoạt động học tập khi được yêu cầu |
| 6 | `digital-competency` | DOCX | `teacher_guide` | Xuất bảng đối chiếu năng lực số khi được yêu cầu |
| 7 | `ai-education` | DOCX | `study_material`, `khbd` | Xuất tài liệu hướng dẫn / giáo án giáo dục AI khi được yêu cầu |
| 8 | `ai-video-creator` | DOCX | `general` | Xuất kịch bản video, Character Bible & Storyboard khi được yêu cầu |
| 9 | `informatics-expert` | DOCX | `study_material` | Xuất tài liệu chuyên môn & phiếu thực hành Tin học khi được yêu cầu |

- Kiểm định toàn bộ 9 Skill: `python scripts/validate_skills.py` → **`Validation passed: 9 skills found.`**

---

## 9. Kết quả 10 nhóm kiểm thử tự động

Chạy thực tế lệnh `python -m unittest discover -s tests/office_generator -v` → **14/14 test PASS (2,177 giây)**:

| Nhóm kiểm thử | Bài kiểm thử thực thi | Kết quả |
|---|---|---:|
| 1. Markdown sang DOCX | `test_docx.py::test_group1_3_4_7_...`, `test_all_vietnamese_docx_templates` (7 template) | **PASS** |
| 2. Markdown sang PPTX | `test_pptx.py::test_markdown_to_pptx_and_themes` (3 theme × 18 slides) | **PASS** |
| 3. Tạo DOCX có bảng | `test_docx.py::test_group1_3_4_7_...` (kiểm tra bảng + chú thích bảng) | **PASS** |
| 4. Tạo DOCX có danh sách | `test_docx.py::test_group1_3_4_7_...` (danh sách dấu đầu dòng lồng cấp & đánh số) | **PASS** |
| 5. Tạo PPTX có hình ảnh | `test_pptx.py::test_group2_5_6_7_all_13_layouts_...` (chèn PNG thật, `embedded_image_count >= 1`) | **PASS** |
| 6. Tạo PPTX có mã Python | `test_pptx.py::test_group2_5_6_7_all_13_layouts_...` (kiểm chứng khung code & font `Consolas`) | **PASS** |
| 7. Kiểm tra tiếng Việt | `test_docx.py` & `test_pptx.py` (xác minh bảo toàn dấu tiếng Việt trên cả DOCX và PPTX) | **PASS** |
| 8. Kiểm tra lỗi file | `test_docx.py`, `test_parser.py`, `test_validator.py` (thiếu file, file hỏng, Markdown sai cấu trúc slide, PDF thiếu backend) | **PASS** |
| 9. Batch generation | `test_docx.py::test_group9_batch_generation_via_cli` (xuất đồng thời DOCX + PPTX + báo cáo) | **PASS** |
| 10. Tích hợp với 9 Skill | `test_validator.py::test_group10_all_9_skills_integrated_and_valid` (`validate_skills.py` + kiểm tra 9/9 `SKILL.md`) | **PASS** |

---

## 10. Kết quả xuất thực tế Bài 16 Tin học 10

Chạy batch từ nguồn nguyên bản `output/bai-16-tin-hoc-10/01_KHBD_Bai_16.md` và `02_Kich_ban_PowerPoint.md` (không sửa nội dung chuyên môn Bài 16):

| Sản phẩm tạo ra | Kích thước | Kết quả `cli.py validate` | Chỉ số xác minh thực tế |
|---|---:|:---:|---|
| `output/bai-16-tin-hoc-10/KHBD_Bai_16.docx` | `61.787 bytes` | **PASS** (`0 errors, 0 warnings`) | A4 `21,0 × 29,7 cm`, Times New Roman `13 pt`, `222` đoạn, `4/4` bảng, `28/28` tiêu đề khớp nguồn, có số trang `PAGE/NUMPAGES`, tiếng Việt nguyên vẹn. |
| `output/bai-16-tin-hoc-10/Bai_16_Ngon_ngu_lap_trinh_va_Python.pptx` | `99.135 bytes` | **PASS** (`0 errors, 0 warnings`) | Tỷ lệ `16:9` (`13,333 × 7,5 in`), đủ `18/18` slide (`0` slide rỗng), `18/18` khớp tiêu đề nguồn, `18/18` có Speaker Notes nhúng, `1` bảng PowerPoint gốc (Slide 12), `0` cảnh báo tràn chữ. |
| `output/bai-16-tin-hoc-10/Speaker_Notes_Bai_16.md` | `203 dòng` | Đầy đủ `18/18` slide | Lưu riêng toàn bộ ghi chú thuyết trình & gợi ý hình ảnh để GV xem song song trên điện thoại/máy tính bảng. |
| `output/bai-16-tin-hoc-10/OFFICE_GENERATION_REPORT.md` | `44 dòng` | Tự động xuất bởi batch | Bảng chỉ số kiểm định đầy đủ cho cả DOCX và PPTX của Bài 16. |

---

## 11. Các giới hạn còn tồn tại

1. **Chưa kiểm tra hình thức trực quan bằng render PDF/ảnh:** Máy hiện tại chưa cài LibreOffice (`soffice`) hay Microsoft Office/docx2pdf, nên chức năng `pdf_engine.py` trả về cảnh báo kiểm soát rõ ràng và việc kiểm định chống tràn chữ dựa trên phép đo hình học bounding-box từ `python-pptx`. Khuyến nghị giáo viên mở kiểm tra nhanh 1 lần bằng Word/PowerPoint trước giờ dạy.
2. **Biểu thức toán học LaTeX phức tạp (`\frac`, `\sum`) và sơ đồ Mermaid:** Hiện được hiển thị an toàn dưới dạng văn bản/khối mã có ghi chú cảnh báo `unconvertible` trong báo cáo kiểm định, chưa render trực tiếp thành OMML equation hoặc ảnh PNG tự động.
3. **Quyền ghi thư mục Windows Sandbox:** Khi chạy CLI từ môi trường sandbox Windows ghi đè vào thư mục `output/` do tiến trình ngoài tạo sẵn, cần cấp quyền ghi cho thư mục đích.

---

## 12. Hướng phát triển tiếp theo

- **Xuất XLSX (`xlsx_engine.py`):** Hỗ trợ xuất ma trận đề kiểm tra, bảng điểm, sổ theo dõi chủ nhiệm và rubric chấm điểm tự động tính công thức Excel.
- **Tài liệu HTML & Song ngữ:** Thêm bộ xuất HTML tương tác cho học liệu số và chế độ xuất tài liệu song ngữ Việt – Anh (dành cho lớp Tin học/STEM tăng cường).
- **Bộ nhận diện thương hiệu nhà trường dạng JSON/YAML:** Cho phép nhà trường lưu 1 tệp `school_profile.json` (logo, màu chủ đạo, header/footer, tên trường, tổ chuyên môn) để mọi giáo viên dùng chung trong lệnh `batch`.
- **Render sơ đồ Mermaid & kiểm định hình ảnh (Visual QA):** Tích hợp tùy chọn render LibreOffice headless → PNG để kiểm tra trực quan tự động từng trang Word và từng slide PowerPoint.
