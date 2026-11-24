"""Tests for DOCX generation (Groups 1, 3, 4, 7, 8, 9)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from docx import Document
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.office_generator import generate_document, run_batch  # noqa: E402
from scripts.office_generator.cli import main as cli_main  # noqa: E402


class TestDocxGenerator(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_group1_3_4_7_markdown_to_docx_tables_lists_images_vietnamese(self):
        # Create a real temporary PNG image
        img_file = self.tmp_dir / "minh_hoa.png"
        Image.new("RGB", (320, 180), color=(29, 78, 216)).save(img_file)

        src_md = self.tmp_dir / "khbd_mau.md"
        src_md.write_text(
            """# KẾ HOẠCH BÀI DẠY TIN HỌC 10

> Tài liệu tham khảo theo hướng dẫn Công văn 5512.

## I. MỤC TIÊU
- Phân biệt **ngôn ngữ lập trình bậc cao** và *ngôn ngữ máy*.
  - Biết vai trò chương trình dịch.
1. Khởi động bằng tình huống thực tế.
2. Thực hành chạy lệnh `print("Xin chào Việt Nam")`.

![Minh họa giao diện Python](minh_hoa.png)

## II. TIẾN TRÌNH DẠY HỌC

| Hoạt động | Mục tiêu | Thời lượng |
|---|---|---|
| Khởi động | Tạo hứng thú | 5 phút |
| Thực hành | Chạy chương trình đầu tiên | 20 phút |
*Bảng 1. Tóm tắt tiến trình*

<!-- pagebreak -->

## III. MÃ MINH HỌA
```python
print("Tổng =", 15 + 25)
```
""",
            encoding="utf-8",
        )

        out_docx = self.tmp_dir / "khbd_mau.docx"
        res = generate_document(
            source_file=src_md,
            output_file=out_docx,
            format="docx",
            template="khbd",
            overrides={"school_name": "Trường THPT Kiểm Thử", "teacher_name": "Nguyễn Văn A"},
        )
        self.assertTrue(res.success, res.error_message)
        self.assertIsNotNone(res.validation)
        self.assertTrue(res.validation.passed)

        doc = Document(str(out_docx))
        self.assertAlmostEqual(doc.sections[0].page_width.cm, 21.0, delta=0.1)
        self.assertAlmostEqual(doc.sections[0].page_height.cm, 29.7, delta=0.1)
        self.assertEqual(doc.styles["Normal"].font.name, "Times New Roman")
        # 1 optional institution header table + 1 content table = 2 tables
        self.assertGreaterEqual(len(doc.tables), 2)
        self.assertGreaterEqual(len(doc.inline_shapes), 1)
        full_text = "\n".join(p.text for p in doc.paragraphs)
        self.assertIn("KẾ HOẠCH BÀI DẠY TIN HỌC 10", full_text)
        self.assertIn("ngôn ngữ lập trình bậc cao", full_text)
        self.assertIn("Bảng 1. Tóm tắt tiến trình", full_text)

    def test_all_vietnamese_docx_templates(self):
        src_md = self.tmp_dir / "sample.md"
        src_md.write_text("# Đề kiểm tra Tin học 10\n\n## Phần I\n- Câu hỏi tiếng Việt có dấu.\n", encoding="utf-8")
        for tmpl in ("khbd", "exam", "matrix", "answer_key", "study_material", "teacher_guide", "general"):
            out = self.tmp_dir / f"out_{tmpl}.docx"
            res = generate_document(src_md, out, format="docx", template=tmpl)
            self.assertTrue(res.success, f"Template {tmpl} failed: {res.error_message}")
            self.assertTrue(out.is_file())

    def test_group8_missing_source_file_returns_controlled_error(self):
        res = generate_document(
            source_file=self.tmp_dir / "khong_ton_tai.md",
            output_file=self.tmp_dir / "out.docx",
            format="docx",
            template="khbd",
        )
        self.assertFalse(res.success)
        self.assertIn("Không tìm thấy", res.error_message)

    def test_group9_batch_generation_via_cli(self):
        md1 = self.tmp_dir / "doc1.md"
        md1.write_text("# Tài liệu 1\n\n- Nội dung tiếng Việt 1.\n", encoding="utf-8")
        md_slides = self.tmp_dir / "slides.md"
        md_slides.write_text(
            "# Slide Batch\n\n## Slide 1: Mở đầu\nLayout: title_slide\n- Mục tiêu 1\nNotes: Ghi chú 1\n",
            encoding="utf-8",
        )
        batch_cfg = self.tmp_dir / "batch.json"
        out_doc = self.tmp_dir / "batch_doc.docx"
        out_ppt = self.tmp_dir / "batch_ppt.pptx"
        out_rep = self.tmp_dir / "batch_report.md"
        batch_cfg.write_text(
            json.dumps(
                {
                    "report_file": str(out_rep),
                    "jobs": [
                        {"input": str(md1), "output": str(out_doc), "format": "docx", "template": "study_material"},
                        {"input": str(md_slides), "output": str(out_ppt), "format": "pptx", "template": "lesson"},
                    ],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        rc = cli_main(["batch", "--config", str(batch_cfg)])
        self.assertEqual(rc, 0)
        self.assertTrue(out_doc.is_file())
        self.assertTrue(out_ppt.is_file())
        self.assertTrue(out_rep.is_file())
        self.assertIn("PASS", out_rep.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
