# Patterns: Information Relationships
Source: Tommy Geoco — Making UX Decisions, 03-Patterns / 11-Information relationships (6 lessons).
Scope: how pieces of content relate and how users navigate those relationships. Five patterns: breadcrumbs, sitemaps, tagging/labeling, faceted search + filters, related content suggestions.

## 00 — Information relationships (overview)

- Information relationships = how content/data pieces are connected and organized in a system. Get them right so users understand app structure, navigate complex data, and find things fast.
- These five patterns are complementary, not alternatives: breadcrumbs (where am I), sitemaps (whole-structure overview), tags (flexible cross-links), faceted search (narrowing), related content (discovery). Pick per job; layer them on complex sites.

## 01 — Breadcrumbs and navigation trails

What they do: show current location in the hierarchy + give a clickable path back up. Support spatial memory, reduce cognitive load, and provide "information scent" (cues about where you've been and can go).

### Rules
- Use breadcrumbs only on multi-level hierarchies. Never on single-level sites/apps — they add noise with zero value.
- Breadcrumbs are supplementary navigation, never the only or primary navigation.
- Make every level clickable EXCEPT the current page — show the current page as plain text, not a link.
- Keep trails simple and concise; don't overload with too many levels or extra information.
- Use a clear, consistent separator between levels (`>` or `/`).
- Place breadcrumbs in a consistent location on every page, typically at the top of the content area.
- Don't repeat information already visible in the primary navigation.
- Pattern format: `Home > Section > Subsection > Item` — user can jump to any ancestor in one click instead of using the browser back button.
- In filtered/search views, breadcrumbs can show the applied filters/categories so users understand how they arrived at the current result set.

### Do / Don't
| Do | Don't |
|---|---|
| Keep breadcrumbs simple and concise | Make the current page a clickable link |
| Use clear separators (`>` or `/`) | Use breadcrumbs on single-level sites |
| Make each ancestor level clickable | Duplicate the primary nav |
| Place consistently, top of page | Rely on breadcrumbs as the only navigation |
| Treat as supplementary aid | Overload with too much info / too many levels |

## 02 — Sitemaps

What they do: visual or textual overview of the entire structure and content hierarchy. Two distinct jobs: (a) user-facing sitemap page for orientation/navigation, (b) XML sitemap for search engines.

### Rules
- Generate an XML sitemap for all public-facing pages — it helps search engines understand and index the structure (direct SEO win; cheap, do it always).
- In a user-facing sitemap, do NOT list every page — include main sections and important pages only.
- Organize the sitemap in a logical hierarchical structure; avoid deep nesting that confuses more than it explains.
- Write labels in the user's language — clear, concise; never technical jargon or internal naming conventions.
- Provide visual cues (indentation, tree lines, grouping) that show relationships between elements.
- Make the sitemap reachable from any page (typically footer link).
- Add a search function to large sitemaps.
- Make the sitemap responsive — it must work on small screens.
- Keep it up to date as the application evolves; a stale sitemap is worse than none.
- Mirror the actual layout/organization of the application in the sitemap's visual arrangement — consistency leverages users' spatial memory.
- A visual, tree-like sitemap communicates complex hierarchy better than text navigation alone; useful in onboarding and help centers.

### Do / Don't
| Do | Don't |
|---|---|
| Logical hierarchical structure | List every single page |
| Clear, concise labels | Internal jargon in labels |
| Visual relationship cues | Overly deep/complex nesting |
| Accessible from any page | Skip search on large sitemaps |
| Keep updated | Ignore small screens |

## 03 — Tagging and labeling

What they do: keyword categorization that is flexible and non-hierarchical — cuts across the folder tree, improves search, and reveals connections between otherwise unrelated content. Supports recognition over recall (users see and click a tag instead of recalling a search term).

### Rules
- Use few, meaningful tags per item. Don't overload content with many tags — each tag must add findability value.
- Reject overly broad or vague tags ("misc", "general", "stuff") — they carry no signal.
- Provide autocomplete suggestions while the user types a tag — this prevents duplicates and near-synonyms.
- Support both system-defined tags (consistency) and user-created tags (personalization) when users organize their own content.
- Build tag management tooling: merge, split, rename. Tag vocabularies rot without it.
- Handle synonyms and variations in search ("ML" should find "Machine Learning") — don't make exact tag text the only match path.
- Use tags consistently across all features/sections — the same tag must mean and do the same thing everywhere.
- Never rely on tags as the only organization method — combine with hierarchy (folders/sections) and search.
- Provide guidelines or examples for effective tagging where users create tags.
- Use shared tags to power "related content" links between items.
- A tag cloud / frequent-tags list gives users one-click access to common topics (recognition over recall).

### Do / Don't
| Do | Don't |
|---|---|
| Clear, concise, meaningful tags | Too many tags per item |
| Autocomplete on tag entry | Broad/vague tags with no value |
| System + user tags | No tagging guidelines |
| Merge/split/rename tooling | Tags as the sole organization scheme |
| Consistent use app-wide | Ignoring synonyms in search |

## 04 — Faceted search and filters

Covers four search modes that combine: global search (whole app), contextual search (within current section), faceted filters (structured narrowing), keyboard shortcuts. Progressive disclosure principle: filters reveal complexity gradually instead of all at once. Flexibility–usability tradeoff: simple search bar for novices, advanced syntax + shortcuts for power users.

### Global search rules
- Place the global search bar prominently in the top navigation; always accessible, visually distinct.
- Make clear what content types global search covers.
- Provide autocomplete/suggestions as the user types (recognition over recall, faster queries).

### Contextual search rules
- Clearly indicate when a search is scoped to a specific area or content type.
- Always offer a one-step way to expand a contextual search to global.
- Use consistent visual language to distinguish contextual from global search.

### Faceted filter rules
- Choose facets by user value, not by what fields exist in the database. Only relevant, useful facets.
- Show the result count next to each facet value (e.g., "Cardiology (12)") — users shouldn't click into empty sets.
- Let users add, remove, and adjust filters easily; applied filters must be visible and individually removable.
- Provide a one-click "reset all filters."
- Don't overwhelm the interface with every search option at once — progressive disclosure.
- Give clear feedback about the current search context (what's searched, what filters are active).
- Optimize search performance for large datasets — slow filtering kills the pattern. (Performance is a feature; a facet UI that takes seconds per click is worse than none.)
- Result relevance/accuracy matters more than search feature count.
- Let users save and reuse complex search queries.

### Keyboard shortcut rules
- Use intuitive, conventional shortcuts (e.g., a global shortcut like `Ctrl+/` or `Ctrl+K` to focus search; `Ctrl+F` semantics for in-page search).
- Keep shortcuts consistent across the whole application.
- Make shortcuts discoverable: UI hints (kbd badges in the search field), cheat sheet, or onboarding mention.
- Avoid ambiguous or hard-to-remember combos.
- Allow customization for power users (only if the product genuinely serves power users — otherwise skip).

### Do / Don't
| Do | Don't |
|---|---|
| Prominent, always-available global search | All search options dumped on screen at once |
| Clear visual cues for scoped search | Ambiguous search context |
| Consistent shortcuts app-wide | Obscure shortcut combos |
| Autocomplete + suggestions | Unoptimized search on large datasets |
| Saved/reusable queries | Irrelevant or inaccurate results |

## 05 — Related content suggestions

What they do: recommend content relevant to what the user is viewing — discovery, deeper research, and an interconnected content structure. Psychology: curiosity gap (teaser titles invite exploration), cognitive momentum (an engaged user keeps going if given relevant next steps), implicit learning.

### Rules
- Show few suggestions at a time — a short, curated set beats a wall of recommendations.
- Keep suggestions subordinate to the main content: place them after/beside it (e.g., end of article), never so prominent they distract from the primary task.
- Suggest content that is related but not near-duplicate — items too similar to the current one add nothing.
- Ensure diversity in suggestions to avoid echo chambers (different angles/subtopics, not five versions of the same piece).
- Match suggestions to context — what's appropriate at the end of an article differs from what belongs in an editor sidebar.
- Base relevance on multiple signals (content similarity, user behavior, popularity), not one.
- Briefly explain why an item is suggested ("Because it shares the tag X") — builds trust.
- Make navigation between related items effortless (one click, no dead ends).
- Let users refine or opt out of suggestions.
- Refine the recommendation logic over time based on real interaction data; static "related" lists go stale.
- Shared tags are the cheapest solid relevance signal — start there before building anything algorithmic.

### Do / Don't
| Do | Don't |
|---|---|
| Multi-factor relevance | Too many suggestions at once |
| Explain why suggested | Near-duplicate suggestions |
| Easy navigation between items | Ignoring the viewing context |
| Diverse suggestions | Suggestions louder than the main content |
| Iterate on the algorithm | No refine/opt-out option |

## Top rules from this unit

1. Breadcrumbs: current page = plain text, every ancestor = clickable link, `>` or `/` separator, consistent position at top of page.
2. Use breadcrumbs only where a real hierarchy exists (2+ levels); they supplement primary navigation, never replace it.
3. Don't duplicate primary navigation inside breadcrumbs, and don't stretch trails across too many levels.
4. Always ship an XML sitemap for public pages — direct, cheap SEO win for crawlability and indexing.
5. A user-facing sitemap lists main sections and key pages only — never every page, never deep nesting, never internal jargon.
6. Make the sitemap reachable from every page (footer), responsive, and keep it current as the site changes.
7. Tags: few and meaningful per item; kill vague catch-alls ("misc", "general") — every tag must earn its findability value.
8. Add autocomplete to tag entry to prevent duplicate/synonym sprawl; handle synonyms in search matching too.
9. Tags complement hierarchy — never make them the sole organization method; plan merge/rename/split tooling from day one.
10. Put global search in the top nav, always visible, with autocomplete suggestions; give it a discoverable keyboard shortcut (`Ctrl+K`-style) shown as a hint in the UI.
11. Show result counts on every facet value and make applied filters visible, individually removable, and resettable in one click.
12. Choose facets by user value, not by available database fields; reveal filter complexity progressively rather than all at once.
13. When search is scoped to a section, say so visibly and offer one-step expansion to global search.
14. Optimize search/filter performance for large datasets — a slow facet UI is worse than none (speed is part of the pattern).
15. Related content: a few diverse, non-duplicate suggestions placed after the main content — never louder than the primary task.
16. Explain why something is recommended and make the next click frictionless; let users refine or dismiss suggestions.
17. Start related-content relevance with shared tags (cheap, solid); add behavior/popularity signals only when data justifies it.
18. Across all five patterns: recognition over recall — show users clickable cues (breadcrumb levels, tags, facet values, suggestions) instead of forcing them to remember and type.
19. Across all five patterns: restraint wins — fewer levels, fewer tags, fewer visible filters, fewer suggestions; every added element must reduce (not add) user effort.
