"""Interactive Classroom Lesson PowerPoint theme (Indigo + Teal + Amber)."""

from scripts.office_generator.models import PptxTemplateConfig


def get_lesson_pptx_template() -> PptxTemplateConfig:
    return PptxTemplateConfig(
        name="lesson",
        display_name="Bài giảng Tương tác THPT",
        slide_width_in=13.333,
        slide_height_in=7.5,
        font_main="Segoe UI",
        font_code="Consolas",
        bg_dark="1E1B4B",
        bg_dark_card="312E81",
        bg_light="F8FAFC",
        primary="4338CA",
        primary_soft="EEF2FF",
        secondary="0F766E",
        secondary_soft="CCFBF1",
        accent="D97706",
        accent_bright="F59E0B",
        accent_soft="FEF3C7",
        danger="DC2626",
        danger_soft="FEE2E2",
        success="059669",
        success_soft="D1FAE5",
        text_dark="1E293B",
        text_muted="475569",
        border="CBD5E1",
        code_bg="0F172A",
        code_text="F8FAFC",
        default_layout="two_columns",
    )
