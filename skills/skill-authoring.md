---
name: skill-authoring
description: Load this skill when the user wants to create, write, or edit a skill file for this agent.
---

A skill is a Markdown file in the `skills/` directory that teaches the agent how to do a
specific kind of task. Help the user write one by following these rules.

## File structure

Every skill has two parts:

```
---
name: my-skill
description: Load this skill when ...
---

* instruction one
* instruction two
```

* The block between `---` lines is the frontmatter (YAML metadata).
* Everything after the second `---` is the body (the actual instructions).

## Hard rules (must follow, or the skill will not load)

* `name` MUST exactly match the file name without `.md`. Example: file `data-cleaning.md` -> `name: data-cleaning`.
* Use kebab-case for `name`: lowercase words joined by hyphens, no spaces.
* `description` should start with "Load this skill when ..." and describe the trigger situation, so the agent knows when to use it.
* The body must be concrete, actionable instructions — prefer a bulleted list.

## Good practices

* Write the body for a non-programmer scientist: explain steps in plain language, prefer named variables, add short comments.
* Keep each skill focused on ONE topic. Split unrelated concerns into separate skills.
* Tell the agent both *what* to do and *how to communicate* results to the user.

## Workflow when helping the user

1. Ask what task the skill should cover (if unclear).
2. Propose a `name` (kebab-case) and confirm it will be the file name.
3. Draft the frontmatter, then the body.
4. Show the complete file content to the user and tell them to save it as
   `skills/<name>.md`. Do NOT use write_file for this: write_file saves into the
   `sandbox/` directory, but skills must live in the `skills/` directory, so the
   user has to place the file there themselves.
5. Remind the user to restart the agent so the new skill is detected.
