from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter
from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.toolsets import FunctionToolset


def load_skill(skill_name: str) -> str:
    """Load a skill's router file (SKILL.md), supporting both
    flat-style (skills/name.md) and folder-style (skills/name/SKILL.md) skills.

    skill_name : str
        The name of the skill to load (e.g. "web-scraping-econ").
        Should be a bare name, not a path.

    Returns
    -------
    str
        The contents of the skill's router file.

    """
    # Defensive: strip any accidental "skills/" prefix or ".md" suffix
    # in case the model passes a path instead of a bare name.
    clean_name = skill_name.removeprefix("skills/").removesuffix(".md")

    folder_path = Path("skills") / clean_name / "SKILL.md"
    flat_path = Path("skills") / f"{clean_name}.md"

    if folder_path.exists():
        file_path = folder_path
    elif flat_path.exists():
        file_path = flat_path
    else:
        msg = f"Skill '{skill_name}' not found in flat or folder format."
        raise FileNotFoundError(msg)

    skill = frontmatter.load(str(file_path))
    return skill.content


@dataclass
class Skills(AbstractCapability[Any]):
    def get_instructions(self) -> str:
        result = (
            "You can extend your capabilities by using skills.\n"
            "Use a skill when doing tasks described in the skill.\n\n"
            "You have the following skills available:"
        )

        skills_dir = Path("skills")

        # Flat-style skills: skills/name.md
        flat_files = skills_dir.glob("*.md")

        # Folder-style skills: skills/name/SKILL.md
        folder_files = skills_dir.glob("*/SKILL.md")

        for f in list(flat_files) + list(folder_files):
            skill = frontmatter.load(str(f))

            name = skill.metadata.get("name")
            description = skill.metadata.get("description")

            result += f"\n- {name}: {description}"

        return result

    def get_toolset(self) -> FunctionToolset:
        toolset = FunctionToolset()
        toolset.add_function(load_skill)

        return toolset
