# Visual Hierarchy — Patterns (Tommy Geoco, Making UX Decisions)

Source: `03-Patterns/04-Visual hierarchy` (6 PDFs). Core claim: visual hierarchy guides attention, signals importance and relationships between elements, and reduces cognitive load. The module's five levers are **Typography, Color & contrast, Whitespace & grouping, Size & scale, Proximity & alignment**. All five are cheap, CSS-only, zero-JS techniques — hierarchy is achieved with structure, not effects.

## 00 — Visual hierarchy (overview)

- Hierarchy = making importance and relationships visible so users don't have to think. Every screen should answer "what do I look at first, second, third" without instructions.
- The five patterns are combinable; a cluttered layout is usually fixed by applying several at once (the course demo takes one messy dashboard and applies each pattern in turn).
- Decision frame: before adding any element, decide its rank in the hierarchy; style it by rank, not by whim.

## 01 — Typography

What it buys you: information hierarchy, readability, brand identity, and attention direction — with fonts alone.

**Rules (imperative):**
- Establish a clear typographic hierarchy: distinct, reusable styles for headers, subheaders, body text, and UI elements. Large+bold for page/section titles, slightly smaller for section headers, standard size for body.
- Differentiate text levels using font weight, size, AND color together — never rely on color alone (fails for color-blind users).
- Use a clean sans-serif for interface text; it stays legible across screen sizes and resolutions.
- Keep typography consistent: the same kind of information always gets the same style everywhere (all card titles identical, all metadata identical). Consistency is what reduces cognitive load.
- Make important interactive text larger and well-spaced — larger text is an easier target (Fitts's Law), especially on touch.
- Give a distinct style to attention-critical elements (primary CTA, system/AI-generated content) so they are visually separable from surrounding content (visual saliency).
- Ensure sufficient contrast between text and background — readability beats aesthetics, always.
- Use responsive typography that adjusts with screen size; test on multiple devices.

**Don'ts:**
- Don't use many fonts or many styles — visual chaos. (Practical ceiling: one or two typefaces, a small fixed set of size/weight styles.)
- Don't sacrifice readability for an aesthetic font choice.
- Don't pick fonts that are nearly identical to each other — subtle differences confuse rather than differentiate.
- Don't skip cross-device testing of type.

**Named principles:** Visual Saliency (standout type gets noticed), Fitts's Law (bigger text = easier target), Cognitive Load Theory (consistent type = less mental effort).

## 02 — Color and contrast

What it buys you: attention direction, visual grouping, brand recognition, legibility.

**Rules (imperative):**
- Reserve one vibrant, high-contrast color for the primary action on a screen; everything else stays quiet. Contrast is a budget — spend it on what matters most.
- Use color to group: give related features/sections a consistent shared color treatment, and keep it different from unrelated areas (Gestalt similarity — same color reads as same group).
- Use a unique high-contrast treatment for new/unread/alert items so they're noticed and remembered (Von Restorff effect: the one different thing is what people remember).
- Ensure high text/background contrast everywhere, and especially in long-reading surfaces (editors, articles).
- Use color to distinguish interactive elements from static ones — links/buttons should look actionable.
- Build one consistent color scheme tied to the brand; use each color for a consistent meaning (a given color always means the same action/state).
- Match color mood to the surface's job (calm blues/greens for focus-and-work areas — color psychology).
- Design for color blindness: pair every color signal with a second cue (icon, label, weight, position).
- Test the palette under different lighting conditions.

**Don'ts:**
- Don't rely on color alone to convey important information.
- Don't use many colors — clutter. Few colors, used purposefully.
- Don't use vibrating/discomforting color combinations (high-saturation complementary pairs).
- Don't use colors that fight common UI conventions (e.g., red for success) or clash with the brand.

**Named principles:** Von Restorff Effect (the contrasting item is noticed/remembered), Color Psychology (colors carry mood), Gestalt Similarity (same color = same group).

## 03 — Whitespace and grouping

What it buys you: readability, hierarchy, organization, and a clean/professional feel — using literally nothing (empty space is free and weighs 0 KB).

**Rules (imperative):**
- Use generous line spacing and paragraph margins for long-form text — whitespace inside text blocks is a readability feature, not waste.
- Put MORE whitespace around the most important elements (primary CTA) — isolation is emphasis.
- Separate distinct content blocks (cards, sections) with clear space; group related info tightly WITHIN each block. Space between groups must be visibly larger than space within groups.
- Keep spacing consistent across the whole interface — pick a spacing scale and reuse it; inconsistent gaps read as visual confusion.
- Prefer whitespace over borders/lines/boxes for grouping — reach for a divider only when space alone can't do the job.
- Give small elements (form fields, buttons) breathing room too — whitespace discipline applies at every size.
- Break up long lists with spacing so they can be scanned in chunks (cognitive load).
- Use subtle background shifts plus ample surrounding whitespace to make the main content area read as figure against ground.
- Plan how spacing/grouping compresses across screen sizes.

**Don'ts:**
- Don't overcrowd — too many elements on one surface is the root failure.
- Don't cut necessary information just to manufacture whitespace — clarity of content still wins.
- Don't box everything in borders when spacing would group it more cleanly.

**Named principles:** Gestalt Proximity (close = related, far = separate), Cognitive Load Theory (organized space = less effort), Figure-Ground (space makes content pop from background).

## 04 — Size and scale

What it buys you: attention direction, rank ordering, usability (touch), and layout structure.

**Rules (imperative):**
- Make the primary action visibly larger than secondary actions — size is read as importance.
- Make touch/click targets at least **44×44 px** on mobile; make frequently used buttons slightly larger than rare ones (Fitts's Law).
- Use a fixed sizing scale (e.g., small / medium / large tokens) instead of ad-hoc sizes — consistency is what makes size legible as a signal.
- Apply size by rank: progressively smaller text for heading → subheading → body creates the information structure by itself.
- Size data by importance: key metrics get the big numbers/charts; secondary metrics get small ones.
- Size cards/thumbnails by priority or recency when a grid needs an importance order.
- Keep size consistent for equal-importance elements across the interface — same rank, same size, everywhere.
- Balance the composition when changing one element's size — size changes ripple through the layout.
- Coordinate size with color and position; the signals must agree, not compete.
- Test size choices across screen sizes and resolutions.

**Don'ts:**
- Don't make important elements too small to notice or hit.
- Don't use many different sizes — visual chaos; a small scale is enough.
- Don't assume bigger is always better — subtle size differences are often more effective than shouting.

**Named principles:** Visual Saliency (bigger = noticed first), Fitts's Law (bigger targets = faster, easier interaction), Information Processing Theory (size cues speed up triage of what matters).

## 05 — Proximity and alignment

What it buys you: logical grouping, scanability, order/professional feel, visible parent-child relationships.

**Rules (imperative):**
- Group related controls physically together and separate them from unrelated ones (formatting tools together, away from save/share). Distance encodes relationship.
- Keep destructive or unrelated actions physically apart from routine ones — closeness creates false association.
- Left-align repeated items (titles in lists/dashboards) so the eye scans down one clean line.
- Pick one alignment strategy (e.g., left-aligned text) and use it consistently across the interface; mixed alignments without purpose = chaos.
- Use indentation to show hierarchy (parent/child, member/role).
- Align related actions ("Move / Copy / Delete") into one cluster so they read as one action group.
- Use a grid system to enforce consistent spacing and alignment rather than eyeballing.
- Align form labels with their fields so the label-field association is unambiguous.
- Mind alignment on small elements too — icons and buttons that sit a few pixels off read as sloppy.
- Check both horizontal AND vertical alignment.
- Re-verify proximity/alignment at every breakpoint and orientation — groupings must survive reflow.

**Don'ts:**
- Don't place unrelated elements close together (false grouping).
- Don't sacrifice readability to force alignment.

**Named principles:** Gestalt Proximity (near = related), Gestalt Continuation (aligned edges guide the eye), Law of Prägnanz (orderly layouts are perceived as simpler and easier).

## Top rules from this unit

1. Rank first, style second: decide every element's importance rank, then assign type size/weight, color, size, and spacing by rank — never ad hoc.
2. One primary action per screen gets the contrast: a single vibrant high-contrast CTA; all other elements stay visually quiet.
3. Never rely on color alone for meaning — always pair it with a second cue (weight, icon, label, position); this covers color-blind users for free.
4. Space-between-groups > space-within-groups: related items tight together, unrelated items clearly apart — this one ratio does most of the grouping work.
5. Prefer whitespace over borders and boxes for grouping; add a line only when space can't do it.
6. Isolation is emphasis: surround the most important element with MORE empty space instead of decorating it.
7. Build a small fixed typographic system (1-2 typefaces; distinct styles for header/subheader/body/UI) and apply it identically everywhere — consistency is what cuts cognitive load.
8. Use a fixed sizing scale (small/medium/large) and a fixed spacing scale; too many distinct sizes or gaps reads as chaos.
9. Touch targets ≥ 44×44 px; make frequently used buttons slightly larger (Fitts's Law).
10. Same rank = same style everywhere: all card titles identical, all metadata identical, a given color always means the same thing.
11. Left-align repeated content into one clean scannable edge; use one consistent alignment strategy across the whole UI.
12. Use a grid — enforce alignment and spacing systematically; check horizontal and vertical alignment, including on icons and small controls.
13. Distance encodes relationship: never put unrelated (especially destructive) actions next to routine ones — closeness creates false associations.
14. Interactive elements must LOOK interactive — differentiate them from static content via color/weight, consistently.
15. Text/background contrast is non-negotiable; readability beats every aesthetic choice.
16. Subtle beats shouting: small, consistent size differences signal hierarchy better than making things huge; bigger is not always better.
17. Show hierarchy structurally — heading/subheading/body size steps and indentation — before reaching for any decorative device.
18. Follow platform color conventions (red = danger, green = success); don't fight learned meanings.
19. Never cut necessary content just to create whitespace, and never sacrifice readability to force alignment — clarity outranks tidiness.
20. Re-test hierarchy at every breakpoint: type scale, spacing, groupings, and target sizes must all survive reflow to small screens.
