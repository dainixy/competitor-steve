# Tommy Geoco — Making UX Decisions · Patterns Unit 3: Cognitive Load

Source: 6 PDFs from `03-Patterns/03-Cognitive load`. Theme: cognitive load = mental effort required to process information and complete a task. Every pattern below exists to lower it. The unit's five load-reduction patterns: pagination/infinite scroll, steppers/wizards, minimalist navigation, chunked lists, simplified forms.

Named principles used throughout this unit (one-liners):
- **Chunking** — the brain processes and remembers information better when it's grouped into small, meaningful units.
- **Miller's Law** — working memory holds ~7 (±2) items; design groups within that limit.
- **Hick's Law** — decision time grows with the number and complexity of choices; fewer options = faster decisions.
- **Progressive Disclosure** — reveal information/options gradually instead of all at once.
- **Goal-Gradient Effect** — motivation increases as people feel closer to a goal; visible progress drives completion.
- **Gestalt Proximity** — items placed close together are perceived as related.
- **Signal-to-Noise Ratio** — emphasize what matters (signal), strip what doesn't (noise).
- **Cognitive Load Theory** — fewer things to process at once = lower mental effort, fewer errors.

---

## 1. Pagination and infinite scroll

Two strategies for large content sets. Pagination divides content into discrete pages; infinite scroll loads more as the user scrolls. Both present manageable amounts at a time — and both improve performance by loading only a subset of content per request (faster page load, less server load). This is a direct Core Web Vitals win: never render a full large dataset up front.

**Decision criteria — which one to use:**
- Use **pagination** for goal-oriented tasks: search results, data tables, historical/analytics reports — anywhere users need to locate a specific item, know where they are, or reach the end.
- Use **infinite scroll** only for exploratory, leisurely browsing: discovery feeds, activity streams — where there is no "destination."
- Never use infinite scroll when users need to reach a specific item or the end of a list.
- Never use pagination for content meant to be consumed in its entirety (e.g., a single article) — don't split articles across pages.

**DO:**
- Clearly indicate current position and total content amount ("Showing 10 of 68 results").
- Provide next / previous / first / last page navigation.
- Show clear visual cues for infinite scroll (loading indicators) so users know more is coming.
- Tune items-per-page / items-per-load to the content type and user need — for text lists, groups of ~10–20 items are easy to process and remember.
- Maintain the user's position when they navigate back to the list (both patterns). Losing scroll/page position on "back" is a classic failure.
- Offer a "View All" option for paginated lists when appropriate.
- Provide context about what each page or load contains.

**DON'T:**
- Implement infinite scroll without a way to return to a specific point.
- Forget back-navigation position restore.
- Leave the user with no sense of progress or extent.

---

## 2. Steppers and wizards

Break a complex process or long form into a sequence of small steps; the user focuses on one step at a time. Benefits: simpler mental model, fewer errors (nothing overlooked), higher completion rates (visible progress motivates via the Goal-Gradient Effect).

**Use when:** multi-part setup flows (project creation, onboarding, configuration), publishing workflows with required sub-tasks (tags, permissions, scheduling).

**DO:**
- Clearly label each step with a brief description of what's required.
- Show current position and how many steps remain (progress bar or completed-step markers).
- Allow reviewing and editing previous steps.
- Provide clear Next and Back navigation.
- Use progressive disclosure inside steps: basic settings first, advanced options only if the user opens them.
- For longer processes, provide a way to save progress and return later.

**DON'T:**
- Include too many steps — the process itself starts to feel overwhelming.
- Force strict step order when it isn't necessary.
- Hide important information behind optional steps.
- Use ambiguous or technical language in step labels/descriptions.

**Anti-pattern shown in the course:** one giant modal with 10+ stacked fields vs. the same task as a 3-step stepper ("Naming → Invite → Review") with 2 fields per step. Prefer the latter.

---

## 3. Minimalist navigation

Present only the most essential navigation options. Fewer choices = less decision fatigue (Hick's Law), more attention on the actual task, faster learning for new users, and better mobile usability where space is scarce.

**Concrete shapes:**
- Main app nav: a handful of essential sections only (e.g., Dashboard / Projects / Team / Settings).
- Focused work surfaces (editors): strip navigation to near zero so the content is the interface.
- Mobile: bottom bar with only the most crucial options; everything else behind a menu.
- Onboarding: start users with a simplified nav and reveal advanced options as they gain familiarity.

**DO:**
- Prioritize the most important and most frequently used items; rank ruthlessly.
- Use clear, concise text labels for navigation options.
- Icons may accompany or replace text (especially mobile) — but never ambiguous icons without labels.
- Keep every key area reachable, even if only through secondary navigation.
- Provide easy access to a fuller/comprehensive menu when needed.

**DON'T:**
- Oversimplify to the point of hiding necessary functions.
- Bury less-frequent-but-important areas with no path to them.
- Apply one minimalist nav uniformly to all user types when advanced users need quick access to more.
- Skip user-testing the reduced navigation — verify it actually meets user needs.

---

## 4. Chunked lists

Break long lists into smaller labeled groups. Improves comprehension (structure and relationships become visible), scanability (find things faster), memory (Miller's Law), and prevents overwhelm.

**Numbers and rules:**
- Keep chunk sizes at **5–9 items per chunk** (Miller's Law: 7±2).
- Cap top-level navigation/menu groupings at **5–9 main categories**.
- Group by logical categories or relationships that match user expectations — never arbitrary groupings.
- Use clear headings or visual separators between chunks; proximity alone (Gestalt) signals relatedness, so add whitespace between groups and tighten it within groups.
- Group related controls together in toolbars (e.g., text styling in one cluster, alignment in another).

**DON'T:**
- Create oversized chunks — defeats the purpose.
- Chunk short lists that don't need it (over-structuring is its own noise).
- Remove the "view all items at once" option if users need it.
- Ignore how chunking reflows across screen sizes.

**Optional:** allow users to customize the grouping when the content genuinely supports multiple valid organizations.

---

## 5. Simplified forms

Minimize the information and decisions demanded from the user: collect only essential fields, use smart defaults, break long forms into steps. Payoffs: higher completion rates, fewer errors, faster entry, forms that respect users' time.

**DO:**
- Collect only essential information now; let users add details later (e.g., registration = minimal fields, profile completion deferred).
- Use clear, concise, non-technical labels.
- Implement smart defaults, pre-filled suggestions, and auto-fill wherever possible.
- Replace long dropdowns with a smart search/autocomplete when option lists are large (Hick's Law).
- Replace complex configuration with clearly labeled toggle switches where a setting is binary.
- Use progressive disclosure for conditional/advanced fields: reveal them only when relevant or when the user opts in (e.g., SEO settings hidden behind "Advanced").
- Break long forms into steps or sections (see steppers).
- Align fields and labels for easy vertical scanning.
- Provide clear error messages with guidance for correction.
- Optimize forms for mobile.

**DON'T:**
- Ask for anything not necessary or immediately useful.
- Pile on optional fields — progressive disclosure beats a wall of "(optional)".
- Use jargon in labels or instructions.

---

## Top rules from this unit

1. Load content in subsets, never all at once — pagination/lazy loading is both a cognitive-load AND a page-performance (Core Web Vitals) win.
2. Choose pagination for goal-oriented tasks (search, tables, reports); reserve infinite scroll for pure exploratory feeds — never where users need to find a specific item or reach the end.
3. Always show position and extent in paginated content: "Showing 10 of 68", current page, first/prev/next/last controls.
4. Preserve the user's list position when they navigate back — for both pagination and infinite scroll.
5. Break complex processes into steppers with labeled steps, visible progress, and Back/edit access to earlier steps — but keep step count low; too many steps is its own overload.
6. Never force strict step order when the task doesn't require it, and never hide required information behind optional steps.
7. Show visible progress (progress bar, completed-step markers, numbered pages) — the Goal-Gradient Effect measurably raises completion.
8. Ruthlessly limit primary navigation to the most important, most-used items (Hick's Law); park everything else in secondary navigation that remains reachable.
9. Never use icon-only navigation with ambiguous icons — label them.
10. Chunk long lists into labeled groups of 5–9 items; cap main nav at 5–9 categories (Miller's Law).
11. Group by logical, user-expected categories with clear headings/separators; use proximity (tight within groups, whitespace between) to signal relationships.
12. Don't chunk short lists — unnecessary structure is noise; and keep a "view all" escape hatch where users need it.
13. In forms, ask only for what is essential right now; defer everything else to later.
14. Use smart defaults, autofill, and autocomplete-instead-of-long-dropdowns to cut decisions per field.
15. Reveal advanced/conditional form fields via progressive disclosure, not a wall of optional fields.
16. Write all labels, steps, and instructions in plain language — no technical jargon anywhere users read.
17. Align form fields and labels for single-column vertical scanning; give clear, corrective error messages.
18. Maximize signal-to-noise: on focused work surfaces (editors, checkout, content), strip navigation and chrome so the task itself dominates.
19. Introduce complexity gradually to new users (simplified nav/options first, more revealed with familiarity).
20. Verify simplification with real users — minimalist structures can hide necessary functions; test that key areas are still findable.
