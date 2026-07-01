# TDHHC Website Redesign

Project workspace for rebuilding [tdhhc.org](https://tdhhc.org/) — the Tyler Deaf and Hard of Hearing Center.

## Contents

| Path | What it is |
|------|------------|
| [`www/`](www/) | **Current website** — board preview mock-up; deploy this folder |
| [`brand/`](brand/) | **Brand kit** — EJC logos (SVG/PNG), fonts, color cheatsheet |
| [`archive/`](archive/) | Original WordPress site snapshot (May 2026) — HTML, logos, metadata only |
| [`content/`](content/) | WordPress content exports (markdown) used when writing new copy |
| [`reference/`](reference/) | Extracted Divi CSS and other build references |
| [`docs/`](docs/) | Redesign plans, sitemap, voice guidelines |

Key docs: [`docs/REDESIGN-PROPOSAL.md`](docs/REDESIGN-PROPOSAL.md) · [`docs/SITEMAP-AND-CONTENT.md`](docs/SITEMAP-AND-CONTENT.md) · [`docs/PAGE-BY-PAGE-PLAN.md`](docs/PAGE-BY-PAGE-PLAN.md)

## Status

**Board preview** in [`www/`](www/) — open `www/index.html` or run `python -m http.server 8080` inside `www/`.

Netlify/Cloudflare: publish directory is `www` (see `netlify.toml`).
