# Progressive Disclosure Patterns — Tommy Geoco, "Making UX Decisions" (Unit 03-Patterns / 02)

Distilled from 7 lessons: overview + 6 patterns (tooltips/popovers, nested menus, expandable rows, drawers/sheets, modals, read-more links). Source examples reference "Cluster," the course's fictional content-collaboration app.

## Core concept

Progressive disclosure = sequence information and actions across steps/screens so users see only the essentials first, and details expand only on request. Hide less-frequently-used options until needed. Origin: IBM's Carroll & Rosson (1983) found hiding advanced functionality early *increased* successful use of it.

Why it matters for fast, restrained UI: it is the anti-clutter tool. Less rendered upfront = lighter pages, easier scanning, lower cognitive load — you get simplicity without deleting capability.

### Anatomy of every drilldown pattern (3 parts)
1. **Trigger** — the behavior that engages the pattern (button click, hover).
2. **Container** — the block holding the secondary information/functionality (modal, popup, drawer).
3. **Contextual reference** — a visual link back to the "parent" view (transparent overlay, breadcrumb) so the user retains where they came from without holding it in working memory.

### The 3 psychological principles every pattern serves
- **Filtering** — hide irrelevant options so the user focuses on what matters now.
- **Recall** — the UI acts as external memory (headers, hierarchy, visible parent view) so the user memorizes less.
- **Efficiency** — quick access to actions/detail without navigating away or scrolling through irrelevant content.

### Choosing among the 6 patterns (decision criteria)
- Brief explanation of one element, no actions → **tooltip** (hover).
- Richer detail or quick actions about one element → **popover** (click).
- Hierarchical navigation across categories → **nested menu**.
- Skimmable list where each item has optional detail, inline on the page → **expandable rows**.
- Supplementary panel/task while main view stays partially visible → **drawer or sheet**.
- Critical confirmation, focused single task, or media preview that must block everything else → **modal** (last resort — most disruptive).
- Text-heavy content that should be truncated to an excerpt → **read-more link**.

---

## Tooltips and popovers

Small containers showing additional info about an element. **Tooltip** = hover-triggered, brief explanatory text only. **Popover** = click-triggered, can hold more detail or actions (e.g., mini profile card, quick-edit of tags).

Use for: explaining unfamiliar features/terms, icon meanings, keyboard-shortcut reminders, extra metadata (creation date, author, tags), mini profiles, quick contextual actions — all without spending permanent screen space.

**Do:**
- Trigger tooltips via keyboard focus as well as hover (accessibility requirement).
- Use appropriate show/hide timing: not so fast that accidental hovers trigger them, not so quick to hide that the user can't read them.
- Keep tooltip text brief and in plain language.
- Put actions in popovers (click), never in tooltips (hover).

**Don't:**
- Put critical or main content in tooltips — anything essential must be visible without hovering.
- Overuse tooltips; they lose their value when everywhere.
- Let tooltips obscure other important content or run off-screen.
- Use jargon or overly technical terms inside tooltip content (defeats their explanatory purpose).
- Show tooltips instantly on hover (unintentional triggers) or hide them the instant the pointer moves.

*(Note: the source PDF's "DO" column for this lesson contains misplaced carousel/slider items — a source error. Valid tooltip guidance extracted above.)*

## Nested menus

Hierarchical navigation: each menu item expands to reveal sub-items, letting users drill through the information architecture (e.g., Content > Articles > News / Blog posts / Research papers).

Use for: broad-AND-deep architectures, filtering step-by-step (type → topic → author), jumping directly to deep pages without intermediary navigation.

**Do:**
- **Limit depth to 2–3 levels** for most cases; beyond that complexity climbs.
- Keep each level thematically consistent — never mix category types at the same level.
- Use clear, concise category labels.
- Order categories logically: by priority, alphabetically, or by theme — pick one and commit.
- Provide escape hatches: Back button, breadcrumbs, ways to move back up levels.
- Keep menu style, behavior, and location consistent across the whole site.
- Add keyboard shortcuts for power users on frequent deep paths.

**Don't:**
- Use nested menus for primary navigation unless the information architecture genuinely justifies it.
- Create a category containing only one item — collapse that level.
- Make hover areas too small; sub-menus become hard to reach.
- Put actions (Delete, Edit) in navigation menus — menus are for navigation only.

## Expandable rows (accordions)

A header/summary that clicks open to reveal detail below, inline in the page. Makes pages skimmable; users drill into only the sections they care about.

Use for: dashboards of project/item summaries, content libraries (title + brief summary, expand for full detail), advanced/power-user settings hidden from novices, analytics (high-level metric visible, detail on expand), help docs, staged workflows.

**Do:**
- Write clear, descriptive headers that genuinely summarize each section's content — the header is the scan surface.
- Visually distinguish expandable headers from static content.
- Provide an obvious expand/collapse icon or button.
- Keep expanded sections scannable too: sub-headers and spacing inside.
- Animate expansion smoothly (short, functional — just enough to maintain context).
- **Default a section to expanded if the majority of users will need its content.**
- Make the expand/collapse hit target comfortably large.
- Support keyboard for expanding/collapsing.

**Don't:**
- Nest expandable sections many levels deep — users get lost.
- Hide information most users need inside a collapsed section.
- Expand ALL sections by default — that forfeits the whole benefit of progressive disclosure.
- Use vague or misleading header titles.

## Drawers and sheets

Containers anchored to a screen edge that overlay the main content when triggered. Drawer = side panel (navigation, filters, metadata detail). Sheet = typically bottom-anchored, common on mobile (create/edit forms, action lists like Edit/Share/Move/Delete for a selected item).

Key property: the main view stays partially visible → context is preserved and the user doesn't have to remember where they were.

**Do:**
- Use drawers for top-level navigation or filtering controls.
- Use sheets for creating, editing, or showing additional information about an item.
- Provide a clear dismissal: close button AND tap/click outside the container.
- Keep the main view partially visible behind the drawer/sheet.
- Use clear, concise labels for navigation items inside drawers.
- Prefer a bottom drawer over a sheet for content-heavy overlays.

**Don't:**
- Overload a drawer/sheet with too many options — it becomes its own overwhelm.
- Put essential, always-needed content in a drawer — essentials stay visible.
- Nest drawers/sheets inside each other — confusing interaction stack.
- Put ads or unrelated content in them.
- Auto-dismiss on item selection when the user likely wants to keep interacting (e.g., multi-select filters).
- Use a drawer as the app's main content area.

## Modals

Overlays that dim the background and **block interaction** with the main interface until closed. The most disruptive pattern — reserve for things that must not be overlooked.

Use for: confirming destructive/irreversible actions (delete project, remove team member — state the consequences), focused single-task editing, media previews (larger image/video without navigation).

**Do:**
- Use modals **sparingly** — only the most important information or actions.
- One primary action per modal; keep secondary actions minimal.
- Use clear, action-oriented button labels ("Save," "Delete") — never vague "OK."
- Provide a visible close button; also allow closing by clicking outside and pressing Esc.
- Size and center properly; darken the background to hold attention.
- Keep the modal focused on a single task with only the necessary fields.
- Test keyboard navigation and keyboard close.

**Don't:**
- Use a modal for nonessential info that could be shown inline (the #1 modal abuse).
- Stack modals (a second on top of the first) — never.
- Make the modal so large it fills most of the viewport — at that point it should be a page.
- Cram in multiple main actions or many secondary actions.

## Read-more links

Truncate text-heavy content to an excerpt with a link that expands the full text in place. Ideal for listings of multiple text items (feeds, content libraries, project descriptions) — each item truncates neatly and the user chooses what to expand.

**Do:**
- Make the excerpt substantial enough for the user to judge whether they're interested.
- Use clear, action-oriented link text ("Read full article"), never vague "More…".
- Position the link at the end of the excerpt so continuity is obvious.
- Consider making the whole excerpt/title clickable in addition to the link (bigger target).
- Expand/collapse with a smooth transition; expanded content must not shove other page elements around disorientingly.
- Provide a collapse control at the point where the user finishes reading — don't force scrolling back up to collapse.

**Don't:**
- Cut the excerpt mid-sentence or mid-thought.
- Hide information that's essential to understanding the main content behind the link.
- Overuse on short content — if the full text is barely longer than the excerpt, just show it.

---

## Top rules from this unit

1. Reveal only essentials first; expand detail on user request. Hiding advanced options early *increases* their successful use (IBM, 1983).
2. Every disclosure pattern needs three parts: a trigger, a container, and a contextual reference back to the parent view — never strand the user without context.
3. Never hide essential or critical information behind any disclosure mechanism (tooltip, collapsed row, drawer, read-more). Essentials stay visible.
4. Match the pattern to the job: tooltip = brief hover explanation, popover = click detail/actions, nested menu = hierarchy navigation, expandable row = inline optional detail, drawer/sheet = side task with context kept, modal = blocking critical task, read-more = text truncation.
5. Use modals sparingly and only for what must not be overlooked (destructive confirmations, focused single tasks). If it could be inline, put it inline.
6. Never nest modals, and never nest drawers/sheets inside each other.
7. One primary action per modal; button labels are action verbs ("Delete," "Save"), never "OK."
8. Every overlay needs an obvious exit: visible close button + click-outside + Esc, all keyboard-accessible.
9. Limit nested-menu depth to 2–3 levels; keep each level thematically consistent; never create a one-item category.
10. Navigation menus contain navigation only — no Delete/Edit actions inside menus.
11. Provide escape hatches in hierarchies: Back buttons and breadcrumbs to move back up levels.
12. In accordions, headers are the scan surface: descriptive titles, visually distinct from static content, obvious expand icon, large hit target.
13. Default an expandable section open if most users need it; never default ALL sections open (kills the pattern's value).
14. Keep the main view partially visible behind drawers/sheets — preserved context is the entire point of choosing them over navigation.
15. Don't auto-dismiss a drawer/sheet on selection when further interaction is likely (filters, multi-select).
16. Tooltips: keyboard-focus triggerable, plain language, correct timing (not instant-show, not instant-hide), never covering important content, never carrying actions.
17. Read-more excerpts must end at a complete thought and give enough context to judge interest; the link says what it does ("Read full article").
18. Expanded content must not disorientingly push the page around; transitions are smooth and short, and a collapse control sits where the user finishes reading.
19. Order menu options deliberately (priority, alphabetical, or thematic) and keep pattern style/behavior/location consistent across the entire product.
20. Overuse destroys every one of these patterns: too many tooltips, too many drawer options, modal-for-everything, read-more on short text — restraint is the operating principle.
