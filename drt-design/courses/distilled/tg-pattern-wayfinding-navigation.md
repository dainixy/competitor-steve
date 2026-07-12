# Tommy Geoco — Making UX Decisions · Patterns: Wayfinding & Navigation

Source: 03-Patterns / 12-Wayfinding and navigation (6 short PDFs). Distilled for practical web UI work: navigation that tells the user *where they are, where they can go, and what they can do* — with restraint (no decorative chrome, minimal persistent overhead, cheap to render).

> Source note: two DON'T/DO tables in the original PDFs were misfiled by the capture tool — the "Priority/progressive" lesson shipped a tooltip table, and the "Off-canvas" lesson duplicated the sticky/fixed table. Rules below are attributed to the correct topic; the stray tooltip rules are kept in an appendix because they are concrete and useful.

## 00 — Wayfinding (framing)

Wayfinding = the user can always answer three questions:
1. **Where am I?** (current location signaled — active states, breadcrumbs, page titles)
2. **How do I get where I want to go?** (visible, predictable navigation)
3. **What can I do here?** (available actions are discoverable)

Good navigation reduces confusion and decision time; it is infrastructure, not decoration. The unit covers five patterns: navigation types/groups, priority + progressive disclosure, off-canvas, sticky vs. fixed, bottom navigation.

## 01 — Types of navigation (three navigation groups)

Classify every nav element into one of three groups before designing layout. Mixing groups in one menu is the most common source of cluttered navigation.

1. **Product / entity navigation** — the primary system for mainline features and product entry points.
   - Use for: main sections ("Dashboard," "Projects," "Library," "Analytics").
   - This is the global nav bar / primary sidebar.
2. **Contextual navigation** — changes based on the user's current context, task, or location.
   - Use for: shortcuts, recently visited pages, related/sub-pages, bookmarks/saved items.
   - Lives near the content it relates to (e.g., in-page sidebar with "Recents" and "Related").
3. **System navigation** — user-specific and app-wide administration.
   - Use for: account, billing, permissions, settings.
   - Tuck behind the profile/avatar dropdown; never let it compete with product nav.

Rules:
- Keep the three groups visually and spatially separate (global bar / local sidebar / profile menu).
- Don't put settings or billing links in the primary nav; don't put product features in the profile menu.
- Contextual nav is the one group allowed to change per page — global and system nav stay constant everywhere.

## 02 — Priority + progressive disclosure in navigation

Show the most important / most frequently used items upfront; keep less common options accessible but initially hidden (hover, click, "More", expandable panels).

Why it works (named principles):
- **Hick's Law** — fewer initial choices = faster decisions, lower cognitive load.
- **Progressive Disclosure** — revealing gradually lets users build a mental model without overwhelm.
- **Recognition over Recall** — visible, clearly labeled options beat menus users must remember.

Rules:
- Surface top-level categories only; reveal subcategories on hover/click.
- Put essential functions in plain sight for new users; advanced/power features behind a "More" dropdown or expandable panel — discoverable, not prominent.
- In editors/toolbars: common actions upfront, advanced tools in an expandable panel.
- Order by frequency of use, not by org chart or alphabet: most-used items first, rare items behind "More."
- Use clear, descriptive labels and icons so users recognize rather than recall.
- Progressive flows: start with basic options, offer advanced settings as the user progresses — don't front-load every setting.
- Responsive: this pattern is how complex nav condenses on small screens — collapse full nav into a menu, but keep primary actions visible (e.g., as bottom-nav icons). Never bury *everything* behind the hamburger.

## 03 — Off-canvas navigation

Main navigation hidden offscreen, revealed by a user action (menu icon tap, edge swipe). Best when screen real estate is scarce (mobile; content-dense desktop views).

When to use:
- **Maximize content space** — hide nav offscreen so the main view is all content.
- **Long navigation lists** — off-canvas holds comprehensive menus without cluttering the interface; organize items into labeled categories inside the panel.
- **Responsive pairing** — visible sidebar on large screens transforms into off-canvas on small screens (same content, different presentation).
- **Contextual panels** — off-canvas isn't only for nav: formatting options, revision history, collaboration tools can live in slide-in panels.

Principle: **Out of sight, out of mind** — hiding complex nav lowers cognitive load during focused tasks, but it also lowers discoverability. That's the trade: only hide what users don't need constantly.

Rules (derived from body text; source table was misfiled):
- Trigger must be an obvious, conventional icon (hamburger/menu) in a consistent position.
- Group items into categories inside the panel — a flat 20-item list defeats the purpose.
- Keep primary actions outside the off-canvas menu (visible bar or bottom nav); off-canvas is for the long tail.
- On desktop with room, prefer a visible sidebar; reserve off-canvas for constrained widths.

## 04 — Sticky vs. fixed navigation

Definitions (use the terms precisely):
- **Sticky** — stays in place until a scroll threshold, then can move off-screen (or: scrolls with page, then pins).
- **Fixed** — stays in the same position regardless of scrolling, always.

When persistent nav earns its keep:
- Key actions reachable from anywhere on a long page (sticky top bar with Create/Search/Notifications).
- Orientation in long content (sticky sidebar showing current section/structure).
- No scroll-to-top tax to navigate between sections.
- Complex tools: fixed top bar for actions + sticky side panel for structure.

Named principles: **Perceived Stability** (consistent nav = sense of stability, lower cognitive load), **Immediacy** (always-available actions), **Spatial Constancy** (fixed positions build muscle memory — keep search/actions in the same spot on every page).

DON'T:
- Make everything sticky or fixed — pin only the most important navigation elements.
- Let sticky/fixed elements cover important content or interactive elements.
- Forget an escape hatch — provide a way for obtrusive persistent nav to get out of the way.
- Apply sticky/fixed inconsistently across similar pages or sections.
- Ignore interaction with form inputs — mobile keyboards + fixed bars collide.

DO:
- Choose sticky vs. fixed deliberately per the interface and content needs (fixed = always-critical actions; sticky = orientation aids that can yield).
- Keep persistent elements small — they must not eat screen space, especially on mobile.
- Visually distinguish pinned elements from scrollable content (border/shadow/background).
- Shrink or add transparency to sticky elements as the user scrolls, to minimize content obstruction.
- **Test the performance impact of sticky/fixed elements, especially on lower-end devices** (position:fixed + effects can cause repaint/jank; keep pinned bars cheap — no heavy blur/shadow stacks, avoid animating layout properties). This is the unit's one explicit performance rule — honor it.

## 05 — Bottom navigation (mobile)

Mobile-first pattern: primary navigation in a bar at the bottom of the screen, icons + labels. Wins because of thumb reach.

Named principles: **Fitts's Law** (bottom placement minimizes reach distance/effort on large phones), **Recognition over Recall** (icons + labels), **Chunking** (3–5 sections make the app's structure memorable).

DON'T:
- Overflow the bar — never more than 5 items; push extras into a "More" menu or other patterns.
- Hide bottom navigation on scroll — it must remain accessible.
- Use bottom navigation on desktop interfaces — it's not a desktop convention.
- Skimp on touch target size for each item.
- Ignore collisions with floating action buttons and the on-screen keyboard.

DO:
- **Limit to 3–5 items** — the hard number for this pattern.
- Pair clear, universally recognized icons with short labels (house = Home, bell = Notifications); icon-only bars force recall.
- Indicate the active state unmistakably.
- Consider a larger central button for the single primary action (e.g., Create/Quick Add).
- Keep the bar identical across all screens — consistency builds muscle memory.
- Populate it with the *most frequently used* features, not one-of-everything.

## Appendix — Tooltip rules (misfiled into this unit's PDFs, kept because concrete)

DON'T: replace main content or convey critical information in tooltips · overuse them (they lose value) · let them obscure content or go off-screen · use jargon · trigger too fast on hover (accidental triggers) · hide too fast when the pointer moves away.
DO: keep tooltip content concise and supplementary · signal discoverability (underline/icon) · position close to the trigger · give content-heavy popovers a clear close button/behavior · use plain language · **make tooltips keyboard-focus triggerable (accessibility)**.

## Top rules from this unit

1. Design so users can always answer: where am I, how do I get there, what can I do here — active states, breadcrumbs, and predictable placement are the mechanism.
2. Sort every nav item into product / contextual / system groups and keep the groups spatially separate; never mix settings into the primary nav.
3. Global and system navigation stay constant on every page; only contextual navigation may change per page.
4. Show the fewest options that cover common tasks first (Hick's Law); put the long tail behind "More" / expandable panels — accessible, not prominent.
5. Order navigation by frequency of use, not internal org structure.
6. Prefer recognition over recall everywhere: descriptive labels + clear icons; never icon-only for primary nav.
7. On small screens, collapse full nav off-canvas but keep primary actions visible (bar or bottom nav) — never bury everything behind a hamburger.
8. Inside off-canvas panels, group items into labeled categories; a long flat list defeats the pattern.
9. On desktop with available width, prefer a visible sidebar over off-canvas; hide nav only when screen space genuinely demands it.
10. Pin (sticky/fixed) only the most important elements — making everything persistent destroys the benefit and eats screen space.
11. Sticky/fixed elements must never cover content or interactive elements; visually distinguish them from scrolling content and shrink them on scroll if they obstruct.
12. Keep pinned element positions identical across similar pages (spatial constancy = muscle memory).
13. Test sticky/fixed elements for performance on low-end devices; keep pinned bars visually cheap to render.
14. Check fixed bars against mobile keyboards and form inputs before shipping.
15. Bottom navigation: 3–5 items maximum, icons + short labels, clear active state, never hidden on scroll, mobile only.
16. Keep bottom nav identical across all screens; consider one larger central button for the app's primary action.
17. Mind touch targets and FAB/keyboard collisions for any bottom-anchored UI.
18. Never put critical information only in a tooltip; tooltips supplement, stay concise, and must be keyboard-focus accessible.
