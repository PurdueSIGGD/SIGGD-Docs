---
title: Contributing to SIGGD Docs
---

# Contributing

All club members can contribute. You only need Python and Git.

=== "Unix"
    ```bash
    # Clone (or fork) the repo
    git clone https://github.com/PurdueSIGGD/SIGGD-Docs.git
    cd SIGGD-Docs

    # Create virtual environment
    python3 -m venv .venv/

    # Enter virtual environment
    source .venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # Start the live-reload preview server
    mkdocs serve
    # → open http://127.0.0.1:8000
    ```

=== "Windows"
    ```bash
    # Clone (or fork) the repo
    git clone https://github.com/PurdueSIGGD/SIGGD-Docs.git
    cd SIGGD-Docs

    # Create virtual environment
    python3 -m venv .venv/

    # Enter virtual environment
    .\.venv\Scripts\activate.bat

    # Install dependencies
    pip install -r requirements.txt

    # Start the live-reload preview server
    mkdocs serve
    # → open http://127.0.0.1:8000
    ```

Before submitting a PR, run `mkdocs build --strict` to catch broken links and nav errors. Every new page also needs an entry in the `nav:` section of `mkdocs.yml`.

---

| Type | Template | Location |
|------|----------|----------|
| Tutorial | [Tutorial Template](templates/tutorial-template.md) | `docs/tutorials/<category>/` |
| Project overview | [Project Template](templates/project-template.md) | `docs/projects/<project-name>/` |
| Codebase docs | [Codebase Template](templates/codebase-template.md) | `docs/projects/<project-name>/codebase/` |
| System doc | [System Template](templates/system-template.md) | `docs/projects/<project-name>/codebase/systems/` |
| Script reference | [Script Template](templates/script-template.md) | `docs/projects/<project-name>/codebase/scripts/` |
| Resource page | [Resource Template](templates/resource-template.md) | `docs/resources/` |

---

**Author attribution** is automatic via git history. Make sure your name is set:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

If you're committing content someone else wrote, add `author: "@their-username"` to the page frontmatter. They get credited as the original author; you show as the editor.
