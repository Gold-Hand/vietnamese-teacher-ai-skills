# Knowledge Base – Vietnamese Teacher AI Skills (V2.0 Draft Infrastructure)

Thư mục này lưu trữ kho tri thức thực tế có kiểm chứng (*Evidence-Based Teaching Knowledge Base*) phục vụ cả 9 Agent Skills.

## Cấu trúc 6 nhóm tri thức

| Thư mục | Loại tài liệu | Mức độ tin cậy mặc định | Nguyên tắc sử dụng |
|---|---|---|---|
| `01_legal/` | Văn bản pháp lý, thông tư, công văn của Bộ GDĐT / Sở GDĐT / nhà trường | **Cấp 1 – Pháp lý chính thức** | Ưu tiên cao nhất cho yêu cầu pháp lý, biểu mẫu, đánh giá, khung năng lực số. Không suy diễn từ tài liệu mẫu. |
| `02_curriculum/` | Chương trình GDPT 2018, phân phối chương trình (PPCT), tài liệu SGK/SGV chính thức | **Cấp 2 – Chương trình / Học liệu chuẩn** | Căn cứ xác định yêu cầu cần đạt (YCCĐ), phạm vi kiến thức đúng khối lớp và bộ sách. |
| `03_practical-khbd/` | Kế hoạch bài dạy (KHBD) mẫu thực chiến tách thành **2 kho độc lập**: `01_TIN_HOC/` (Tin học 10–12) và `02_TRI_TUE_NHAN_TAO_AI/` (Trí tuệ nhân tạo 10–12), kèm vùng chờ `_staging/` | **Cấp 4 – Thực chiến tham khảo** | Tham khảo tổ chức hoạt động đúng môn qua `../KHBD_INDEX.md`; **không trộn lẫn Tin học và AI**, **không coi là chuẩn pháp lý áp dụng chung**, không khai thác tài liệu chưa xác nhận trong `_staging/`. |
| `04_assessment/` | Ma trận, bản đặc tả, đề kiểm tra, rubric, ngân hàng câu hỏi thực tế | **Cấp 3 – Chuyên môn đánh giá** | Tham khảo cấu trúc câu hỏi, thang điểm, tiêu chí chấm theo môn/khối lớp cụ thể. |
| `05_teaching-materials/` | Phiếu học tập, slide mẫu, mã nguồn lab, dữ liệu thực hành | **Cấp 4 – Học liệu dạy học** | Khai thác ví dụ, bài tập thực hành và ý tưởng trực quan hóa bài giảng. |
| `06_reference-analysis/` | Bản phân tích tri thức Markdown do pipeline tạo ra từ tài liệu gốc (không sửa tài liệu gốc) | **Bản trích xuất dẫn xuất** | Luôn gắn liên kết về đường dẫn tài liệu gốc trong `KNOWLEDGE_INDEX.md` để bảo đảm khả năng truy xuất. |

> **Trạng thái hiện tại:** Hạ tầng trống (gồm 2 kho KHBD độc lập `01_TIN_HOC/` và `02_TRI_TUE_NHAN_TAO_AI/`), sẵn sàng tiếp nhận tài liệu thực tế do người dùng cung cấp theo từng đợt. Không tạo dữ liệu giả thay thế tài liệu thực tế. Xem sổ quản lý tập trung tại `../KNOWLEDGE_INDEX.md`, sổ quản lý hai kho KHBD tại `../KHBD_INDEX.md` và hướng dẫn nạp tại `../KNOWLEDGE_INGESTION_GUIDE.md`.
