"""Build wide logo without subtitle band (vector edit, not viewBox crop)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "brand/logo/svg/tdhhc-wide-color-dark-erstoria.svg"
BRAND_OUT = ROOT / "brand/logo/svg/tdhhc-wide-no-subtitle-erstoria.svg"
ASSETS = ROOT / "www/assets"


def strip_subtitle(svg: str) -> str:
    parts = svg.split('<g clip-path="url(#_clip1)">', 1)
    if len(parts) != 2:
        raise SystemExit("clip structure not found")
    head, body = parts
    m = re.search(r"(</g>)(<g>)(.*?)(</g>)(<rect id=\"tdhhc-icon)", body, re.DOTALL)
    if not m:
        raise SystemExit("subtitle group not found")
    body = body[: m.start(2)] + body[m.end(4) :]
    return head + '<g clip-path="url(#_clip1)">' + body


def recolor(text: str, mapping: dict[str, str]) -> str:
    for old, new in mapping.items():
        text = text.replace(f"fill:{old}", f"fill:{new}")
    return text


def main() -> None:
    src = SRC.read_text(encoding="utf-8")
    no_sub = strip_subtitle(src)

    BRAND_OUT.write_text(no_sub, encoding="utf-8")
    ASSETS.mkdir(parents=True, exist_ok=True)

    # Brand colors — for light backgrounds / reference
    (ASSETS / "logo-mark.svg").write_text(no_sub, encoding="utf-8")

    # On dark chrome: light wordmark + hands, brand red roses, teal leaves
    on_dark = recolor(
        no_sub,
        {
            "#472d30": "#f8fafc",
            "#438c4f": "#55BAAC",
            "#8d213d": "#C62026",
            "#e84139": "#C62026",
        },
    )
    (ASSETS / "logo-mark-on-dark.svg").write_text(on_dark, encoding="utf-8")

    # Optional: navy wordmark on white (legacy theme tests)
    on_light_navy = recolor(
        no_sub,
        {
            "#472d30": "#0f172a",
            "#438c4f": "#55BAAC",
            "#8d213d": "#C62026",
            "#e84139": "#C62026",
        },
    )
    (ASSETS / "logo-mark-navy.svg").write_text(on_light_navy, encoding="utf-8")

    print(f"Wrote {BRAND_OUT.name}, logo-mark.svg, logo-mark-on-dark.svg")


if __name__ == "__main__":
    main()
