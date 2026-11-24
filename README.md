# Vietnamese Teacher AI Skills

**Bộ Gemini CLI Agent Skills hỗ trợ giáo viên Việt Nam — trọng tâm Tin học THPT và giáo dục AI.**

- Phiên bản: `1.0.0`
- Ngôn ngữ mặc định: Tiếng Việt
- Định dạng: Agent Skills với `SKILL.md`
- Nền tảng mục tiêu: Gemini CLI
- Giấy phép: MIT

## 1. Bộ kỹ năng

| Skill | Chức năng |
|---|---|
| `lesson-planner` | Thiết kế kế hoạch bài dạy, hoạt động học tập, phân hóa |
| `curriculum-analyzer` | Phân tích chương trình, SGK, yêu cầu cần đạt |
| `informatics-expert` | Tin học THPT: thuật toán, lập trình, dữ liệu, mạng, an toàn số |
| `ai-education` | Dạy học AI, AI literacy, hoạt động và dự án AI cho học sinh |
| `slide-designer` | Kịch bản slide, cấu trúc trình chiếu, nội dung và chỉ dẫn thiết kế |
| `ai-video-creator` | Kịch bản video, storyboard, prompt tạo video và lời dẫn |
| `assessment-generator` | Ma trận, đặc tả, câu hỏi, đề, đáp án và rubric |
| `digital-competency` | Tích hợp năng lực số vào mục tiêu và hoạt động dạy học |
| `teaching-assistant` | Chủ nhiệm, tình huống sư phạm, phối hợp phụ huynh và công việc giáo viên |

## 2. Cài đặt

### Cài từng Skill từ GitHub

Repository chứa nhiều Skill trong `.agents/skills/`. Dùng `--path` để chỉ rõ thư mục Skill cần cài. Ví dụ:

```bash
gemini skills install https://github.com/<YOUR-ORG>/vietnamese-teacher-ai-skills --path .agents/skills/lesson-planner
gemini skills install https://github.com/<YOUR-ORG>/vietnamese-teacher-ai-skills --path .agents/skills/ai-education
gemini skills install https://github.com/<YOUR-ORG>/vietnamese-teacher-ai-skills --path .agents/skills/informatics-expert
```

Lặp lại với các thư mục Skill còn lại. Thêm `--scope workspace` nếu chỉ muốn cài trong dự án hiện tại:

```bash
gemini skills install https://github.com/<YOUR-ORG>/vietnamese-teacher-ai-skills --path .agents/skills/lesson-planner --scope workspace
```

Gemini CLI có thể hỏi xác nhận nguồn cài đặt. Hãy kiểm tra repository và nội dung trước khi chấp thuận.

### Dùng trực tiếp khi phát triển

Clone repository:

```bash
git clone https://github.com/<YOUR-ORG>/vietnamese-teacher-ai-skills.git
cd vietnamese-teacher-ai-skills
gemini skills link . --scope user
```

Hoặc sao chép thư mục `.agents/skills/` vào thư mục dự án của bạn. Gemini CLI nhận diện `.agents/skills/` và `.gemini/skills/`.

## 3. Kiểm tra

Trong Gemini CLI:

```text
/skills list
```

Sau khi thêm hoặc sửa Skill:

```text
/skills reload
```

Chạy kiểm tra cấu trúc bằng Python:

```bash
python scripts/validate_skills.py
```

## 4. Ví dụ yêu cầu

- "Phân tích Bài 1 Tin học 10 bộ Kết nối tri thức và xác định điểm khó."
- "Soạn kế hoạch bài dạy theo Công văn 5512 cho chủ đề dữ liệu và thông tin."
- "Thiết kế hoạt động 2 tiết giúp học sinh lớp 10 hiểu AI học từ dữ liệu như thế nào."
- "Tạo ma trận và đề kiểm tra 45 phút về thuật toán tìm kiếm."
- "Viết storyboard video 60 giây, chia cảnh 10 giây, giữ nhân vật nhất quán."
- "Tích hợp năng lực số vào hoạt động học tập này."

## 5. Nguyên tắc quan trọng

1. Skill là hướng dẫn chuyên môn, không thay thế văn bản chính thức hoặc quyết định của nhà trường.
2. Không tự tạo số hiệu, ngày ban hành, điều khoản hoặc trích dẫn văn bản pháp luật.
3. Khi cần quy định hiện hành, tra cứu nguồn chính thức và ghi ngày kiểm tra.
4. Không giả định một bộ SGK nếu người dùng chưa nêu. Hỏi hoặc nêu rõ giả định.
5. Phân biệt nội dung chính thức, đề xuất sư phạm và ví dụ minh họa.
6. Bảo vệ dữ liệu cá nhân của học sinh; không đưa thông tin định danh lên dịch vụ AI khi chưa được phép.
7. Kiểm tra tính chính xác chuyên môn, độ tuổi phù hợp, khả năng tiếp cận và tính khả thi trong lớp học.

## 6. Cấu trúc

```text
.agents/skills/
  lesson-planner/SKILL.md
  curriculum-analyzer/SKILL.md
  informatics-expert/SKILL.md
  ai-education/SKILL.md
  slide-designer/SKILL.md
  ai-video-creator/SKILL.md
  assessment-generator/SKILL.md
  digital-competency/SKILL.md
  teaching-assistant/SKILL.md
references/
  vietnam-education-guidance.md
  lesson-plan-template.md
  assessment-template.md
  ai-literacy-framework.md
scripts/
  validate_skills.py
```

## 7. Lộ trình phát triển

- v1.0: 9 kỹ năng nền tảng, quy tắc an toàn, mẫu đầu ra, script kiểm tra.
- v1.1: Bổ sung ví dụ theo từng bộ SGK Tin học THPT và ngân hàng hoạt động.
- v1.2: Thêm công cụ kiểm tra cấu trúc đề, rubric và xuất tài liệu.
- v2.0: Tích hợp quy trình làm việc với tài liệu, slide và hệ thống quản lý học tập.

## 8. Đóng góp

Mở issue hoặc pull request. Khi bổ sung tài liệu pháp lý, cần ghi tên văn bản, cơ quan ban hành, ngày ban hành, đường dẫn nguồn chính thức và ngày truy cập.
