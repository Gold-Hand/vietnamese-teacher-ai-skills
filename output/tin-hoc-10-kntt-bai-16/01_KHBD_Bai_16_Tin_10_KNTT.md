# KẾ HOẠCH BÀI DẠY – TIN HỌC LỚP 10 (BÀI 16)

> **Lưu ý về căn cứ, tài liệu nguồn và tính pháp lý:**
> - Kế hoạch bài dạy được thiết kế theo khung mẫu `references/lesson-plan-template.md`, nguyên tắc đối chiếu tại `references/vietnam-education-guidance.md` và cấu trúc tham khảo của **Công văn 5512/BGDĐT-GDTrH** dành cho cấp THPT. Đây là mẫu tham khảo phổ biến, **không khẳng định là quy định bắt buộc duy nhất** cho mọi cơ sở giáo dục; giáo viên đối chiếu biểu mẫu hiện hành của Sở GDĐT và nhà trường trước khi ban hành.
> - **Minh bạch nguồn tài liệu:** Repository hiện không lưu trữ bản PDF/toàn văn SGK *Tin học 10 – Kết nối tri thức với cuộc sống* (Bài 16), không có tệp Phân phối chương trình (PPCT) của trường và không có bảng mã Khung năng lực số chính thức. Vì vậy giáo án không tự bịa số trang hay trích dẫn nguyên văn SGK, không tự tạo mã năng lực số, và tách bạch rõ phần **Nội dung cốt lõi bám khung Bài 16**, **Nội dung mở rộng tham khảo** và **Nội dung thực hành**.

---

## THÔNG TIN BÀI HỌC

- **Trường:** ............................................................
- **Tổ/nhóm chuyên môn:** Tin học
- **Giáo viên:** .......................................................
- **Môn học:** Tin học – **Lớp:** 10
- **Bộ sách giáo khoa:** Kết nối tri thức với cuộc sống *(đối chiếu bản in SGK gốc khi lên lớp)*
- **Chủ đề 5:** Giải quyết vấn đề với sự trợ giúp của máy tính
- **Tên bài học:** Bài 16 – Ngôn ngữ lập trình bậc cao và Python
- **Thời lượng:** 02 tiết (90 phút = Tiết 1: 45 phút + Tiết 2: 45 phút)
- **Đối tượng & Điều kiện dạy học (giả định):** Lớp 10 đại trà (36–40 HS), phòng thực hành 20 máy tính (2 HS/máy) cài sẵn Python 3 (IDLE), có máy chiếu; có sẵn phương án dự phòng nếu thiếu máy hoặc mất Internet.
- **Ngày thực hiện:** ................................................

---

## PHÂN TÍCH NỘI DUNG & RANH GIỚI BÀI 16 (GDPT 2018 – KNTT)

### 1. Phân tách nội dung cốt lõi, mở rộng và thực hành

| TT | Nội dung bài học | Mức độ trong bài | Trọng tâm cần hình thành cho học sinh |
|---:|---|---|---|
| 1 | Khái niệm ngôn ngữ lập trình | **Cốt lõi bám SGK** | Ngôn ngữ dùng để viết chương trình (dãy câu lệnh) hướng dẫn máy tính thực hiện thuật toán giải bài toán. |
| 2 | Ngôn ngữ máy, hợp ngữ và ngôn ngữ lập trình bậc cao | **Cốt lõi** *(ngôn ngữ máy vs bậc cao)* + **Mở rộng** *(hợp ngữ)* | Máy tính chỉ hiểu trực tiếp ngôn ngữ máy (`0`, `1`); hợp ngữ dùng ký hiệu gợi nhớ (`MOV`, `ADD`) nhưng phụ thuộc phần cứng; NNLT bậc cao gần ngôn ngữ tự nhiên/toán học, độc lập loại máy, dễ viết và dễ sửa lỗi. |
| 3 | Đặc điểm và ưu điểm của Python | **Cốt lõi bám SGK** | Cú pháp ngắn gọn, dễ đọc, gần tiếng Anh tự nhiên; miễn phí, mã nguồn mở, đa nền tảng; hệ sinh thái thư viện phong phú cho AI, khoa học dữ liệu, web, tự động hóa. |
| 4 | Chương trình dịch | **Cốt lõi** *(vai trò chuyển đổi)* + **Mở rộng** *(thông dịch vs biên dịch)* | Chuyển chương trình từ NNLT bậc cao sang ngôn ngữ máy. Python dùng trình thông dịch (dịch & chạy từng lệnh), khác với C/C++ thường dùng trình biên dịch. |
| 5 | Môi trường lập trình Python (IDLE) | **Cốt lõi + Thực hành** | Làm quen phần mềm IDLE cài sẵn cùng Python 3 (mở rộng tham khảo: Thonny, VS Code). |
| 6 | Chế độ gõ lệnh trực tiếp (Interactive Mode) | **Cốt lõi + Thực hành** | Cửa sổ Python Shell có dấu nhắc `>>>`; gõ từng lệnh/biểu thức, nhấn `Enter` chạy ngay; không lưu thành tệp chương trình. |
| 7 | Chế độ soạn thảo chương trình (Script Mode) | **Cốt lõi + Thực hành** | Mở `File → New File` (không có `>>>`), viết nhiều lệnh, lưu tệp `.py` (`Ctrl + S`) và chạy cả tệp (`Run → Run Module` / `F5`). |
| 8 | Tạo, lưu và thực hiện chương trình Python đầu tiên | **Thực hành bắt buộc** | Viết, lưu và chạy tệp `.py` chỉ dùng `print(...)` và các phép toán số học (`+`, `-`, `*`, `/`, ngoặc đơn); nhận diện và sửa lỗi cú pháp cơ bản (`SyntaxError`). |

### 2. Ranh giới nghiêm ngặt không lấn sang Bài 17
- **Không đưa kiến thức Bài 17 (*Biến và lệnh gán*) và Bài 18 (*Các lệnh vào ra đơn giản*) vào làm nội dung chính Bài 16:** Toàn bộ ví dụ, phiếu thực hành và câu hỏi đánh giá chỉ sử dụng `print(...)` và biểu thức số học trực tiếp; **không dùng biến, lệnh gán `=`, `input()`, `if`, `for`, `while`, `def`**.
- **Hiểu lầm phổ biến cần gỡ sớm:** Nhầm gõ lệnh ở Shell (`>>>`) là đã lưu bài; gõ nhầm ký tự `>>>` vào Script Mode; viết hoa `Print`; quên đóng cặp dấu nháy `"..."` hoặc dấu ngoặc `(...)`; quên lưu tệp trước khi nhấn `F5`.

---

## I. MỤC TIÊU

### 1. Kiến thức
Sau bài học, học sinh đạt được 4 mục tiêu trọng tâm (đồng bộ mã `M1–M4` với Slide, Phiếu học tập và Đánh giá):
- **M1:** Nêu được khái niệm ngôn ngữ lập trình; phân biệt được ngôn ngữ máy, hợp ngữ và ngôn ngữ lập trình bậc cao; giải thích được vai trò của chương trình dịch.
- **M2:** Trình bày được đặc điểm, ưu điểm nổi bật và một số lĩnh vực ứng dụng thực tế của ngôn ngữ lập trình Python.
- **M3:** Phân biệt được chế độ gõ lệnh trực tiếp (*Interactive Mode*, dấu nhắc `>>>`) và chế độ soạn thảo chương trình (*Script Mode*, tệp `.py`) trong môi trường IDLE.
- **M4:** Sử dụng được IDLE để gõ lệnh trực tiếp và thực hiện đúng quy trình tạo, lưu tệp `.py`, chạy chương trình Python đầu tiên dùng `print()` cùng phép toán số học; nhận diện và sửa được lỗi cú pháp cơ bản.

### 2. Năng lực
- **Năng lực Tin học:**
  - *Sử dụng và quản lý các phương tiện CNTT và truyền thông:* Khởi động và thao tác thành thạo trên IDLE, phân biệt đúng 2 chế độ làm việc và lưu trữ tệp `.py` đúng quy ước thư mục/tên tệp.
  - *Giải quyết vấn đề với sự trợ giúp của máy tính:* Diễn đạt bài toán hiển thị thông tin và tính toán số học đơn giản bằng câu lệnh Python hợp lệ; đọc thông báo lỗi cú pháp cơ bản để tự sửa chương trình.
- **Năng lực chung:**
  - *Tự chủ và tự học:* Chủ động đối chiếu thông báo lỗi của IDLE với cú pháp chuẩn để tự khắc phục; lựa chọn mức nhiệm vụ cơ bản/nâng cao phù hợp.
  - *Giao tiếp và hợp tác:* Trao đổi cặp đôi/nhóm 4 khi phân tích 3 mức ngôn ngữ và đổi vai hợp tác trên cùng một máy tính khi thực hành.

### 3. Phẩm chất
- **Chăm chỉ, cẩn thận:** Rèn tác phong viết câu lệnh chính xác từng ký tự (phân biệt chữ hoa/thường, đóng mở ngoặc/nháy) và lưu tệp gọn gàng.
- **Trung thực, trách nhiệm:** Tự tay thực hành, trung thực ghi nhận lỗi để rút kinh nghiệm và tuân thủ nội quy an toàn phòng máy tính.

---

## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU

### 1. Giáo viên
- Máy tính GV kết nối máy chiếu/TV lớp học, cài sẵn **Python 3 (IDLE)** chạy hoàn toàn ngoại tuyến.
- Bộ trình chiếu PowerPoint `Bai_16_Ngon_ngu_lap_trinh_bac_cao_va_Python.pptx` (18 slide, kèm `Speaker_Notes_Bai_16.md`).
- Tệp mã nguồn kiểm chứng `06_Ma_Nguon_Python_Bai_16.py`.
- Học liệu in sẵn phát cho học sinh (`Phieu_Hoc_Tap_Va_Thuc_Hanh_Bai_16.docx`):
  - **Phiếu học tập số 1** (Tiết 1): 3 thẻ lệnh Robot + Bảng so sánh 3 mức ngôn ngữ + Khám phá Python.
  - **Phiếu thực hành số 2** (Tiết 2): Hướng dẫn IDLE từng bước (Cơ bản – Nâng cao), bài tập Săn lỗi cú pháp và khung mô phỏng trên giấy (dùng khi dự phòng).
- Thẻ giơ tay A, B, C, D (hoặc quy ước giơ 1–4 ngón tay) kiểm tra nhanh không phụ thuộc Internet.

### 2. Học sinh
- Sách giáo khoa *Tin học 10 – Kết nối tri thức với cuộc sống* (Bài 16), vở ghi, bút viết.
- Máy tính phòng Tin học (2 HS/máy) cài sẵn **Python 3 (IDLE)**.

### 3. Phương án dự phòng khi thiếu máy tính hoặc mất Internet
- **Mất kết nối Internet:** Không ảnh hưởng đến tiết học vì IDLE, bài trình chiếu và mã mẫu chạy **100% ngoại tuyến**.
- **Thiếu máy tính / một số máy lỗi IDLE:** Ghép 3 HS/máy, phân 3 vai luân phiên (*Người gõ lệnh – Người rà cú pháp – Người ghi kết quả*), đổi vai sau 7 phút.
- **Mất điện / học tại phòng lý thuyết không có máy:** Dùng bảng phấn minh họa cửa sổ Shell (`>>>`) và Script (`.py`); HS làm trọn vẹn **Phần dự phòng trên giấy** của Phiếu thực hành số 2 (viết mã, khoanh tròn 3 lỗi `SyntaxError`, tự tính tay kết quả dự kiến); GV dùng 1 laptop chạy pin (hoặc Pydroid 3 offline) trình diễn kiểm chứng kết quả cho các nhóm.

---

## III. TIẾN TRÌNH DẠY HỌC (TỔNG: 2 TIẾT – 90 PHÚT)

### Bảng tổng quan tiến trình 2 tiết (90 phút)

| Tiết | Hoạt động | Mục tiêu | Nội dung trọng tâm | Hình thức / Phương pháp | Thời lượng |
|---:|---|---|---|---|---:|
| **Tiết 1**<br>*(45p)* | **HĐ 1: Khởi động** | Dẫn nhập M1 | Tình huống *"Ra lệnh cho Robot tính `5 + 3`"* (3 thẻ ngôn ngữ) | Giải mã nhóm cặp đôi | 8 phút |
| | **HĐ 2.1: Hình thành KT** | M1 | NNLT, Ngôn ngữ máy – Hợp ngữ – NNLT bậc cao & Chương trình dịch | Đọc SGK + Phiếu học tập số 1 (Phần 1) | 14 phút |
| | **HĐ 2.2: Hình thành KT** | M2 | Khám phá đặc điểm, ưu điểm & ứng dụng thực tế của Python | Thảo luận nhóm 4 + Phiếu số 1 (Phần 2) | 13 phút |
| | **HĐ 3.1: Luyện tập Tiết 1** | Củng cố M1, M2 | Kiểm tra nhanh 4 câu trắc nghiệm (Slide 6 & Slide 9) | Giơ thẻ A–D đồng loạt toàn lớp | 10 phút |
| **Tiết 2**<br>*(45p)* | **HĐ 2.3: Hình thành KT** | M3 | Môi trường IDLE: Interactive Mode (`>>>`) vs Script Mode (`.py`) | GV demo trực quan + HS điền bảng so sánh | 12 phút |
| | **HĐ 3.2: Thực hành trên máy** | M3, M4 | Chạy lệnh trực tiếp; tạo–lưu–chạy `.py` đầu tiên; Săn lỗi cú pháp | Thực hành 2 HS/máy (Phiếu số 2, có phân hóa) | 20 phút |
| | **HĐ 4: Vận dụng & Tổng kết** | M4 (M1–M4) | Bài toán *"Dự toán trang trí lớp 10"* + Chốt bài & mở sang Bài 17 | Thực hành vận dụng + tổng kết 4 ý vàng | 13 phút |
| **Tổng** | **7 chặng (4 pha CV 5512)** | **M1 – M4** | **Chuẩn phạm vi Bài 16 (không lấn Bài 17)** | **Tương tác – Phân hóa – Có dự phòng** | **90 phút** |

---

### TIẾT 1 (45 PHÚT): NGÔN NGỮ LẬP TRÌNH BẬC CAO, CHƯƠNG TRÌNH DỊCH VÀ PYTHON

#### Hoạt động 1: Khởi động – "Ra lệnh cho Robot tính `5 + 3`" (8 phút)
- **a) Mục tiêu:** Tạo động cơ học tập, giúp HS tự nhận ra sự khác biệt trực quan giữa ngôn ngữ máy, hợp ngữ và NNLT bậc cao trước khi tiếp cận thuật ngữ.
- **b) Nội dung:** HS quan sát 3 thẻ lệnh trên Slide 2 (và Phiếu số 1) cùng thực hiện phép tính `5 + 3`:
  - **Thẻ A (Ngôn ngữ máy):** `10110000 00000101` / `00000100 00000011` / `11100110 00000001`
  - **Thẻ B (Hợp ngữ):** `MOV AL, 5` / `ADD AL, 3` / `OUT 1, AL`
  - **Thẻ C (Python):** `print(5 + 3)`
  - *Câu hỏi gợi mở:* (1) Thẻ nào dễ hiểu nhất dù chưa học lập trình? (2) Nếu máy tính chỉ hiểu Thẻ A toàn `0` và `1`, còn con người viết Thẻ C thì cần thêm gì ở giữa?
- **c) Sản phẩm dự kiến:** Câu trả lời của HS nhận diện Thẻ C giống tiếng Anh/toán học dễ đọc nhất, Thẻ A khó đọc nhất nhưng máy hiểu trực tiếp, và dự đoán cần một "bộ phận phiên dịch" ở giữa.
- **d) Tổ chức thực hiện (4 bước CV 5512):**
  1. *Chuyển giao (1,5 phút):* GV chiếu Slide 1–2, giới thiệu tình huống Robot và phát Phiếu học tập số 1.
  2. *Thực hiện (2 phút):* HS trao đổi cặp đôi theo bàn, chọn thẻ dễ hiểu và lý giải ngắn.
  3. *Báo cáo, thảo luận (2,5 phút):* Mời 2 HS trả lời; dự kiến HS nêu đúng Thẻ C dễ nhất và cần "người phiên dịch" để máy hiểu Thẻ C.
  4. *Kết luận, nhận định (2 phút):* GV chốt: Thẻ A, B, C tương ứng 3 cấp độ ngôn ngữ lập trình, và Thẻ C chính là **Python** → dẫn vào Bài 16.

#### Hoạt động 2.1: Hình thành kiến thức – Ngôn ngữ lập trình, 3 mức ngôn ngữ & Chương trình dịch (14 phút)
- **a) Mục tiêu:** Đạt **M1** (khái niệm NNLT, phân biệt 3 mức ngôn ngữ, vai trò chương trình dịch).
- **b) Nội dung:** HS đọc SGK kết hợp Slide 3–5, hoàn thành **Phần 1 Phiếu học tập số 1**:
  - *(Cơ bản – cốt lõi SGK)* Nêu khái niệm ngôn ngữ lập trình; hoàn thành bảng so sánh Ngôn ngữ máy – Hợp ngữ *(mở rộng)* – NNLT bậc cao theo 3 tiêu chí (*Ký hiệu lệnh, Mức độ dễ học, Máy tính hiểu trực tiếp?*), và giải thích vai trò **chương trình dịch**.
  - *(Mở rộng cho GV & HS khá)* Phân biệt ngắn **Thông dịch (Python)** vs **Biên dịch (C/C++)**; trả lời câu hỏi: *"Vì sao mã nguồn Python viết trên Windows mang sang macOS/Linux vẫn chạy được?"*
- **c) Sản phẩm dự kiến:** Bảng so sánh hoàn chỉnh trên Phiếu số 1; sơ đồ luồng `Mã nguồn bậc cao → [Chương trình dịch] → Ngôn ngữ máy → Kết quả`; câu trả lời mở rộng nêu được tính độc lập phần cứng nhờ trình thông dịch tương thích từng hệ điều hành.
- **d) Tổ chức thực hiện (4 bước CV 5512):**
  1. *Chuyển giao (2 phút):* GV hướng dẫn HS đọc SGK và hoàn thành Phần 1 Phiếu số 1 trong 5 phút (cặp xong sớm làm câu nâng cao).
  2. *Thực hiện (5 phút):* HS thảo luận cặp đôi. *Hỗ trợ HS yếu:* Sử dụng kho từ khóa gợi ý in sẵn trên Phiếu số 1 để ghép vào bảng; GV trực tiếp gỡ vướng tại bàn.
  3. *Báo cáo, thảo luận (4 phút):* Mời 1 cặp đọc bảng so sánh, 1 cặp khác bổ sung; mời 1 HS khá giải đáp câu tính đa nền tảng.
  4. *Kết luận, nhận định (3 phút):* GV chốt trên Slide 4–5, tách rõ kiến thức cốt lõi cần ghi vở với phần mở rộng (*hợp ngữ, thông dịch vs biên dịch*).

#### Hoạt động 2.2: Hình thành kiến thức – Khám phá ngôn ngữ lập trình Python (13 phút)
- **a) Mục tiêu:** Đạt **M2** (đặc điểm, ưu điểm và lĩnh vực ứng dụng của Python).
- **b) Nội dung:** Nhóm 4 HS quan sát đoạn so sánh in `"Xin chao lop 10!"` giữa C++ (5 dòng minh họa trực quan) và Python (1 dòng `print("Xin chao lop 10!")`) trên Slide 7–8, hoàn thành **Phần 2 Phiếu học tập số 1**:
  - *(Cơ bản)* Nêu 4 ưu điểm nổi bật của Python và kể tên ít nhất 3 lĩnh vực ứng dụng thực tế.
  - *(Nâng cao)* Python có giới hạn nào khi so với ngôn ngữ biên dịch như C/C++ không?
- **c) Sản phẩm dự kiến:** 4 ưu điểm (ngắn gọn–dễ đọc, gần ngôn ngữ tự nhiên, mã nguồn mở miễn phí–đa nền tảng, thư viện phong phú); 4 lĩnh vực ứng dụng (AI & học máy, khoa học dữ liệu, phát triển web, tự động hóa/giáo dục); ý nâng cao (tốc độ thuần chậm hơn C/C++ do là ngôn ngữ thông dịch).
- **d) Tổ chức thực hiện (4 bước CV 5512):**
  1. *Chuyển giao (1,5 phút):* GV chiếu Slide 7–8, chia nhóm 4 HS (2 bàn liền kề), giao 4,5 phút thảo luận.
  2. *Thực hiện (4,5 phút):* Nhóm ghi ý vào Phần 2 Phiếu số 1. GV gợi mở bằng các sản phẩm thực tế quen thuộc (trợ lý AI, phân tích dữ liệu, web).
  3. *Báo cáo, thảo luận (4 phút):* Mời 2 nhóm trình bày ưu điểm và ứng dụng; 1 HS chia sẻ ý nâng cao để có góc nhìn khách quan.
  4. *Kết luận, nhận định (3 phút):* GV chốt 4 từ khóa về Python (*Ngắn gọn – Dễ học – Miễn phí/Đa nền tảng – Ứng dụng mạnh*).

#### Hoạt động 3.1: Luyện tập Tiết 1 – Kiểm tra nhanh M1 & M2 (10 phút)
- **a) Mục tiêu:** Củng cố M1, M2 ngay cuối Tiết 1.
- **b) Nội dung:** Trả lời nhanh 4 câu trắc nghiệm 4 phương án A, B, C, D trên Slide 6 (Câu 1–2 kiểm tra M1) và Slide 9 (Câu 3–4 kiểm tra M2) bằng hình thức giơ thẻ đồng loạt.
- **c) Sản phẩm dự kiến:** Phản hồi giơ thẻ của cả lớp khớp đáp án (`1-B, 2-C, 3-A, 4-B`) và lời giải thích ngắn lý do loại phương án sai.
- **d) Tổ chức thực hiện (4 bước CV 5512):**
  1. *Chuyển giao (1 phút):* Phổ biến khẩu lệnh "3–2–1 giơ thẻ!".
  2. *Thực hiện (4 phút):* Lần lượt chiếu 4 câu hỏi (1 phút/câu), cả lớp giơ thẻ đồng loạt.
  3. *Báo cáo, thảo luận (3 phút):* Gọi HS giải thích nhanh câu có nhiều ý kiến khác nhau.
  4. *Kết luận, nhận định (2 phút):* Tổng kết Tiết 1, giới thiệu Tiết 2 trực tiếp thực hành mở IDLE và chạy chương trình đầu tiên.

---

### TIẾT 2 (45 PHÚT): MÔI TRƯỜNG LẬP TRÌNH PYTHON & CHƯƠNG TRÌNH ĐẦU TIÊN

#### Hoạt động 2.3: Hình thành kiến thức – Môi trường IDLE & 2 chế độ làm việc (12 phút)
- **a) Mục tiêu:** Đạt **M3** (phân biệt Interactive Mode và Script Mode trong IDLE).
- **b) Nội dung:** GV thao tác trực tiếp trên **IDLE (Python 3)** chiếu màn hình lớn (Slide 10–12):
  - *Thao tác 1 (Interactive Mode – dấu nhắc `>>>`):* Gõ `15 + 25` → `40`; gõ `print("Chao mung den voi Python!")`. Đặt câu hỏi: *"Nếu tắt IDLE, các lệnh vừa gõ có lưu thành tệp không?"*
  - *Thao tác 2 (Script Mode – `File → New File`):* Viết 2 dòng lệnh `print(...)`, lưu tệp `bai_dau_tien.py` (`Ctrl + S`), nhấn `F5` chạy. GV cố tình gõ thử `>>> print(5)` trong Script Mode để HS thấy báo lỗi `SyntaxError`.
  - HS hoàn thành **Bảng so sánh 2 chế độ** trên Phiếu thực hành số 2:

| Tiêu chí | Chế độ gõ lệnh trực tiếp (Interactive Mode) | Chế độ soạn thảo (Script Mode) |
|---|---|---|
| Dấu hiệu nhận biết | Có dấu nhắc `>>>` (cửa sổ Shell) | Không có `>>>` (cửa sổ soạn thảo tệp) |
| Cách thực hiện | Gõ từng lệnh, nhấn `Enter` chạy ngay | Viết nhiều dòng, lưu `.py`, nhấn `F5` chạy cả tệp |
| Lưu trữ chương trình | Không lưu thành tệp để chạy lại | Lưu thành tệp `.py`, mở sửa và nộp bài được |
| Mục đích sử dụng | Thử lệnh nhanh, tính toán tức thời | Viết chương trình nhiều dòng, làm bài tập/dự án |

- **c) Sản phẩm dự kiến:** HS điền đủ bảng so sánh 4 tiêu chí trên Phiếu số 2 và nắm quy trình 4 bước tạo–lưu–chạy tệp `.py`.
- **d) Tổ chức thực hiện (4 bước CV 5512):**
  1. *Chuyển giao (1,5 phút):* Yêu cầu HS quan sát kỹ thao tác mẫu của GV và điền bảng so sánh trên Phiếu số 2.
  2. *Thực hiện (4,5 phút):* GV demo trực tiếp cả 2 chế độ trên IDLE, xen kẽ câu hỏi ngắn; HS quan sát và ghi nhận.
  3. *Báo cáo, thảo luận (3 phút):* Gọi 2 HS phân biệt 2 chế độ và nêu tác hại khi gõ `>>>` vào Script Mode.
  4. *Kết luận, nhận định (3 phút):* GV chốt bảng so sánh (Slide 12) và nhấn mạnh quy tắc đặt tên tệp `.py` không dấu, không khoảng trắng.

#### Hoạt động 3.2: Luyện tập – Thực hành chạy chương trình đầu tiên & Săn lỗi cú pháp (20 phút)
- **a) Mục tiêu:** Đạt **M3, M4** (kiểm tra nhanh M3; tạo, lưu, chạy chương trình Python đầu tiên; tự sửa lỗi cú pháp cơ bản).
- **b) Nội dung:** Thực hành 2 HS/máy theo **Phiếu thực hành số 2** (Slide 13–16), đổi vai gõ phím sau 10 phút:
  - *Kiểm tra nhanh M3 & Quy trình 4 bước (4 phút – Slide 13–14):* Trả lời 2 câu TN (Câu 5–6) và chốt 4 bước `New File → Viết lệnh → Save (.py) → F5`.
  - *Nhiệm vụ Cơ bản (12 phút – Bắt buộc, có hỗ trợ HS yếu):*
    1. Gõ ở Shell (`>>>`): `2026 - 2010`, `(12 + 8) * 5 / 2`, `print("Toi dang hoc Python o lop 10")`.
    2. Tạo tệp `bai16_th1.py` trong Script Mode in: tên nhóm, lớp và tính chu vi, diện tích hình chữ nhật `12 × 5`:
       ```python
       print("Nhom thuc hanh: Minh - Lan")
       print("Lop: 10A1 - Mon: Tin hoc")
       print("Chu vi:", (12 + 5) * 2, "| Dien tich:", 12 * 5)
       ```
    3. *Săn 3 lỗi cú pháp:* Sửa `Print("Xin chao")`, `print("Tin hoc 10)` và `print(10 + 5 * 2` cho chạy đúng.
  - *Nhiệm vụ Nâng cao (4 phút / HS xong sớm – đúng phạm vi Bài 16, không dùng biến):*
    - Tạo `bai16_nangcao.py` dùng `print()` vẽ khung hóa đơn 3 món đồ dùng học tập (`4 × 12000`, `3 × 5000`, `1 × 18000` → tổng `81000`); thử chạy `print(10 / 0)` để phân biệt sơ lược `SyntaxError` với lỗi khi chạy `ZeroDivisionError`.
- **c) Sản phẩm dự kiến:** Tệp `bai16_th1.py` chạy ra `Chu vi: 34 | Dien tich: 60`; sửa đúng 3 lỗi cú pháp; cặp làm nâng cao xuất khung hóa đơn với tổng `81000`.
- **d) Tổ chức thực hiện (4 bước CV 5512):**
  1. *Chuyển giao (2 phút):* Giao Phiếu số 2, nhắc quy tắc lưu bài (`D:\Tin10\Bai16\...`) và đổi vai cặp đôi.
  2. *Thực hiện (13 phút):* HS thực hành trên IDLE. *Hỗ trợ HS yếu:* Phiếu số 2 có dòng mẫu đánh dấu sẵn vị trí dấu `""` và `()`; GV hỗ trợ trực tiếp lỗi bộ gõ Unikey và mở `New File`. *Thử thách HS khá giỏi:* Làm `bai16_nangcao.py` và hỗ trợ bạn bàn bên rà lỗi.
  3. *Báo cáo, thảo luận (3 phút):* Chiếu 1 bài cơ bản và 1 bài nâng cao; HS chia sẻ 1 lỗi thực tế vừa tự sửa được.
  4. *Kết luận, nhận định (2 phút):* GV tổng hợp 4 lỗi phổ biến của cả lớp (chữ hoa `Print`, thiếu nháy/ngoặc, gõ thừa `>>>`, quên lưu).

#### Hoạt động 4: Vận dụng & Tổng kết (13 phút)
- **a) Mục tiêu:** Vận dụng tổng hợp `print()` và biểu thức số học giải bài toán thực tế của lớp 10; hệ thống hóa Bài 16 và kết nối sang Bài 17.
- **b) Nội dung (Slide 17–18):**
  - *Bài toán Vận dụng (`bai16_vandung.py`):* Dự toán trang trí lớp 10 gồm `2` cuộn giấy màu (`25000`đ/cuộn), `5` cây bút dạ (`8000`đ/cây), `1` cuộn băng keo (`15000`đ).
    - *(Cơ bản)* In chi phí từng khoản, **Tổng chi phí** và **Số tiền mỗi tổ góp** (4 tổ) bằng biểu thức trực tiếp trong `print()`.
    - *(Nâng cao)* Tính thêm **Số tiền còn dư** nếu quỹ lớp có `150000`đ và đóng khung bảng bằng ký tự.
  - *Tổng kết & Mở sang Bài 17:* Chốt 4 từ khóa vàng (M1–M4) và đặt câu hỏi: *"Ở bài vừa rồi ta phải gõ lặp lại biểu thức `2*25000 + 5*8000 + 15000` nhiều lần. Muốn đặt tên ngắn lưu kết quả để dùng lại thì làm thế nào?"* → Dặn đọc trước **Bài 17: Biến và lệnh gán**.
- **c) Sản phẩm dự kiến:** Tệp `bai16_vandung.py` chạy ra đúng: Tổng `105000` đồng, Mỗi tổ `26250.0` đồng (Nâng cao: Còn dư `45000` đồng).
- **d) Tổ chức thực hiện (4 bước CV 5512):**
  1. *Chuyển giao (1,5 phút):* Chiếu yêu cầu mức Cơ bản & Nâng cao trên Slide 17.
  2. *Thực hiện (5,5 phút):* Cặp đôi gõ, lưu và chạy `bai16_vandung.py` (dự phòng mất máy: viết mã và tính kết quả ra vở).
  3. *Báo cáo, thảo luận (2 phút):* Kiểm tra 2–3 máy đại diện, bấm hiện đáp số chuẩn đối chiếu.
  4. *Kết luận, nhận định & Dặn dò (4 phút):* Chốt 4 ý cốt lõi trên Slide 18, giao bài tập tự luyện ở nhà và dẫn chuyển sang Bài 17.

---

## IV. ĐÁNH GIÁ VÀ PHƯƠNG ÁN PHÂN HÓA

### 1. Liên kết Mục tiêu – Minh chứng – Công cụ đánh giá

| Mục tiêu | Hoạt động tương ứng | Minh chứng học tập | Công cụ đánh giá |
|---|---|---|---|
| **M1** | HĐ 1, HĐ 2.1, HĐ 3.1 | Phiếu số 1 (Phần 1), thẻ giơ tay Câu 1–2 | Bảng kiểm phiếu, trắc nghiệm nhanh |
| **M2** | HĐ 2.2, HĐ 3.1 | Phiếu số 1 (Phần 2), thẻ giơ tay Câu 3–4 | Nhận xét nhóm, trắc nghiệm nhanh |
| **M3** | HĐ 2.3, HĐ 3.2 | Bảng so sánh 2 chế độ (Phiếu số 2), Câu 5–6 | Vấn đáp nhanh, thẻ A–D |
| **M4** | HĐ 3.2, HĐ 4 | `bai16_th1.py`, sửa 3 lỗi, `bai16_vandung.py` | Rubric chấm thực hành (`04_De_Kiem_Tra_Va_Dap_An_Bai_16.md`) |

### 2. Tổng hợp phân hóa học sinh (không gắn nhãn học sinh)
- **Hỗ trợ mức nền (HS gặp khó khăn):** Phiếu số 1 có kho từ khóa ghép ô; Phiếu số 2 có dòng mẫu đánh dấu sẵn vị trí dấu ngoặc/nháy; cho phép gõ chuỗi không dấu ở tiết đầu để tránh lỗi bộ gõ; ghép cặp đôi hỗ trợ nhau rà lỗi.
- **Mở rộng mức nâng cao (HS tiếp thu nhanh):** Câu hỏi mở rộng về tính đa nền tảng và giới hạn tốc độ của ngôn ngữ thông dịch; thực hành vẽ khung hóa đơn `bai16_nangcao.py`, thử nghiệm phân biệt `SyntaxError` vs `ZeroDivisionError` và tính phần tiền quỹ còn dư ở HĐ 4.

---

## V. ĐIỀU CHỈNH SAU BÀI DẠY

*(Giáo viên ghi nhận sau khi triển khai thực tế trên lớp)*

- **Những nội dung/hoạt động thực hiện hiệu quả:**
  ........................................................................................................................................
- **Khó khăn, vướng mắc phát sinh (thời lượng 2 tiết, lỗi IDLE/bộ gõ, mức độ tiếp thu của HS):**
  ........................................................................................................................................
- **Nguyên nhân:**
  ........................................................................................................................................
- **Dự kiến điều chỉnh cho các lớp/lần dạy sau (và khi đối chiếu bản in SGK Bài 16 & PPCT chính thức của trường):**
  ........................................................................................................................................
