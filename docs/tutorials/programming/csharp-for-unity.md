---
title: "C# for Unity"
description: "A quick C# primer for people who already know Java, Python, or C++: the language features Unity code leans on, and the Unity-specific surprises."
tags:
  - programming
  - unity
  - reference
difficulty: beginner   # beginner | intermediate | advanced
time_estimate: "30 minutes (or look things up as you need them)"
prerequisites:
  - "Some experience in another programming language"
status: published   # draft | review | published
# author: "@github-username"  # only if committing someone else's work
---

# C# for Unity

!!! abstract "What's in here"
    - The C# features Unity code uses constantly, with comparisons to Java, Python, and C++
    - The Unity-specific surprises: its strange version of `null`, serialization limits, and coroutines
    - What Unity's C# version can't do yet

---

## How to Use This Page

This is NOT a from-scratch C# course. It's for people who can already program in *something* and want to read and write Unity code without getting ambushed by the differences. Thus, I recommend skimming the headings, reading what's new to you, and coming back when a snippet in another guide (or someone else's code) uses something you haven't seen.

Where it helps, sections have tabs comparing C# to Java, Python, and C++ as well.

!!! info "Unity uses C# 9"
    Microsoft's docs often show newer C# than Unity supports. If a snippet gives you a strange syntax error, check the [C# 9 note in the style guide](csharp-style-guide.md#how-to-read-the-rules) first.

---

## Value Types and Reference Types

C# has two kinds of types:

- **Classes are reference types.** A variable holds a *reference* to an object. Assign it to another variable and both point at the same object.
- **Structs are value types.** A variable holds the *value itself*. Assign it and you get a copy.

Unity's math types are structs: `Vector3`, `Quaternion`, `Color`. Thus, you can't do this:

```csharp
// Error CS1612: Cannot modify the return value of 'Transform.position'
// because it is not a variable.
transform.position.x = 5f;
```

`transform.position` is a property that hands you a *copy* of the position. Changing `.x` on that copy would do nothing, so the compiler stops you. The fix is to copy, change, and assign back:

```csharp
Vector3 position = transform.position;
position.x = 5f;
transform.position = position;
```

=== "Coming from Java"

    Java has no user-defined value types. Everything except the primitives is a reference. In C#, a `struct` behaves like a primitive: copied on assignment, compared by value, and never `null` (unless you make it nullable, below).

=== "Coming from Python"

    In Python, every variable is a reference, so `b = a` never copies anything. C# structs don't do this; `Vector3 b = a;` makes an independent copy, and changing `b` leaves `a` alone.

=== "Coming from C++"

    Note that in C++, `struct` and `class` only differ in default access. In C#, they're totally different: `struct` is a value type (copied, usually on the stack or inline), and `class` is a reference type (always on the heap, garbage collected). There's no choosing per-variable like `T` versus `T*`.

---

## Properties

A property looks like a field from the outside, but runs code when you read or write it.

```csharp
public class Health : MonoBehaviour
{
    // Auto-property: anyone can read it, only this class can set it.
    public int Current { get; private set; }

    // Computed property: no storage, calculated every time.
    public bool IsDead => Current <= 0;
}
```

The [style guide](csharp-style-guide.md#access-and-properties) has the conventions I recommend for them.

=== "Coming from Java"

    Properties replace `getX()`/`setX()` pairs. `health.Current` reads like a field but calls the getter, and `{ get; private set; }` is a public getter with a private setter in one line.

=== "Coming from Python"

    Same idea as `@property`, with the getter and setter declared together, and an auto-property generates the storage for you.

=== "Coming from C++"

    There's no direct equivalent. Think of a pair of inline accessor methods with field syntax at the call site. Note that properties can't be passed by `ref`, which is part of why the `transform.position.x` error above exists.

---

## Access Modifiers

| Modifier | Who can see it |
|---|---|
| `public` | Everyone |
| `private` | Only this class. The default for class members if you don't write anything. |
| `protected` | This class and classes that inherit from it |
| `internal` | Anything in the same assembly (for us, usually the whole game, this isn't super relevant) |

Best practice is to [default to private](csharp-style-guide.md#access-and-properties) and open things up only when something outside actually needs them.

---

## Namespaces and `using`

Namespaces group related types and stop names from colliding. `using` at the top of a file lets you skip the namespace prefix.

```csharp
using System.Collections.Generic;
using UnityEngine;

namespace Combat
{
    public class DamageCalculator
    {
        // ...
    }
}
```

Unity's C# 9 only supports the block form above, not the newer `namespace Combat;` one-liner.

=== "Coming from Java"

    Namespaces are like packages, and `using` is like `import`, except that C# namespaces don't have to match your folder structure.

=== "Coming from Python"

    `using` is roughly `from module import *`, scoped to one file. There's no per-name import; you get the whole namespace.

=== "Coming from C++"

    Namespaces work almost exactly like C++ namespaces, and `using UnityEngine;` is like `using namespace` (but it's normal and fine here, not a code smell).

---

## Delegates, `Action`, `Func`, and Lambdas

A **delegate** is a variable that holds a method. You'll mostly use the two built-in delegate types:

- `Action`, `Action<T>`, `Action<T1, T2>`: a method that returns nothing and takes the specified types (T) as parameters
- `Func<TResult>`, `Func<T, TResult>`: a method that returns something (the *last* type is the return type)

```csharp
Action onLanded = () => Debug.Log("Landed!");
Func<int, int> doubleIt = x => x * 2;

onLanded();
int result = doubleIt(21);
```

The `=>` syntax is a **lambda**: a small inline function.

=== "Coming from Java"

    Like functional interfaces (`Runnable`, `Function<T, R>`) and Java lambdas, but you don't need an interface: `Action` and `Func` cover almost everything.

=== "Coming from Python"

    Functions are first-class in Python, and delegates are how C# does the same thing with types attached. Lambdas can have full bodies with braces, unlike Python's one-expression `lambda`.

=== "Coming from C++"

    Like `std::function` combined with lambdas, with automatic capture by reference of local variables (be careful with that inside loops).

---

## Events

An **event** is a delegate with a lock on it: outside code can only subscribe (`+=`) and unsubscribe (`-=`), and only the class that owns the event can raise it.

```csharp
public class Boss : MonoBehaviour
{
    public event Action Defeated;

    private void Die()
    {
        Defeated?.Invoke();
    }
}

// Somewhere else:
boss.Defeated += OpenExitDoor;
boss.Defeated -= OpenExitDoor;
```

Every `+=` needs a matching `-=`, usually in `OnEnable` and `OnDisable`. [The OOP Toolkit](oop-toolkit.md#events-who-needs-to-know) explains in more detail why that's important.

---

## Generics

Generics let one class or method work with any type, while keeping full type checking.

```csharp
List<Enemy> enemies = new List<Enemy>();
Dictionary<string, int> scores = new Dictionary<string, int>();

T GetOrAdd<T>(GameObject target) where T : Component
{
    if (!target.TryGetComponent(out T component))
    {
        component = target.AddComponent<T>();
    }

    return component;
}
```

`where T : Component` is a **constraint**: it promises the compiler that `T` will be some kind of component, which is what makes calling `AddComponent<T>()` legal.

=== "Coming from Java"

    Similar syntax, but C# generics aren't erased: `List<int>` really stores `int`s (no boxing), and you can use `typeof(T)` at runtime. Look up reification for more info!

=== "Coming from Python"

    Like type hints (`list[Enemy]`), except the compiler actually enforces them.

=== "Coming from C++"

    Like templates, but checked once when you write the generic code (using constraints) instead of per instantiation. Much friendlier error messages, and less power than templates.

---

## Attributes

The things in square brackets are **attributes**: metadata attached to code, which tools (like Unity) read.

```csharp
[Tooltip("Seconds between shots.")]
[SerializeField] private float fireRate = 2f;
```

`[SerializeField]`, `[Tooltip]`, `[Header]`, and `[CreateAssetMenu]` are the ones you'll see most. They don't change what your code does when it runs; they change how Unity treats it.

=== "Coming from Java"

    Exactly like annotations (`@Override`, `@Deprecated`).

=== "Coming from Python"

    They look a bit like decorators, but they never wrap or change the function. They're just labels something else reads.

=== "Coming from C++"

    Similar in spirit to `[[nodiscard]]`-style attributes, but far more common, and readable at runtime through reflection.

---

## Interfaces and Abstract Classes

Both describe what something can do.

```csharp
public interface IDamageable
{
    void TakeDamage(int amount);
}

public abstract class Weapon : MonoBehaviour
{
    [SerializeField] protected int damage = 10;

    public abstract void Fire();

    public virtual void Reload() { }

    protected void PlayFireSound()
    {
        // Shared code every weapon gets for free.
    }
}
```

- An **interface** is a pure contract: method signatures, no fields (you can provide default implementations, however). A class can implement as many as it wants.
- An **abstract class** can also share real code and fields, but a class can only inherit from one. Virtual fields can also provide a default body.

So interfaces are for "can do X" (damageable, interactable, flammable), and abstract classes are for "is a kind of X that shares the same interior." [The OOP Toolkit](oop-toolkit.md#interfaces-as-contracts) covers when to use each.

---

## Null (and Unity's Weird Null)

Reference types can be `null`, and using a `null` reference throws a `NullReferenceException`, the single most common error in Unity. C# gives you some shortcuts for dealing with null:

```csharp
// Null-conditional: only calls Invoke if Died isn't null.
Died?.Invoke();

// Null-coalescing: use the right side if the left side is null.
string label = customName ?? "Unnamed";
```

**There's a catch in Unity.** When you `Destroy` a GameObject or component, the C# object doesn't actually disappear. Unity destroys the real object on its side, but your variable still points at a C# shell. To make that less confusing, Unity overrides `==` so that a destroyed object compares equal to `null`:

```csharp
Destroy(enemy);

// Later, on a following frame:
if (enemy == null)
{
    // true, even though the C# variable isn't technically null
}
```

The catch is that `?.` and `??` *can't* be overridden, so they skip Unity's check and see the shell as "not null." Read [Unity's docs](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Object.html) for more.

So for anything that's a Unity object (GameObjects, components, ScriptableObjects):

```csharp
// Works correctly with destroyed objects:
if (target != null)
{
    target.TakeDamage(10);
}

// Also works: Unity objects convert to false when destroyed or missing.
if (target)
{
    target.TakeDamage(10);
}

// Looks fine, but lets a destroyed target through:
target?.TakeDamage(10);
```

`?.` is still perfectly fine on plain C# things, like events, lists, and your own non-Unity classes.

??? info "Three flavors of 'it's null'"
    - **`NullReferenceException`:** a plain C# reference was `null` when you used it.
    - **`MissingReferenceException`:** you used a Unity object that's been destroyed. Usually a sign that something kept a reference to an object after it was gone (like an event that was never unsubscribed).
    - **`UnassignedReferenceException`:** a serialized field was left empty in the Inspector. The fix is usually dragging the right object into that field.

---

## Nullable Value Types

Value types like `int` can't normally be `null`. Add a `?` and they can:

```csharp
int? bestTime = null;

if (bestTime.HasValue)
{
    Debug.Log($"Best: {bestTime.Value}");
}

int shown = bestTime ?? 0;
```

Handy for "no value yet," like a best time before the first run.

---

## `var`

`var` lets the compiler figure out a variable's type from the right-hand side. It's still fully typed; you just didn't write the type. The [style guide rule](csharp-style-guide.md#formatting) is to use it only when the type is obvious from the right side, like `var enemies = new List<Enemy>();`.

---

## Strings

```csharp
// Interpolation: the easy way to build strings.
string message = $"{playerName} took {damage} damage";

// Verbatim strings: backslashes are literal.
string path = @"C:\Games\Save.json";
```

Strings are immutable; every change makes a new string. That's fine almost everywhere, but building a big string in a loop is faster with `System.Text.StringBuilder`.

---

## Collections

| Type | Use it for | Unity serializes it? |
|---|---|---|
| `T[]` (array) | Fixed-size lists | Yes |
| `List<T>` | Lists that grow and shrink | Yes |
| `Dictionary<TKey, TValue>` | Looking things up by key | **No** |
| `HashSet<T>` | "Is this in the set?" checks | No |

Note that `Dictionary` field won't show up in the Inspector, and Unity [doesn't save it](https://docs.unity3d.com/6000.3/Documentation/Manual/script-serialization-rules.html). A common workaround is a serialized `List` of key/value pairs that you turn into a dictionary in `Awake`. Alternatively, if you use Odin Inspector (which the SIGGD games will be using), you can serialize special types of dictionaries.

`foreach` loops over any of them:

```csharp
foreach (Enemy enemy in enemies)
{
    enemy.Alert();
}
```

Don't add or remove items from a collection while you're `foreach`-ing over it. That throws an exception. Loop over a copy, or collect the changes and apply them after.

??? info "A quick note on LINQ"
    `using System.Linq;` gives you methods like `Where`, `Select`, `OrderBy`, and `First` that make collection code short and readable. Most of them allocate memory as they go, though, so keep them out of code that runs every frame. These are super helpful though!

---

## Exceptions

When code throws an exception in Unity, the error shows up in the Console, the rest of that method call is skipped, and the game keeps running. Next frame, `Update` runs again like nothing happened. That's forgiving, but it also means you have to be more intentional. Ensure that your code doesn't throw unnecessary errors.

Only catch exceptions you can actually do something about. Wrapping code in a `try`/`catch` that swallows everything tends to hide bugs that could be fixed.

---

## Coroutines and Async

Games often need something to happen *over time*: wait two seconds, fade out, then respawn. There are two main ways to write that.

**Coroutines** are Unity's built-in way. A method returns `IEnumerator`, and `yield return` pauses it:

```csharp
private IEnumerator RespawnAfterDelay(float seconds)
{
    yield return new WaitForSeconds(seconds);
    Respawn();
}

// Start it:
StartCoroutine(RespawnAfterDelay(2f));
```

A coroutine belongs to the MonoBehaviour that started it. It stops if that GameObject is deactivated or the script is destroyed, but [*not*](https://docs.unity3d.com/6000.3/Documentation/Manual/Coroutines.html) if you just disable the script with `enabled = false`.

**`async`/`await`** is C#'s general version of the same idea. The game project uses a library called **UniTask**, which makes async code work nicely with Unity's frame loop. You'll see it in the real codebase, but coroutines are completely fine for most people. I personally prefer UniTask, but it can be complicated to learn!

---

## Next Steps

- [How Unity Thinks](how-unity-thinks.md): the Unity side of the mental model, if you haven't done it yet.
- [C# Style Guide](csharp-style-guide.md): how we write all of the above in the game.
- [The OOP Toolkit](oop-toolkit.md): putting interfaces, events, and generics to work.

---

## Further Reading

- [Microsoft's C# documentation](https://learn.microsoft.com/en-us/dotnet/csharp/): the official language reference (remember it shows newer versions than Unity's C# 9).
- [Unity Manual: Script serialization rules](https://docs.unity3d.com/6000.3/Documentation/Manual/script-serialization-rules.html): exactly what Unity can and can't save.
- [Unity Manual: Coroutines](https://docs.unity3d.com/6000.3/Documentation/Manual/Coroutines.html): everything about writing and stopping coroutines.
- [Unity Scripting API: Object](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Object.html): the official word on Unity's null behavior.
