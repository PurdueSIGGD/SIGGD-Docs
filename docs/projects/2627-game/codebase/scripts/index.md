---
title: 26-27 Game - Script Index
description: "Every C# script in the Space Jam project at Milestone 1, and the page that documents it."
tags:
  - project
  - reference
  - programming
---

# Script Index

--8<-- "includes/2627-game/milestone.md"

All 68 game scripts at v0.1.0 in alphabetical order, not counting third-party code in `Assets/Plugins/`. Each script links to its source, and each system links to its docs page.

| Script | Kind | Documented in |
|---|---|---|
| [`Asteroid.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerHealthTesting/Asteroid.cs) | `MonoBehaviour`, test only | [Asteroids](../systems/asteroids.md#the-test-asteroids-in-masterscene) |
| [`AsteroidController.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Asteroids/Scripts/AsteroidController.cs) | `MonoBehaviour` | [Asteroids](../systems/asteroids.md#asteroidcontroller) |
| [`AsteroidData.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Asteroids/Scripts/AsteroidData.cs) | `ScriptableObject` | [Asteroids](../systems/asteroids.md#asteroiddata) |
| [`AsteroidDespawnZone.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Asteroids/Scripts/AsteroidDespawnZone.cs) | `MonoBehaviour` | [Asteroids](../systems/asteroids.md#asteroiddespawnzone) |
| [`AsteroidSpawner.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Asteroids/Scripts/AsteroidSpawner.cs) | `MonoBehaviour` | [Asteroids](../systems/asteroids.md#asteroidspawner) |
| [`AsteroidSpawnerData.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Asteroids/Scripts/AsteroidSpawnerData.cs) | `ScriptableObject` | [Asteroids](../systems/asteroids.md#asteroidspawnerdata) |
| [`AttackPercents.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/AttackPercents.cs) | `ScriptableObject` | [Boss](../systems/boss.md#attackpercents) |
| [`AudioEvents.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Audio/AudioEvents.cs) | `static class`, generated | [Audio](../systems/audio.md#audioevents) |
| [`AudioEventsGenerator.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Audio/Editor/AudioEventsGenerator.cs) | `static class`, editor only | [Audio](../systems/audio.md#audioeventsgenerator-editor-only) |
| [`AudioManager.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Audio/AudioManager.cs) | `MonoBehaviour`, static methods | [Audio](../systems/audio.md#audiomanager) |
| [`Bomb.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Projectiles/Bomb.cs) | `ToolProjectile` | [Tools](../systems/tools.md#bomb) |
| [`BombData.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Data/BombData.cs) | `ToolProjectileData` | [Tools](../systems/tools.md#data-assets) |
| [`BombThrower.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Tools/BombThrower.cs) | `ProjectileTool` | [Tools](../systems/tools.md#bombthrower) |
| [`Bootstrapper.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/EventBus/Bootstrapper.cs) | `MonoBehaviour`, empty | [Shared Infrastructure](../systems/infrastructure.md#bootstrapper) |
| [`BossAttack.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/BossAttack.cs) | `abstract ScriptableObject` | [Boss](../systems/boss.md#bossattack) |
| [`BossAttackBomb.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/BossAttackBomb.cs) | `BossAttack` | [Boss](../systems/boss.md#the-attack-types) |
| [`BossAttackLaser.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/BossAttackLaser.cs) | `BossAttack` | [Boss](../systems/boss.md#the-attack-types) |
| [`BossAttackLinearFan.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/BossAttackLinearFan.cs) | `BossAttack` | [Boss](../systems/boss.md#the-attack-types) |
| [`BossAttackRobotSpawn.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/BossAttackRobotSpawn.cs) | `BossAttack` | [Boss](../systems/boss.md#the-attack-types) |
| [`BossData.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/BossData.cs) | `ScriptableObject` | [Boss](../systems/boss.md#bossdata) |
| [`Bullet.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Projectiles/Scripts/Bullet.cs) | `MonoBehaviour` | [Weapons and Projectiles](../systems/weapons.md#bullet) |
| [`EquipGunButton.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/LoadoutMenu/EquipGunButton.cs) | `MonoBehaviour` | [Loadout and Passives](../systems/loadout.md#equipgunbutton-equiptoolbutton-equippassivebutton) |
| [`EquipPassiveButton.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/LoadoutMenu/EquipPassiveButton.cs) | `MonoBehaviour` | [Loadout and Passives](../systems/loadout.md#equipgunbutton-equiptoolbutton-equippassivebutton) |
| [`EquipToolButton.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/LoadoutMenu/EquipToolButton.cs) | `MonoBehaviour` | [Loadout and Passives](../systems/loadout.md#equipgunbutton-equiptoolbutton-equippassivebutton) |
| [`EventBinding.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/EventBus/EventBinding.cs) | `class` | [Shared Infrastructure](../systems/infrastructure.md#eventbus) |
| [`EventBus.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/EventBus/EventBus.cs) | `static class` | [Shared Infrastructure](../systems/infrastructure.md#eventbus) |
| [`EventBusEditorUtils.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/EventBus/EventBusEditorUtils.cs) | `static class`, editor only | [Shared Infrastructure](../systems/infrastructure.md#eventbus) |
| [`Events.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/EventBus/Events.cs) | `IEvent` interface, `TestEvent` | [Shared Infrastructure](../systems/infrastructure.md#eventbus) |
| [`ExplosionEffect.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Asteroids/Scripts/ExplosionEffect.cs) | `MonoBehaviour` | [Asteroids](../systems/asteroids.md#explosioneffect) |
| [`GenericBoss.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/GenericBoss.cs) | `MonoBehaviour` | [Boss](../systems/boss.md#genericboss) |
| [`IDamageable.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Damage/IDamageable.cs) | `IDamageable` interface, `DamageContext` struct | [Damage and Health](../systems/damage.md#idamageable) |
| [`IEquipment.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/EquipmentManager/IEquipment.cs) | `interface` | [Loadout and Passives](../systems/loadout.md#iequipment) |
| [`Laser.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/Laser.cs) | `MonoBehaviour` | [Boss](../systems/boss.md#laser) |
| [`LazySingleton.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/Singleton/LazySingleton.cs) | `class` | [Shared Infrastructure](../systems/infrastructure.md#singletons) |
| [`LoadoutMenuEditors.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/LoadoutMenu/Editor/LoadoutMenuEditors.cs) | Five custom Inspectors, editor only | [Loadout and Passives](../systems/loadout.md#the-menu) |
| [`LoadoutReadout.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/LoadoutMenu/LoadoutReadout.cs) | `MonoBehaviour` | [Loadout and Passives](../systems/loadout.md#loadoutreadout) |
| [`LoadoutTarget.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/LoadoutMenu/LoadoutTarget.cs) | `MonoBehaviour` | [Loadout and Passives](../systems/loadout.md#loadouttarget) |
| [`Passive.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/PassiveFiles/Passive.cs) | `ScriptableObject`, `StatModifyMode` enum | [Loadout and Passives](../systems/loadout.md#passive-and-statmodifymode) |
| [`PassiveEditor.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/PassiveFiles/Editor/PassiveEditor.cs) | Custom Inspector, editor only | [Loadout and Passives](../systems/loadout.md#passives) |
| [`PassiveHolder.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/PassiveFiles/PassiveHolder.cs) | `MonoBehaviour` | [Loadout and Passives](../systems/loadout.md#passiveholder) |
| [`PersistentSingleton.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/Singleton/PersistentSingleton.cs) | `MonoBehaviour` base class | [Shared Infrastructure](../systems/infrastructure.md#singletons) |
| [`PlanetRotation.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/PlanetRotation.cs) | `MonoBehaviour` | [Boss](../systems/boss.md#planetrotation) |
| [`Player.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/Player.cs) | `MonoBehaviour` | [Player](../systems/player.md#class-reference) |
| [`PlayerAiming.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerAiming.cs) | `MonoBehaviour` | [Player](../systems/player.md#playeraiming) |
| [`PlayerAnimator.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerAnimator.cs) | `MonoBehaviour` | [Player](../systems/player.md#playeranimator) |
| [`PlayerController.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerController.cs) | `MonoBehaviour` | [Player](../systems/player.md#playercontroller) |
| [`PlayerData.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerData.cs) | `ScriptableObject` | [Player](../systems/player.md#playerdata) |
| [`PlayerDeath.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerDeath.cs) | `MonoBehaviour` | [Player](../systems/player.md#playerdeath) |
| [`PlayerHealth.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerHealth.cs) | `MonoBehaviour` | [Player](../systems/player.md#playerhealth) |
| [`PlayerInputHandler.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerInputHandler.cs) | `MonoBehaviour` | [Player](../systems/player.md#playerinputhandler) |
| [`PlayerRegistry.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerRegistry.cs) | `static class` | [Player](../systems/player.md#playerregistry) |
| [`PrefabPool.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Asteroids/Scripts/PrefabPool.cs) | `static class`, not asteroid-specific | [Shared Infrastructure](../systems/infrastructure.md#prefabpool) |
| [`PrimaryGun.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Projectiles/Scripts/PrimaryGun.cs) | `MonoBehaviour` | [Weapons and Projectiles](../systems/weapons.md#primarygun) |
| [`PrimaryWeapon.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/WeaponScripts/PrimaryWeapon.cs) | `ScriptableObject` | [Weapons and Projectiles](../systems/weapons.md#primaryweapon) |
| [`ProjectileManager.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Projectiles/Scripts/ProjectileManager.cs) | `Singleton<ProjectileManager>` | [Weapons and Projectiles](../systems/weapons.md#projectilemanager) |
| [`ProjectileScriptableObject.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Projectiles/ScriptableObjects/ProjectileScriptableObject.cs) | `ScriptableObject` | [Weapons and Projectiles](../systems/weapons.md#projectilescriptableobject) |
| [`ProjectileTool.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Tools/ProjectileTool.cs) | `abstract Tool` | [Tools](../systems/tools.md#projectiletool) |
| [`Robot.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/GenericBoss/Robot.cs) | `MonoBehaviour` | [Boss](../systems/boss.md#robot) |
| [`RotateArmToAim.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/WeaponScripts/RotateArmToAim.cs) | `MonoBehaviour` | [Weapons and Projectiles](../systems/weapons.md#rotatearmtoaim) |
| [`Singleton.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Extensions/Singleton/Singleton.cs) | `MonoBehaviour` base class | [Shared Infrastructure](../systems/infrastructure.md#singletons) |
| [`Spawner.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/PlayerHealthTesting/Spawner.cs) | `MonoBehaviour`, test only | [Asteroids](../systems/asteroids.md#the-test-asteroids-in-masterscene) |
| [`Tags.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Player/Tags.cs) | `static class` | [Player](../systems/player.md#tags) |
| [`Tool.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Core/Tool.cs) | `abstract MonoBehaviour` | [Tools](../systems/tools.md#tool) |
| [`ToolData.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Data/ToolData.cs) | `ScriptableObject` | [Tools](../systems/tools.md#data-assets) |
| [`ToolProjectile.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Projectiles/ToolProjectile.cs) | `abstract MonoBehaviour` | [Tools](../systems/tools.md#toolprojectile) |
| [`ToolProjectileData.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Data/ToolProjectileData.cs) | `ScriptableObject` | [Tools](../systems/tools.md#data-assets) |
| [`ToolUser.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/Tools/Scripts/Core/ToolUser.cs) | `MonoBehaviour` | [Tools](../systems/tools.md#tooluser) |
| [`WeaponPrefabTransformHolder.cs`](https://github.com/PurdueSIGGD/SIGGD-Game-2026/blob/v0.1.0/Assets/Equipment/WeaponScripts/WeaponPrefabTransformHolder.cs) | `MonoBehaviour` | [Weapons and Projectiles](../systems/weapons.md#weaponprefabtransformholder) |

