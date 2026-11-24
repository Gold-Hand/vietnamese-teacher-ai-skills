#!/usr/bin/env python3
"""Unified CLI for the Vietnamese Teacher AI shared Office Document Generator.

Examples (Windows PowerShell / Gemini CLI / Antigravity):
    python scripts/office_generator/cli.py docx --input input.md --output output.docx --template khbd
    python scripts/office_generator/cli.py pptx --input slides.md --output slides.pptx --template education
    python scripts/office_generator/cli.py validate --input output.docx --source input.md
    python scripts/office_generator/cli.py batch --config batch.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.office_generator.generator import generate_document, run_batch  # noqa: E402
from scripts.office_generator.validator import (  # noqa: E402
    format_validation_report_markdown,
    validate_document,
)


def _collect_overrides(args: argparse.Namespace) -> Dict:
    ov: Dict = {}
    for key in ("school_name", "department_name", "teacher_name", "logo_path", "header_text", "footer_text", "font_name", "body_font_size"):
        val = getattr(args, key, None)
        if val is not None:
            ov[key] = val
    return ov


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="office-generator",
        description="Công cụ xuất và kiểm định tài liệu Microsoft Office (DOCX, PPTX, PDF) dùng chung cho Vietnamese Teacher AI Skills.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # docx subcommand
    p_docx = sub.add_parser("docx", help="Xuất Markdown sang Microsoft Word (.docx)")
    p_docx.add_argument("--input", required=True, help="Đường dẫn tệp Markdown đầu vào")
    p_docx.add_argument("--output", required=True, help="Đường dẫn tệp .docx đầu ra")
    p_docx.add_argument(
        "--template",
        default="khbd",
        help="Tên mẫu DOCX (khbd, assessment/exam, matrix, answer_key, study_material, teacher_guide, general)",
    )
    p_docx.add_argument("--font-size", dest="body_font_size", type=float, default=None, help="Cỡ chữ nội dung (13 hoặc 14)")
    p_docx.add_argument("--school-name", dest="school_name", default=None, help="Tên trường (tùy chọn)")
    p_docx.add_argument("--department-name", dest="department_name", default=None, help="Tên tổ chuyên môn (tùy chọn)")
    p_docx.add_argument("--teacher-name", dest="teacher_name", default=None, help="Tên giáo viên (tùy chọn)")
    p_docx.add_argument("--logo", dest="logo_path", default=None, help="Đường dẫn logo trường (tùy chọn)")
    p_docx.add_argument("--report", default=None, help="Lưu báo cáo kiểm định Markdown (tùy chọn)")
    p_docx.add_argument("--no-validate", action="store_true", help="Bỏ qua bước kiểm định tự động")

    # pptx subcommand
    p_pptx = sub.add_parser("pptx", help="Xuất kịch bản slide (Markdown/JSON) sang PowerPoint (.pptx)")
    p_pptx.add_argument("--input", required=True, help="Đường dẫn tệp kịch bản slide (.md hoặc .json)")
    p_pptx.add_argument("--output", required=True, help="Đường dẫn tệp .pptx đầu ra")
    p_pptx.add_argument("--template", default="education", help="Tên theme PPTX (education, lesson, assessment)")
    p_pptx.add_argument("--speaker-notes", default=None, help="Đường dẫn xuất thêm tệp Speaker Notes (.md)")
    p_pptx.add_argument("--school-name", dest="school_name", default=None, help="Tên trường (tùy chọn)")
    p_pptx.add_argument("--teacher-name", dest="teacher_name", default=None, help="Tên giáo viên (tùy chọn)")
    p_pptx.add_argument("--logo", dest="logo_path", default=None, help="Đường dẫn logo trường (tùy chọn)")
    p_pptx.add_argument("--report", default=None, help="Lưu báo cáo kiểm định Markdown (tùy chọn)")
    p_pptx.add_argument("--no-validate", action="store_true", help="Bỏ qua bước kiểm định tự động")

    # pdf subcommand
    p_pdf = sub.add_parser("pdf", help="Chuyển DOCX/PPTX sang PDF (cần LibreOffice soffice hoặc docx2pdf)")
    p_pdf.add_argument("--input", required=True, help="Đường dẫn tệp .docx hoặc .pptx")
    p_pdf.add_argument("--output", required=True, help="Đường dẫn tệp .pdf đầu ra")

    # validate subcommand
    p_val = sub.add_parser("validate", help="Kiểm định chất lượng tệp DOCX hoặc PPTX")
    p_val.add_argument("--input", required=True, help="Đường dẫn tệp .docx hoặc .pptx cần kiểm định")
    p_val.add_argument("--source", default=None, help="Tệp Markdown/JSON nguồn để đối chiếu nội dung (tùy chọn)")
    p_val.add_argument("--report", default=None, help="Đường dẫn lưu báo cáo kiểm định Markdown (tùy chọn)")
    p_val.add_argument("--json", action="store_true", help="In kết quả dưới dạng JSON")

    # batch subcommand
    p_batch = sub.add_parser("batch", help="Xuất hàng loạt nhiều tệp Office từ tệp cấu hình JSON")
    p_batch.add_argument("--config", required=True, help="Đường dẫn tệp cấu hình batch.json")

    args = parser.parse_args(argv)

    if args.command in ("docx", "pptx"):
        res = generate_document(
            source_file=args.input,
            output_file=args.output,
            format=args.command,
            template=args.template,
            overrides=_collect_overrides(args) or None,
            validate=(not args.no_validate),
            speaker_notes_file=getattr(args, "speaker_notes", None),
            report_file=args.report,
        )
        if not res.success:
            print(f"FAIL: {res.error_message or 'Kiểm định phát hiện lỗi.'}", file=sys.stderr)
            if res.validation:
                for issue in res.validation.errors:
                    print(f"  - [{issue.category}] {issue.message}", file=sys.stderr)
            return 1
        extra = ""
        if args.command == "pptx":
            extra = f" | layouts={len(res.layouts_used)} ({', '.join(res.layouts_used)})"
            if res.speaker_notes_file:
                extra += f" | notes={res.speaker_notes_file}"
        val_txt = ""
        if res.validation:
            val_txt = f" | validation={'PASS' if res.validation.passed else 'FAIL'} (warnings={len(res.validation.warnings)})"
        print(f"OK [{args.command.upper()}]: {res.output_file} (template={res.template}){extra}{val_txt}")
        return 0

    if args.command == "pdf":
        res = generate_document(source_file=args.input, output_file=args.output, format="pdf")
        if not res.success:
            print(f"ERROR [PDF]: {res.error_message}", file=sys.stderr)
            return 1
        print(f"OK [PDF]: {res.output_file}")
        return 0

    if args.command == "validate":
        rep = validate_document(Path(args.input), Path(args.source) if args.source else None)
        if args.report:
            rp = Path(args.report)
            rp.parent.mkdir(parents=True, exist_ok=True)
            rp.write_text(format_validation_report_markdown([rep]), encoding="utf-8")
        if args.json:
            print(json.dumps(rep.to_dict(), ensure_ascii=False, indent=2))
        else:
            status = "PASS" if rep.passed else "FAIL"
            print(f"VALIDATE [{status}]: {rep.file_path} | errors={len(rep.errors)}, warnings={len(rep.warnings)}")
            for issue in rep.issues:
                print(f"  - [{issue.severity.upper()}/{issue.category}] {issue.message}")
        return 0 if rep.passed else 1

    if args.command == "batch":
        results = run_batch(args.config)
        all_ok = True
        for res in results:
            flag = "OK" if res.success else "FAIL"
            if not res.success:
                all_ok = False
            print(f"{flag} [{res.file_format.upper()}]: {res.output_file} (template={res.template})")
            if res.error_message:
                print(f"   -> {res.error_message}", file=sys.stderr)
        return 0 if all_ok else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
