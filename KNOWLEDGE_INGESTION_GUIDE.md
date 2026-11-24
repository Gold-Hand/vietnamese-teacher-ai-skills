# HƯỚNG DẪN NẠP VÀ PHÂN TÍCH TÀI LIỆU KNOWLEDGE BASE (V2.0)

Tài liệu này quy định quy trình chuẩn để tiếp nhận, phân loại, phân tích và đăng ký tài liệu thực tế vào **Vietnamese Teacher AI Skills Knowledge Base** mà **tuyệt đối không làm thay đổi nội dung tài liệu gốc**.

---

## 1. Nguyên tắc bất biến khi nạp tài liệu

1. **Bất biến tài liệu gốc (Immutable Source):** Tệp gốc (`.docx`, `.pdf`, `.pptx`, `.xlsx`, `.md`) do giáo viên cung cấp được lưu nguyên vẹn, không tự ý biên tập hay ghi đè.
2. **Không tạo dữ liệu giả:** Nếu một nhóm tri thức chưa có tài liệu thật, để trống và ghi rõ chưa có dữ liệu; tuyệt đối không tự sáng tác văn bản pháp lý, trích dẫn SGK hay KHBD giả.
3. **Phân tách rõ loại nguồn & mức độ tin cậy:**
   - `01_legal/` → **T1 – Pháp lý chính thức**
   - `02_curriculum/` → **T2 – Chương trình / SGK chuẩn**
   - `04_assessment/` → **T3 – Chuyên môn đánh giá**
   - `03_practical-khbd/` → **T4 – KHBD thực chiến tham khảo** (tách hai kho độc lập `01_TIN_HOC/` và `02_TRI_TUE_NHAN_TAO_AI/`, kèm vùng chờ `_staging/`, quản lý qua `KHBD_INDEX.md`).
   - `05_teaching-materials/` → **T4 – Học liệu tham khảo**.
   - `06_reference-analysis/` → **T5 – Bản phân tích Markdown dẫn xuất** (luôn gắn liên kết tới tệp gốc).
4. **Không suy diễn pháp lý từ KHBD mẫu:** Mọi kết luận về quy định bắt buộc, biểu mẫu hành chính hay mã chỉ báo năng lực số chỉ được phép rút ra từ tài liệu trong `01_legal/` hoặc `02_curriculum/`.
5. **Xác nhận bắt buộc trước khi vào kho chính thức:** Mọi tài liệu mới tiếp nhận chưa được giáo viên xác nhận môn học, loại tài liệu và đường dẫn lưu chỉ được giữ ở vùng chờ (`knowledge-base/03_practical-khbd/_staging/`), **tuyệt đối không tự động đưa vào kho chính thức**.

---

## 2. Quy trình tiếp nhận & phân loại KHBD (Tin học vs Trí tuệ nhân tạo – AI)

Khi tiếp nhận bất kỳ tài liệu KHBD, bài thực hành, dự án hoặc best practice nào:

1. **Bước A – Lưu tạm bất biến tại `_staging/`:** Đặt bản sao nguyên gốc vào `knowledge-base/03_practical-khbd/_staging/` (chế độ chỉ đọc; **không tự sửa tài liệu gốc**).
2. **Bước B – Tự nhận diện môn học (Tin học hay Trí tuệ nhân tạo – AI):**
   - **Nhận diện `01_TIN_HOC`:** Có bộ SGK Tin học GDPT 2018 (Kết nối tri thức, Cánh diều, Chân trời sáng tạo), chủ đề/YCCĐ Tin học (thuật toán, Python/C++, CSDL/SQL, mạng máy tính, thiết kế web, an toàn thông tin, ứng dụng tin học, STEM Tin học).
   - **Nhận diện `02_TRI_TUE_NHAN_TAO_AI`:** Chuyên đề/chương trình giáo dục AI, nguyên lý AI/học máy, dữ liệu & thiên lệch, AI tạo sinh, kỹ thuật prompt, thực nghiệm/dự án AI, ứng dụng AI trong học tập, đạo đức và trách nhiệm AI.
   - **Trường hợp giao thoa / liên môn:** Báo rõ cả hai thành phần (Tin học và AI), nêu lý do phân loại chính và hỏi người dùng xác nhận kho lưu chính (kèm thẻ liên môn trong `KHBD_INDEX.md`).
3. **Bước C – Đề xuất vị trí lưu cụ thể:**
   - Kho Tin học: `knowledge-base/03_practical-khbd/01_TIN_HOC/khoi-{10|11|12}/{bo-sach|chu-de|bai-thuc-hanh|du-an-stem|khbd-mau-thuc-chien}/` hoặc `best-practices/`.
   - Kho AI: `knowledge-base/03_practical-khbd/02_TRI_TUE_NHAN_TAO_AI/khoi-{10|11|12}/{chu-de-ai|thuc-hanh-ai|du-an-ai|ung-dung-ai|dao-duc-va-trach-nhiem-ai|khbd-mau-thuc-chien}/` hoặc `best-practices/`.
4. **Bước D – Trích xuất cấu trúc KHBD & Phân tích phương pháp dạy học:**
   - Trích xuất cấu trúc KHBD (bố cục mục La Mã, tiến trình pha dạy học, phân bổ thời lượng, thiết bị/học liệu, phương án dự phòng).
   - Phân tích phương pháp và hoạt động dạy học (cách chuyển giao nhiệm vụ, hoạt động GV–HS, kỹ thuật phân hóa, sản phẩm học tập, công cụ đánh giá, kiểm tra sự phù hợp đặc thù Tin học vs AI).
   - Xuất bản phân tích sơ bộ vào `knowledge-base/06_reference-analysis/<ma_tai_lieu>_analysis.md` (trỏ rõ về tệp gốc).
5. **Bước E – Cổng xác nhận (Human-in-the-Loop Gate):**
   - Trình người dùng phiếu đề xuất gồm: *Môn học nhận diện, Khối lớp, Bộ sách/Chương trình, Loại tài liệu, Vị trí lưu đề xuất, ID tài liệu dự kiến và tóm tắt phân tích*.
   - **Chỉ sau khi người dùng xác nhận**, mới di chuyển tệp gốc từ `_staging/` vào đúng kho chính thức (`01_TIN_HOC/` hoặc `02_TRI_TUE_NHAN_TAO_AI/`), ghi nhận vào `KHBD_INDEX.md` (11 cột metadata) và đồng bộ lên `KNOWLEDGE_INDEX.md` (12 cột metadata).

---

## 3. Quy trình Pipeline phân tích 10 bước (Toàn hệ thống Knowledge Base)

Mỗi đợt tiếp nhận tài liệu mới đều đi qua đúng 10 bước sau:

1. **Tiếp nhận tệp nguồn:** Kiểm tra định dạng (`.docx`, `.pdf`, `.pptx`, `.xlsx`, `.md`), mã hóa UTF-8, đặt tên không dấu dễ truy vết và lưu vào đúng thư mục đích trong `knowledge-base/01..05`.
2. **Trích xuất nội dung:**
   - `.docx`: Trích xuất tiêu đề, đoạn văn, bảng biểu, ghi chú bằng `python-docx`.
   - `.pptx`: Trích xuất tiêu đề slide, nội dung khung chữ, bảng và Speaker Notes bằng `python-pptx`.
   - `.pdf`: Trích xuất văn bản theo từng trang bằng `pypdf` / `pdfplumber` *(lưu ý nếu là PDF scan ảnh thì ghi nhận cần OCR)*.
   - `.xlsx`: Trích xuất từng sheet, ma trận, bảng điểm bằng `openpyxl`.
   - `.md`: Đọc trực tiếp bằng parser Markdown của hệ thống.
3. **Phân tích cấu trúc tài liệu:** Nhận diện đề mục lớn, bảng biểu, danh sách hoạt động, mục tiêu, phụ lục.
4. **Nhận diện bản chất nội dung:** Gắn nhãn chính xác đoạn/mục nào là *quy định pháp lý*, *yêu cầu cần đạt chuyên môn* hay *kinh nghiệm thực chiến*.
5. **Trích xuất phương pháp dạy học:** Kỹ thuật tổ chức lớp, khởi động, trực quan hóa, phân hóa đối tượng, dự phòng thiết bị.
6. **Trích xuất cấu trúc KHBD (nếu là KHBD):** Bố cục mục La Mã, phân bổ thời lượng theo pha và theo tiết.
7. **Trích xuất hoạt động giáo viên & học sinh:** 4 bước tổ chức (chuyển giao – thực hiện – báo cáo/thảo luận – kết luận), câu hỏi gợi mở và dự kiến phản hồi của HS.
8. **Trích xuất sản phẩm học tập & đánh giá:** Phiếu học tập, mã nguồn thực hành, câu hỏi kiểm tra, rubric/tiêu chí chấm.
9. **Sinh tài liệu tri thức Markdown** trong `knowledge-base/06_reference-analysis/<ma_tai_lieu>_analysis.md` (giữ nguyên thông tin nguồn gốc, không viết lại làm sai lệch nội dung gốc).
10. **Cập nhật `KNOWLEDGE_INDEX.md` & `KHBD_INDEX.md`** (với KHBD thực chiến) sau khi được xác nhận, bảo đảm đầy đủ metadata và chạy kiểm thử truy xuất + không hồi quy V1.2 sau mỗi đợt nạp.

---

## 4. Quy ước đặt tên tệp đề xuất

```text
<loai>_<mon>_<lop>_<bo-sach-hoac-co-quan>_<ten-ngan-khong-dau>.<ext>
```

**Ví dụ minh họa quy ước đặt tên:**
- `knowledge-base/01_legal/legal_bgddt_cv5512_2020_khbd_thcs_thpt.pdf`
- `knowledge-base/02_curriculum/curr_tinhoc_10_kntt_ppct_namhoc.xlsx`
- `knowledge-base/03_practical-khbd/01_TIN_HOC/khoi-10/khbd-mau-thuc-chien/khbd_tinhoc_10_kntt_bai16_thuc_chien.docx`
- `knowledge-base/03_practical-khbd/02_TRI_TUE_NHAN_TAO_AI/khoi-10/thuc-hanh-ai/khbd_ai_10_thpt_kiem_chung_dau_ra_ai.docx`
- `knowledge-base/06_reference-analysis/khbd_tinhoc_10_kntt_bai16_thuc_chien_analysis.md`

---

## 5. Cách gửi tài liệu theo từng đợt để tích hợp

Khi sẵn sàng cung cấp tài liệu thực chiến, người dùng chỉ cần gửi tệp hoặc đặt vào vùng chờ `knowledge-base/03_practical-khbd/_staging/` (với KHBD) hoặc nhóm thư mục tương ứng kèm 4 thông tin ngắn:
1. **Nhóm tài liệu & Môn/Kho dự kiến** (`01_legal` / `02_curriculum` / `03_practical-khbd/01_TIN_HOC` / `03_practical-khbd/02_TRI_TUE_NHAN_TAO_AI` / `04_assessment` / `05_teaching-materials`).
2. **Nguồn cung cấp & tình trạng pháp lý** (văn bản chính thức của cơ quan nào, hay tài liệu cá nhân/tổ chuyên môn).
3. **Phạm vi áp dụng** (môn, cấp học, lớp, bộ sách hoặc chương trình AI, chủ đề).
4. **Xác nhận đưa vào kho chính thức** sau khi hệ thống tự nhận diện, phân tích và đề xuất vị trí lưu.
