"""DOCX templates registry for Vietnamese education documents."""

from .khbd_template import get_khbd_template
from .assessment_template import (
    get_answer_key_template,
    get_assessment_template,
    get_matrix_template,
)
from .general_document_template import (
    get_general_document_template,
    get_study_material_template,
    get_teacher_guide_template,
)

DOCX_TEMPLATE_REGISTRY = {
    "khbd": get_khbd_template,
    "lesson_plan": get_khbd_template,
    "assessment": get_assessment_template,
    "exam": get_assessment_template,
    "matrix": get_matrix_template,
    "answer_key": get_answer_key_template,
    "study_material": get_study_material_template,
    "teacher_guide": get_teacher_guide_template,
    "general": get_general_document_template,
}


def resolve_docx_template(name: str, overrides: dict | None = None):
    """Resolve a DOCX template by name and apply optional user overrides."""
    key = (name or "general").strip().lower()
    factory = DOCX_TEMPLATE_REGISTRY.get(key)
    if factory is None:
        supported = ", ".join(sorted(DOCX_TEMPLATE_REGISTRY.keys()))
        raise ValueError(f"DOCX template '{name}' không được hỗ trợ. Hỗ trợ: {supported}")
    cfg = factory()
    if overrides:
        cfg = cfg.with_overrides(overrides)
    return cfg
