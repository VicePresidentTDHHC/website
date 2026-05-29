# Visual themes (V1, V2, V3)

The mock-up uses **CSS custom properties** for all color and typography. Swapping the look is one file — no HTML changes.

## Try them

Use the **Look:** buttons in the top banner on any page. Choice is saved in `localStorage`.

| Theme | Personality | Accent | Best for |
|-------|-------------|--------|----------|
| **V1 Teal** | Warm slate + teal | `#0f766e` | Default — calm, trustworthy, clinical-but-human |
| **V2 Navy** | Navy + amber | `#b45309` | Bolder headers, gold accent stripe on cards |
| **V3 Forest** | Cream + forest green | `#2d6a4f` | Editorial serif headings, East Texas warmth |

## True red = alerts only

`--color-alert: #c62828` is used for `.notice--alert` (warnings). Buttons, links, and nav use `--color-accent` per theme — never alarm red.

See the donate page for a side-by-side draft notice (amber) vs alert notice (red).

## Curved bands (legacy shape, softer color)

The old Divi site used **wavy section dividers** and a **red footer band** (`#d7282f`). The mock-up keeps the **curve shape** but uses theme-specific **muted rose/terracotta** bands — a nod to the original brand without alarm red.

| Token | Role |
|-------|------|
| `--color-band` | Footer / CTA band background |
| `--color-band-soft` | Decorative blob behind content |
| `--color-band-text` | Text on bands |
| `--color-alert` | Warnings only — never bands |

| Theme | Band color | Character |
|-------|------------|-----------|
| **V1** | `#9b5a5c` | Dusty rosewood + teal buttons |
| **V2** | `#6b3a45` | Burgundy rose + amber buttons |
| **V3** | `#a67c6b` | Terracotta blush + forest buttons |

Waves and bands live in `shapes.css` (`.wave-divider`, `.site-band`, `.page-hero`).

## Files

```
site/css/
  main.css      ← imports base + themes + shapes
  base.css      ← layout & components (theme-agnostic)
  themes.css    ← V1 / V2 / V3 variable blocks
  shapes.css    ← waves, bands, page heroes
site/js/theme.js ← banner switcher
```

## When EJC delivers new brand

Add `themes/ejc.css` that overrides `:root` tokens — or tune one of V1–V3 to match. HTML stays put.
