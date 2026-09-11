---
title: Style Guide
---

# Style Guide

!!! info "Looking for how to write code?"
    This page is about writing *docs*. For how we write C# in the game, see the
    [C# Style Guide](../tutorials/programming/csharp-style-guide.md).

**Voice:** Write in second person ("you") or imperative, active voice, and keep it concise. This is a club wiki, so feel free to be casual! Contractions and the occasional "I" are totally fine.

---

**Frontmatter:** Every page needs at minimum a `title`. Add `author: "@username"` only when committing someone else's work.

```yaml
---
title: "Page Title"
tags:
  - relevant-tag
---
```

```yaml
---
title: "Page Title"
author: "@github-username"   # committing someone else's work
---
```

For tutorials, also add `difficulty`, `time_estimate`, and `prerequisites`.

---

**Code blocks:** Always specify the language identifier.

````markdown
```csharp
// C# code
```
```gdscript
# GDScript
```
```bash
# shell
```
````

Use inline code for file paths (`Assets/Scripts/`), variable names (`playerHealth`), and menu items (`File > Save`).

---

**Links:** Use descriptive text: `[Contributing Guide](index.md)` not `[click here](index.md)`. Use relative paths for internal links.

---

**Admonitions:**

```markdown
!!! tip         helpful but optional
!!! info        neutral info
!!! warning     must-know before proceeding
!!! danger      serious, destructive
!!! example     worked example
!!! question    an exercise prompt
??? note        collapsible
```

Don't overuse them, as if every paragraph has one, none stand out.

**Exercises:** The programming onboarding guides use a consistent set of blocks for exercises. If you're writing a guide with exercises, reuse them so readers know what to expect:

| Block | Use it for |
|---|---|
| `!!! question "Predict: ..."` | Code or a scenario the reader predicts the outcome of before checking |
| `??? success "Check your prediction"` | Right after a Predict: what happens, and *why* |
| `!!! example "Make: ..."` | A design or build exercise. Never include the answer. |
| `??? tip "Hint 1"`, `"Hint 2"`, `"Hint 3"` | After a Make: a nudge question, then the concept with a docs link, then an approach in words (a little code is OK) |
| `??? note "What a good answer includes"` | After the hints: criteria readers can check their own answer against, not a solution |
| `??? info "New to this? ..."` | Background that experienced readers can skip |
| `!!! example "This week's game idea"` | One per onboarding guide. The only block that gets edited for a specific meeting. |

---

**Images:** Store in `docs/assets/images/`. Always include alt text. Add an italic caption below.

```markdown
![Description of image](../../assets/images/example.png)
*Caption here.*
```

---

**Tags:** Lowercase, hyphen-separated. Reuse existing tags before adding new ones.

`programming` · `art` · `game-design` · `audio` · `general` · `unity` · `godot` · `unreal` · `pixel-art` · `3d` · `animation` · `ui` · `tools` · `assets` · `project` · `game-jam` · `tutorial` · `reference` · `setup` · `beginner` · `intermediate` · `advanced`

---

**Difficulty ratings (tutorials):**

| Value | Meaning |
|-------|---------|
| `beginner` | No prior knowledge needed |
| `intermediate` | Comfortable with basics |
| `advanced` | Significant experience expected |
