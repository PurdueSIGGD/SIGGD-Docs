"""
Author attribution hook for SIGGD Docs.

Usage in page frontmatter:

    ---
    author: "@github-username"
    ---

    # or multiple authors:

    author:
      - "@github-username"
      - "First Last"

When `author` is set, the page renders an "Original author" block below the
content. The git-authors plugin continues to show whoever committed the file
as the editor. If `author` is not set, the committer gets full credit as usual.
"""


def on_page_content(html, page, **kwargs):
    author = page.meta.get("author", None)
    if not author:
        return html

    # Normalise to a list so single strings and lists both work
    if isinstance(author, str):
        authors = [author]
    else:
        authors = list(author)

    names_html = ", ".join(f"<strong>{a}</strong>" for a in authors)

    block = (
        '<div class="siggd-original-author">'
        '<span class="siggd-author-label">Original author</span>'
        f'<span class="siggd-author-names">{names_html}</span>'
        "</div>"
    )

    return html + block
