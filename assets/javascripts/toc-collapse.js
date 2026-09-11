/*
 * Collapsible table of contents.
 *
 * Material renders every heading in the right-hand sidebar, which gets long on
 * pages with several steps per section. This adds a chevron to any entry that
 * has sub-entries, starts them collapsed, and opens the section you're
 * currently reading as you scroll. Clicking a chevron wins: anything you open
 * or close by hand stays that way until the page is reloaded.
 *
 * Everything here is progressive enhancement. With JavaScript off, the table of
 * contents is exactly what Material rendered, fully expanded.
 */
(function () {
  "use strict";

  var PARENT = "siggd-toc-parent";
  var COLLAPSED = "siggd-toc-collapsed";
  var MANUAL = "siggd-toc-manual";
  var CHEVRON =
    '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' +
    '<path d="M8.59 16.59 13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41Z"/></svg>';

  var counter = 0;

  function childNav(item) {
    for (var i = 0; i < item.children.length; i++) {
      if (item.children[i].matches("nav.md-nav")) return item.children[i];
    }
    return null;
  }

  function childLink(item) {
    for (var i = 0; i < item.children.length; i++) {
      if (item.children[i].matches("a.md-nav__link")) return item.children[i];
    }
    return null;
  }

  function setExpanded(item, expanded) {
    item.classList.toggle(COLLAPSED, !expanded);
    var button = item.querySelector(":scope > .siggd-toc-toggle");
    if (!button) return;
    button.setAttribute("aria-expanded", String(expanded));
    var label = button.getAttribute("data-label") || "section";
    button.setAttribute(
      "aria-label",
      (expanded ? "Hide subsections of " : "Show subsections of ") + label
    );
  }

  function enhance(item) {
    if (item.classList.contains(PARENT)) return;
    var link = childLink(item);
    var nav = childNav(item);
    if (!link || !nav) return;

    if (!nav.id) nav.id = "siggd-toc-" + ++counter;

    var button = document.createElement("button");
    button.type = "button";
    button.className = "siggd-toc-toggle";
    button.innerHTML = CHEVRON;
    button.setAttribute("aria-controls", nav.id);
    button.setAttribute("data-label", link.textContent.trim());
    button.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      item.classList.add(MANUAL);
      setExpanded(item, item.classList.contains(COLLAPSED));
    });

    item.classList.add(PARENT);
    link.insertAdjacentElement("afterend", button);
    setExpanded(item, false);
  }

  /* Opens the section the reader is in, and closes the ones they've left. */
  function syncActive(toc) {
    var active = toc.querySelector(".md-nav__link--active");
    var open = [];
    if (active) {
      var node = active.closest(".md-nav__item");
      while (node && toc.contains(node)) {
        if (node.classList.contains(PARENT)) open.push(node);
        node = node.parentElement && node.parentElement.closest(".md-nav__item");
      }
    }

    var parents = toc.querySelectorAll("." + PARENT);
    for (var i = 0; i < parents.length; i++) {
      var item = parents[i];
      if (item.classList.contains(MANUAL)) continue;
      var shouldOpen = open.indexOf(item) !== -1;
      if (shouldOpen === !item.classList.contains(COLLAPSED)) continue;
      setExpanded(item, shouldOpen);
    }
  }

  function setup() {
    var tocs = document.querySelectorAll('[data-md-component="toc"]');
    for (var i = 0; i < tocs.length; i++) {
      var toc = tocs[i];
      if (toc.dataset.siggdToc) continue;
      toc.dataset.siggdToc = "1";

      var items = toc.querySelectorAll(".md-nav__item");
      for (var j = 0; j < items.length; j++) enhance(items[j]);
      syncActive(toc);

      /* Material marks the heading you're reading as it scrolls by. */
      (function (node) {
        var queued = false;
        new MutationObserver(function (records) {
          var relevant = records.some(function (record) {
            return (
              record.target.nodeType === 1 &&
              record.target.matches &&
              record.target.matches("a.md-nav__link")
            );
          });
          if (!relevant || queued) return;
          queued = true;
          requestAnimationFrame(function () {
            queued = false;
            syncActive(node);
          });
        }).observe(node, {
          subtree: true,
          attributes: true,
          attributeFilter: ["class"],
        });
      })(toc);
    }
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(setup);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setup);
  } else {
    setup();
  }
})();
