"""Shared QA Validator for generated DOCX and PPTX Office files."""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import List, Optional

from docx import Document
from pptx import Presentation

from scripts.office_generator.markdown_parser import (
    load_slide_deck,
    parse_markdown_blocks,
    strip_markdown_inline,
)
from scripts.office_generator.models import ValidationIssue, ValidationReport

VIETNAMESE_DIACRITICS_RE = re.compile(
    r"[ăâđêôơưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]",
    re.IGNORECASE,
)


def validate_docx(
    docx_path: Path,
    source_md: Optional[Path] = None,
    unconvertible_notes: Optional[List[str]] = None,
) -> ValidationReport:
    """Validate a generated DOCX file thoroughly using python-docx."""
    issues: List[ValidationIssue] = []
    metrics: dict = {}

    if not docx_path.is_file():
        issues.append(ValidationIssue("error", "file_error", f"Tệp DOCX không tồn tại: {docx_path}"))
        return ValidationReport(str(docx_path), "docx", False, metrics, issues, str(source_md or ""))

    try:
        doc = Document(str(docx_path))
    except Exception as exc:
        issues.append(ValidationIssue("error", "file_error", f"Không thể mở tệp DOCX bằng python-docx: {exc}"))
        return ValidationReport(str(docx_path), "docx", False, metrics, issues, str(source_md or ""))

    sec = doc.sections[0]
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    table_texts = [c.text.strip() for t in doc.tables for r in t.rows for c in r.cells if c.text.strip()]
    full_text = "\n".join(paragraphs + table_texts)

    metrics = {
        "file_size_bytes": docx_path.stat().st_size,
        "page_width_cm": round(sec.page_width.cm, 2),
        "page_height_cm": round(sec.page_height.cm, 2),
        "paragraph_count": len(paragraphs),
        "table_count": len(doc.tables),
        "inline_image_count": len(doc.inline_shapes),
        "has_page_numbers": ("PAGE" in sec.footer._element.xml),
        "vietnamese_chars_detected": bool(VIETNAMESE_DIACRITICS_RE.search(full_text)),
    }

    if not paragraphs and not table_texts:
        issues.append(ValidationIssue("error", "content_error", "Tệp DOCX không có nội dung văn bản nào."))

    # Check A4 format
    if not (20.5 <= metrics["page_width_cm"] <= 21.5 and 29.0 <= metrics["page_height_cm"] <= 30.2):
        issues.append(
            ValidationIssue(
                "warning",
                "format_warning",
                f"Kích thước trang ({metrics['page_width_cm']}×{metrics['page_height_cm']} cm) khác khổ A4 chuẩn (21×29,7 cm).",
            )
        )

    # Check tables for valid row/col structure
    for idx, tbl in enumerate(doc.tables, 1):
        if len(tbl.rows) == 0 or len(tbl.columns) == 0:
            issues.append(ValidationIssue("error", "format_warning", f"Bảng {idx} rỗng.", f"Table {idx}"))

    # Source parity verification
    if source_md and source_md.is_file():
        src_text = source_md.read_text(encoding="utf-8")
        src_blocks, _ = parse_markdown_blocks(src_text)
        src_headings = [strip_markdown_inline(b.text) for b in src_blocks if b.kind == "heading"]
        src_tables = [b for b in src_blocks if b.kind == "table"]

        metrics["source_heading_count"] = len(src_headings)
        metrics["source_table_count"] = len(src_tables)

        full_lower = full_text.lower()
        missing_headings = [h for h in src_headings if h and h.lower() not in full_lower]
        if missing_headings:
            issues.append(
                ValidationIssue(
                    "error",
                    "content_error",
                    f"Thiếu {len(missing_headings)} tiêu đề từ nguồn Markdown: {missing_headings[:3]}",
                )
            )
        if len(doc.tables) < len(src_tables):
            issues.append(
                ValidationIssue(
                    "error",
                    "content_error",
                    f"Số bảng trong DOCX ({len(doc.tables)}) ít hơn nguồn Markdown ({len(src_tables)}).",
                )
            )
        if VIETNAMESE_DIACRITICS_RE.search(src_text) and not metrics["vietnamese_chars_detected"]:
            issues.append(
                ValidationIssue("error", "content_error", "Nguồn có tiếng Việt có dấu nhưng DOCX bị mất dấu tiếng Việt.")
            )

    for note in unconvertible_notes or []:
        issues.append(ValidationIssue("warning", "unconvertible", note))

    passed = not any(i.severity == "error" for i in issues)
    return ValidationReport(str(docx_path), "docx", passed, metrics, issues, str(source_md or ""))


def validate_pptx(
    pptx_path: Path,
    source_file: Optional[Path] = None,
    unconvertible_notes: Optional[List[str]] = None,
) -> ValidationReport:
    """Validate a generated PPTX file thoroughly using python-pptx."""
    issues: List[ValidationIssue] = []
    metrics: dict = {}

    if not pptx_path.is_file():
        issues.append(ValidationIssue("error", "file_error", f"Tệp PPTX không tồn tại: {pptx_path}"))
        return ValidationReport(str(pptx_path), "pptx", False, metrics, issues, str(source_file or ""))

    try:
        prs = Presentation(str(pptx_path))
    except Exception as exc:
        issues.append(ValidationIssue("error", "file_error", f"Không thể mở tệp PPTX bằng python-pptx: {exc}"))
        return ValidationReport(str(pptx_path), "pptx", False, metrics, issues, str(source_file or ""))

    total_slides = len(prs.slides)
    ratio = round(prs.slide_width / prs.slide_height, 3) if prs.slide_height else 0.0
    empty_slides: List[int] = []
    notes_present = 0
    table_count = 0
    image_count = 0
    overflow_items: List[str] = []
    all_text_parts: List[str] = []

    for s_idx, slide in enumerate(prs.slides, 1):
        slide_texts: List[str] = []
        for sh in slide.shapes:
            if sh.shape_type == 13:  # MSO_SHAPE_TYPE.PICTURE
                image_count += 1
            if sh.has_table:
                table_count += 1
                for r in sh.table.rows:
                    for c in r.cells:
                        if c.text.strip():
                            slide_texts.append(c.text.strip())
            if sh.has_text_frame:
                txt = sh.text_frame.text.strip()
                if txt:
                    slide_texts.append(txt)
                    # Estimate overflow against textbox height
                    w_in = max(sh.width.inches - 0.16, 0.5)
                    h_in = max(sh.height.inches - 0.08, 0.2)
                    est_h_pt = 0.0
                    for p in sh.text_frame.paragraphs:
                        ptxt = p.text
                        if not ptxt:
                            continue
                        sizes = [r.font.size.pt for r in p.runs if r.font.size]
                        fs = max(sizes) if sizes else 14.0
                        cpl = max(int((w_in * 72.0) / (fs * 0.53)), 8)
                        n_lines = max(1, math.ceil(len(ptxt) / cpl))
                        sp = p.space_after.pt if p.space_after else 3.0
                        est_h_pt += n_lines * (fs * 1.28) + sp
                    avail_h_pt = h_in * 72.0
                    if est_h_pt > avail_h_pt * 1.15 and len(txt) > 30:
                        overflow_items.append(
                            f"Slide {s_idx}: '{txt[:40]}...' (ước lượng {est_h_pt:.0f}pt > {avail_h_pt:.0f}pt)"
                        )
        if not slide_texts:
            empty_slides.append(s_idx)
        all_text_parts.extend(slide_texts)
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip():
            notes_present += 1

    full_text = "\n".join(all_text_parts)
    metrics = {
        "file_size_bytes": pptx_path.stat().st_size,
        "slide_width_in": round(prs.slide_width.inches, 3),
        "slide_height_in": round(prs.slide_height.inches, 3),
        "aspect_ratio": ratio,
        "slide_count": total_slides,
        "empty_slide_count": len(empty_slides),
        "slides_with_speaker_notes": notes_present,
        "native_table_count": table_count,
        "embedded_image_count": image_count,
        "overflow_warning_count": len(overflow_items),
        "vietnamese_chars_detected": bool(VIETNAMESE_DIACRITICS_RE.search(full_text)),
    }

    if total_slides == 0:
        issues.append(ValidationIssue("error", "content_error", "Tệp PPTX không có slide nào."))
    if empty_slides:
        issues.append(ValidationIssue("error", "content_error", f"Phát hiện slide rỗng: {empty_slides}"))
    if abs(ratio - (16 / 9)) > 0.03:
        issues.append(ValidationIssue("warning", "format_warning", f"Tỷ lệ slide ({ratio}) khác chuẩn 16:9 (1.778)."))
    for ov in overflow_items:
        issues.append(ValidationIssue("warning", "format_warning", f"Nguy cơ tràn chữ – {ov}"))

    # Source parity verification
    if source_file and source_file.is_file():
        try:
            src_deck = load_slide_deck(source_file)
            metrics["source_slide_count"] = len(src_deck.slides)
            if total_slides != len(src_deck.slides):
                issues.append(
                    ValidationIssue(
                        "error",
                        "content_error",
                        f"Số slide PPTX ({total_slides}) không khớp nguồn ({len(src_deck.slides)}).",
                    )
                )
            matched_titles = 0
            for idx, ms in enumerate(src_deck.slides):
                if idx >= total_slides:
                    break
                sl_txt = " ".join(
                    sh.text_frame.text for sh in prs.slides[idx].shapes if sh.has_text_frame
                )
                if ms.title in sl_txt:
                    matched_titles += 1
                else:
                    issues.append(
                        ValidationIssue(
                            "error",
                            "content_error",
                            f"Tiêu đề Slide {ms.number} ('{ms.title}') không xuất hiện trên slide PPTX.",
                            f"Slide {ms.number}",
                        )
                    )
            metrics["matched_title_count"] = matched_titles
        except Exception as exc:
            issues.append(ValidationIssue("warning", "format_warning", f"Không thể đối chiếu nguồn slide: {exc}"))

    for note in unconvertible_notes or []:
        issues.append(ValidationIssue("warning", "unconvertible", note))

    passed = not any(i.severity == "error" for i in issues)
    return ValidationReport(str(pptx_path), "pptx", passed, metrics, issues, str(source_file or ""))


def validate_document(
    file_path: Path,
    source_file: Optional[Path] = None,
    unconvertible_notes: Optional[List[str]] = None,
) -> ValidationReport:
    """Auto-dispatch validation by file extension (.docx or .pptx)."""
    ext = file_path.suffix.lower()
    if ext == ".docx":
        return validate_docx(file_path, source_file, unconvertible_notes)
    if ext == ".pptx":
        return validate_pptx(file_path, source_file, unconvertible_notes)
    return ValidationReport(
        str(file_path),
        ext.lstrip("."),
        False,
        {},
        [ValidationIssue("error", "file_error", f"Định dạng không hỗ trợ kiểm định tự động: {ext}")],
        str(source_file or ""),
    )


def format_validation_report_markdown(reports: List[ValidationReport], title: str = "BÁO CÁO KIỂM ĐỊNH XUẤT TÀI LIỆU OFFICE") -> str:
    """Render one or more ValidationReport objects as a clean Markdown QA report."""
    lines = [f"# {title}", ""]
    for rep in reports:
        status = "PASS" if rep.passed else "FAIL"
        lines.append(f"## {Path(rep.file_path).name} (`{rep.file_format.upper()}`) — **{status}**")
        lines.append(f"- **Tệp đầu ra:** `{rep.file_path}`")
        if rep.source_file:
            lines.append(f"- **Tệp nguồn:** `{rep.source_file}`")
        lines.append(f"- **Lỗi nghiêm trọng (errors):** {len(rep.errors)} | **Cảnh báo (warnings):** {len(rep.warnings)}")
        if rep.metrics:
            lines.append("\n| Chỉ số kiểm định | Giá trị thực đo |")
            lines.append("|---|---|")
            for k, v in rep.metrics.items():
                lines.append(f"| `{k}` | `{v}` |")
        if rep.issues:
            lines.append("\n### Chi tiết vấn đề phát hiện")
            for issue in rep.issues:
                loc = f" ({issue.location})" if issue.location else ""
                lines.append(f"- **[{issue.severity.upper()} / {issue.category}]{loc}:** {issue.message}")
        else:
            lines.append("\n- Không phát hiện lỗi nội dung hoặc lỗi định dạng.")
        lines.append("")
    return "\n".join(lines)
