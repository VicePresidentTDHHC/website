(function () {
  const STORAGE_KEY = "tdhhc-theme";
  const DEFAULT = "v1";

  function setTheme(id) {
    document.documentElement.setAttribute("data-theme", id);
    localStorage.setItem(STORAGE_KEY, id);
    document.querySelectorAll("[data-set-theme]").forEach((btn) => {
      const active = btn.getAttribute("data-set-theme") === id;
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  const saved = localStorage.getItem(STORAGE_KEY) || DEFAULT;
  document.documentElement.setAttribute("data-theme", saved);

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-set-theme]").forEach((btn) => {
      const id = btn.getAttribute("data-set-theme");
      btn.setAttribute("aria-pressed", id === saved ? "true" : "false");
      btn.addEventListener("click", () => setTheme(id));
    });
  });
})();
