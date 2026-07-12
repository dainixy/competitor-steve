# Tommy Geoco — Making UX Decisions · Patterns Unit 1: Chunking

Source: 03-Patterns/01-Chunking (6 PDFs). Distilled for use when designing/building web UI.

## Chunking (core principle)

Chunking = break large amounts of information into smaller, discrete units so users can process, scan, and remember them. It is the single biggest lever for reducing cognitive load in dense interfaces (dashboards, libraries, forms, search results).

The unit covers 5 concrete patterns that implement chunking. Decision guide for which to reach for:

| Situation | Pattern |
|---|---|
| Collection of similar items (articles, products, projects) | Card-based layout |
| Related content categories that don't need to be seen at once | Tabs (switching/comparison) or accordions (vertical stacking, space-saving) |
| Long or complex form | Grouped form fields |
| Large dataset / long list (search results, listings) | Pagination |
| Multiple visual items in limited space, promotional/featured content | Carousel/slider — use sparingly, last resort |

## Card-based layouts

What it is: content in discrete rectangular containers; best for collections of similar items.

Why it works: chunking (each card = one mental unit), recognition over recall (icons/images let users recognize instead of remember), Gestalt proximity (metadata grouped inside a card reads as belonging to that content).

**Do:**
- Use consistent card sizes and layouts across the collection — inconsistent styling confuses users.
- Give every card a clear, descriptive title.
- Build visual hierarchy inside the card: most important info most prominent.
- Use white space inside cards; don't let them feel cluttered.
- Make each card a single clear interaction target (whole card clickable/tappable) — improves touch UX.
- Indicate interactivity with hover states (subtle, not decorative animation).
- Group related metadata (date, tags, collaborators) inside the card, near the content it describes.
- Let cards reflow responsively: multi-column grid on desktop → single column on mobile.

**Don't:**
- Overload a card with too much information or too many functions/actions.
- Use cards for single, linear processes — a step flow or form fits better.
- Skip the call-to-action: each card needs an obvious next step.
- Forget accessibility: proper contrast and keyboard navigation on cards.

## Tabs and accordions

What they are: tabs = horizontal row of headers, one panel visible at a time (good for comparison/switching). Accordions = vertically stacked expandable headers (good for saving vertical space, showing an outline of all sections even when collapsed).

Why they work: chunking, progressive disclosure (reveal detail only when asked — hide advanced options by default), recognition over recall (visible headers are a table of contents).

**Do:**
- Use clear, concise labels for headers.
- Always indicate the active tab / expanded section visually.
- Optionally pair icons with header text to aid recognition.
- Keep each panel's content cohesive and matching its header — no surprises behind a label.
- Transition smoothly between states (cheap CSS transitions, not heavy animation).
- Use accordions for detail/metadata and advanced settings collapsed by default.
- Use tabs when users switch between categories to compare (e.g., metric views).

**Don't:**
- Hide content users need to see simultaneously behind tabs/accordions — if they must compare it side by side, show it side by side.
- Hide critical information or primary actions behind a tab or collapsed accordion. Critical content is always visible.
- Nest accordions more than one level deep.
- Use tabs/accordions for sequential tasks or content meant to be consumed in a fixed order — use a stepper/flow instead.
- Cram in too many sections (a tab bar that wraps or scrolls is a smell — restructure).

## Grouped form fields

What it is: related inputs clustered under a common subheading or inside a visual container. The main tool for making long forms manageable.

Why it works: chunking, Gestalt proximity (visually grouped fields read as logically related), progressive disclosure (advanced groups collapsible/hidden by default).

**Do:**
- Give each group a clear, descriptive label — never ambiguous or overly broad.
- Visually distinguish groups with spacing, borders, or background — spacing alone is often enough and cheapest.
- Order groups in a natural progression (identity → details → settings; content fields before publishing settings).
- Keep fields that are commonly used together in the same group.
- Collapse less-frequently-used / advanced option groups by default.
- On mobile, consider one group per screen with clear navigation between groups.
- Style field groups consistently across the whole product.

**Don't:**
- Create too many groups — over-segmentation is its own overload.
- Group a very short form at all (roughly ≤5 fields: grouping adds complexity, not clarity).
- Separate fields users fill in together.
- Leave group-to-group navigation unclear, especially on mobile.

## Pagination

What it is: dividing a large set of items into pages. For search results, listings, tables, historical data.

Why it works: chunking, sense of progress (numbered pages = Goal-Gradient Effect), avoids choice overload by capping visible options.

**Performance note (important for our fast-loading goal):** pagination directly improves load time and server load by fetching only a subset — e.g., 20 items at a time instead of the whole library. Prefer it over rendering everything for any long list.

**Do:**
- Show current page and total ("Showing 10 of 68 results · pages 1 2 3 … 6").
- Provide next/previous AND jump-to first/last/numbered pages — never only next/prev on large datasets.
- Preserve the user's position when they navigate back to a paginated list.
- Offer a "View all" option where the set is small enough to be reasonable.
- Tune items-per-page to the content type; 10–20 items per page is the cited working range for lists.
- Keep pagination controls identical everywhere in the product.
- Make paginated pages linkable/bookmarkable (state in URL) so users can share a specific page.

**Don't:**
- Paginate content meant to be read in its entirety (articles) — that's hostile chunking.
- Show raw overwhelming totals without orientation (bad: "128814 items · Page 7 of 2610"; good: bounded, readable result count with a short page list).
- Use pagination where infinite scroll genuinely fits better (continuous feeds) — but default to pagination for anything findable/shareable/SEO-relevant.
- Omit context about what each page contains.

## Carousels and sliders

What they are: horizontal scrolling collections. Carousels auto-rotate (promo use); sliders are user-controlled. Treat this as the most abuse-prone pattern in the unit — use only for genuinely optional, visual, browsable content (media thumbnails, template galleries, featured items).

Why they can work: curiosity (peek of next item encourages exploration), recency effect, limits choice overload.

**Do:**
- Provide clear manual navigation controls (arrows) — never rely on auto-advance alone.
- Show a position indicator (dots or progress bar).
- Peek the next item (partially visible) so users know there's more.
- Make every item keyboard-accessible.
- Make it touch-friendly (swipe) on mobile before shipping it there.
- If auto-advancing at all: timing must be long enough to comprehend the content; never auto-advance content that takes time to read.

**Don't:**
- Put critical content or navigation in a carousel — assume users will NOT interact with items beyond the first.
- Overload with too many items.
- Auto-advance text-heavy content.
- Ship a carousel on mobile without touch support.

Practical bias for our stack: auto-rotating carousels also cost JS weight and layout shifts (CLS). Prefer a static grid or a manual, CSS-scroll-snap slider; reach for a carousel only when space is truly constrained and the content is optional.

## Top rules from this unit

1. Break every dense screen into discrete chunks — cards, groups, tabs, pages — before reaching for any other fix; chunking is the primary cognitive-load lever.
2. Never hide critical information or primary actions behind tabs, collapsed accordions, or carousel slides — critical content stays visible.
3. If users need to compare two things, show them simultaneously; tabs/accordions are only for content that doesn't need to be seen at once.
4. Use cards for collections of similar items; keep card size/style consistent, one clear title, one clear CTA, visual hierarchy inside, whole card as the click target.
5. Don't overload any container — cards with too many actions, tab bars with too many sections, carousels with too many items all defeat the pattern.
6. Prefer recognition over recall: visible labels, icons, and headers so users recognize where things are instead of remembering.
7. Use progressive disclosure: advanced/rare options grouped and collapsed by default, revealed on demand.
8. Group related form fields under clear, specific labels in natural order; keep commonly-co-filled fields together; skip grouping on short forms (≈≤5 fields).
9. Distinguish form groups with spacing/borders/background and keep group styling consistent product-wide.
10. Paginate long lists at 10–20 items per page — it chunks cognition AND cuts load time/server work (fetch only what's shown).
11. Pagination controls: show current page + total, give first/last/numbered jumps (not just next/prev), preserve scroll/position on back-navigation, put page state in the URL.
12. Never paginate continuous reading content (articles); never use tabs/accordions/pagination for strictly sequential tasks — use a linear flow.
13. Nest accordions at most one level deep.
14. Always mark the active state: current tab, expanded section, current page, carousel position.
15. Avoid carousels for anything important; assume only the first slide is seen. If used: manual controls, position dots, keyboard access, touch support, no fast auto-advance.
16. Prefer static grids or CSS scroll-snap sliders over JS auto-rotating carousels — lighter, no layout shift, no timing hazards.
17. Every chunking container needs accessibility basics: sufficient contrast, keyboard navigation, clear focus/active states.
18. Use white space as the default grouping tool — proximity groups content before borders and backgrounds are needed.
