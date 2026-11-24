"""Controlled PDF export engine (uses LibreOffice soffice or docx2pdf when installed).

Never fabricates a PDF or claims success if no real PDF conversion backend exists.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Optional


class PdfBackendUnavailableError(RuntimeError):
    """Raised when neither LibreOffice (soffice) nor docx2pdf is available."""


def detect_pdf_backend() -> Optional[str]:
    """Detect available PDF conversion backend on the current machine."""
    if shutil.which("soffice"):
        return "libreoffice"
    try:
        import docx2pdf  # noqa: F401

        return "docx2pdf"
    except ImportError:
        return None


def convert_to_pdf(input_office_file: Path, output_pdf: Path) -> Path:
    """Convert an existing DOCX or PPTX file into PDF using a verified local backend."""
    if not input_office_file.is_file():
        raise FileNotFoundError(f"Không tìm thấy tệp nguồn để xuất PDF: {input_office_file}")

    backend = detect_pdf_backend()
    if backend is None:
        raise PdfBackendUnavailableError(
            "Không tìm thấy công cụ xuất PDF khả dụng (LibreOffice `soffice` hoặc `docx2pdf`). "
            "Cài đặt LibreOffice (https://www.libreoffice.org/) hoặc `pip install docx2pdf` (cần Microsoft Word) "
            "để kích hoạt chức năng xuất PDF."
        )

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    if backend == "libreoffice":
        cmd = [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(output_pdf.parent),
            str(input_office_file),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            raise RuntimeError(f"LibreOffice xuất PDF thất bại: {proc.stderr.strip()}")
        produced = output_pdf.parent / f"{input_office_file.stem}.pdf"
        if produced != output_pdf and produced.is_file():
            produced.replace(output_pdf)
        if not output_pdf.is_file():
            raise RuntimeError(f"LibreOffice không tạo ra tệp PDF mong đợi tại {output_pdf}")
        return output_pdf

    # docx2pdf backend (DOCX only)
    if input_office_file.suffix.lower() != ".docx":
        raise PdfBackendUnavailableError(
            "`docx2pdf` chỉ hỗ trợ chuyển đổi tệp .docx sang .pdf. Để xuất .pptx sang .pdf cần cài đặt LibreOffice (`soffice`)."
        )
    from docx2pdf import convert  # type: ignore

    convert(str(input_office_file), str(output_pdf))
    return output_pdf
