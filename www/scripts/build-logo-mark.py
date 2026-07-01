"""Build header logo marks: cropped wide lockup without subtitle band."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
src = (ROOT / "brand/logo/svg/tdhhc-wide-color-dark-erstoria.svg").read_text(encoding="utf-8")

parts = src.split('<g clip-path="url(#_clip1)">', 1)
if len(parts) != 2:
    raise SystemExit("clip structure not found")
head, body = parts

m = re.search(r"(</g>)(<g>)(.*?)(</g>)(<rect id=\"tdhhc-icon)", body, re.DOTALL)
if not m:
    raise SystemExit("subtitle group not found")
body = body[: m.start(2)] + body[m.end(4) :]

svg = head + '<g clip-path="url(#_clip1)">' + body
svg = svg.replace('viewBox="0 0 4117 1405"', 'viewBox="0 0 4117 980"')
svg = svg.replace('width="4113.84" height="1400.32"', 'width="4113.84" height="980"')


def recolor(text: str, mapping: dict[str, str]) -> str:
    for old, new in mapping.items():
        text = text.replace(f"fill:{old}", f"fill:{new}")
    return text


assets = ROOT / "www/assets"
assets.mkdir(parents=True, exist_ok=True)
(assets / "logo-mark.svg").write_text(svg, encoding="utf-8")

navy_map = {
    "#472d30": "#0f172a",
    "#438c4f": "#55BAAC",
    "#8d213d": "#C62026",
    "#e84139": "#C62026",
}
(assets / "logo-mark-navy.svg").write_text(recolor(svg, navy_map), encoding="utf-8")
print("Wrote logo-mark.svg and logo-mark-navy.svg")
