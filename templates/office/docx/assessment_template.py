"""Assessment DOCX templates: Exam (Đề kiểm tra), Matrix (Ma trận & Đặc tả), Answer Key (Đáp án)."""

from scripts.office_generator.models import DocxTemplateConfig


def get_assessment_template() -> DocxTemplateConfig:
    """Template for Vietnamese school exams/tests (Đề kiểm tra)."""
    return DocxTemplateConfig(
        name="assessment",
        display_name="Đề kiểm tra",
        page_width_cm=21.0,
        page_height_cm=29.7,
        margin_top_cm=1.8,
        margin_bottom_cm=1.8,
        margin_left_cm=2.2,
        margin_right_cm=1.8,
        font_name="Times New Roman",
        code_font_name="Consolas",
        body_font_size=13.0,
        heading1_size=15.0,
        heading2_size=13.5,
        heading3_size=13.0,
        heading4_size=13.0,
        table_font_size=11.5,
        line_spacing=1.15,
        primary_hex="0F172A",
        accent_hex="1D4ED8",
        text_hex="0F172A",
        muted_hex="475569",
        border_hex="94A3B8",
        table_alt_row_hex="F8FAFC",
        quote_bg_hex="F8FAFC",
        code_bg_hex="F1F5F9",
        footer_prefix="Đề kiểm tra",
        show_heading2_underline=True,
        show_formal_banner=True,
        first_page_header_suppressed=True,
    )


def get_matrix_template() -> DocxTemplateConfig:
    """Template optimized for dense assessment matrices and specification tables."""
    return DocxTemplateConfig(
        name="matrix",
        display_name="Ma trận và Bản đặc tả đề kiểm tra",
        page_width_cm=21.0,
        page_height_cm=29.7,
        margin_top_cm=1.8,
        margin_bottom_cm=1.8,
        margin_left_cm=1.8,
        margin_right_cm=1.5,
        font_name="Times New Roman",
        code_font_name="Consolas",
        body_font_size=13.0,
        heading1_size=15.0,
        heading2_size=13.5,
        heading3_size=13.0,
        heading4_size=13.0,
        table_font_size=11.0,
        line_spacing=1.12,
        primary_hex="1E3A8A",
        accent_hex="0D9488",
        text_hex="1E293B",
        muted_hex="475569",
        border_hex="94A3B8",
        table_alt_row_hex="F0FDFA",
        quote_bg_hex="F0FDFA",
        code_bg_hex="F1F5F9",
        footer_prefix="Ma trận & Bản đặc tả",
        show_heading2_underline=True,
        show_formal_banner=False,
        first_page_header_suppressed=True,
    )


def get_answer_key_template() -> DocxTemplateConfig:
    """Template for Answer Keys & Grading Rubrics (Đáp án và hướng dẫn chấm)."""
    return DocxTemplateConfig(
        name="answer_key",
        display_name="Đáp án và Hướng dẫn chấm",
        page_width_cm=21.0,
        page_height_cm=29.7,
        margin_top_cm=2.0,
        margin_bottom_cm=2.0,
        margin_left_cm=2.5,
        margin_right_cm=1.8,
        font_name="Times New Roman",
        code_font_name="Consolas",
        body_font_size=13.0,
        heading1_size=15.0,
        heading2_size=13.5,
        heading3_size=13.0,
        heading4_size=13.0,
        table_font_size=11.5,
        line_spacing=1.15,
        primary_hex="166534",
        accent_hex="15803D",
        text_hex="1E293B",
        muted_hex="475569",
        border_hex="CBD5E1",
        table_alt_row_hex="F0FDF4",
        quote_bg_hex="F0FDF4",
        code_bg_hex="F1F5F9",
        footer_prefix="Đáp án & Hướng dẫn chấm",
        show_heading2_underline=True,
        show_formal_banner=False,
        first_page_header_suppressed=True,
    )
