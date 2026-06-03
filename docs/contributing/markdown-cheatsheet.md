---
title: Markdown Cheatsheet
---

# Markdown Cheatsheet

**Formatting**

```markdown
**bold**  *italic*  ~~strikethrough~~  `inline code`
[Link text](https://example.com)
[Internal link](../about/index.md)
```

---

**Lists**

```markdown
- Unordered item
    - Nested item

1. Ordered item

- [x] Checked task
- [ ] Unchecked task
```

---

**Code blocks** — always include a language identifier

````markdown
```csharp
public class Example : MonoBehaviour { }
```
````

Common identifiers: `csharp` `gdscript` `python` `bash` `yaml` `json` `markdown`

---

**Admonitions**

```markdown
!!! tip
    Helpful tip.

!!! info "Custom title"
    Neutral info.

!!! warning
    Be careful.

!!! danger
    Serious warning.

!!! example
    Worked example.

??? note "Collapsible"
    Click to expand.
```

??? note "Collapsible"
    This is the collapsed content.

---

**Tabbed content**

```markdown
=== "Tab One"
    Content for tab one.

=== "Tab Two"
    Content for tab two.
```

=== "Tab One"
    Content for tab one.

=== "Tab Two"
    Content for tab two.

---

**Tables**

```markdown
| Header A | Header B |
|----------|----------|
| Cell     | Cell     |
```

---

**Images**

```markdown
![Alt text](../assets/images/example.png)
*Caption.*
```

---

**Mermaid diagrams**

````markdown
```mermaid
graph LR
    A[Player] --> B[PlayerController]
    B --> C[Health]
```
````

```mermaid
graph LR
    A[Player] --> B[PlayerController]
    B --> C[Health]
```

---

**Emoji** — browse all at [squidfunk.github.io/mkdocs-material/reference/icons-emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)

```markdown
:material-gamepad-variant:  :material-code-braces:  :fontawesome/brands/github:
```

---

**Grid cards**

```markdown
<div class="grid cards" markdown>

-   :material-gamepad-variant:{ .lg .middle } **Card Title**

    ---

    Description.

    [:octicons-arrow-right-24: Link](target.md)

</div>
```

---

**Keyboard keys**

```markdown
++ctrl+s++  ++enter++  ++alt+f4++
```

++ctrl+s++ · ++enter++

---

**Math (LaTeX)**

Inline: `\(E = mc^2\)` → \(E = mc^2\)

Block:
```markdown
\[ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \]
```
