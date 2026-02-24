(function () {
  "use strict";

  var STORAGE_KEY = "preferred-lang";
  var DEFAULT_LANG = "ja";

  function getPreferredLang() {
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored) return stored;
    var browserLang = (navigator.language || navigator.userLanguage || "").toLowerCase();
    return browserLang.startsWith("ja") ? "ja" : "en";
  }

  function applyLang(lang) {
    document.documentElement.lang = lang;

    var jaDivs = document.querySelectorAll('[lang="ja"]');
    var enDivs = document.querySelectorAll('[lang="en"]');

    for (var i = 0; i < jaDivs.length; i++) {
      jaDivs[i].style.display = lang === "ja" ? "" : "none";
    }
    for (var i = 0; i < enDivs.length; i++) {
      enDivs[i].style.display = lang === "en" ? "" : "none";
    }

    var buttons = document.querySelectorAll(".lang-toggle-btn");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].textContent = lang === "ja" ? "Read in English" : "\u65E5\u672C\u8A9E\u3067\u8AAD\u3080";
      buttons[i].setAttribute("aria-label",
        lang === "ja" ? "Switch to English" : "\u65E5\u672C\u8A9E\u306B\u5207\u308A\u66FF\u3048");
    }

    // Update bilingual title display
    var titleJa = document.querySelectorAll(".title-ja");
    var titleEn = document.querySelectorAll(".title-en");
    for (var i = 0; i < titleJa.length; i++) {
      titleJa[i].style.display = lang === "ja" ? "" : "none";
    }
    for (var i = 0; i < titleEn.length; i++) {
      titleEn[i].style.display = lang === "en" ? "" : "none";
    }
  }

  function toggleLang() {
    var current = localStorage.getItem(STORAGE_KEY) || getPreferredLang();
    var next = current === "ja" ? "en" : "ja";
    localStorage.setItem(STORAGE_KEY, next);
    applyLang(next);
  }

  // Expose only what button onclick handlers need
  window.toggleLang = toggleLang;

  // Apply on DOM ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      applyLang(getPreferredLang());
    });
  } else {
    applyLang(getPreferredLang());
  }
})();
