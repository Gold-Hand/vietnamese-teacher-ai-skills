# KỊCH BẢN POWERPOINT – TIN HỌC 10 – BÀI 16
**Bài học:** Ngôn ngữ lập trình bậc cao và Python (Chủ đề 5 – Bộ sách Kết nối tri thức với cuộc sống)

---

## 1. Thông tin tổng quan & Mục tiêu bài học

- **Môn học / Khối lớp:** Tin học – Lớp 10 (GDPT 2018 – Bộ Kết nối tri thức với cuộc sống).
- **Thời lượng:** 2 tiết (90 phút = Tiết 1: 45 phút | Tiết 2: 45 phút) — **đồng bộ 100% với `01_KHBD_Bai_16_Tin_10_KNTT.md`**.
- **Tổng số slide:** **18 slide** (Tiết 1: Slide 1–9; Tiết 2: Slide 10–18).
- **Công cụ xuất:** Tự động xuất PowerPoint 16:9 bằng `scripts/office_generator/cli.py pptx --template education` kèm `Speaker_Notes_Bai_16.md` (và có hướng dẫn Canva / NotebookLM).
- **Ranh giới nội dung:** Chuẩn Bài 16 (`print()` và biểu thức số học trực tiếp; **không đưa biến/lệnh gán của Bài 17**).

### Mục tiêu bài học (đồng bộ mã với KHBD)
- **M1:** Nêu khái niệm NNLT; phân biệt ngôn ngữ máy, hợp ngữ và NNLT bậc cao; nêu vai trò chương trình dịch.
- **M2:** Nêu đặc điểm, ưu điểm nổi bật và ứng dụng thực tế của Python.
- **M3:** Phân biệt chế độ gõ lệnh trực tiếp (*Interactive Mode*, `>>>`) và chế độ soạn thảo (*Script Mode*, `.py`) trong IDLE.
- **M4:** Thực hành gõ lệnh trực tiếp; tạo, lưu tệp `.py`, chạy chương trình Python đầu tiên và sửa lỗi cú pháp cơ bản.

---

## 2. Bảng đối chiếu nhất quán với KHBD (90 phút / 18 slide)

| Mã mục tiêu | Hoạt động KHBD | Slide nội dung & minh họa | Slide kiểm tra / tương tác | Thời lượng |
|---|---|---|---|---:|
| **M1** | HĐ 1, HĐ 2.1, HĐ 3.1 | Slide 1, 2, 3, 4, 5 | Slide 2 (Tình huống Robot), **Slide 6 (TN Câu 1–2)** | 27 phút |
| **M2** | HĐ 2.2, HĐ 3.1 | Slide 7, 8 | **Slide 9 (TN Câu 3–4 & Chốt Tiết 1)** | 18 phút |
| **M3** | HĐ 2.3, HĐ 3.2 | Slide 10, 11, 12 | **Slide 13 (TN Câu 5–6)** | 16 phút |
| **M4** | HĐ 3.2, HĐ 4 | Slide 14, 15, 16, 17, 18 | Slide 15 (Thực hành & Săn lỗi), Slide 16 (Nâng cao), Slide 17 (Vận dụng) | 29 phút |
| **Tổng cộng** | **7 chặng (2 tiết)** | **18 slide** | **6 câu TN đầy đủ A–D + 3 bài thực hành** | **90 phút** |

---

## 3. Bảng phân bổ 18 slide chi tiết (Nội dung hiển thị & Ghi chú thuyết trình)

### TIẾT 1 (45 PHÚT) – SLIDE 1 ĐẾN SLIDE 9

| Số slide | Tiêu đề | Mục tiêu & Thời lượng | Nội dung hiển thị trên slide *(súc tích, không nhồi chữ)* | Hình ảnh / Sơ đồ đề xuất | Ghi chú thuyết trình (Speaker Notes) & Hoạt động tương tác |
|---:|---|---|---|---|---|
| **1** | **BÀI 16: NGÔN NGỮ LẬP TRÌNH BẬC CAO VÀ PYTHON** | Mở bài (M1–M4)<br>*(2 phút)* | • Tin học 10 – Chủ đề 5 *(Kết nối tri thức)*<br>• Thời lượng: 2 tiết (90 phút)<br>• **4 mục tiêu khám phá:**<br>&nbsp;&nbsp;1. Ngôn ngữ lập trình & Chương trình dịch<br>&nbsp;&nbsp;2. Vì sao chọn **Python**?<br>&nbsp;&nbsp;3. Hai chế độ làm việc của **IDLE**<br>&nbsp;&nbsp;4. Chạy chương trình Python đầu tiên | Nền xanh navy `#0F172A`, 4 thẻ mục tiêu `M1–M4` nổi bật màu xanh dương, ngọc, vàng, xanh lá. | **Lời dẫn:** "Ở THCS các em đã kéo thả khối lệnh Scratch. Lên lớp 10, ta bước sang ngôn ngữ lập trình văn bản phổ biến hàng đầu thế giới là Python. Trong 2 tiết này lớp mình sẽ chinh phục 4 mục tiêu trên màn hình!" |
| **2** | **Khởi động: Ra lệnh cho Robot tính `5 + 3`** | Dẫn vào **M1**<br>*(6 phút)* | **Cùng yêu cầu tính `5 + 3`, chọn thẻ dễ hiểu nhất:**<br>• **Thẻ A:** `10110000 00000101` / `00000100 00000011`<br>• **Thẻ B:** `MOV AL, 5` / `ADD AL, 3`<br>• **Thẻ C:** `print(5 + 3)`<br><br>❓ **Thảo luận (2 phút):** Thẻ nào dễ hiểu nhất? Nếu máy chỉ hiểu Thẻ A còn người viết Thẻ C thì cần gì ở giữa? | Bố cục 3 thẻ so sánh song song (xám – xanh – vàng) và thanh câu hỏi thảo luận đậm phía dưới. | **Tương tác (HĐ 1):** Phát Phiếu số 1, cho cặp đôi thảo luận 2 phút → gọi 2 HS trả lời.<br>**Dự kiến trả lời:** Thẻ C dễ nhất vì gần tiếng Anh và phép cộng; Thẻ A toàn 0/1 máy hiểu trực tiếp; cần "bộ phận phiên dịch" chuyển Thẻ C sang Thẻ A. |
| **3** | **Ngôn ngữ lập trình là gì?** | **M1**<br>*(4 phút)* | • **Chương trình:** Dãy câu lệnh chỉ dẫn máy tính thực hiện một thuật toán.<br>• **Ngôn ngữ lập trình (NNLT):** Ngôn ngữ dùng để viết chương trình cho máy tính.<br>• **Vai trò:** Cầu nối chuyển ý tưởng thuật toán của con người thành chỉ dẫn chính xác cho máy. | Sơ đồ 3 khối mũi tên ngang: `Ý tưởng/Thuật toán → Ngôn ngữ lập trình → Máy tính thực thi`. | **Lời dẫn (HĐ 2.1):** Liên hệ từ ngôn ngữ giao tiếp hằng ngày sang ngôn ngữ giao tiếp với máy tính; nhắc lại sự chuyển tiếp từ Scratch (THCS) sang viết lệnh văn bản (THPT). |
| **4** | **3 mức ngôn ngữ: Máy – Hợp ngữ – Bậc cao** | **M1**<br>*(6 phút)* | **So sánh 3 mức ngôn ngữ lập trình:**<br>• **Ngôn ngữ máy** *(Cốt lõi)*: Dãy bit `0`, `1` • Máy hiểu trực tiếp • Rất khó viết, phụ thuộc phần cứng.<br>• **Hợp ngữ** *(Mở rộng)*: Từ gợi nhớ (`MOV`, `ADD`) • Cần hợp dịch • Phụ thuộc phần cứng.<br>• **NNLT bậc cao** *(Cốt lõi)*: Gần tiếng Anh/toán (`print(5+3)`) • Độc lập máy • Dễ học, dễ sửa lỗi (Python, C++, Java). | 3 thẻ so sánh rõ nhãn *Cốt lõi* và *Mở rộng* để HS không bị quá tải. | **Điều phối (HĐ 2.1):** Cho HS hoàn thành Phần 1 Phiếu số 1 trong 5 phút (HS yếu dùng kho từ khóa gợi ý). Hỏi mở rộng HS khá: *"Vì sao code Python viết trên Windows sang macOS vẫn chạy được?"* |
| **5** | **Chương trình dịch – "Người phiên dịch" của máy tính** | **M1**<br>*(4 phút)* | • **Vấn đề:** Máy tính chỉ hiểu `0` và `1`, không tự hiểu `print(5 + 3)`.<br>• **Chương trình dịch** *(Cốt lõi)*: Chuyển mã nguồn **NNLT bậc cao → Ngôn ngữ máy**.<br>• **Mở rộng tham khảo:**<br>&nbsp;&nbsp;– *Thông dịch (Python):* Dịch & chạy từng lệnh.<br>&nbsp;&nbsp;– *Biên dịch (C/C++):* Dịch toàn bộ rồi chạy. | Sơ đồ 4 khối mũi tên: `Mã nguồn Python → Chương trình dịch → Ngôn ngữ máy → Kết quả`. | **Lời dẫn:** Nhấn mạnh ưu điểm thực tiễn của trình thông dịch Python: gõ sai ở dòng nào máy dừng báo ngay dòng đó, rất phù hợp cho người mới học lớp 10. |
| **6** | **Kiểm tra nhanh 1 (Củng cố M1)** | Kiểm tra **M1**<br>*(5 phút)* | **Câu 1:** Máy tính có thể thực hiện trực tiếp chương trình viết bằng ngôn ngữ nào?<br>**A.** Ngôn ngữ tự nhiên &emsp; **B.** Ngôn ngữ máy<br>**C.** Hợp ngữ &emsp;&emsp;&emsp;&emsp;&nbsp; **D.** Ngôn ngữ lập trình bậc cao<br><br>**Câu 2:** Vai trò chính của chương trình dịch là gì?<br>**A.** Soạn thảo văn bản báo cáo cho lập trình viên.<br>**B.** Bảo vệ máy tính khỏi phần mềm độc hại.<br>**C.** Chuyển chương trình viết bằng NNLT bậc cao sang ngôn ngữ máy.<br>**D.** Tăng dung lượng bộ nhớ RAM của máy tính. | 2 khung câu hỏi trắc nghiệm rõ ràng với 4 thẻ A, B, C, D cân đối; không lộ đáp án trên mặt slide. | **Tương tác (HĐ 3.1):** Cả lớp giơ thẻ A/B/C/D đồng loạt.<br>**Đáp án & Giải thích GV:**<br>• **Câu 1 – B:** Phần cứng CPU chỉ xử lý trực tiếp dãy bit của ngôn ngữ máy.<br>• **Câu 2 – C:** Chương trình dịch chuyển đổi mã nguồn bậc cao sang ngôn ngữ máy. |
| **7** | **Khám phá Python: Ngắn gọn & Dễ học** | **M2**<br>*(7 phút)* | **Cùng in `"Xin chao lop 10!"`:**<br>• **Minh họa C++ (5 dòng):** `#include <iostream>` ... `std::cout << ...`<br>• **Python (1 dòng duy nhất):** `print("Xin chao lop 10!")`<br><br>**Ưu điểm nổi bật của Python:**<br>✅ Cú pháp ngắn gọn, gần tiếng Anh tự nhiên<br>✅ Miễn phí, mã nguồn mở, chạy đa nền tảng<br>✅ Dễ đọc, dễ học cho học sinh mới bắt đầu | Khung code tối màu so sánh trực quan C++ (5 dòng) vs Python (1 dòng) bên trái + thẻ ưu điểm bên phải. | **Điều phối (HĐ 2.2):** Nhóm 4 HS thảo luận Phần 2 Phiếu số 1 (4,5 phút). Hỏi nâng cao: *"Python có hạn chế nào không?"* *(Tốc độ thực thi thuần chậm hơn C/C++ do cơ chế thông dịch)*. |
| **8** | **Python đang ở đâu quanh ta?** | **M2**<br>*(6 phút)* | **4 lĩnh vực ứng dụng mạnh của Python:**<br>• 🤖 **Trí tuệ nhân tạo (AI) & Học máy**<br>• 📊 **Khoa học dữ liệu & Phân tích số liệu**<br>• 🌐 **Phát triển Web** *(hệ thống phía máy chủ)*<br>• ⚙️ **Tự động hóa & Giáo dục lập trình** | Lưới 2×2 gồm 4 thẻ đánh số `01–04` màu phân biệt rõ nét. | **Lời dẫn:** Kết nối nghề nghiệp và thực tiễn: Python không chỉ để học ở lớp 10 mà là công cụ chủ lực trong AI, khoa học dữ liệu và tự động hóa hiện nay. |
| **9** | **Kiểm tra nhanh 2 & Chốt Tiết 1** | Kiểm tra **M2**<br>*(5 phút)* | **Câu 3:** Ưu điểm nào khiến Python rất phù hợp cho học sinh lớp 10 mới học lập trình?<br>**A.** Cú pháp ngắn gọn, rõ ràng, gần ngôn ngữ tự nhiên.<br>**B.** Không cần cài đặt bất kỳ chương trình dịch nào.<br>**C.** Chỉ chạy được duy nhất trên hệ điều hành Windows.<br>**D.** Bắt buộc viết lệnh bằng các dãy số `0` và `1`.<br><br>**Câu 4:** Lĩnh vực nào sau đây ứng dụng Python rất phổ biến?<br>**A.** Chế tạo linh kiện bán dẫn vật lý.<br>**B.** Trí tuệ nhân tạo, khoa học dữ liệu và phát triển web.<br>**C.** Sửa chữa trực tiếp mạch điện nguồn máy tính.<br>**D.** Thay thế hoàn toàn hệ điều hành máy tính. | 2 khung câu hỏi trắc nghiệm đủ 4 phương án A, B, C, D; không lộ đáp án trên mặt slide. | **Tương tác (HĐ 3.1):** Giơ thẻ đồng loạt.<br>**Đáp án & Giải thích GV:**<br>• **Câu 3 – A** (loại B: vẫn cần trình thông dịch; C: đa nền tảng; D: ngôn ngữ máy).<br>• **Câu 4 – B** (3 thế mạnh lớn của thư viện Python).<br>**Chuyển tiết:** Chuẩn bị thực hành IDLE ở Tiết 2. |

---

### TIẾT 2 (45 PHÚT) – SLIDE 10 ĐẾN SLIDE 18

| Số slide | Tiêu đề | Mục tiêu & Thời lượng | Nội dung hiển thị trên slide *(súc tích, không nhồi chữ)* | Hình ảnh / Sơ đồ đề xuất | Ghi chú thuyết trình (Speaker Notes) & Hoạt động tương tác |
|---:|---|---|---|---|---|
| **10** | **Môi trường lập trình Python (IDLE)** | **M3**<br>*(4 phút)* | • **IDLE** *(Integrated Development and Learning Environment)*: Môi trường lập trình chuẩn đi kèm bộ cài Python 3.<br>• **Gồm 2 chế độ làm việc chính:**<br>&nbsp;&nbsp;1. **Chế độ gõ lệnh trực tiếp** *(Interactive Mode)*<br>&nbsp;&nbsp;2. **Chế độ soạn thảo chương trình** *(Script Mode)*<br>• *(Mở rộng tham khảo: Thonny, VS Code)* | Bố cục 2 cột giới thiệu IDLE và 2 chế độ làm việc; kết hợp GV mở trực tiếp IDLE thật trên máy chiếu. | **Lời dẫn (HĐ 2.3):** GV khởi động IDLE (Python 3) từ Start Menu cho HS quan sát trực tiếp thanh menu `File`, `Run` và dấu nhắc `>>>`. Nhấn mạnh IDLE chạy 100% ngoại tuyến. |
| **11** | **Chế độ 1: Gõ lệnh trực tiếp (Interactive Mode)** | **M3**<br>*(4 phút)* | **Dấu hiệu nhận biết:** Cửa sổ Python Shell có dấu nhắc **`>>>`**<br><br>```python
>>> 15 + 25
40
>>> print("Chao mung den voi Python!")
Chao mung den voi Python!
```<br>• Gõ từng lệnh → nhấn `Enter` → nhận kết quả ngay.<br>• **Hạn chế:** Không lưu thành tệp chương trình hoàn chỉnh. | Khung mô phỏng IDLE Shell nền sáng chuẩn màu dấu nhắc `>>>` bên trái + thẻ đặc điểm bên phải. | **Demo trực tiếp:** GV gõ 2 lệnh trên vào IDLE Shell.<br>**Câu hỏi gợi mở:** "Đóng IDLE lại thì lệnh vừa gõ còn lưu thành tệp không?" → Chốt: Tiện tính nhanh/thử nghiệm như máy tính bỏ túi, không lưu chương trình dài. |
| **12** | **Chế độ 2: Soạn thảo (Script Mode) & So sánh** | **M3**<br>*(4 phút)* | **Mở cửa sổ soạn thảo:** `File → New File` *(không có `>>>`)*<br><br>| Tiêu chí | Trực tiếp (`>>>`) | Soạn thảo (`.py`) |<br>|---|---|---|<br>| Dấu nhắc `>>>` | Có | Không |<br>| Chạy lệnh | Từng lệnh (`Enter`) | Cả tệp (`F5`) |<br>| Lưu chương trình | Không lưu tệp | Lưu tệp `.py` | | Bảng so sánh PowerPoint gốc 4×3 rõ nét kèm thanh hướng dẫn `File → New File`. | **Demo trực tiếp:** GV mở `New File`, viết 2 dòng `print(...)`, lưu `bai_dau_tien.py`, nhấn `F5`. Demo thêm lỗi khi gõ nhầm `>>>` trong Script Mode để HS nhớ tránh. |
| **13** | **Kiểm tra nhanh 3 (Củng cố M3)** | Kiểm tra **M3**<br>*(4 phút)* | **Câu 5:** Dấu hiệu nào giúp nhận biết em đang ở chế độ gõ lệnh trực tiếp (Interactive Mode) trong IDLE?<br>**A.** Thanh tiêu đề có đuôi `.py`. &emsp; **B.** Có dấu nhắc `>>>` ở đầu dòng.<br>**C.** Không thể dùng lệnh `print()`. &nbsp; **D.** Phải nhấn `F5` mới chạy được.<br><br>**Câu 6:** Để viết chương trình Python nhiều dòng và lưu lại chạy nhiều lần, em chọn thao tác nào?<br>**A.** Gõ trực tiếp sau dấu `>>>` rồi chụp ảnh màn hình.<br>**B.** Đổi tên tệp sang đuôi `.docx`.<br>**C.** Chọn `File → New File`, viết lệnh, lưu đuôi `.py` và nhấn `F5`.<br>**D.** Khởi động lại máy tính sau mỗi dòng lệnh. | 2 khung câu hỏi trắc nghiệm đủ A, B, C, D rõ ràng. | **Tương tác (đầu HĐ 3.2):** Giơ thẻ đồng loạt.<br>**Đáp án & Giải thích GV:**<br>• **Câu 5 – B:** Dấu `>>>` đặc trưng của Shell.<br>• **Câu 6 – C:** Quy trình chuẩn Script Mode để lưu và chạy tệp `.py`. |
| **14** | **Quy trình 4 bước tạo chương trình Python đầu tiên** | **M4**<br>*(4 phút)* | **4 bước vàng trong IDLE:**<br>1. **Tạo mới:** `File → New File` (`Ctrl + N`)<br>2. **Viết lệnh:** Dùng `print(...)` và phép tính `+`, `-`, `*`, `/`<br>3. **Lưu tệp:** `File → Save` (`Ctrl + S`) → đặt tên không dấu, đuôi **`.py`**<br>4. **Chạy:** `Run → Run Module` (phím **`F5`**)<br><br>⚠️ *Lưu ý:* Python phân biệt chữ **hoa/thường** (`print` ≠ `Print`). | Sơ đồ quy trình 4 bước ngang có vòng tròn đánh số `1 → 2 → 3 → 4` và thanh cảnh báo màu vàng. | **Lời dẫn (HĐ 3.2):** Phổ biến thư mục lưu bài (`D:\Tin10\Bai16\...`) và quy ước đổi vai gõ phím sau 10 phút cho cặp 2 HS/máy. |
| **15** | **Thực hành 1 (Cơ bản) & "Săn lỗi cú pháp"** | **M4**<br>*(8 phút)* | **Nhiệm vụ Cơ bản (`bai16_th1.py`):**<br>1. Gõ ở `>>>`: `2026 - 2010`, `(12 + 8) * 5 / 2`, `print(...)`.<br>2. Tạo `bai16_th1.py` in: Tên nhóm, Lớp, và chu vi/diện tích HCN `(12 × 5)`:<br>`print("Chu vi:", (12 + 5) * 2, "| Dien tich:", 12 * 5)`<br><br>**Săn 3 lỗi cú pháp (`SyntaxError`):**<br>• `Print("Xin chao")` &nbsp; • `print("Tin hoc 10)` &nbsp; • `print(10 + 5 * 2` | Bố cục 2 cột: Cột trái nhiệm vụ thực hành xanh dương; Cột phải khung viền đỏ săn 3 lỗi cú pháp. | **Điều phối (HĐ 3.2):** HS làm Phần 2 Phiếu số 2. GV hỗ trợ HS yếu (chú ý bộ gõ tiếng Việt, quên ngoặc/nháy).<br>**Đáp án Săn lỗi GV:** (1) `print("Xin chao")`; (2) `print("Tin hoc 10")`; (3) `print(10 + 5 * 2)`. |
| **16** | **Thực hành 2 (Nâng cao – Phân hóa)** | **M4** *(nâng cao)*<br>*(4 phút)* | **Dành cho cặp hoàn thành sớm (`bai16_nangcao.py`):**<br>• Dùng `print()` vẽ khung hóa đơn 3 món đồ dùng học tập:<br>&nbsp;&nbsp;4 vở × 12.000đ \| 3 bút × 5.000đ \| 1 thước × 18.000đ.<br>• Tính tổng trực tiếp: `print("Tong:", 4*12000 + 3*5000 + 1*18000)`<br>• **Thử nghiệm thêm:** Chạy `print(10 / 0)` và nhận xét thông báo lỗi! | Bố cục 2 cột tách phần nhiệm vụ nâng cao (cột trái) và thử nghiệm lỗi `ZeroDivisionError` (cột phải). | **Điều phối phân hóa:** Khuyến khích HS khá, giỏi trình bày khung bảng đẹp và giải thích khác biệt sơ lược giữa `SyntaxError` (lỗi cú pháp) và `ZeroDivisionError` (lỗi khi chạy). Đáp số tổng: `81000`. |
| **17** | **Vận dụng: Dự toán trang trí lớp 10** | **M4** *(vận dụng)*<br>*(9 phút)* | **Tạo tệp `bai16_vandung.py` in bảng dự toán lớp 10:**<br>• 2 cuộn giấy màu (`25000`đ/cuộn)<br>• 5 cây bút dạ (`8000`đ/cây)<br>• 1 cuộn băng keo (`15000`đ)<br><br>**Yêu cầu:**<br>• *(Cơ bản)* In từng khoản, **Tổng tiền** và **Mỗi tổ góp** (4 tổ).<br>• *(Nâng cao)* Tính **Tiền còn dư** nếu quỹ lớp có `150000`đ. | Bố cục 2 cột tách dữ kiện bài toán (trái) và yêu cầu phân hóa Cơ bản – Nâng cao (phải). | **Điều phối (HĐ 4):** Cho cặp thực hành 5,5 phút → kiểm tra nhanh 2–3 máy.<br>**Đáp số chuẩn GV:** Tổng = `105000`đ; Mỗi tổ góp = `26250.0`đ; Tiền dư = `45000`đ.<br>**Gợi mở Bài 17:** Nhấn mạnh sự bất tiện khi gõ lặp biểu thức tính tổng 3 lần. |
| **18** | **Tổng kết Bài 16 & Chuẩn bị Bài 17** | Tổng kết (M1–M4)<br>*(4 phút)* | **4 điểm cốt lõi cần nhớ:**<br>1. **NNLT bậc cao** gần ngôn ngữ tự nhiên, cần **chương trình dịch**.<br>2. **Python** ngắn gọn, dễ học, miễn phí, ứng dụng mạnh (AI, dữ liệu, web).<br>3. **IDLE** có 2 chế độ: **Trực tiếp (`>>>`)** & **Soạn thảo (`.py`, `F5`)**.<br>4. Chương trình đầu tiên dùng `print()` & phép tính; chú ý đúng cú pháp.<br><br>🔭 **Chuẩn bị Bài 17:** Muốn đặt tên lưu giá trị để không gõ lặp biểu thức? → Đọc trước **Bài 17: Biến và lệnh gán**. | Nền xanh navy `#0F172A`, 4 thẻ tổng kết đánh số `1–4` và khung vàng dẫn nối Bài 17 ở chân trang. | **Lời dẫn chốt bài:** Mời 1 HS nhắc lại khác biệt giữa 2 chế độ IDLE; dặn lưu bài đúng thư mục, tắt máy đúng quy định phòng Tin học và đọc trước Bài 17. |

---

## 4. Phụ lục đáp án trắc nghiệm nhanh trên Slide (Dành cho giáo viên)

| Câu | Slide | Mục tiêu | Đáp án | Giải thích ngắn |
|---:|:---:|:---:|:---:|---|
| 1 | Slide 6 | M1 | **B** | CPU chỉ thực hiện trực tiếp dãy bit của ngôn ngữ máy. |
| 2 | Slide 6 | M1 | **C** | Chương trình dịch chuyển đổi NNLT bậc cao sang ngôn ngữ máy. |
| 3 | Slide 9 | M2 | **A** | Cú pháp ngắn gọn, gần ngôn ngữ tự nhiên là ưu thế lớn của Python. |
| 4 | Slide 9 | M2 | **B** | Python mạnh về AI, khoa học dữ liệu, web và tự động hóa. |
| 5 | Slide 13 | M3 | **B** | Dấu nhắc `>>>` là đặc trưng của cửa sổ Shell (Interactive Mode). |
| 6 | Slide 13 | M3 | **C** | Script Mode (`File → New File`, lưu `.py`, `F5`) lưu và chạy lại chương trình nhiều dòng. |

---

## 5. Hướng dẫn sử dụng PowerPoint xuất tự động & Gợi ý NotebookLM

- **Tệp PowerPoint đã xuất sẵn:** `Bai_16_Ngon_ngu_lap_trinh_bac_cao_va_Python.pptx` (16:9, 18 slide đa dạng bố cục, Speaker Notes nhúng sẵn trên cả 18 slide + tệp `Speaker_Notes_Bai_16.md`).
- **Tùy chọn tạo nhanh thêm bản nháp bằng NotebookLM:** Tải phần nội dung hiển thị của 18 slide (bỏ Mục 4 đáp án để không lộ trên slide) vào NotebookLM → Studio → Slide Deck với yêu cầu giữ chuẩn tiếng Việt GDPT 2018, chỉ dùng `print()` và biểu thức số học, đủ A–D không lộ đáp án.
