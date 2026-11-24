"""PPTX themes and templates registry."""

from .education_template import get_education_pptx_template
from .lesson_template import get_lesson_pptx_template
from .assessment_template import get_assessment_pptx_template

PPTX_TEMPLATE_REGISTRY = {
    "education": get_education_pptx_template,
    "lesson": get_lesson_pptx_template,
    "assessment": get_assessment_pptx_template,
    "quiz": get_assessment_pptx_template,
}


def resolve_pptx_template(name: str, overrides: dict | None = None):
    """Resolve a PPTX template by name and apply optional user overrides."""
    key = (name or "education").strip().lower()
    factory = PPTX_TEMPLATE_REGISTRY.get(key)
    if factory is None:
        supported = ", ".join(sorted(PPTX_TEMPLATE_REGISTRY.keys()))
        raise ValueError(f"PPTX template '{name}' không được hỗ trợ. Hỗ trợ: {supported}")
    cfg = factory()
    if overrides:
        cfg = cfg.with_overrides(overrides)
    return cfg
