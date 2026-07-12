# UX Top Rules — Injection Reference

The ~100 highest-leverage rules from Tommy Geoco's *Making UX Decisions* and Nguyen Le's *Process Masterclass*. Selection criterion: rules that most change what a coding agent produces when building web UI. Grouped by topic. Every line earns its place. See UX-PLAYBOOK.md for full context, attribution, and conflicts.

## Process & Decision-Making
1. Work in order: Outcome → Structure → Interaction → Visual. Never start with visual polish; the decision *order* determines the outcome.
2. Structure content (IA, flows, wireframes) before styling anything; if you can't justify an element's position by a user goal or business objective, it's wrong.
3. For every screen/component, be able to state instantly what it achieves for the business and the user (the "tap-on-the-shoulder" test).
4. Aim for effectiveness, not perfection — ship a reversible bet and iterate rather than perfect an irreversible one.
5. Default to established patterns; innovate only for a core differentiator with the resources to validate it. Copy the commodity (login/settings/nav/upload), design the differentiator.
6. Never invent a new interaction for originality's sake — if a standard dropdown works, ship the dropdown.
7. Weigh conflicting decisions: research > user familiarity > institutional best-practice; fall back up the chain when a level is missing. Familiarity beats "optimal" absent data.
8. Follow established conventions by default (nav placement, familiar labels) — breaking familiarity has a measured cost.
9. Go wide before deep: ≥6 distinct low-fi concepts at identical fidelity, then pick 1–2; build 2+ real layout alternatives before committing.
10. Test with realistic minimal AND massive datasets and real copy — lorem ipsum and happy-path data hide real failures.
11. Consistency is the meta-rule: same type styles, spacing scale, size scale, and color meanings everywhere — every inconsistency is added cognitive load.

## Information Architecture & User Tasks
12. Build IA around the top 5–10 user tasks first; design the most frequent/important tasks before settings/billing; defer edge cases.
13. Group items the way users think, not the org chart; validate IA with card sorting or tree testing.
14. Write JTBD as outcome ("so I can…"), never as feature; every user story ladders up to a business objective or gets cut.
15. Nav labels are literal, never clever ("My Clusters," "Analytics"); breadcrumbs on any hierarchy deeper than one level.
16. Classify every nav item as Product, Contextual, or System nav; never mix system items (settings/billing) into primary nav.
17. Design for every entry point, not just the homepage — every standalone page must make sense on its own.
18. Prioritize nav by frequency of use; few grouped items up front, everything else behind a clearly-cued "More," but all options stay discoverable including on small screens.

## Visual Hierarchy
19. Build hierarchy from size + weight + color together, never one channel alone; one visually dominant primary action per view.
20. When a design feels flat, check whether everything competes at the same visual weight — that's usually the bug.
21. Mix hierarchy mechanisms per tier: size, contrast, and color are separate levers (a small button can win attention via color while a hero wins via size).
22. Actively de-emphasize (shrink/tighten) secondary elements that would compete with the primary one.
23. Prefer whitespace over borders/boxes/shadows for grouping; give the primary CTA extra surrounding whitespace.
24. Group related tightly, separate unrelated with more space; adjacency creates association — false proximity creates false associations.
25. Left-align text by default; align labels to fields; use a grid; consistent alignment reads as order.
26. Reserve one unique high-contrast color for the single thing that must be noticed (Von Restorff).

## Typography
27. One typeface, 2–3 weights (regular/medium/bold) — variety from size/weight/spacing, not more fonts.
28. 16px base font size for reading UIs (14px acceptable for dense app UIs); use a modular scale, ratio 1.2–1.25.
29. Reference scale: 12 / 14 / 16 / 18 / 20 / 24 / 30 / 36 / 48 / 60 / 72 px; every text element belongs to a named style (H1/H2/H3/body/caption/UI).
30. Body line length 50–75 characters (cap with max-width); line height ≈ 1.5× font size.
31. Left-align body copy; don't center or justify past ~5 lines; center only short headings/buttons.
32. Prefer a clean sans-serif for interface text; neutral product UI → neo-grotesque or humanist; reserve display/geometric/high-contrast serifs for branded moments.
33. Display typefaces are for headlines only — never body copy.
34. Never wide-track lowercase (it reads wonky); wide tracking is for caps only; keep body-copy tracking default.
35. h1 occurs once per page; if text is too big for its importance, demote the heading level rather than force the size.
36. Match icon stroke weight to adjacent letterform stroke weight.

## Color
37. Limit the palette to 3–5 core colors; get variety from tints/shades, not new hues.
38. Reserve one primary/accent color for the actions you most want taken; if the accent is everywhere it points nowhere.
39. Status colors are fixed vocabulary: green = success, red = error, yellow = warning — never repurposed.
40. Never encode meaning in color alone — pair with icon/label/pattern; verify with a color-blindness simulator.
41. Contrast floors (treat as floors): 4.5:1 normal text, 3:1 large text; check every state and text over images/gradients.
42. Reserve color as the interactivity signal — clickable elements get a treatment static text never gets.
43. Dark mode is a designed variant, not an inversion — re-tune shadows, textures, and icon contrast.

## Spacing & Layout / Grids
44. Define one base spacing unit (8px) and use only multiples of it everywhere — this single rule creates rhythm.
45. Larger gaps BETWEEN sections than WITHIN them; if between ≤ within, hierarchy reads flat.
46. Spacing communicates grouping — tight within a related group, generous between groups.
47. Grid by product type: 12-column + baseline grid for responsive websites; 8px/8pt grid for dense app UIs.
48. Baseline unit = body line-height ÷ 2 (24px line-height → 12px baseline); keep spacing to multiples of it.
49. Responsive columns: desktop 12 (margins ~30–50px, gutter ~30px) → tablet 12 (margin ~20, gutter ~15) → mobile 4 (margin ~25, gutter ~20).
50. Card-grid responsive cascade: 3-column → 2-column → 1-column as width shrinks.
51. Don't design to named device sizes — let the layout break wherever content naturally demands it.
52. Use relative units (rem/em/%), not fixed px, so text scales with device and user preference; build on flexbox/grid.
53. Design desktop and mobile concurrently; the grid is a guide — snap by default, break only as a deliberate optical call.
54. Build reflowing panels with Auto Layout and stress-test the overflow case (~30 items).

## Components & States
55. Design every state: default, hover, active, disabled, keyboard focus (+ async "processing").
56. Every interactive element gets a hover state (e.g. darken 10%, same shift everywhere); disabled reads as dead.
57. Always show a visible focus indicator; never remove the default outline without a replacement.
58. Feedback animations 200–300ms; standardize easing/duration; animation is feedback, not decoration.
59. Style all primary actions identically app-wide; weight action prominence by frequency of use (Edit ≫ Delete); give immediate feedback on click.
60. Progressively disclose secondary actions behind a consistent "…" overflow affordance; never let them compete with the primary.
61. Match input control to data type: date picker for dates, dropdown for categories, checkbox multi-select, radio single-select.
62. Buttons (not a dropdown) for a small set of options so users see all choices + stock state at a glance; dropdown only for long lists.
63. Label every field specifically ("Enter article title," not "Enter text"); placeholders are format hints, never the label.
64. Prefer a smart/searchable input over a very long dropdown (Hick's Law).
65. Define 3–5 elevation tokens; elevation must mean interactivity/importance — no decorative shadows.
66. Soft-and-wide beats hard-and-tight for separation shadows (e.g. modal ~250px blur at ~20% opacity).
67. One icon set, uniform stroke/corner; universal metaphors only for icon-only; label anything non-obvious; ship as SVG with accessible names.
68. Componentize the moment something repeats; name components by what they ARE (never by breakpoint); enforce one team-wide term per component.

## UI Patterns
69. Never hide critical info or primary actions behind any disclosure container (tooltip, collapsed accordion, drawer, read-more).
70. Every drilldown needs three parts: trigger, container, and a contextual reference back to the parent (breadcrumb/overlay).
71. Reserve modals for critical/irreversible actions; one decision per modal; action-verb labels ("Delete Project," never "OK"); closable via button, Esc, and click-outside; never nest.
72. Prefer undo (control placed where the action happened) over confirmation dialogs for reversible actions.
73. Limit nested menu depth to 2–3 levels; never put actions inside navigation menus; never a category with one item.
74. Default expandable sections open when most users need them, closed otherwise.
75. Chunk lists into groups of 5–9 items with headings; cap top-level nav at 5–9 (ideally 4–5).
76. Paginate goal-oriented lists (10–20/page, show current/total); infinite-scroll only exploratory feeds; always preserve list position on back.
77. Auto-rotating carousels with no user control are wrong; keep critical content out of carousels entirely.
78. Steppers: label each step, show position + steps remaining, allow back-edit and save-and-resume; keep step count low.
79. Forms: ask only what's essential now; smart defaults + prefill + autofill; reveal advanced fields via progressive disclosure, not a wall of "(optional)."
80. Validate on blur (not per keystroke); state why input is invalid and how to fix it; show the positive state; always re-validate server-side.
81. Error message = plain language + what went wrong + one actionable fix; non-blaming tone; no bare error codes.
82. Immediate feedback for every action: global events → toast/banner, local events → inline.
83. No progress indicator under 1–2 seconds; determinate bar when duration is known, spinner only for unknown; never fake progress.
84. Autosave at intervals + after significant changes; subtle "saved" indicator; keep versions revertible; still allow manual save.
85. Empty states are helpful and actionable: one explanatory element + a clear next action, without crowding functionality.
86. Tours/tips/tutorials never substitute for intuitive design; onboarding is always skippable; never gate app usage behind it.
87. Bottom navigation (mobile): 3–5 items, icons + short labels, clear active state, never hidden on scroll, never on desktop.
88. Breadcrumbs: every level clickable except the current page; supplement primary nav, never replace it.
89. Global search prominent in top nav with a visible shortcut (⌘K) + autocomplete; faceted filters show per-facet counts, total results, one-click reset-all.
90. Social proof must be authentic, permissioned, current; ratings + counts at the decision point; never fake quotes or stock faces.
91. Adaptive/personalized behavior is subtle, explained, override-able, based on consistent (not single) signals, and never removes access to anything.

## Accessibility
92. POUR is the floor; semantic HTML first, ARIA only for what HTML can't express — and test with a real screen reader.
93. Every interactive element keyboard-reachable with a logical tab order; no keyboard traps; provide a "skip to main content" link; never hover-only.
94. `aria-label` on ambiguous/icon-only controls; `aria-live` for dynamic changes; `aria-current="page"` for active nav; keep ARIA in sync.
95. Alt text on every meaningful image; `alt=""` on decorative; no "image of…" prefix; keywords natural not stuffed.
96. Layout must survive 200% browser zoom with nothing clipped; never disable browser zoom; use rem/em for font sizes.
97. Build accessibility in from the start — cheaper than retrofitting and improves usability for everyone.

## Performance / Speed
98. Load large datasets in subsets (pagination/lazy-load), never all at once — a cognitive-load AND Core Web Vitals win.
99. Compress and correctly format every image (hard requirement); prefer SVG for icons/illustrations/patterns; keep one aspect ratio from full-size to thumbnail.
100. Use box-shadows judiciously on repeated elements; test sticky/fixed elements and animations on low-end devices; never let animation block input; avoid layout shift (CLS) from expansion.
101. Response speed is a UX feature (Doherty Threshold) — treat "loads fast" and "updates without lag" as design requirements, not afterthoughts.

## Copywriting in UI
102. Copy is part of design — use real content in wireframes; label actions in plain human words; no jargon in labels, tooltips, steps, or errors.
103. Button/link text names the action ("Save," "Read full article"), never "OK"/"More…"; feed brand voice into microcopy.
104. Match vocabulary to the audience; preserve users' verbatim words when synthesizing research; spell-check every page before "done."

## Encoding a Visual Direction
105. Test directions with moodboards (broad references) and styleboards (assets you build) before any full concept; time-box a styleboard to hours–1 day.
106. Encode direction in plain adjectives + a written purpose statement + personality/copy direction, not just pinned images.
107. Climb the maturity pyramid in order — functional → reliable → usable → pleasurable; don't ship "delightful" on day one.
108. Restraint is the house style: 1–2 typefaces, strict grid, black/white + one accent — hierarchy through structure, not decoration.
109. Mine offline/adjacent-domain inspiration before Dribbble so output doesn't look templated; prioritize references matching your goals over flashy consumer apps.
110. Build a design system only when multiple teams/sub-brands need it; organize components Atomic-Design style (atoms → components), keep it flexible enough to extend.
