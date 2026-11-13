---
title: 26-27 Game - Milestones
description: "What each Space Jam milestone added to the codebase, and how to update these docs for the next one."
tags:
  - project
  - reference
---

# Milestones

The codebase docs always describe the latest milestone. This page records what each milestone added, so you can see how the project got here. To read the docs as they were for an older milestone, open this site's history on GitHub at the commit that updated them.

| Milestone | Game release | Code as of | Docs updated |
|---|---|---|---|
| Milestone 1 | [v0.1.0](https://github.com/PurdueSIGGD/SIGGD-Game-2026/releases/tag/v0.1.0) | `e3d0779`, 2026-11-08 | 2026-11-13 |

---

## Milestone 1 (v0.1.0)

The first playable build: one player can fly, shoot, bomb, and fight the Factory Planet in MasterScene, with sound.

| Area | Pull requests |
|---|---|
| Damage interface | [#45 Add damageable interface](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/45) |
| Player | [#47 Player movement prototype](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/47), [#61 Player health and damage](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/61), [#102 Starting impulse](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/102), [#104 Input refactor](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/104) |
| Weapons, tools, loadout, passives | [#77 Projectile systems](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/77) |
| Asteroids | [#85 Asteroid system](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/85) |
| Audio | In FMOD Studio: [#86 FMOD project](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/86), [#98 FMOD events](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/98), [#99 First half of the sound effects](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/99), [#101 All MVP 1 sound effects](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/101). In Unity (`AudioManager`, `AudioEvents`, every sound call): #105 below. |
| Boss, HUD, audio in Unity, art, integration | [#105 Add art assets and unify systems](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/105) |
| Direct commits after #105 | `bcb3b27`: drone art, the boss's no-repeat attack rule, robot nearest-player targeting, killable robots, the seven test asteroids in MasterScene, and balancing. `e3d0779`: the Factory Planet's background color and bullet sprite. |
| Project setup and shared infrastructure | `57e14c5` Pre-production setup commit (singletons, event bus, repo setup), [#68 Switch to the 2D renderer](https://github.com/PurdueSIGGD/SIGGD-Game-2026/pull/68) |

**Open at the end of Milestone 1:** single-player game over and the boss death sequence, tool swapping and passive effects in the loadout, a fire-rate limit, wiring the asteroid system into MasterScene, and the GDD's second Factory phase. Each system page lists the details under **Known Issues**.

---

## Updating the Docs for a New Milestone

For whoever updates these pages next. Do it on one branch, as one pull request.

1. **Tag the release** in the game repo, using [semantic versioning](https://semver.org/): `v0.2.0` for Milestone 2. Publish a GitHub Release with short notes.
2. **Update the banner** in `docs/includes/2627-game/milestone.md`: milestone name, tag, short commit hash, and date. Every codebase page includes this file.
3. **Repoint source links.** Replace `blob/v0.1.0/` and `tree/v0.1.0/` with the new tag everywhere under `docs/projects/2627-game/`. Then re-check every link with a line number (`#L123`), since the lines will have moved.
4. **Find what changed.** In the game repo:

    ```bash
    git diff --stat v0.1.0 v0.2.0 -- Assets ':!Assets/Plugins'
    git diff --name-status v0.1.0 v0.2.0 -- '*.cs' ':!Assets/Plugins'
    ```

    Added, removed, and renamed scripts go in the [Script Index](scripts/index.md) and on their system page. Changed `.asset` files mean the [Tuning Guide](tuning-guide.md) values need updating.

5. **Revisit every Known Issues list.** Delete what was fixed, add what's new, and re-check the "Differs from the GDD" notes against the current GDD.
6. **Update the Overview's "Milestone 1 at a Glance" table** and rename it for the new milestone.
7. **Add a row and a section to this page.**
8. **Build with `mkdocs build --strict`** and click through the diagrams. Mermaid fails quietly, so a broken diagram renders as raw text instead of failing the build.
