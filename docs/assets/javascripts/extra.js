/* MathJax configuration required by pymdownx.arithmatex */
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

/*
 * Load MathJax only on pages that actually contain math.
 *
 * arithmatex wraps every formula in `.arithmatex`, so a page with no formulas
 * has nothing for MathJax to render. Loading it on demand keeps the request to
 * unpkg off every other page on the site.
 */
(function () {
  "use strict";

  var SRC = "https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js";
  var loaded = false;

  function loadMathJaxIfNeeded() {
    if (loaded || !document.querySelector(".arithmatex")) return;
    loaded = true;
    var script = document.createElement("script");
    script.src = SRC;
    script.async = true;
    document.head.appendChild(script);
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(loadMathJaxIfNeeded);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadMathJaxIfNeeded);
  } else {
    loadMathJaxIfNeeded();
  }
})();
