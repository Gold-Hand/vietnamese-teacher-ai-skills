# Document Generator – Bộ công cụ xuất DOCX & PPTX cho Vietnamese Teacher AI Skills

Bộ công cụ Python giúp chuyển đổi trực tiếp **Kế hoạch bài dạy (KHBD) Markdown** thành tệp **Microsoft Word (`.docx`)** chuẩn A4 và **Kịch bản PowerPoint Markdown** thành tệp **PowerPoint (`.pptx`)** tỷ lệ 16:9 có bố cục đa dạng và Speaker Notes.

## 1. Cấu trúc thư mục

```text
scripts/document_generator/
├── common.py          # Bộ phân tích Markdown & kịch bản slide dùng chung
├── generate_docx.py   # Xuất KHBD Markdown -> Word (.docx) khổ A4, Times New Roman
├── generate_pptx.py   # Xuất Kịch bản Slide Markdown -> PowerPoint (.pptx) 16:9
├── requirements.txt   # Danh sách thư viện cần thiết
└── README.md          # Tài liệu hướng dẫn sử dụng
```

## 2. Cài đặt

Yêu cầu Python 3.10+. Cài đặt thư viện phụ thuộc bằng `pip`:

```bash
pip install -r scripts/document_generator/requirements.txt
```

Hoặc cài trực tiếp:

```bash
pip install python-docx python-pptx
```

## 3. Hướng dẫn sử dụng

### A. Xuất Kế hoạch bài dạy sang Word (`.docx`)

```bash
python scripts/document_generator/generate_docx.py <duong_dan_KHBD.md> [duong_dan_ra.docx] [--font-size 13]
```

**Ví dụ (Bài 16 Tin học 10):**

```bash
python scripts/document_generator/generate_docx.py output/bai-16-tin-hoc-10/01_KHBD_Bai_16.md output/bai-16-tin-hoc-10/KHBD_Bai_16.docx
```

**Đặc điểm đầu ra DOCX:**
- Khổ giấy A4 (`21,0 × 29,7 cm`), lề văn bản giáo dục (Trên/Dưới `2,0 cm`, Trái `2,8 cm`, Phải `1,8 cm`).
- Font **Times New Roman** (cỡ nội dung mặc định `13 pt`, tùy chọn `--font-size 14`), mã Python dùng **Consolas**.
- Phân cấp rõ đề mục `I, II, III, IV, V`, khung ghi chú trích dẫn, bảng biểu tự căn tỷ lệ cột (`tblHeader` lặp tiêu đề trang, `cantSplit` chống vỡ hàng).
- Có Header (từ trang 2) và Footer kèm số trang động `Trang X / Y`.

### B. Xuất Kịch bản Slide sang PowerPoint (`.pptx`)

```bash
python scripts/document_generator/generate_pptx.py <duong_dan_Kich_ban.md> [duong_dan_ra.pptx]
```

**Ví dụ (Bài 16 Tin học 10):**

```bash
python scripts/document_generator/generate_pptx.py output/bai-16-tin-hoc-10/02_Kich_ban_PowerPoint.md output/bai-16-tin-hoc-10/Bai_16_Ngon_ngu_lap_trinh_va_Python.pptx
```

**Đặc điểm đầu ra PPTX:**
- Tỷ lệ màn ảnh rộng **16:9**, font **Segoe UI** (tiếng Việt rõ nét) và **Consolas** (mã Python trong khung code editor/IDLE Shell).
- Tự động phân tích nội dung từng slide để chọn **9 bố cục khác nhau**: `cover`, `cards_3col`, `process_flow`, `quiz_cards`, `grid_2x2`, `table_compare`, `code_focus`, `split_practice`, `summary_dark`.
- Tự động nhúng **Ghi chú thuyết trình (Speaker Notes)** vào từng slide (không làm lộ đáp án trắc nghiệm trên mặt slide).

## 4. Tích hợp với Agent Skills

- `lesson-planner` tự động gọi `scripts/document_generator/generate_docx.py` sau khi lưu KHBD Markdown (khi người dùng yêu cầu tạo tệp bài dạy).
- `slide-designer` tự động gọi `scripts/document_generator/generate_pptx.py` sau khi lưu kịch bản PowerPoint Markdown (khi người dùng yêu cầu tạo bộ slide).
