#!/usr/bin/env python3
"""Backward-compatible wrapper delegating to `scripts/office_generator`."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.office_generator import generate_document  # noqa: E402


def build_docx_from_markdown(input_md: Path, output_docx: Path, font_size: float = 13.0) -> Path:
    res = generate_document(
        source_file=input_md,
        output_file=output_docx,
        format="docx",
        template="khbd",
        overrides={"body_font_size": font_size},
    )
    if not res.success:
        raise RuntimeError(res.error_message or "DOCX generation failed")
    return Path(res.output_file)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compatibility wrapper -> scripts/office_generator/cli.py docx")
    parser.add_argument("input_md", type=Path)
    parser.add_argument("output_docx", type=Path, nargs="?", default=None)
    parser.add_argument("--font-size", type=float, default=13.0)
    args = parser.parse_args()
    out = args.output_docx or args.input_md.with_suffix(".docx")
    saved = build_docx_from_markdown(args.input_md, out, font_size=args.font_size)
    print(f"OK: Đã tạo tệp DOCX tại {saved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
