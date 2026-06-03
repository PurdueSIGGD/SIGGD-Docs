---
title: "ScriptTemplate.cs"
description: "One sentence describing what this script does."
tags:
  - project
  - reference
  - programming
# author: "@github-username"  # only if committing someone else's work
---

# ScriptName.cs

**Path:** `Assets/Scripts/Path/ScriptName.cs`  
**Type:** `MonoBehaviour` / `ScriptableObject` / `static class` / etc.  
**Namespace:** YourNamespace (or "None")

One sentence summary of this script's responsibility. Be specific.

---

## Class Summary

Describe the class's role in the broader codebase: what it owns, what
it responds to, and what other scripts depend on it.

---

## Fields & Properties

### Public Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `publicField` | `float` | `1.0` | What this controls |
| `aReference` | `GameObject` | — | What this reference is for |

### Public Properties

| Property | Type | Get/Set | Description |
|----------|------|---------|-------------|
| `IsActive` | `bool` | Get | Returns true when the script is in its active state |
| `CurrentValue` | `float` | Get/Set | The current value with clamping applied on set |

### Serialized Private Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `_speed` | `float` | `5.0` | Internal movement speed |

---

## Methods

### Public Methods

#### `void MethodName(ParameterType param)`

What this method does.

**Parameters:**
- `param` — What this parameter means.

```csharp
scriptInstance.MethodName(someValue);
```

---

#### `ReturnType AnotherMethod()`

What this method does and what it returns.

**Returns:** What the return value represents.

```csharp
var result = scriptInstance.AnotherMethod();
```

---

### Unity Lifecycle Methods

| Method | Usage |
|--------|-------|
| `Awake` | Component references resolved here |
| `Start` | Initial state set, events subscribed |
| `Update` | [Describe what runs every frame, or "Not used"] |
| `FixedUpdate` | [Physics updates, or "Not used"] |
| `OnDestroy` | Event unsubscription |

---

## Events

| Event | Type | When fired |
|-------|------|-----------|
| `OnValueChanged` | `UnityEvent<float>` | When the primary value changes |

---

## Usage Examples

### Common Use Case

```csharp
// How another script typically interacts with this one
var script = GetComponent<ScriptName>();
script.MethodName(value);
script.OnValueChanged.AddListener(HandleValueChange);
```

---

## Called By / Calls Into

| Direction | Script | Why |
|-----------|--------|-----|
| Called by | `GameManager.cs` | Initializes this script on scene load |
| Called by | `UIController.cs` | Reads `CurrentValue` to update the display |
| Calls into | `AudioManager.cs` | Triggers sound effects on state changes |
