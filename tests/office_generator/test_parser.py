"""Tests for Markdown block parser and structured SlideDeck parser."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.office_generator.markdown_parser import (  # noqa: E402
    parse_markdown_blocks,
    parse_slide_deck_from_json,
    parse_slide_deck_from_markdown,
)


class TestMarkdownAndSlideParser(unittest.TestCase):
    def test_parse_blocks_headings_lists_tables_images_breaks(self):
        md = """# Kế hoạch bài dạy Tin học 10

> Ghi chú tham khảo Công văn 5512.

## I. Mục tiêu
- Kiến thức cơ bản
  - Nhánh con
1. Bước một
2. Bước hai

![Sơ đồ kết nối](diagram.png)

| Cột 1 | Cột 2 |
|---|---|
| Giá trị A | Giá trị B |
*Bảng 1. Minh họa*

<!-- pagebreak -->

```python
print("Xin chào Python")
```
"""
        blocks, notices = parse_markdown_blocks(md)
        kinds = [b.kind for b in blocks]
        self.assertIn("heading", kinds)
        self.assertIn("quote", kinds)
        self.assertIn("bullet", kinds)
        self.assertIn("numbered", kinds)
        self.assertIn("image", kinds)
        self.assertIn("table", kinds)
        self.assertIn("page_break", kinds)
        self.assertIn("code", kinds)
        tbl = next(b for b in blocks if b.kind == "table")
        self.assertEqual(tbl.caption, "Bảng 1. Minh họa")
        self.assertEqual(len(notices), 0)

    def test_parse_slide_table_with_multiline_code_and_embedded_table(self):
        bai16_md = REPO_ROOT / "output/tin-hoc-10-kntt-bai-16/03_Kich_ban_Slide_Bai_16.md"
        deck = parse_slide_deck_from_markdown(bai16_md.read_text(encoding="utf-8"))
        self.assertEqual(len(deck.slides), 18)
        self.assertTrue(any(">>> 15 + 25" in c for c in deck.slides[10].code_lines))
        self.assertEqual(len(deck.slides[11].table_rows), 4)

    def test_parse_slide_sections_format(self):
        md = """# Slide chuyên đề
## Slide 1: Mở đầu
Layout: title_slide
- Giới thiệu bài học
Notes: Lời dẫn mở đầu.

## Slide 2: Ví dụ Python
Layout: code_example
```python
print(2 + 3)
```
Notes: Chạy thử trên IDLE.
"""
        deck = parse_slide_deck_from_markdown(md)
        self.assertEqual(deck.source_format, "markdown_sections")
        self.assertEqual(len(deck.slides), 2)
        self.assertEqual(deck.slides[1].layout, "code_example")
        self.assertEqual(deck.slides[1].code_lines, ["print(2 + 3)"])

    def test_parse_unrecognized_slide_markdown_raises_clear_error(self):
        with self.assertRaises(ValueError):
            parse_slide_deck_from_markdown("# Tài liệu thường\n\nChỉ có đoạn văn, không có cấu trúc slide.")

    def test_parse_slide_json(self):
        raw = '{"title": "Demo", "slides": [{"number": 1, "title": "Tiêu đề", "layout": "closing", "content_lines": ["Cảm ơn"]}]}'
        deck = parse_slide_deck_from_json(raw)
        self.assertEqual(len(deck.slides), 1)
        self.assertEqual(deck.slides[0].layout, "closing")


if __name__ == "__main__":
    unittest.main()
