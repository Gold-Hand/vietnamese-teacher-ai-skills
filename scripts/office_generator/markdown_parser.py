"""Markdown and structured Slide Script parser for the shared Office Document Generator."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import List, Tuple

from scripts.office_generator.models import InlineSpan, MdBlock, SlideDeck, SlideModel

INLINE_TOKEN_RE = re.compile(
    r"(\*\*[^*]+\*\*|`[^`]+`|\*(?!\s)[^*]+(?<!\s)\*)"
)
IMAGE_RE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")
PAGE_BREAK_RE = re.compile(r"^(?:<!--\s*pagebreak\s*-->|\\pagebreak|---pagebreak---)\s*$", re.IGNORECASE)
SECTION_BREAK_RE = re.compile(r"^(?:<!--\s*sectionbreak\s*-->|\\sectionbreak|---sectionbreak---)\s*$", re.IGNORECASE)


def clean_html_entities(text: str) -> str:
    """Convert common Markdown/HTML line-break and spacing entities cleanly."""
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = text.replace("&nbsp;", " ").replace("&emsp;", "   ")
    return html.unescape(text)


def strip_markdown_inline(text: str) -> str:
    """Strip Markdown inline formatting markers while preserving plain text."""
    text = clean_html_entities(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*(?!\s)([^*]+)(?<!\s)\*", r"\1", text)
    return text.strip()


def parse_inline_spans(text: str) -> List[InlineSpan]:
    """Parse inline **bold**, *italic*, and `code` spans."""
    text = clean_html_entities(text)
    spans: List[InlineSpan] = []
    pos = 0
    for match in INLINE_TOKEN_RE.finditer(text):
        if match.start() > pos:
            spans.append(InlineSpan(text=text[pos : match.start()]))
        token = match.group(0)
        if token.startswith("**") and token.endswith("**"):
            inner = token[2:-2]
            if inner.startswith("`") and inner.endswith("`") and len(inner) > 2:
                spans.append(InlineSpan(text=inner[1:-1], bold=True, code=True))
            else:
                spans.append(InlineSpan(text=inner, bold=True))
        elif token.startswith("`") and token.endswith("`"):
            spans.append(InlineSpan(text=token[1:-1], code=True))
        elif token.startswith("*") and token.endswith("*"):
            spans.append(InlineSpan(text=token[1:-1], italic=True))
        pos = match.end()
    if pos < len(text):
        spans.append(InlineSpan(text=text[pos:]))
    return spans or [InlineSpan(text="")]


def _is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if "|" not in stripped:
        return False
    cells = [c.strip() for c in stripped.strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)


def _split_pipes_outside_backticks(line: str) -> List[str]:
    """Split a Markdown table row on pipes '|' that are unescaped and outside backticks."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]

    parts: List[str] = []
    buf: List[str] = []
    in_code = False
    i = 0
    while i < len(stripped):
        ch = stripped[i]
        if ch == "\\" and i + 1 < len(stripped) and stripped[i + 1] == "|":
            buf.append("|")
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
            buf.append(ch)
            i += 1
            continue
        if ch == "|" and not in_code:
            parts.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    parts.append("".join(buf).strip())
    return parts


def parse_markdown_blocks(markdown_text: str) -> Tuple[List[MdBlock], List[str]]:
    """Parse Markdown into structured MdBlock items plus any unconvertible-element notices."""
    lines = markdown_text.replace("\r\n", "\n").split("\n")
    blocks: List[MdBlock] = []
    notices: List[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if PAGE_BREAK_RE.match(stripped):
            blocks.append(MdBlock(kind="page_break"))
            i += 1
            continue

        if SECTION_BREAK_RE.match(stripped):
            blocks.append(MdBlock(kind="section_break"))
            i += 1
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            blocks.append(MdBlock(kind="hr"))
            i += 1
            continue

        # Image block: ![Caption](path/to/image.png)
        img_match = IMAGE_RE.match(stripped)
        if img_match:
            alt_text = img_match.group(1).strip()
            img_path = img_match.group(2).strip()
            blocks.append(MdBlock(kind="image", image_path=img_path, caption=alt_text))
            i += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            code_lines: List[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < n:
                i += 1
            if lang.lower() == "mermaid":
                notices.append("Phát hiện khối sơ đồ Mermaid (được hiển thị dạng khối mã/mô tả trong DOCX).")
            blocks.append(MdBlock(kind="code", text="\n".join(code_lines), language=lang))
            continue

        # Headings (# .. ####)
        heading_match = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            blocks.append(
                MdBlock(kind="heading", level=level, text=heading_match.group(2).strip())
            )
            i += 1
            continue

        # Markdown table
        if "|" in stripped and i + 1 < n and _is_table_separator(lines[i + 1]):
            header = _split_pipes_outside_backticks(stripped)
            rows = [header]
            i += 2
            while i < n and lines[i].strip() and "|" in lines[i]:
                row = _split_pipes_outside_backticks(lines[i])
                if len(row) < len(header):
                    row.extend([""] * (len(header) - len(row)))
                elif len(row) > len(header):
                    row = row[: len(header)]
                rows.append(row)
                i += 1
            # Optional table caption directly below table (*Bảng ...* or _Bảng ..._)
            caption = ""
            if i < n and re.match(r"^\*(?:Bảng|Table)\s+.+\*$", lines[i].strip(), re.IGNORECASE):
                caption = strip_markdown_inline(lines[i].strip())
                i += 1
            blocks.append(MdBlock(kind="table", rows=rows, caption=caption))
            continue

        # Blockquote
        if stripped.startswith(">"):
            quote_lines: List[str] = []
            while i < n and lines[i].strip().startswith(">"):
                content = lines[i].strip()[1:].strip()
                if content:
                    quote_lines.append(content)
                i += 1
            blocks.append(MdBlock(kind="quote", text="\n".join(quote_lines)))
            continue

        # Unordered list
        bullet_match = re.match(r"^(\s*)[-*]\s+(.+)$", line)
        if bullet_match:
            indent = len(bullet_match.group(1).replace("\t", "  "))
            level = min(indent // 2, 2)
            blocks.append(
                MdBlock(kind="bullet", level=level, text=bullet_match.group(2).strip())
            )
            i += 1
            continue

        # Ordered list
        num_match = re.match(r"^(\s*)(\d+)\.\s+(.+)$", line)
        if num_match:
            indent = len(num_match.group(1).replace("\t", "  "))
            level = min(indent // 2, 2)
            blocks.append(
                MdBlock(
                    kind="numbered",
                    level=level,
                    text=f"{num_match.group(2)}. {num_match.group(3).strip()}",
                )
            )
            i += 1
            continue

        # Plain HTML block warning
        if stripped.startswith("<") and stripped.endswith(">") and not stripped.lower().startswith("<br"):
            notices.append(f"Bỏ qua thẻ HTML thô không hỗ trợ trực tiếp: {stripped[:60]}")
            i += 1
            continue

        # Regular paragraph
        para_lines = [stripped]
        i += 1
        while i < n:
            nxt = lines[i]
            nxt_s = nxt.strip()
            if (
                not nxt_s
                or nxt_s.startswith(("#", ">", "```"))
                or PAGE_BREAK_RE.match(nxt_s)
                or SECTION_BREAK_RE.match(nxt_s)
                or IMAGE_RE.match(nxt_s)
                or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", nxt_s)
                or re.match(r"^\s*[-*]\s+", nxt)
                or re.match(r"^\s*\d+\.\s+", nxt)
                or ("|" in nxt_s and i + 1 < n and _is_table_separator(lines[i + 1]))
            ):
                break
            para_lines.append(nxt_s)
            i += 1
        blocks.append(MdBlock(kind="paragraph", text=" ".join(para_lines)))

    return blocks, notices


def _is_slide_row_start(line: str) -> bool:
    return bool(
        re.match(r"^\|\s*(?:\*\*)?(?:Slide\s*)?\d+(?:\*\*)?\s*\|", line.strip(), re.IGNORECASE)
    )


def _extract_code_and_lines(display_raw: str) -> Tuple[List[str], List[str]]:
    code_lines: List[str] = []
    other_lines: List[str] = []
    in_code = False
    for raw in display_raw.split("\n"):
        s = raw.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(raw)
        elif s:
            other_lines.append(s)
    return code_lines, other_lines


def _extract_embedded_table(display_raw: str) -> Tuple[List[List[str]], List[str]]:
    rows: List[List[str]] = []
    other: List[str] = []
    for raw in display_raw.split("\n"):
        s = raw.strip()
        if s.startswith("|") and s.endswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                continue
            rows.append(cells)
        elif s:
            other.append(s)
    return rows, other


def _extract_image_from_text(text: str) -> Tuple[str, str]:
    for raw in text.split("\n"):
        m = IMAGE_RE.match(raw.strip())
        if m:
            return m.group(2).strip(), m.group(1).strip()
    return "", ""


def parse_slide_deck_from_json(json_text: str) -> SlideDeck:
    """Parse structured JSON slide deck into SlideDeck model."""
    data = json.loads(json_text)
    slides: List[SlideModel] = []
    for idx, item in enumerate(data.get("slides", []), 1):
        lines = item.get("content_lines", [])
        raw = item.get("display_raw") or "\n".join(lines)
        slides.append(
            SlideModel(
                number=int(item.get("number", idx)),
                title=str(item.get("title", f"Slide {idx}")),
                layout=str(item.get("layout", "auto")),
                meta=str(item.get("meta", "")),
                content_lines=list(lines) if lines else [l for l in raw.split("\n") if l.strip()],
                display_raw=raw,
                visual_suggestion=str(item.get("visual_suggestion", "")),
                speaker_notes=str(item.get("speaker_notes", "")),
                section_label=str(item.get("section_label", "")),
                image_path=str(item.get("image_path", "")),
                image_caption=str(item.get("image_caption", "")),
                code_lines=list(item.get("code_lines", [])),
                code_language=str(item.get("code_language", "python")),
                table_rows=list(item.get("table_rows", [])),
            )
        )
    return SlideDeck(
        title=str(data.get("title", "Bài giảng Tin học THPT")),
        subtitle=str(data.get("subtitle", "")),
        slides=slides,
        source_format="json",
    )


def parse_slide_deck_from_markdown(markdown_text: str) -> SlideDeck:
    """Parse slide-designer Markdown (6-col tables OR `## Slide N:` sections) into SlideDeck.

    Never silently drops content: if structure cannot be recognized, raises ValueError
    explaining the expected structured format.
    """
    lines = markdown_text.replace("\r\n", "\n").split("\n")
    deck_title = "Bài giảng Tin học THPT"
    deck_subtitle = ""

    for line in lines[:25]:
        s = line.strip()
        if s.startswith("# ") and deck_title == "Bài giảng Tin học THPT":
            deck_title = strip_markdown_inline(s[2:])
        elif s.startswith("**Bài học:**"):
            deck_subtitle = strip_markdown_inline(s.replace("**Bài học:**", ""))

    slides: List[SlideModel] = []
    warnings: List[str] = []
    current_section = ""
    i = 0
    n = len(lines)

    # Strategy 1: Standard 6-column slide-designer distribution tables
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("### "):
            current_section = strip_markdown_inline(stripped[4:])
            i += 1
            continue

        if "|" in stripped and i + 1 < n and _is_table_separator(lines[i + 1]):
            header = [strip_markdown_inline(h).lower() for h in _split_pipes_outside_backticks(stripped)]
            is_slide_table = (
                len(header) >= 6
                and ("slide" in header[0] or "số" in header[0])
                and ("tiêu đề" in header[1] or "tieu de" in header[1])
            )
            i += 2
            if not is_slide_table:
                while i < n and lines[i].strip() and "|" in lines[i]:
                    i += 1
                continue

            raw_rows: List[str] = []
            while i < n:
                cur = lines[i]
                cur_s = cur.strip()
                if not cur_s:
                    if raw_rows and raw_rows[-1].count("```") % 2 == 1:
                        raw_rows[-1] += "\n"
                        i += 1
                        continue
                    break
                if cur_s.startswith(("#", "---")) and (
                    not raw_rows or raw_rows[-1].count("```") % 2 == 0
                ):
                    break
                if _is_slide_row_start(cur) and (
                    not raw_rows or raw_rows[-1].count("```") % 2 == 0
                ):
                    raw_rows.append(cur)
                elif raw_rows:
                    raw_rows[-1] += "\n" + cur
                else:
                    break
                i += 1

            for raw_row in raw_rows:
                parts = _split_pipes_outside_backticks(raw_row)
                if len(parts) < 6:
                    warnings.append(f"Bỏ qua hàng bảng thiếu cột (<6 cột): {raw_row[:60]}")
                    continue
                if len(parts) > 6:
                    col0, col1, col2 = parts[0], parts[1], parts[2]
                    col3 = " | ".join(parts[3:-2])
                    col3 = re.sub(r"<br>\s*\|\s*", "<br>|", col3)
                    col4, col5 = parts[-2], parts[-1]
                    cols = [col0, col1, col2, col3, col4, col5]
                else:
                    cols = parts

                num_match = re.search(r"\d+", strip_markdown_inline(cols[0]))
                slide_num = int(num_match.group(0)) if num_match else len(slides) + 1
                display_raw = clean_html_entities(cols[3]).strip()
                visual_raw = clean_html_entities(cols[4]).strip()
                notes_raw = clean_html_entities(cols[5]).strip()
                code_lines, content_lines = _extract_code_and_lines(display_raw)
                table_rows, _ = _extract_embedded_table(display_raw)
                img_path, img_cap = _extract_image_from_text(display_raw)
                if not img_path:
                    img_path, img_cap = _extract_image_from_text(visual_raw)

                slides.append(
                    SlideModel(
                        number=slide_num,
                        title=strip_markdown_inline(cols[1]),
                        layout="auto",
                        meta=clean_html_entities(cols[2]).strip(),
                        content_lines=content_lines,
                        display_raw=display_raw,
                        visual_suggestion=visual_raw,
                        speaker_notes=notes_raw,
                        section_label=current_section,
                        image_path=img_path,
                        image_caption=img_cap,
                        code_lines=code_lines,
                        table_rows=table_rows,
                    )
                )
            continue

        i += 1

    if slides:
        return SlideDeck(
            title=deck_title,
            subtitle=deck_subtitle,
            slides=slides,
            source_format="markdown_table",
            warnings=warnings,
        )

    # Strategy 2: Structured `## Slide N: Title` sections (with optional Layout:, Image:, Notes:)
    section_re = re.compile(r"^##\s+Slide\s+(\d+)\s*[:\-–]\s*(.+)$", re.IGNORECASE)
    slide_starts = [idx for idx, l in enumerate(lines) if section_re.match(l.strip())]
    if slide_starts:
        for s_pos, start_idx in enumerate(slide_starts):
            end_idx = slide_starts[s_pos + 1] if s_pos + 1 < len(slide_starts) else n
            m = section_re.match(lines[start_idx].strip())
            assert m is not None
            slide_num = int(m.group(1))
            slide_title = strip_markdown_inline(m.group(2))
            body_lines = lines[start_idx + 1 : end_idx]

            layout = "auto"
            meta = ""
            visual = ""
            notes_lines: List[str] = []
            content_raw_lines: List[str] = []
            img_path = ""
            img_cap = ""
            in_notes = False

            for bl in body_lines:
                bs = bl.strip()
                if not bs:
                    if not in_notes:
                        content_raw_lines.append("")
                    continue
                if re.match(r"^(?:\*\*)?(?:Layout|Bố cục)\s*:\s*", bs, re.IGNORECASE):
                    layout = strip_markdown_inline(re.sub(r"^(?:\*\*)?(?:Layout|Bố cục)\s*:\s*", "", bs, flags=re.IGNORECASE)).lower()
                    continue
                if re.match(r"^(?:\*\*)?(?:Mục tiêu|Meta)\s*:\s*", bs, re.IGNORECASE):
                    meta = strip_markdown_inline(re.sub(r"^(?:\*\*)?(?:Mục tiêu|Meta)\s*:\s*", "", bs, flags=re.IGNORECASE))
                    continue
                if re.match(r"^(?:\*\*)?(?:Hình ảnh|Minh họa|Visual)\s*:\s*", bs, re.IGNORECASE):
                    visual = strip_markdown_inline(re.sub(r"^(?:\*\*)?(?:Hình ảnh|Minh họa|Visual)\s*:\s*", "", bs, flags=re.IGNORECASE))
                    continue
                if re.match(r"^(?:\*\*)?(?:Ghi chú thuyết trình|Speaker Notes|Notes)\s*:\s*", bs, re.IGNORECASE):
                    in_notes = True
                    rest = re.sub(r"^(?:\*\*)?(?:Ghi chú thuyết trình|Speaker Notes|Notes)\s*:\s*", "", bs, flags=re.IGNORECASE)
                    if rest:
                        notes_lines.append(strip_markdown_inline(rest))
                    continue
                im = IMAGE_RE.match(bs)
                if im:
                    img_path, img_cap = im.group(2).strip(), im.group(1).strip()
                    continue
                if in_notes:
                    notes_lines.append(strip_markdown_inline(bs))
                else:
                    content_raw_lines.append(bl)

            display_raw = "\n".join(content_raw_lines).strip()
            code_lines, content_lines = _extract_code_and_lines(display_raw)
            table_rows, _ = _extract_embedded_table(display_raw)
            slides.append(
                SlideModel(
                    number=slide_num,
                    title=slide_title,
                    layout=layout,
                    meta=meta,
                    content_lines=content_lines,
                    display_raw=display_raw,
                    visual_suggestion=visual,
                    speaker_notes="\n".join(notes_lines).strip(),
                    image_path=img_path,
                    image_caption=img_cap,
                    code_lines=code_lines,
                    table_rows=table_rows,
                )
            )
        return SlideDeck(
            title=deck_title,
            subtitle=deck_subtitle,
            slides=slides,
            source_format="markdown_sections",
            warnings=warnings,
        )

    raise ValueError(
        "Không nhận diện được cấu trúc kịch bản slide hợp lệ trong Markdown. "
        "Cần dùng bảng phân bổ slide chuẩn 6 cột (`Số slide | Tiêu đề | Mục tiêu | Nội dung hiển thị | Hình ảnh/Sơ đồ | Ghi chú thuyết trình`) "
        "hoặc các mục `## Slide N: Tiêu đề` (không tự ý tách tùy tiện bằng dấu `#` để tránh bỏ sót nội dung)."
    )


def load_slide_deck(source_file: Path) -> SlideDeck:
    """Load a SlideDeck from a Markdown (.md) or JSON (.json) file."""
    text = source_file.read_text(encoding="utf-8")
    if source_file.suffix.lower() == ".json":
        return parse_slide_deck_from_json(text)
    return parse_slide_deck_from_markdown(text)
