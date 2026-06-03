---
title: Style Guide
---

# Style Guide

**Voice:** Write in second person ("you"), active voice, and keep it concise. This is a club wiki, not a corporate manual — be direct and approachable.

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

**Links:** Use descriptive text — `[Contributing Guide](index.md)` not `[click here](index.md)`. Use relative paths for internal links.

---

**Admonitions:**

```markdown
!!! tip       — helpful but optional
!!! info      — neutral info
!!! warning   — must-know before proceeding
!!! danger    — serious, destructive
!!! example   — worked example
??? note      — collapsible
```

Don't overuse them — if every paragraph has one, none stand out.

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
