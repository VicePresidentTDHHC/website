# TDHHC.org — Sitemap & Content Decisions

Build brief for the redesign. Use alongside [`REDESIGN-PROPOSAL.md`](REDESIGN-PROPOSAL.md) and [`CONTENT-VOICE.md`](CONTENT-VOICE.md). Every page lists **content source**, **build decision**, and **staff action** where needed.

**Voice constraint:** Do not migrate patronizing language from the archive. Rewrite all copy per [CONTENT-VOICE.md](CONTENT-VOICE.md) — e.g. no "here to help," "we're here for you," "curious about," "we hope you enjoy."

---

## Critical fixes before launch

Issues found in homepage and interpreter services audit (May 2026 archive + live review).

| Issue | Severity | Finding | Action |
|-------|----------|---------|--------|
| **Ghost email link** | 🔴 Critical | Empty `<a href="mailto:nick@ImperiousExpo.com"></a>` in sitewide footer template — no visible text, present in DOM on **every page** | Remove entirely. Audit for other stray links from prior developers/host. |
| **Address mismatch** | 🔴 Critical | Archive footer consistently shows `1828 ESE Loop 323, Suite LL-14`. Homepage (live review) also referenced `1530 SSW Loop 323, Suite 114`. | **Staff must confirm canonical physical address** before build. Use one address everywhere: footer, contact, JSON-LD, Google Business Profile. |
| **Empty alt text** | 🟠 High | Homepage promo cards (`Our_Services-min.jpg`, `Oue_Services-min.jpg`, `Donate_-min.jpg`), events screenshot, interpreter page `signing_2-women-min.jpg` all `alt=""` | Write descriptive alt text or mark decorative with `role="presentation"` and empty alt intentionally. |
| **WPBakery inside Divi** | 🟡 Medium | Interpreter page right column contains `wpb_text_column`, `vc_row`, `l-section` — legacy paste from another builder | Do not migrate. Rewrite as clean semantic HTML in new build. |
| **Events as screenshots** | 🟠 High | PNG images used for event listings | Replace with structured event content (CMS). |
| **Blank About page** | 🔴 Critical | `/about/` has empty Divi layout | New copy required (see About section below). |

---

## Site map

### Primary navigation

```
Home
Our Services
  ├── Interpreter Services      /services/interpreters/
  ├── Caseworker & Advocacy     /services/caseworker/          [NEW]
  ├── Programs                  /services/programs/            [NEW]
  └── Events & Calendar         /services/events/
About
  ├── Mission & History         /about/
  ├── Board of Directors        /about/board/
  └── Staff                     /about/staff/                  [OPTIONAL]
Support Us
  ├── Donate                    /support/donate/
  ├── Volunteer                 /support/volunteer/
  ├── Newsletter                /support/newsletter/
  ├── Sponsorship               /support/sponsorship/
  └── Amazon Wishlist           /support/wishlist/
Resources
  ├── Helpful Links             /resources/
  ├── Places of Worship         /resources/places-of-worship/
  └── College & Training        /resources/college-guide/
Contact                       /contact/
News                          /news/                           [NEW — index]
  └── [posts]                   /news/[slug]/
```

### Utility / legal (footer links)

| Page | URL | Status |
|------|-----|--------|
| Privacy Policy | `/privacy/` | New — required |
| Accessibility Statement | `/accessibility/` | New — required |
| 501(c)(3) notice | Footer text | Exists in donate copy |

### URL redirects (301)

| Old | New |
|-----|-----|
| `/` | `/` (home) |
| `/interpreter-services/` | `/services/interpreters/` |
| `/about/` | `/about/` (repopulated) |
| `/b-o-d/` | `/about/board/` |
| `/volunteer/` | `/support/volunteer/` |
| `/donate/` | `/support/donate/` |
| `/events/` | `/services/events/` |
| `/calendar/` | `/services/events/#calendar` |
| `/resources/` | `/resources/` |
| `/places-of-worship/` | `/resources/places-of-worship/` |
| `/contact/` | `/contact/` |

---

## Global elements (every page)

### Header

| Element | Decision |
|---------|----------|
| Logo | New Eastland Jones Creative assets (SVG preferred) |
| Nav | 5 items: Our Services · About · Support Us · Resources · Contact |
| VP number | `903-206-2210` — **equal visual weight to voice**; `tel:` link |
| Voice number | `903-617-6204` — `tel:` link |
| Email | `coordinator@tdhhc.org` |
| Primary CTA (optional in header) | "Request Interpreter" → `/services/interpreters/#request` |

### Footer

| Element | Decision |
|---------|----------|
| Physical address | **TBD — staff confirms** (see critical fixes) |
| Mailing address | P.O. Box 6134, Tyler, TX 75711 |
| VP + voice + email | Same prominence; no ghost links |
| Social | Facebook group (confirmed in archive); add others if active |
| Quick links | Donate · Volunteer · Interpreter Request · Contact |
| Copyright | © Tyler Deaf and Hard of Hearing Center |
| Legal | Privacy · Accessibility |

**Explicit exclusion:** No `nick@ImperiousExpo.com` or any empty anchor tags.

---

## Page-by-page content decisions

### Home (`/`)

**Purpose:** Within 3 seconds, visitor knows who TDHHC serves and how to reach them. Primary audience = service seekers.

| Section | Content decision | Source |
|---------|------------------|--------|
| Hero headline | "East Texas resource center for Deaf, Hard of Hearing, and DeafBlind communities" (refine with staff) | New + existing tagline |
| ASL welcome video | Record 30–60 sec intro; captions + transcript | **New** |
| Primary CTA | "Request an Interpreter" → `/services/interpreters/#request` | New IA |
| Secondary links | Contact · Our Services | — |
| Three pathway cards | Our Services · Resources · Support Us | Replaces current Contact/Services/Donate cards |
| News & updates | 3 latest posts from `/news/` | **New** CMS |
| Community voices | 1–2 testimonials | **New** — staff collects |
| Upcoming events | Structured cards (not screenshot) | Migrate from `events` |
| Mission blurb | "One-stop shop" paragraph | `home` archive |
| Interpreter CTA band | "Entities request interpreters, not clients" + button | `home` + `interpreter-services` |

**Homepage images to replace or fix:**

| Image | Current issue | Decision |
|-------|---------------|----------|
| `Our_Services-min.jpg` | Empty alt; generic | Replace or alt: "People connecting at TDHHC community event" |
| `Oue_Services-min.jpg` | Typo filename; empty alt | Replace; alt text required |
| `Donate_-min.jpg` | Empty alt; competes with mission in card layout | Move to Support Us pathway only |
| `Screenshot-2026-03-27...png` | Events as image; empty alt | **Remove** — use structured events |
| `signing-blog-CTA-min-1.jpg` | Background CTA image | Keep if contrast passes; add text overlay |

---

### Interpreter Services (`/services/interpreters/`)

**Purpose:** Highest-traffic page. Two audiences: businesses needing ADA-compliant interpreters, and Deaf individuals needing help accessing services.

**Layout decision:** Keep **form-left** pattern. Cognito Forms embed stays. Improve everything around it.

```
┌─────────────────────────────────────────────────────────────┐
│  [ Request an Interpreter ]  ← sticky / top of page         │
├─────────────────────────────────────────────────────────────┤
│  Plain-language summary (2–3 sentences) + audience picker │
│  ┌─────────────────────┐  ┌─────────────────────┐         │
│  │ I'm a business /    │  │ I'm Deaf/HoH and    │         │
│  │ organization        │  │ need access help    │         │
│  └─────────────────────┘  └─────────────────────┘         │
├──────────────────────────────┬──────────────────────────────┤
│  COGNITO FORM EMBED          │  ANDREA SHORT — contact card   │
│  (preserve integration)      │  Coordinator                   │
│                              │  coordinator@tdhhc.org         │
│                              │  VP: 903-206-2210              │
│                              │  Voice: 903-617-6204           │
│                              │  ─────────────────────────     │
│                              │  Optional: signing photo WITH  │
│                              │  alt text, or remove if purely │
│                              │  decorative                    │
├──────────────────────────────┴──────────────────────────────┤
│  FOR BUSINESSES: ADA value prop · rates · billing FAQ        │
├─────────────────────────────────────────────────────────────┤
│  FOR DEAF INDIVIDUALS: how TDHHC advocates for access        │
├─────────────────────────────────────────────────────────────┤
│  FAQ accordion                                               │
├─────────────────────────────────────────────────────────────┤
│  FOR INTERPRETERS: hiring · mentoring · TJC ITP link         │
└─────────────────────────────────────────────────────────────┘
```

| Content block | Decision | Source |
|---------------|----------|--------|
| Request button | Top of page + anchor `#request` | New UX |
| Cognito embed | Keep `data-key="RUV9PohCIkqzMCpW5J2vsQ"` form 1 | Live integration |
| Jordyn Babyak contact | **Move adjacent to form** — not buried below WPBakery markup | `interpreter-services` |
| "Have more questions?" filler | **Remove.** Replace with: "Questions: Jordyn Babyak" + VP, voice, email (see CONTENT-VOICE.md) | Rewrite — do not migrate |
| Signing women photo | Either meaningful alt ("Two women conversing in ASL") or remove | `signing_2-women-min.jpg` |
| WPBakery block | **Do not migrate** | Discard |
| ADA / rates copy | Keep substance; shorten intro; add rate table or PDF | `interpreter-services` — staff confirms rates |
| Entity-only requests | Bold callout above form | Existing policy |
| Interpreter hiring | Lower section | Existing copy |
| TJC ITP link | `www.tjc.edu/signlanguage` | Existing |

**Key messages to preserve (from archive):**
- Businesses request and pay; TDHHC bills end of month
- Can request/reject specific interpreter (subject to availability)
- Master vs. basic level — same community/medical rate
- Specialty (court/legal) separate rate
- Nonprofit goal: pay interpreters fairly, not maximize profit

---

### Caseworker & Advocacy (`/services/caseworker/`) — NEW

| Field | Decision |
|-------|----------|
| Status | **Must be written by staff** — referenced on site but never dedicated |
| Topics to cover | DHHS Access Specialist, STAP, navigating medical/legal/social services |
| Source hints | `resources` page links (STAP, DHHS) |
| CTA | Contact coordinator |

---

### Programs (`/services/programs/`) — NEW

| Program | Mentioned in archive? | Decision |
|---------|----------------------|----------|
| Adult literacy classes | Home page | Include if still active — confirm with staff |
| Interpreter mentoring / shadowing | Interpreter page | Include |
| Community outreach | Implied | Staff to describe |

---

### Events & Calendar (`/services/events/`)

| Element | Decision | Source |
|---------|----------|--------|
| Event list | CMS-managed structured entries | Replace screenshots |
| Calendar embed | Zoho (current) or Google Calendar — staff preference | `calendar` page |
| Newsletter CTAs | Move to Support Us; link from events | Zeffy URLs from `events` |
| Filters | Optional: community / interpreter / fundraiser | New |

---

### About — Mission & History (`/about/`)

| Field | Decision |
|-------|----------|
| Status | **Blank today — write from scratch** |
| Must include | Founded 2012 · 501(c)(3) · East Texas · mission · "one-stop shop" vision |
| ASL video | Same or different from homepage — staff choice |
| Photos | Center, events, staff |

### About — Board (`/about/board/`)

| Field | Decision |
|-------|----------|
| Source | Ready from archive | `b-o-d` |
| Last updated | Feb 17, 2026 |
| Content | President Susie Grona; full board + honorary members |

### About — Staff (`/about/staff/`) — OPTIONAL

Staff bios + photos if desired.

---

### Support Us pages

| Page | Content | Integration |
|------|---------|-------------|
| Donate | Thank-you copy, tax-deductible notice, mail-in address | Zeffy: `donate-to-tdhhc` |
| Volunteer | ASL fluency note, application process | `volunteer` archive |
| Newsletter | Email + paper options | Zeffy ticketing links |
| Sponsorship | Sponsor opportunities | Zeffy: `sponsorship-opportunities-22` |
| Wishlist | Amazon link | `amazon.com/hz/wishlist/ls/1XOKWYVUJEUCI` |

---

### Resources

| Page | Decision | Source |
|------|----------|--------|
| Helpful Links | Keep curated lists; verify links alive at launch | `resources` |
| Places of Worship | Promote from hidden page; add city/service filters | `places-of-worship` |
| College Guide | Deaf/HoH college guide + TJC ITP | `resources` |

**Link categories to preserve:**
- News: D-Pan, Daily Moth
- Orgs: NAD, TAD, HLAA, AADB, THHS DHHS
- Interpreting: RID, BEI, TSID
- Training: TJC ITP

---

### Contact (`/contact/`)

| Field | Decision |
|-------|----------|
| Form fields | Name, company, email, phone, message, referral source |
| Implementation | New form service (Formspree/Netlify) or Cognito — not Divi contact form |
| VP + voice | Display **above** form with equal weight |
| Map | Embed once canonical address confirmed |
| Interpreter requests | Direct link to `/services/interpreters/#request` |

---

### News (`/news/`) — NEW

| Field | Decision |
|-------|----------|
| Purpose | Show org is active; support SEO |
| Cadence | Staff goal: minimum 1 post/month |
| Types | Event recaps, announcements, program news |
| CMS | Decap or Sanity |
| Homepage | Surface 3 latest |

---

## Content reuse matrix

| Status | Pages |
|--------|-------|
| **Ready to migrate** (rewrite voice, keep facts) | Board facts, Resources links, Places of Worship, interpreter policies/rates — strip patronizing phrases per CONTENT-VOICE.md |
| **Restructure** (rewrite voice + layout) | Interpreter Services, Contact, Home pathway cards |
| **Replace format** | Events (screenshots → structured) |
| **Write new** | About/Mission, Caseworker, Programs, News, Testimonials, Privacy, Accessibility |
| **Do not migrate** | WPBakery markup, ghost email, Divi boilerplate, Sogo plugin dependency |

---

## Integrations checklist

| Integration | Keep? | Notes |
|-------------|-------|-------|
| Cognito Forms (interpreter) | ✅ Yes | Form 1, key `RUV9PohCIkqzMCpW5J2vsQ` |
| Zeffy donations | ✅ Yes | |
| Zeffy newsletters | ✅ Yes | Email + paper |
| Zeffy sponsorship | ✅ Yes | |
| Amazon Wishlist | ✅ Yes | |
| Zoho Calendar | ⚠️ Evaluate | Consider Google Calendar or CMS events |
| Facebook group | ✅ Yes | `facebook.com/groups/295002970853564` |
| Sogo Accessibility | ❌ Replace | Build accessibility into theme defaults |
| Google Analytics UA | ❌ Replace | GA4 or Plausible |
| Divi contact form | ❌ Replace | |

---

## Staff decisions required

Check off before development starts:

- [ ] **Canonical physical address** — 1828 ESE Loop 323, Suite LL-14 vs. 1530 SSW Loop 323, Suite 114?
- [ ] **Rate sheet** — publish on interpreter page or coordinator-quote only?
- [ ] **Caseworker page** — what services are offered today?
- [ ] **Programs** — which are still active (literacy, etc.)?
- [ ] **Testimonials** — who can provide quotes (with permission)?
- [ ] **ASL videos** — who records; captioning service?
- [ ] **Social accounts** — which platforms to link?
- [ ] **Events owner** — who maintains calendar post-launch?
- [ ] **New logo files** — delivery date from Eastland Jones Creative?
- [ ] **nick@ImperiousExpo.com** — any reason this was ever on site? (Remove regardless.)

---

## Image & media inventory

| Asset | File | Alt text (proposed) |
|-------|------|---------------------|
| Logo | New from EJC | "Tyler Deaf and Hard of Hearing Center" |
| Home card 1 | `Our_Services-min.jpg` | TBD — community/services scene |
| Home card 2 | `Oue_Services-min.jpg` | Replace file; fix typo |
| Home card 3 | `Donate_-min.jpg` | Move to Support Us only |
| Interpreter | `signing_2-women-min.jpg` | "Two women signing in conversation" or remove |
| Events | Screenshot PNGs | **Deprecate** — use text events |
| CTA background | `signing-blog-CTA-min-1.jpg` | Decorative or describe scene |

---

## Build order (recommended)

1. Global shell (header, footer, nav, VP/voice, **no ghost links**)
2. Interpreter Services (highest traffic + most audit findings)
3. Home
4. Support Us hub + subpages
5. Resources + Places of Worship
6. About (once copy written)
7. Events + News CMS
8. Contact
9. Legal pages
10. Redirects + launch QA
11. **Voice pass** — every page against [CONTENT-VOICE.md](CONTENT-VOICE.md)

---

*Last updated: May 29, 2026. Original HTML: `archive/raw/`. Content exports: `content/`.*
