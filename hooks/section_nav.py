"""
Section-bounded footer navigation for SIGGD Docs.

MkDocs' navigation.footer feature links pages linearly across the entire nav
tree, so the last page of one section points to the first page of the next.
This hook suppresses those cross-section links so prev/next only appear when
both pages share the same top-level section.
"""


def _top_section(nav_item):
    """Walk the parent chain to find the root-level nav item."""
    current = nav_item
    while current.parent is not None:
        current = current.parent
    return current


def on_page_context(context, page, **kwargs):
    current_top = _top_section(page)

    if page.previous_page is not None:
        if _top_section(page.previous_page) is not current_top:
            page.previous_page = None

    if page.next_page is not None:
        if _top_section(page.next_page) is not current_top:
            page.next_page = None
