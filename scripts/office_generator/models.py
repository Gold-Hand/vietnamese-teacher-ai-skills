"""Core data models for the shared Office Document Generator."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class InlineSpan:
    text: str
    bold: bool = False
    italic: bool = False
    code: bool = False


@dataclass
class MdBlock:
    """Structured Markdown document block."""

    kind: str  # heading, paragraph, bullet, numbered, table, code, quote, image, page_break, section_break, hr
    text: str = ""
    level: int = 0
    rows: List[List[str]] = field(default_factory=list)
    language: str = ""
    image_path: str = ""
    caption: str = ""


@dataclass
class SlideModel:
    """Structured slide model that Agent Skills can pass directly to the PPTX engine."""

    number: int
    title: str
    layout: str = "auto"  # auto | title_slide | section_divider | text_image | two_columns | comparison | timeline | process | diagram | table | code_example | quiz | summary | closing
    meta: str = ""
    content_lines: List[str] = field(default_factory=list)
    display_raw: str = ""
    visual_suggestion: str = ""
    speaker_notes: str = ""
    section_label: str = ""
    image_path: str = ""
    image_caption: str = ""
    code_lines: List[str] = field(default_factory=list)
    code_language: str = "python"
    table_rows: List[List[str]] = field(default_factory=list)


@dataclass
class SlideDeck:
    """Structured presentation deck containing metadata and SlideModel items."""

    title: str = "Bài giảng Tin học THPT"
    subtitle: str = ""
    slides: List[SlideModel] = field(default_factory=list)
    source_format: str = "markdown_table"
    warnings: List[str] = field(default_factory=list)


@dataclass
class DocxTemplateConfig:
    """Configurable DOCX template (zero hardcoded school/teacher identities)."""

    name: str = "general"
    display_name: str = "Tài liệu giáo dục"
    page_width_cm: float = 21.0
    page_height_cm: float = 29.7
    margin_top_cm: float = 2.0
    margin_bottom_cm: float = 2.0
    margin_left_cm: float = 2.5
    margin_right_cm: float = 1.8
    font_name: str = "Times New Roman"
    code_font_name: str = "Consolas"
    body_font_size: float = 13.0
    heading1_size: float = 15.5
    heading2_size: float = 14.0
    heading3_size: float = 13.5
    heading4_size: float = 13.0
    table_font_size: float = 11.5
    line_spacing: float = 1.15
    primary_hex: str = "1E3A8A"
    accent_hex: str = "1D4ED8"
    text_hex: str = "1E293B"
    muted_hex: str = "475569"
    border_hex: str = "CBD5E1"
    table_alt_row_hex: str = "F8FAFC"
    quote_bg_hex: str = "EFF6FF"
    code_bg_hex: str = "F1F5F9"
    # Optional institution / teacher branding (supplied by caller, never hardcoded)
    school_name: str = ""
    department_name: str = ""
    teacher_name: str = ""
    logo_path: str = ""
    header_text: str = ""
    footer_prefix: str = "Tài liệu giáo dục"
    show_heading2_underline: bool = True
    show_formal_banner: bool = False
    first_page_header_suppressed: bool = True

    def with_overrides(self, overrides: Dict[str, Any]) -> "DocxTemplateConfig":
        valid = {k: v for k, v in overrides.items() if hasattr(self, k) and v is not None}
        return replace(self, **valid)


@dataclass
class PptxTemplateConfig:
    """Configurable PPTX theme & branding template (zero hardcoded school/teacher names)."""

    name: str = "education"
    display_name: str = "Giáo dục THPT"
    slide_width_in: float = 13.333
    slide_height_in: float = 7.5
    font_main: str = "Segoe UI"
    font_code: str = "Consolas"
    bg_dark: str = "0F172A"
    bg_dark_card: str = "1E293B"
    bg_light: str = "F8FAFC"
    primary: str = "1D4ED8"
    primary_soft: str = "EFF6FF"
    secondary: str = "0D9488"
    secondary_soft: str = "CCFBF1"
    accent: str = "D97706"
    accent_bright: str = "EAB308"
    accent_soft: str = "FEF3C7"
    danger: str = "DC2626"
    danger_soft: str = "FEE2E2"
    success: str = "16A34A"
    success_soft: str = "DCFCE7"
    text_dark: str = "1E293B"
    text_muted: str = "475569"
    border: str = "CBD5E1"
    code_bg: str = "1E293B"
    code_text: str = "F8FAFC"
    default_layout: str = "two_columns"
    # Optional institution / teacher branding
    school_name: str = ""
    teacher_name: str = ""
    logo_path: str = ""
    footer_text: str = ""
    show_slide_numbers: bool = True

    def with_overrides(self, overrides: Dict[str, Any]) -> "PptxTemplateConfig":
        valid = {k: v for k, v in overrides.items() if hasattr(self, k) and v is not None}
        return replace(self, **valid)


@dataclass
class ValidationIssue:
    """Single validation finding distinguishing content errors vs format warnings."""

    severity: str  # "error" | "warning"
    category: str  # "file_error" | "content_error" | "format_warning" | "unconvertible"
    message: str
    location: str = ""


@dataclass
class ValidationReport:
    """Structured QA verification report for a generated Office artifact."""

    file_path: str
    file_format: str
    passed: bool
    metrics: Dict[str, Any] = field(default_factory=dict)
    issues: List[ValidationIssue] = field(default_factory=list)
    source_file: str = ""

    @property
    def errors(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "warning"]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class GenerationResult:
    """Unified return object from `generate_document()`."""

    success: bool
    output_file: str
    file_format: str
    template: str
    source_file: str = ""
    speaker_notes_file: str = ""
    speaker_notes_embedded: bool = False
    layouts_used: List[str] = field(default_factory=list)
    unconvertible_notes: List[str] = field(default_factory=list)
    validation: Optional[ValidationReport] = None
    error_message: str = ""

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        return data
