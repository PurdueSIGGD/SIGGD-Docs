---
title: Add a Tool
description: "Write a new right-click tool by extending Tool, then put it on the player."
tags:
  - project
  - programming
  - unity
---

# Add a Tool

--8<-- "includes/2627-game/milestone.md"

A tool is a component that extends `Tool` and implements `OnUse()`. The base class handles the cooldown, and `ToolUser` handles input, so your class only says what the tool does. For background, see [Tools](../systems/tools.md).

This recipe builds the GDD's **Shockwave Shield**: an instant blast centered on the player that shoves everything nearby away and leaves the player in place.

!!! info "Pick the right base class"
    - Tools that **throw something** (bombs, grapples, portals) extend `ProjectileTool` and come with their own `ToolProjectile` subclass. Copy `BombThrower` and `Bomb`.
    - Everything else extends `Tool` directly, like this recipe.

---

## 1. Write the Tool Class

Create `Assets/Equipment/Tools/Scripts/Tools/ShockwaveShield.cs`:

```csharp
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Pushes every dynamic body near the player away from them. The player isn't moved.
/// </summary>
public class ShockwaveShield : Tool
{
    [SerializeField, Min(0f)] private float radius = 3f;
    [SerializeField] private float impulse = 15f;

    private readonly HashSet<Rigidbody2D> pushed = new HashSet<Rigidbody2D>();

    protected override void OnUse()
    {
        // This component sits on WeaponHolder, out at the player's hand, so center the
        // blast on the player's body instead of on this object.
        Rigidbody2D self = GetComponentInParent<Rigidbody2D>();
        Vector2 origin = self != null ? self.worldCenterOfMass : (Vector2)transform.position;
        pushed.Clear();

        foreach (Collider2D hit in Physics2D.OverlapCircleAll(origin, radius))
        {
            Rigidbody2D body = hit.attachedRigidbody;
            if (body == null || body == self || body.bodyType != RigidbodyType2D.Dynamic)
            {
                continue;
            }

            // A body with several colliders shows up once per collider.
            if (!pushed.Add(body))
            {
                continue;
            }

            Vector2 away = (body.worldCenterOfMass - origin).normalized;
            body.AddForce(away * impulse, ForceMode2D.Impulse);
        }
    }
}
```

What this relies on from `Tool`:

- **`Use()` runs `OnUse()` only when the cooldown is ready.** You don't check cooldowns yourself. The cooldown comes from the tool's `ToolData` asset.
- **`UseAlt()` is the second button.** It runs when the player holds ++e++ or the gamepad's north button for 0.4 s, because the input action uses a Hold interaction. Override it if your tool has an alternate action, like detonating a remote bomb. Unlike `Use()`, it has no cooldown.

## 2. Make the Tool's Data

1. In `Assets/Equipment/Tools/Scriptable Objects/Tools/`, right-click and choose **Create > Scriptable Objects > ToolData**. Name it `ShockwaveShieldData`.
2. In the Inspector, set **Cooldown** (in seconds) and **Tool Name**.

## 3. Put It on the Player

1. Open `Assets/Player/Player.prefab` and select `WeaponHolder`. It already has `PrimaryGun`, `BombThrower`, and `ToolUser`.
2. Add your `ShockwaveShield` component and drag `ShockwaveShieldData` into its **Data** field.
3. In `ToolUser`, set **Secondary Tool** to your new component. `ToolUser` only uses that one tool, so `BombThrower` can stay on the object.

## 4. Try It

Press **Play** in MasterScene and right-click next to one of the test asteroids. Do it in the first few seconds, because the test asteroids destroy themselves about 7 seconds in, or as soon as they touch anything.

Before committing, decide whether your tool replaces the Bomb Thrower as the default. If it doesn't, set `Secondary Tool` back to `BombThrower` and keep your component on the prefab so it's ready for the loadout menu. At v0.1.0 the menu [can't switch tools yet](../systems/loadout.md#known-issues).

---

## Checklist

- [ ] Tuning numbers are serialized fields or live in a data asset, not hard-coded. If designers will tune the tool a lot, move them into a `ToolData` subclass, the way `BombData` extends `ToolProjectileData`.
- [ ] The tool plays a sound, or there's a request in to the audio team. See [Add a Sound Effect](add-a-sound.md).
- [ ] New `.cs` and `.asset` files are committed with their `.meta` files.
