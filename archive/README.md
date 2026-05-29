# TDHHC.org Site Archive

Frozen snapshot of [tdhhc.org](https://tdhhc.org/) as it existed on **WordPress/Divi**, captured **May 29, 2026** before redesign and hosting migration.

**This folder is read-only history.** The new site is in [`../www/`](../www/). Migration copy is in [`../content/`](../content/).

## What is archived here

| Path | Description |
|------|-------------|
| `raw/*.html` | Full HTML source for every public WordPress page (11 pages) |
| `assets/` | Logos and favicon from the live site |
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

## Original tech stack (from HTML)

- **CMS:** WordPress 7.0
- **Theme:** Divi 4.19.2
- **Forms:** Divi contact form, Cognito Forms (interpreter requests)
- **Brand color:** `#d7282f`

See [`../reference/divi-css/`](../reference/divi-css/) for CSS extracted during the redesign (not part of this snapshot).

## Re-capturing later

```powershell
$pages = @{ "home"="https://tdhhc.org/"; "about"="https://tdhhc.org/about/"; ... }
foreach ($entry in $pages.GetEnumerator()) {
  Invoke-WebRequest -Uri $entry.Value -OutFile "archive/raw/$($entry.Key).html"
}
```
