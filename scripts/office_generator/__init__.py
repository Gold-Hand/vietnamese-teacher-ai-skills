"""Shared Office Document Generator for Vietnamese Teacher AI Skills."""

from scripts.office_generator.generator import generate_document, run_batch
from scripts.office_generator.models import (
    DocxTemplateConfig,
    GenerationResult,
    PptxTemplateConfig,
    SlideDeck,
    SlideModel,
    ValidationIssue,
    ValidationReport,
)
from scripts.office_generator.validator import (
    format_validation_report_markdown,
    validate_document,
)

__all__ = [
    "generate_document",
    "run_batch",
    "validate_document",
    "format_validation_report_markdown",
    "DocxTemplateConfig",
    "PptxTemplateConfig",
    "SlideModel",
    "SlideDeck",
    "GenerationResult",
    "ValidationReport",
    "ValidationIssue",
]
