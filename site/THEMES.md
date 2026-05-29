# Visual themes (V1, V2, V3)

Themes are **CSS-only** — swap with the **Look:** buttons in the preview banner.

## Ground rules

1. **Themes are options, not requirements.** V1/V2/V3 are mock-up directions; production can pick one or replace entirely.
2. **Original footer curve** on the wine theme uses `TDHHC_footer_lite.png` from the live site (same asset as Divi `et_pb_section_7`). Slate and Navy use an SVG traced from that silhouette in the theme’s chrome color.
3. **High contrast** for low vision: Atkinson Hyperlegible, body text `#0a0a0a` range on light backgrounds, muted text no lighter than `#3d3d3d`, bold headings, 1.125rem base size.
4. **Top and bottom match** via `--color-chrome`: contact bar, preview banner, and footer band share one hue per theme. Red appears as a **full wine theme (V3)**, not a mismatched footer on teal/navy headers.
5. **True alarm red** stays on `.notice--alert` only (`--color-alert`).

## Themes

| Theme | Label | Chrome | Accent | Character |
|-------|-------|--------|--------|-------------|
| **V1** | Slate | `#2d2a28` | `#0c5c6e` | Neutral, high-contrast default |
| **V2** | Navy | `#0f172a` | `#b45309` | Navy + gold, unified top/bottom |
| **V3** | Wine | `#58181f` / `#9b1e2e` | Ruby `#9b1e2e` | Brand-red nod; original footer PNG |

V3 reds from your palette: Wine `#58181F`, Ruby `#9B1E2E`, Romantic `#BD2734` (accent hover via Deep `#7C0D0E`). No `#FF0000` / highlighter reds in chrome.

## Files

```
site/css/
  themes.css         — V1 / V2 / V3 tokens (--color-chrome)
  footer-curve.css   — PNG (v3) + SVG curve (v1/v2)
site/assets/
  TDHHC_footer_lite.png — original curve band
  footer-curve.svg      — silhouette for non-red themes
  logo-white.png        — footer logo on dark/chrome bands
```

## EJC brand

When new brand CSS arrives, override `:root` tokens or add `themes/ejc.css`. HTML layout stays put.
