"""General educational DOCX templates: Study Material, Teacher Guide, General Document."""

from scripts.office_generator.models import DocxTemplateConfig


def get_study_material_template() -> DocxTemplateConfig:
    """Template for student study guides, handouts, and lab worksheets (Tài liệu học tập)."""
    return DocxTemplateConfig(
        name="study_material",
        display_name="Tài liệu học tập",
        page_width_cm=21.0,
        page_height_cm=29.7,
        margin_top_cm=2.0,
        margin_bottom_cm=2.0,
        margin_left_cm=2.5,
        margin_right_cm=1.8,
        font_name="Times New Roman",
        code_font_name="Consolas",
        body_font_size=13.5,
        heading1_size=16.0,
        heading2_size=14.0,
        heading3_size=13.5,
        heading4_size=13.0,
        table_font_size=12.0,
        line_spacing=1.2,
        primary_hex="0F766E",
        accent_hex="0D9488",
        text_hex="1E293B",
        muted_hex="475569",
        border_hex="CBD5E1",
        table_alt_row_hex="F0FDFA",
        quote_bg_hex="CCFBF1",
        code_bg_hex="F1F5F9",
        footer_prefix="Tài liệu học tập",
        show_heading2_underline=True,
        show_formal_banner=False,
        first_page_header_suppressed=True,
    )


def get_teacher_guide_template() -> DocxTemplateConfig:
    """Template for teacher reports, curriculum analyses, and digital competency tables."""
    return DocxTemplateConfig(
        name="teacher_guide",
        display_name="Tài liệu giáo viên",
        page_width_cm=21.0,
        page_height_cm=29.7,
        margin_top_cm=2.0,
        margin_bottom_cm=2.0,
        margin_left_cm=2.6,
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
        accent_hex="2563EB",
        text_hex="1E293B",
        muted_hex="475569",
        border_hex="CBD5E1",
        table_alt_row_hex="F8FAFC",
        quote_bg_hex="EFF6FF",
        code_bg_hex="F1F5F9",
        footer_prefix="Tài liệu giáo viên",
        show_heading2_underline=True,
        show_formal_banner=False,
        first_page_header_suppressed=True,
    )


def get_general_document_template() -> DocxTemplateConfig:
    """General-purpose clean A4 Vietnamese document template."""
    return DocxTemplateConfig(
        name="general",
        display_name="Tài liệu giáo dục",
        page_width_cm=21.0,
        page_height_cm=29.7,
        margin_top_cm=2.0,
        margin_bottom_cm=2.0,
        margin_left_cm=2.5,
        margin_right_cm=2.0,
        font_name="Times New Roman",
        code_font_name="Consolas",
        body_font_size=13.0,
        heading1_size=15.0,
        heading2_size=14.0,
        heading3_size=13.0,
        heading4_size=13.0,
        table_font_size=11.5,
        line_spacing=1.15,
        primary_hex="1E293B",
        accent_hex="1D4ED8",
        text_hex="1E293B",
        muted_hex="475569",
        border_hex="CBD5E1",
        table_alt_row_hex="F8FAFC",
        quote_bg_hex="F8FAFC",
        code_bg_hex="F1F5F9",
        footer_prefix="Tài liệu giáo dục",
        show_heading2_underline=False,
        show_formal_banner=False,
        first_page_header_suppressed=True,
    )
