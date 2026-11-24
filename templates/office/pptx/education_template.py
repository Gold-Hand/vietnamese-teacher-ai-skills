"""Modern THPT Education PowerPoint theme (Navy + Tech Blue + Gold)."""

from scripts.office_generator.models import PptxTemplateConfig


def get_education_pptx_template() -> PptxTemplateConfig:
    return PptxTemplateConfig(
        name="education",
        display_name="Giáo dục THPT Hiện đại",
        slide_width_in=13.333,
        slide_height_in=7.5,
        font_main="Segoe UI",
        font_code="Consolas",
        bg_dark="0F172A",
        bg_dark_card="1E293B",
        bg_light="F8FAFC",
        primary="1D4ED8",
        primary_soft="EFF6FF",
        secondary="0D9488",
        secondary_soft="CCFBF1",
        accent="D97706",
        accent_bright="EAB308",
        accent_soft="FEF3C7",
        danger="DC2626",
        danger_soft="FEE2E2",
        success="16A34A",
        success_soft="DCFCE7",
        text_dark="1E293B",
        text_muted="475569",
        border="CBD5E1",
        code_bg="1E293B",
        code_text="F8FAFC",
        default_layout="two_columns",
    )
