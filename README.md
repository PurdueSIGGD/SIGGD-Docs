# SIGGD Docs

Documentation, tutorials, and resources for Purdue's Special Interest Group
in Game Development.

**Live site:** https://PurdueSIGGD.github.io/SIGGD-Docs/

---

## Contributing

All club members are welcome to contribute. You only need Python and Git.

### Local Setup

```bash
# Clone the repo (or your fork)
git clone https://github.com/PurdueSIGGD/SIGGD-Docs.git
cd SIGGD-Docs

# Install dependencies
pip install -r requirements.txt

# Start the live-reload dev server
mkdocs serve
```

Open http://127.0.0.1:8000 — the site refreshes automatically as you edit files.

### Validate Before Submitting

```bash
mkdocs build --strict
```

This catches broken internal links, missing nav entries, and frontmatter
errors. Fix all warnings before opening a pull request.

### Submitting Changes

1. Create a branch: `git checkout -b your-branch-name`
2. Make your changes and run `mkdocs build --strict`
3. Push and open a pull request on GitHub
4. The PR checklist will guide you through the review requirements

See [docs/contributing/index.md](docs/contributing/index.md) for the full
contributing guide, style guide, and templates.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [MkDocs](https://www.mkdocs.org/) | Static site generator |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | Theme |
| [mkdocs-git-authors-plugin](https://github.com/timvink/mkdocs-git-authors-plugin) | Author attribution from git history |
| [mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin) | "Last updated" dates |
| GitHub Actions | CI/CD — auto-deploys to GitHub Pages on merge to `main` |
| GitHub Pages | Hosting |

## Deployment

Merging to `main` triggers a GitHub Actions workflow that builds the site
and pushes it to the `gh-pages` branch. GitHub Pages serves from that branch.

**First-time setup:** After the first successful deploy, go to
`Settings → Pages` in this repo, set source to **Deploy from a branch**,
choose `gh-pages` / `/(root)`, and save.
