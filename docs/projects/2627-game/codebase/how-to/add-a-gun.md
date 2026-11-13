---
title: Add a Gun
description: "Make a new gun for Space Jam from assets alone: a projectile, a gun, and a visual."
tags:
  - project
  - programming
  - unity
---

# Add a Gun

--8<-- "includes/2627-game/milestone.md"

A gun is three assets and no code: a **projectile** (what comes out), a **gun** (how it fires), and a **visual prefab** (what the player holds). The quickest way to start is to copy the Pistol's three assets and change them. For how firing works, see [Weapons and Projectiles](../systems/weapons.md).

---

## 1. Make the Projectile

Skip this step if an existing projectile works; several guns can share one.

1. In `Assets/Projectiles/Bullets/`, duplicate `PistolBullet.asset` (++ctrl+d++) and rename it, say `SniperBullet`.
2. Set its fields. The [Tuning Guide](../tuning-guide.md#projectiles) explains each one.
    - **Damage**, **Lifetime** (seconds), and **Velocity** (units per second).
    - **Projectile Sprite**. The bullet's collider takes this sprite's physics shape, so a long thin sprite gets a long thin hitbox.
    - **Projectile Color** and **Projectile Scale** to tint and size it without new art.
3. Leave **Spline Game Object** empty. Spline bullets are a work in progress.

## 2. Make the Gun Visual

1. In `Assets/Equipment/WeaponPrefabs/`, duplicate `Test_Pistol_Prefab.prefab` and open it.
2. Swap the sprite for your gun's art.
3. Move the two child objects so they sit where they should:
    - `Holdpoint` goes where the hand grips the gun.
    - `Firepoint` goes at the muzzle. Bullets spawn here.

Make sure the root still has `WeaponPrefabTransformHolder` with both fields filled in. `PrimaryGun` reads it when the gun is equipped.

## 3. Make the Gun Asset

1. In `Assets/Equipment/WeaponScriptableObjects/`, right-click and choose **Create > Scriptable Objects > PrimaryWeapon**. (Or duplicate `Pistol.asset`. Don't duplicate `Shotgun.asset`, which is a projectile asset by mistake.)
2. Fill it in:

    | Field | Set it to |
    |---|---|
    | `Projectile` | The projectile from step 1 |
    | `Weapon Name` | The display name, shown by the loadout menu |
    | `Num Bullets` | Bullets per shot. Use `1` for a single bullet. |
    | `Spread` | Width of the bullet fan in degrees. With one bullet, the bullet lands at a random angle inside it. |
    | `Offset` | Extra random angle per bullet, in degrees either way |
    | `Recoil` | How hard each shot pushes the player backward |
    | `Ammo Capacity` | Rounds in a full magazine |
    | `Reload Time` | Seconds to refill from empty. Refilling is continuous. |
    | `Weapon Visual Prefab` | The prefab from step 2 |
    | `Weapon Visual Rotation Offset` | Degrees to rotate the visual if it points the wrong way |
    | `Fire Speed` | Anything. It's unused at v0.1.0, since fire rate isn't limited yet. |

## 4. Try It

1. Open `Assets/Player/Player.prefab`, select `WeaponHolder`, and drag your gun asset into `Primary Gun > Weapon`.
2. Press **Play** in MasterScene and shoot.
3. Undo the prefab change before you commit, unless your gun should be the new default. To offer it as a choice instead, give it a button in the [loadout menu](../systems/loadout.md).

---

## Things to Watch For

- **Multi-bullet guns.** Bullets collide with each other at v0.1.0, so a shotgun's pellets that spawn overlapping cancel each other out at the muzzle. See [Known Issues](../systems/weapons.md#known-issues).
- **Recoil and the speed cap.** The player's speed is clamped to `Max Velocity` every physics step, so at top speed recoil can turn you or slow you down, but not add lasting speed.
- **Commit the `.meta` files.** Every new asset has a matching `.meta` file, and Unity loses references without it.
