---
title: 26-27 Game - How-To
description: "Step-by-step recipes for the most common changes to Space Jam."
tags:
  - project
  - programming
  - unity
---

# How-To

--8<-- "includes/2627-game/milestone.md"

Recipes for the changes people make most often. Each one assumes you have the project open in Unity and a branch for your change (see [The PR Workflow](../../../../tutorials/general/gitgood2.md)). For background on how a system works, follow the links to its system page.

| Recipe | Code? | You'll touch |
|---|---|---|
| [Add a Gun](add-a-gun.md) | No | A projectile asset, a gun asset, a gun visual prefab |
| [Add a Boss Attack](add-a-boss-attack.md) | Yes, one class | A `BossAttack` subclass, its asset, an `AttackPercents` asset, the boss's `BossData` |
| [Add a Tool](add-a-tool.md) | Yes, one class | A `Tool` subclass, a `ToolData` asset, the player prefab |
| [Add a Sound Effect](add-a-sound.md) | One line | FMOD Studio, the generated `AudioEvents.cs`, the script that plays it |

To change a number, like gun recoil, boss health, or player speed, find its asset in the [Tuning Guide](../tuning-guide.md) and edit it.
