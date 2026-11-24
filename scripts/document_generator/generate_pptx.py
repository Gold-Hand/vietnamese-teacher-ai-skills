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


def build_pptx_from_markdown(input_md: Path, output_pptx: Path):
    res = generate_document(
        source_file=input_md,
        output_file=output_pptx,
        format="pptx",
        template="education",
    )
    if not res.success:
        raise RuntimeError(res.error_message or "PPTX generation failed")
    return Path(res.output_file), [(idx + 1, name) for idx, name in enumerate(res.layouts_used)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Compatibility wrapper -> scripts/office_generator/cli.py pptx")
    parser.add_argument("input_md", type=Path)
    parser.add_argument("output_pptx", type=Path, nargs="?", default=None)
    args = parser.parse_args()
    out = args.output_pptx or args.input_md.with_suffix(".pptx")
    saved, layouts = build_pptx_from_markdown(args.input_md, out)
    print(f"OK: Đã tạo tệp PPTX tại {saved} (layouts={len(layouts)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
