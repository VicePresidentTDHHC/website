"""Build wide logo without subtitle band (vector edit, not viewBox crop)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "www/assets"
BRAND_DIR = ROOT / "brand/logo/svg"


def strip_subtitle(svg: str) -> str:
    # Subtitle is always the Erstoria letterform group starting at M1711,986.16
    result, count = re.subn(
        r'<g><path d="M1711,986\.16.*?</g>',
        "",
        svg,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise SystemExit("subtitle group not found")
    return result


def recolor(text: str, mapping: dict[str, str]) -> str:
    for old, new in mapping.items():
        text = text.replace(f"fill:{old}", f"fill:{new}")
    return text


def build_variant(src_path: Path, brand_out: Path | None, asset_name: str | None) -> str:
    no_sub = strip_subtitle(src_path.read_text(encoding="utf-8"))
    if brand_out:
        brand_out.write_text(no_sub, encoding="utf-8")
    if asset_name:
        (ASSETS / asset_name).write_text(no_sub, encoding="utf-8")
    return no_sub


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)

    dark = build_variant(
        BRAND_DIR / "tdhhc-wide-color-dark-erstoria.svg",
        BRAND_DIR / "tdhhc-wide-no-subtitle-erstoria.svg",
        "logo-mark.svg",
    )

    build_variant(
        BRAND_DIR / "tdhhc-wide-color-light-erstoria.svg",
        BRAND_DIR / "tdhhc-wide-no-subtitle-light-erstoria.svg",
        "logo-mark-light.svg",
    )

    # Header chrome — adapted palette for navy themes
    on_dark = recolor(
        dark,
        {
            "#472d30": "#f8fafc",
            "#438c4f": "#55BAAC",
            "#8d213d": "#C62026",
            "#e84139": "#C62026",
        },
    )
    (ASSETS / "logo-mark-on-dark.svg").write_text(on_dark, encoding="utf-8")

    on_light_navy = recolor(
        dark,
        {
            "#472d30": "#0f172a",
            "#438c4f": "#55BAAC",
            "#8d213d": "#C62026",
            "#e84139": "#C62026",
        },
    )
    (ASSETS / "logo-mark-navy.svg").write_text(on_light_navy, encoding="utf-8")

    print(
        "Wrote no-subtitle variants (dark + light), logo-mark.svg, "
        "logo-mark-light.svg, logo-mark-on-dark.svg"
    )


if __name__ == "__main__":
    main()
