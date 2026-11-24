"""KHBD (Kế hoạch bài dạy) DOCX template following Vietnamese education standards."""

from scripts.office_generator.models import DocxTemplateConfig


def get_khbd_template() -> DocxTemplateConfig:
    """Return A4 Times New Roman template configured for Vietnamese lesson plans (CV 5512/2345)."""
    return DocxTemplateConfig(
        name="khbd",
        display_name="Kế hoạch bài dạy (KHBD)",
        page_width_cm=21.0,
        page_height_cm=29.7,
        margin_top_cm=2.0,
        margin_bottom_cm=2.0,
        margin_left_cm=2.8,
        margin_right_cm=1.8,
        font_name="Times New Roman",
        code_font_name="Consolas",
        body_font_size=13.0,
        heading1_size=15.5,
        heading2_size=14.0,
        heading3_size=13.5,
        heading4_size=13.0,
        table_font_size=11.5,
        line_spacing=1.15,
        primary_hex="1E3A8A",
        accent_hex="1D4ED8",
        text_hex="1E293B",
        muted_hex="475569",
        border_hex="CBD5E1",
        table_alt_row_hex="F8FAFC",
        quote_bg_hex="EFF6FF",
        code_bg_hex="F1F5F9",
        footer_prefix="Kế hoạch bài dạy",
        show_heading2_underline=True,
        show_formal_banner=False,
        first_page_header_suppressed=True,
    )
