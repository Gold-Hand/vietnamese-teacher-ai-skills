---
name: assessment-generator
description: Xây dựng ma trận, bản đặc tả, đề kiểm tra, câu hỏi trắc nghiệm/tự luận/thực hành, đáp án, hướng dẫn chấm và rubric cho giáo dục phổ thông Việt Nam. Dùng khi người dùng yêu cầu ra đề, ôn tập, ngân hàng câu hỏi, kiểm tra thường xuyên hoặc định kỳ.
---

# Assessment Generator

## Tài liệu tham chiếu bắt buộc

- Đọc mẫu `../../../references/assessment-template.md` và đối chiếu mục *Đánh giá* trong `../../../references/vietnam-education-guidance.md` trước khi thiết kế ma trận và đề kiểm tra.

## Cơ chế xác định phạm vi & Kiểm soát đúng khối lớp

Trước khi lập ma trận hoặc viết bất kỳ câu hỏi nào, phải xác định rõ:
1. **Lớp, môn học, bộ SGK (hoặc tài liệu trường dùng), chủ đề và phạm vi kiến thức/kỹ năng đã học.**
2. **Kiểm tra độ khớp khối lớp theo Chương trình GDPT 2018:**
   - **Không đưa kiến thức lớp 11 (hoặc khối lớp khác) vào đề kiểm tra lớp 10 nếu người dùng không yêu cầu rõ.**
   - Nếu yêu cầu của người dùng có nội dung thường thuộc khối lớp khác theo Chương trình GDPT 2018 (ví dụ: cài đặt thuật toán tìm kiếm nhị phân và sắp xếp cơ bản bằng Python thường thuộc **Tin học 11 – định hướng Khoa học máy tính** thay vì lõi bắt buộc của **Tin học 10**, trong khi Tin học 10 học lập trình cơ bản với `list`, vòng lặp, hàm), **phải cảnh báo rõ ràng ngay tại Mục 1 (Căn cứ và phạm vi)**, phân biệt giữa nội dung chương trình chuẩn và nội dung theo yêu cầu/phân phối riêng của trường; không âm thầm đưa thêm kiến thức ngoài phạm vi lớp học (như đệ quy, độ phức tạp Big-O hình thức, cấu trúc dữ liệu nâng cao) nếu chưa được yêu cầu.

## Quy trình

1. Đọc `../../../references/assessment-template.md` và `../../../references/vietnam-education-guidance.md`.
2. Xác định lớp, môn, bộ sách, chủ đề, phạm vi đã học, thời lượng, hình thức, thang điểm và quy định áp dụng; rà soát độ khớp khối lớp.
3. Thu thập và đối chiếu **yêu cầu cần đạt (YCCĐ)** của chương trình; ưu tiên tài liệu người dùng cung cấp. Mọi câu hỏi trong đề phải ánh xạ được tới một YCCĐ cụ thể.
4. Xây dựng **ma trận đề** tương ứng chặt chẽ với nội dung kiểm tra và **bản đặc tả** trước khi viết câu hỏi.
5. Phân loại câu hỏi theo **mức độ nhận thức** (Nhận biết, Thông hiểu, Vận dụng — hoặc thêm Vận dụng cao nếu người dùng yêu cầu); phân bổ nội dung và điểm hợp lý, nêu rõ giả định nếu người dùng chưa chỉ định tỷ lệ.
6. **Kiểm soát chặt chẽ thời lượng làm bài:** Ước lượng thời gian làm bài thực tế cho từng phần (trắc nghiệm, tự luận, thực hành lập trình trên máy) phù hợp học sinh đại trà. Trong đề 45 phút có cả lý thuyết và thực hành lập trình, giữ tải lượng vừa sức (ví dụ giới hạn số câu chạy tay dài và số hàm phải tự cài đặt từ đầu trong phần thực hành để học sinh kịp viết, chạy thử và gỡ lỗi trong quỹ thời gian thực tế).
7. Viết câu hỏi đúng trình độ, rõ lệnh, không đánh đố, đối chiếu khớp 1–1 với ma trận và bản đặc tả.
8. Tạo đáp án và hướng dẫn chấm chi tiết; câu thực hành cần tiêu chí sản phẩm và quy trình.
9. **Kiểm tra tính chính xác của đáp án và lời giải:** Tự giải thử/chạy tay từng câu; với câu lập trình, nếu có môi trường thực thi an toàn thì chạy kiểm thử mã nguồn đáp án trên các ví dụ và trường hợp biên (nếu chưa thực thi, ghi rõ). Rà soát lại tổng điểm, độ phủ YCCĐ, phân bố mức độ nhận thức và thời lượng.

## Quy tắc câu hỏi

- Trắc nghiệm một lựa chọn: chỉ có một phương án tốt nhất.
- Phương án nhiễu phải hợp lý nhưng không gây tranh cãi.
- Không dùng "tất cả đều đúng" nếu làm giảm chất lượng đánh giá.
- Với câu lập trình, xác định rõ ngôn ngữ, phiên bản, phạm vi cú pháp đã học, input/output và ràng buộc.
- Với câu thực hành, đánh giá cả kết quả (sản phẩm) và kỹ năng/quy trình khi phù hợp.
- Phân biệt rõ câu hỏi kiểm tra ghi nhớ (Nhận biết) với câu yêu cầu giải thích/mô phỏng (Thông hiểu) và giải quyết bài toán (Vận dụng).
- Đối chiếu mỗi câu hỏi với YCCĐ tương ứng trong Bản đặc tả; loại bỏ câu ngoài phạm vi đã học.

## Đầu ra

1. Căn cứ, phạm vi, giả định & lưu ý độ khớp chương trình/khối lớp *(kèm ước lượng thời lượng từng phần)*.
2. Ma trận đề kiểm tra *(khớp 100% số câu, mức độ nhận thức và tổng điểm)*.
3. Bản đặc tả *(đối chiếu từng câu hỏi với YCCĐ)*.
4. Đề kiểm tra.
5. Đáp án và giải thích/lời giải đã kiểm chứng.
6. Hướng dẫn chấm và rubric *(sản phẩm + quy trình cho câu thực hành)*.
7. Bảng tự kiểm chất lượng *(độ phủ YCCĐ, đúng khối lớp, thời lượng khả thi, tổng điểm, kiểm chứng đáp án)*.

Dùng mẫu `../../../references/assessment-template.md`. Không tuyên bố đề phù hợp quy định hiện hành nếu chưa kiểm tra văn bản áp dụng.

## Hướng dẫn sử dụng & Ví dụ thực tế

- **Cách dùng hiệu quả:** Nêu rõ *lớp, môn, bộ SGK, phạm vi kiến thức/cú pháp đã học, thời lượng, hình thức (trắc nghiệm/tự luận/thực hành)* và tỷ lệ mức độ nhận thức của trường (nếu đã chốt).
- **Ví dụ yêu cầu thực tế:**
  - *"Lập ma trận, bản đặc tả và đề kiểm tra 45 phút Tin học 10 (bộ Kết nối tri thức) về danh sách (`list`), vòng lặp và hàm cơ bản trong Python 3; tỷ lệ 40% Nhận biết – 30% Thông hiểu – 30% Vận dụng; có 1 câu thực hành vừa sức 15–18 phút."*
  - *"Thiết kế đề kiểm tra 45 phút Tin học 11 (định hướng KHMT) về tìm kiếm tuần tự, tìm kiếm nhị phân và sắp xếp chọn kèm rubric chấm bài thực hành Python 3."*

## Xuất tài liệu Office (Dùng chung Office Generator)

- Khi người dùng yêu cầu xuất tệp Word (đề kiểm tra, ma trận, đáp án) hoặc slide câu hỏi PowerPoint, chỉ gọi công cụ **sau khi đã có nội dung Markdown nguồn hợp lệ** (nếu người dùng chỉ yêu cầu Markdown thì không tự ý tạo tệp Office):
  ```bash
  python scripts/office_generator/cli.py docx --input <de_kiem_tra.md> --output <de_kiem_tra.docx> --template exam
  python scripts/office_generator/cli.py docx --input <ma_tran.md> --output <ma_tran.docx> --template matrix
  python scripts/office_generator/cli.py docx --input <dap_an.md> --output <dap_an.docx> --template answer_key
  python scripts/office_generator/cli.py pptx --input <slide_cau_hoi.md> --output <slide_cau_hoi.pptx> --template assessment
  ```
- Luôn kiểm định tệp đầu ra bằng `python scripts/office_generator/cli.py validate --input <output> --source <source.md>`.
