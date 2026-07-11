# DRT.FM Design System — DESIGN.md

Read this before building or changing ANY DRT.FM screen. Values here are law unless Dainis overrides them.
Identity in one line: **quiet luxury, dark-first — the UI stays quiet so Alexis and the conversation carry all the emotion.**
Decision order, always: outcome → structure/IA → interaction → visual polish. Never start with styling.

## 1 · Surfaces & depth (dark ramp — never pure black)

```
--bg-page:    #0f0e11   /* page canvas */
--bg-surface: #1a191e   /* cards, inputs, nav */
--bg-raised:  #242229   /* hover/active tiles, dropdowns */
--hairline:   rgba(255,255,255,0.08)
```
- Depth = stepping this ladder + hairlines. **Box-shadows only on floating layers** (modals, popovers, toasts): one token, `0 16px 48px rgba(0,0,0,0.5)`. Zero shadows on in-flow cards or buttons.
- First paint must match `--bg-page` — no white flash, ever.

## 2 · Text tones

```
--text-hi:  #f2f0f3   /* headings, names — near-white, never #fff */
--text-mid: #a9a4b0   /* body, descriptions */
--text-low: #6f6a78   /* metadata, captions, timestamps */
```
Hierarchy comes from weight + tone dimming, not from more sizes. Floor: no text below 11px rendered.

## 3 · Accent — one color, with a job description

Evolved from the current site: **rose stays, purple is retired** (purple gradients are the definitive AI-slop fingerprint; the two-accent scheme dies here).

```
--accent:        #f2436b   /* refined rose */
--accent-hover:  #d63a5e
--accent-tint:   rgba(242,67,107,0.10)  /* selected-state backgrounds only */
```
Accent MAY appear as: (1) the single money CTA per viewport region, (2) active-nav indicator, (3) selection rings/borders + `--accent-tint` fill, (4) at most one accented word in a display headline.
Accent is BANNED from: icons, links, borders, hovers, focus rings (use white), gradients, decoration. Target: under 2% of any screen's pixels.
Semantic colors own exactly one meaning each: `--live: #e5484d` (live status only) · `--success: #46a758` · `--warn: #e6a13c`. If a color means two things anywhere, remove one.

## 4 · Typography (two families, self-hosted, subsetted)

- **UI: Satoshi** — 400 / 500 / 700. Everything: nav, buttons, body, forms, cards.
- **Display: Instrument Serif** — 400 only. ONLY for: page-level headlines, Alexis/character names at showcase size, pull-quotes in marketing prose. If it appears more than ~2 times per screen, it stops being special — cut back.
- Scale (px): 12 · 14 · 16 · 18 · 22 · 28 · 36 · 48. Body = 16/1.5 (14 allowed in dense app panels). Display ≥28px gets line-height ~1.1 and letter-spacing −0.5px.
- Line length 50–75 characters. Sentence case everywhere. UPPERCASE only on tiny badge pills (11–12px, tracked). **Never letter-space lowercase text.**

## 5 · Spacing, layout, radii

- 8px spacing scale (4px allowed for icon-to-label micro gaps): 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96.
- Unit-block rule: space **inside** a group is always smaller than space **between** groups. Whitespace separates; borders are a last resort.
- 12-col grid desktop (max content 1200px), 4-col mobile. Touch targets ≥48px. One alignment strategy per screen.
- Radius tokens, bound to component class — no other values exist:
  `--r-control: 10px` (buttons, inputs, selects) · `--r-card: 16px` (media/content cards) · `--r-modal: 24px` · `--r-pill: 999px` (chips, badges, filter tags).

## 6 · Components (recipes — do not improvise)

**Buttons, three tiers, every state defined at design time (default/hover/active/disabled):**
1. *Accent* — `--accent` fill, white text. Max ONE visible per region (Subscribe, Upgrade, the step's primary action).
2. *Inverse* — white fill, near-black text. The primary in-flow action (Chat, Continue).
3. *Quiet* — `--bg-surface` fill or ghost text. Everything else. Paired actions = inverse + quiet, never two accents.

**Character/content cards:** image fills the card 100% (no border, no padded frame, no shadow). Text overlays the bottom on a **multi-stop eased scrim** (≥8 stops, alpha 0.65→0 over the lower ~55% — if you can see where the gradient starts, add stops). One identity line (name 500 + age dimmed, single line) + one hook line in second person, clamped at 2 lines. No tag lists or stat rows on cards.
**Hover reveals content** (motion preview, next frame, live state) or steps the background — never scale beyond 1.02, never glow.

**Inputs:** `--bg-surface` fill, hairline border, white focus ring (2px). Validate on blur; error text says what + why + how to fix, next to the field, never color-alone.

**Empty states are doorways:** render the action that fills the space, at content size and position (a "Create" tile occupying the future card's slot; fanned character images + one button — never a gray "nothing here yet"). Custom-designed 404 in brand palette, one exit path.

**Promos/upsells inside content obey the content grid**: exact card size, radius, and type of the units around them; one differentiating treatment max.

**Overflow is always designed:** 2-line clamp + "see more", N-visible + "+K more" counter chip, or horizontal rail with edge fade + arrow. Selected chips use inverted contrast (white bg, dark text) — not accent.

## 7 · Motion (restraint is the brand)

- Durations: 120ms (micro) · 200ms (standard) · 300ms (overlays). One curve: `cubic-bezier(0.2, 0, 0, 1)`.
- Animate only `opacity` and `transform`. No scroll-triggered animation, no parallax, no ambient/looping motion, no animated status dots.
- Motion exists for feedback and orientation only. Respect `prefers-reduced-motion`. When in doubt, don't animate.

## 8 · Voice & copy (copy is a design material)

- Plain verbs, sentence case: buttons say exactly what happens ("Start chatting", not "Submit"); the name stays consistent through the flow.
- Where Alexis/a character speaks, she is in character; the chrome around her never is.
- Chat never opens empty — the character has already sent an in-character opener; the idle composer teaches features as tappable chips.
- Placeholders teach by example (a real query the user could type verbatim, not "Search...").
- Trust microcopy sits at the anxiety point: discreet bank-statement label + "cancel anytime in settings" within eyeshot of every pay button.
- Pricing: 2–3 plans max, one pre-selected via accent border + `--accent-tint`; convert credits to concrete outputs ("X images / Y minutes of voice"); no comparison matrices.

## 9 · Performance budget (hard gates — this site must rank)

- Page weight <1.5MB · JS <300KB compressed · above-fold images <500KB · fonts: these 2 families only, subsetted, ≤100KB total.
- LCP <2.5s · CLS <0.1 · INP <200ms. Images AVIF/WebP, explicit dimensions (zero layout shift), lazy below fold.
- No animation libraries, no carousels autoplaying media below the fold, no third-party scripts without sign-off. Video: poster-first, muted, never the LCP element.

## 10 · Landing page (Alexis-first showcase)

Above the fold: **Alexis as real presence** — poster frame/inline trailer (muted, poster-first for LCP), her name in the display serif, one line of promise, ONE accent CTA. This is the thing competitors can't copy; it must feel like meeting her, not like an ad about her.
Below: the character grid with working search/filters (real product, browsable logged-out). Below that: SEO/marketing prose styled as quiet article text. Feature education happens in-context (composer chips, benefit rows) — never a three-column icon feature grid.

## 11 · Never (the anti-slop list)

Purple or purple-to-pink gradients anywhere · glassmorphism panels · glow borders/neon edges · shadows or lifts on cards · more than one accent color per screen · centered hero + two buttons + floating blobs · three-column feature grids · emoji as icons (one drawn icon set only) · uppercase tracked section labels · "Search..." placeholders · dead-end empty states · scale/zoom image hovers · ad-hoc hex/px values not in this file · Inter/Roboto/Arial/Space Grotesk.

## 12 · Logo (locked 2026-07-11 — do not redesign)

The brand mark is the **Heartwave**: seven rose sound bars tracing a heart silhouette (love + .fm audio in one shape). The logo is the mark-led lockup: Heartwave + `drt.fm` in Satoshi Bold, white text, rose period, generous gap between mark and text. Files live in `drtfm-logo-kit/`:
- `lockup-dark.svg` (primary, on dark) · `lockup-light.svg` · `lockup-mono-white/black.svg` (single-color contexts)
- `lockup-dark-animated.svg` / `mark-animated.svg` — bars pulse (1.6s ease, staggered); use ONLY where Alexis is actively speaking or as a loading indicator; static everywhere else; both respect `prefers-reduced-motion`
- `mark.svg` + `favicon.ico` + `favicon-16/32/48/64.png` (transparent) + `app-icon-180/192/512.png` (dark tile)

Rules: never recolor the mark outside `--accent`/white/ink · never place the heart-dot or a second heart near the lockup (one heart per surface) · minimum lockup height 20px, below that use the mark alone · clear space around lockup = height of one bar · the animated variant never autoplays on marketing pages (speed budget).

## 13 · Working loop (for any Claude session)

1. Read this file fully before the first line of markup. Every color/size/duration comes from here.
2. Unsure between directions? Build 3–5 plain-HTML variants and let Dainis pick — never ship the first pass.
3. After building: run `/design-deslop` (or `/baseline-ui`), then a live design review on the preview URL (screenshots + Lighthouse; budgets in §9 are blockers).
4. The squint test before handoff: blur your eyes — is there exactly one focal point and a clear reading order? If everything ranks the same, the screen is broken: nothing is accentuated.
5. When in doubt, remove one thing (not add).
