# TDHHC.org Redesign Plan

Unified plan combining site archive findings, technical migration needs, and user-intent analysis. Goal: reorganize existing content around **who visits and why**, fill trust gaps, and rebuild on reliable hosting with the new Eastland Jones Creative brand.

---

## Guiding principle

**The bones are solid. The content is mostly there.** The redesign is primarily reorganization around user intent, a few missing trust-building pieces, refreshed visual identity, and dependable infrastructure.

Visitors fall into two very different groups:

| Audience | Primary goal | Nav home |
|----------|--------------|----------|
| **People who need services** | Interpreter, caseworker help, programs, resources | **Our Services** |
| **People who want to support** | Donate, volunteer, stay connected | **Support Us** |

Navigation should reflect that split immediately — not make visitors hunt through equal-weight menu items.

---

## Current state (from archive, May 2026)

### What works

- Interpreter services page has strong policy and coordinator contact detail
- Donation flow via Zeffy (zero platform fee for nonprofits)
- Curated resources link directory
- Board of Directors page is current
- Top bar already surfaces interpreter and VP links

### What blocks the redesign from succeeding as-is

| Issue | Impact |
|-------|--------|
| **Flat nav with too many equal-weight items** | Service seekers and supporters get the same menu — no intent-based path |
| **About page is blank** | No mission, history, or institutional trust |
| **Homepage buries critical info** | Donation ask competes with mission; interpreter contact not dominant |
| **VP treated as secondary** | Deaf visitors must dig; voice number gets equal or better placement |
| **Events as PNG screenshots** | Not accessible, searchable, or maintainable |
| **Orphaned pages** | `/calendar/`, `/places-of-worship/` exist but aren't in nav |
| **Interpreter page is text-heavy** | Highest-traffic page lacks scannable structure and audience split |
| **No testimonials, news, or social** | Site feels institutional; doesn't show active community |
| **No ASL / bilingual content** | Reads as hearing org that serves Deaf people, not Deaf-friendly space |
| **Unreliable WordPress/Divi host** | Sitemap 500, migration risk, slow loads, plugin dependency |
| **Accessibility is opt-in** | Sogo toolbar helps, but contrast/font fixes shouldn't require toggles |
| **Legacy analytics (UA)** | No longer collects data |

### Integrations to preserve

| Service | Purpose |
|---------|---------|
| Zeffy | Donations, sponsorship, email + paper newsletters |
| Cognito Forms | Interpreter request form |
| Zoho Calendar | Community calendar (consider replacing) |
| Amazon Wishlist | In-kind giving |
| Facebook group | Community (`facebook.com/groups/295002970853564`) |

---

## Information architecture

### Primary navigation (5 items)

Replace the current flat list (HOME, ABOUT, INTERPRETER SERVICES, DONATE, RESOURCES, CONTACT, EVENTS) with intent-based structure:

```
[Logo]   Our Services   About   Support Us   Resources   Contact
```

| Nav item | Subpages / anchors | Source content |
|----------|-------------------|----------------|
| **Our Services** | Interpreter Services · Caseworker & Advocacy · Programs · Events & Calendar | `interpreter-services`, new outlines, `events` + `calendar` |
| **About** | Mission & History · Board of Directors · Staff | blank `about`, `b-o-d` |
| **Support Us** | Donate · Volunteer · Newsletter · Sponsorship · Wishlist | `donate`, `volunteer`, Zeffy links |
| **Resources** | Helpful Links · Places of Worship · College Guide | `resources`, `places-of-worship` |
| **Contact** | Contact form · VP · voice · address · map | `contact` |

**Removed from top nav:** standalone Donate, Events, Interpreter Services, Volunteer, B.O.D. — all live under the sections above.

### URL redirects (preserve SEO)

| Old URL | New URL |
|---------|---------|
| `/interpreter-services/` | `/services/interpreters/` |
| `/b-o-d/` | `/about/board/` |
| `/volunteer/` | `/support/volunteer/` |
| `/donate/` | `/support/donate/` |
| `/events/`, `/calendar/` | `/services/events/` |
| `/places-of-worship/` | `/resources/places-of-worship/` |

---

## Page-by-page plan

### Homepage

**Problem:** Visitors should know within 3 seconds what TDHHC does, who it serves, and how to reach them. Today the donation ask competes with the mission statement.

**Above the fold — one clear primary CTA:**

```
┌──────────────────────────────────────────────────────────────┐
│  VP 903-206-2210  ·  Voice 903-617-6204  ·  coordinator@…   │  ← equal visual weight
├──────────────────────────────────────────────────────────────┤
│  [Logo]    Our Services   About   Support Us   Resources   Contact
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  HERO: "East Texas's resource center for Deaf, Hard of      │
│         Hearing, and DeafBlind communities."                   │
│                                                              │
│  [ASL welcome video — captioned]                             │
│                                                              │
│  ┌─────────────────────────────┐                            │
│  │  Request an Interpreter  →  │  ← single primary CTA      │
│  └─────────────────────────────┘                            │
│  Secondary: Contact Us · Our Services                        │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  NEWS & UPDATES (3 latest — shows org is active)              │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ Our Services│  │  Resources  │  │  Support Us │         │
│  │  (need help)│  │  (find links)│  │  (give back)│         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
├──────────────────────────────────────────────────────────────┤
│  COMMUNITY VOICES (1–2 testimonials)                         │
├──────────────────────────────────────────────────────────────┤
│  UPCOMING EVENTS (structured cards — not screenshots)        │
├──────────────────────────────────────────────────────────────┤
│  Footer: address · VP · voice · social · 501(c)(3)          │
└──────────────────────────────────────────────────────────────┘
```

**Homepage rules:**
- Lead with **who TDHHC serves**, not a donation ask
- **Interpreter request** is the #1 CTA (links to `/services/interpreters/#request`)
- **VP and voice numbers equally prominent** in header and footer — click-to-call / click-to-VP on mobile
- Donate moves to Support Us section and footer — not hero competition
- Donation is one tap away via nav, never buried

---

### Our Services

Hub page routing two audiences to the right content.

#### Interpreter Services (`/services/interpreters/`) — highest traffic

**Problem:** Text-heavy wall; businesses and Deaf individuals have different needs but share one page.

**Structure:**

1. **Sticky top bar:** `[ Request an Interpreter ]` button → jumps to Cognito form or `mailto:coordinator@tdhhc.org`
2. **Audience picker** (two cards, equal prominence):
   - **"I'm a business or organization"** → ADA compliance value prop, billing, rates, Cognito form
   - **"I'm Deaf/HoH and need help accessing services"** → caseworker advocacy, how TDHHC helps navigate appointments, contact info
3. **Plain-language ADA summary** (for businesses):
   - Entities must provide effective communication
   - TDHHC is your backup plan — certified interpreters, predictable rates, no exclusivity
4. **Rate information** — currently vague ("reasonable and competitive"). **Action item for staff:** publish a rate table or downloadable PDF. Until then, "Contact coordinator for current rates" with direct VP/email.
5. **FAQ accordion** — billing cycle, requesting specific interpreters, cancellation, certification levels
6. **For interpreters** — resume submission, mentoring, TJC ITP link (existing content, lower on page)
7. **Cognito Forms embed** (preserve existing integration)

#### Caseworker & Advocacy (new page)

Content to develop with staff — referenced on current site but never dedicated:
- DHHS Access Specialist program
- STAP telephone equipment assistance
- Help navigating medical, legal, and social services

#### Programs (new page)

Consolidate scattered mentions:
- Adult literacy classes
- Interpreter mentoring / shadowing
- Community outreach

#### Events & Calendar (`/services/events/`)

- Merge `events` + `calendar` pages
- Replace screenshot images with structured event entries (title, date, time, location, description, ASL/interpreter noted)
- Embed or sync calendar (Zoho, Google Calendar, or CMS-managed)
- "Add to Calendar" / `.ics` download per event

---

### About

| Page | Content | Status |
|------|---------|--------|
| **Mission & History** | Founded 2012, 501(c)(3), East Texas service area, "one-stop shop" vision, photos | **Blank today — must write** |
| **Board of Directors** | Existing B.O.D. content (current through Feb 2026) | Ready from archive |
| **Staff** (optional) | Key personnel, photos, ASL intro videos | New |

Include at least one **ASL video introduction** from coordinator or board member — signals genuine Deaf-friendly space.

---

### Support Us

Consolidates all giving and engagement paths for the "supporter" audience.

| Page | Content | Source |
|------|---------|--------|
| **Donate** | Zeffy embed, mail-in address, tax-deductible notice | `donate` |
| **Volunteer** | ASL fluency requirements, application process | `volunteer` |
| **Newsletter** | Email + paper signup via Zeffy | `events`, `resources` |
| **Sponsorship** | Zeffy sponsorship link | `donate` |
| **Wishlist** | Amazon wishlist link | `donate` |

Supporter audience gets a single nav destination with clear sub-paths — no hunting between Donate, Volunteer, and Events for newsletter signup.

---

### Resources

| Page | Content | Status |
|------|---------|--------|
| **Helpful Links** | News (D-Pan, Daily Moth), orgs (NAD, TAD, HLAA), interpreting orgs (RID, BEI, TSID) | Ready |
| **Places of Worship** | Full list from orphaned page — Tyler/Longview churches, ASL fellowship | Ready (hidden today) |
| **College Guide** | Deaf/HoH college student guide, TJC ITP | Ready |

Add filters on Places of Worship: city, interpreted vs. ASL worship.

---

### Contact

- Keep contact form fields (name, company, email, phone, message, referral source)
- **VP and voice displayed with equal weight** above the form
- Embedded map
- Office hours (if applicable — confirm with staff)
- Link to interpreter request for entity inquiries

---

## Accessibility (especially important for this audience)

Move from **opt-in fixes** (Sogo toolbar) to **accessible by default**. Keep an enhanced toolbar as optional, not required.

| Current | Redesign |
|---------|----------|
| Standard contrast; high contrast is toggle | **High contrast on by default**; optional standard mode |
| VP number in secondary header bar | **VP = voice prominence** everywhere: header, footer, contact, interpreter page |
| Many images `alt=""` | **Descriptive alt text** on every image; decorative images marked `alt=""` explicitly |
| 14px body; resize via toolbar | **18px base font**, comfortable line-height (1.6+); no resize needed for most users |
| No video captions | **Captions on all video**; transcripts linked below |
| `user-scalable=0` blocks zoom | **Allow pinch-zoom** |
| Sogo plugin dependency | Built-in CSS tokens + optional toolbar |

**Standards target:** WCAG 2.2 AA minimum; AAA for body text contrast where possible.

**Additional:**
- Semantic HTML landmarks, skip links, keyboard-navigable menus
- `prefers-reduced-motion` respected
- Plain language; acronym glossary (ADA, BEI, RID, STAP, DHHS, VP)
- Atkinson Hyperlegible or Source Sans 3 typography

---

## New content to create

These pieces are missing entirely and build trust, community, and donations:

| Content | Purpose | Effort |
|---------|---------|--------|
| **Community testimonials** | 2–4 quotes from Deaf community members, businesses, or families — humanizes the org | Staff outreach |
| **News & updates feed** | Announcements, event recaps, program news — proves the org is active | CMS-managed; 1 post/month minimum |
| **Social media links** | Facebook group at minimum; add Instagram/YouTube if active | Confirm accounts with staff |
| **ASL video introductions** | Homepage hero + About page — immediate Deaf-friendly signal | Record with coordinator/board |
| **Mission & history copy** | About page body (currently blank) | Staff workshop |
| **Caseworker & programs pages** | Services mentioned but never detailed | Staff workshop |
| **Rate sheet or pricing FAQ** | Interpreter page transparency | Coordinator input |
| **Privacy policy & accessibility statement** | Legal/compliance pages | Template + review |

---

## Design & brand

Eastland Jones Creative new logo + refreshed palette do heavy lifting. Define early:

- Logo files: SVG, PNG (full color, reversed, icon-only)
- Color tokens from new brand (evaluate whether `#d7282f` red carries forward)
- High-contrast default palette
- No text baked into images (especially events)
- Photography: community, signing, events — not stock handshakes

---

## Technical architecture

**Recommended:** Static site + lightweight CMS on reliable CDN hosting.

| Layer | Choice |
|-------|--------|
| Framework | Astro or Next.js (static export) |
| CMS | Decap CMS (Git-based) or Sanity — for news, events, testimonials |
| Hosting | Cloudflare Pages or Netlify |
| Forms | Cognito Forms (interpreter), contact form via Formspree or Netlify Forms |
| Donations / newsletters | Zeffy embeds (unchanged) |
| Analytics | Google Analytics 4 or Plausible |
| Calendar | Google Calendar embed or CMS events |

**Why not stay on WordPress/Divi:** unreliable current host, heavy page weight, Divi lock-in, blank About page suggests builder fragility. If staff strongly prefer WordPress, use managed hosting (Kinsta, WP Engine) with a block theme — not Divi.

**Estimated ongoing cost:** $0–50/month.

---

## Migration phases

### Phase 1 — Foundation (weeks 1–2)
- [x] Archive current site (`archive/`)
- [x] Unified redesign plan (this document)
- [ ] Collect new logo assets from Eastland Jones Creative
- [ ] Confirm Zeffy, Cognito, Zoho credentials
- [ ] Content workshop: About, caseworker, programs, testimonials
- [ ] Confirm social media accounts to link
- [ ] Coordinator: rate sheet or pricing FAQ content

### Phase 2 — Design (weeks 2–3)
- [ ] Design tokens (color, type, contrast defaults)
- [ ] Wireframes: homepage, interpreter services, nav
- [ ] Component library (header with VP, CTA buttons, event cards, testimonial block)
- [ ] Stakeholder review with board + Eastland Jones Creative

### Phase 3 — Build (weeks 3–5)
- [ ] Scaffold site repo
- [ ] Build all pages from archived content + new copy
- [ ] Integrate Zeffy, Cognito, calendar
- [ ] Record and embed ASL videos
- [ ] 301 redirects from all old URLs
- [ ] News/updates CMS workflow for staff

### Phase 4 — QA & launch (week 6)
- [ ] Accessibility audit (axe, WAVE, screen reader, VP click-to-call on mobile)
- [ ] Staff CMS training
- [ ] DNS cutover
- [ ] Monitor forms, donations, analytics for 30 days
- [ ] Decommission old host

---

## Quick wins (current site, before launch)

Can be done on the existing WordPress site while the rebuild is in progress:

1. Fix the **blank About page** with mission/history draft
2. Add **Places of Worship** link on Resources (content already exists)
3. Link **Calendar** from Events page
4. Add **Facebook group** link to footer
5. Remove **`user-scalable=0`** from viewport
6. Add **alt text** to homepage images
7. Replace **UA analytics** with GA4

---

## Success metrics

| Metric | Target |
|--------|--------|
| Homepage clarity | Visitor can state TDHHC's purpose within 3 seconds (user testing) |
| Interpreter requests | Form submissions maintained or increased post-launch |
| Accessibility | WCAG 2.2 AA audit pass; VP reachable in ≤2 taps on mobile |
| Performance | LCP < 2.5s on mobile |
| Uptime | 99.9%+ (vs. current unreliable host) |
| Engagement | Newsletter signups, donations, event page views tracked in GA4 |

---

## Open questions for TDHHC staff

1. **Caseworker services** — what is offered today, and what should the page say?
2. **Rate sheet** — can published rates be shared, or coordinator-quote only?
3. **Social media** — which platforms are active and should be linked?
4. **Testimonials** — who can provide quotes (with permission)?
5. **ASL videos** — who will record, and is captioning service available?
6. **Events** — who will maintain the calendar post-launch?
7. **New logo** — when will final assets be delivered from Eastland Jones Creative?

---

## Next step

Review this plan with the board and Eastland Jones Creative, answer the open questions, then begin **Phase 2 design** with homepage and interpreter services wireframes.

---

*Combined from site archive (May 29, 2026) and stakeholder analysis. Source: [tdhhc.org](https://tdhhc.org/)*
