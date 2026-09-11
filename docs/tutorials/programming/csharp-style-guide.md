---
title: "C# Style Guide"
description: "How we write C# in SIGGD's Unity projects: naming, formatting, comments, and the everyday habits that keep a shared codebase readable."
tags:
  - programming
  - unity
  - reference
---

# C# Style Guide

!!! abstract "What's in here"
    - How to read the rules (DO, CONSIDER, AVOID, DO NOT)
    - **Part 1, Style:** naming, files and namespaces, formatting, organization, comments
    - **Part 2, Practices:** access and properties, values, events, Unity attributes
    - The `.editorconfig` in the game repo that checks some of this for you

---

## Why Have a Style Guide?

Code gets read way more often than it gets written. When a lot of people share one codebase, every file that looks a little different gets very annoying over the course of the year. Thus, this year we have a rudimentary style guide.

This isn't a grading rubric, either. Most of it is standard C# convention (the same rules Microsoft and Unity publish), plus a few Unity-specific habits that save you from real bugs. Code is super subjective, so I have some general preferences and considerations here, but a lot of it is up to you.

If you do completely disagree with a rule here, please let me know, as I could be totally wrong or in the minority. This is an ever updating guide, so any and all feedback is appreciated!

!!! tip "Not covered here? Match the file you're in."
    If you hit a situation this guide doesn't mention, do whatever the surrounding code does. Consistency with the code around you beats your personal favorite.

---

## How to Read the Rules

Every rule starts with a label, borrowed from Microsoft's [Framework Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/names-of-type-members):

| Label | What it means |
|---|---|
| **DO** | The rule. Follow it unless you have a genuinely good reason, and say what that reason is in your PR. |
| **CONSIDER** | Usually the right call, but use your judgment. |
| **AVOID** | Usually the wrong call. There are rare exceptions. |
| **DO NOT** | Don't. |

In code review, a broken **DO** or **DO NOT** is a fair reason to request changes. **CONSIDER** and **AVOID** are judgment calls, so comments about them should usually start with `nit:` (see [What Makes a Good Review](../general/gitgood2.md#what-makes-a-good-review)).

Every rule also comes with a *why*. If a rule ever seems to be counterintuitive with what you're doing, read the why first. It usually tells you whether you've found a real exception or just an annoying case.

!!! info "Unity speaks C# 9"
    Unity 6.3 compiles **C# 9.0**, which is a few versions behind what Microsoft's docs show you today. If you copy modern C# into a Unity project, these won't compile:

    - File-scoped namespaces: `namespace Combat;`
    - Collection expressions: `int[] costs = [1, 2, 3];`
    - Raw string literals: `"""like this"""`
    - `init` setters and `required` members

    Records technically work, but don't use them for anything Unity serializes. When a snippet from the internet gives you a strange syntax error, this is the first thing to check. [Unity's C# compiler page](https://docs.unity3d.com/6000.3/Documentation/Manual/csharp-compiler.html) has the full list.

### The `.editorconfig`

The game repository has an `.editorconfig` file at its root. Most code editors pick it up automatically, and it:

- indents with four spaces and puts braces on their own lines whenever you format a file,
- flags naming mistakes on types, public members, parameters, and locals as warnings,
- nudges you toward the `var` rule below with subtle suggestions.

Unity itself ignores the file, so it can never break a build. If your editor doesn't support it, you just miss out on the hints. It also can't check everything: private field naming, comments, and most of Part 2 are up to you and your reviewer.

---

## Part 1: Style

### Naming

Naming conventions are pretty freeform across languages, but this is what we'll be using in C#:

| Thing | Style | Example |
|---|---|---|
| Classes, structs, enums, delegates | PascalCase | `PlayerHealth` |
| Interfaces | `I` + PascalCase | `IDamageable` |
| Methods, properties, events | PascalCase | `TakeDamage`, `MaxHealth`, `Died` |
| Public fields (rare, see Part 2) | PascalCase | `Damage` |
| Constants | PascalCase | `MaxLives` |
| Enum types and values | PascalCase | `EnemyState.Chasing` |
| `[SerializeField]` fields | camelCase | `moveSpeed` |
| Other private fields | `_camelCase` or `camelCase`, one per file | `_currentTarget` |
| Parameters and local variables | camelCase | `damageAmount` |

**DO** use PascalCase for types, methods, properties, events, and anything public.

**Why:** It's the .NET convention, and Unity's types and methods follow it too (`Transform`, `GetComponent`). Unity's *properties* are the famous exception (`transform.position`, `Time.deltaTime`), and that's just something you live with when calling Unity API. Don't copy it in your own code.

**DO** use camelCase for local variables and parameters.

**Why:** It's the other half of the same convention. PascalCase says "this belongs to a type", and camelCase says "this only exists inside this method/class."

**DO** start interface names with `I`.

```csharp
public interface IDamageable
{
    void TakeDamage(int amount);
}
```

**Why:** `IDamageable` tells you immediately that you're holding a contract, not a specific class. Every interface in .NET and Unity follows this, so breaking it confuses everyone.

**DO** use PascalCase for enum types and their values. Name the enum in the singular, unless it's a `[Flags]` enum, which gets a plural.

```csharp
public enum EnemyState
{
    Idle,
    Chasing,
    Attacking
}

[System.Flags]
public enum DamageTypes
{
    None = 0,
    Fire = 1,
    Ice = 2,
    Poison = 4
}
```

**Why:** A variable of type `EnemyState` holds exactly one state, so the name reads as one. A flags enum holds a *set* of values, so the plural reads correctly: "this attack deals these damage types."

**DO** name private fields either `_camelCase` or `camelCase`, and pick one per file.

```csharp
private Transform _currentTarget;
private int _comboCount;
```

**Why:** Both styles are fairly common. Microsoft uses the underscore, and a lot of Unity code doesn't. The underscore makes fields easy to tell apart from locals and parameters (and typing `_` pulls up every field in autocomplete), while plain camelCase is less noisy. I personally try to use _camelCase when I can, but just be consistent.

**DO** name `[SerializeField]` fields in camelCase, with no prefix.

```csharp
[SerializeField] private float moveSpeed = 5f;
[SerializeField] private GameObject projectilePrefab;
```

**Why:** Serialized fields are a different kind of thing from internal state. They're data that lives in scenes and prefabs, and designers see them in the Inspector (Unity displays `moveSpeed` as "Move Speed"). Keeping them unprefixed marks them apart from the `_` fields in files that use underscores. It's also just kinda convention among Unity devs. Just remember that renaming a serialized field loses its saved values unless you follow the [`FormerlySerializedAs` rule](#unity-attributes).

**DO** use PascalCase for constants. **DO NOT** use SCREAMING_CASE.

```csharp
// Yes
private const int MaxLives = 3;

// No
private const int MAX_LIVES = 3;
```

**Why:** Ask Microsoft.

**DO** name Booleans so they read as a yes/no question, phrased positively: `isGrounded`, `hasKey`, `CanDash`.

**Why:** The `is`/`has`/`can` prefix tells you it's a bool without checking the type, and `if (canDash)` reads like English. Positive phrasing matters too: `if (!isNotDead)` is a double negative that can get confusing.

**CONSIDER** naming methods with verbs, and naming bool-returning methods as questions.

```csharp
public void SpawnEnemy() { ... }
public bool TryGetTarget(out Transform target) { ... }
public bool CanAfford(Item item) { ... }
```

**Why:** Methods *do* things, so a verb tells you what happens when you call one. A bool method named as a question makes the call site read naturally: `if (CanAfford(item))`.

**DO** name events one of these two ways, and stick to one within a system.

=== "Verb phrase"

    The Microsoft and Unity convention. The event is named after what happened, and `On` is saved for the method that raises it. Use the present tense for "about to happen" and the past tense for "just happened".

    ```csharp
    public event Action DoorOpening;
    public event Action DoorOpened;

    private void OnDoorOpened()
    {
        DoorOpened?.Invoke();
    }
    ```

=== "OnEventName"

    Very common in Unity community code. The event itself carries the `On`.

    ```csharp
    public event Action OnDoorOpened;
    ```

**Why:** Both styles are everywhere and both are readable. Once again, just stay consistent.

---

### Files and Namespaces

**DO** put each MonoBehaviour and ScriptableObject in its own file, named exactly like the class. **CONSIDER** doing the same for everything else.

**Why:** For MonoBehaviours and ScriptableObjects this isn't a style choice. Unity matches scripts to classes by file name, so if `PlayerHealth.cs` contains `class PlayerHP`, Unity won't let you add it to a GameObject. For plain C# classes it's just the fastest way to find things. A tiny helper that only one class uses (a small struct, say) can share that class's file.

**CONSIDER** using namespaces to group the scripts that make up a system, as you need them.

```csharp
namespace Combat
{
    public class DamageCalculator
    {
        // ...
    }
}
```

**Why:** Namespaces stop two systems' `Controller` classes from colliding, and they make it obvious which system a script belongs to. Use the block form shown above, since Unity's C# 9 doesn't support `namespace Combat;`.

---

### Formatting

**DO** put braces on their own lines (Allman style).

```csharp
if (isGrounded)
{
    Jump();
}
else
{
    ApplyGravity();
}
```

**Why:** It's the C# default. Microsoft's conventions, Unity's script templates, and the formatter in basically every C# editor all do it this way. The `.editorconfig` makes formatting produce this for you.

**DO** indent with four spaces, not tabs.

**Why:** Tabs show up at different widths in different editors and on GitHub, so four spaces is the C# standard, and the `.editorconfig` sets it automatically.

**DO** use `var` only when the type is obvious from the right-hand side.

```csharp
// Obvious: it's a new List<Enemy>.
var enemies = new List<Enemy>();

// Not obvious from the call, so write the type out.
float damage = CalculateDamage(target);
```

**Why:** On GitHub there's no hover tooltip, so a reviewer reading `var damage = CalculateDamage(target);` has to go find the method to learn whether that's an `int` or a `float`.

**CONSIDER** wrapping lines that run past about 120 characters.

**Why:** Long lines disappear off the side of split editors and GitHub's side-by-side diff. 120 is roomy enough that you'll rarely hit it unless a line is doing too much anyway.

---

### Organization

**CONSIDER** ordering class members the same way in every file. If you don't have a preference, use Unity's:

1. Fields
2. Properties
3. Events
4. MonoBehaviour methods (`Awake`, `Start`, `Update`, and so on)
5. Public methods
6. Private methods
7. Nested types

**Why:** When every file is laid out the same way, you know where to look before you open it.

**CONSIDER** regions when writing your own class. They're optional, and there are no required names.

**Why:** Some people like folding a big class into labeled chunks. Others, including Unity's own style guide, discourage regions because they can hide how complex a class has gotten. If you *need* regions to find your way around, the class is probably doing too much.

**CONSIDER** breaking long methods into well-named private helper methods. **AVOID** using partial classes to split up a big class.

```csharp
private void HandleHit(Hit hit)
{
    ApplyDamage(hit);
    ApplyKnockback(hit);
    PlayHitEffects(hit);
}
```

**Why:** A method called `ApplyKnockback()` explains a block of code better than a comment above it, and it's reusable. Partial classes do the opposite: they spread one class across several files, so it *looks* smaller than it is while you still have to open all of them to understand it. If a class is too big for one file, it's probably more than one class.

---

### Comments and Documentation

**DO** write XML doc comments for every type and every public member. Trivial members (an obvious getter, a one-line method that just forwards to another) can skip it. Either `///` or `/** */` works, as long as you pick one per file.

=== "/// style"

    ```csharp
    /// <summary>
    /// Tracks an actor's health and raises Died when it reaches zero.
    /// </summary>
    public class Health : MonoBehaviour
    ```

=== "/** */ style"

    ```csharp
    /** <summary>
     * Tracks an actor's health and raises Died when it reaches zero.
     * </summary>
     */
    public class Health : MonoBehaviour
    ```

**Why:** Doc comments show up in your editor's tooltips everywhere the type or method is used, so the next person learns what `Health` does without opening `Health.cs`. Both syntaxes are valid. Microsoft's templates use `///`, and I personally write `/** */`, but it doesn't matter as long as a file doesn't mix them.

**DO** keep method docs short: one sentence on what it does, plus `<param>`, `<returns>`, or `<exception>` only where the name and signature don't already make them obvious. Write what a caller needs to know, not how the method works inside.

```csharp
/// <summary>Applies damage after armor and returns the amount actually dealt.</summary>
/// <param name="amount">Raw damage before armor.</param>
public int TakeDamage(int amount)
```

**Why:** A doc comment that narrates the implementation goes stale the first time someone changes the implementation. What the caller sees (what goes in, what comes out, what can go wrong) changes far less often.

**CONSIDER** keeping class summaries to one or two sentences about what the class is and its job.

**Why:** The summary is the first thing anyone reads. Design history, rejected alternatives, and every edge case the class handles all belong somewhere else, like the PR description or the system's page in the docs (the [System Template](../../contributing/templates/system-template.md) exists for exactly that).

**CONSIDER** a one-line doc comment on `Dictionary` fields saying what the key and value mean.

```csharp
/// <summary>Keyed by enemy ID, resolving to that enemy's current aggro target.</summary>
private Dictionary<int, Transform> _aggroTargets;
```

**Why:** `Dictionary<int, Transform>` tells you the types, but not what they *mean*. Is that `int` an enemy ID? A player index? A wave number? Who knows! Other collections can get the same treatment when their contents aren't obvious from the name.

**DO** add a `[Tooltip]` to any serialized field whose purpose or units aren't obvious from its name. **DO NOT** also put a doc comment on top of it.

```csharp
[Tooltip("Seconds of invulnerability after taking a hit.")]
[SerializeField] private float invulnerabilityDuration = 0.5f;
```

**Why:** A tooltip shows up for designers hovering over the field in the Inspector *and* for programmers reading the code, so it does the doc comment's job twice. (Unity's own style guide recommends exactly this.) Units are the big one: is `duration` in seconds or frames? Definitely note things like this down.

**CONSIDER** pulling a confusing block into a well-named method before you reach for a comment. When you do write an inline comment, **DO NOT** restate what the code does. Explain *why* it does it.

```csharp
// Bad: says exactly what the code already says.
// Wait for the next fixed update.
yield return new WaitForFixedUpdate();

// Good: says the thing the code can't.
// The spawned collider doesn't exist until the next physics step,
// so raycasting before this would miss it.
yield return new WaitForFixedUpdate();
```

**Why:** Code already tells you *what* happens. Comments are for everything it can't say: why this approach, what constraint forced it, which weird bug it dodges. A comment that restates the code is one more thing to keep in sync for zero new information.

**CONSIDER** Microsoft's comment formatting: comments on their own line (not at the end of a line of code), starting with a capital letter, ending with a period, with a space after `//`.

**Why:** It's the most common C# convention, and end-of-line comments get cut off in narrow editors and diffs.

---

## Part 2: Practices

### Access and Properties

**DO** make everything `private` unless something outside the class actually needs it.

**Why:** Everything public is a promise. Once another script calls a public method, you can't change or remove it without checking every caller. Private members can change freely, so you want as much of your class as possible on that side of the line.

**AVOID** public fields. Expose Inspector values with `[SerializeField] private`, and give other scripts a property if they need to read the value.

```csharp
[SerializeField] private int maxHealth = 100;

public int MaxHealth => maxHealth;
```
or
```csharp
[field: SerializeField] public int maxHealth { get; private set; } = 100;
```

**Why:** A public field can be overwritten by any script, at any time, with no way to validate the new value or even notice it happened. `[SerializeField] private` gets you the Inspector without handing the entire codebase write access. The usual exception is a small plain-data struct that's just a bundle of values.

**DO** use auto-properties for state a class exposes, instead of a private field plus a property that just returns it.

```csharp
// Instead of this:
private int _score;
public int Score => _score;

// Write this:
public int Score { get; private set; }
```

Use `{ get; private set; }` when outside code should read the value but not change it, and `{ get; set; }` only when outside code is *meant* to change it. A separate field is still the right call when the property does different things (clamping, validation, raising an event when it changes), or when the value needs to be serialized, like `maxHealth` above.

**Why:** The two-line version is the same thing with twice the code and two names to keep in sync. The auto-property also puts the access rules right in the declaration, so `private set` tells you "only this class changes this" immmediately.

**CONSIDER** `[field: SerializeField]` when you want an auto-property to show up in the Inspector.

```csharp
[field: SerializeField, Tooltip("Top speed in units per second.")]
public float MaxSpeed { get; private set; } = 8f;
```

!!! warning "Renaming it quietly wipes saved values"
    Unity doesn't save the property. It saves the hidden field the compiler generates behind it, named `<MaxSpeed>k__BackingField`. Rename the property and every value set in the Inspector silently resets to the default, unless you add `[field: FormerlySerializedAs("<MaxSpeed>k__BackingField")]` with the *old* name. With a plain `[SerializeField]` field, the same fix is just `[FormerlySerializedAs("oldName")]`, which is a lot easier to remember.

**Why:** One declaration instead of a field plus a property is just simpler.

---

### Values

**DO** give meaningful numbers and strings a name: a `const` if it never changes, or a serialized field if a designer should be able to tune it.

```csharp
// What's 3.5? What's 0.2? Nobody knows.
if (distanceToPlayer < 3.5f)
{
    StartCoroutine(Lunge(0.2f));
}

// Now it explains itself, and a designer can tune it without touching code.
[Tooltip("How close the player must be before this enemy lunges, in units.")]
[SerializeField] private float lungeRange = 3.5f;

[Tooltip("How long the lunge wind-up lasts, in seconds.")]
[SerializeField] private float lungeWindUp = 0.2f;
```

`0`, `1`, `-1`, and obvious math (like `* 0.5f` to halve something) are fine as they are.

**Why:**  `3.5f` doesn't say what it is, and once it's been copied into three places, changing it means you have to find all three. If you want to take this further and move tuning data out of scripts entirely, that's what [Data-Driven Design](data-driven-design.md) is about.

**AVOID** scattering string lookups for tags, scene names, layers, and animator parameters through your code.

```csharp
// Rename the scene and this only fails when the line actually runs.
SceneManager.LoadScene("Level_02");

// One place to change, and a typo in SceneNames.LevelTwo is a compile error.
public static class SceneNames
{
    public const string LevelTwo = "Level_02";
}

SceneManager.LoadScene(SceneNames.LevelTwo);
```

A few more habits in the same spirit:

- Keep tag names in one static class too, and check them with `CompareTag(Tags.Enemy)`.
- Turn animator parameter names into IDs once, in a `static readonly int` holding `Animator.StringToHash("Speed")`, instead of passing the string every frame. This one is also important as hashing a string can get expensive.
- When you can drag a reference into a serialized field instead of looking something up by name, do that.

**Why:** The compiler checks the names of your classes and variables, but it has no idea what's inside a string. If there's ever a typo, keeping the strings in one place means one fix instead of a project-wide search.

---

### Events

**DO** pick one way to raise events and stick to it within a class: either invoke with `?.`, or give the event an empty default so it's never null.

=== "?.Invoke()"

    ```csharp
    public event Action Died;

    private void Die()
    {
        Died?.Invoke();
    }
    ```

=== "delegate { }"

    ```csharp
    public event Action Died = delegate { };

    private void Die()
    {
        Died.Invoke();
    }
    ```

**Why:** An event with no subscribers is `null`, and invoking `null` throws, which both patterns handle. Mixing them is the problem: in a class that relies on `?.`, a bare `Died.Invoke()` throws the first time nobody's listening, and you can only tell which kind of class you're in by checking the declaration. (`?.` is perfectly safe on events and other plain C# objects. Unity objects are a different story, which the [C# for Unity primer](csharp-for-unity.md#null-and-unitys-weird-null) explains.)

---

### Unity Attributes

**DO** add `[FormerlySerializedAs]` when you rename a serialized field.

```csharp
using UnityEngine.Serialization;

// ...

[FormerlySerializedAs("speed")]
[SerializeField] private float moveSpeed = 5f;
```

**Why:** Unity saves Inspector values by field name. Rename `speed` to `moveSpeed` and every scene and prefab that set a value quietly falls back to the default, with no error or warning. The attribute tells Unity to also look for the old name when loading.

**CONSIDER** `[DisallowMultipleComponent]` on components that would break if a GameObject had two of them.

```csharp
[DisallowMultipleComponent]
public class PlayerMovement : MonoBehaviour
```

**Why:** Two `PlayerMovement` components on one player means two scripts fighting over the same velocity. The attribute makes Unity refuse to add a second one in the first place, which is just a nice sanity check.

**AVOID** `[DefaultExecutionOrder]` unless you really need to force one script to run before another, and when you do use it, leave a comment saying why.

```csharp
// Must run before any gameplay script reads input this frame.
[DefaultExecutionOrder(-100)]
public class InputReader : MonoBehaviour
```

**Why:** It's a global lever. It reorders your script relative to *every* other script in the project, and nobody reading those other scripts will know it's there. Most ordering problems have a simpler fix: set yourself up in `Awake` and talk to other objects in `Start` (see [How Unity Thinks](how-unity-thinks.md#the-lifecycle)), or have one script call the others explicitly.

**DO** wrap anything that uses the `UnityEditor` namespace in `#if UNITY_EDITOR` (or keep it in a folder named `Editor`). **CONSIDER** wrapping gizmo and debug-only code too.

```csharp
#if UNITY_EDITOR
using UnityEditor;
#endif

public class PatrolPoint : MonoBehaviour
{
#if UNITY_EDITOR
    private void OnDrawGizmosSelected()
    {
        Handles.Label(transform.position, name);
    }
#endif
}
```

**Why:** `UnityEditor` only exists inside the editor. Code that uses it works perfectly while you're testing, then breaks the build, and the game repo builds every pull request automatically (see [What Happens Automatically](../general/gitgood2.md#what-happens-automatically)). Plain gizmo code does compile in builds, so guarding it is just tidiness.

---

## Before You Open a PR

A quick pass over the DO and DO NOT rules:

- [ ] Names follow the [naming table](#naming): PascalCase for types and public members, camelCase for serialized fields, locals, and parameters, one private-field style per file, `I` on interfaces, no SCREAMING_CASE.
- [ ] MonoBehaviours and ScriptableObjects are in files named after the class.
- [ ] Every type and public member has a doc comment, except the truly trivial ones.
- [ ] Non-obvious serialized fields have a `[Tooltip]` (and no doc comment on top of it).
- [ ] No public fields sneaking in where `[SerializeField] private` would do.
- [ ] Meaningful numbers and strings have names.
- [ ] Renamed serialized fields have `[FormerlySerializedAs]`.
- [ ] Anything touching `UnityEditor` is inside `#if UNITY_EDITOR` or an `Editor` folder.
- [ ] You ran your editor's formatter, so braces and indentation match the `.editorconfig`.

---

## What's Deliberately Not Here

This guide is about how code *looks* and the everyday habits around it. It doesn't cover how to structure systems, when to use ScriptableObjects, or how scripts should interface with each other. That's a system design issue rather than a style rule, so take a look at the [onboarding workshops](index.md).

---

## Further Reading

- [C# identifier naming rules and conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names): Microsoft's naming rules, which most of Part 1 follows.
- [.NET coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions): Microsoft's formatting, `var`, and comment conventions.
- [Framework Design Guidelines: Names of Type Members](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/names-of-type-members): where the DO/CONSIDER/AVOID labels and the event naming rules come from.
- [Unity's C# style guide (Unity 6 edition)](https://unity.com/resources/c-sharp-style-guide-unity-6): Unity's free e-book on the same topic, with its own choices where they differ from Microsoft's.
- [Unity: naming and code style tips](https://unity.com/how-to/naming-and-code-style-tips-c-scripting-unity): the short web version of that e-book.
- [Google's code review standard](https://google.github.io/eng-practices/review/reviewer/standard.html): the "style guide is the absolute authority" quote, plus a great read on reviewing in general.
- [Unity script serialization rules](https://docs.unity3d.com/6000.3/Documentation/Manual/script-serialization-rules.html): exactly which fields and properties Unity saves.
