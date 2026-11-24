"""Tests for PPTX generation (Groups 2, 5, 6, 7, 8 & all 13 layouts)."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image
from pptx import Presentation

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.office_generator import SlideDeck, SlideModel, generate_document  # noqa: E402


class TestPptxGenerator(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_group2_5_6_7_all_13_layouts_images_python_code_vietnamese(self):
        img_file = self.tmp_dir / "python_demo.png"
        Image.new("RGB", (640, 360), color=(13, 148, 136)).save(img_file)

        slides = [
            SlideModel(1, "BÀI 16: NGÔN NGỮ PYTHON", layout="title_slide", display_raw="• Tin học 10\n1. Mục tiêu 1\n2. Mục tiêu 2", speaker_notes="Chào lớp."),
            SlideModel(2, "Phần 1: Tổng quan", layout="section_divider", content_lines=["Giới thiệu ngôn ngữ lập trình"], speaker_notes="Chuyển phần."),
            SlideModel(3, "Giao diện IDLE có hình ảnh", layout="text_image", content_lines=["Môi trường chuẩn Python 3"], image_path=str(img_file), image_caption="Hình minh họa IDLE", speaker_notes="Chỉ rõ thanh menu."),
            SlideModel(4, "Thực hành 2 cột", layout="two_columns", display_raw="Nhiệm vụ cơ bản\nYêu cầu:\nChạy lệnh print()", speaker_notes="Chia cặp 2 HS/máy."),
            SlideModel(5, "So sánh 3 loại ngôn ngữ", layout="comparison", display_raw="• Ngôn ngữ máy: 0 và 1\n• Hợp ngữ: MOV, ADD\n• Bậc cao: print(5+3)", speaker_notes="So sánh độ dễ học."),
            SlideModel(6, "Tiến trình phát triển", layout="timeline", content_lines=["1950: Ngôn ngữ máy", "1960: Hợp ngữ", "1991: Python ra đời", "Hiện nay: AI & Data"], speaker_notes="Tóm tắt lịch sử."),
            SlideModel(7, "Quy trình 4 bước", layout="process", display_raw="1. Mở New File\n2. Viết lệnh\n3. Lưu .py\n4. Nhấn F5", speaker_notes="Thao tác chậm rãi."),
            SlideModel(8, "Sơ đồ chương trình dịch", layout="diagram", display_raw="Chuyển mã bậc cao sang mã máy.", speaker_notes="Giải thích phiên dịch."),
            SlideModel(9, "Bảng so sánh 2 chế độ", layout="table", table_rows=[["Tiêu chí", "Shell", "Script"], ["Lưu tệp", "Không", "Có (.py)"]], speaker_notes="Nhấn mạnh đuôi .py."),
            SlideModel(10, "Ví dụ mã Python", layout="code_example", code_lines=['print("Xin chào lớp 10!")', "print(15 + 25)"], content_lines=["Chạy bằng phím F5"], speaker_notes="Chạy demo."),
            SlideModel(11, "Kiểm tra nhanh", layout="quiz", display_raw="**Câu 1:** Đuôi tệp Python là gì?\n**A.** .txt **B.** .py **C.** .doc **D.** .jpg", speaker_notes="Đáp án đúng: B."),
            SlideModel(12, "Tổng kết kiến thức", layout="summary", display_raw="1. NNLT bậc cao\n2. Python ngắn gọn\n3. Hai chế độ IDLE", speaker_notes="Chốt bài."),
            SlideModel(13, "Cảm ơn và Hỏi đáp", layout="closing", content_lines=["Hẹn gặp lại ở Bài 17: Biến và lệnh gán!"], speaker_notes="Kết thúc tiết học."),
        ]
        deck = SlideDeck(title="Kiểm thử 13 bố cục", subtitle="Tin học 10 – Python", slides=slides)
        out_pptx = self.tmp_dir / "all_13_layouts.pptx"
        notes_md = self.tmp_dir / "Speaker_Notes_13.md"

        res = generate_document(
            output_file=out_pptx,
            format="pptx",
            template="education",
            slide_deck=deck,
            speaker_notes_file=notes_md,
        )
        self.assertTrue(res.success, res.error_message)
        self.assertEqual(len(res.layouts_used), 13)
        self.assertTrue(res.speaker_notes_embedded)
        self.assertTrue(notes_md.is_file())
        self.assertIsNotNone(res.validation)
        self.assertTrue(res.validation.passed)
        self.assertGreaterEqual(res.validation.metrics["embedded_image_count"], 1)
        self.assertEqual(res.validation.metrics["slides_with_speaker_notes"], 13)
        self.assertTrue(res.validation.metrics["vietnamese_chars_detected"])

        prs = Presentation(str(out_pptx))
        self.assertEqual(len(prs.slides), 13)
        # Verify Slide 10 has Python code in Consolas
        sl10_fonts = [
            r.font.name
            for sh in prs.slides[9].shapes
            if sh.has_text_frame
            for p in sh.text_frame.paragraphs
            for r in p.runs
            if "print(" in r.text
        ]
        self.assertIn("Consolas", sl10_fonts)

    def test_markdown_to_pptx_and_themes(self):
        src_md = REPO_ROOT / "output/tin-hoc-10-kntt-bai-16/03_Kich_ban_Slide_Bai_16.md"
        for theme in ("education", "lesson", "assessment"):
            out = self.tmp_dir / f"bai16_{theme}.pptx"
            res = generate_document(src_md, out, format="pptx", template=theme)
            self.assertTrue(res.success, f"Theme {theme} failed")
            self.assertEqual(res.validation.metrics["slide_count"], 18)


if __name__ == "__main__":
    unittest.main()
