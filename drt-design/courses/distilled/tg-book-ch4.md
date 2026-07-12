# Making UX Decisions (Tommy Geoco) — pages 301-400

**Page range covered:** PDF pages 301-400 of 603.
**Chapters in this range:** Module 14 "Patterns for progressive disclosure" (second half: tooltips/popovers guidelines, nested menus, expandable rows, drawers & sheets, modals, read-more links — pp. 301-330), Module 15 "Patterns for cognitive load" (pp. 331-358), Module 16 "Patterns for visual hierarchy" (pp. 359-387), Module 17 "Patterns for social proof" (start: intro, testimonials & reviews, user-generated content — pp. 388-400, module continues past 400).
Notes for merge: many pages are reference-image pages ("Wrong way vs Right way" comparisons); captions captured below. The book's running example app is "Cluster" (a fictional AI content-management tool) — product specifics dropped, rules kept.

---

## Module 14 — Patterns for progressive disclosure (continued)

Progressive disclosure = show only what's needed now; reveal detail on demand. The book grounds every pattern in three psychological jobs: **Filtering** (hide the irrelevant), **Recall** (interface as external memory — users shouldn't have to memorize), **Efficiency** (fast path to detail when wanted). Every pattern below trades a click/hover for a cleaner, faster first paint — aligned with lightweight, no-clutter design.

### Tooltips & popovers
Use for: extra context without spending screen space; defining unfamiliar terms; showing extra data on click (e.g. mini profile on a username); reminding users of shortcuts/icon meanings.

**Do**
- Keep tooltip content concise; it must *supplement* the main content, never replace it.
- Make tooltips discoverable with visual cues (dotted underline, info icon).
- Position tooltips/popovers close to their trigger element.
- Give content-heavy popovers a clear close button or dismiss behavior.
- Use plain language — no jargon in tooltip text.
- Ensure tooltips can be triggered via keyboard focus (accessibility requirement).

**Don't**
- Put critical or essential information only in a tooltip.
- Overuse tooltips — they lose value when everywhere.
- Let tooltips obscure other important content or run off-screen.
- Trigger tooltips instantly on hover (causes accidental triggers — add a short delay).
- Hide the tooltip too quickly after the pointer moves away.

### Nested menus
Use for: hierarchical navigation in broad+deep architectures; fast access to deep content; step-by-step filtering (each level hides irrelevant options).

**Do**
- **Limit menu depth to 2-3 levels.** Beyond that, complexity rises and users get lost.
- Use clear, concise category labels; order items logically (by priority, alphabetically, or by theme).
- Provide escape hatches: Back button or breadcrumbs to move up levels.
- Keep menu style, behavior, and location consistent site-wide.

**Don't**
- Mix different category types at the same level — keep each level thematically consistent.
- Use nested menus for primary navigation unless the information architecture justifies it.
- Create a category containing only one item (collapse the level instead).
- Make hover areas too small — sub-menus become hard to reach.
- Put actions (Delete, Edit) inside navigation menus — menus are for navigation only.

### Expandable rows / accordion sections
Use for: scannable summaries with drill-down (project lists, advanced settings, help docs); reducing scrolling on mobile; hiding advanced options from novices while keeping them reachable for power users; focusing attention on critical content by collapsing the rest.

**Do**
- Write clear, descriptive headers that accurately summarize the hidden content.
- Visually distinguish expandable headers from static content; show an obvious expand/collapse icon.
- Keep expanded content scannable (sub-headers, spacing).
- Animate expansion smoothly — a brief functional transition to maintain context, not decoration.
- **Default a section to expanded if the majority of users need its content.**

**Don't**
- Nest expandable sections many levels deep.
- Hide information most users need inside a collapsed section.
- Expand all sections by default — that forfeits the benefit of progressive disclosure.
- Use vague or misleading header titles.
- Make the expand/collapse click target too small.
- Skip keyboard accessibility for expand/collapse.

### Drawers & sheets (edge-anchored overlays)
Use for: navigation menus (side drawer), filtering controls (right-side drawer), create/edit surfaces (bottom sheet on mobile), contextual action lists (Edit/Share/Move/Delete on a selected item) — all while keeping the main view visible for context.

**Do**
- Use drawers for top-level navigation or filter controls; use sheets for creating, editing, or displaying extra info about an item.
- Always provide a clear dismiss: close button and tap-outside.
- Keep the main view partially visible to maintain context.
- Use clear, concise labels for navigation items in drawers.
- For content-heavy overlays, prefer a bottom drawer over a small sheet.

**Don't**
- Overload a drawer/sheet with options — it becomes overwhelming.
- Put essential always-needed content in a drawer.
- Nest drawers/sheets inside each other.
- Show ads or unrelated content in them.
- Auto-dismiss on item selection if further interaction is likely.
- Use a drawer as the app's main content area.

### Modals
Modals dim and block the whole interface — the most expensive attention pattern. Reserve for genuinely critical moments.

Use for: confirming destructive/irreversible actions (with consequences explained); short focused edits without losing page context; media previews without navigation.

**Do**
- **Use modals sparingly — only for the most important information or actions.**
- Provide a visible close button; also allow Esc key and click-outside to close.
- Size the modal properly and center it; darken the background to hold attention.
- Use action-oriented button labels ("Save", "Delete") — never vague "OK".
- Keep the modal focused on a single task with only the necessary fields.

**Don't**
- Use a modal for nonessential info that could be displayed inline.
- Include more than one main action (or many secondary actions).
- Make the modal so large it fills most of the viewport.
- Nest modals (open a second on top of the first).
- Ship without testing keyboard navigation and keyboard close.

### "Read more" links / truncation
Use for: text-heavy listings (cards, feeds, summaries) where full text would overwhelm; improves scannability and keeps the initial page short and concise.

**Do**
- Truncate so the excerpt gives enough context to judge interest.
- Use action-specific link text ("Read full article"), never vague "More…".
- Place the link at the end of the excerpt; consider making the whole excerpt/title clickable too.
- Expand/collapse in place with a smooth transition; provide a way to re-collapse near the end of expanded content (don't force scrolling back up).
- If the link navigates to a new page instead of expanding inline, make that obvious (warn/label it).

**Don't**
- Cut the excerpt mid-sentence or mid-thought — jarring.
- Hide information essential to understanding the main content.
- Use read-more on content already short enough to show fully.
- Let expanded content shove other page elements around disorientingly (layout-shift / CLS concern).

---

## Module 15 — Patterns for cognitive load

Cognitive load = mental effort required to process information and complete tasks. Every pattern here reduces the amount shown/asked at once. This module is the book's most direct support for lean, fast pages: fewer options, fewer fields, smaller payloads per view. Patterns: pagination & infinite scroll, steppers & wizards, minimalist navigation, chunked lists, simplified forms.

### Pagination vs. infinite scroll
Both chunk large datasets into manageable amounts. **Performance benefit is explicit in the book: loading only a subset at a time significantly improves page-load time and reduces server load.**

Decision criteria:
- **Use pagination when** the task is goal-oriented — users need to find a specific item, know their position and total, or reach the end (search results, reports, historical data). Numbered pages also give a sense of progress.
- **Use infinite scroll when** browsing is exploratory and continuous (discovery/activity feeds).

**Do**
- For pagination: clearly indicate current position and total content; provide next/prev/first/last navigation; consider a "View all" option where appropriate.
- For infinite scroll: show a clear loading indicator.
- Tune items-per-page/per-load to content type and user need (book's example: ~10-20 items per page).
- Preserve the user's position when they navigate back to a paginated or infinitely-scrolled list.
- Provide context about the content in each page/scroll load.

**Don't**
- Paginate content meant to be consumed whole (e.g. a single article).
- Use infinite scroll without a way to return to a specific point.
- Use infinite scroll for goal-oriented tasks or when users need to reach a specific item or the end of the list.

### Steppers & wizards
Break complex processes/forms into sequential steps: one decision set at a time. Improves completion rates (Goal-Gradient Effect: users are motivated as they see progress), reduces errors and overlooked information.

**Do**
- Label each step clearly with a brief description of what's required.
- Show current position and how many steps remain (progress bar / completed-step markers).
- Allow reviewing and editing previous steps where possible.
- Provide clear Next and Back navigation.
- For long processes, provide a way to save progress and return later.
- Progressively disclose advanced options within steps — basics first.

**Don't**
- Include too many steps — the process feels overwhelming.
- Force strict step order when it isn't necessary.
- Hide important information inside optional steps.
- Use ambiguous or technical language in step descriptions.

### Minimalist navigation
Present only essential navigation options. Grounded in **Hick's Law** (decision time increases with the number and complexity of choices) and **signal-to-noise ratio** (emphasize important elements, reduce distractions). Especially valuable on mobile and in focused work surfaces.

**Do**
- Prioritize the most important and most frequently used items in primary nav (book's examples use 4-5 top-level items, e.g. Dashboard / Projects / Team / Settings).
- Use clear, concise labels; icons may accompany or replace text on mobile — only if unambiguous.
- Provide easy access to a more comprehensive menu for everything else.
- Ensure all key areas remain reachable, even if via secondary navigation.
- On mobile, prefer a bottom nav bar with only crucial options; hide less-used features in a menu.
- In editors/focused tasks, strip navigation to keep attention on the work.
- For onboarding, start users with the simplified structure and reveal advanced options gradually.

**Don't**
- Oversimplify to the point of obscuring necessary functions.
- Use ambiguous icons without labels.
- Apply the same minimal nav to all user types if advanced users need quick access to more options.
- Skip user-testing the slimmed-down navigation.

### Chunked lists
Break long lists into smaller labeled groups. Grounded in **Miller's Law** (average person holds ~7±2 items in working memory) and the **Gestalt principle of proximity**. Improves comprehension, scannability, recall; reduces overwhelm.

**Do**
- Group by logical categories/relationships that match user expectations (e.g. "To Do / In Progress / Completed").
- Use clear headings or visual separators between chunks.
- **Keep chunks to roughly 5-9 items each**; keep main navigation to no more than 5-9 categories.
- Provide a way to view all items at once if users need it.
- Consider letting users customize the grouping where appropriate.
- Verify chunking works across screen sizes and devices.

**Don't**
- Make chunks so large they defeat the purpose.
- Use arbitrary or confusing groupings that don't align with user expectations.
- Chunk short lists that don't need it.

### Simplified forms
Collect only essential information; use smart defaults; break complex forms into manageable steps. Simpler forms → higher completion rates, fewer errors, faster data entry, more respect for the user's time.

**Do**
- Ask only for essential fields; make the rest optional or deferred (e.g. registration asks for essentials now, details later; quick-add asks only title + URL).
- Use clear, concise labels.
- Implement smart defaults, pre-filled suggestions, and auto-fill wherever possible.
- Break long forms into steps or sections.
- Provide clear error messages with guidance for correction.
- Align fields and labels for easy scanning; optimize for mobile.
- Prefer a smart/searchable input over a very long dropdown (Hick's Law).
- Reveal additional fields only when relevant, based on previous answers (progressive disclosure in forms).

**Don't**
- Ask for information that isn't necessary or immediately useful.
- Use complex, technical language in labels or instructions.
- Pile on optional fields — progressively disclose instead.
- Neglect field/label alignment or mobile optimization.

---

## Module 16 — Patterns for visual hierarchy

Visual hierarchy guides attention and communicates importance and relationships between elements. Five levers: typography, color & contrast, whitespace & grouping, size & scale, proximity & alignment. All five are zero-cost in bytes — hierarchy comes from structure, not assets.

### Typography
**Do**
- Establish a clear typographic hierarchy: distinct styles for headers, subheaders, body text, and UI elements (e.g. large bold page title → slightly smaller section headers → standard body).
- Differentiate text using weight, size, AND color together — not one channel alone.
- Ensure sufficient contrast between text and background for readability.
- Keep typography consistent across the interface: the same information type always uses the same style (consistency itself reduces cognitive load).
- Use responsive typography that adjusts to screen size.
- Prefer a clean sans-serif for interface text (readability across screen sizes/resolutions).
- Make tappable text elements large and well-spaced on touch devices (Fitts's Law).
- A distinct type treatment can flag special content (e.g. AI-generated vs user-written) — visual saliency.

**Don't**
- Use too many fonts or styles — visual chaos.
- Sacrifice readability for aesthetic choices.
- Rely solely on color to differentiate text (problematic for color-blind users).
- Pair fonts that are too similar — subtle differences confuse.
- Skip testing typography across devices and screen sizes.

### Color & contrast
**Do**
- Use color *purposefully* to guide attention and create hierarchy: one bright, contrasting color for the primary CTA; a muted palette for backgrounds and cards (calm, focused environment).
- Ensure sufficient text/background contrast (readability, long-session comfort).
- Create one consistent color scheme aligned with the brand; use the same color consistently for the same action/information type.
- Use color to differentiate interactive from static elements.
- Account for color blindness and other visual impairments in every color choice.
- Use similar colors to visually group related elements (Gestalt similarity); reserve one unique high-contrast color for the thing that must be noticed (Von Restorff effect — e.g. unread notifications).

**Don't**
- Rely solely on color to convey important information.
- Use too many colors — visual clutter.
- Choose combinations that vibrate or create visual discomfort.
- Clash with common UI conventions or the brand.
- Skip testing the scheme under different lighting conditions.

### Whitespace & grouping
Whitespace (negative space) is a structural tool, not wasted space: it improves readability, creates hierarchy, organizes information, and reads as clean/modern/professional — all for free.

**Do**
- Use consistent spacing throughout the interface.
- Group related elements tightly; separate unrelated ones with more space (Gestalt proximity).
- Give important elements and CTAs extra surrounding whitespace to make them stand out.
- Use generous line spacing and paragraph margins for long-form text readability.
- Use whitespace to break up long lists for easier scanning.
- Apply whitespace inside small components too (form fields, buttons).
- Check spacing behavior across screen sizes.
- A border or background tint can group related settings — but see the don't below.

**Don't**
- Overcrowd the interface with too many elements.
- Use inconsistent spacing — it creates visual confusion.
- Default to borders/lines for grouping when whitespace alone would be more effective (prefer space over chrome).
- Sacrifice necessary information just to add whitespace.

### Size & scale
Larger elements are noticed first and perceived as more important (visual saliency); larger targets are easier to hit (Fitts's Law); progressive size steps encode structure (information processing).

**Do**
- Use size consistently as an importance signal across the whole interface.
- Make the primary action visibly larger than secondary actions.
- **Make interactive elements at least 44x44 px on touch devices.**
- Use a fixed sizing scale (e.g. small/medium/large tokens) for consistency.
- Step heading → subheading → body sizes down progressively to create clear structure.
- Make key metrics/numbers/charts larger on dashboards so they're immediately noticeable.
- Use larger thumbnails for high-priority content, smaller for less crucial items.
- Test size choices across screen sizes and resolutions; consider layout balance when adjusting sizes.

**Don't**
- Make important elements too small to notice or interact with.
- Use too many different sizes — visual chaos.
- Ignore the impact of size on overall layout and composition.
- Assume bigger is always better — subtle size differences are sometimes more effective.
- Treat size in isolation from color and position.

### Proximity & alignment
Proximity = spatial relationships communicate grouping; alignment = clean lines guide the eye and read as order.

**Do**
- Group related elements together and separate unrelated ones (e.g. formatting tools together, away from save/share).
- Use consistent alignment throughout — left-aligned text as the default.
- Consider both horizontal and vertical alignment.
- **Use a grid system** to ensure consistent spacing and alignment.
- Align form labels with their fields to create clear associations.
- Place paired actions adjacent and aligned (e.g. Save + Cancel next to each other, right-aligned in a modal).
- Use indentation to show hierarchical relationships (e.g. team members under roles).

**Don't**
- Place unrelated elements too close together — creates false associations.
- Mix different alignments without a clear purpose — visual chaos.
- Ignore alignment on small elements (icons, buttons).
- Sacrifice readability for the sake of alignment.
- Forget to re-check proximity/alignment across screen sizes and orientations.

### Named principles used in this range (one-liners)
- **Hick's Law** — decision time grows with the number/complexity of choices; cut options.
- **Miller's Law** — working memory holds ~7±2 items; chunk accordingly.
- **Fitts's Law** — bigger/closer targets are faster to hit; size interactive elements up.
- **Von Restorff effect** — the one different-looking item gets noticed and remembered; reserve the standout treatment.
- **Gestalt proximity / similarity / continuation** — closeness, matching color, and alignment all read as "related".
- **Law of Prägnanz** — well-organized, aligned layouts are perceived as simpler; order lowers cognitive load.
- **Figure-ground** — whitespace around content separates foreground from background, improving focus.
- **Goal-Gradient effect** — visible progress toward a goal increases motivation to finish.
- **Signal-to-noise ratio** — emphasize the important (signal), remove distraction (noise).
- **Chunking / Cognitive Load Theory** — grouped, reduced information is easier to process and remember.

---

## Module 17 — Patterns for social proof (start; continues past p. 400)

Social proof = people look to others' actions to guide their own decisions, especially in uncertain situations. Module patterns: testimonials & reviews, user-generated content, social media integration, badges & seals (the last two fall after p. 400).

### Testimonials & reviews
Use for: building trust on landing/pricing pages; addressing common objections; leveraging Authority (known companies/industry experts) and the Bandwagon effect (usage counters, average ratings, review counts). Placement guidance from examples: recognizable-name testimonials on the homepage; average rating + review count at the pricing/decision point; detailed case studies for enterprise buyers.

**Do**
- Use authentic, verifiable testimonials from real users — always get permission first.
- Prefer specific, detailed feedback over generic praise; mix short quotes with detailed testimonials/case studies.
- Show average rating + total number of reviews where the buying decision happens.
- Feature testimonials that directly address common concerns/objections.
- Update testimonials and reviews regularly to keep them current.
- Include user ratings alongside written reviews when possible.

**Don't**
- Use fake or misleading testimonials, or obvious stock-photo faces / unrelated testimonials.
- Ignore or hide negative reviews.
- Overwhelm users with too many testimonials at once.
- Use overly complex language or jargon in testimonials.

### User-generated content (UGC)
Use for: authenticity (unfiltered real perspectives), engagement (peers' content motivates contribution), fresh content, diverse use cases (community feeds, highlighted contributions, "X of the week" showcases, contributor recognition). Psychology: social proof, belongingness (community), IKEA effect (users value what they helped build — e.g. shareable user-made templates).

**Do**
- Provide clear guidelines for UGC submissions.
- Implement a moderation system for quality and appropriateness before showcasing.
- Make creating and sharing content easy; showcase high-quality UGC prominently.
- Encourage contribution through incentives, recognition, or gamification.

**Don't**
- Use UGC without user permission.
- Ignore the potential for misuse or inappropriate content.
- Overwhelm the interface with UGC.
- Forget to engage with contributors; don't let showcased UGC go stale — remove outdated items.

---

## Top rules from this unit

1. **Reserve modals for critical moments only** (destructive confirmations, focused single tasks); one primary action per modal, action-verb button labels ("Delete", not "OK"), closable via button, Esc, and click-outside.
2. **Limit nested menu depth to 2-3 levels**; never put actions (Edit/Delete) inside navigation menus, and never create a category with a single item.
3. **Never put essential information behind progressive disclosure** — tooltips, collapsed sections, drawers, and read-more links are for supplementary content only.
4. **Default expandable sections open when most users need them, closed otherwise** — all-open and all-closed both defeat the pattern.
5. **Paginate goal-oriented lists; infinite-scroll only exploratory feeds** — and always preserve list position on back-navigation. Loading subsets at a time explicitly improves page-load performance and server load.
6. **Show ~10-20 items per page/load** and chunk lists into groups of **5-9 items** with clear headings (Miller's Law); cap top-level nav at 5-9 categories, ideally 4-5.
7. **Cut navigation to essential items** (Hick's Law): fewer choices = faster decisions; keep everything else reachable via secondary nav, and never use ambiguous icons without labels.
8. **Forms: ask only what's essential now**; smart defaults + pre-fill + auto-fill; break long forms into steps; reveal advanced fields only when relevant to prior answers.
9. **Steppers: show position + steps remaining, allow back-editing, allow save-and-resume** on long flows; visible progress raises completion (Goal-Gradient Effect).
10. **Build text hierarchy from a few distinct, consistently applied styles** (header/subheader/body/UI); differentiate with weight + size + color together; too many fonts or sizes = visual chaos.
11. **One vibrant contrast color for the primary CTA, muted palette everywhere else**; the same color always means the same thing; too many colors = clutter.
12. **Never rely on color alone** to convey information (color-blind users); always ensure sufficient text/background contrast.
13. **Prefer whitespace over borders/boxes for grouping**; consistent spacing everywhere; extra whitespace around CTAs makes them stand out at zero byte cost.
14. **Group related, separate unrelated** (Gestalt proximity); adjacency creates association — false proximity creates false associations.
15. **Left-align text, align labels to fields, use a grid system**; consistent alignment reads as simplicity (Prägnanz) and improves scannability.
16. **Touch targets ≥ 44x44 px**; primary action larger than secondary; use a fixed sizing scale (S/M/L) rather than ad-hoc sizes; subtle size differences often beat huge ones.
17. **Make every disclosure interaction keyboard-accessible** (tooltips on focus, accordion toggle, modal close) — stated as a requirement for each pattern in this unit.
18. **Avoid layout shift from disclosure**: expanded content must not shove page elements around disorientingly; position tooltips/popovers next to triggers without covering important content (CLS-relevant).
19. **Never use vague trigger text** — "Read full article" not "More…", "Save"/"Delete" not "OK"; every link/button label states its action; warn when a link navigates instead of expanding.
20. **Consistency is the meta-rule of this unit**: same menu behavior everywhere, same type styles for the same content class, same spacing scale, same size scale, same color meanings — every inconsistency is added cognitive load.
21. **Social proof must be authentic and specific**: real, permissioned, current testimonials with ratings + counts at decision points; never fake quotes or stock faces; don't hide negative reviews; moderate and curate UGC before showcasing it.
