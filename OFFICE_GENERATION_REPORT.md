# BÁO CÁO HOÀN THIỆN CHỨC NĂNG XUẤT FILE OFFICE (DOCX & PPTX)

- **Dự án:** Vietnamese Teacher AI Skills
- **Thời điểm thực hiện & kiểm định:** 24/11/2026
- **Mục tiêu:** Xây dựng bộ công cụ xuất Microsoft Word (`.docx`) và PowerPoint (`.pptx`) tái sử dụng cho mọi bài dạy, tích hợp trực tiếp vào `lesson-planner` và `slide-designer`, và kiểm chứng thực tế trên **Bài 16 – Tin học 10 (Kết nối tri thức với cuộc sống)**.

---

## 1. Môi trường thực thi & Thư viện đã cài đặt

| Thành phần | Phiên bản thực tế đã xác minh | Ghi chú |
|---|---|---|
| **Python** | `3.12.3` | Chạy ổn định trên Windows |
| **pip** | `24.0` | Quản lý gói Python |
| **`python-docx`** | `1.2.0` | Thư viện tạo/đọc Microsoft Word (`.docx`) |
| **`python-pptx`** | `1.0.2` | Thư viện tạo/đọc Microsoft PowerPoint (`.pptx`) |
| **Phụ thuộc đi kèm** | `lxml 6.1.3`, `Pillow 13.0.0`, `XlsxWriter 3.3.4`, `typing_extensions 4.16.0` | Cài tự động cùng `python-docx` và `python-pptx` |

### Cách cài đặt lại trên máy mới
```bash
pip install -r scripts/document_generator/requirements.txt
```
*(Hoặc trực tiếp: `pip install python-docx python-pptx`)*

---

## 2. Bộ công cụ xuất Office đã xây dựng (`scripts/document_generator/`)

| Tệp | Chức năng chính |
|---|---|
| `scripts/document_generator/common.py` | Bộ phân tích cú pháp Markdown dùng chung (`parse_markdown_blocks`, `parse_inline_spans`) và bộ phân tích kịch bản slide (`parse_slide_script_markdown`) hỗ trợ cả khối mã nhiều dòng (` ```python ... ``` `) và bảng Markdown lồng bên trong ô nội dung slide. |
| `scripts/document_generator/generate_docx.py` | Chuyển KHBD Markdown → Word (`.docx`) khổ **A4 (`21,0 × 29,7 cm`)**, lề chuẩn văn bản giáo dục (`Trên/Dưới 2,0 cm`, `Trái 2,8 cm`, `Phải 1,8 cm`), font **Times New Roman** (cỡ nội dung mặc định `13 pt`, hỗ trợ `--font-size 14`), mã code **Consolas**, đề mục `I–V` rõ ràng, bảng tự tính độ rộng cột (`tblHeader` lặp tiêu đề trang, `cantSplit` chống vỡ hàng), Header từ trang 2 và Footer kèm số trang động `Trang X / Y`. |
| `scripts/document_generator/generate_pptx.py` | Chuyển Kịch bản PowerPoint Markdown → PowerPoint (`.pptx`) tỷ lệ **16:9 (`13,333 × 7,5 in`)**, font **Segoe UI** + **Consolas**, tự động phân tích từng slide để chọn **9 bố cục trực quan khác nhau** (`cover`, `cards_3col`, `process_flow`, `quiz_cards`, `code_focus`, `grid_2x2`, `table_compare`, `split_practice`, `summary_dark`), định dạng khung code editor / IDLE Shell và nhúng trực tiếp **Speaker Notes** vào từng slide. |
| `scripts/document_generator/requirements.txt` | Khai báo phụ thuộc chuẩn (`python-docx>=1.2.0`, `python-pptx>=1.0.2`). |
| `scripts/document_generator/README.md` | Hướng dẫn cài đặt, câu lệnh CLI và quy trình tích hợp với Agent Skills. |

### Hướng dẫn sử dụng nhanh (tái sử dụng cho mọi bài dạy)

- **Tạo KHBD Word (`.docx`):**
  ```bash
  python scripts/document_generator/generate_docx.py <duong_dan_KHBD.md> <duong_dan_ra.docx>
  ```
- **Tạo PowerPoint (`.pptx`):**
  ```bash
  python scripts/document_generator/generate_pptx.py <duong_dan_Kich_ban.md> <duong_dan_ra.pptx>
  ```

---

## 3. Tích hợp vào quy trình Agent Skills

Chỉ cập nhật bổ sung quy trình xuất tệp tự động cho **2 Skill liên quan** (giữ nguyên 100% quy tắc chuyên môn hiện có, không chỉnh sửa 7 Skill còn lại):

1. **`.agents/skills/lesson-planner/SKILL.md`:** Bổ sung mục *Tự động xuất tệp Word (`.docx`)* gọi `scripts/document_generator/generate_docx.py` ngay sau khi lưu KHBD Markdown và xác minh bằng `python-docx`.
2. **`.agents/skills/slide-designer/SKILL.md`:** Bổ sung mục *Tự động xuất tệp PowerPoint (`.pptx`)* gọi `scripts/document_generator/generate_pptx.py` ngay sau khi lưu kịch bản PowerPoint Markdown và xác minh bằng `python-pptx`.

- **Kiểm định cấu trúc bộ Skills sau tích hợp:** `python scripts/validate_skills.py` → `Validation passed: 9 skills found.`

---

## 4. Kết quả chạy thử thực tế & Kiểm định sản phẩm trên Bài 16 Tin học 10

### 4.1. Sản phẩm đầu ra đã tạo (giữ nguyên toàn bộ tệp Markdown gốc)
- `output/bai-16-tin-hoc-10/KHBD_Bai_16.docx` — **61.835 bytes** *(nguồn: `01_KHBD_Bai_16.md`)*
- `output/bai-16-tin-hoc-10/Bai_16_Ngon_ngu_lap_trinh_va_Python.pptx` — **99.286 bytes** *(nguồn: `02_Kich_ban_PowerPoint.md`)*

### 4.2. Lỗi thực tế đã phát hiện và khắc phục trong quá trình kiểm thử
- **Phát hiện 1 (Parser slide gặp khối code nhiều dòng & bảng lồng trong ô):** Ở lần chạy đầu tiên, bộ phân tích dòng đơn dừng tại Slide 11 (chứa khối ` ```python ... ``` ` 5 dòng) nên chỉ xuất 10/18 slide. Đã nâng cấp `parse_slide_script_markdown()` trong `common.py` để gom đúng hàng slide nhiều dòng và tách 6 cột an toàn ngoài cặp backtick (giữ nguyên bảng so sánh lồng ở Slide 12 và không sửa bất kỳ nội dung nào của file Markdown gốc). Kết quả sau sửa: xuất đủ **18/18 slide** và **9/9 bố cục**.

### 4.3. Bảng kiểm định thực tế bằng `python-docx` và `python-pptx` (8/8 tiêu chí)

| TT | Tiêu chí kiểm định | Trạng thái | Bằng chứng đo kiểm thực tế |
|---:|---|:---:|---|
| 1 | **DOCX mở và đọc được** | **PASS** | Mở thành công bằng `docx.Document(...)`; khổ giấy **21,00 × 29,70 cm (A4)**; lề `T=2,0 / B=2,0 / L=2,8 / R=1,8 cm`; Normal font **Times New Roman 13,0 pt**; Header `'KẾ HOẠCH BÀI DẠY – TIN HỌC LỚP 10 (BÀI 16)'`; Footer có trường động `PAGE` / `NUMPAGES`. |
| 2 | **PPTX mở và đọc được** | **PASS** | Mở thành công bằng `pptx.Presentation(...)`; kích thước **13,333 × 7,500 in** (tỷ lệ `1,778` = đúng **16:9**). |
| 3 | **Số lượng slide & đa dạng bố cục** | **PASS** | Đúng **18 / 18 slide** khớp kịch bản Markdown; sử dụng **9 bố cục khác nhau** (`cover`, `cards_3col`, `process_flow`, `quiz_cards`, `code_focus`, `grid_2x2`, `table_compare`, `split_practice`, `summary_dark`). |
| 4 | **Kiểm tra tràn chữ trên slide** | **PASS** | Chạy kiểm tra ước lượng chiều cao văn bản/hộp chữ trên toàn bộ shape của 18 slide → **0 cảnh báo tràn chữ (`Overflow warnings: 0`)**. |
| 5 | **Các bảng trong Word** | **PASS** | Có đủ **4/4 bảng** (`9×4`, `9×6`, `5×3`, `5×4`), tổng bề rộng cột mỗi bảng đúng **16,40 cm** khớp vùng in A4, **100% bảng** bật `tblHeader=True` (lặp tiêu đề khi sang trang) và `cantSplit=True` (không cắt đôi dòng). |
| 6 | **Nội dung tiếng Việt** | **PASS** | Kiểm tra UTF-8 tiếng Việt có dấu trên cả DOCX (`DOCX VN check: True`) và PPTX (`18/18` tiêu đề khớp nguyên văn, không lỗi dấu/mojibake). |
| 7 | **Đối chiếu DOCX với `01_KHBD_Bai_16.md`** | **PASS** | Đủ `222` đoạn văn + `4` bảng; kiểm tra 15 mốc cấu trúc bắt buộc (`THÔNG TIN BÀI HỌC`, `I. MỤC TIÊU` → `V. ĐIỀU CHỈNH SAU BÀI DẠY`, đủ 7 hoạt động HĐ 1 → HĐ 4, mã Python mẫu) → **0 mục thiếu (`Missing: []`)**. |
| 8 | **Đối chiếu PPTX với `02_Kich_ban_PowerPoint.md`** | **PASS** | `18/18` tiêu đề khớp chính xác; **18/18 slide có Speaker Notes**; Slide 11 hiển thị đúng khung IDLE Shell (`>>> 15 + 25` / `40` / `print(...)`); Slide 12 dựng đúng **bảng PowerPoint gốc 4×3** (`Tiêu chí | Trực tiếp (>>>) | Soạn thảo (.py)`); cả 3 slide trắc nghiệm (Slide 6, 9, 13) có đủ **A, B, C, D**, **không lộ đáp án trên mặt slide** và **đặt đáp án + giải thích trong Speaker Notes**. |

---

## 5. Lưu ý vận hành & Đề xuất hoàn thiện tiếp theo

1. **Kiểm tra trực quan cuối cùng bằng Microsoft Word / PowerPoint:** Do môi trường máy chủ chạy không có Microsoft Office/LibreOffice để xuất ảnh chụp từng trang/slide, kiểm định chống tràn chữ hiện được thực hiện bằng công thức đo hình học + kiểm tra cấu trúc XML/text qua `python-docx` và `python-pptx`. Khi sử dụng lần đầu trên máy chiếu lớp học, giáo viên nên mở nhanh bằng PowerPoint/Word để tinh chỉnh thêm ảnh chụp giao diện IDLE thực tế (Slide 10) hoặc hiệu ứng `Appear` cho đáp án nếu cần.
2. **Quyền ghi thư mục trên Windows khi chạy từ sandbox:** Khi chạy `generate_docx.py` / `generate_pptx.py` ghi vào thư mục có sẵn được tạo bởi tiến trình khác, cần đảm bảo tiến trình Python có quyền ghi vào thư mục đích `output/`.
3. **Mở rộng trong tương lai:** Có thể bổ sung tùy chọn xuất thêm đề kiểm tra (`03_Cau_hoi_Danh_gia.md`) sang DOCX khổ A4 có khung phách/điểm và hỗ trợ chèn ảnh PNG/SVG tự động vào slide khi kịch bản có đính kèm đường dẫn hình ảnh thực tế.
