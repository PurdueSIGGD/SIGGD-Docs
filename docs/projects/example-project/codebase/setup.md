---
title: Example Project — Setup Guide
description: How to get Example Project running locally for development.
tags:
  - project
  - setup
---

# Local Setup Guide

Follow these steps to get Example Project running locally for development or
contribution.

---

## Prerequisites

| Requirement | Version | Where to get it |
|-------------|---------|----------------|
| Unity Hub | Latest | [unity.com/download](https://unity.com/download) |
| Unity Editor | 2022.3 LTS | Via Unity Hub |
| Git | Any recent | [git-scm.com](https://git-scm.com) |

!!! warning "Use the correct Unity version"
    Opening the project with a different Unity version may cause import
    errors or behavioral changes. Always use **Unity 2022.3 LTS**.

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/PurdueSIGGD/example-project.git
cd example-project
```

Or use GitHub Desktop: **File → Clone Repository → GitHub.com →** search for
`PurdueSIGGD/example-project`.

---

## Step 2: Open in Unity Hub

1. Open **Unity Hub**.
2. Click **Open** → **Add project from disk**.
3. Navigate to the cloned folder and select it.
4. The project will appear in Unity Hub — click it to open.

Unity will import all assets on the first open (may take a few minutes).

---

## Step 3: Install Required Packages

The project uses the following Unity packages (installed automatically via
the Package Manager manifest):

| Package | Purpose |
|---------|---------|
| Input System | New input system for player controls |
| TextMeshPro | UI text rendering |
| Cinemachine | Camera management |

If a package fails to import: **Window → Package Manager → Packages: In Project**
and reinstall any package with an error icon.

---

## Step 4: Open the Main Scene

1. In the **Project** panel, navigate to `Assets/Scenes/`.
2. Double-click `Level01.unity` to open it.
3. Press **Play (▶)** in the editor toolbar.

---

## Common Issues

=== "Pink / magenta materials"
    **Cause:** URP (Universal Render Pipeline) shaders not compiled.

    **Fix:** **Edit → Render Pipeline → Universal Render Pipeline →
    Upgrade Project Materials to UniversalRP Materials.**

=== "Missing script errors"
    **Cause:** Script compilation errors preventing Unity from loading components.

    **Fix:** Check the **Console** panel for compiler errors and fix them.
    Usually caused by missing packages or wrong Unity version.

=== "Input not working in Play mode"
    **Cause:** New Input System requires the active input handling to be set.

    **Fix:** **Edit → Project Settings → Player → Active Input Handling →
    Input System Package (New)** — then restart the editor.

---

## Making Changes

Create a branch before making changes:

```bash
git checkout -b feature/your-feature-name
```

When done, push and open a pull request on GitHub.
