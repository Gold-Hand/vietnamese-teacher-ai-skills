# KNOWLEDGE INDEX – SỔ QUẢN LÝ TRI THỨC (V2.0)

> **Trạng thái:** `Chuẩn bị hạ tầng (Chưa phát hành V2.0 chính thức)`  
> **Cập nhật lần cuối:** 24/11/2026  
> **Quy tắc bắt buộc:** Mọi tài liệu trong `knowledge-base/` phải được đăng ký đầy đủ 12 trường dưới đây trước khi các Agent Skills khai thác. Không tự tạo tài liệu giả khi chưa có nguồn thực tế được cung cấp.

---

## 1. Thang mức độ tin cậy & Thứ tự ưu tiên khai thác

| Mức độ tin cậy | Nhóm thư mục | Ý nghĩa & Quy tắc ưu tiên |
|---|---|---|
| **T1 – Pháp lý chính thức** | `01_legal/` | Văn bản quy phạm/hướng dẫn chính thức của cơ quan quản lý hoặc nhà trường. **Ưu tiên số 1** cho mọi câu hỏi về quy định, biểu mẫu, kiểm tra đánh giá, khung năng lực số. |
| **T2 – Chương trình chuẩn** | `02_curriculum/` | Chương trình GDPT 2018, PPCT chính thức, SGK/SGV đúng bộ sách. **Ưu tiên số 1** cho YCCĐ, phân bổ thời lượng và phạm vi khối lớp. |
| **T3 – Chuyên môn đánh giá** | `04_assessment/` | Ma trận, đặc tả, đề kiểm tra, rubric đã thẩm định từ tổ chuyên môn/nhà trường. |
| **T4 – Thực chiến tham khảo** | `03_practical-khbd/` (`01_TIN_HOC/`, `02_TRI_TUE_NHAN_TAO_AI/`), `05_teaching-materials/` | KHBD mẫu thực chiến (tách riêng kho **Tin học** và kho **Trí tuệ nhân tạo – AI**, quản lý chi tiết tại `KHBD_INDEX.md`), slide, phiếu học tập, lab của giáo viên. **Ưu tiên tham khảo** thiết kế hoạt động sư phạm đúng môn; **không trộn lẫn phương pháp Tin học và AI**, **tuyệt đối không dùng để suy diễn quy định pháp lý hay áp đặt chuẩn chung**. Tài liệu chưa xác nhận chỉ nằm ở `03_practical-khbd/_staging/` và chưa được khai thác. |
| **T5 – Phân tích dẫn xuất** | `06_reference-analysis/` | Bản phân tích Markdown sinh bởi pipeline từ tài liệu gốc (mọi trích dẫn phải truy ngược được về tài liệu gốc và vị trí mục/trang). |

---

## 2. Danh mục tài liệu trong Knowledge Base

> **Chỉ mục chuyên biệt cho hai kho KHBD (`01_TIN_HOC/` & `02_TRI_TUE_NHAN_TAO_AI/`):** Xem và cập nhật đồng bộ tại [`KHBD_INDEX.md`](KHBD_INDEX.md).

| Tên tài liệu | Đường dẫn | Loại tài liệu | Môn học | Cấp học | Khối lớp | Bộ sách | Chủ đề | Nguồn cung cấp | Ngày cập nhật | Mức độ tin cậy | Các Skill được phép khai thác |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(Chưa có tài liệu thực tế nào được nạp — đang chờ người dùng cung cấp Đợt 1)* | — | — | — | — | — | — | — | — | — | — | — |

---

## 3. Tài liệu nguyên tắc nền tảng sẵn có từ V1.2 (`references/` – giữ nguyên không thay thế)

Các tệp dưới đây là nguyên tắc làm việc và khung mẫu tham khảo cấp repository của V1.2 (không phải văn bản pháp lý hay SGK gốc):

| Tên tài liệu | Đường dẫn | Loại tài liệu | Vai trò |
|---|---|---|---|
| Hướng dẫn tham chiếu giáo dục Việt Nam | `references/vietnam-education-guidance.md` | Nguyên tắc làm việc nội bộ | Quy tắc kiểm chứng văn bản pháp lý, SGK, đánh giá, năng lực số |
| Khung kế hoạch bài dạy tham khảo | `references/lesson-plan-template.md` | Khung mẫu tham khảo | Cấu trúc mẫu KHBD cho `lesson-planner` |
| Mẫu thiết kế kiểm tra đánh giá | `references/assessment-template.md` | Khung mẫu tham khảo | Cấu trúc mẫu ma trận/đặc tả/đề cho `assessment-generator` |
| Khung thiết kế giáo dục AI THPT | `references/ai-literacy-framework.md` | Khung sư phạm gợi ý | Khung mạch nội dung & an toàn cho `ai-education` |
