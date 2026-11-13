---
title: 26-27 Game
description: "Space Jam, SIGGD's 2026-2027 project: a 2D physics boss rush where you destroy evil planets by ramming things into them."
tags:
  - project
  - unity
status: in-development
year: 2027
engine: Unity
genre: 2D physics boss rush
repo_url: https://github.com/PurdueSIGGD/SIGGD-Game-2026
---

# Space Jam (26-27 Game)

Space Jam is a 2D boss rush where you, solo or with a friend, destroy evil planets. You float in zero gravity, build up speed with your jetpack and equipment, and damage each planet boss by ramming yourself or an asteroid into it. The design team's one-line pillar is **Speed = Damage = Good**.

| | |
|---|---|
| **Engine** | Unity 6 (6000.3.21f1), 2D, Universal Render Pipeline |
| **Genre** | 2D side-view boss rush, physics-based, co-op |
| **Players** | 1 or 2, local |
| **Status** | In development. Milestone 1 shipped as [v0.1.0](https://github.com/PurdueSIGGD/SIGGD-Game-2026/releases/tag/v0.1.0). |
| **Source** | [PurdueSIGGD/SIGGD-Game-2026](https://github.com/PurdueSIGGD/SIGGD-Game-2026) |

---

## The Game Loop

Each level is one boss fight against a planet. The [Game Design Document](design/game-design-doc.md) plans seven bosses, starting with the Factory Planet and ending with the Sun.

1. Pick a loadout: a gun, a tool, and a passive.
2. Fight the boss. Learn its attack patterns, dodge, and land hits by building speed.
3. Win, earn a rank and a reward, and buy new equipment for the next fight.

Bosses only take damage from collisions: an asteroid you pushed into them, or you ramming them fast enough. In the design, your gun doesn't hurt the boss: bullets clear boss projectiles, break asteroids, and push you around through recoil.

!!! info "What you can play at v0.1.0"
    One player fights the Factory Planet in a single phase, with the Pistol and the Bomb Thrower. Several things don't match the design yet: bullets do hurt the boss, the test asteroids hurt you instead of being pushable, robots are harmless, and nothing happens when either side dies. The [codebase overview](codebase/index.md#milestone-1-at-a-glance) lists what's built.

---

## Controls

These are the bindings in the game's input actions as of Milestone 1.

| Action | Keyboard and mouse | Gamepad |
|---|---|---|
| Move | ++w++ ++a++ ++s++ ++d++ or arrow keys | Left stick |
| Aim | Mouse | Right stick |
| Fire gun | Left click | Right trigger |
| Use tool | Right click | Left trigger |
| Tool alternate (hold) | ++e++ | North button (Y on Xbox) |
| Brake | ++space++ | Left bumper |
| Previous / next (not used yet) | ++1++ / ++2++ | D-pad left / right |

---

## Where to Go Next

<div class="grid cards" markdown>

-   :material-file-document-outline:{ .lg .middle } **Design**

    ---

    The Game Design Document, the Art Document, and the Audio Tracker, embedded live from Google Drive.

    [:octicons-arrow-right-24: Design docs](design/index.md)

-   :material-tune-variant:{ .lg .middle } **Tuning Guide**

    ---

    For designers: every number you can change to make the game feel different, with no code.

    [:octicons-arrow-right-24: Tuning Guide](codebase/tuning-guide.md)

-   :material-code-braces:{ .lg .middle } **Codebase**

    ---

    How the Unity project is put together: architecture, every system, and how-to recipes.

    [:octicons-arrow-right-24: Codebase docs](codebase/index.md)

-   :material-book-open-variant:{ .lg .middle } **Story**

    ---

    The story team's design document and task list.

    [:octicons-arrow-right-24: Story](story/index.md)

</div>
