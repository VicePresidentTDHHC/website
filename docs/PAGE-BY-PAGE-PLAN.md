# TDHHC Page-by-Page Plan

Merged plan from:

- [`TDHHC_Page_by_Page_Analysis.docx`](TDHHC_Page_by_Page_Analysis.docx) (May 2026 HTML audit)
- [`REDESIGN-PROPOSAL.md`](REDESIGN-PROPOSAL.md)
- [`SITEMAP-AND-CONTENT.md`](SITEMAP-AND-CONTENT.md)
- [`CONTENT-VOICE.md`](CONTENT-VOICE.md)

This document is the **detailed build brief**. It adopts most audit findings but flags items where we **adapt** or **disagree** — see [Discussion: agree, adapt, push back](#discussion-agree-adapt-push-back).

---

## Severity legend

| Level | Meaning |
|-------|---------|
| **Critical** | Fix before launch; may affect trust, access, or security |
| **High** | Important for UX, SEO, or core tasks |
| **Medium** | Should fix in redesign; lower urgency on live site |
| **Low** | Nice to have |

---

## Discussion: agree, adapt, push back

Items worth talking through before build — not automatic yeses.

| Topic | Docx says | Our position |
|-------|-----------|--------------|
| **Interim WordPress fixes** | Phase 1–2 fixes on current Divi site (nav, meta, GA4) | **Agree** if the site stays live during rebuild. Skip sunk cost on Divi H1 settings if rebuild is &lt;8 weeks out. |
| **VP not visible** | "VP referenced but not clearly visible in source" | **Partially disagree.** Archive shows `tel:903-206-2210` in top bar on every page + footer. Real issue is **hierarchy** (VP should match voice prominence on Contact), not absence. |
| **No H1/H2 on any page** | No semantic headings found | **Adapt.** Interpreter/events pages use `<h2>` in Divi modules; problem is **missing H1** and inconsistent hierarchy, not zero headings. About has **no content headings** (blank page). |
| **Cognito / interpreter form** | "Add a web form" (low priority) | **Disagree — form exists.** Cognito embed is on interpreter page. Improve placement and UX; don't add a second form. |
| **Sogo accessibility overlay** | Remove; overlays criticized by advocates | **Strongly agree.** Build WCAG into the theme; optional enhancement only. Target **WCAG 2.2 AA** (doc says 2.1). |
| **Nav: title case labels** | "About Us", "Board of Directors", etc. | **Adapt.** Title case beats ALL CAPS, but **new IA replaces nav** (Our Services, Support Us, etc.) — don't invest in renaming old menu. |
| **Donate meta description** | "Your donation makes a difference" | **Push back on voice.** Conflicts with [CONTENT-VOICE.md](CONTENT-VOICE.md). Use factual copy: what donations fund, 501(c)(3). |
| **Volunteer testimonials** | Add quotes to increase sign-ups | **Agree with care.** Community voices yes; avoid inspiration/pity framing. |
| **Phase 4: lightweight theme replacement** | Stay on WordPress, lighter theme | **Adapt — go further.** Full static rebuild on reliable hosting, not Divi theme swap. Same goals, more durable fix. |
| **Security: remove generator meta** | Low priority obscurity | **Agree it's low.** Real wins: no xmlrpc, no ghost emails, modern host, HTTPS. |
| **Events Calendar WP plugin** | Use The Events Calendar plugin | **Interim only.** New site: CMS-managed structured events (already planned). |
| **Phone format** | Standardize `(903) 617-6204` | **Agree.** Use `tel:+19036176204` and `tel:+19032062210` in HTML. |
| **Physical address / map** | Add map on Contact | **Confirmed:** 1828 ESE Loop 323, Suite LL-14 ([Tyler Paper](https://tylerpaper.com/2026/03/10/tyler-deaf-and-hard-of-hearing-center-connects-services-advocacy-and-connection-across-east-texas/), Navigate Life Texas). 1530 SSW was incorrect/outdated. |
| **nick@ ghost link** | On 8+ pages | **Confirmed: 10 of 11 pages** (all except blank `about.html` footer template instance). Remove everywhere. |

---

## Part 1 — Sitewide (all pages)

Apply in **new build** globally. Interim fixes on live WordPress where noted.

| Sev | Issue | Fix | Interim WP? |
|-----|-------|-----|-------------|
| Critical | `user-scalable=0` / `maximum-scale=1.0` blocks pinch-zoom | Standard viewport only | Yes — theme settings or child theme |
| Critical | UA analytics `UA-129587592-4` dead since 2023 | GA4 or Plausible | Yes |
| Critical | Ghost `mailto:nick@ImperiousExpo.com` in footer | Remove from theme/footer module | Yes — search in WP admin |
| High | No meta descriptions | Unique 150–160 char description per page | Yes if staying live |
| High | Missing **H1** per page; weak heading hierarchy | One H1 per page; logical H2→H3 | New build (skip Divi module tuning if rebuilding soon) |
| High | Duplicate Font Awesome v4 + v5 | Single FA6 subset or SVG icons | New build |
| High | Sogo overlay as accessibility strategy | Native contrast, type scale, semantics | New build |
| Medium | Divi version in HTML | N/A after rebuild | — |
| Medium | `xmlrpc.php` pingback in `<head>` | Disable XML-RPC if unused | Yes |
| Medium | RSS feed links (not a blog) | Omit on static site | New build |
| Low | Generator meta / admin-ajax exposure | Low priority | Optional |

### Voice constraint (all pages)

Audit meta descriptions and body copy against [CONTENT-VOICE.md](CONTENT-VOICE.md). Reject patronizing filler even when suggested in the docx (e.g. "makes a difference," "here to help").

---

## Part 2 — Navigation

### Docx findings (current site)

| Sev | Issue | New-build resolution |
|-----|-------|----------------------|
| Critical | Places of Worship not in nav | Under **Resources → Places of Worship** |
| Critical | Calendar orphaned | Merge with **Our Services → Events & Calendar** |
| High | ALL CAPS nav labels | New nav: title case, intent-based (5 items) |
| Medium | "B.O.D." unclear | **About → Board of Directors** |

### Target navigation (unchanged from redesign plan)

```
Our Services · About · Support Us · Resources · Contact
```

---

## Part 3 — Page-by-page

For each page: **audit issues** → **new URL** → **build decisions** → **voice notes**.

---

### 1. Home

**Current:** `tdhhc.org/`  
**New:** `/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Title tag ~140 chars | `Tyler Deaf and Hard of Hearing Center \| East Texas` (~50 chars) |
| Critical | No meta description | Factual, non-patronizing (see voice) |
| Critical | No primary CTA | **Request an Interpreter** above fold |
| High | Donation competes with mission | Donate under Support Us pathway, not hero |
| High | Empty alt on promo images | Descriptive alt or replace images |
| High | Events as screenshot PNG | Structured event cards |
| Medium | "Curious about…" / "hope you enjoy" | Rewrite per CONTENT-VOICE |
| Medium | VP visibility | Keep top-bar `tel:` VP; equal weight with voice in header/footer |

**Proposed meta description:**  
"TDHHC provides interpreter services, advocacy, and resources for Deaf, Hard of Hearing, and DeafBlind communities in East Texas."

**H1:** Tyler Deaf and Hard of Hearing Center — or community-focused headline from voice guide.

**Sections:** Hero + ASL video · Primary CTA · Three pathways (Services / Resources / Support) · News · Testimonials · Events.

---

### 2. About

**Current:** `tdhhc.org/about/` — **body is empty**  
**New:** `/about/` (Mission & History)

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Blank content | **New copy required** — mission, founded 2012, 501(c)(3), service area |
| Critical | Title "ABOUT" all caps | `About \| Tyler Deaf and Hard of Hearing Center` |
| High | No H1 | H1: About TDHHC |
| Medium | Should link to board | Link to `/about/board/` |

**Voice:** Factual mission statement. No "passionate leaders" clichés on board cross-link.

---

### 3. Board of Directors

**Current:** `tdhhc.org/b-o-d/`  
**New:** `/about/board/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Title "B.O.D." | `Board of Directors \| TDHHC` |
| Critical | nick@ in footer | Remove |
| High | Plain list layout | Card/grid with names + roles; photos if available |
| Medium | Stale listings | Verify against Feb 2026 archive; process to update |

**Content ready** from archive. Rewrite board intro — drop "voices are heard" language.

**H1:** Board of Directors

---

### 4. Calendar

**Current:** `tdhhc.org/calendar/` (orphaned)  
**New:** `/services/events/#calendar` or embedded on Events page

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Not in nav | Merged under Our Services → Events |
| Critical | Zoho iframe; mobile zoom blocked | Evaluate Google Calendar or CMS events; responsive embed |
| High | Unclear vs Events page | **One destination:** featured events + full calendar |

**H1:** Events & Calendar (on combined page)

---

### 5. Contact

**Current:** `tdhhc.org/contact/`  
**New:** `/contact/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Patronizing intro | "Contact TDHHC by VP, voice, email, or the form below." |
| High | VP should be first contact method | **VP listed before voice** in contact block |
| High | Phone format inconsistency | `(903) 206-2210` VP · `(903) 617-6204` voice · `tel:` links |
| High | Map / address | Embed map **after** canonical address confirmed |
| Medium | Form placeholder patronizing | "Your message" not "what we can help you with" |
| Medium | Office hours | Add if staff provides |

Replace Divi form with Formspree, Netlify Forms, or Cognito.

**H1:** Contact

---

### 6. Donate

**Current:** `tdhhc.org/donate/`  
**New:** `/support/donate/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Dead analytics = no conversion tracking | GA4 conversion events on Zeffy click/completion |
| High | Verify Zeffy flow | Test donate + sponsorship + wishlist links |
| Medium | Impact of giving ($25/$50/$100) | **Factual** impact breakdown — not emotional manipulation |
| Medium | 501(c)(3) trust signal | Prominent tax-exempt status |
| Low | Recurring giving | If Zeffy supports it |

**Voice:** Remove "life blood," "generous donation," excessive thanks.

**H1:** Donate

---

### 7. Events

**Current:** `tdhhc.org/events/`  
**New:** `/services/events/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Events as image screenshots | CMS structured events |
| High | Title inconsistency | `Events \| TDHHC` |
| Medium | Stale manual updates | CMS workflow + owner |
| Low | ASL/CART per event | Field: `accessibility_notes` on each event |

**H1:** Events

---

### 8. Interpreter Services

**Current:** `tdhhc.org/interpreter-services/`  
**New:** `/services/interpreters/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | No meta description | Include VP + request action |
| High | Text wall; WPBakery in Divi | Clean layout; form-left + coordinator card |
| High | Cognito form overlooked in audit | **Keep** Cognito embed at `#request` |
| High | tap-to-call on 903-206-2210 | `tel:+19032062210` on all instances |
| Medium | How-to-request steps | Numbered steps above form |
| Medium | ADA value prop | Plain-language business section |
| Medium | Rates vague | Rate table or PDF — staff decision |
| Medium | "Here to help" filler | Replace with direct coordinator contact |
| Low | Signing photo empty alt | Alt text or remove |

**Audience split:** Businesses (request + pay + ADA) vs Deaf individuals (access advocacy) — separate sections.

**H1:** Interpreter Services  
**Page-top CTA:** Request an Interpreter → `#request`

---

### 9. Places of Worship

**Current:** `tdhhc.org/places-of-worship/` (isolated)  
**New:** `/resources/places-of-worship/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Critical | Invisible to users | Nav under Resources + link from Resources hub |
| High | High community value | Optional feature card on home Resources pathway |
| Medium | Structured listing fields | Address, times, interpreted vs ASL, city filter |
| Low | Congregation submissions | Form to suggest listings |

**Content ready** from archive (Tyler/Longview churches, New Beginnings Deaf Fellowship).

**H1:** Places of Worship

---

### 10. Resources

**Current:** `tdhhc.org/resources/`  
**New:** `/resources/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| High | No link to Places of Worship | Prominent internal link |
| Medium | Link rot on externals | Audit before launch; `rel="noopener"` on external |
| Medium | Flat list | Categories: News, Local Services, National Orgs, Interpreting, Training, Worship |
| Low | "Helpful resources" filler intro | Direct intro per voice guide |

**H1:** Resources

---

### 11. Volunteer

**Current:** `tdhhc.org/volunteer/`  
**New:** `/support/volunteer/`

| Sev | Audit issue | Build decision |
|-----|-------------|----------------|
| Medium | Vague opportunities | Structured roles + ASL requirements |
| Medium | No application path | Email CTA or simple form |
| Low | Volunteer quotes | Only if authentic; no pity framing |

**H1:** Volunteer

**Note:** Archive says applications open when posted — state that plainly.

---

## Part 4 — Prioritized action list

### Track A — Live site (if it stays up during rebuild)

From docx Phase 1–2; do in one WP session where possible:

1. Remove `nick@ImperiousExpo.com` from footer theme module
2. Add Places of Worship + Calendar to nav **or** accept they're hidden until launch
3. Replace UA with GA4
4. Fix viewport meta (allow zoom)
5. Add meta descriptions (voice-reviewed)
6. Test Zeffy donation flow and contact form delivery

**Skip if rebuild launches within ~8 weeks:** Divi H1 retagging, nav label renames, Font Awesome cleanup.

### Track B — New site build (primary)

1. Global shell: semantics, VP/voice, meta, analytics, no ghost links
2. Interpreter Services (highest traffic)
3. Home
4. Support Us + Resources (incl. Places of Worship)
5. About + Board
6. Events CMS
7. Contact + legal pages
8. 301 redirects from all 11 old URLs
9. Voice pass ([CONTENT-VOICE.md](CONTENT-VOICE.md))
10. Accessibility audit (WCAG 2.2 AA)

---

## Part 5 — Confirmed contact info

| Channel | Value | Display rule |
|---------|-------|--------------|
| Video Phone | (903) 206-2210 | `tel:+19032062210` — **equal prominence to voice** |
| Voice | (903) 617-6204 | `tel:+19036176204` |
| Email | coordinator@tdhhc.org | mailto link |
| Mailing | P.O. Box 6134, Tyler, TX 75711 | Footer |
| Physical | **Staff to confirm** | 1828 ESE Loop 323, Suite LL-14 vs 1530 SSW Loop 323, Suite 114 |

**Remove:** nick@ImperiousExpo.com everywhere.

---

## Part 6 — Issue scorecard

| Source | Critical | High | Medium | Low |
|--------|----------|------|--------|-----|
| Docx audit | 31 | 22 | 18 | 12 |
| Addressed in new plan | All critical sitewide + per-page | Most via rebuild | Scheduled | Backlog |

New issues from our analysis **not in docx:** patronizing voice sitewide, WPBakery markup on interpreter page, address conflict, blank About body.

---

## Related documents

| Doc | Role |
|-----|------|
| [TDHHC_Page_by_Page_Analysis.docx](TDHHC_Page_by_Page_Analysis.docx) | Original HTML audit |
| [REDESIGN-PROPOSAL.md](REDESIGN-PROPOSAL.md) | Strategy, IA, architecture |
| [SITEMAP-AND-CONTENT.md](SITEMAP-AND-CONTENT.md) | URLs, integrations, build order |
| [CONTENT-VOICE.md](CONTENT-VOICE.md) | Tone constraint |

---

*Last updated: May 29, 2026*
