document.addEventListener("DOMContentLoaded", () => {
  if (!document.querySelector(".migration-notice")) {
    const banner = document.createElement("div");
    banner.className = "migration-notice";
    banner.setAttribute("role", "status");
    banner.innerHTML =
      '<p class="migration-notice__text"><strong>Website migration in progress.</strong> ' +
      "We are moving TDHHC.org to a new host. Some pages and forms are still being updated. " +
      'For interpreter requests or urgent needs, use Voice <a href="tel:+19036176204">(903) 617-6204</a>, ' +
      'VP <a href="tel:+19032062210">(903) 206-2210</a>, or ' +
      '<a href="mailto:coordinator@tdhhc.org">coordinator@tdhhc.org</a>.</p>';
    const header = document.querySelector("header.site-chrome");
    if (header) {
      header.parentNode.insertBefore(banner, header);
    } else {
      document.body.prepend(banner);
    }
  }

  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
});
