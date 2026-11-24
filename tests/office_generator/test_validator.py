"""Tests for Validator, error handling, PDF controlled behavior, and 9-Skill integration (Groups 8 & 10)."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.office_generator import generate_document, validate_document  # noqa: E402
from scripts.office_generator.pdf_engine import detect_pdf_backend  # noqa: E402


class TestValidatorAndSkillIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_group8_corrupted_docx_and_pptx_fail_validation(self):
        bad_docx = self.tmp_dir / "corrupted.docx"
        bad_docx.write_bytes(b"NOT A VALID DOCX ZIP FILE")
        rep_d = validate_document(bad_docx)
        self.assertFalse(rep_d.passed)
        self.assertEqual(rep_d.errors[0].category, "file_error")

        bad_pptx = self.tmp_dir / "corrupted.pptx"
        bad_pptx.write_bytes(b"NOT A VALID PPTX FILE")
        rep_p = validate_document(bad_pptx)
        self.assertFalse(rep_p.passed)
        self.assertEqual(rep_p.errors[0].category, "file_error")

        missing = validate_document(self.tmp_dir / "missing.docx")
        self.assertFalse(missing.passed)

    def test_group8_pdf_controlled_response_when_backend_missing(self):
        if detect_pdf_backend() is not None:
            self.skipTest("PDF backend is installed on this host")
        dummy = self.tmp_dir / "doc.docx"
        dummy.write_bytes(b"placeholder")
        res = generate_document(dummy, self.tmp_dir / "doc.pdf", format="pdf")
        self.assertFalse(res.success)
        self.assertIn("LibreOffice", res.error_message)

    def test_group10_all_9_skills_integrated_and_valid(self):
        # 1. Existing validate_skills.py must pass for all 9 skills
        proc = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts/validate_skills.py")],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("9 skills found", proc.stdout)

        # 2. All 9 skills must reference the single shared scripts/office_generator/cli.py
        skills_dir = REPO_ROOT / ".agents/skills"
        expected_skills = {
            "ai-education": "docx",
            "ai-video-creator": "docx",
            "assessment-generator": "docx",
            "curriculum-analyzer": "docx",
            "digital-competency": "docx",
            "informatics-expert": "docx",
            "lesson-planner": "docx",
            "slide-designer": "pptx",
            "teaching-assistant": "docx",
        }
        for skill_name, expected_cmd in expected_skills.items():
            text = (skills_dir / skill_name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("scripts/office_generator/cli.py", text, f"{skill_name} missing shared CLI link")
            self.assertIn(f"cli.py {expected_cmd}", text, f"{skill_name} missing {expected_cmd} command")
            # Ensure no skill copies python-docx/python-pptx code directly into SKILL.md
            self.assertNotIn("from docx import", text)
            self.assertNotIn("from pptx import", text)


if __name__ == "__main__":
    unittest.main()
