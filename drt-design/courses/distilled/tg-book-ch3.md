# Making UX Decisions (Tommy Geoco) — pages 201–300

Covers: end of **Module 10 (Checklists for improving fidelity — User Input, Navigation)**, all of **Module 11 (Checklists for improving visual style)**, all of **Module 12 (Checklists for innovating — the 5-level originality spectrum)**, all of **Module 13 (Patterns for chunking)**, and the opening of **Module 14 (Patterns for progressive disclosure — intro + tooltips/popovers)**.

---

## Module 10 (end): Fidelity checklists — User Input & Navigation

### User input (forms, fields, controls)

- Match the control to the data type: calendar picker for dates (never free-text), dropdowns for predefined categories, checkboxes for multi-select, radio for single-select.
- Label every field specifically. "Enter article title", not "Enter text". "Summary Length", not "Length".
- Use placeholder text only for format hints/examples ("Enter tags separated by commas") — never as the label itself.
- Validate in real time: green checkmark on valid input, red inline error on invalid, and the error message must suggest a resolution (e.g. duplicate name → suggest alternatives).
- Enable autofill/autocomplete wherever possible to cut data-entry time.
- Group related inputs logically (all metadata fields together — tags, category, publish date).
- Make interactive input areas visibly clickable and sufficiently large (clear affordances on dropdowns, checkboxes).
- Use progressive disclosure for complex input: show basic fields first, reveal advanced filters on demand.
- Design for all input methods: mouse, touch, keyboard; consider voice on mobile.

### Navigation

- Categorize navigation into distinct kinds and treat them differently: **product navigation** (core sections), **contextual navigation** (within a view), **system navigation** (settings, profile, help).
- Use plain, literal labels ("My Clusters", "Team", "Analytics") — never clever or ambiguous terms.
- Organize nav items by user goals and information hierarchy, not by internal org structure.
- Visually distinguish navigation levels: global nav prominent and persistent (e.g. left sidebar), local nav smaller and contextual (tabs/sub-menus inside a view).
- Show location: breadcrumbs or a clear current-location indicator for any hierarchy deeper than one level ("My Clusters > Marketing Campaign > Blog Post").
- Keep navigation patterns consistent — if a dropdown selects X in one place, use the same pattern for similar selection tasks everywhere.
- Provide shortcuts to frequently used sections (e.g. "Recent items" quick-access).
- Use sticky navigation on long scrolling pages so the main nav stays reachable.
- On small screens, collapse main nav into hamburger/off-canvas/dropdown — plan the responsive collapse, don't improvise it.

---

## Module 11: Checklists for improving visual style

The 8 elements of visual style: **spacing, colors, elevation, iconography, typography, imagery/illustration, motion, texture/patterns.**

### Spacing

- Define a base spacing unit (**8px**) and use only multiples of it (8 / 16 / 24 / 32 …) everywhere. One scale, no ad-hoc values.
- Use spacing to build hierarchy: larger vertical gaps BETWEEN sections than between items WITHIN a section.
- Apply proximity: keep related actions (Edit/Delete/Share) close together, separated from unrelated content.
- Give important elements generous whitespace to make them stand out (e.g. extra padding around the primary CTA).
- Minimum touch targets: **48×48px** with adequate spacing between tappable elements.
- Line spacing (leading) for body text: **~1.5× the font size**, consistent across all body text.
- Adjust density to purpose: tighter spacing in data-dense areas (analytics, tables), more generous in content/reading areas.
- On mobile, reduce inter-card spacing to maximize limited screen real estate — spacing responds to breakpoint, it is not fixed.
- Balance elements against negative space; an editor/reading surface should feel focused and uncluttered.

### Colors

- Limit the core palette to **3–5 colors**; get variety from tints and shades, not new hues.
- Establish a color hierarchy and use it consistently: one primary brand color reserved for important actions/CTAs, neutrals for everything else.
- Contrast minimums (WCAG): **4.5:1 for normal text, 3:1 for large text** — especially check text on colored backgrounds.
- Reserve color as a signal for interactivity: clickable elements (buttons, links) get color treatment static text never gets.
- Use status colors consistently everywhere: green = success, red = error, yellow = warning.
- Use subtle background color differences to group/separate sections.
- Test for color-vision deficiencies (tools: Stark, Color Oracle); never encode meaning in color alone.
- Plan a dark theme that inverts while preserving readability and brand; test colors on multiple devices/lighting.
- Check cultural color associations before shipping to new markets.

### Elevation (shadows/depth)

- Define **3–5 elevation levels** (e.g. subtle / medium / high) and use them consistently — don't invent per-component shadows.
- Elevation must be meaningful, not decorative: higher elevation = interactive or focal (cards, primary buttons); flat = static background.
- Raise elevation on interaction (hover lifts a card) as feedback.
- In dark mode, adjust shadow color/intensity — default shadows disappear or turn harsh on dark backgrounds.
- **Performance rule: use CSS `box-shadow` judiciously, especially on frequently repeated elements** — complex shadows have rendering cost.
- Combine elevation with size and color for the primary action; elevation alone is a weak cue.
- Shadows must never obscure or reduce legibility of underlying content (modals/overlays).

### Iconography

- Pick one icon style (outlined vs solid vs illustrated) with uniform stroke weight and corner radius across the whole set.
- Use universally recognized metaphors for common actions: magnifying glass = search, gear = settings, bell = notifications, plus = add.
- Pair icons with text labels for anything non-universal ("Generate AI Summary", "Export to PDF"). Icon-only is for the top ~10 universal actions.
- Build icons as **SVG** so they scale cleanly at every size.
- Use color in icons purposefully (e.g. brand color only on create/primary actions), not decoratively.
- Ensure icon/background contrast; in dark mode adjust icon colors or add subtle outlines.
- Animate icons sparingly and only as feedback (e.g. save → checkmark tick).
- Every meaningful icon needs descriptive alt text / accessible name for screen readers.
- Use icons to compress meaning (chart-type pickers) — reduce cognitive load, don't add ornament.

### Typography

- One primary typeface with **2–3 weights** (regular, medium, bold). That is the whole system.
- Define a full type scale up front. Reference scale from the book (Cluster, Neue Montreal):
  - H1: 32px / medium
  - H2: 24px / regular
  - Body 1: 14px / medium
  - Body 2: 13px / medium
  - Body 3: 12px / regular
  - Caption: 10px / regular / letter-spacing +10
- Use a **modular scale ratio of 1.2 or 1.25** to relate sizes harmoniously.
- Line length: **50–75 characters** in content areas; line height ~1.5×.
- Contrast: same 4.5:1 / 3:1 minimums as color.
- Letter-spacing: slightly tighter on headings; leave body text at default for readability.
- Weight/style for emphasis is purposeful: bold for primary UI actions, italic for subtle in-text emphasis — not sprinkled.
- Left-align body content (easier reading); center only short headings or buttons.
- Interface must survive user text-enlargement without breaking (accessibility).
- Distinct defined styles for H1/H2/H3, body, and UI text (buttons, labels) — no improvised sizes.

### Imagery & illustrations

- One consistent illustration style + color palette that matches the interface; no mixed styles.
- **Performance rule: compress and properly format every image; optimize for web load times** — assume slow connections.
- Prefer **SVG** for illustrations so they hold quality across resolutions with small file size.
- Every meaningful image gets descriptive alt text.
- Use illustrations to explain complex concepts/processes (onboarding, empty states) — sparingly, so they highlight rather than crowd the real content and functionality.
- Images must earn their place: meaningful, not decorative; if it doesn't add understanding, cut it.
- Represent diverse users if depicting people.
- Micro-animation on illustrations only as functional feedback (e.g. loading state), not ambience.

### Motion & animation

- Animate purposefully only: feedback, state change, progress, spatial orientation. Decorative animation is a cost, not a feature.
- **Micro-interactions (hover states, toggles): 200–300ms.** Short and snappy; anything longer feels sluggish.
- Standardize one animation language: same easing curves and durations for the same interaction types.
- Use motion to explain spatial relationships: a modal animates from its trigger so the user sees where it came from.
- **Respect the OS-level "reduce motion" setting** and offer a static alternative; also provide an in-app option to minimize animation.
- Animation must never block interaction — autosave indicators etc. cannot delay typing or clicks.
- Test on low-end devices; an animation that stutters is worse than no animation.
- In data-heavy sections, keep animation minimal and strictly functional.
- Use loading/progress animations to manage expectations during long operations (with estimated completion where possible).
- Draw attention to changes with subtle highlights (new item added), never disruptive effects.

### Texture & patterns

- If used at all: subtle, low-contrast (e.g. faint noise on a background) — texture adds depth, never noise.
- Never let a pattern sit under critical text/UI; if it does, raise the contrast of what's on top.
- Keep content-heavy areas (editors, reading surfaces) completely clean and pattern-free.
- **Performance rule: use SVG patterns where possible — sharp at all sizes, small files.**
- In dark mode, adjust texture opacity/blending; textures create artifacts when the scheme inverts.
- For a fast, foundation-driven site: textures are the first thing to cut. Everything here is optional polish.

---

## Module 12: Checklists for innovating — the 5-level originality spectrum

The spectrum, least → most original: **1. Direct copies → 2. Remixes → 3. Indirect parallels → 4. Metaphors & analogies → 5. True innovation.**

Rules of thumb:
- Aim for originality but learn from the past; don't reinvent what already works.
- Don't get hung up on being 100% original — **focus on solving problems.** If a standard dropdown works best, use it.
- Never invent a new interaction "for the sake of originality."

### Level 1 — Direct copies
- Copy directly for standard, non-differentiating features users expect to work familiarly: login forms, settings pages, basic navigation, file upload.
- Standard patterns buy familiarity and learnability for free — leverage existing mental models (gear = settings).
- Never rely on copies for the product's core differentiating feature; copy the commodity, design the differentiator.
- Use copies for rapid prototyping and as the baseline benchmark you later improve on.
- Still usability-test copied designs with YOUR users — proven elsewhere ≠ proven here.
- Check legal rights before copying anything unique/trademarked/patented.

### Level 2 — Remixes (combine proven elements from multiple sources)
- Pick elements by proven effectiveness and relevance, then integrate them cohesively — consistent visual style and interaction patterns across the hybrid.
- The remix must genuinely improve on either source alone; if not, use the simpler original.
- Don't force incompatible elements together (data-heavy dashboard + minimalist writing surface serve different needs).
- Test the hybrid thoroughly — combinations create new confusion points; iterate on feedback.
- Verify the remix still plays well with the rest of the interface (search, filters, etc.).

### Level 3 — Indirect parallels (borrow a solution from another domain)
- Look for analogous problems in unrelated fields (library catalogs → content organization; playlists → collections).
- Borrow the **underlying principle**, not the surface UI (from a matching algorithm take "intelligent recommendation," not the swipe cards).
- Weigh innovation payoff vs. learning curve; novel concepts need onboarding.
- Don't force a parallel that doesn't fit real user needs (no game-achievement system in a professional tool).
- Test whether the borrowed concept translates; check cultural portability of the source domain.

### Level 4 — Metaphors & analogies
- Choose metaphors your audience already knows; map product functions to metaphor parts explicitly (garden: create=plant, curate=prune).
- Check the metaphor scales with the roadmap before committing.
- **Don't overextend**: a file-cabinet metaphor works for storage, breaks for real-time collaboration. Stop at the metaphor's useful limit.
- Keep the metaphor consistent across UI, feature names, icons, and docs once adopted.
- Multiple complementary metaphors for different areas are fine (canvas for editor, gallery for showcase).
- The metaphor must never overpromise capability or overshadow actual functionality.
- Watch cultural limits (baseball-diamond stages fail outside the US).

### Level 5 — True innovation
- Only pursue where existing solutions are inadequate or absent; find the unaddressed pain point first.
- Envision the ideal outcome without constraints, then work backwards to what's feasible.
- Expect many failed iterations; budget for extensive prototyping.
- Balance novelty with learnability — if it needs extensive training, it's not done.
- **Don't innovate for innovation's sake** — a complex 3D visualization loses to a simpler solution that meets the need.

---

## Module 13: Patterns for chunking

Chunking = breaking information into smaller units to cut cognitive load. Five patterns: **card layouts, tabs & accordions, grouped form fields, pagination, carousels & sliders.**

### Card-based layouts
Use for collections of similar items (articles, products, projects). Cards support responsiveness (multi-column grid → single column on mobile), modularity (drag/drop/rearrange), and give clear touch targets (whole card tappable). Psychology: chunking, recognition-over-recall (visual cues on cards), proximity (metadata grouped inside the card reads as belonging to it).

DO:
- Consistent card sizes and layouts across the set.
- Clear descriptive title on every card.
- Visual hierarchy inside the card — most important info dominant.
- Whitespace inside cards; never cram.
- Hover states / subtle cues to signal interactivity.

DON'T:
- Overload cards with information or functions.
- Use cards for single linear processes (wrong tool).
- Omit clear calls-to-action in/near cards.
- Style cards inconsistently.
- Skip contrast and keyboard-navigation accessibility.

### Tabs & accordions
Tabs = horizontal headers, one panel visible, good for switching/comparing categories. Accordions = stacked expand/collapse headers, good for hiding detail and advanced options. Both save space and give an overview via visible headers. Psychology: chunking, progressive disclosure, recognition-over-recall.

DO:
- Clear, concise header labels; optionally icons + text.
- Clearly mark the active tab / expanded section.
- Keep each panel's content cohesive with its header.
- Smooth transitions on switch/expand.

DON'T:
- Use tabs/accordions for content users must see simultaneously.
- Nest accordions deeply.
- Use them for sequential tasks that must be consumed in order.
- Overload with too many sections.
- **Hide critical information or primary actions behind tabs or collapsed accordions.**

### Grouped form fields
Group related inputs under a shared container/subheading (e.g. "Details" vs "Settings"). Improves comprehension, cuts cognitive load, helps mobile (one group per screen with navigation between), enables progressive disclosure (collapse advanced groups by default). Psychology: chunking, proximity, progressive disclosure.

DO:
- Clear descriptive label per group.
- Distinguish groups with borders, background color, or spacing.
- Collapsible groups for rarely used options.
- Group in a logical, natural progression.
- Consistent group styling across the app.

DON'T:
- Create too many groups.
- Separate fields commonly used together.
- Group very short forms (adds complexity for nothing).
- Leave group-to-group navigation unclear, especially on mobile.
- Use vague/overbroad group labels.

### Pagination
Split large sets into pages. **Performance benefit is explicit: loading a subset (e.g. 20 items) at a time improves page-load times and reduces server load.** Chunk lists into **10–20 items per page**. Numbered pages give progress sense (Goal-Gradient Effect) and prevent choice overload; paginated content is bookmarkable/shareable at specific points.

DO:
- Show current page and total pages.
- Offer next / previous / first / last navigation.
- Consider a "View All" option.
- Consistent pagination controls everywhere.
- Tune items-per-page to content type and user needs.

DON'T:
- Paginate content meant to be read in its entirety (articles).
- Rely only on Next/Previous for large datasets.
- Lose the user's position when they navigate back to the list.
- Use pagination where infinite scroll fits better (social-style feeds).
- Omit context about what each page contains.

### Carousels & sliders
Carousel = auto-rotating, promotional; slider = user-controlled browsing. Save space, showcase several items, suit visual content (thumbnails, templates). Psychology: curiosity (peek of next item), recency effect, limited choices at a time.

Key rule from the book's comparison figures: **auto-rotating carousels with no user control are the "wrong way"; user-controlled carousels with clear navigation and pause/play are the "right way."** (For a fast, conversion-focused site, default to NOT using carousels for critical content — anything important deserves its own static placement.)
*(Note: the book's printed DO/DON'T list on p.295 erroneously repeats the pagination list — the visual comparison on p.294 carries the actual guidance.)*

---

## Module 14 (start): Patterns for progressive disclosure

Progressive disclosure solves three mental models: **Filtering** (separating signal from noise), **Recall** (limited working memory), **Efficiency** (deciding under time pressure). Origin: IBM's Carroll & Rosson, 1983 — hiding advanced functionality early increased successful use.

- Reveal only essentials first; expand with details on user request; hide infrequently used options until needed.
- Anatomy of any drilldown pattern — design all three parts:
  1. **Trigger** — the behavior that opens it (click, hover).
  2. **Container** — the block holding secondary info (modal, popup, drawer).
  3. **Contextual reference** — a visual link back to the parent view (transparent overlay, breadcrumb) so users keep context without holding it in working memory.
- Six patterns covered by the module: tooltips & popovers, nested menus, expandable rows, drawers & sheets, modals, read-more links.

### Tooltips & popovers (partial — continues past p.300)
- **Tooltip** = hover-triggered, brief explanatory text. **Popover** = click-triggered, can hold richer info or actions.
- Use tooltips to explain unfamiliar features in place; use popovers for detail (e.g. person's role/contact) without navigating away from the main view.

---

## Top rules from this unit

1. Define a base spacing unit (8px) and use only multiples of it — larger gaps between sections than within them; that alone creates hierarchy.
2. Touch targets minimum 48×48px, with real spacing between tappable elements.
3. Contrast minimums: 4.5:1 normal text, 3:1 large text — verify especially on colored backgrounds, and never encode meaning in color alone.
4. Limit the palette to 3–5 core colors; one brand color reserved for primary actions; status colors (green/red/yellow) used identically everywhere.
5. One typeface, 2–3 weights, a defined modular scale (ratio 1.2–1.25); body text ~1.5× line height, 50–75 characters per line, left-aligned.
6. Labels are literal and specific — "Enter article title" not "Enter text"; nav labels plain, never clever.
7. Validate forms in real time with inline errors that suggest a fix; match every input control to its data type (date picker for dates, etc.).
8. Define 3–5 elevation levels and make elevation mean something (interactive/focal vs static); use box-shadow judiciously on repeated elements — shadows have rendering cost.
9. Micro-interactions run 200–300ms with standardized easing; animation exists only for feedback, progress, and spatial orientation — decorative motion is cut.
10. Respect the OS "reduce motion" setting and never let animation block interaction; test motion on low-end devices.
11. Compress and web-optimize every image; prefer SVG for icons, illustrations, and patterns (sharp at any size, small files).
12. Icons: one style, uniform stroke; universal metaphors only for icon-only buttons; everything else gets a text label; all icons get accessible names.
13. Don't be original about commodities: directly copy standard patterns (login, settings, nav, upload) and spend design effort only on the differentiating feature.
14. Never invent a new interaction for originality's sake — solve the problem; if a standard dropdown works, ship the dropdown.
15. Never hide critical information or primary actions behind tabs, collapsed accordions, tooltips, or any progressive-disclosure container.
16. Paginate large lists at 10–20 items per page — it's a stated performance win (faster loads, less server work); show current/total pages and preserve position on back-navigation.
17. Auto-rotating carousels with no user control are the wrong way; if you must use one, make it user-controlled with pause/play — and keep critical content out of carousels entirely.
18. Group related form fields under clear labels with visual separation; collapse advanced/rare options by default; don't group short forms.
19. Every drilldown (modal, popover, drawer) needs three designed parts: trigger, container, and a contextual reference back to the parent view.
20. Textures/patterns are optional polish: subtle, never under text, never in content areas, first thing to cut for speed.
