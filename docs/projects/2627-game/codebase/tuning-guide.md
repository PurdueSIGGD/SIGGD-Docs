---
title: Tuning Guide
description: "Every asset a designer can edit to change how Space Jam plays, with units and the values shipped in Milestone 1."
tags:
  - project
  - game-design
  - reference
---

# Tuning Guide

--8<-- "includes/2627-game/milestone.md"

Most of Space Jam's feel comes from numbers stored in assets. This page lists those assets, what each field does, and its value at v0.1.0, so you can tune the game without opening a script.

---

## Before You Start

1. **Get the project open.** If you haven't installed Unity and cloned the game, follow [Getting Set Up](../../../tutorials/general/getting-set-up.md) first. It walks through GitHub Desktop and the right Unity version.
2. **Find the asset** in Unity's **Project** window (bottom of the screen by default), using the path given in each section below.
3. **Click it.** Its fields appear in the **Inspector** (right side). Each field below is listed by the name the Inspector shows.
4. **Change a value, then press Play** in `Assets/Scenes/MasterScene.unity` to try it.
5. **Share the change.** Either open a pull request with the changed `.asset` file ([The PR Workflow](../../../tutorials/general/gitgood2.md) shows how), or send the numbers to a programmer to put in.

!!! warning "Asset edits made during Play mode are kept"
    Changes to an object in the scene are thrown away when you stop playing, but changes to these assets are **saved**. That makes it easy to tune while playing, and just as easy to forget what you changed. Write down your starting values, and check GitHub Desktop's **Changes** tab before you share anything.

!!! info "When a tooltip disagrees with this page, trust this page"
    Hovering over a field shows its tooltip, but three tooltips are wrong at v0.1.0: `Impulse` and `Mass` on the player stats, and `Debuff` on passives. The rows below give the real behavior.

Units used below: distances are in **units** (Unity's world units), speeds in **units per second**, angles in **degrees**, and times in **seconds** unless a row says otherwise.

---

## Common Goals

**Make the player feel faster.** In [Player](#player), raise `Max Velocity` (top speed) and `Acceleration` (how fast you reach it), or lower `Deceleration` so you glide longer. Careful: raising `Max Velocity` also makes rams hit harder. At 10 or more, a single full-speed ram kills the Factory Planet.

**Make the first boss easier.** In [Boss](#boss) and [Boss Attacks](#boss-attacks):

- Lower its health (the first number in `Phase Health Boundaries`), or raise `Damage Multiplier` so rams do more.
- Lengthen each attack's `Cooldown` so there's more rest between attacks.
- Shorten the lasers' `Lifetime`. At v0.1.0 it's 500 seconds, so lasers pile up all fight.
- Lower the scrap fan's `Projectile Count`, or lower `Damage` on `BossBasicBullet`.

### What Hurts What at v0.1.0

**The player** has 3 HP. Hits come from boss scrap bullets (1 each), lasers (1 per second while inside one), and the test asteroids (1 each). Robots touch you for no damage. Getting caught in your own bomb's blast counts as a hit that does 0 damage but still slows you.

**The boss** has 100 HP. Hits come from rams and pushed objects moving faster than 5 units per second (10 damage per unit per second of speed), player bullets (5 each, with no fire-rate limit), and bombs (0 damage as shipped). The GDD doesn't want bullets to hurt the boss; that's a [known gap](systems/damage.md#differs-from-the-gdd).

---

## Player

**Asset:** `Assets/Player/PlayerStats.asset` &nbsp;&middot;&nbsp; **System:** [Player](systems/player.md)

| Field | v0.1.0 | What it does |
|---|---|---|
| Max Velocity | 8 | Top speed, in units per second. The player can creep slightly past it while thrusting (about 8.4). |
| Acceleration | 20 | How quickly the player speeds up while holding a direction (units per second, every second). Heavier players accelerate slower. |
| Deceleration | 4 | How quickly the player slows down after letting go (units per second, every second). |
| Impulse | 20 | A one-time push when starting from a standstill. Heavier players get a smaller push. Its tooltip wrongly says it's unused. |
| Mass | 1 | How heavy the player is. Heavier means slower to accelerate, a smaller starting push, and harder shoves on whatever you hit. It doesn't change deceleration, despite its tooltip. |
| Max Health | 3 | Hit points. |
| Revive Health | 1 | Health after a teammate revives your ghost. |
| Iframe Duration | 1 | Seconds of invincibility after taking a hit. |
| Damage Speed Decrease | 2 | Speed lost when hit, in units per second. |
| Base Ghost Speed | 2 | How fast a ghost drifts after the player's first death. |
| Death Speed Increase | 1 | Extra ghost speed for each later death of the same player. |
| Move Speed | 8 | Unused at v0.1.0. |

!!! tip "How these interact"
    - With `Impulse` at 20 and `Max Velocity` at 8, starting from a standstill launches the player straight to top speed. Lower `Impulse` below `Max Velocity` if you want a visible ramp-up.
    - A ram faster than 5 units per second deals 10 x its speed in damage to the boss. At a `Max Velocity` of 8, a full-speed ram deals about 80 of the Factory Planet's 100 HP.

---

## Guns

**Assets:** `Assets/Equipment/WeaponScriptableObjects/` (the Pistol is `Pistol.asset`) &nbsp;&middot;&nbsp; **System:** [Weapons and Projectiles](systems/weapons.md)

| Field | Pistol | What it does |
|---|---|---|
| Projectile | `PistolBullet` | Which projectile asset the gun fires. |
| Weapon Name | Test Pistol | Name shown in the loadout menu. |
| Num Bullets | 0 (fires 1) | Bullets per shot. Below 1 counts as 1. |
| Spread | 0 | Width of the cone the bullets spread across, in degrees. A single bullet lands at a random angle inside it; several are spaced evenly. |
| Offset | 0 | Extra random angle added to each bullet, either way, in degrees. |
| Recoil | 2 | Push on the player opposite the shot, in units per second. Heavier players get pushed less. |
| Ammo Capacity | 12 | Rounds in a full magazine. Each shot uses one, however many bullets it fires. |
| Reload Time | 10 | Seconds to refill from empty. The gun refills continuously and can fire while refilling. |
| Weapon Visual Prefab | `Test_Pistol_Prefab` | The gun art the player holds. |
| Weapon Visual Rotation Offset | 0 | Rotates the held art if it points the wrong way, in degrees. |
| Fire Speed | 30 | Unused at v0.1.0, since fire rate isn't limited yet. |

To make a new gun, see [Add a Gun](how-to/add-a-gun.md).

---

## Projectiles

**Assets:** `Assets/Projectiles/Bullets/` &nbsp;&middot;&nbsp; **System:** [Weapons and Projectiles](systems/weapons.md)

Guns, boss attacks, and robots all read projectile assets, so changing one changes everything that uses it.

| Field | What it does |
|---|---|
| Damage | Damage dealt to whatever the projectile hits. Whole numbers only. |
| Lifetime | Seconds before the projectile disappears on its own. |
| Velocity | Travel speed, in units per second. |
| Sprite Angle Offset | Turns the projectile's direction of travel, and its sprite, by this many degrees. |
| Projectile Sprite | The art. Its shape becomes the hitbox. |
| Projectile Color | Tint over the sprite. |
| Projectile Scale | Size, without needing new art. |
| Is Explosive | Unused at v0.1.0. |
| Spline Game Object | Work in progress. Leave empty. |

| Asset | Used by | Damage | Lifetime | Velocity |
|---|---|---|---|---|
| `PistolBullet` | The Pistol | 5 | 15 | 20 |
| `BossBasicBullet` | The boss's scrap fan | 1 | 10 | 5 |
| `Robot` | Spawned robots (their look, lifetime, and speed) | Unused: robots deal no damage | 20 | 2 |
| `BossBomb` | The boss's AOE bomb attack, which isn't in use | 0 | 10000 | 1 |
| `TestBullet` | Spline testing | 4 | 15 | 10 |

---

## Boss

**Asset:** `Assets/GenericBoss/Factory Boss Data.asset` &nbsp;&middot;&nbsp; **System:** [Boss](systems/boss.md)

| Field | v0.1.0 | What it does |
|---|---|---|
| Phase Health Boundaries | `[100]` (one phase) | Health where each phase begins, highest first. The first number is max health. `[100, 50]` would add a second phase below 50 HP. |
| Speed Damage Threshold | 5 | Impacts must be faster than this (units per second) to hurt the boss. |
| Damage Multiplier | 10 | Damage per unit per second of impact speed. |
| Attack Percent List | `BasicAttack`, `LaserAttack`, `RobotSpawn` | The attacks the boss can pick from (weight assets, below). |
| Boss Sound Track | `Boss_1_Music` | The music. |

### Attack Weights

**Assets:** `BasicAttack.asset`, `LaserAttack.asset`, and `RobotSpawn.asset` in `Assets/GenericBoss/`

Each weight asset pairs one attack with a list of `Chance Weights`, one number per phase. An attack's chance is its weight divided by the total weight of all attacks in that phase. `0` takes an attack out of a phase. The boss never uses the same attack twice in a row unless it's the only option.

| Asset | Attack | Chance Weights | Chance at v0.1.0 |
|---|---|---|---|
| `BasicAttack` | Scrap fan | `[1, 1]` | About 1 in 3 overall |
| `LaserAttack` | Lasers | `[1, 1]` | About 1 in 3 overall |
| `RobotSpawn` | Robot spawn | `[1, 2]` | About 1 in 3 overall |

Because of the no-repeat rule, each pick is really a coin flip between the two attacks that didn't just fire. The second weight in each list is ready for a phase 2 that doesn't exist yet. If you add phases to `Phase Health Boundaries`, every weight asset needs a number for each one.

### Boss Attacks

**Assets:** in `Assets/GenericBoss/`. The [Boss page](systems/boss.md#names-for-the-same-attack) maps each attack's name to its files.

!!! warning "Watch the units and the angles"
    `Delay` is in **milliseconds** (500 = half a second), but `Cooldown` and `Lifetime` are in **seconds**. Positions are **world coordinates**: spots in the scene, not distances from the boss. The scrap fan and robots measure angles from **up, clockwise**; lasers measure them from **right, counterclockwise**.

**Scrap fan** (`BossAtkLinearFan.asset`): fires bullets one at a time, turning between shots.

| Field | v0.1.0 | What it does |
|---|---|---|
| Cooldown | 2 | Seconds of rest after the attack before the boss picks again. |
| Pso | `BossBasicBullet` | The projectile asset it fires. |
| Origin | `[1, 1]` | Where the bullets come from, as `[x, y]`. |
| Projectile Count | 100 | Number of shots. At 500 ms apart, the attack lasts 50 seconds. |
| Delay | 500 | Milliseconds between shots. |
| Init Angle | -45 | Direction of the first shot (0 = up, 90 = right). |
| Angle Offset | 15 | How far each shot turns from the last. |
| H Offset | 0 | How far the origin slides sideways after each shot. |
| Target Layer Mask | `Asteroid`, `Player` | No effect at v0.1.0. |
| Ignore Player Mask | `Enemy`, `Boss` | What the bullets pass through. Keep `Boss` in it. |

**Lasers** (`BossAttackLaser.asset`): two beams at once.

| Field | v0.1.0 | What it does |
|---|---|---|
| Cooldown | 2 | Seconds of rest after the attack. The attack itself ends instantly, so the next one can start while the beams are still up. |
| Origin | `(26, 0)` | Where both beams start. |
| Length | 70 | Beam length, in units. |
| Left Angle, Right Angle | 165, 195 | Direction of each beam (0 = right, 90 = up, 180 = left). |
| Damage | 1 | Damage per second to anything inside a beam. Nothing is hurt during a beam's first second. |
| Lifetime | 500 | How long the beams stay, in seconds. 500 is over eight minutes and is probably a mistake; see [Boss](systems/boss.md#known-issues). |
| Laser | `Laser` prefab | The beam's art and collider. |

**Robot spawn** (`BossAttackRobotSpawn.asset`): launches robots that chase the nearest player.

| Field | v0.1.0 | What it does |
|---|---|---|
| Cooldown | 2 | Seconds of rest after the attack. |
| Pso | `Robot` | The projectile asset for the robots' look, speed, and lifetime. |
| Origin | `[1, 1]` | Where robots spawn. |
| Projectile Count | 3 | Number of robots. |
| Delay | 500 | Milliseconds between robots. |
| Init Angle, Angle Offset, H Offset | -45, 45, 0 | Launch directions, as with the scrap fan. |

Each robot has 10 HP (set on `Assets/Projectiles/Prefabs/Robot.prefab`) and re-aims at the nearest player every 3 seconds. Robots don't hurt the player at v0.1.0.

**AOE bomb** (`BossAttackBomb.asset`) isn't in the Factory Planet's attack list. It fires `Projectile Count` (1) projectiles from `Origin` (`[10, 0]`), `Delay` (0) ms apart, at where the player will be one second later, using the `BossBomb` projectile.

---

## Tools

**Assets:** `Assets/Equipment/Tools/Scriptable Objects/` &nbsp;&middot;&nbsp; **System:** [Tools](systems/tools.md)

**Bomb Thrower** (`Tools/BombThrowerData.asset`):

| Field | v0.1.0 | What it does |
|---|---|---|
| Cooldown | 1 | Seconds between throws. |

**Bomb** (`Projectiles/BombData.asset`):

| Field | v0.1.0 | What it does |
|---|---|---|
| Speed | 8 | How fast the bomb floats away, in units per second. |
| Fuse Time | 2 | Seconds until it explodes. |
| Blast Radius | 3 | How far the explosion reaches, in units. |
| Blast Damage | 0 | Damage to everything in the blast, the thrower included. Even at 0, catching yourself counts as a hit that slows you. |
| Blast Impulse | 20 | Push at the center of the blast. |
| Blast Min Distance | 0.5 | Inside this distance, things get the full push. Beyond it, the push falls off: twice as far gets half. |
| Lifetime | 0 | Unused at v0.1.0. |

---

## Passives

**Assets:** `Assets/PassiveFiles/` &nbsp;&middot;&nbsp; **System:** [Loadout and Passives](systems/loadout.md)

!!! info "Passives don't do anything yet"
    You can create and edit passive assets, and the loadout menu stores the chosen one, but no code applies them at v0.1.0. The values below are what's in the assets, ready for when it does.

| Field | Meaning (from the Passive Inspector's guide) |
|---|---|
| Description | What the passive does, in words. |
| Buff | A positive change to a stat. |
| Debuff | A negative change to a stat. Its tooltip, about extra asteroids, is wrong. |
| Mode | `Flat` adds or subtracts the number directly. `Percent` changes the stat by that percentage. |

A passive that turns on an ability instead of changing a number keeps `Buff` and `Debuff` at 0.

| Asset | Buff | Debuff | Mode |
|---|---|---|---|
| `Asteroid Spawner` | 0 | 0 | Flat |
| `Coolant` | 20 | 0 | Percent |
| `HPIncrease` | 20 | 0 | Percent |
| `ImprovedThruster` | 20 | 0 | Percent |
| `Tungsten Cube` | 20 | 0 | Percent |

---

## Asteroids

**System:** [Asteroids](systems/asteroids.md)

??? note "No asteroid assets exist yet (open for the fields you'll get)"
    The full asteroid system isn't in MasterScene yet, so there's nothing to edit. Once someone creates these assets, they'll have the fields below, starting at these defaults.

    **Asteroid Data**, one per asteroid type:

    | Field | Default | What it does |
    |---|---|---|
    | Base Mass, Mass Variation Percentage | 1, 0.2 | Average mass, randomized by up to this fraction either way (0.2 = 20%). |
    | Base Size, Size Variation Percentage | 1, 0.2 | Average scale, randomized the same way. |
    | Base Max Health | 100 | Health at spawn. |
    | Max Initial Spin | 30 | Largest random starting spin, in degrees per second. |
    | Asteroid Sprite | none | Sprite used when this data is applied to a fragment. |
    | Debris Count | 3 | Fragments it breaks into. 0 means it just explodes. |
    | Fragment Prefab, Fragment Data | none | What the fragments are. Give the fragment data a `Debris Count` of 0 to stop splitting. |
    | Explosion Prefab, Explosion Scale | none, 1 | The flash when it breaks (optional), and its size relative to the asteroid. |
    | Explosion Impulse, Impulse Variation Percentage | 1, 0.25 | How hard fragments fly apart, randomized by up to this fraction. |
    | Fragment Spawn Radius | 0.3 | How far from the center fragments appear, as a fraction of the asteroid's size. |

    **Asteroid Spawner Data:**

    | Field | Default | What it does |
    |---|---|---|
    | Asteroid Prefab | none | What to spawn. |
    | Period | 2 | Seconds between spawns. |
    | Boundary Type | Camera | Aim at the camera view, or at the spawner's box collider. |
    | Center Angle, Spread | 270, 0 | Direction asteroids travel (0 = right, 90 = up, 270 = down), plus or minus a random spread. |
    | Min Travel Distance | 2 | Shortest distance from spawn point to target point. |
    | Offscreen Margin | 1 | How far past the screen edge asteroids spawn. Use at least the asteroid's radius. |
    | Target Inset | 0 | Keeps target points this far in from the screen edges. |
    | Linear Damping | 1 | How quickly asteroids slow down. The spawner adjusts launch speed so they still drift to their target. |

    On the asteroid prefab itself, `Speed Damage Threshold` (5) and `Damage Multiplier` (10) work like the boss's.
