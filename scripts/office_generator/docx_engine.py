"""Reusable Microsoft Word (.docx) rendering engine for Vietnamese education documents."""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Cm, Pt, RGBColor

from scripts.office_generator.markdown_parser import (
    parse_inline_spans,
    parse_markdown_blocks,
    strip_markdown_inline,
)
from scripts.office_generator.models import DocxTemplateConfig, MdBlock

WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def hex_to_rgb(hex_str: str) -> RGBColor:
    h = hex_str.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _set_run_font(
    run,
    font_name: str,
    size_pt: float,
    bold: bool = False,
    italic: bool = False,
    color: RGBColor | None = None,
) -> None:
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    rpr = run._r.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), font_name)


def _add_formatted_runs(
    paragraph,
    text: str,
    cfg: DocxTemplateConfig,
    base_size: float | None = None,
    base_bold: bool = False,
    base_italic: bool = False,
    base_color: RGBColor | None = None,
) -> None:
    size = base_size if base_size is not None else cfg.body_font_size
    color = base_color if base_color is not None else hex_to_rgb(cfg.text_hex)
    primary_rgb = hex_to_rgb(cfg.primary_hex)

    lines = text.split("\n")
    for idx, line in enumerate(lines):
        if idx > 0:
            paragraph.add_run().add_break()
        for span in parse_inline_spans(line):
            run = paragraph.add_run(span.text)
            if span.code:
                _set_run_font(
                    run,
                    cfg.code_font_name,
                    max(size - 1.5, 9.5),
                    bold=base_bold or span.bold,
                    italic=False,
                    color=WHITE if color == WHITE else primary_rgb,
                )
            else:
                _set_run_font(
                    run,
                    cfg.font_name,
                    size,
                    bold=base_bold or span.bold,
                    italic=base_italic or span.italic,
                    color=color,
                )


def _set_paragraph_shading(
    paragraph, fill_hex: str, border_hex: str, left_border_hex: str | None = None
) -> None:
    ppr = paragraph._p.get_or_add_pPr()
    ppr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))
    if left_border_hex:
        ppr.append(
            parse_xml(
                f'<w:pBdr {nsdecls("w")}>'
                f'<w:left w:val="single" w:sz="18" w:space="8" w:color="{left_border_hex}"/>'
                f'<w:top w:val="single" w:sz="4" w:space="4" w:color="{border_hex}"/>'
                f'<w:bottom w:val="single" w:sz="4" w:space="4" w:color="{border_hex}"/>'
                f'<w:right w:val="single" w:sz="4" w:space="6" w:color="{border_hex}"/>'
                f"</w:pBdr>"
            )
        )


def _set_paragraph_bottom_border(paragraph, color_hex: str, sz: int = 6) -> None:
    ppr = paragraph._p.get_or_add_pPr()
    ppr.append(
        parse_xml(
            f'<w:pBdr {nsdecls("w")}>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="4" w:color="{color_hex}"/>'
            f"</w:pBdr>"
        )
    )


def _set_cell_shading(cell, fill_hex: str) -> None:
    cell._tc.get_or_add_tcPr().append(
        parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    )


def _set_cell_margins(cell, top: int = 70, bottom: int = 70, left: int = 95, right: int = 95) -> None:
    cell._tc.get_or_add_tcPr().append(
        parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{top}" w:type="dxa"/>'
            f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
            f'<w:left w:w="{left}" w:type="dxa"/>'
            f'<w:right w:w="{right}" w:type="dxa"/>'
            f"</w:tcMar>"
        )
    )


def _set_table_borders(table, color_hex: str) -> None:
    table._tbl.tblPr.append(
        parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>'
            f'<w:left w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>'
            f'<w:right w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
            f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
            f"</w:tblBorders>"
        )
    )


def _set_row_cant_split(row) -> None:
    row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))


def _set_row_header(row) -> None:
    row._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))


def _add_field(paragraph, field_name: str, cfg: DocxTemplateConfig, size_pt: float = 10.0) -> None:
    run = paragraph.add_run()
    _set_run_font(run, cfg.font_name, size_pt, color=hex_to_rgb(cfg.muted_hex))
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = f" {field_name} "
    fld_sep = OxmlElement("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    for el in (fld_begin, instr, fld_sep, fld_end):
        run._r.append(el)


def _compute_column_widths(rows: List[List[str]], total_cm: float) -> List[float]:
    num_cols = len(rows[0])
    if num_cols == 1:
        return [round(total_cm, 2)]

    weights: List[float] = []
    for c in range(num_cols):
        hdr = strip_markdown_inline(rows[0][c]).lower()
        sample_lens = [len(strip_markdown_inline(r[c])) for r in rows[1 : min(len(rows), 12)]]
        avg_len = (sum(sample_lens) / len(sample_lens)) if sample_lens else len(hdr)
        if hdr in ("tt", "stt", "#", "câu"):
            w = 0.7
        elif "thời lượng" in hdr or hdr in ("tiết", "điểm", "tổng", "tỉ lệ", "tỉ lệ (%)", "tỷ lệ"):
            w = 1.5
        elif "mục tiêu" in hdr and avg_len < 30:
            w = 2.0
        else:
            w = max(1.8, min(avg_len / 12.0 + 1.4, 7.5))
        weights.append(w)

    total_w = sum(weights)
    widths = [round(total_cm * (w / total_w), 2) for w in weights]
    min_cm = 1.0 if num_cols >= 5 else 1.4
    adjusted = False
    for idx, val in enumerate(widths):
        if val < min_cm:
            widths[idx] = min_cm
            adjusted = True
    if adjusted:
        scale = total_cm / sum(widths)
        widths = [round(v * scale, 2) for v in widths]
    return widths


def _configure_section(section, cfg: DocxTemplateConfig, header_title: str) -> None:
    section.orientation = WD_ORIENT.PORTRAIT
    section.page_width = Cm(cfg.page_width_cm)
    section.page_height = Cm(cfg.page_height_cm)
    section.top_margin = Cm(cfg.margin_top_cm)
    section.bottom_margin = Cm(cfg.margin_bottom_cm)
    section.left_margin = Cm(cfg.margin_left_cm)
    section.right_margin = Cm(cfg.margin_right_cm)
    section.header_distance = Cm(1.0)
    section.footer_distance = Cm(1.0)
    section.different_first_page_header_footer = cfg.first_page_header_suppressed

    muted_rgb = hex_to_rgb(cfg.muted_hex)
    header_p = section.header.paragraphs[0]
    header_p.text = ""
    header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    h_text = cfg.header_text or header_title
    if cfg.school_name and cfg.school_name not in h_text:
        h_text = f"{cfg.school_name}  |  {h_text}"
    h_run = header_p.add_run(h_text)
    _set_run_font(h_run, cfg.font_name, 10.0, italic=True, color=muted_rgb)
    _set_paragraph_bottom_border(header_p, cfg.border_hex, sz=4)

    footer_prefix = cfg.footer_prefix or cfg.display_name
    if cfg.teacher_name:
        footer_prefix = f"{footer_prefix} – GV: {cfg.teacher_name}"

    for footer in (section.first_page_footer, section.footer):
        fp = footer.paragraphs[0]
        fp.text = ""
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_left = fp.add_run(f"{footer_prefix}   |   Trang ")
        _set_run_font(r_left, cfg.font_name, 10.0, italic=True, color=muted_rgb)
        _add_field(fp, "PAGE", cfg, 10.0)
        r_mid = fp.add_run(" / ")
        _set_run_font(r_mid, cfg.font_name, 10.0, color=muted_rgb)
        _add_field(fp, "NUMPAGES", cfg, 10.0)


def _add_optional_institution_header(doc: Document, cfg: DocxTemplateConfig, base_dir: Path | None) -> None:
    """Add optional school logo, school name, department, or teacher branding if configured."""
    if not any([cfg.school_name, cfg.department_name, cfg.teacher_name, cfg.logo_path, cfg.show_formal_banner]):
        return

    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    usable_cm = cfg.page_width_cm - cfg.margin_left_cm - cfg.margin_right_cm
    left_cell, right_cell = tbl.rows[0].cells[0], tbl.rows[0].cells[1]
    left_cell.width = Cm(usable_cm * 0.5)
    right_cell.width = Cm(usable_cm * 0.5)

    lp = left_cell.paragraphs[0]
    lp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if cfg.logo_path:
        logo_p = Path(cfg.logo_path)
        if not logo_p.is_absolute() and base_dir is not None:
            logo_p = (base_dir / logo_p).resolve()
        if logo_p.is_file():
            lp.add_run().add_picture(str(logo_p), width=Cm(1.8))
            lp.add_run().add_break()
    school_line = cfg.school_name or "TRƯỜNG THPT ................................"
    r1 = lp.add_run(school_line.upper())
    _set_run_font(r1, cfg.font_name, 11.5, bold=True, color=hex_to_rgb(cfg.primary_hex))
    if cfg.department_name:
        lp.add_run().add_break()
        r2 = lp.add_run(cfg.department_name)
        _set_run_font(r2, cfg.font_name, 11.0, bold=False, color=hex_to_rgb(cfg.text_hex))

    rp = right_cell.paragraphs[0]
    rp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = rp.add_run(cfg.display_name.upper())
    _set_run_font(r3, cfg.font_name, 11.5, bold=True, color=hex_to_rgb(cfg.primary_hex))
    if cfg.teacher_name:
        rp.add_run().add_break()
        r4 = rp.add_run(f"Giáo viên: {cfg.teacher_name}")
        _set_run_font(r4, cfg.font_name, 11.0, italic=True, color=hex_to_rgb(cfg.muted_hex))

    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)


def render_docx(
    markdown_text: str,
    output_docx: Path,
    cfg: DocxTemplateConfig,
    base_dir: Path | None = None,
) -> Tuple[Path, List[str]]:
    """Render Markdown text into a formatted Microsoft Word (.docx) file."""
    blocks, notices = parse_markdown_blocks(markdown_text)

    header_title = cfg.display_name
    for b in blocks:
        if b.kind == "heading" and b.level == 1:
            header_title = strip_markdown_inline(b.text)
            break

    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = cfg.font_name
    normal.font.size = Pt(cfg.body_font_size)
    normal.font.color.rgb = hex_to_rgb(cfg.text_hex)
    rpr = normal._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), cfg.font_name)

    _configure_section(doc.sections[0], cfg, header_title)
    _add_optional_institution_header(doc, cfg, base_dir)

    primary_rgb = hex_to_rgb(cfg.primary_hex)
    text_rgb = hex_to_rgb(cfg.text_hex)
    muted_rgb = hex_to_rgb(cfg.muted_hex)
    usable_cm = cfg.page_width_cm - cfg.margin_left_cm - cfg.margin_right_cm

    fig_counter = 0
    tbl_counter = 0

    for block in blocks:
        if block.kind == "hr":
            continue

        if block.kind == "page_break":
            doc.add_page_break()
            continue

        if block.kind == "section_break":
            new_sec = doc.add_section(WD_SECTION.NEW_PAGE)
            _configure_section(new_sec, cfg, header_title)
            continue

        if block.kind == "heading":
            p = doc.add_paragraph()
            p.paragraph_format.keep_with_next = True
            if block.level == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(10)
                _add_formatted_runs(p, block.text, cfg, base_size=cfg.heading1_size, base_bold=True, base_color=primary_rgb)
            elif block.level == 2:
                p.paragraph_format.space_before = Pt(12)
                p.paragraph_format.space_after = Pt(6)
                _add_formatted_runs(p, block.text, cfg, base_size=cfg.heading2_size, base_bold=True, base_color=primary_rgb)
                if cfg.show_heading2_underline:
                    _set_paragraph_bottom_border(p, cfg.primary_hex, sz=6)
            elif block.level == 3:
                p.paragraph_format.space_before = Pt(9)
                p.paragraph_format.space_after = Pt(4)
                _add_formatted_runs(p, block.text, cfg, base_size=cfg.heading3_size, base_bold=True, base_color=primary_rgb)
            else:
                p.paragraph_format.space_before = Pt(7)
                p.paragraph_format.space_after = Pt(3)
                _add_formatted_runs(p, block.text, cfg, base_size=cfg.heading4_size, base_bold=True, base_color=text_rgb)
            continue

        if block.kind == "quote":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.4)
            p.paragraph_format.right_indent = Cm(0.3)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing = cfg.line_spacing
            _add_formatted_runs(p, block.text, cfg, base_size=max(cfg.body_font_size - 1.0, 11.0), base_italic=True, base_color=text_rgb)
            _set_paragraph_shading(p, cfg.quote_bg_hex, cfg.border_hex, left_border_hex=cfg.accent_hex)
            continue

        if block.kind == "code":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            p.paragraph_format.right_indent = Cm(0.4)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing = 1.1
            for idx, code_line in enumerate(block.text.split("\n")):
                if idx > 0:
                    p.add_run().add_break()
                r = p.add_run(code_line)
                _set_run_font(r, cfg.code_font_name, max(cfg.body_font_size - 2.0, 10.0), color=text_rgb)
            _set_paragraph_shading(p, cfg.code_bg_hex, cfg.border_hex, left_border_hex=cfg.primary_hex)
            continue

        if block.kind == "image":
            img_path = Path(block.image_path)
            if not img_path.is_absolute() and base_dir is not None:
                img_path = (base_dir / img_path).resolve()
            if img_path.is_file():
                fig_counter += 1
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(6)
                p_img.paragraph_format.space_after = Pt(2)
                p_img.paragraph_format.keep_with_next = True
                p_img.add_run().add_picture(str(img_path), width=Cm(min(usable_cm * 0.78, 12.5)))
                cap_p = doc.add_paragraph()
                cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cap_p.paragraph_format.space_after = Pt(8)
                cap_text = block.caption or f"Hình {fig_counter}"
                if not cap_text.lower().startswith("hình"):
                    cap_text = f"Hình {fig_counter}. {cap_text}"
                r_cap = cap_p.add_run(cap_text)
                _set_run_font(r_cap, cfg.font_name, 11.5, italic=True, color=muted_rgb)
            else:
                notices.append(f"Không tìm thấy hình ảnh để chèn vào DOCX: {block.image_path}")
                p_miss = doc.add_paragraph()
                r_m = p_miss.add_run(f"[Hình ảnh chưa tìm thấy: {block.caption or block.image_path}]")
                _set_run_font(r_m, cfg.font_name, 11.5, italic=True, color=muted_rgb)
            continue

        if block.kind == "bullet":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.75 + block.level * 0.55)
            p.paragraph_format.first_line_indent = Cm(-0.35)
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(2.5)
            p.paragraph_format.line_spacing = cfg.line_spacing
            marker = "• " if block.level == 0 else ("– " if block.level == 1 else "▪ ")
            r_mark = p.add_run(marker)
            _set_run_font(r_mark, cfg.font_name, cfg.body_font_size, bold=(block.level == 0), color=primary_rgb)
            _add_formatted_runs(p, block.text, cfg)
            continue

        if block.kind == "numbered":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.8 + block.level * 0.55)
            p.paragraph_format.first_line_indent = Cm(-0.45)
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(2.5)
            p.paragraph_format.line_spacing = cfg.line_spacing
            _add_formatted_runs(p, block.text, cfg)
            continue

        if block.kind == "table" and block.rows:
            tbl_counter += 1
            num_cols = len(block.rows[0])
            table = doc.add_table(rows=len(block.rows), cols=num_cols)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.autofit = False
            _set_table_borders(table, cfg.border_hex)

            col_widths = _compute_column_widths(block.rows, total_cm=usable_cm)
            cell_font_size = cfg.table_font_size - 0.5 if num_cols >= 6 else cfg.table_font_size

            for r_idx, row_data in enumerate(block.rows):
                row = table.rows[r_idx]
                _set_row_cant_split(row)
                is_header = r_idx == 0
                if is_header:
                    _set_row_header(row)

                for c_idx, cell_text in enumerate(row_data):
                    cell = row.cells[c_idx]
                    cell.width = Cm(col_widths[c_idx])
                    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER if is_header else WD_ALIGN_VERTICAL.TOP
                    _set_cell_margins(cell)
                    if is_header:
                        _set_cell_shading(cell, cfg.primary_hex)
                    elif r_idx % 2 == 0:
                        _set_cell_shading(cell, cfg.table_alt_row_hex)

                    cp = cell.paragraphs[0]
                    cp.paragraph_format.space_before = Pt(1)
                    cp.paragraph_format.space_after = Pt(1)
                    cp.paragraph_format.line_spacing = 1.1
                    if is_header:
                        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        _add_formatted_runs(cp, cell_text, cfg, base_size=cell_font_size, base_bold=True, base_color=WHITE)
                    else:
                        _add_formatted_runs(cp, cell_text, cfg, base_size=cell_font_size, base_color=text_rgb)

            if block.caption:
                cap_p = doc.add_paragraph()
                cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cap_p.paragraph_format.space_before = Pt(2)
                cap_p.paragraph_format.space_after = Pt(6)
                r_tc = cap_p.add_run(block.caption)
                _set_run_font(r_tc, cfg.font_name, 11.0, italic=True, color=muted_rgb)
            else:
                sp = doc.add_paragraph()
                sp.paragraph_format.space_before = Pt(0)
                sp.paragraph_format.space_after = Pt(4)
            continue

        # Regular paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = cfg.line_spacing
        _add_formatted_runs(p, block.text, cfg)

    output_docx.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_docx))
    return output_docx, notices
