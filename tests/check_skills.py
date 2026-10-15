#!/usr/bin/env python3
"""Validate skill metadata and registry/evidence consistency, not LLM reasoning.
Dependency: PyYAML. Run from any directory: python tests/check_skills.py.
"""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

def validate(root):
    errors = []
    files = sorted((root / "skills").glob("*/SKILL.md"))
    names = {path.parent.name for path in files}
    for path in files:
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
            if not lines or lines[0] != "---":
                raise ValueError("missing YAML frontmatter")
            try:
                end = lines.index("---", 1)
            except ValueError:
                raise ValueError("unclosed YAML frontmatter") from None
            data = yaml.safe_load("\n".join(lines[1:end]))
            if not isinstance(data, dict):
                raise ValueError("frontmatter must be a mapping")
            name = data.get("name")
            if (not isinstance(name, str) or not 1 <= len(name) <= 64
                    or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                    or name != path.parent.name):
                raise ValueError("invalid name or directory mismatch")
            desc = data.get("description")
            if not isinstance(desc, str) or not 1 <= len(desc) <= 1024:
                raise ValueError("description must be 1-1024 characters")
            metadata = data.get("metadata", {})
            if (not isinstance(metadata, dict) or any(
                    not isinstance(k, str) or not isinstance(v, str)
                    for k, v in metadata.items())):
                raise ValueError("metadata must map strings to strings")
            if "compatibility" in data and (
                    not isinstance(data["compatibility"], str)
                    or not 1 <= len(data["compatibility"]) <= 500):
                raise ValueError("compatibility must be 1-500 characters")
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    if not files:
        errors.append("no skills found")
    try:
        config = yaml.safe_load((root / "config/assistant.yaml").read_text())
        if not isinstance(config, dict):
            raise ValueError("assistant configuration must be a mapping")
        registered = []
        for key in ("shared_skills", "discipleship_skills"):
            values = config.get(key)
            if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
                raise ValueError(f"{key} must be a list of skill names")
            registered.extend(values)
        if len(registered) != len(set(registered)):
            errors.append("duplicate skill in configuration registry")
        if names != set(registered):
            errors.append(f"skill registry mismatch: missing={sorted(names - set(registered))}; "
                          f"unknown={sorted(set(registered) - names)}")
        agents = (root / "AGENTS.md").read_text()
        taxonomy = agents.split("## Evidence taxonomy\n", 1)[1].split("\n## ", 1)[0]
        labels = set(re.findall("^- " + chr(96) + "([A-Z_]+)" + chr(96), taxonomy, re.MULTILINE))
        configured = config.get("evidence_labels")
        if not isinstance(configured, list) or any(not isinstance(v, str) for v in configured):
            raise ValueError("evidence_labels must be a list of labels")
        if not labels or len(configured) != len(set(configured)) or labels != set(configured):
            errors.append("configured evidence labels do not match AGENTS.md taxonomy")
    except (OSError, ValueError, IndexError, yaml.YAMLError) as exc:
        errors.append(f"configuration consistency: {exc}")
    return len(files), errors

if __name__ == "__main__":
    count, errors = validate(ROOT)
    for error in errors:
        print(error)
    print(f"{'FAIL' if errors else 'PASS'}: {count} skills, {len(errors)} errors")
    sys.exit(bool(errors))
