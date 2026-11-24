# KHBD INDEX – SỔ QUẢN LÝ KHO KẾ HOẠCH BÀI DẠY TIN HỌC & TRÍ TUỆ NHÂN TẠO (V2.0)

> **Trạng thái:** `Khởi tạo hạ tầng 2 kho KHBD độc lập (Chưa phát hành V2.0 chính thức)`  
> **Cập nhật lần cuối:** 24/11/2026  
> **Sổ tổng hợp cấp hệ thống:** `KNOWLEDGE_INDEX.md`  
> **Quy trình tiếp nhận & phân loại:** `KNOWLEDGE_INGESTION_GUIDE.md`

---

## Nguyên tắc quản trị hai kho KHBD độc lập

1. **Tách biệt tuyệt đối hai môn/lĩnh vực:**
   - **Kho 01 – Tin học:** `knowledge-base/03_practical-khbd/01_TIN_HOC/`
   - **Kho 02 – Trí tuệ nhân tạo (AI):** `knowledge-base/03_practical-khbd/02_TRI_TUE_NHAN_TAO_AI/`
2. **Mức độ tin cậy mặc định:** **T4 – Thực chiến tham khảo**. Không tự suy diễn quy định pháp lý (T1) hay mặc định là yêu cầu cần đạt chính thức của chương trình GDPT (T2) nếu không có văn bản tương ứng trong `knowledge-base/01_legal/` và `knowledge-base/02_curriculum/`.
3. **Không trộn lẫn phương pháp dạy học:** Không áp đặt máy móc phương pháp dạy Tin học cho giáo dục AI, và không dùng tài liệu AI thay thế nội dung chương trình Tin học. Chỉ kết hợp hai kho khi người dùng yêu cầu bài học **liên môn / tích hợp** và phải ghi rõ nguồn từng phần.
4. **Cơ chế xác nhận trước khi đưa vào kho chính thức:** Mọi tài liệu mới tiếp nhận chưa được người dùng xác nhận phân loại và vị trí lưu chỉ nằm ở `knowledge-base/03_practical-khbd/_staging/` và **chưa được phép khai thác chính thức**.
5. **Quy ước mã `ID tài liệu`:**
   - Kho Tin học: `KHBD-TH-<Khối/BP>-<STT>` (ví dụ: `KHBD-TH-10-001`, `KHBD-TH-11-002`, `KHBD-TH-BP-001`).
   - Kho Trí tuệ nhân tạo: `KHBD-AI-<Khối/BP>-<STT>` (ví dụ: `KHBD-AI-10-001`, `KHBD-AI-12-001`, `KHBD-AI-BP-001`).

---

## 1. Kho KHBD Tin học (`knowledge-base/03_practical-khbd/01_TIN_HOC/`)

**Cấu trúc tổ chức:** `khoi-10/`, `khoi-11/`, `khoi-12/` (`bo-sach/`, `chu-de/`, `bai-thuc-hanh/`, `du-an-stem/`, `khbd-mau-thuc-chien/`) và `best-practices/`.

| ID tài liệu | Tên bài học | Môn học | Khối lớp | Bộ sách hoặc chương trình | Chủ đề | Loại tài liệu | Nguồn | Ngày cập nhật | Đường dẫn | Skill có thể sử dụng |
|---|---|---|---|---|---|---|---|---|---|---|
| *(Chưa có tài liệu thực tế được xác nhận — chờ tiếp nhận Đợt 1)* | — | Tin học | — | — | — | — | — | — | — | `lesson-planner`, `informatics-expert`, `curriculum-analyzer`, `assessment-generator`, `slide-designer` |

---

## 2. Kho KHBD Trí tuệ nhân tạo – AI (`knowledge-base/03_practical-khbd/02_TRI_TUE_NHAN_TAO_AI/`)

**Cấu trúc tổ chức:** `khoi-10/`, `khoi-11/`, `khoi-12/` (`chu-de-ai/`, `thuc-hanh-ai/`, `du-an-ai/`, `ung-dung-ai/`, `dao-duc-va-trach-nhiem-ai/`, `khbd-mau-thuc-chien/`) và `best-practices/`.

| ID tài liệu | Tên bài học | Môn học | Khối lớp | Bộ sách hoặc chương trình | Chủ đề | Loại tài liệu | Nguồn | Ngày cập nhật | Đường dẫn | Skill có thể sử dụng |
|---|---|---|---|---|---|---|---|---|---|---|
| *(Chưa có tài liệu thực tế được xác nhận — chờ tiếp nhận Đợt 1)* | — | Trí tuệ nhân tạo (AI) | — | — | — | — | — | — | — | `lesson-planner`, `ai-education`, `curriculum-analyzer`, `digital-competency`, `slide-designer` |

---

## 3. Vùng chờ xác nhận – Staging (`knowledge-base/03_practical-khbd/_staging/`)

> Tài liệu tại đây đang chờ giáo viên xác nhận môn học, loại tài liệu và vị trí lưu đề xuất trước khi chuyển vào kho chính thức và đồng bộ lên `KNOWLEDGE_INDEX.md`.

| Mã tạm | Tên tệp gốc | Nhận diện môn học đề xuất | Vị trí lưu đề xuất | Trạng thái xác nhận | Đường dẫn tạm |
|---|---|---|---|---|---|
| *(Trống)* | — | — | — | — | — |
