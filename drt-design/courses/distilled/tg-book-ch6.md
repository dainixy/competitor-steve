# Making UX Decisions (Tommy Geoco) — Pages 501-603

Covers: end of **Module 21 (Patterns for personalization)** (pp. 501-522), **Module 22 (Patterns for onboarding and learning)** (pp. 523-550), **Module 23 (Patterns for information relationships)** (pp. 551-575), **Module 24 (Patterns for wayfinding and navigation)** (pp. 576-596), **Module 25 (How to grow from here — the ceiling of design patterns)** (pp. 597-603).

Every pattern module follows the same template: definition → benefits/use cases → psychological principles → Do/Don't implementation guidelines. The Do/Don't lists are the actionable core; they are preserved in full below.

---

## Module 21 (tail): Patterns for personalization

### Customizable dashboards (Do/Don't tail)
DO:
- Provide an intuitive drag-and-drop interface for dashboard customization.
- Offer a mix of pre-designed templates and fully customizable options.
- Allow users to save multiple dashboard configurations.
- Ensure all essential functions are available even if not displayed by default.
- Provide clear instructions or a tour explaining how to customize.

DON'T:
- Overwhelm users with too many customization options.
- Make it difficult to reset to a default configuration.
- Forget to save user preferences across sessions and devices.
- Hide critical features or notifications in the pursuit of customization.
- **Neglect performance optimization when loading customized dashboards** (customization must not slow load).

### Adaptive content
Definition: dynamically adjust content/layout/functionality from user behavior, preferences, or context — personalization without explicit user configuration.
Named principles: Relevance Theory (people focus on what's relevant now), Cognitive Fit Theory (match interface to user's mental model/expertise), Familiarity Principle (matching learned behavior increases comfort).

DO:
- Base adaptations on clear, **consistent** behavior patterns — never a single interaction.
- Be transparent about why content or layout is changing.
- Let users easily override or adjust adaptive features.
- Regularly review and update the rules driving adaptation.
- Keep adaptive changes **subtle** — never disorient the user.

DON'T:
- Make drastic layout changes that confuse or frustrate.
- Adapt on single interactions or unreliable data.
- Ignore privacy concerns when collecting adaptation data.
- Remove access to features or content through adaptation (adapt = reorder/emphasize, never delete).
- Assume all users benefit from the same adaptive rules.

### Personalized recommendations
Named principles: Curiosity Gap (tease to spark exploration), Social Proof ("Trending in your network"), Endowment Effect ("Handpicked for you").

DO:
- Base recommendations on a **combination** of behavior + stated preferences + current context.
- Explain why each item is recommended.
- Let users dismiss or refine recommendations easily.
- Continuously improve the algorithm from user interactions.
- Keep recommendations **diverse** to avoid echo chambers.

DON'T:
- Show too many recommendations at once.
- Rely solely on past behavior (limits discovery of new interests).
- Make recommendations that feel invasive or presumptuous (creepy > helpful line).
- Ignore the context in which a recommendation appears (e.g., don't recommend actions on other people's private changes).
- Omit an opt-out from personalization.

### User preferences and settings
Named principles: Locus of Control, Self-Determination Theory (autonomy), Cognitive Load Theory (hiding unneeded features reduces clutter).

DO:
- Organize settings logically with clear labels **and one-line descriptions** under each.
- Ship sensible defaults; customization is optional, never required.
- Provide live previews of setting changes when possible.
- Make settings discoverable without cluttering the main interface.
- Allow easy reset to defaults.

DON'T:
- Overwhelm with too many granular settings.
- Bury critical settings deep in menus.
- Drastically change core functionality via a setting without the user clearly understanding it.
- Forget to sync settings across devices.
- Ignore accessibility in the settings UI itself (text size, color scheme, contrast options are themselves settings users need).

### Localization and language selection
DO:
- Offer language selection prominently in settings or initial setup.
- Use standard language/region codes (en-US, fr-FR).
- Use a translation management system to keep all languages current.
- Localize design elements (icons, colors, metaphors), not just text.
- Detect browser language as a default, but let the user override.

DON'T:
- Rely solely on machine translation without human review.
- Forget to localize date formats, numbers, units, currency.
- Assume text length is the same across languages (plan for expansion).
- Ignore right-to-left (RTL) languages in layout.
- Limit language options by IP location — location ≠ language preference.

---

## Module 22: Patterns for onboarding and learning

Five patterns covered: product tours/walkthroughs, contextual tips and hints, interactive tutorials, onboarding checklists, help centers/documentation. Recurring meta-rule across all five: **tips/tours/tutorials are never a substitute for intuitive design** — if the UI needs heavy explanation, fix the UI.

### Product tours and walkthroughs
Named principles: Cognitive Load Reduction (one feature at a time), Curiosity (tease advanced features), Self-Efficacy (include a "quick win" early).

DO:
- Keep tours concise and focused on key features only.
- Allow skipping or exiting the tour **at any point**.
- Use visual cues (highlights, arrows) to point at specific elements.
- Explain *why* each feature is valuable, not just what it is.
- Offer replay / access to specific tour parts later.
- Show step progress (e.g., "1 of 13") with a Dismiss option on every step.

DON'T:
- Force completing the tour before the app is usable.
- Dump too much information at once.
- Use technical jargon in tour copy.
- Assume all users need the same level of guidance.
- Let tours go stale when the UI changes.

### Contextual tips and hints
Just-in-time guidance at the point of need. Named principles: Just-in-Time Learning, Progressive Disclosure (advanced tips only after basics mastered), Curiosity ("Did you know?" framing).

DO:
- Keep tips concise and directly relevant to the user's **current** context.
- Use clear, action-oriented language.
- Provide a way to dismiss/hide tips permanently.
- Make tips noticeable but not intrusive.
- **Test timing and frequency** — a mistimed tip is an annoyance.

DON'T:
- Show many tips at once.
- Use tips to patch unintuitive design.
- Re-show tips the user already dismissed.
- Interrupt active tasks with intrusive or poorly timed hints.
- Let tips go stale when features change.

### Interactive tutorials
"Learning by doing" — the user performs real actions, vs. a passive tour. Named principles: Learning by Doing, Immediate Feedback, Scaffolding (basic → advanced).

DO:
- Break tutorials into small, manageable steps.
- Give clear instructions and feedback at each stage.
- Allow pause, resume, restart anytime.
- Use real-world tasks, not abstract demos.
- Keep tutorials re-accessible later as refreshers.

DON'T:
- Make tutorials long or complex.
- Gate app usage behind tutorial completion.
- Substitute tutorials for intuitive design.
- Let tutorials drift out of date.
- Assume everyone needs the same guidance.
- Write verbose, flowery copy — the book's "Don't" example mocks a paragraph-long description of a button; instruction copy should be one or two plain sentences ("To create a new Cluster, select this button, then add a title and description").

### Onboarding checklists
Named principles: Goal-Gradient Effect (motivation rises near completion — show % complete), Endowed Progress Effect (pre-check items like "Create account" so users start with progress), Gamification (milestone messages).

DO:
- Keep items clear, concise, actionable ("Invite 2 collaborators", "Generate your first summary").
- Give immediate feedback on completion; show progress ("2/4 complete").
- Allow completing items in any order where possible.
- Allow skipping/dismissing the checklist.
- Keep it prominent but not intrusive.

DON'T:
- List too many items.
- Include complex/time-consuming tasks in initial onboarding.
- Force full completion before the app is usable.
- Omit guidance/help for each item.
- Keep showing the checklist long after the user is active.

### Help centers and documentation
Named principles: Self-Determination (competence), Recognition over Recall (browse categories beat remembering terms), Learning Styles (text + video + interactive).

DO:
- Organize content into clear categories/subcategories with article counts visible.
- Use plain language; avoid jargon.
- Provide robust search with common-topic shortcuts.
- Keep documentation current with the product.
- Embed **context-sensitive help links** inside the app ("Learn more" next to the setting it explains).

DON'T:
- Skip basic "Getting Started" content.
- Bury important info deep in a complex structure.
- Skip gathering feedback on article helpfulness.
- Rely on text alone — include visuals and video where they help.
- Assume users will find the help center on their own; promote it inside the app.

---

## Module 23: Patterns for information relationships

Five patterns: breadcrumbs/navigation trails, sitemaps, tagging and labeling, faceted search and filters, related content suggestions.

### Breadcrumbs and navigation trails
Named principles: Spatial Memory, Cognitive Load Reduction, Information Scent (cues to where you've been / can go).

DO:
- Keep breadcrumbs simple and concise.
- Use clear separators (">" or "/").
- Make **every level clickable** — except the current page.
- Place them consistently, typically at the top of the page.
- Treat breadcrumbs as a supplement to primary navigation, never a replacement.

DON'T:
- Make the current page a clickable link in the trail.
- Use breadcrumbs on single-level sites/apps (pointless).
- Duplicate what primary navigation already shows.
- Use breadcrumbs as the only navigation.
- Overload the trail with too many levels.

### Sitemaps
DO:
- Organize hierarchically and logically.
- Use clear, concise, user-facing labels (no internal naming conventions).
- Show visual cues for relationships between sections.
- Make the sitemap reachable from any page.
- Keep it current as the app evolves.
- **Generate an XML sitemap for public pages — it directly supports SEO / search-engine indexing.**

DON'T:
- Include every single page — main sections and important pages only.
- Use technical jargon or internal names as labels.
- Skip search for large sitemaps.
- Build deeply nested, over-complex sitemaps.
- Forget to make the sitemap responsive.

### Tagging and labeling
Flexible non-hierarchical categorization. Named principles: Associative Memory, Recognition over Recall (tag clouds), Personalization (user-created tags).

DO:
- Use clear, concise, meaningful tags.
- Autocomplete/suggest tags while the user types.
- Support both system-generated and user-generated tags.
- Provide tag management: merge, split, rename.
- Apply tags consistently across all features and sections.
- Color-code labels to distinguish content types at a glance (e.g., blue = articles, green = videos).

DON'T:
- Overload content with too many tags.
- Use broad/vague tags that add no value.
- Skip guidelines/examples for effective tagging.
- Rely on tags alone for organization — combine with hierarchy/search.
- Ignore synonyms and variants in tag search.

### Faceted search and filters
Four sub-systems, each with its own guidelines:

Global search:
- Place the search bar prominently in top navigation, always visible and distinguishable.
- Make clear what content types global search covers.

Contextual search:
- Clearly indicate when a search is scoped to a section/content type.
- Provide one-click expansion from contextual to global search.
- Use consistent visual language to distinguish the two.

Faceted filters:
- Choose facets that are actually valuable to users.
- Make filters easy to add, remove, adjust.
- **Show the result count for each facet value.**
- Provide a one-click "reset all filters."
- Show total results and pagination state ("Showing 10 of 68 results").

Keyboard shortcuts:
- Use intuitive shortcuts (Ctrl+F in-page, ⌘K global search).
- Publish a shortcut cheat sheet / quick reference.
- Allow shortcut customization.
- Make shortcuts discoverable via UI cues (show "⌘K" inside the search box) or onboarding.

Overall DO: prominent global search; clear visual cues for context; consistent shortcuts app-wide; autocomplete and suggestions; let users save/reuse complex queries.
Overall DON'T: cram too many search options into one view; leave the current search context ambiguous; use hard-to-remember shortcuts; **forget to optimize search performance on large datasets**; tolerate irrelevant results — relevance is the product.

### Related content suggestions
Named principles: Curiosity Gap, Cognitive Momentum (keep exploration going with relevant next steps), Implicit Learning.

DO:
- Combine multiple signals (content similarity, user behavior, popularity).
- Explain why each item is suggested.
- Make navigation between related items effortless.
- Refine the algorithm from interaction data.
- Keep suggestions diverse (anti-echo-chamber).

DON'T:
- Show too many suggestions at once.
- Suggest content nearly identical to what's on screen.
- Ignore placement context.
- Let suggestions visually compete with the main content — related content is secondary, keep it at the bottom/side and visually quieter.
- Omit refine/opt-out controls.

---

## Module 24: Patterns for wayfinding and navigation

### The three navigation groups (classify before designing)
1. **Product/Entity navigation** — primary system for mainline features and product entry points (e.g., Dashboard, Projects, Library, Analytics in the main nav bar).
2. **Contextual navigation** — changes with the user's current task/location: shortcuts, recently visited, related/sub-pages, bookmarks/saved items (e.g., a project sidebar showing recent edits).
3. **System navigation** — account, billing, permissions, settings; typically behind the profile/avatar menu.

Rule: assign every nav item to one of these groups first; don't mix system items into product navigation.

### Priority and progressive disclosure (navigation)
Show the most important/frequent items up front; keep the rest accessible but initially hidden. Named principles: **Hick's Law** (fewer initial choices = faster decisions), Progressive Disclosure, Recognition over Recall.

DO:
- Prioritize nav items by frequency of use and importance (data, not opinion).
- Use clear visual hierarchy to separate primary from secondary navigation.
- Give clear cues for reaching hidden options ("More…", expandable sections).
- Ensure ALL options remain discoverable even when not visible.
- Test the prioritization with real users.
- Collapse into fewer grouped items rather than listing everything: the book's "Do" sidebar shows 5 items (Search, Activity, Bookmarks, Clusters, Help & support, Account & settings — grouped); the "Don't" shows 9+ ungrouped items.

DON'T:
- Hide critical or frequently used features deep in the structure.
- Use ambiguous labels/icons, especially for hidden options.
- Overload primary navigation with too many items.
- Lose access to any option on small screens.
- Design only for new users or only for power users.

### Off-canvas navigation (drawer/hamburger)
Best when screen real estate is scarce (mobile). Named principles: Out of Sight Out of Mind (hiding nav reduces distraction during focused tasks), Progressive Disclosure, Spatial Memory (always slide from the same side).

DO:
- Use a clear, recognizable icon or gesture to open it.
- Keep open/close transitions smooth and quick.
- Order contents logically, most important items first.
- Allow easy dismissal (tap outside or close button).
- Hint that more content exists off-screen.
- On desktop, show a visible sidebar; transform it into off-canvas only on small screens (responsive strategy).

DON'T:
- Hide critical, frequently used actions inside the drawer.
- Make the drawer so wide it obscures the content.
- Nest off-canvas menus inside each other.
- Skip keyboard access (accessibility).
- Make off-canvas the ONLY navigation.

### Sticky vs. fixed navigation
Definitions: **sticky** stays until a scroll point then can move off; **fixed** never moves. Named principles: Perceived Stability, Immediacy, Spatial Constancy (muscle memory for fixed elements).

DO:
- Choose sticky vs. fixed based on the content's actual needs, not habit.
- Keep persistent elements small — they must not eat screen space, especially on mobile.
- Visually distinguish persistent chrome from scrollable content.
- Consider shrinking or fading the sticky element on scroll to reduce content obstruction.
- **Test the performance impact of sticky/fixed elements, especially on low-end devices** (position:fixed/sticky can trigger repaints and jank).

DON'T:
- Make everything sticky — pin only the most important navigation.
- Let persistent elements cover content or interactive elements.
- Omit a way to hide persistent nav if it gets in the way.
- Apply sticky behavior inconsistently across similar pages.
- Ignore how fixed elements collide with form inputs and the mobile keyboard.

### Bottom navigation (mobile)
Named principles: **Fitts's Law** (bottom placement minimizes thumb travel), Recognition over Recall (universal icons: house = home, bell = notifications), Chunking (3-5 sections = memorable app structure).

DO:
- **Limit to 3-5 items.**
- Pair recognizable icons with short text labels.
- Clearly indicate the active state.
- Consider a larger central button for the single primary action.
- Keep the bar identical across all screens.

DON'T:
- Overflow it — push extras into a "More" menu.
- Hide the bar on scroll; it must stay accessible.
- Use bottom navigation on desktop (not a desktop pattern).
- Skimp on touch target sizes per item.
- Ignore collisions with FABs and the keyboard.

---

## Module 25: How to grow from here (the ceiling of design patterns)

(Career/motivational content skipped; the decision framework is kept.)

- **Two forces, both needed**: standardization (design systems, UI kits, established patterns, accessibility principles) raises the *floor* of design quality and lets non-experts ship usable products; innovation raises the *ceiling*. Neither replaces the other.
- **Pattern lifecycle**: every standard pattern (hamburger menu, pull-to-refresh) began as someone's experiment; patterns are tools, not rigid rules.
- **Decision criterion — when to use patterns vs. invent**: when time is short and risk is low, use existing patterns — they are battle-tested, familiar to users, and fast to implement. Only innovate when (a) you've identified a meaningful UX improvement AND (b) you have the clarity and resources to explore it properly. Default = pattern.
- Convergent-looking interfaces are not a failure state; familiarity is a usability feature.
- Craft serves the business: most celebrated craft-first companies could only afford that focus after becoming profitable. Ship first, polish within means.

---

## Top rules from this unit

1. **Default to established patterns; innovate only with a clear UX win and the resources to validate it.** Battle-tested + familiar + fast beats novel in almost every low-risk situation.
2. **Bottom navigation: 3-5 items max**, icons + short labels, clear active state, never hidden on scroll, never on desktop.
3. **Prioritize navigation by frequency of use (Hick's Law)**: few grouped items up front, everything else behind a clearly cued "More" — but every option must stay discoverable, including on small screens.
4. Classify every nav item as **product, contextual, or system navigation** before placing it; don't mix system items (settings/billing) into primary nav.
5. **Never hide critical or frequent actions** — not in drawers, not in adaptive re-layouts, not behind customization, not deep in settings.
6. **Persistent (sticky/fixed) chrome must be minimal**: pin only what matters, keep it small, shrink it on scroll, and test its rendering performance on low-end devices.
7. **Breadcrumbs**: every level clickable except the current page; supplement primary nav, never replace it; skip them entirely on shallow sites.
8. **Faceted search**: show result counts per facet value, one-click reset-all, visible total-results state, and optimize search performance for large datasets.
9. Put global search prominently in the top nav with a visible keyboard shortcut (⌘K) and autocomplete; scoped search must state its scope and offer one-click expansion to global.
10. **Tours, tips, and tutorials are never a substitute for intuitive design** — if you're explaining basic UI in a tooltip, redesign the UI.
11. Onboarding must always be skippable/dismissible; never gate app usage behind a tour, tutorial, or checklist.
12. Onboarding checklists: small actionable items, visible progress (2/4), pre-check completed steps (endowed progress), and stop showing it once the user is active.
13. Contextual tips: one at a time, at the moment of need, action-oriented copy, dismiss-and-stay-dismissed, tested timing.
14. **Adaptive/personalized behavior must be subtle, explained, override-able, based on consistent (not single) signals, and never remove access to anything.**
15. Recommendations: blend behavior + stated preference + context, explain the "why," keep them diverse, keep them visually secondary to main content, and provide opt-out.
16. Settings: sensible defaults, logical grouping with one-line descriptions, live preview, easy reset, synced across devices.
17. Localization: standard locale codes; localize dates/numbers/units/currency and visuals, not just strings; plan for text expansion and RTL; never lock language to IP location.
18. Provide an XML sitemap for public pages (SEO) and a user-facing sitemap of main sections only — clear labels, no internal jargon.
19. Tags: concise and meaningful, autocompleted, consistently applied, with merge/rename management; combine with hierarchy — tags alone don't organize.
20. Performance is part of the pattern: customized dashboards must load fast, search must stay fast at scale, sticky elements must not jank — test on low-end hardware.
