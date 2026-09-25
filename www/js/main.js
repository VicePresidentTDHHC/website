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

(function () {
  var list = document.getElementById("upcoming-events");
  if (!list || !window.TDHHC_EVENTS) return;

  var today = new Date();
  today.setHours(0, 0, 0, 0);

  var upcoming = window.TDHHC_EVENTS
    .filter(function (e) {
      var d = new Date(e.date + "T00:00:00");
      return d >= today;
    })
    .sort(function (a, b) {
      return new Date(a.date) - new Date(b.date);
    });

  var shown = upcoming.slice(0, 5);

  if (shown.length === 0) {
    var empty = document.createElement("li");
    empty.textContent = "No upcoming events scheduled. Check back soon!";
    list.appendChild(empty);
    return;
  }

  var monthNames = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];

  function formatDate(dateStr) {
    var d = new Date(dateStr + "T00:00:00");
    return monthNames[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear();
  }

  shown.forEach(function (e) {
    var li = document.createElement("li");

    var time = document.createElement("time");
    time.setAttribute("datetime", e.date);
    time.textContent = formatDate(e.date);
    li.appendChild(time);

    var title = document.createElement("strong");
    title.textContent = e.title;
    li.appendChild(title);

    var p = document.createElement("p");
    p.innerHTML = e.detail + ' <a href="' + e.href + '">Details</a>';
    li.appendChild(p);

    list.appendChild(li);
  });
})();
