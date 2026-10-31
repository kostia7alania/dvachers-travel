#!/usr/bin/env python3
"""Check portable skill structure and local Markdown references, without packages."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check():
    errors = []
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills or (ROOT / "SKILL.md").exists():
        errors.append("Keep selectable skills under skills/<name>/SKILL.md; no root skill.")
    for skill in skills:
        text = skill.read_text()
        front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not front:
            errors.append(f"Missing metadata: {skill.relative_to(ROOT)}")
            continue
        fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", front[1], re.M))
        name = fields.get("name", "")
        if name != skill.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"Invalid skill name: {skill.relative_to(ROOT)}")
        if not fields.get("description") or len(fields["description"]) > 1024:
            errors.append(f"Missing or long description: {skill.relative_to(ROOT)}")

    for document in ROOT.rglob("*.md"):
        if any(part in {".git", "_site", "node_modules", "dist", ".astro", ".jekyll-cache"} for part in document.parts):
            continue
        text = document.read_text()
        if re.search(r"/(?:Users|home)/[^\s]+|(?:[A-Za-z]:\\Users\\)", text):
            errors.append(f"Private machine path: {document.relative_to(ROOT)}")
        for target in re.findall(r"\]\(([^\s)]+)", text):
            if ":" in target or target.startswith("#") or "{{" in target:
                continue
            path = (document.parent / target.split("#", 1)[0]).resolve()
            if not path.is_relative_to(ROOT) or not path.exists():
                errors.append(f"Broken local link: {document.relative_to(ROOT)} -> {target}")
            if document.is_relative_to(ROOT / "skills"):
                skill_root = ROOT / "skills" / document.relative_to(ROOT / "skills").parts[0]
                if not path.is_relative_to(skill_root):
                    errors.append(f"Skill depends on files outside its install: {target}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Passed: {len(skills)} selectable skill(s), metadata and local references.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
