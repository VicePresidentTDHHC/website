"""Merge contact-bar + site-header into unified site-chrome on all pages."""
import re
from pathlib import Path

WWW = Path(__file__).resolve().parents[1]


def rel_prefix(html_path: Path) -> str:
    depth = len(html_path.relative_to(WWW).parts) - 1
    return "../" * depth if depth else ""


def contact_href(prefix: str) -> str:
    return f"{prefix}contact.html"


def index_href(prefix: str) -> str:
    return f"{prefix}index.html"


CHROME_PATTERN = re.compile(
    r'<div class="contact-bar">.*?</div>\s*</div>\s*'
    r'<header class="site-header">\s*<div class="site-header__inner">.*?</nav>\s*</div>\s*</header>',
    re.DOTALL,
)

FOOTER_CONTACT = re.compile(
    r'\s*<div>\s*<h2>Contact</h2>\s*<p>VP:.*?</div>',
    re.DOTALL,
)


def build_chrome(prefix: str, nav: str) -> str:
    return f"""  <header class="site-chrome">
    <div class="site-chrome__inner">
      <div class="site-chrome__contacts" aria-label="Contact">
        <span>Video Phone: <a href="tel:+19032062210">(903) 206-2210</a></span>
        <span>Voice: <a href="tel:+19036176204">(903) 617-6204</a></span>
        <span><a href="mailto:coordinator@tdhhc.org">coordinator@tdhhc.org</a></span>
      </div>
      <div class="site-chrome__bar">
        <a class="logo" href="{index_href(prefix)}">
          <img class="logo__mark" src="{prefix}assets/logo-mark-on-dark.svg" alt="TDHHC" width="300" height="102">
          <span class="logo__tagline">Tyler Deaf &amp; Hard of Hearing Center</span>
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu</button>
        {nav}
      </div>
    </div>
  </header>"""


def build_footer_reach(prefix: str) -> str:
    return f"""
        <div>
          <h2>Reach us</h2>
          <p><a href="{contact_href(prefix)}">Contact form &amp; directions</a></p>
        </div>"""


def main() -> None:
    for path in sorted(WWW.rglob("*.html")):
        if "examples" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        prefix = rel_prefix(path)

        m = CHROME_PATTERN.search(text)
        if not m:
            print(f"skip (no match): {path.relative_to(WWW)}")
            continue
        nav_m = re.search(
            r'(<nav class="main-nav" id="main-nav" aria-label="Main">.*?</nav>)',
            m.group(0),
            re.DOTALL,
        )
        if not nav_m:
            print(f"skip (no nav): {path.relative_to(WWW)}")
            continue
        text = CHROME_PATTERN.sub(build_chrome(prefix, nav_m.group(1)), text, count=1)
        text = FOOTER_CONTACT.sub(build_footer_reach(prefix), text, count=1)

        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(f"updated: {path.relative_to(WWW)}")


if __name__ == "__main__":
    main()
