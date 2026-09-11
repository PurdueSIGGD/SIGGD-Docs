---
title: "Google Doc Template"
description: "How to put a Google Doc, Sheet, Slides deck, or Form on the site."
tags:
  - reference
---

# Google Doc Template

Some things are easier to write in Google Docs, and some people just prefer it. You can put any Google Doc, Sheet, Slides deck, or Form straight onto the site, either as a whole page or inside a normal page.

The doc stays live. Edit it in Google Docs and the site shows the new version immediately, with no commit and no rebuild.

---

## Before You Embed

- [ ] The file lives in the **SIGGD Shared Drive**, not someone's personal Drive. Files in a personal Drive disappear when that person deletes them or leaves the club. Ask a lead if you don't have access to the shared drive.
- [ ] Sharing is set to **Anyone with the link** (Viewer is enough). Without this, visitors see Google's "you need access" screen inside the frame.
- [ ] You have the normal share link, the one the **Share → Copy link** button gives you.

!!! warning "Anyone with the link means anyone"
    The site is public, so treat an embedded file as public. Don't embed anything with personal information, and remember that a doc can be edited by anybody you've given edit access to, without review.

---

## A Whole Page That Is Just a Doc

Create a new `.md` file, give it a title, and point `google_doc` at your file. That's the entire page:

```yaml
---
title: "Story Design Doc"
google_doc: https://docs.google.com/document/d/FILE_ID/edit?usp=sharing
---
```

You can write normal Markdown under the frontmatter too. It shows up above the embed, which is a good place for a sentence of context or a warning.

The right-hand table of contents is hidden automatically on these pages, since the site can't see the headings inside the file, and the embed takes the full width instead.

Then add the page to the `nav:` section of `mkdocs.yml` like any other page.

---

## A Doc Inside a Normal Page

Add `{ .google-doc }` to an ordinary Markdown link:

```markdown
[Story Design Doc](https://docs.google.com/document/d/FILE_ID/edit){ .google-doc }
```

The link text becomes the frame's title for screen readers. If the embed ever breaks, this is still a working link to the doc.

---

## Sizing

Embeds are as tall as most of your screen by default, and Slides keep a 16:9 shape. A cross-origin frame can't measure its own contents, so the document scrolls inside its frame rather than growing to fit.

To override the height, use any CSS length (a bare number means pixels):

```markdown
[Meeting Notes](https://docs.google.com/document/d/FILE_ID/edit){ .google-doc height="600" }
```

```yaml
---
title: "Task Tracker"
google_doc: https://docs.google.com/spreadsheets/d/FILE_ID/edit
google_doc_height: 1200
---
```

---

## What Works

| File type | Paste this | Notes |
|---|---|---|
| Docs | `https://docs.google.com/document/d/FILE_ID/edit` | |
| Sheets | `https://docs.google.com/spreadsheets/d/FILE_ID/edit` | Embeds the whole spreadsheet, tabs included |
| Slides | `https://docs.google.com/presentation/d/FILE_ID/edit` | Shown at 16:9 with Google's slide controls |
| Forms | `https://docs.google.com/forms/d/e/FORM_ID/viewform` | Use the **live** link from Send → link, not the editor link |

Published links (**File → Share → Publish to web**) work too, and so does any embed URL you copy out of Google's own Embed dialog. Both are passed through as they are, so use them if you want Google's cleaner published view.

---

## Things to Know

- **Site search can't see inside an embed.** Searching the site won't find text that lives in the doc. If something needs to be findable, write it in Markdown instead.
- **The doc keeps its own look.** A Google frame can't be restyled, so it stays white on our dark theme.
- **Google sets its own cookies** inside the frame. Nothing else on this site does.
- **The "Open in Google Docs" button** in the corner of every embed opens the real file in a new tab, which is where editing happens.
- **A bad link fails the build.** If the URL isn't a Google file link, the pull request build says so, with the page name and the reason.

---

## Troubleshooting

=== "The frame says I need access"
    **Symptom:** The embed shows a Google sign-in or "You need access" page.

    **Fix:** Sharing isn't set to "Anyone with the link." Open the file, click **Share**, and change **General access** from "Restricted" to **Anyone with the link**.

=== "The build failed on my page"
    **Symptom:** The PR build reports something like `not a Google Docs, Sheets, Slides or Forms link`.

    **Fix:** Use the link from the file's **Share → Copy link** button. A search-result link, a `drive.google.com/file/...` link, or a Forms *editor* link won't work.

=== "The embed is too short or too tall"
    **Symptom:** Lots of empty space, or a tiny scrolling window.

    **Fix:** Set a height, as shown in [Sizing](#sizing).
