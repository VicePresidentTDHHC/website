# Visual themes (V1, V2, V3)

Themes are **CSS-only** — swap with the **Look:** buttons in the preview banner.

## Ground rules

1. **Themes are options, not requirements.**
2. **Footer curve:** SVG on all three themes (same shape), filled with `--color-footer-bg` (= `--color-chrome`).
3. **High contrast** for low vision: Atkinson Hyperlegible, dark body text, bold headings.
4. **Top and bottom match** via `--color-chrome` per theme.
5. **Links are not red** on Navy or Wine — `--color-link` is blue; red is chrome/buttons only on Wine.
6. **True alarm red** stays on `.notice--alert` only.

## Themes

| Theme | Chrome | Links | Buttons (accent) |
|-------|--------|-------|------------------|
| **V1 Slate** | `#2d2a28` | Teal `#0c5c6e` | Teal |
| **V2 Navy** | `#0f172a` | Blue `#1d4ed8` | Navy buttons; gold on hero |
| **V3 Wine** | `#58181f` | Blue `#1e40af` | Romantic `#BD2734` |

Wine footer/contact links on chrome: white text, gold link color `#fde68a`.

## Files

```
site/css/themes.css       — tokens including --color-link
site/css/footer-curve.css — SVG curve (all themes)
site/assets/footer-curve.svg
```
