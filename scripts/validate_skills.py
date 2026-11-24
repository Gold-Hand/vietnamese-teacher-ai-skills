#!/usr/bin/env python3
"""Validate the repository's Agent Skills metadata and basic structure."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
errors = []
count = 0

if not SKILLS.exists():
    print("ERROR: .agents/skills directory not found")
    sys.exit(1)

for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        errors.append(f"{skill_dir.name}: missing SKILL.md")
        continue
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{skill_dir.name}: YAML frontmatter must be first")
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{skill_dir.name}: malformed frontmatter")
        continue
    fm = parts[1]
    name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", fm)
    desc = re.search(r"(?m)^description:\s*(.+)$", fm)
    if not name:
        errors.append(f"{skill_dir.name}: missing/invalid name")
    elif name.group(1) != skill_dir.name:
        errors.append(f"{skill_dir.name}: name does not match directory")
    if not desc or not desc.group(1).strip():
        errors.append(f"{skill_dir.name}: missing description")
    if len(parts[2].strip()) < 100:
        errors.append(f"{skill_dir.name}: body looks too short")
    count += 1

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"Validation passed: {count} skills found.")
