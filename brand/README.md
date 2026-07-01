# TDHHC brand kit (Eastland Jones Creative)

Source: `TDHHC branding.zip` — logos, fonts, and color reference for the redesign.

## Contents

| Path | Description |
|------|-------------|
| `TDHHC-cheatsheet.jpg` | Brand colors, typography, logo usage |
| `TDHHC.afpalette` | Affinity Designer palette |
| `fonts/` | Erstoria (display), Optima (body) — **check licensing before web embedding** |
| `logo/png/` | All logo variants (@3x PNG) |
| `logo/svg/` | All logo variants (SVG) |

## Logo naming

| Pattern | Use |
|---------|-----|
| `wide` | Header / horizontal lockup |
| `stacked` | Narrow columns, social |
| `medallion` | Square / avatar contexts |
| `icon` | Favicon, app icon |
| `color-dark` | Light backgrounds |
| `color-light` | Dark backgrounds (footer chrome) |
| `mono-*` | Single-color print / restricted use |

## Site deploy copies

These files in [`www/assets/`](../www/assets/) are copied from this kit for the mock-up:

- `logo.svg` / `logo.png` — wide color dark (header)
- `logo-white.svg` / `logo-white.png` — wide color light (footer)
- `favicon.svg` / `favicon.png` — icon color dark
- `logo-mark.svg` / `logo-mark-navy.svg` — cropped lockup (icon + TDHHC, no subtitle); navy variant for V2 theme

Header tagline (“Tyler Deaf & Hard of Hearing Center”) is HTML text beside the mark — see `build-logo-mark.py` to regenerate marks from the brand SVG.

## Web typography (mock-up)

Erstoria is self-hosted in [`www/assets/fonts/`](../www/assets/fonts/) and loaded via [`www/css/fonts.css`](../www/css/fonts.css):

- **H1 / hero titles** — Erstoria (40px max)
- **H2** — Atkinson Hyperlegible bold (32px; stands in for Optima until web license)
- **Body** — Atkinson Hyperlegible (16px)
- **`.callout`** — Erstoria uppercase (24px)

Confirm web embedding rights with EJC before production launch.

## Logo naming
