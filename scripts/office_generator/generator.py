"""Unified public API for the shared Vietnamese Teacher AI Office Document Generator."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.office_generator.docx_engine import render_docx
from scripts.office_generator.markdown_parser import load_slide_deck
from scripts.office_generator.models import GenerationResult, SlideDeck
from scripts.office_generator.pdf_engine import PdfBackendUnavailableError, convert_to_pdf
from scripts.office_generator.pptx_engine import render_pptx
from scripts.office_generator.validator import (
    format_validation_report_markdown,
    validate_document,
)
from templates.office.docx import resolve_docx_template
from templates.office.pptx import resolve_pptx_template


def generate_document(
    source_file: Optional[str | Path] = None,
    output_file: str | Path = "",
    format: str = "docx",
    template: str = "",
    *,
    slide_deck: Optional[SlideDeck] = None,
    overrides: Optional[Dict[str, Any]] = None,
    validate: bool = True,
    speaker_notes_file: Optional[str | Path] = None,
    report_file: Optional[str | Path] = None,
) -> GenerationResult:
    """Unified entry point used by all Agent Skills to generate DOCX, PPTX, or PDF.

    Examples:
        generate_document("01_KHBD.md", "KHBD.docx", format="docx", template="khbd")
        generate_document("02_Slides.md", "Slides.pptx", format="pptx", template="education")
    """
    fmt = format.strip().lower()
    if not output_file:
        raise ValueError("Tham số `output_file` không được để trống.")

    out_path = Path(output_file)
    src_path = Path(source_file) if source_file else None
    base_dir = src_path.parent if src_path else Path.cwd()

    if fmt == "docx":
        if src_path is None or not src_path.is_file():
            return GenerationResult(
                success=False,
                output_file=str(out_path),
                file_format="docx",
                template=template or "general",
                source_file=str(src_path or ""),
                error_message=f"Không tìm thấy tệp nguồn Markdown: {src_path}",
            )
        tmpl_name = template or "general"
        cfg = resolve_docx_template(tmpl_name, overrides)
        md_text = src_path.read_text(encoding="utf-8")
        saved, notices = render_docx(md_text, out_path, cfg, base_dir=base_dir)
        val_report = validate_document(saved, src_path, notices) if validate else None
        if report_file and val_report:
            rp = Path(report_file)
            rp.parent.mkdir(parents=True, exist_ok=True)
            rp.write_text(format_validation_report_markdown([val_report]), encoding="utf-8")
        return GenerationResult(
            success=(val_report.passed if val_report else True),
            output_file=str(saved),
            file_format="docx",
            template=tmpl_name,
            source_file=str(src_path),
            unconvertible_notes=notices,
            validation=val_report,
        )

    if fmt == "pptx":
        tmpl_name = template or "education"
        cfg = resolve_pptx_template(tmpl_name, overrides)
        if slide_deck is None:
            if src_path is None or not src_path.is_file():
                return GenerationResult(
                    success=False,
                    output_file=str(out_path),
                    file_format="pptx",
                    template=tmpl_name,
                    source_file=str(src_path or ""),
                    error_message=f"Không tìm thấy tệp nguồn slide: {src_path}",
                )
            deck = load_slide_deck(src_path)
        else:
            deck = slide_deck

        notes_target = Path(speaker_notes_file) if speaker_notes_file else None
        saved, layout_log, notes_embedded, notes_md_path, notices = render_pptx(
            deck, out_path, cfg, base_dir=base_dir, speaker_notes_file=notes_target
        )
        val_report = validate_document(saved, src_path, notices) if validate else None
        if report_file and val_report:
            rp = Path(report_file)
            rp.parent.mkdir(parents=True, exist_ok=True)
            rp.write_text(format_validation_report_markdown([val_report]), encoding="utf-8")
        return GenerationResult(
            success=(val_report.passed if val_report else True),
            output_file=str(saved),
            file_format="pptx",
            template=tmpl_name,
            source_file=str(src_path or ""),
            speaker_notes_file=notes_md_path,
            speaker_notes_embedded=notes_embedded,
            layouts_used=sorted({name for _, name in layout_log}),
            unconvertible_notes=notices,
            validation=val_report,
        )

    if fmt == "pdf":
        if src_path is None or not src_path.is_file():
            return GenerationResult(
                success=False,
                output_file=str(out_path),
                file_format="pdf",
                template=template or "default",
                source_file=str(src_path or ""),
                error_message=f"Không tìm thấy tệp nguồn để xuất PDF: {src_path}",
            )
        try:
            saved = convert_to_pdf(src_path, out_path)
            return GenerationResult(
                success=True,
                output_file=str(saved),
                file_format="pdf",
                template=template or "default",
                source_file=str(src_path),
            )
        except (PdfBackendUnavailableError, Exception) as exc:
            return GenerationResult(
                success=False,
                output_file=str(out_path),
                file_format="pdf",
                template=template or "default",
                source_file=str(src_path),
                error_message=str(exc),
            )

    raise ValueError(f"Định dạng '{format}' không được hỗ trợ. Hỗ trợ: docx, pptx, pdf.")


def run_batch(config_path: str | Path) -> List[GenerationResult]:
    """Execute batch generation of multiple Office files from a JSON configuration file."""
    cfg_file = Path(config_path)
    if not cfg_file.is_file():
        raise FileNotFoundError(f"Không tìm thấy tệp cấu hình batch: {cfg_file}")
    payload = json.loads(cfg_file.read_text(encoding="utf-8"))
    global_overrides = payload.get("overrides", {})
    jobs = payload.get("jobs", [])
    results: List[GenerationResult] = []
    reports = []

    for job in jobs:
        merged_overrides = {**global_overrides, **job.get("overrides", {})}
        res = generate_document(
            source_file=job.get("input") or job.get("source_file"),
            output_file=job["output"],
            format=job["format"],
            template=job.get("template", ""),
            overrides=merged_overrides or None,
            validate=job.get("validate", True),
            speaker_notes_file=job.get("speaker_notes"),
        )
        results.append(res)
        if res.validation is not None:
            reports.append(res.validation)

    report_out = payload.get("report_file")
    if report_out and reports:
        rp = Path(report_out)
        rp.parent.mkdir(parents=True, exist_ok=True)
        rp.write_text(format_validation_report_markdown(reports), encoding="utf-8")

    return results
