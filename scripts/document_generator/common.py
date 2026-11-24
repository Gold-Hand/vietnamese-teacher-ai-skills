"""Shared Markdown parsing and text-formatting utilities for Office document generation."""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple


# Inline markdown token pattern: **bold**, *italic*, `code`
INLINE_TOKEN_RE = re.compile(
    r"(\*\*[^*]+\*\*|`[^`]+`|\*(?!\s)[^*]+(?<!\s)\*)"
)


@dataclass
class InlineSpan:
    text: str
    bold: bool = False
    italic: bool = False
    code: bool = False


@dataclass
class MdBlock:
    kind: str  # heading, paragraph, bullet, numbered, table, code, quote, hr
    text: str = ""
    level: int = 0
    rows: List[List[str]] = field(default_factory=list)
    language: str = ""


@dataclass
class SlideSpec:
    number: int
    title: str
    meta: str  # Mục tiêu & Thời lượng
    display_raw: str  # Nội dung hiển thị trên slide
    visual_raw: str  # Hình ảnh / Sơ đồ đề xuất
    notes_raw: str  # Ghi chú thuyết trình & hoạt động tương tác
    section_label: str = ""  # e.g., "TIẾT 1 (45 PHÚT)"


def clean_html_entities(text: str) -> str:
    """Convert common Markdown/HTML break and space entities to readable plain text."""
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = text.replace("&nbsp;", " ").replace("&emsp;", "   ")
    text = html.unescape(text)
    return text


def strip_markdown_inline(text: str) -> str:
    """Remove inline markdown markers (**bold**, *italic*, `code`) while keeping text."""
    text = clean_html_entities(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*(?!\s)([^*]+)(?<!\s)\*", r"\1", text)
    return text.strip()


def parse_inline_spans(text: str) -> List[InlineSpan]:
    """Parse inline bold, italic, and code spans from a single line of Markdown."""
    text = clean_html_entities(text)
    spans: List[InlineSpan] = []
    pos = 0
    for match in INLINE_TOKEN_RE.finditer(text):
        if match.start() > pos:
            spans.append(InlineSpan(text=text[pos : match.start()]))
        token = match.group(0)
        if token.startswith("**") and token.endswith("**"):
            inner = token[2:-2]
            # Handle inline code inside bold, e.g. **`print()`**
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


def _split_table_row(line: str) -> List[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    # Split on unescaped pipe
    parts = re.split(r"(?<!\\)\|", stripped)
    return [p.replace(r"\|", "|").strip() for p in parts]


def parse_markdown_blocks(markdown_text: str) -> List[MdBlock]:
    """Parse a Markdown document into structured blocks for DOCX generation."""
    lines = markdown_text.replace("\r\n", "\n").split("\n")
    blocks: List[MdBlock] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Horizontal rule
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            blocks.append(MdBlock(kind="hr"))
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
                i += 1  # consume closing fence
            blocks.append(
                MdBlock(kind="code", text="\n".join(code_lines), language=lang)
            )
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
            header = _split_table_row(stripped)
            rows = [header]
            i += 2
            while i < n and lines[i].strip() and "|" in lines[i]:
                row = _split_table_row(lines[i])
                # Normalize column count
                if len(row) < len(header):
                    row.extend([""] * (len(header) - len(row)))
                elif len(row) > len(header):
                    row = row[: len(header)]
                rows.append(row)
                i += 1
            blocks.append(MdBlock(kind="table", rows=rows))
            continue

        # Blockquote (group consecutive > lines)
        if stripped.startswith(">"):
            quote_lines: List[str] = []
            while i < n and lines[i].strip().startswith(">"):
                content = lines[i].strip()[1:].strip()
                if content:
                    quote_lines.append(content)
                i += 1
            blocks.append(MdBlock(kind="quote", text="\n".join(quote_lines)))
            continue

        # Unordered list item (- or *)
        bullet_match = re.match(r"^(\s*)[-*]\s+(.+)$", line)
        if bullet_match:
            indent = len(bullet_match.group(1).replace("\t", "  "))
            level = min(indent // 2, 2)
            blocks.append(
                MdBlock(kind="bullet", level=level, text=bullet_match.group(2).strip())
            )
            i += 1
            continue

        # Ordered list item (1. or a))
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

        # Regular paragraph (merge consecutive plain lines)
        para_lines = [stripped]
        i += 1
        while i < n:
            nxt = lines[i]
            nxt_s = nxt.strip()
            if (
                not nxt_s
                or nxt_s.startswith(("#", ">", "```"))
                or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", nxt_s)
                or re.match(r"^\s*[-*]\s+", nxt)
                or re.match(r"^\s*\d+\.\s+", nxt)
                or ("|" in nxt_s and i + 1 < n and _is_table_separator(lines[i + 1]))
            ):
                break
            para_lines.append(nxt_s)
            i += 1
        blocks.append(MdBlock(kind="paragraph", text=" ".join(para_lines)))

    return blocks


def _split_pipes_outside_backticks(line: str) -> List[str]:
    """Split a Markdown table row on pipes '|' that are not escaped and not inside backticks."""
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


def _is_slide_row_start(line: str) -> bool:
    """Return True if a line begins a new slide table row like `| **11** |` or `| 11 |`."""
    return bool(re.match(r"^\|\s*(?:\*\*)?(?:Slide\s*)?\d+(?:\*\*)?\s*\|", line.strip(), re.IGNORECASE))


def parse_slide_script_markdown(
    markdown_text: str,
) -> Tuple[str, str, List[SlideSpec]]:
    """
    Parse a slide-designer Markdown script into (deck_title, deck_subtitle, slides).

    Supports standard 6-column slide distribution tables produced by `slide-designer`,
    including multi-line fenced code blocks and embedded Markdown tables inside column 4:
    `Số slide | Tiêu đề | Mục tiêu (& Thời lượng) | Nội dung hiển thị | Hình ảnh/Sơ đồ | Ghi chú thuyết trình`
    """
    lines = markdown_text.replace("\r\n", "\n").split("\n")
    deck_title = "Bài giảng Tin học THPT"
    deck_subtitle = ""

    for line in lines[:20]:
        s = line.strip()
        if s.startswith("# ") and deck_title == "Bài giảng Tin học THPT":
            deck_title = strip_markdown_inline(s[2:])
        elif s.startswith("**Bài học:**"):
            deck_subtitle = strip_markdown_inline(s.replace("**Bài học:**", ""))

    slides: List[SlideSpec] = []
    current_section = ""
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("### "):
            current_section = strip_markdown_inline(stripped[4:])
            i += 1
            continue

        if "|" in stripped and i + 1 < n and _is_table_separator(lines[i + 1]):
            header = [strip_markdown_inline(h).lower() for h in _split_table_row(stripped)]
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

            # Collect logical slide rows (joining multi-line fenced code blocks inside a row)
            raw_rows: List[str] = []
            while i < n:
                cur = lines[i]
                cur_s = cur.strip()
                if not cur_s:
                    # Blank line terminates the table unless inside an unclosed code fence
                    if raw_rows and raw_rows[-1].count("```") % 2 == 1:
                        raw_rows[-1] += "\n"
                        i += 1
                        continue
                    break
                if cur_s.startswith(("#", "---")) and (not raw_rows or raw_rows[-1].count("```") % 2 == 0):
                    break
                if _is_slide_row_start(cur) and (not raw_rows or raw_rows[-1].count("```") % 2 == 0):
                    raw_rows.append(cur)
                elif raw_rows:
                    raw_rows[-1] += "\n" + cur
                else:
                    break
                i += 1

            for raw_row in raw_rows:
                parts = _split_pipes_outside_backticks(raw_row)
                if len(parts) < 6:
                    continue
                if len(parts) > 6:
                    # Col 0..2 are number/title/meta; Col -2..-1 are visual/notes;
                    # everything between is Col 3 (display content, e.g. embedded table).
                    col0, col1, col2 = parts[0], parts[1], parts[2]
                    col3 = " | ".join(parts[3:-2])
                    # Restore clean embedded table boundaries if `<br>` surrounds pipes
                    col3 = re.sub(r"<br>\s*\|\s*", "<br>|", col3)
                    col4, col5 = parts[-2], parts[-1]
                    cols = [col0, col1, col2, col3, col4, col5]
                else:
                    cols = parts

                num_match = re.search(r"\d+", strip_markdown_inline(cols[0]))
                slide_num = int(num_match.group(0)) if num_match else len(slides) + 1
                slides.append(
                    SlideSpec(
                        number=slide_num,
                        title=strip_markdown_inline(cols[1]),
                        meta=clean_html_entities(cols[2]).strip(),
                        display_raw=clean_html_entities(cols[3]).strip(),
                        visual_raw=clean_html_entities(cols[4]).strip(),
                        notes_raw=clean_html_entities(cols[5]).strip(),
                        section_label=current_section,
                    )
                )
            continue

        i += 1

    return deck_title, deck_subtitle, slides


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")
