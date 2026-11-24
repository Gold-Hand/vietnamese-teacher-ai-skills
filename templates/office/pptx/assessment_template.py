"""Assessment & Interactive Review Quiz PowerPoint theme (Slate + Emerald + Coral)."""

from scripts.office_generator.models import PptxTemplateConfig


def get_assessment_pptx_template() -> PptxTemplateConfig:
    return PptxTemplateConfig(
        name="assessment",
        display_name="Trình chiếu Câu hỏi & Ôn tập",
        slide_width_in=13.333,
        slide_height_in=7.5,
        font_main="Segoe UI",
        font_code="Consolas",
        bg_dark="064E3B",
        bg_dark_card="065F46",
        bg_light="F8FAFC",
        primary="047857",
        primary_soft="ECFDF5",
        secondary="0369A1",
        secondary_soft="E0F2FE",
        accent="B45309",
        accent_bright="F59E0B",
        accent_soft="FEF3C7",
        danger="B91C1C",
        danger_soft="FEE2E2",
        success="15803D",
        success_soft="DCFCE7",
        text_dark="0F172A",
        text_muted="475569",
        border="CBD5E1",
        code_bg="1E293B",
        code_text="F8FAFC",
        default_layout="quiz",
    )
