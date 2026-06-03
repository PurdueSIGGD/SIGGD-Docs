---
title: Example Project — Systems Overview
description: Overview of all game systems in Example Project with links to detailed documentation.
tags:
  - project
  - reference
---

# Systems Overview

Each major game system has its own documentation page covering what it does,
how it works, its public interface, and how to use it.

| System | Script | Status | Description |
|--------|--------|--------|-------------|
| [Player Controller](player-controller.md) | `PlayerController.cs` | Documented | Input, movement, animation |
| Enemy AI | `EnemyAI.cs` | Needs docs | Patrol, detect, chase FSM |
| Game Manager | `GameManager.cs` | Needs docs | Singleton, scene management |
| Save System | `SaveSystem.cs` | Needs docs | JSON save/load |

---

!!! tip "Adding system docs"
    Copy the [System Template](../../../../contributing/templates/system-template.md)
    and create a new file in this folder. Then add it to the table above and
    to the `nav:` in `mkdocs.yml`.
