# TDHHC.org Redesign Proposal

A plan to rebuild the Tyler Deaf and Hard of Hearing Center website on reliable hosting, using the new Eastland Jones Creative logo, and following modern nonprofit and accessibility best practices.

---

## Executive summary

The current site runs on WordPress + Divi on an unreliable host. Content is spread across 11 pages with two orphaned pages, one blank page (`/about/`), events posted as screenshots, and several third-party embeds (Zeffy, Cognito Forms, Zoho Calendar) that must be carried forward.

**Recommended direction:** Rebuild as a **fast, accessible static or headless site** on dependable hosting (Vercel, Netlify, or Cloudflare Pages), with a simple CMS layer for staff to update events and news without touching code. Integrate the new logo and a Deaf-community-first design system.

---

## Current state assessment

### What works well

- Clear top-bar CTAs: **Call for Interpreter** and **Video Phone**
- Strong interpreter services page with policy details and coordinator contact
- Donation flow via Zeffy (no platform fees for nonprofits)
- Sogo accessibility toolbar (contrast, font size, stop motion)
- Board of Directors page is current (updated Feb 2026)
- Resources page has a useful curated link directory

### Critical problems

| Issue | Impact |
|-------|--------|
| **About page is blank** | Visitors learn nothing about TDHHC's mission, history, or team |
| **Unreliable hosting** | Downtime, sitemap 500 errors, migration risk |
| **Events as PNG screenshots** | Not searchable, not accessible, not mobile-friendly, hard to maintain |
| **Orphaned pages** | `/calendar/` and `/places-of-worship/` exist but aren't in navigation |
| **"Coming soon" on Resources** | Worship list exists on a hidden page |
| **Heavy WordPress/Divi stack** | Slow loads, large HTML, plugin dependency, security surface |
| **Legacy Google Analytics (UA)** | UA stopped processing in 2024; no current analytics |
| **Zoom disabled** | `user-scalable=0` violates WCAG |
| **No ASL video content** | Missed opportunity for primary audience |
| **No structured services page** | Services mentioned on home/resources but never detailed |

---

## Proposed information architecture

Simplify navigation while surfacing hidden content:

```
HOME
├── About
│   ├── Our Story & Mission      ← NEW (replaces blank About page)
│   ├── Board of Directors       ← existing B.O.D. content
│   └── Volunteer                ← existing
├── Services                     ← NEW dedicated section
│   ├── Interpreter Services     ← existing (primary revenue/service)
│   ├── Community Programs       ← literacy, STAP, DHHS outreach
│   └── For Businesses (ADA)     ← entity-focused interpreter info
├── Resources
│   ├── Helpful Links            ← existing curated list
│   ├── Places of Worship        ← move from orphaned page
│   └── College & Training       ← TJC ITP, interpreter training
├── Events & Calendar            ← merge Events + Calendar
├── Donate
└── Contact
```

**Retire or redirect:** `/calendar/` → `/events/`, `/b-o-d/` → `/about/board/`

---

## Design recommendations

### 1. Deaf-first, accessibility-led design

This audience should drive every decision—not be an afterthought.

- **WCAG 2.2 AA minimum** (aim for AAA on contrast for body text)
- **ASL welcome video** on homepage hero (with captions and transcript)
- **Persistent VP button** — sticky "Video Phone" FAB on mobile, always visible
- **No autoplay** audio/video; respect `prefers-reduced-motion`
- **Allow zoom** — remove `user-scalable=0`
- **Semantic HTML** — proper headings, landmarks, skip links
- **Keyboard navigation** — all menus, forms, and modals fully operable
- **Built-in accessibility** — prefer native CSS (contrast modes, font scaling) over third-party toolbar plugins where possible; keep toolbar as optional enhancement
- **Plain language** — short sentences, scannable headings, glossary for acronyms (ADA, BEI, RID, STAP, DHHS)

### 2. New brand integration (Eastland Jones Creative logo)

- Request logo files in **SVG + PNG** (full color, reversed/white, icon-only)
- Define a small design token set:
  - Primary: new brand color(s) from logo
  - Accent: keep recognizable red `#d7282f` if it remains in new brand, or migrate gracefully
  - Neutral palette for high contrast
  - Typography: one readable sans-serif (e.g., **Source Sans 3**, **Inter**, or **Atkinson Hyperlegible**—designed for low vision)
- **Do not** use text-in-images for headings (current events screenshots)

### 3. Homepage layout (wireframe concept)

```
┌─────────────────────────────────────────────────────┐
│  VP: 903-206-2210  |  Voice: 903-617-6204  |  Email  │
├─────────────────────────────────────────────────────┤
│  [Logo]     About  Services  Resources  Events  ... │
├─────────────────────────────────────────────────────┤
│  HERO: Mission statement + ASL video thumbnail      │
│  [Request Interpreter]  [Contact Us]  [Donate]      │
├─────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │Interpret │ │ Resources│ │  Donate  │            │
│  │ Services │ │ & Links  │ │  Support │            │
│  └──────────┘ └──────────┘ └──────────┘            │
├─────────────────────────────────────────────────────┤
│  UPCOMING EVENTS (structured cards, not screenshots) │
├─────────────────────────────────────────────────────┤
│  Footer: address, VP, social, 501(c)(3) notice      │
└─────────────────────────────────────────────────────┘
```

### 4. Mobile-first

Most community members will visit on phones. Prioritize:

- Tap targets ≥ 44×44px
- Click-to-call and click-to-VP links
- Hamburger menu with clear labels (not "Select Page")
- Fast load on 4G (< 3s LCP)

---

## Technical architecture options

### Option A — Recommended: Static site + headless CMS

| Layer | Suggestion |
|-------|------------|
| Framework | **Astro** or **Next.js** (static export) |
| CMS | **Sanity**, **Decap CMS** (Git-based), or **WordPress headless** if staff prefer familiar WP admin |
| Hosting | **Cloudflare Pages** or **Netlify** (generous free tier, global CDN, 99.9%+ uptime) |
| Forms | Keep **Cognito Forms** embed or migrate to **Formspree** / **Netlify Forms** |
| Donations | Keep **Zeffy** embeds (already zero-fee) |
| Calendar | Replace Zoho iframe with **Google Calendar embed**, **Zeffy events**, or CMS-managed events |
| Analytics | **Plausible** or **Google Analytics 4** (privacy-respecting) |

**Pros:** Fast, secure, cheap, portable, no WordPress maintenance  
**Cons:** Staff need brief CMS training

### Option B: Modern WordPress on managed hosting

| Layer | Suggestion |
|-------|------------|
| Host | **WP Engine**, **Kinsta**, or **Cloudways** |
| Theme | Lightweight block theme (not Divi)—**Twenty Twenty-Five** or custom block theme |
| Builder | Native Gutenberg blocks only |

**Pros:** Familiar editing for staff already used to WordPress  
**Cons:** Ongoing plugin/theme updates, higher cost, still heavier than static

### Option C: Fully managed nonprofit platform

Platforms like **Neon One**, **Bloomerang**, or **CharityStack** bundle CRM + donations + events.

**Pros:** All-in-one  
**Cons:** Monthly cost, less design flexibility, may not fit interpreter-service workflows

**Our recommendation: Option A** for reliability and performance, with Decap CMS or Sanity for easy event/news updates.

---

## Content improvements

### About page (currently blank) — draft outline

Staff should fill in, but the page needs:

1. **Mission statement** — "comprehensive services for deaf, hard of hearing, and deaf-blind people"
2. **Founded 2012** — 501(c)(3) nonprofit
3. **Service area** — East Texas
4. **One-stop shop** vision (quoted from current home page)
5. **Photo** of center, staff, or community event
6. **ASL video** introduction from coordinator or board member

### Services page (new)

Break out what the home page mentions in passing:

- Interpreter services (link to full page)
- Adult literacy classes
- STAP / telephone equipment assistance (link to Texas HHSC)
- Deaf & Hard of Hearing Access Specialist program
- Mentoring / shadowing for student interpreters

### Events (replace screenshots)

Move from static images to structured events:

```yaml
- title: "April Community Meetup"
  date: 2026-04-15
  time: "6:00 PM"
  location: "TDHHC Office"
  description: "..."
  asl_interpreter_available: true
```

Display as accessible cards with `.ics` download / "Add to Calendar" links.

### Places of worship

Merge the full `/places-of-worship/` content into Resources. Add filter by city (Tyler, Longview) and service type (interpreted vs. ASL).

### Interpreter services

- Keep Cognito form embed
- Add FAQ accordion (billing, cancellation, certification levels)
- Prominent note: **"Entities request interpreters, not individual clients"** (already stated—make it unmissable)
- Add downloadable rate sheet PDF if appropriate

---

## SEO and discoverability

- Unique `<title>` and meta description per page
- LocalBusiness + NGO **structured data** (JSON-LD) with address, VP, hours
- Google Business Profile sync
- XML sitemap (auto-generated on static hosts)
- `robots.txt` and canonical URLs
- Alt text on all images (many currently empty, e.g. `alt=""` on home promos)

---

## Security and compliance

- **HTTPS** everywhere (Let's Encrypt via host)
- **HIPAA awareness** — interpreter requests may contain appointment details; ensure Cognito Forms encryption and privacy policy are current
- **ADA compliance** for the website itself (ironically critical for this organization)
- **Privacy policy** and **accessibility statement** pages (missing today)
- Remove unused WordPress attack surface (`xmlrpc.php` was exposed on old site)

---

## Migration plan (phased)

### Phase 1 — Foundation (weeks 1–2)
- [x] Archive current site (done — see `archive/`)
- [ ] Collect new logo assets from Eastland Jones Creative
- [ ] Confirm hosting choice
- [ ] Draft About page content with TDHHC staff
- [ ] Inventory all Zeffy/Cognito/Zoho account credentials

### Phase 2 — Build (weeks 3–5)
- [ ] Set up repo, design tokens, component library
- [ ] Build pages from archived content
- [ ] Integrate forms, donations, calendar
- [ ] Add ASL video(s) and accessibility features
- [ ] 301 redirects from all old URLs

### Phase 3 — Review (week 6)
- [ ] Accessibility audit (WAVE, axe, manual screen reader test)
- [ ] Staff CMS training
- [ ] Board/stakeholder review

### Phase 4 — Launch
- [ ] DNS cutover (low-traffic window)
- [ ] Monitor analytics and form submissions
- [ ] Decommission old host after 30-day parallel run

---

## Estimated ongoing costs

| Item | Approx. monthly |
|------|-----------------|
| Cloudflare Pages / Netlify | $0–$20 |
| Domain (tdhhc.org) | ~$1–2 (annual amortized) |
| CMS (Sanity free tier / Decap) | $0 |
| Zeffy donations | $0 platform fee |
| Cognito Forms | $0–$15 depending on volume |
| Analytics (Plausible) | $0–$9 |
| **Total** | **~$0–$50/mo** vs. unreliable shared hosting |

---

## Quick wins (can do immediately)

1. **Fix the blank About page** on current site while redesign is in progress
2. **Add Places of Worship** link to Resources (content already exists)
3. **Link Calendar** from Events page
4. **Replace UA analytics** with GA4
5. **Remove `user-scalable=0`** from viewport meta tag
6. **Add alt text** to homepage promo images

---

## Next steps

1. Review this proposal with TDHHC board and Eastland Jones Creative
2. Choose architecture (we recommend **Option A: Astro + Cloudflare Pages**)
3. Provide new logo files and any brand guidelines
4. Schedule a content workshop to fill the About page and Services section
5. Begin Phase 2 build in this repository

---

*Prepared from site archive captured May 29, 2026. Source: [tdhhc.org](https://tdhhc.org/)*
