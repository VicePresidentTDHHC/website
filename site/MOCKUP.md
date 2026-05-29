# TDHHC Board Preview Mock-up

Static HTML preview of the redesigned tdhhc.org for board review. **Not connected to the live site.**

## Purpose

Demonstrate scope and quality of an in-house rebuild vs. the ~$5,000 redesign quote — without fixing the failing WordPress host.

## View locally

```powershell
cd site
python -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080)

Or open `site/index.html` directly in a browser (relative links work).

## Deploy for board (free)

Push to GitHub and connect **Netlify** or **Cloudflare Pages**:

- **Build command:** (none)
- **Publish directory:** `site`

The repo includes `netlify.toml` for one-click Netlify deploy.

## What's included

| Page | Path |
|------|------|
| Home | `/index.html` |
| Interpreter Services | `/services/interpreters.html` |
| Events & Calendar | `/services/events.html` |
| About | `/about/index.html` |
| Board (names only) | `/about/board.html` |
| Donate (factual tiers — draft) | `/support/donate.html` |
| Volunteer | `/support/volunteer.html` |
| Newsletter | `/support/newsletter.html` |
| Resources | `/resources/index.html` |
| Places of Worship | `/resources/places-of-worship.html` |
| Contact | `/contact.html` |

## What's placeholder

- Cognito interpreter form (box on interpreters page)
- Contact form
- Calendar embed
- Sample events
- Donation impact tiers (marked draft — staff to confirm)
- About mission copy (draft)
- Current logo from archive (new EJC logo when available)
- No ASL video yet

## Confirmed facts used

- **Address:** 1828 ESE Loop 323, Suite LL-14, Tyler, TX 75701 ([Tyler Morning Telegraph](https://tylerpaper.com/2026/03/10/tyler-deaf-and-hard-of-hearing-center-connects-services-advocacy-and-connection-across-east-texas/), tdhhc.org, Navigate Life Texas)
- **VP:** (903) 206-2210 · **Voice:** (903) 617-6204
- **No** `nick@ImperiousExpo.com` ghost link
- **No** patronizing copy per `docs/CONTENT-VOICE.md`

## Production next steps (after board approval)

1. New logo / brand from Eastland Jones Creative
2. Embed Cognito + Zeffy + real forms
3. CMS for events/news
4. Deploy to Cloudflare Pages / Netlify on tdhhc.org DNS
5. 301 redirects from old URLs
