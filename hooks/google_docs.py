"""
Google Docs (and Sheets, Slides, Forms) embeds for SIGGD Docs.

There are two ways to embed a Google file.

1. A whole page that is just an embedded file: set `google_doc` in the page's
   frontmatter. The embed is added below whatever the page's Markdown contains,
   and the right-hand table of contents is hidden so the file gets full width.

       ---
       title: "Story Design Doc"
       google_doc: https://docs.google.com/document/d/FILE_ID/edit?usp=sharing
       ---

2. An embed inside a normal page: tag an ordinary Markdown link with the
   `google-doc` class. If this hook ever stops running, the link still works.

       [Story Design Doc](https://docs.google.com/document/d/FILE_ID/edit){ .google-doc }

Height can be overridden per embed with `height="900"` on the link, or
`google_doc_height: 900` in frontmatter. Any CSS length works.

The file has to be shared ("Anyone with the link") or published to the web, or
visitors will see Google's "you need access" screen inside the frame. URLs that
are already embed URLs (Google's own Embed dialog, or a published `/pub` link)
are passed through untouched.

A URL that isn't a recognised Google file link logs a warning, which fails the
strict build used on pull requests.
"""

import re
from html import escape
from urllib.parse import urlsplit, urlunsplit

from mkdocs.plugins import get_plugin_logger

log = get_plugin_logger(__name__)

# Matches the Markdown-rendered <a> for an inline embed, e.g.
# <a class="google-doc" href="...">Story Design Doc</a>
INLINE_LINK = re.compile(
    r'<a\b(?P<attrs>[^>]*\bclass="[^"]*\bgoogle-doc\b[^"]*"[^>]*)>(?P<text>.*?)</a>',
    re.DOTALL,
)

ATTR = re.compile(r'(?P<name>[a-zA-Z_:][-\w:.]*)\s*=\s*"(?P<value>[^"]*)"')

# /document/d/FILE_ID/..., /spreadsheets/d/e/PUBLISHED_ID/... and friends
FILE_URL = re.compile(
    r"^https://docs\.google\.com/(?P<kind>document|spreadsheets|presentation|forms)/"
    r"d/(?P<published>e/)?(?P<id>[a-zA-Z0-9_-]+)"
)

# A URL that is already an embeddable view. Passed through as-is.
ALREADY_EMBED = ("/preview", "/pub", "/pubhtml", "/htmlembed", "/embed", "/viewform")

KINDS = {
    "document": ("Google Doc", "Open in Google Docs"),
    "spreadsheets": ("Google Sheet", "Open in Google Sheets"),
    "presentation": ("Google Slides", "Open in Google Slides"),
    "forms": ("Google Form", "Open in Google Forms"),
}


class EmbedError(ValueError):
    """Raised when a URL can't be turned into an embed."""


def _css_length(height):
    """Normalises a height into a CSS length. Bare numbers are pixels."""
    if height is None:
        return None
    value = str(height).strip()
    if not value:
        return None
    if re.fullmatch(r"\d+(\.\d+)?", value):
        return f"{value}px"
    if not re.fullmatch(r"[\w.%()+*/ -]+", value):
        raise EmbedError(f"'{value}' is not a usable height (try 900 or 80vh)")
    return value


def _path_of(url):
    return urlsplit(url).path


def _with_query(url, addition):
    """Adds a query parameter, keeping anything already there."""
    parts = urlsplit(url)
    key = addition.split("=", 1)[0]
    if parts.query and key in parts.query:
        return url
    query = f"{parts.query}&{addition}" if parts.query else addition
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, ""))


def _embed_url(url, kind, file_id, is_published):
    """Turns a share link into the URL that belongs in the iframe."""
    path = _path_of(url)

    # Already an embeddable view: leave it alone, beyond the flags Google's own
    # embed codes set.
    if any(segment in path for segment in ALREADY_EMBED):
        if kind in ("document", "forms"):
            return _with_query(url, "embedded=true")
        return url

    base = f"https://docs.google.com/{kind}/d/{'e/' if is_published else ''}{file_id}"

    if kind == "presentation":
        return f"{base}/embed?start=false&loop=false&delayms=3000"
    if kind == "forms":
        # A /forms/d/ID/edit link is the editor, which has no public view we can
        # derive. The author has to paste the live form link instead.
        raise EmbedError(
            "that looks like a Google Forms editor link. Send the form (Send -> link) "
            "and paste the live '/viewform' link instead"
        )
    return f"{base}/preview"


def _open_url(url, kind, file_id, is_published):
    """The URL for the 'Open in Google ...' button."""
    if is_published or kind == "forms" or any(s in _path_of(url) for s in ALREADY_EMBED):
        return url
    return f"https://docs.google.com/{kind}/d/{file_id}/edit"


def build_embed(url, title=None, height=None, page_level=False):
    """Returns the HTML for one embed. Raises EmbedError for unusable URLs."""
    url = (url or "").strip()
    if not url:
        raise EmbedError("no URL given")

    match = FILE_URL.match(url)
    if not match:
        raise EmbedError(
            f"'{url}' is not a Google Docs, Sheets, Slides or Forms link "
            "(expected https://docs.google.com/document/d/...)"
        )

    kind = match.group("kind")
    file_id = match.group("id")
    is_published = bool(match.group("published"))
    label, open_text = KINDS[kind]

    embed = _embed_url(url, kind, file_id, is_published)
    opens = _open_url(url, kind, file_id, is_published)
    frame_title = title.strip() if title and title.strip() else label

    classes = ["siggd-embed", f"siggd-embed--{kind}"]
    if page_level:
        classes.append("siggd-embed--page")

    length = _css_length(height)
    style = f' style="--siggd-embed-height: {escape(length, quote=True)}"' if length else ""

    return (
        f'<div class="{" ".join(classes)}"{style}>'
        f'<div class="siggd-embed__bar">'
        f'<span class="siggd-embed__label">{escape(label)}</span>'
        f'<a class="siggd-embed__open" href="{escape(opens, quote=True)}"'
        f' target="_blank" rel="noopener">{escape(open_text)}</a>'
        f"</div>"
        f'<iframe class="siggd-embed__frame" src="{escape(embed, quote=True)}"'
        f' title="{escape(frame_title, quote=True)}" loading="lazy"'
        f' allowfullscreen></iframe>'
        f"</div>"
    )


def on_page_markdown(markdown, page, config, files, **kwargs):
    """Validates frontmatter embeds early, and hides the empty table of contents."""
    url = page.meta.get("google_doc")
    if not url:
        return markdown

    try:
        build_embed(url)
    except EmbedError as error:
        log.warning("%s: %s", page.file.src_uri, error)
        return markdown

    # The site can't see headings inside the embedded file, so the right sidebar
    # would be empty. Hiding it gives the file the full width of the page.
    hide = page.meta.get("hide") or []
    if isinstance(hide, str):
        hide = [hide]
    if "toc" not in hide:
        page.meta["hide"] = list(hide) + ["toc"]

    return markdown


def on_page_content(html, page, config, files, **kwargs):
    """Replaces tagged links with embeds, and appends the frontmatter embed."""

    def replace(match):
        attrs = dict(ATTR.findall(match.group("attrs")))
        text = re.sub(r"<[^>]+>", "", match.group("text")).strip()
        try:
            return build_embed(
                attrs.get("href", ""),
                title=text,
                height=attrs.get("height"),
            )
        except EmbedError as error:
            log.warning("%s: %s", page.file.src_uri, error)
            return match.group(0)

    html = INLINE_LINK.sub(replace, html)

    url = page.meta.get("google_doc")
    if url:
        try:
            html += build_embed(
                url,
                title=page.title,
                height=page.meta.get("google_doc_height"),
                page_level=True,
            )
        except EmbedError:
            pass  # already reported in on_page_markdown

    return html
