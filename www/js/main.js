(function () {
  var stored = localStorage.getItem("tdhhc-theme");
  if (stored === "hi-contrast") {
    document.documentElement.setAttribute("data-theme", "hi-contrast");
  }
})();

document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    var isHighContrast = document.documentElement.getAttribute("data-theme") === "hi-contrast";
    updateToggleLabel(toggle, isHighContrast);

    toggle.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-theme");
      var next = current === "hi-contrast" ? "v4" : "hi-contrast";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("tdhhc-theme", next);
      updateToggleLabel(toggle, next === "hi-contrast");
    });
  }

  var navToggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (navToggle && nav) {
    navToggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
});

function updateToggleLabel(btn, isHighContrast) {
  var label = btn.querySelector(".theme-toggle__label");
  var icon = btn.querySelector(".theme-toggle__icon");
  if (isHighContrast) {
    if (label) label.textContent = "Standard View";
    if (icon) icon.textContent = "◉";
    btn.setAttribute("aria-pressed", "true");
  } else {
    if (label) label.textContent = "High Contrast";
    if (icon) icon.textContent = "◎";
    btn.setAttribute("aria-pressed", "false");
  }
}
