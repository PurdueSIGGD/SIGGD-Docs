---
title: Add a Boss Attack
description: "Write a new BossAttack pattern, make an asset for it, and add it to a boss's attack pool."
tags:
  - project
  - programming
  - unity
---

# Add a Boss Attack

--8<-- "includes/2627-game/milestone.md"

Boss attacks are ScriptableObjects, so a new pattern is one class plus a few assets. Before you write code, check whether one of the [four existing attack types](../systems/boss.md#the-attack-types) can do it with different settings. More bullets, a different angle, or a new projectile is a new asset, not a new class.

This recipe builds a **ring**: a burst of bullets in every direction at once, fired from the boss itself.

---

## 1. Write the Attack Class

Create `Assets/GenericBoss/BossAttackRing.cs`:

```csharp
using Cysharp.Threading.Tasks;
using UnityEngine;

/// <summary>
/// Fires one bullet in each of <c>bulletCount</c> evenly spaced directions from the boss.
/// </summary>
[CreateAssetMenu(fileName = "BossAttackRing", menuName = "Data/BossAttackRing")]
public class BossAttackRing : BossAttack
{
    [SerializeField] private ProjectileScriptableObject projectile;
    [SerializeField, Min(1)] private int bulletCount = 12;
    [SerializeField, Tooltip("Rotates the whole ring, in degrees.")] private float startAngle;
    [SerializeField] private LayerMask targetLayers;
    [SerializeField] private LayerMask ignoreLayers;

    public override UniTask Shoot(GameObject bossObject)
    {
        AudioManager.PlayOneShot(AudioEvents.Sound_Effects.Boss_1.Attacks.Boss_1_ShootScrap);

        for (int i = 0; i < bulletCount; i++)
        {
            float angle = startAngle + 360f * i / bulletCount;
            Vector2 direction = Quaternion.Euler(0f, 0f, angle) * Vector2.right;
            ProjectileManager.Instance.ShootProjectileTowardsDirection(
                projectile, bossObject.transform, direction, targetLayers, ignoreLayers);
        }

        return UniTask.CompletedTask;
    }
}
```

Things to copy from this into your own attack:

- **`Shoot` returns a task that finishes when the attack is done firing.** This one fires everything at once, so it returns `UniTask.CompletedTask` right away. The boss waits for the task, then waits `Cooldown` seconds, then picks again.
- **An attack that fires over time** should be `async` and wait between shots. Pass the boss's destroy token to each delay, so the attack stops if the boss is destroyed partway through. (The existing attacks don't, so they keep firing after the boss is gone.)

    ```csharp
    public override async UniTask Shoot(GameObject bossObject)
    {
        var token = bossObject.GetCancellationTokenOnDestroy();
        for (int i = 0; i < bulletCount; i++)
        {
            // fire one bullet here
            await UniTask.Delay(delayMilliseconds, cancellationToken: token);
        }
    }
    ```

- **Fire from `bossObject`**, not from fixed world coordinates. The existing attacks use world positions, so they break when the boss moves; passing `bossObject.transform` as the fire point keeps the attack attached to the boss.
- **Put every number in a serialized field**, so designers can make variants without touching code. The fields follow the [C# Style Guide](../../../../tutorials/programming/csharp-style-guide.md): `[SerializeField] private`, camelCase. (The older attack classes use `[field: SerializeField]` auto-properties instead.)

## 2. Make the Attack Asset

1. In `Assets/GenericBoss/`, right-click and choose **Create > Data > BossAttackRing**.
2. Set **Projectile** to an existing boss bullet, such as `Assets/Projectiles/Bullets/BossBasicBullet.asset`.
3. Set **Ignore Layers** to **Boss** and **Enemy**, so bullets spawned inside the boss don't hit it. (**Target Layers** has no effect at v0.1.0; see [Weapons and Projectiles](../systems/weapons.md#layers-who-a-bullet-can-hit).)
4. Set **Cooldown**, the seconds the boss rests after this attack. `2` is the default.

## 3. Give It a Weight

The boss doesn't reference attacks directly. It reads `AttackPercents` assets, which pair an attack with a weight for each phase.

1. Right-click and choose **Create > Data > AttackPercents**.
2. Set `Attack` to your new asset.
3. Set `ChanceWeights` to one number per boss phase. The Factory Boss has one phase, so one entry, such as `1`. An entry of `0` means "not in this phase".

!!! warning "One weight per phase, always"
    If a boss has three phases, every `AttackPercents` in its list needs three weights. A shorter array makes the boss read past the end of it when it reaches a later phase.

## 4. Add It to the Boss

Open `Assets/GenericBoss/Factory Boss Data.asset` and add your `AttackPercents` to `AttackPercentList`.

## 5. Try It

Press **Play** in MasterScene. To see your attack every time instead of about a quarter of the time, temporarily set the other attacks' weights to `0`. When only one attack has weight, the boss is allowed to repeat it. Put the weights back before committing.

---

## Checklist

- [ ] Delays are in **milliseconds** (`UniTask.Delay`), and `Cooldown` is in **seconds**.
- [ ] The attack plays a sound. If the right one doesn't exist yet, ask the audio team, then see [Add a Sound Effect](add-a-sound.md).
- [ ] Every `AttackPercents` you touched has one weight per phase.
- [ ] New `.cs` and `.asset` files are committed with their `.meta` files.
