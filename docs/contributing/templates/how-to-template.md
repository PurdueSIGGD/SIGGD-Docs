---
title: "How-To Template"
description: "Step-by-step recipe for one common change to a project's codebase."
tags:
  - project
  - programming
# author: "@github-username"  # only if committing someone else's work
---

# Add a Thing

A how-to is a recipe for one change someone makes often, like adding a gun or a sound. It assumes the reader already has the project open and knows what they want to build. Link to the system page for background instead of explaining the system again here.

One or two sentences on what the change involves (which assets, which classes), and a link to the system page. If the recipe builds an example, say what it is.

---

## 1. First Step

Numbered steps, each one action. Give exact paths and menu items:

1. In `Assets/YourSystem/`, right-click and choose **Create > Data > YourAsset**.
2. Set `fieldName` to the value it needs.

Code goes in a full, compilable example the reader can paste, following the [C# Style Guide](../../tutorials/programming/csharp-style-guide.md):

```csharp
public class NewThing : BaseThing
{
    [SerializeField] private float strength = 1f;

    protected override void OnUse()
    {
        // ...
    }
}
```

After the code, list what the reader should copy from it into their own version.

## 2. Next Step

...

## 3. Try It

How to see the change working in the editor, and anything to undo before committing.

---

## Checklist

End with a checklist, a "Things to Watch For" list, or a Troubleshooting section (tabs work well for symptom and fix), whichever suits the recipe:

- [ ] Units are right (seconds or milliseconds, degrees or radians).
- [ ] New files are committed with their `.meta` files.
