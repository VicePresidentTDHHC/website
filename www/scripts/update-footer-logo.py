"""Replace footer logo PNG with no-subtitle mark + readable org name."""
import re
from pathlib import Path

WWW = Path(__file__).resolve().parents[1]

OLD = re.compile(
    r'\s*<div class="footer__logo">\s*'
    r'<img src="(?:\.\./)?assets/logo-white\.png" alt="" width="392" height="245" class="footer__logo-img">\s*'
    r'</div>\s*'
    r'<div>\s*'
    r'<h2>Tyler Deaf and Hard of Hearing Center</h2>\s*'
    r'<p>501\(c\)\(3\) nonprofit &middot; Serving East Texas since 2012</p>\s*'
    r'</div>',
    re.DOTALL,
)


def rel_prefix(html_path: Path) -> str:
    depth = len(html_path.relative_to(WWW).parts) - 1
    return "../" * depth if depth else ""


def block(prefix: str) -> str:
    return f"""
        <div class="footer__brand">
          <a class="footer__brand-link" href="{prefix}index.html">
            <img src="{prefix}assets/logo-mark-light.svg" alt="TDHHC" width="240" height="82" class="footer__logo-mark">
            <span class="footer__org-name">Tyler Deaf &amp; Hard of Hearing Center</span>
          </a>
          <p class="footer__org-meta">501(c)(3) nonprofit &middot; Serving East Texas since 2012</p>
        </div>"""


def main() -> None:
    for path in sorted(WWW.rglob("*.html")):
        if "examples" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        updated = OLD.sub(block(rel_prefix(path)), text, count=1)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            print(f"updated: {path.relative_to(WWW)}")


if __name__ == "__main__":
    main()
