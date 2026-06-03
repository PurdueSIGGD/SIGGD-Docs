---
title: Contributing to SIGGD Docs
description: How to add tutorials, project documentation, and resources to this site.
---

# Contributing to SIGGD Docs

This documentation site is built and maintained by SIGGD members — which
means **you** can add to it. Contributions of any size are welcome: fixing a
typo, adding a tutorial, or fully documenting a project you worked on.

---

## Quick Start

**Prerequisites:** Python 3.8+, Git, a GitHub account.

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/SIGGD-Docs.git
cd SIGGD-Docs

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the local dev server with live reload
mkdocs serve

# 4. Open http://127.0.0.1:8000 in your browser
```

Make your changes, then:

```bash
# Validate the build before submitting (catches broken links and nav errors)
mkdocs build --strict

# Open a pull request on GitHub when ready
```

---

## What to Contribute

| Type | Template to use | Where to put it |
|------|----------------|-----------------|
| Tutorial | [Tutorial Template](templates/tutorial-template.md) | `docs/tutorials/<category>/` |
| Project overview | [Project Template](templates/project-template.md) | `docs/projects/<project-name>/` |
| Codebase docs | [Codebase Template](templates/codebase-template.md) | `docs/projects/<project-name>/codebase/` |
| System doc | [System Template](templates/system-template.md) | `docs/projects/<project-name>/codebase/systems/` |
| Script reference | [Script Template](templates/script-template.md) | `docs/projects/<project-name>/codebase/scripts/` |
| Resource page | [Resource Template](templates/resource-template.md) | `docs/resources/` |
| Style fix | — | Anywhere |

---

## Adding Your Page to the Navigation

Every new page must be added to the `nav:` section of `mkdocs.yml` to appear
in the sidebar. Find the section your page belongs to and add an entry:

```yaml
nav:
  - Tutorials:
      - Programming:
          - tutorials/programming/index.md
          - Your New Tutorial: tutorials/programming/your-new-tutorial.md  # ← add this
```

If you're adding a new project, follow the pattern of `example-project` in
the nav — create the full folder structure with `codebase/`, `team.md`, etc.

---

## Before You Submit a PR

- [ ] `mkdocs build --strict` passes with zero errors
- [ ] Your page has correct [frontmatter](#frontmatter-reference) (title, description, tags)
- [ ] You've added your page to `nav:` in `mkdocs.yml`
- [ ] All external links you added are live
- [ ] You followed the [Style Guide](style-guide.md)

---

## Frontmatter Reference

Every page should start with YAML frontmatter between `---` delimiters:

```yaml
---
title: "Your Page Title"
description: "One sentence shown in search results and social previews."
tags:
  - programming   # see tags.md for the full tag list
status: draft     # draft | review | published
---
```

---

## Author Crediting

Author attribution is **automatic** — the `git-authors` plugin reads your git
commit history and displays your name at the bottom of every page you
contribute to. Just commit your changes with your real name configured in git:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

No extra steps needed. Your contribution is permanently credited.
