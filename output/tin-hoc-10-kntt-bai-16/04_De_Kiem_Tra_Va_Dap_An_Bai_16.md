# BỘ ĐỀ KIỂM TRA, MA TRẬN, ĐẶC TẢ VÀ ĐÁP ÁN – TIN HỌC 10 – BÀI 16
**Chủ đề:** Ngôn ngữ lập trình bậc cao và Python (Chủ đề 5 – Bộ sách Kết nối tri thức với cuộc sống)

---

## 1. Căn cứ, phạm vi, giả định & kiểm soát đúng khối lớp

- **Môn học / Khối lớp:** Tin học – Lớp 10 (Bộ sách *Kết nối tri thức với cuộc sống*, Chủ đề 5, Bài 16).
- **Cấu trúc đánh giá (thang 10,0 điểm | thời lượng dự kiến 45 phút nếu gộp thành 1 bài kiểm tra, hoặc tách lẻ dùng đánh giá thường xuyên):**
  - **Phần I:** 10 câu trắc nghiệm nhiều lựa chọn 4 phương án A, B, C, D (`5,0 điểm`; ~10 phút).
  - **Phần II:** 3 câu hỏi tự luận ngắn (`2,0 điểm`; ~12 phút).
  - **Phần III:** 2 bài tập thực hành lập trình Python 3 trên IDLE (`3,0 điểm`; ~20 phút; rà soát ~3 phút).
- **Kiểm soát chặt phạm vi Bài 16 (không vượt sang Bài 17 hoặc lớp 11):**
  - Chỉ kiểm tra: khái niệm NNLT, ngôn ngữ máy/hợp ngữ *(mức cơ bản)*/NNLT bậc cao, chương trình dịch, đặc điểm & ứng dụng Python, IDLE (Interactive Mode `>>>` và Script Mode `.py`), viết & chạy chương trình đầu tiên dùng `print(...)` cùng biểu thức số học (`+`, `-`, `*`, `/`, ngoặc đơn) và sửa lỗi cú pháp cơ bản.
  - **Không đưa vào đề:** biến, lệnh gán `=` (Bài 17), `input()` (Bài 18), rẽ nhánh `if`, vòng lặp `for`/`while`, hàm `def`.
- **Giả định & lưu ý pháp lý:** Tỷ lệ mức độ nhận thức **40% Nhận biết – 30% Thông hiểu – 30% Vận dụng** là đề xuất tham khảo (do repository chưa có văn bản quy định tỷ lệ riêng của trường/Sở GDĐT); giáo viên đối chiếu quy định kiểm tra đánh giá hiện hành của đơn vị và bản in SGK Bài 16 trước khi ban hành chính thức.

---

## 2. Ma trận & Bản đặc tả đối chiếu Yêu cầu cần đạt (YCCĐ)

### 2.1. Ma trận đề kiểm tra (Thang 10,0 điểm)

| TT | Nội dung / Đơn vị kiến thức | Nhận biết | Thông hiểu | Vận dụng | Tổng câu/bài | Tổng điểm | Tỉ lệ (%) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | NNLT, 3 mức ngôn ngữ & Chương trình dịch (M1) | 3 TN *(C1–C3: 1,50 đ)* | 1 TL *(TL1: 0,50 đ)* | 0 | 3 TN + 1 TL | **2,00 đ** | **20,0%** |
| 2 | Đặc điểm, ưu điểm & ứng dụng Python (M2) | 2 TN *(C4–C5: 1,00 đ)* | 0 | 0 | 2 TN | **1,00 đ** | **10,0%** |
| 3 | Môi trường IDLE, Interactive & Script Mode (M3) | 3 TN *(C6–C8: 1,50 đ)* | 1 TL *(TL2: 0,75 đ)* | 0 | 3 TN + 1 TL | **2,25 đ** | **22,5%** |
| 4 | Chương trình Python đầu tiên (`print()`, phép toán, lỗi cú pháp) (M4) | 0 | 2 TN *(C9–C10)* + 1 TL *(TL3)* *(1,75 đ)* | 2 TH *(TH1, TH2: 3,00 đ)* | 2 TN + 1 TL + 2 TH | **4,75 đ** | **47,5%** |
| | **Tổng số câu / điểm** | **8 TN (4,00 đ)** | **2 TN + 3 TL (3,00 đ)** | **2 TH (3,00 đ)** | **10 TN + 3 TL + 2 TH** | **10,00 đ** | **100%** |

### 2.2. Bản đặc tả câu hỏi

| Nội dung | Yêu cầu cần đạt (YCCĐ) | Nhận biết | Thông hiểu | Vận dụng | Tổng |
|---|---|---:|---:|---:|---:|
| **1. NNLT & Chương trình dịch (M1)** | - **YCCĐ 1.1:** Nêu được khái niệm NNLT, nhận biết ngôn ngữ máy, NNLT bậc cao và vai trò chương trình dịch.<br>- **YCCĐ 1.2:** Giải thích ngắn vì sao chọn NNLT bậc cao và cần chương trình dịch. | C1, C2, C3 *(1,50 đ)* | TL1 *(0,50 đ)* | — | **2,00 đ** |
| **2. Python (M2)** | - **YCCĐ 2.1:** Nêu được ưu điểm và lĩnh vực ứng dụng thực tế của Python. | C4, C5 *(1,00 đ)* | — | — | **1,00 đ** |
| **3. IDLE & 2 chế độ (M3)** | - **YCCĐ 3.1:** Nhận biết dấu nhắc `>>>`, đuôi `.py` và thao tác tạo–lưu–chạy.<br>- **YCCĐ 3.2:** Phân biệt 2 chế độ và chọn đúng chế độ theo yêu cầu học tập. | C6, C7, C8 *(1,50 đ)* | TL2 *(0,75 đ)* | — | **2,25 đ** |
| **4. Chương trình đầu tiên (M4)** | - **YCCĐ 4.1:** Tính đúng kết quả lệnh `print()` kết hợp phép toán số học; phát hiện và sửa lỗi cú pháp cơ bản.<br>- **YCCĐ 4.2:** Tạo, lưu tệp `.py` và chạy được chương trình hiển thị thông tin và tính toán số học trực tiếp. | — | C9, C10, TL3 *(1,75 đ)* | TH1, TH2 *(3,00 đ)* | **4,75 đ** |
| **Tổng** | **Bao phủ đầy đủ M1–M4 của Bài 16** | **4,00 đ (40%)** | **3,00 đ (30%)** | **3,00 đ (30%)** | **10,00 đ** |

<!-- pagebreak -->

## 3. ĐỀ KIỂM TRA

### PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (5,0 điểm – 10 câu × 0,5 điểm)
*Chọn **01 phương án đúng nhất** cho mỗi câu hỏi sau:*

**Câu 1 (NB – M1).** Máy tính có thể hiểu và thực hiện **trực tiếp** chương trình viết bằng ngôn ngữ nào?
- A. Ngôn ngữ máy (biểu diễn bằng các dãy bit `0` và `1`).
- B. Ngôn ngữ lập trình bậc cao như Python, Java.
- C. Ngôn ngữ tự nhiên như tiếng Việt, tiếng Anh.
- D. Sơ đồ khối thuật toán vẽ trên giấy.

**Câu 2 (NB – M1).** Đặc điểm cơ bản của **ngôn ngữ lập trình bậc cao** là gì?
- A. Chỉ sử dụng hai chữ số `0` và `1` để viết câu lệnh.
- B. Câu lệnh gần ngôn ngữ tự nhiên và toán học, ít phụ thuộc phần cứng, dễ viết và dễ sửa lỗi.
- C. Chạy trực tiếp trên CPU mà không cần chương trình dịch.
- D. Chỉ dùng được trên một dòng máy tính duy nhất.

**Câu 3 (NB – M1).** Vai trò của **chương trình dịch** là gì?
- A. Dịch văn bản tiếng Anh sang tiếng Việt.
- B. Tự động sửa lỗi tư duy thuật toán cho lập trình viên.
- C. Chuyển đổi chương trình viết bằng ngôn ngữ lập trình bậc cao sang ngôn ngữ máy để máy tính thực hiện.
- D. Tăng tốc độ kết nối mạng Internet cho phòng máy.

**Câu 4 (NB – M2).** Ưu điểm nổi bật nào khiến **Python** phù hợp với học sinh lớp 10 mới bắt đầu lập trình?
- A. Đòi hỏi khai báo cú pháp phức tạp trước khi in một dòng chữ.
- B. Chỉ chạy được khi có kết nối Internet tốc độ cao.
- C. Là phần mềm đóng có phí bản quyền cao.
- D. Cú pháp ngắn gọn, rõ ràng, gần ngôn ngữ tự nhiên, mã nguồn mở miễn phí và đa nền tảng.

**Câu 5 (NB – M2).** Nhóm lĩnh vực nào sau đây ứng dụng ngôn ngữ **Python** rất phổ biến?
- A. Trí tuệ nhân tạo (AI), khoa học dữ liệu, phát triển web và tự động hóa.
- B. Lắp ráp phần cứng vỏ máy tính và hàn bảng mạch.
- C. Thay thế hoàn toàn bàn phím và chuột máy tính.
- D. Chỉ dùng để thay thế phần mềm soạn thảo văn bản.

**Câu 6 (NB – M3).** Trong **IDLE (Python 3)**, dấu nhắc nào cho biết em đang ở **chế độ gõ lệnh trực tiếp (Interactive Mode)**?
- A. `C:\>`
- B. `>>>`
- C. `###`
- D. `***`

**Câu 7 (NB – M3).** Tệp mã nguồn Python lưu từ **chế độ soạn thảo (Script Mode)** có phần mở rộng mặc định là gì?
- A. `.docx`
- B. `.xlsx`
- C. `.py`
- D. `.mp3`

**Câu 8 (NB – M3).** Để tạo cửa sổ soạn thảo chương trình mới và chạy chương trình sau khi lưu tệp trong IDLE, em thực hiện cặp thao tác nào?
- A. `File → New File` để tạo mới, sau đó `Run → Run Module` (hoặc phím `F5`) để chạy.
- B. `Edit → Copy` để tạo mới, sau đó `File → Close` để chạy.
- C. `Help → About IDLE` để tạo mới, sau đó nhấn `Esc` để chạy.
- D. `Shell → Restart Shell` để tạo mới, sau đó tắt cửa sổ IDLE.

**Câu 9 (TH – M4).** Kết quả hiển thị khi chạy câu lệnh Python 3 sau là gì?
```python
print("Ket qua:", (12 + 8) * 3 - 10 / 2)
```
- A. `Ket qua: 55`
- B. `Ket qua: 55.0`
- C. `Ket qua: 25.0`
- D. Báo lỗi cú pháp `SyntaxError`.

**Câu 10 (TH – M4).** Câu lệnh nào sau đây viết **đúng cú pháp Python 3** và chạy không báo lỗi?
- A. `Print("Xin chao Python")`
- B. `print("Xin chao Python)`
- C. `print(Xin chao Python)`
- D. `print("Xin chao Python")`

---

### PHẦN II. TỰ LUẬN NGẮN (2,0 điểm – 3 câu)

**Câu TL1 (0,50 điểm – TH – M1):** Vì sao khi viết phần mềm, lập trình viên thường dùng **ngôn ngữ lập trình bậc cao** thay vì **ngôn ngữ máy**? Để máy tính chạy được chương trình viết bằng Python cần thành phần nào hỗ trợ?

**Câu TL2 (0,75 điểm – TH – M3):** Nêu **02 điểm khác nhau** giữa **Interactive Mode** và **Script Mode** trong IDLE. Nếu cần viết chương trình gồm 6 dòng lệnh để nộp cho giáo viên, em chọn chế độ nào và vì sao?

**Câu TL3 (0,75 điểm – TH – M4):** Một bạn học sinh gõ 3 dòng sau vào cửa sổ Script Mode của IDLE nhưng không chạy được:
```python
>>> print("Chao mung den voi Tin hoc 10")
Print("Tong cua 15 va 25 la:")
print(15 + 25
```
Chỉ ra **03 lỗi sai** và viết lại đúng 3 dòng lệnh hoàn chỉnh trong Python 3.

---

### PHẦN III. THỰC HÀNH PYTHON 3 (3,0 điểm – 2 bài)

> *Quy định:* Thực hiện trong **IDLE (Script Mode)**, lưu đúng tên tệp `.py`, chạy kiểm thử bằng `F5`. Chỉ dùng `print(...)` và biểu thức số học (`+`, `-`, `*`, `/`, ngoặc đơn); **không cần dùng biến hay `input()`**.

**Bài thực hành 1 (1,25 điểm – VD – M4):** Tạo tệp `bai16_the_gioi_thieu.py` in thẻ giới thiệu học sinh có khung viền ký tự gồm tối thiểu 4 dòng: Tiêu đề `THE GIOI THIEU HOC SINH`, Họ tên/biệt danh & Lớp, Môn học yêu thích & Mục tiêu học Python, và tuổi ước tính tính bằng phép trừ trực tiếp trong `print()` (ví dụ `2026 - 2010`).

**Bài thực hành 2 (1,75 điểm – VD – M4):** Tạo tệp `bai16_du_toan.py` in bảng dự toán mua dụng cụ học tập gồm `4` quyển vở (`12000`đ/quyển), `3` cây bút (`5000`đ/cây), `1` bộ thước (`18000`đ/bộ) với tối thiểu 4 dòng: (1) Thành tiền từng món; (2) Tổng số tiền phải trả; (3) Số tiền trung bình mỗi bạn góp (nhóm 3 bạn); (4) *(Mức tối đa)* Tiền còn dư nếu nhóm mang theo `100000`đ — tất cả tính trực tiếp bằng biểu thức số học trong `print()`.

<!-- pagebreak -->

## 4. ĐÁP ÁN, HƯỚNG DẪN CHẤM & RUBRIC

### 4.1. Đáp án Phần I – Trắc nghiệm (5,0 điểm | phân bố cân đối 3A–2B–3C–2D)

| Câu | Đáp án | Giải thích ngắn |
|---:|:---:|---|
| 1 | **A** | Bộ xử lý chỉ thực thi trực tiếp ngôn ngữ máy (`0`, `1`). |
| 2 | **B** | NNLT bậc cao gần ngôn ngữ tự nhiên/toán học, ít phụ thuộc phần cứng, dễ học và dễ sửa. |
| 3 | **C** | Chương trình dịch chuyển đổi mã nguồn bậc cao sang mã máy. |
| 4 | **D** | Python ngắn gọn, rõ ràng, mã nguồn mở miễn phí, đa nền tảng. |
| 5 | **A** | Python mạnh về AI, khoa học dữ liệu, web và tự động hóa. |
| 6 | **B** | Dấu nhắc `>>>` đặc trưng của cửa sổ Python Shell (Interactive Mode). |
| 7 | **C** | Tệp mã nguồn Python có phần mở rộng chuẩn `.py`. |
| 8 | **A** | `File → New File` mở cửa sổ soạn thảo, `Run → Run Module` (`F5`) chạy chương trình. |
| 9 | **B** | `(12 + 8) * 3 - 10 / 2 = 60 - 5.0 = 55.0` (phép `/` trong Python 3 luôn cho `float`). |
| 10 | **D** | A sai chữ hoa `Print`, B thiếu dấu `"` đóng, C thiếu dấu nháy bao chuỗi. |

### 4.2. Hướng dẫn chấm Phần II – Tự luận ngắn (2,0 điểm)
- **TL1 (0,50 đ):** Nêu lý do NNLT bậc cao dễ viết/đọc/sửa, ít phụ thuộc máy hơn ngôn ngữ máy `0`/`1` *(0,25 đ)*; nêu đúng cần **chương trình dịch** (trình thông dịch Python) *(0,25 đ)*.
- **TL2 (0,75 đ):** Nêu đúng 2 điểm khác nhau về dấu nhắc/cách chạy và khả năng lưu tệp `.py` *(0,50 đ)*; chọn **Script Mode** để lưu tệp `.py` nhiều dòng nộp cho giáo viên *(0,25 đ)*.
- **TL3 (0,75 đ):** Chỉ đúng 3 lỗi: (1) thừa `>>>` dòng 1; (2) viết hoa `Print` dòng 2; (3) thiếu `)` dòng 3 *(0,45 đ)*; viết lại đúng 3 dòng `print(...)` *(0,30 đ)*.

### 4.3. Rubric chấm Phần III – Thực hành Python 3 (3,0 điểm | Sản phẩm + Quy trình)
*(Đáp số kiểm chứng bài TH2 trên Python 3.12.3: Từng món `48000`, `15000`, `18000`; Tổng `81000`; Mỗi bạn `27000.0`; Tiền dư `19000` — xem mã nguồn đầy đủ tại `06_Ma_Nguon_Python_Bai_16.py`.)*

| Tiêu chí | Điểm | Mức Tốt (100%) | Mức Đạt (50–75%) | Chưa đạt (0–25%) | Minh chứng |
|---|---:|---|---|---|---|
| **1. Bài TH1 (`bai16_the_gioi_thieu.py`)** | **1,00 đ** | Chạy không lỗi, khung viền gọn đẹp, đủ 4 dòng và tính tuổi trực tiếp bằng phép trừ trong `print()`. | Chạy được nhưng thiếu khung hoặc thiếu 1 ý / gõ cứng con số tuổi. | Lỗi cú pháp không chạy được hoặc chưa tạo tệp. | Tệp `.py` & kết quả Shell. |
| **2. Bài TH2 (`bai16_du_toan.py`)** | **1,50 đ** | Chạy không lỗi; biểu thức số học trực tiếp ra đúng cả 4 ý (`48000/15000/18000`, `81000`, `27000.0`, `19000`). | Đúng 3 ý cơ bản (thiếu ý tiền dư) hoặc sai ngoặc ở phép chia 3. | Tự tính nhẩm gõ sẵn số hoặc lỗi không chạy được. | Tệp `.py` & kết quả Shell. |
| **3. Quy trình IDLE & Lưu trữ tệp** | **0,50 đ** | Mở đúng Script Mode (không gõ `>>>`), lưu đúng tên `.py` vào đúng thư mục, tự chạy `F5` kiểm tra và sửa lỗi. | Lưu được `.py` nhưng sai tên/thư mục hoặc cần GV nhắc chạy `F5`. | Chỉ gõ ở Shell không lưu tệp `.py`. | Quan sát thao tác & thư mục bài nộp. |
