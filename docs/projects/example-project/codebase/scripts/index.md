---
title: Example Project — Script Reference
description: Quick-reference index of all major scripts in Example Project.
tags:
  - project
  - reference
---

# Script Reference

Quick-reference index for all major scripts. Click a script name for full
API documentation.

| Script | Location | Purpose |
|--------|----------|---------|
| [PlayerController](../systems/player-controller.md) | `Scripts/Player/` | Movement, input, animation |
| PlayerHealth | `Scripts/Player/` | HP, damage, death |
| EnemyAI | `Scripts/Enemies/` | Patrol, detect, chase |
| EnemyHealth | `Scripts/Enemies/` | Enemy HP and death |
| GameManager | `Scripts/Systems/` | Scene management, global state |
| SaveSystem | `Scripts/Systems/` | JSON save and load |
| HUDController | `Scripts/UI/` | Health bar, score display |
| PauseMenu | `Scripts/UI/` | Pause/resume, settings |

---

!!! tip "Adding script docs"
    Copy the [Script Template](../../../../contributing/templates/script-template.md)
    to create a new script reference page. Link it from the table above
    and add it to `nav:` in `mkdocs.yml`.
