"""Reusable 16:9 Microsoft PowerPoint (.pptx) rendering engine with 13 visual layouts.

Supported layouts (selectable via SlideModel.layout or automatic content classification):
1.  title_slide      - Dark hero cover slide with goal cards
2.  section_divider  - Clean section/period transition slide
3.  text_image       - Split text + real embedded image (or structured visual card)
4.  two_columns      - Balanced two-column content/practice layout
5.  comparison       - Side-by-side 2 or 3 comparison cards
6.  timeline         - Horizontal milestone/evolution timeline
7.  process          - Step-by-step numbered horizontal process flow
8.  diagram          - Conceptual block/arrow diagram + explanation
9.  table            - Native PowerPoint comparison/data table
10. code_example     - Syntax-styled Code Editor / IDLE Shell window + takeaways
11. quiz             - Structured A/B/C/D quiz cards (answers strictly in Speaker Notes)
12. summary          - Dark/high-contrast key takeaways summary slide
13. closing          - Clean closing / next-lesson / Q&A slide
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from scripts.office_generator.markdown_parser import (
    parse_inline_spans,
    strip_markdown_inline,
)
from scripts.office_generator.models import PptxTemplateConfig, SlideDeck, SlideModel

WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def _rgb(hex_str: str) -> RGBColor:
    h = hex_str.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _set_bg(slide, color: RGBColor) -> None:
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_rect(
    slide,
    left: float,
    top: float,
    width: float,
    height: float,
    fill_color: RGBColor,
    line_color: RGBColor | None = None,
    line_pt: float = 1.0,
    rounded: bool = True,
):
    stype = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(stype, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color is not None:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(line_pt)
    else:
        shape.line.fill.background()
    if rounded:
        shape.adjustments[0] = 0.06
    return shape


def _auto_font_size(lines: List[str], width_in: float, height_in: float, max_pt: float, min_pt: float = 11.5) -> float:
    """Estimate a readable font size within [min_pt, max_pt] to prevent textbox overflow."""
    if not lines:
        return max_pt
    usable_w_pt = max((width_in - 0.18) * 72.0, 80.0)
    usable_h_pt = max((height_in - 0.12) * 72.0, 36.0)
    size = max_pt
    while size > min_pt:
        total_h = 0.0
        chars_per_line = max(int(usable_w_pt / (size * 0.54)), 10)
        for line in lines:
            clean = strip_markdown_inline(line)
            n_lines = max(1, (len(clean) + chars_per_line - 1) // chars_per_line)
            total_h += n_lines * (size * 1.28) + 4.5
        if total_h <= usable_h_pt:
            return round(size, 1)
        size -= 0.5
    return min_pt


def _add_rich_p(
    tf,
    text: str,
    cfg: PptxTemplateConfig,
    size_pt: float = 15.5,
    color: RGBColor | None = None,
    bold: bool = False,
    italic: bool = False,
    align=PP_ALIGN.LEFT,
    space_after: float = 4.5,
    first: bool = False,
    code_color: RGBColor | None = None,
) -> None:
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    text_rgb = color or _rgb(cfg.text_dark)
    default_code = _rgb(cfg.accent_bright) if text_rgb == WHITE else _rgb(cfg.primary)
    for span in parse_inline_spans(text):
        run = p.add_run()
        run.text = span.text
        if span.code:
            run.font.name = cfg.font_code
            run.font.size = Pt(max(size_pt - 1.0, 10.5))
            run.font.bold = bold or span.bold
            run.font.color.rgb = code_color or default_code
        else:
            run.font.name = cfg.font_main
            run.font.size = Pt(size_pt)
            run.font.bold = bold or span.bold
            run.font.italic = italic or span.italic
            run.font.color.rgb = text_rgb


def _add_textbox(
    slide,
    cfg: PptxTemplateConfig,
    left: float,
    top: float,
    width: float,
    height: float,
    lines: List[str],
    size_pt: float = 15.5,
    color: RGBColor | None = None,
    bold: bool = False,
    align=PP_ALIGN.LEFT,
    space_after: float = 5.0,
    valign=MSO_ANCHOR.TOP,
    auto_fit: bool = True,
    min_pt: float = 11.5,
    code_color: RGBColor | None = None,
):
    actual_size = _auto_font_size(lines, width, height, size_pt, min_pt) if auto_fit else size_pt
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = valign
    tf.margin_left = Inches(0.08)
    tf.margin_right = Inches(0.08)
    tf.margin_top = Inches(0.05)
    tf.margin_bottom = Inches(0.05)
    for idx, line in enumerate(lines):
        _add_rich_p(
            tf,
            line,
            cfg,
            size_pt=actual_size,
            color=color,
            bold=bold,
            align=align,
            space_after=space_after,
            first=(idx == 0),
            code_color=code_color,
        )
    return tb


def _add_chrome(
    slide,
    spec: SlideModel,
    deck: SlideDeck,
    total_slides: int,
    cfg: PptxTemplateConfig,
    base_dir: Path | None = None,
    dark: bool = False,
) -> None:
    """Render consistent header bar, optional logo, and slide footer."""
    if not dark:
        _add_rect(slide, 0, 0, cfg.slide_width_in, 0.12, _rgb(cfg.primary), rounded=False)
        badge_text = " | ".join(
            [strip_markdown_inline(x) for x in spec.meta.split("\n") if x.strip()]
        )
        title_left = 0.55
        if cfg.logo_path:
            logo_p = Path(cfg.logo_path)
            if not logo_p.is_absolute() and base_dir is not None:
                logo_p = (base_dir / logo_p).resolve()
            if logo_p.is_file():
                slide.shapes.add_picture(str(logo_p), Inches(0.45), Inches(0.22), height=Inches(0.62))
                title_left = 1.25

        if badge_text:
            badge_w = min(max(len(badge_text) * 0.105 + 0.45, 2.1), 3.8)
            pill = _add_rect(
                slide,
                12.78 - badge_w,
                0.28,
                badge_w,
                0.42,
                _rgb(cfg.primary_soft),
                _rgb(cfg.primary),
                1.0,
            )
            pill.text_frame.word_wrap = True
            pill.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
            _add_rich_p(
                pill.text_frame,
                badge_text,
                cfg,
                size_pt=11.5,
                color=_rgb(cfg.primary),
                bold=True,
                align=PP_ALIGN.CENTER,
                space_after=0,
                first=True,
            )
            title_w = 12.55 - badge_w - title_left
        else:
            title_w = 12.78 - title_left

        title_sz = 23.5 if len(spec.title) <= 48 else 20.0
        _add_textbox(
            slide,
            cfg,
            title_left,
            0.20,
            title_w,
            0.80,
            [spec.title],
            size_pt=title_sz,
            color=_rgb(cfg.bg_dark),
            bold=True,
            space_after=0,
            valign=MSO_ANCHOR.MIDDLE,
            auto_fit=True,
            min_pt=16.0,
        )
        _add_rect(slide, 0.55, 1.05, 12.23, 0.03, _rgb(cfg.border), rounded=False)

    footer_color = _rgb(cfg.text_muted) if not dark else RGBColor(0x94, 0xA3, 0xB8)
    left_parts: List[str] = []
    if cfg.school_name:
        left_parts.append(cfg.school_name)
    if spec.section_label:
        left_parts.append(spec.section_label.split("–")[0].strip())
    footer_main = cfg.footer_text or deck.subtitle or deck.title
    if footer_main:
        left_parts.append(footer_main[:68])
    if cfg.teacher_name:
        left_parts.append(f"GV: {cfg.teacher_name}")

    _add_textbox(
        slide,
        cfg,
        0.55,
        7.05,
        9.7,
        0.34,
        ["  •  ".join(left_parts) if left_parts else "Vietnamese Teacher AI"],
        size_pt=10.0,
        color=footer_color,
        space_after=0,
        auto_fit=False,
    )
    if cfg.show_slide_numbers:
        _add_textbox(
            slide,
            cfg,
            10.55,
            7.05,
            2.23,
            0.34,
            [f"Slide {spec.number} / {total_slides}"],
            size_pt=10.5,
            color=footer_color,
            bold=True,
            align=PP_ALIGN.RIGHT,
            space_after=0,
            auto_fit=False,
        )


def _add_code_window(
    slide,
    cfg: PptxTemplateConfig,
    left: float,
    top: float,
    width: float,
    height: float,
    title: str,
    code_lines: List[str],
    light_shell: bool = False,
) -> None:
    bg = WHITE if light_shell else _rgb(cfg.code_bg)
    bar = _rgb(cfg.primary_soft) if light_shell else _rgb(cfg.bg_dark)
    border = _rgb(cfg.primary) if light_shell else RGBColor(0x33, 0x41, 0x55)

    _add_rect(slide, left, top, width, height, bg, border, 1.2)
    _add_rect(slide, left, top, width, 0.42, bar, None, rounded=False)
    for idx, dot_hex in enumerate((cfg.danger, cfg.accent_bright, cfg.success)):
        dot = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(left + 0.16 + idx * 0.22),
            Inches(top + 0.14),
            Inches(0.13),
            Inches(0.13),
        )
        dot.fill.solid()
        dot.fill.fore_color.rgb = _rgb(dot_hex)
        dot.line.fill.background()

    _add_textbox(
        slide,
        cfg,
        left + 0.88,
        top + 0.05,
        width - 1.0,
        0.32,
        [title],
        size_pt=11.0,
        color=_rgb(cfg.bg_dark) if light_shell else RGBColor(0xCB, 0xD5, 0xE1),
        bold=True,
        space_after=0,
        auto_fit=False,
    )

    tb = slide.shapes.add_textbox(
        Inches(left + 0.18), Inches(top + 0.50), Inches(width - 0.36), Inches(height - 0.60)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    font_sz = _auto_font_size(code_lines, width - 0.36, height - 0.60, max_pt=14.5, min_pt=10.5)
    for idx, line in enumerate(code_lines):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.space_after = Pt(2.5)
        r = p.add_run()
        r.text = line
        r.font.name = cfg.font_code
        r.font.size = Pt(font_sz)
        if light_shell:
            if line.strip().startswith(">>>"):
                r.font.color.rgb = _rgb(cfg.danger)
                r.font.bold = True
            elif not line.strip().startswith("#") and "(" not in line and not line.strip().startswith(">>>"):
                r.font.color.rgb = _rgb(cfg.primary)
            else:
                r.font.color.rgb = _rgb(cfg.text_dark)
        else:
            if line.strip().startswith("#"):
                r.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)
            elif "print(" in line or "def " in line or "return " in line:
                r.font.color.rgb = _rgb(cfg.accent_bright)
            else:
                r.font.color.rgb = _rgb(cfg.code_text)


def classify_layout(spec: SlideModel, total_slides: int, default_layout: str = "two_columns") -> str:
    """Resolve explicit SlideModel.layout or classify automatically across 13 layouts."""
    valid_layouts = set(LAYOUT_RENDERERS.keys())
    if spec.layout and spec.layout != "auto" and spec.layout in valid_layouts:
        return spec.layout

    title_l = spec.title.lower()
    raw_l = spec.display_raw.lower()

    if spec.number == 1:
        return "title_slide"
    if "cảm ơn" in title_l or "kết thúc" in title_l or "closing" in title_l:
        return "closing"
    if spec.number == total_slides or "tổng kết" in title_l:
        return "summary"
    if "phần " in title_l[:8] or "tiết " in title_l[:8] or "chương " in title_l[:10]:
        return "section_divider"
    if spec.image_path:
        return "text_image"
    if "kiểm tra nhanh" in title_l or "trắc nghiệm" in title_l or ("**a.**" in raw_l and "**b.**" in raw_l):
        return "quiz"
    if spec.table_rows:
        return "table"
    if "tiến trình" in title_l or "lịch sử" in title_l or "dòng thời gian" in title_l or "timeline" in title_l:
        return "timeline"
    if "thẻ a:" in raw_l and "thẻ b:" in raw_l and "thẻ c:" in raw_l:
        return "comparison"
    if "3 mức ngôn ngữ" in title_l or ("ngôn ngữ máy" in raw_l and "hợp ngữ" in raw_l and "bậc cao" in raw_l):
        return "comparison"
    if "quy trình" in title_l or "4 bước" in raw_l:
        return "process"
    if "chương trình dịch" in title_l or "ngôn ngữ lập trình là gì" in title_l or "sơ đồ" in title_l:
        return "diagram"
    if spec.code_lines or "c++" in raw_l or "trực tiếp" in title_l:
        return "code_example"
    if "đâu quanh ta" in title_l or "4 lĩnh vực" in raw_l:
        return "diagram"
    return default_layout if default_layout in valid_layouts else "two_columns"


# ==============================================================================
# 13 DISTINCT SLIDE LAYOUT RENDERERS
# ==============================================================================

def render_title_slide(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_dark))
    _add_rect(slide, 0, 0, 0.24, cfg.slide_height_in, _rgb(cfg.accent_bright), rounded=False)
    _add_rect(slide, 12.95, 0, 0.38, cfg.slide_height_in, _rgb(cfg.primary), rounded=False)

    lines = [l.strip() for l in spec.display_raw.split("\n") if l.strip()]
    subtitle_lines = [l.lstrip("• ").strip() for l in lines if l.startswith("•") and "mục tiêu" not in l.lower()]
    goal_lines = [re.sub(r"^\d+\.\s*", "", l.strip()) for l in lines if re.match(r"^\d+\.\s*", l.strip())]

    tag_text = cfg.school_name or (subtitle_lines[0] if subtitle_lines else cfg.display_name)
    tag = _add_rect(slide, 0.85, 0.68, min(max(len(tag_text) * 0.12 + 0.6, 3.6), 6.2), 0.45, _rgb(cfg.primary), None)
    tag.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    _add_rich_p(tag.text_frame, tag_text, cfg, size_pt=13.0, color=WHITE, bold=True, align=PP_ALIGN.CENTER, space_after=0, first=True)

    _add_textbox(slide, cfg, 0.85, 1.32, 11.6, 1.45, [spec.title], size_pt=33.0, color=WHITE, bold=True, min_pt=22.0)

    sub_str = subtitle_lines[1] if len(subtitle_lines) > 1 else (deck.subtitle or spec.meta.replace("\n", " | "))
    if sub_str:
        _add_textbox(slide, cfg, 0.85, 2.75, 11.0, 0.48, [sub_str], size_pt=16.0, color=_rgb(cfg.accent_bright), bold=True)

    palette = [_rgb(cfg.primary), _rgb(cfg.secondary), _rgb(cfg.accent), _rgb(cfg.success)]
    for idx, goal in enumerate(goal_lines[:4]):
        col, row = idx % 2, idx // 2
        cx, cy = 0.85 + col * 5.9, 3.55 + row * 1.55
        _add_rect(slide, cx, cy, 5.55, 1.32, _rgb(cfg.bg_dark_card), palette[idx], 1.5)
        badge = _add_rect(slide, cx + 0.22, cy + 0.34, 0.62, 0.62, palette[idx], None)
        badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        _add_rich_p(badge.text_frame, f"M{idx+1}", cfg, size_pt=14.5, color=WHITE, bold=True, align=PP_ALIGN.CENTER, space_after=0, first=True)
        _add_textbox(slide, cfg, cx + 1.0, cy + 0.18, 4.35, 0.96, [goal], size_pt=15.5, color=WHITE, valign=MSO_ANCHOR.MIDDLE)

    _add_chrome(slide, spec, deck, total, cfg, base_dir, dark=True)


def render_section_divider(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.primary))
    _add_rect(slide, 0, 5.9, cfg.slide_width_in, 1.6, _rgb(cfg.bg_dark), rounded=False)
    _add_rect(slide, 0.9, 2.0, 1.2, 0.12, _rgb(cfg.accent_bright), rounded=False)
    _add_textbox(slide, cfg, 0.9, 2.3, 11.5, 1.5, [spec.title], size_pt=34.0, color=WHITE, bold=True, min_pt=24.0)
    if spec.content_lines:
        _add_textbox(slide, cfg, 0.9, 3.95, 11.2, 1.6, spec.content_lines[:4], size_pt=17.0, color=_rgb(cfg.primary_soft))
    _add_chrome(slide, spec, deck, total, cfg, base_dir, dark=True)


def render_text_image(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    # Left: content card
    _add_rect(slide, 0.55, 1.32, 6.25, 5.35, WHITE, _rgb(cfg.primary), 1.4)
    _add_rect(slide, 0.55, 1.32, 6.25, 0.14, _rgb(cfg.primary), None, rounded=False)
    text_lines = [l for l in spec.content_lines if not l.strip().startswith("![")]
    _add_textbox(slide, cfg, 0.8, 1.62, 5.75, 4.85, text_lines or [spec.title], size_pt=15.5, space_after=8)

    # Right: real image if valid path exists, else visual callout card
    _add_rect(slide, 7.05, 1.32, 5.73, 5.35, WHITE, _rgb(cfg.border), 1.2)
    img_p = Path(spec.image_path) if spec.image_path else None
    if img_p and not img_p.is_absolute() and base_dir is not None:
        img_p = (base_dir / img_p).resolve()

    if img_p and img_p.is_file():
        slide.shapes.add_picture(str(img_p), Inches(7.25), Inches(1.52), width=Inches(5.33), height=Inches(4.35))
        cap = spec.image_caption or spec.visual_suggestion or img_p.name
        _add_textbox(slide, cfg, 7.2, 6.02, 5.4, 0.52, [strip_markdown_inline(cap)], size_pt=11.5, color=_rgb(cfg.text_muted), align=PP_ALIGN.CENTER)
    else:
        _add_rect(slide, 7.35, 1.72, 5.13, 3.85, _rgb(cfg.primary_soft), _rgb(cfg.primary), 1.0)
        _add_textbox(
            slide,
            cfg,
            7.55,
            2.1,
            4.73,
            3.1,
            [f"Hình ảnh / Minh họa đề xuất:\n{strip_markdown_inline(spec.visual_suggestion or spec.image_caption)}"],
            size_pt=14.0,
            color=_rgb(cfg.bg_dark),
            align=PP_ALIGN.CENTER,
            valign=MSO_ANCHOR.MIDDLE,
        )


def render_two_columns(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    lines = [l.strip() for l in spec.display_raw.split("\n") if l.strip()]
    split_idx = None
    for idx, l in enumerate(lines):
        if idx > 0 and any(k in l.lower() for k in ("săn", "yêu cầu:", "thử nghiệm thêm", "gồm 2 chế độ", "nâng cao")):
            split_idx = idx
            break
    if split_idx is not None:
        left_lines, right_lines = lines[:split_idx], lines[split_idx:]
    else:
        mid = max(1, (len(lines) + 1) // 2)
        left_lines, right_lines = lines[:mid], lines[mid:] or lines

    is_err = any("lỗi" in l.lower() or "syntax" in l.lower() for l in right_lines)
    r_accent = _rgb(cfg.danger if is_err else cfg.secondary)
    r_bg = _rgb(cfg.danger_soft if is_err else cfg.secondary_soft)

    _add_rect(slide, 0.55, 1.32, 6.25, 5.35, WHITE, _rgb(cfg.primary), 1.4)
    _add_rect(slide, 0.55, 1.32, 6.25, 0.14, _rgb(cfg.primary), None, rounded=False)
    _add_textbox(slide, cfg, 0.8, 1.62, 5.75, 4.85, left_lines, size_pt=15.0, space_after=8)

    _add_rect(slide, 7.08, 1.32, 5.70, 5.35, r_bg, r_accent, 1.4)
    _add_rect(slide, 7.08, 1.32, 5.70, 0.14, r_accent, None, rounded=False)
    _add_textbox(slide, cfg, 7.32, 1.62, 5.22, 3.55, right_lines, size_pt=15.0, color=_rgb(cfg.bg_dark), space_after=8)

    if spec.visual_suggestion:
        _add_rect(slide, 7.32, 5.35, 5.22, 1.08, WHITE, _rgb(cfg.border), 1.0)
        _add_textbox(
            slide,
            cfg,
            7.45,
            5.42,
            4.96,
            0.94,
            [f"Gợi ý minh họa: {strip_markdown_inline(spec.visual_suggestion)[:145]}"],
            size_pt=11.0,
            color=_rgb(cfg.text_muted),
            space_after=0,
        )


def render_comparison(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    lines = [l.strip() for l in spec.display_raw.split("\n") if l.strip()]
    cards = [l.lstrip("•- ").strip() for l in lines if l.startswith(("•", "-"))]
    prompt_lines = [l for l in lines if not l.startswith(("•", "-"))]
    if len(cards) < 2:
        cards = lines[:3]
        prompt_lines = lines[3:]

    if prompt_lines:
        _add_textbox(slide, cfg, 0.55, 1.2, 12.2, 0.5, [prompt_lines[0]], size_pt=16.5, color=_rgb(cfg.bg_dark), bold=True)

    count = min(max(len(cards), 2), 3)
    accents = [_rgb(cfg.text_muted), _rgb(cfg.primary), _rgb(cfg.accent)]
    softs = [WHITE, _rgb(cfg.primary_soft), _rgb(cfg.accent_soft)]
    card_w = (12.23 - 0.3 * (count - 1)) / count
    card_top = 1.85
    card_h = 3.65 if len(prompt_lines) > 1 else 4.65

    for idx, card_text in enumerate(cards[:count]):
        cx = 0.55 + idx * (card_w + 0.3)
        _add_rect(slide, cx, card_top, card_w, card_h, softs[idx], accents[idx], 1.5)
        _add_rect(slide, cx, card_top, card_w, 0.16, accents[idx], None, rounded=False)
        if ":" in card_text:
            head, body = card_text.split(":", 1)
            _add_textbox(slide, cfg, cx + 0.18, card_top + 0.28, card_w - 0.36, 0.72, [head.strip()], size_pt=16.0, color=accents[idx], bold=True)
            parts = [p.strip() for p in re.split(r"•|/", body) if p.strip()]
            _add_textbox(
                slide,
                cfg,
                cx + 0.18,
                card_top + 1.05,
                card_w - 0.36,
                card_h - 1.25,
                [f"• {bp}" if len(parts) > 1 else bp for bp in parts],
                size_pt=14.5,
                space_after=7,
            )
        else:
            _add_textbox(slide, cfg, cx + 0.18, card_top + 0.35, card_w - 0.36, card_h - 0.5, [card_text], size_pt=14.5)

    if len(prompt_lines) > 1:
        _add_rect(slide, 0.55, 5.75, 12.23, 1.05, _rgb(cfg.bg_dark), None)
        _add_textbox(
            slide,
            cfg,
            0.8,
            5.86,
            11.75,
            0.84,
            prompt_lines[1:],
            size_pt=15.0,
            color=WHITE,
            valign=MSO_ANCHOR.MIDDLE,
            code_color=_rgb(cfg.accent_bright),
        )


def render_timeline(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    items = [l.lstrip("•- ").strip() for l in spec.content_lines if l.strip()]
    count = min(max(len(items), 1), 4)
    # Horizontal timeline track
    _add_rect(slide, 0.85, 3.65, 11.63, 0.08, _rgb(cfg.primary), rounded=False)
    colors = [_rgb(cfg.primary), _rgb(cfg.secondary), _rgb(cfg.accent), _rgb(cfg.success)]
    step_w = 11.8 / count

    for idx, item in enumerate(items[:count]):
        cx = 0.75 + idx * step_w
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx + step_w / 2 - 0.28), Inches(3.41), Inches(0.56), Inches(0.56))
        dot.fill.solid()
        dot.fill.fore_color.rgb = colors[idx]
        dot.line.fill.background()
        dot.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        _add_rich_p(dot.text_frame, str(idx + 1), cfg, size_pt=14.0, color=WHITE, bold=True, align=PP_ALIGN.CENTER, space_after=0, first=True)

        box_top = 1.45 if idx % 2 == 0 else 4.25
        _add_rect(slide, cx + 0.1, box_top, step_w - 0.25, 1.75, WHITE, colors[idx], 1.4)
        _add_textbox(slide, cfg, cx + 0.22, box_top + 0.14, step_w - 0.48, 1.48, [item], size_pt=13.5, valign=MSO_ANCHOR.MIDDLE)


def render_process(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    lines = [l.strip() for l in spec.display_raw.split("\n") if l.strip()]
    steps = [l for l in lines if re.match(r"^\d+\.\s*", l)]
    if not steps:
        steps = [l.lstrip("•- ").strip() for l in lines if l.startswith(("•", "-"))] or lines[:4]
    intro = [l for l in lines if l not in steps and not l.startswith("⚠️")]
    warn = [l for l in lines if l.startswith("⚠️")]

    if intro:
        _add_textbox(slide, cfg, 0.55, 1.2, 12.2, 0.45, [intro[0]], size_pt=16.5, color=_rgb(cfg.bg_dark), bold=True)

    colors = [_rgb(cfg.primary), _rgb(cfg.secondary), _rgb(cfg.accent), _rgb(cfg.success)]
    count = min(max(len(steps), 1), 4)
    card_w = (12.23 - 0.35 * (count - 1)) / count
    for idx, st in enumerate(steps[:count]):
        cx = 0.55 + idx * (card_w + 0.35)
        _add_rect(slide, cx, 1.9, card_w, 3.45, WHITE, colors[idx], 1.6)
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx + card_w / 2 - 0.36), Inches(2.15), Inches(0.72), Inches(0.72))
        circle.fill.solid()
        circle.fill.fore_color.rgb = colors[idx]
        circle.line.fill.background()
        circle.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        _add_rich_p(circle.text_frame, str(idx + 1), cfg, size_pt=19.0, color=WHITE, bold=True, align=PP_ALIGN.CENTER, space_after=0, first=True)
        clean_st = re.sub(r"^\d+\.\s*", "", st)
        _add_textbox(slide, cfg, cx + 0.16, 3.05, card_w - 0.32, 2.1, [clean_st], size_pt=14.5, align=PP_ALIGN.CENTER)
        if idx < count - 1:
            arr = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(cx + card_w + 0.06), Inches(3.42), Inches(0.23), Inches(0.35))
            arr.fill.solid()
            arr.fill.fore_color.rgb = _rgb(cfg.text_muted)
            arr.line.fill.background()

    if warn:
        _add_rect(slide, 0.55, 5.65, 12.23, 1.05, _rgb(cfg.accent_soft), _rgb(cfg.accent), 1.5)
        _add_textbox(slide, cfg, 0.8, 5.78, 11.75, 0.8, warn, size_pt=15.0, color=_rgb(cfg.bg_dark), bold=True, valign=MSO_ANCHOR.MIDDLE)


def render_diagram(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    lines = [l.strip() for l in spec.display_raw.split("\n") if l.strip()]
    # 2x2 visual grid for 4-item domain maps (e.g., Slide 8)
    bullets = [l.lstrip("•- ").strip() for l in lines if l.startswith(("•", "-"))]
    if "4 lĩnh vực" in spec.display_raw.lower() or "đâu quanh ta" in spec.title.lower():
        header_l = [l for l in lines if not l.startswith(("•", "-"))]
        if header_l:
            _add_textbox(slide, cfg, 0.55, 1.22, 12.2, 0.5, header_l[:1], size_pt=17.5, color=_rgb(cfg.bg_dark), bold=True)
        colors = [_rgb(cfg.primary), _rgb(cfg.secondary), _rgb(cfg.accent), _rgb(cfg.success)]
        softs = [_rgb(cfg.primary_soft), _rgb(cfg.secondary_soft), _rgb(cfg.accent_soft), _rgb(cfg.success_soft)]
        for idx, item in enumerate(bullets[:4]):
            col, row = idx % 2, idx // 2
            cx, cy = 0.55 + col * 6.28, 1.9 + row * 2.48
            _add_rect(slide, cx, cy, 5.95, 2.22, WHITE, colors[idx], 1.5)
            _add_rect(slide, cx, cy, 0.22, 2.22, colors[idx], None, rounded=False)
            badge = _add_rect(slide, cx + 0.42, cy + 0.25, 0.65, 0.52, softs[idx], None)
            badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
            _add_rich_p(badge.text_frame, f"0{idx+1}", cfg, size_pt=14.5, color=colors[idx], bold=True, align=PP_ALIGN.CENTER, space_after=0, first=True)
            _add_textbox(slide, cfg, cx + 0.42, cy + 0.88, 5.3, 1.15, [item], size_pt=16.5, color=_rgb(cfg.bg_dark), valign=MSO_ANCHOR.MIDDLE)
        return

    # Conceptual block-arrow flow diagram
    if "chương trình dịch" in spec.title.lower():
        nodes = [
            ("Mã nguồn Python", "print(5 + 3)", _rgb(cfg.primary)),
            ("Chương trình dịch", "Chuyển đổi lệnh", _rgb(cfg.accent)),
            ("Ngôn ngữ máy", "10110000 00000101", _rgb(cfg.bg_dark)),
            ("Kết quả thực thi", "8", _rgb(cfg.success)),
        ]
    else:
        nodes = [
            ("1. Ý tưởng / Thuật toán", "Các bước giải bài toán", _rgb(cfg.primary)),
            ("2. Ngôn ngữ lập trình", "Viết thành chương trình", _rgb(cfg.secondary)),
            ("3. Máy tính thực thi", "Chính xác & tự động", _rgb(cfg.success)),
        ]

    n_nodes = len(nodes)
    nw = (12.23 - 0.45 * (n_nodes - 1)) / n_nodes
    for idx, (ntitle, nsub, ncol) in enumerate(nodes):
        nx = 0.55 + idx * (nw + 0.45)
        _add_rect(slide, nx, 1.35, nw, 1.45, ncol, None)
        _add_textbox(slide, cfg, nx + 0.12, 1.48, nw - 0.24, 0.56, [ntitle], size_pt=15.0, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
        _add_textbox(slide, cfg, nx + 0.12, 2.08, nw - 0.24, 0.56, [nsub], size_pt=13.0, color=_rgb(cfg.accent_soft), align=PP_ALIGN.CENTER)
        if idx < n_nodes - 1:
            arr = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(nx + nw + 0.08), Inches(1.88), Inches(0.29), Inches(0.38))
            arr.fill.solid()
            arr.fill.fore_color.rgb = _rgb(cfg.bg_dark)
            arr.line.fill.background()

    _add_rect(slide, 0.55, 3.15, 12.23, 3.60, WHITE, _rgb(cfg.border), 1.2)
    _add_textbox(slide, cfg, 0.85, 3.35, 11.65, 3.20, lines, size_pt=16.0, space_after=9)


def render_table(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    rows = spec.table_rows
    others = [l for l in spec.content_lines if not (l.strip().startswith("|") and l.strip().endswith("|"))]
    top_y = 1.28
    if others:
        _add_rect(slide, 0.55, top_y, 12.23, 0.72, _rgb(cfg.primary_soft), _rgb(cfg.primary), 1.2)
        _add_textbox(slide, cfg, 0.75, top_y + 0.08, 11.8, 0.56, others[:2], size_pt=15.0, color=_rgb(cfg.bg_dark), bold=True, valign=MSO_ANCHOR.MIDDLE)
        top_y = 2.22

    if rows:
        n_rows, n_cols = len(rows), len(rows[0])
        tbl_shape = slide.shapes.add_table(n_rows, n_cols, Inches(0.55), Inches(top_y), Inches(12.23), Inches(min(4.45, n_rows * 0.95)))
        tbl = tbl_shape.table
        for c in range(n_cols):
            tbl.columns[c].width = Inches(12.23 / n_cols)
        for r_idx, row in enumerate(rows):
            for c_idx, val in enumerate(row):
                cell = tbl.cell(r_idx, c_idx)
                cell.vertical_anchor = MSO_ANCHOR.MIDDLE
                cell.fill.solid()
                if r_idx == 0:
                    cell.fill.fore_color.rgb = _rgb(cfg.bg_dark)
                elif r_idx % 2 == 1:
                    cell.fill.fore_color.rgb = WHITE
                else:
                    cell.fill.fore_color.rgb = _rgb(cfg.primary_soft)
                _add_rich_p(
                    cell.text_frame,
                    val,
                    cfg,
                    size_pt=15.0 if r_idx == 0 else 14.0,
                    color=WHITE if r_idx == 0 else _rgb(cfg.text_dark),
                    bold=(r_idx == 0 or c_idx == 0),
                    align=PP_ALIGN.CENTER if r_idx == 0 else PP_ALIGN.LEFT,
                    space_after=0,
                    first=True,
                )


def render_code_example(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    code_lines = list(spec.code_lines)
    other_lines = list(spec.content_lines)
    is_shell = "trực tiếp" in spec.title.lower() or any(">>>" in c for c in code_lines)

    if not code_lines:
        if "c++" in spec.display_raw.lower():
            code_lines = [
                "# C++ (minh họa 5 dòng):",
                "#include <iostream>",
                "int main() {",
                '  std::cout << "Xin chao lop 10!";',
                "  return 0;",
                "}",
                "",
                "# Python (1 dòng duy nhất):",
                'print("Xin chao lop 10!")',
            ]
            other_lines = [l for l in other_lines if "minh họa c++" not in l.lower() and "python (1 dòng" not in l.lower() and 'print("xin chao' not in l.lower()]
        else:
            code_lines = ['# Mã Python minh họa', 'print("Xin chao Python!")']

    win_title = "IDLE Shell 3.12 (Interactive Mode)" if is_shell else f"Ví dụ mã nguồn ({spec.code_language.upper()})"
    _add_code_window(slide, cfg, 0.55, 1.32, 6.45, 5.30, win_title, code_lines, light_shell=is_shell)

    _add_rect(slide, 7.28, 1.32, 5.50, 5.30, WHITE, _rgb(cfg.primary), 1.3)
    _add_rect(slide, 7.28, 1.32, 5.50, 0.14, _rgb(cfg.primary), None, rounded=False)
    _add_textbox(slide, cfg, 7.52, 1.62, 5.02, 4.80, other_lines or [spec.visual_suggestion], size_pt=15.0, space_after=9)


def render_quiz(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_light))
    _add_chrome(slide, spec, deck, total, cfg, base_dir)

    raw_blocks = re.split(r"(?=\*\*Câu\s+\d+)", spec.display_raw)
    questions = [b.strip() for b in raw_blocks if b.strip()]
    num_q = min(max(len(questions), 1), 2)
    box_h = 2.65 if num_q == 2 else 5.30

    for q_idx, q_block in enumerate(questions[:2]):
        top = 1.28 + q_idx * 2.88
        accent = _rgb(cfg.primary if q_idx == 0 else cfg.secondary)
        _add_rect(slide, 0.55, top, 12.23, box_h, WHITE, accent, 1.5)
        _add_rect(slide, 0.55, top, 0.14, box_h, accent, None, rounded=False)

        q_lines = [l.strip() for l in q_block.split("\n") if l.strip()]
        stem = q_lines[0] if q_lines else ""
        opt_blob = " ".join(q_lines[1:])
        opts = re.findall(r"(\*\*[A-D]\.\*\*.*?)(?=\*\*[A-D]\.\*\*|$)", opt_blob)
        opts = [o.strip() for o in opts if o.strip()]

        _add_textbox(slide, cfg, 0.85, top + 0.10, 11.75, 0.74, [stem], size_pt=14.5, color=_rgb(cfg.bg_dark), bold=True, space_after=2)

        if len(opts) == 4:
            for o_idx, opt in enumerate(opts):
                col, row = o_idx % 2, o_idx // 2
                ox = 0.85 + col * 5.95
                oy = top + 0.90 + row * 0.84
                _add_rect(slide, ox, oy, 5.75, 0.74, _rgb(cfg.bg_light), _rgb(cfg.border), 1.0)
                _add_textbox(slide, cfg, ox + 0.12, oy + 0.05, 5.50, 0.64, [opt], size_pt=13.5, valign=MSO_ANCHOR.MIDDLE, space_after=0, min_pt=11.0)
        else:
            _add_textbox(slide, cfg, 0.85, top + 0.90, 11.75, box_h - 1.0, q_lines[1:], size_pt=13.5)


def render_summary(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_dark))
    _add_rect(slide, 0, 0, cfg.slide_width_in, 0.14, _rgb(cfg.accent_bright), rounded=False)
    _add_textbox(slide, cfg, 0.65, 0.32, 12.0, 0.78, [spec.title], size_pt=27.0, color=WHITE, bold=True)

    lines = [l.strip() for l in spec.display_raw.split("\n") if l.strip()]
    points = [l for l in lines if re.match(r"^\d+\.\s*", l)] or [l.lstrip("•- ").strip() for l in lines if l.startswith(("•", "-"))]
    next_lesson = [l for l in lines if "chuẩn bị" in l.lower() or "bài 17" in l.lower() or "nhiệm vụ" in l.lower()]

    colors = [_rgb(cfg.primary), _rgb(cfg.secondary), _rgb(cfg.accent), _rgb(cfg.success)]
    for idx, pt in enumerate(points[:4]):
        py = 1.35 + idx * 1.08
        _add_rect(slide, 0.65, py, 12.03, 0.92, _rgb(cfg.bg_dark_card), colors[idx], 1.4)
        badge = _add_rect(slide, 0.85, py + 0.18, 0.56, 0.56, colors[idx], None)
        badge.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        _add_rich_p(badge.text_frame, str(idx + 1), cfg, size_pt=15.0, color=WHITE, bold=True, align=PP_ALIGN.CENTER, space_after=0, first=True)
        clean_pt = re.sub(r"^\d+\.\s*", "", pt)
        _add_textbox(slide, cfg, 1.58, py + 0.10, 10.9, 0.72, [clean_pt], size_pt=15.0, color=WHITE, valign=MSO_ANCHOR.MIDDLE, code_color=_rgb(cfg.accent_bright))

    if next_lesson:
        _add_rect(slide, 0.65, 5.82, 12.03, 0.98, _rgb(cfg.accent_soft), _rgb(cfg.accent_bright), 1.6)
        _add_textbox(slide, cfg, 0.9, 5.94, 11.55, 0.74, next_lesson, size_pt=15.0, color=_rgb(cfg.bg_dark), bold=True, valign=MSO_ANCHOR.MIDDLE)

    _add_chrome(slide, spec, deck, total, cfg, base_dir, dark=True)


def render_closing(slide, spec: SlideModel, deck: SlideDeck, total: int, cfg: PptxTemplateConfig, base_dir: Path | None) -> None:
    _set_bg(slide, _rgb(cfg.bg_dark))
    _add_rect(slide, 0, 0, cfg.slide_width_in, 0.18, _rgb(cfg.primary), rounded=False)
    _add_rect(slide, 0, 7.32, cfg.slide_width_in, 0.18, _rgb(cfg.accent_bright), rounded=False)
    _add_textbox(slide, cfg, 1.0, 2.2, 11.33, 1.4, [spec.title], size_pt=36.0, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    if spec.content_lines:
        _add_textbox(slide, cfg, 1.5, 3.85, 10.33, 1.8, spec.content_lines[:4], size_pt=17.0, color=_rgb(cfg.accent_soft), align=PP_ALIGN.CENTER)
    _add_chrome(slide, spec, deck, total, cfg, base_dir, dark=True)


LAYOUT_RENDERERS: Dict[str, object] = {
    "title_slide": render_title_slide,
    "section_divider": render_section_divider,
    "text_image": render_text_image,
    "two_columns": render_two_columns,
    "comparison": render_comparison,
    "timeline": render_timeline,
    "process": render_process,
    "diagram": render_diagram,
    "table": render_table,
    "code_example": render_code_example,
    "quiz": render_quiz,
    "summary": render_summary,
    "closing": render_closing,
}


def export_speaker_notes_markdown(deck: SlideDeck, output_notes_md: Path) -> Path:
    """Export companion Speaker Notes Markdown document for teachers."""
    lines = [
        f"# GHI CHÚ THUYẾT TRÌNH (SPEAKER NOTES)",
        f"**Bài giảng:** {deck.subtitle or deck.title}",
        f"**Tổng số slide:** {len(deck.slides)}",
        "",
        "---",
        "",
    ]
    for s in deck.slides:
        lines.append(f"## Slide {s.number}: {s.title}")
        if s.meta:
            lines.append(f"- **Mục tiêu / Thời lượng:** {strip_markdown_inline(s.meta.replace(chr(10), ' | '))}")
        if s.speaker_notes:
            lines.append(f"- **Ghi chú thuyết trình & tương tác:**\n\n{s.speaker_notes}")
        else:
            lines.append("- **Ghi chú thuyết trình:** *(Không có ghi chú bổ sung)*")
        if s.visual_suggestion:
            lines.append(f"\n- **Gợi ý hình ảnh/sơ đồ:** {strip_markdown_inline(s.visual_suggestion)}")
        lines.append("\n---\n")

    output_notes_md.parent.mkdir(parents=True, exist_ok=True)
    output_notes_md.write_text("\n".join(lines), encoding="utf-8")
    return output_notes_md


def render_pptx(
    deck: SlideDeck,
    output_pptx: Path,
    cfg: PptxTemplateConfig,
    base_dir: Path | None = None,
    speaker_notes_file: Path | None = None,
) -> Tuple[Path, List[Tuple[int, str]], bool, str, List[str]]:
    """Render a SlideDeck into a 16:9 PowerPoint (.pptx) file.

    Returns: (saved_path, layout_log, speaker_notes_embedded, speaker_notes_md_path, notices)
    """
    if not deck.slides:
        raise ValueError("SlideDeck không có slide nào để xuất PowerPoint.")

    prs = Presentation()
    prs.slide_width = Inches(cfg.slide_width_in)
    prs.slide_height = Inches(cfg.slide_height_in)
    blank_layout = prs.slide_layouts[6]

    total = len(deck.slides)
    layout_log: List[Tuple[int, str]] = []
    notices: List[str] = list(deck.warnings)
    notes_embedded_ok = True

    for spec in deck.slides:
        slide = prs.slides.add_slide(blank_layout)
        layout_name = classify_layout(spec, total, cfg.default_layout)
        layout_log.append((spec.number, layout_name))
        renderer = LAYOUT_RENDERERS[layout_name]
        renderer(slide, spec, deck, total, cfg, base_dir)

        # Embed native PowerPoint Speaker Notes
        try:
            notes_slide = slide.notes_slide
            notes_tf = notes_slide.notes_text_frame
            parts = [f"[Slide {spec.number} – {spec.title}]"]
            if spec.speaker_notes:
                parts.append(strip_markdown_inline(spec.speaker_notes))
            if spec.visual_suggestion:
                parts.append(f"\n[Đề xuất hình ảnh/sơ đồ]: {strip_markdown_inline(spec.visual_suggestion)}")
            notes_tf.text = "\n".join(parts)
        except Exception as exc:
            notes_embedded_ok = False
            notices.append(f"Không thể nhúng Speaker Notes vào Slide {spec.number}: {exc}")

    output_pptx.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output_pptx))

    saved_notes_path = ""
    if speaker_notes_file is not None or not notes_embedded_ok:
        target_notes = speaker_notes_file or output_pptx.with_name(f"Speaker_Notes_{output_pptx.stem}.md")
        export_speaker_notes_markdown(deck, target_notes)
        saved_notes_path = str(target_notes)

    return output_pptx, layout_log, notes_embedded_ok, saved_notes_path, notices
