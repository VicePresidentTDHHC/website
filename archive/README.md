# TDHHC.org Site Archive

Snapshot of [tdhhc.org](https://tdhhc.org/) captured **May 29, 2026** before a planned redesign and hosting migration.

## What was archived

| Path | Description |
|------|-------------|
| `raw/*.html` | Full HTML source for every public WordPress page (11 pages) |
| `content/*.md` | Page content exported via WordPress REST API |
| `assets/` | Key logos and favicon from the live site |
| `wp-pages.json` | Page metadata (slug, URL, last modified) |

## Pages captured

| Slug | URL | In main nav? | Last modified |
|------|-----|--------------|---------------|
| home | https://tdhhc.org/ | Yes | 2026-03-27 |
| about | https://tdhhc.org/about/ | Yes | 2025-08-19 |
| volunteer | https://tdhhc.org/volunteer/ | Yes (under About) | 2023-05-13 |
| b-o-d | https://tdhhc.org/b-o-d/ | Yes (under About) | 2026-02-17 |
| interpreter-services | https://tdhhc.org/interpreter-services/ | Yes | 2025-11-18 |
| donate | https://tdhhc.org/donate/ | Yes | 2026-02-17 |
| resources | https://tdhhc.org/resources/ | Yes | 2026-02-17 |
| contact | https://tdhhc.org/contact/ | Yes | 2025-11-17 |
| events | https://tdhhc.org/events/ | Yes | 2026-03-27 |
| calendar | https://tdhhc.org/calendar/ | No (orphaned) | 2023-05-14 |
| places-of-worship | https://tdhhc.org/places-of-worship/ | No (orphaned) | 2023-05-14 |

## Current tech stack (from HTML analysis)

- **CMS:** WordPress 7.0
- **Theme:** Divi 4.19.2 (Elegant Themes page builder)
- **Accessibility plugin:** Sogo Accessibility 1.0.5
- **Forms:** Divi contact form (contact page), Cognito Forms (interpreter requests)
- **Analytics:** Google Analytics UA-129587592-4 (legacy Universal Analytics)
- **Brand color:** `#d7282f` (red accent)

## Third-party integrations to preserve

| Service | Used for | URL / embed |
|---------|----------|-------------|
| Zeffy | Online donations | `zeffy.com/en-US/donation-form/donate-to-tdhhc` |
| Zeffy | Sponsorship | `zeffy.com/en-US/ticketing/sponsorship-opportunities-22` |
| Zeffy | Email newsletter signup | `zeffy.com/.../subscribe-to-tyler-deaf-and-hard-of-hearing-centers-monthly-newsletter` |
| Zeffy | Paper newsletter signup | `zeffy.com/.../subscribe-to-tdhhcs-paper-monthly-newsletter` |
| Amazon | Wishlist | `amazon.com/hz/wishlist/ls/1XOKWYVUJEUCI` |
| Cognito Forms | Interpreter request form | `cognitoforms.com` (key: `RUV9PohCIkqzMCpW5J2vsQ`, form 1) |
| Zoho Calendar | Community calendar embed | `calendar.zoho.com` iframe on `/calendar/` |
| Facebook | Community group | `facebook.com/groups/295002970853564` |

## Contact information (from site footer)

- **Address:** 1828 ESE Loop 323, Suite LL-14, Tyler, TX 75701
- **Mailing:** P.O. Box 6134, Tyler, TX 75711
- **Video Phone:** 903.206.2210
- **Office Phone:** 903.617.6204
- **Email:** coordinator@tdhhc.org

## Known issues at time of archive

- **Ghost email in sitewide footer:** empty `<a href="mailto:nick@ImperiousExpo.com"></a>` on every page — remove before launch
- **Address needs reconciliation:** archive footers use `1828 ESE Loop 323, Suite LL-14`; live homepage review also cited `1530 SSW Loop 323, Suite 114` — staff must confirm
- `/about/` page body is **completely empty** (blank Divi layout)
- `/sitemap.xml` returns HTTP 500
- Events are published as **screenshot images** rather than structured data
- `/places-of-worship/` has full content but Resources page says "coming soon"
- `/calendar/` exists but is not linked in navigation (Events page is separate)
- Home page promo image filename typo: `Oue_Services-min.jpg` (should be "Our")
- `user-scalable=0` in viewport meta tag blocks pinch-to-zoom (accessibility concern)

## Re-capturing later

```powershell
# Re-download all pages
$pages = @{ "home"="https://tdhhc.org/"; "about"="https://tdhhc.org/about/"; ... }
foreach ($entry in $pages.GetEnumerator()) {
  Invoke-WebRequest -Uri $entry.Value -OutFile "archive/raw/$($entry.Key).html"
}
```
