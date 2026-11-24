# Office Document Generator – Vietnamese Teacher AI Skills

Thành phần dùng chung cấp hệ thống giúp tất cả 9 Agent Skills trong **Vietnamese Teacher AI Skills** xuất tài liệu **Microsoft Word (`.docx`)**, **PowerPoint (`.pptx`)** và mở rộng **PDF** theo chuẩn giáo dục Việt Nam mà không cần cài đặt Microsoft Office.

---

## 1. Cài đặt

```bash
pip install -r scripts/office_generator/requirements.txt
```

*(Tùy chọn để bật xuất PDF: cài thêm [LibreOffice](https://www.libreoffice.org/) có lệnh `soffice` trong PATH, hoặc `pip install docx2pdf` nếu máy có Microsoft Word.)*

---

## 2. Sử dụng qua CLI (Windows PowerShell / Gemini CLI / Antigravity)

### Xuất Word (`.docx`)
```powershell
python scripts/office_generator/cli.py docx --input input.md --output output.docx --template khbd
```
**Các mẫu DOCX hỗ trợ (`--template`):**
- `khbd` / `lesson_plan`: Kế hoạch bài dạy (Công văn 5512/2345, A4, Times New Roman 13 pt).
- `assessment` / `exam`: Đề kiểm tra.
- `matrix`: Ma trận và bản đặc tả đề kiểm tra.
- `answer_key`: Đáp án và hướng dẫn chấm.
- `study_material`: Tài liệu học tập, phiếu bài tập, bài thực hành.
- `teacher_guide`: Tài liệu giáo viên, báo cáo phân tích, bảng năng lực số.
- `general`: Tài liệu giáo dục chung.

### Xuất PowerPoint (`.pptx`)
```powershell
python scripts/office_generator/cli.py pptx --input slides.md --output slides.pptx --template education --speaker-notes Speaker_Notes.md
```
**Các theme PPTX hỗ trợ (`--template`):** `education`, `lesson`, `assessment`.  
**13 bố cục hỗ trợ:** `title_slide`, `section_divider`, `text_image`, `two_columns`, `comparison`, `timeline`, `process`, `diagram`, `table`, `code_example`, `quiz`, `summary`, `closing`.

### Kiểm định tệp Office
```powershell
python scripts/office_generator/cli.py validate --input output.docx --source input.md --report QA_Report.md
```

### Xuất hàng loạt (Batch Mode)
```powershell
python scripts/office_generator/cli.py batch --config batch.json
```

---

## 3. Sử dụng qua Python API

```python
from scripts.office_generator import generate_document

res_docx = generate_document(
    source_file="output/bai-16-tin-hoc-10/01_KHBD_Bai_16.md",
    output_file="output/bai-16-tin-hoc-10/KHBD_Bai_16.docx",
    format="docx",
    template="khbd",
    overrides={"school_name": "Trường THPT Mẫu", "teacher_name": "Nguyễn Văn A"},
)

res_pptx = generate_document(
    source_file="output/bai-16-tin-hoc-10/02_Kich_ban_PowerPoint.md",
    output_file="output/bai-16-tin-hoc-10/Bai_16.pptx",
    format="pptx",
    template="education",
    speaker_notes_file="output/bai-16-tin-hoc-10/Speaker_Notes_Bai_16.md",
)
```

Có thể truyền trực tiếp đối tượng `SlideDeck` / `SlideModel` vào tham số `slide_deck=...` của `generate_document()`.
