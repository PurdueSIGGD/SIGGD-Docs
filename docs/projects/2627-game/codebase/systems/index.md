---
title: 26-27 Game - Systems
description: "One page per gameplay system in Space Jam, with class reference and known issues."
tags:
  - project
  - reference
  - programming
---

# Systems

--8<-- "includes/2627-game/milestone.md"

Each page covers one system: what it does, how the classes connect, the public API of every class, and what's broken or unfinished.

| System | What it covers | Main classes |
|---|---|---|
| [Player](player.md) | Movement, braking, input, aiming, health, death, co-op ghosts | `PlayerController`, `PlayerInputHandler`, `PlayerHealth`, `PlayerDeath`, `PlayerRegistry` |
| [Damage and Health](damage.md) | The contract between everything that deals and takes damage | `IDamageable`, `DamageContext` |
| [Weapons and Projectiles](weapons.md) | The gun, gun and bullet assets, the bullet pool, arm aiming | `PrimaryGun`, `ProjectileManager`, `Bullet`, `PrimaryWeapon`, `ProjectileScriptableObject` |
| [Tools](tools.md) | The right-click tool slot and the bomb | `Tool`, `ToolUser`, `ProjectileTool`, `Bomb` |
| [Loadout and Passives](loadout.md) | The loadout menu and passive upgrades | `LoadoutTarget`, `Equip*Button`, `Passive`, `PassiveHolder` |
| [Boss](boss.md) | Phases, weighted random attacks, the four attack types, lasers, robots | `GenericBoss`, `BossData`, `BossAttack`, `Laser`, `Robot` |
| [Asteroids](asteroids.md) | Spawning, impact damage, momentum-conserving fragments | `AsteroidSpawner`, `AsteroidController`, `AsteroidData` |
| [Audio](audio.md) | FMOD events, the generated `AudioEvents` class, music | `AudioManager`, `AudioEvents`, `AudioEventsGenerator` |
| [Shared Infrastructure](infrastructure.md) | Singletons, the event bus, and the object pool | `Singleton<T>`, `EventBus<T>`, `PrefabPool` |

## Reading a System Page

System pages follow the same order, so you can jump to the part you need. Two pages differ: Audio opens with its asset pipeline instead of a class diagram, and Shared Infrastructure has one section per tool, since its three tools are unrelated.

1. **How It's Put Together:** a class diagram of the system. In these diagrams, a solid arrow means "holds a reference to", a dotted arrow means "uses or creates", a hollow triangle means "inherits from", and a dotted line with a hollow triangle means "implements".
2. **How It Works:** the runtime behavior, with state diagrams where something changes state.
3. **Class Reference:** each class's public members and Inspector fields, with a link to its source at v0.1.0. Fields with (Inspector) after their type are private `[SerializeField]`s.
4. **Extending:** where new code should go, and the matching [How-To](../how-to/index.md) recipe.
5. **Known Issues:** bugs and gaps at v0.1.0, then where the code **differs from the GDD** (the [Game Design Document](../../design/game-design-doc.md)). Each is a candidate task.
