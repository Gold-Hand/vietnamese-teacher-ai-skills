# BỘ PHIẾU HỌC TẬP VÀ PHIẾU THỰC HÀNH – TIN HỌC 10 – BÀI 16
**Bài học:** Ngôn ngữ lập trình bậc cao và Python (Chủ đề 5 – Bộ sách Kết nối tri thức với cuộc sống)

---

## PHIẾU HỌC TẬP SỐ 1 (DÙNG CHO TIẾT 1 – 45 PHÚT)

- **Nhóm / Cặp học sinh:** ...................................................... **Lớp:** ..............

### KHỞI ĐỘNG: THỬ THÁCH "RA LỆNH CHO ROBOT TÍNH `5 + 3`"
Quan sát 3 tấm thẻ cùng yêu cầu máy tính tính `5 + 3` và hiển thị kết quả:
- **Thẻ A:** `10110000 00000101` / `00000100 00000011` / `11100110 00000001`
- **Thẻ B:** `MOV AL, 5` / `ADD AL, 3` / `OUT 1, AL`
- **Thẻ C:** `print(5 + 3)`

1. Thẻ nào em hiểu ngay lập tức? Vì sao? .................................................................................
2. Nếu máy tính chỉ hiểu Thẻ A còn con người viết Thẻ C, cần bộ phận gì ở giữa? ...........................

---

### PHẦN 1: SO SÁNH 3 MỨC NGÔN NGỮ LẬP TRÌNH & CHƯƠNG TRÌNH DỊCH

*Gợi ý từ khóa hỗ trợ (dùng để ghép vào bảng):* `chỉ gồm 0 và 1` • `ký hiệu gợi nhớ (MOV, ADD)` • `gần tiếng Anh và toán học` • `Có (hiểu trực tiếp)` • `Không (cần chương trình dịch)` • `Rất khó viết, phụ thuộc máy` • `Dễ học, ít phụ thuộc máy`.

| Tiêu chí | Ngôn ngữ máy *(Cốt lõi)* | Hợp ngữ *(Mở rộng)* | Ngôn ngữ lập trình bậc cao *(Cốt lõi)* |
|---|---|---|---|
| **Hình thức câu lệnh** | | | |
| **Máy tính hiểu trực tiếp?** | | | |
| **Mức độ dễ viết / sửa lỗi** | | | |
| **Ví dụ** | Mã nhị phân `0101...` | Assembly | Python, C++, Java |

- **Vai trò của chương trình dịch:** ..........................................................................................................
- **Câu hỏi nâng cao (khuyến khích):** Vì sao chương trình viết bằng Python trên Windows có thể mang sang macOS hoặc Linux chạy mà gần như không phải viết lại?
  ............................................................................................................................................................

---

### PHẦN 2: KHÁM PHÁ NGÔN NGỮ LẬP TRÌNH PYTHON (NHÓM 4 HS)

1. **Nêu ít nhất 3–4 ưu điểm nổi bật của Python đối với người mới học:**
   - .......................................................................................................................................................
   - .......................................................................................................................................................
   - .......................................................................................................................................................
2. **Kể tên 3–4 lĩnh vực ứng dụng thực tế phổ biến của Python hiện nay:**
   ............................................................................................................................................................
3. **Câu hỏi nâng cao (khuyến khích):** Theo nhóm em, Python có hạn chế nào so với ngôn ngữ biên dịch như C/C++ không?
   ............................................................................................................................................................

<!-- pagebreak -->

## PHIẾU THỰC HÀNH SỐ 2 (DÙNG CHO TIẾT 2 – 45 PHÚT)

- **Cặp học sinh:** (Bạn 1) ...................................... – (Bạn 2) ...................................... **Máy số:** ......
- *Quy tắc đổi vai:* Bạn 1 gõ máy 10 phút đầu (Phần A & B), Bạn 2 gõ máy 10 phút sau (Phần C & Vận dụng).

### PHẦN 1: BẢNG SO SÁNH 2 CHẾ ĐỘ LÀM VIỆC CỦA IDLE (ĐIỀN KHI QUAN SÁT GV DEMO)

| Tiêu chí | Chế độ gõ lệnh trực tiếp (Interactive Mode) | Chế độ soạn thảo chương trình (Script Mode) |
|---|---|---|
| **Dấu nhắc `>>>`** | | |
| **Cách chạy lệnh** | | |
| **Khả năng lưu tệp `.py`** | | |
| **Khi nào nên dùng?** | | |

---

### PHẦN 2: THỰC HÀNH CƠ BẢN TRÊN MÁY TÍNH (BẮT BUỘC)

**Nhiệm vụ A – Thử nghiệm trên chế độ gõ lệnh trực tiếp (`>>>`):**  
Mở **IDLE (Python 3)**, gõ lần lượt 3 lệnh sau vào sau dấu nhắc `>>>`, nhấn `Enter` và ghi lại kết quả màn hình:

| STT | Lệnh gõ sau dấu nhắc `>>>` | Kết quả hiển thị thực tế |
|---:|---|---|
| 1 | `2026 - 2010` | |
| 2 | `(12 + 8) * 5 / 2` | |
| 3 | `print("Toi dang hoc Python o lop 10")` | |

**Nhiệm vụ B – Tạo, lưu và chạy chương trình đầu tiên trong Script Mode (`bai16_th1.py`):**
1. Chọn **`File → New File`** (`Ctrl + N`) *(lưu ý: cửa sổ mới **không có** dấu `>>>`)*.
2. Gõ 3 dòng lệnh sau *(không dùng biến, chỉ dùng `print()` và phép toán số học; có thể gõ tiếng Việt không dấu để tránh lỗi bộ gõ)*:
   ```python
   print("Nhom thuc hanh: [Ghi ten 2 ban]")
   print("Lop: 10... - Mon: Tin hoc")
   print("Chu vi:", (12 + 5) * 2, "| Dien tich:", 12 * 5)
   ```
3. Chọn **`File → Save`** (`Ctrl + S`), lưu vào thư mục `D:\Tin10\Bai16\bai16_th1.py`.
4. Chọn **`Run → Run Module`** (nhấn **`F5`**) và ghi lại kết quả dòng 3: ..........................................

**Nhiệm vụ C – "Săn 3 lỗi cú pháp" (`SyntaxError` / `NameError`):**  
Chỉ ra lỗi sai ở mỗi dòng lệnh dưới đây và viết lại cho đúng:

| Dòng lệnh bị lỗi | Nguyên nhân lỗi | Viết lại đúng cú pháp Python 3 |
|---|---|---|
| `Print("Xin chao")` | | |
| `print("Tin hoc 10)` | | |
| `print(10 + 5 * 2` | | |

---

### PHẦN 3: NHIỆM VỤ NÂNG CAO (DÀNH CHO CẶP HOÀN THÀNH SỚM)
1. Tạo tệp `bai16_nangcao.py` trong Script Mode, dùng các lệnh `print(...)` và phép tính số học trực tiếp *(không dùng biến)* để in khung bảng hóa đơn gọn đẹp cho 3 món đồ dùng học tập:
   - `4` quyển vở × `12000`đ | `3` cây bút × `5000`đ | `1` bộ thước × `18000`đ | **Tổng số tiền phải trả**.
2. Thử gõ `print(10 / 0)` trên IDLE Shell và ghi lại tên lỗi máy báo: ...........................................

---

### PHẦN 4: VẬN DỤNG – DỰ TOÁN TRANG TRÍ LỚP 10 (`bai16_vandung.py`)
Lớp 10 cần mua: **2 cuộn giấy màu** (`25000`đ/cuộn), **5 cây bút dạ** (`8000`đ/cây), **1 cuộn băng keo** (`15000`đ).
- **Mức Cơ bản:** Viết tệp `bai16_vandung.py` in chi phí từng món, **Tổng chi phí** và **Số tiền mỗi tổ góp** (chia đều 4 tổ).
- **Mức Nâng cao:** In thêm **Số tiền còn dư** nếu quỹ lớp có `150000`đ.

*(Khung dự phòng khi mất điện / thiếu máy: Học sinh viết trực tiếp các dòng lệnh `print(...)` của `bai16_vandung.py` và dự đoán kết quả màn hình vào phần trống bên dưới để giáo viên chấm tương đương.)*

- **Mã lệnh dự kiến:**
  .......................................................................................................................................................
  .......................................................................................................................................................
  .......................................................................................................................................................
- **Kết quả dự kiến:** Tổng chi phí = .................... đ | Mỗi tổ góp = .................... đ | Còn dư = .................... đ.
