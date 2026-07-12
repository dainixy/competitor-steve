# Tommy Geoco — Making UX Decisions: Checklists — Improving Visual Style

Source: `02-Checklists/03-Improving visual style` (9 PDFs). Distilled for a coding agent building fast, foundation-driven web UI. Course examples reference "Cluster," a content-curation SaaS; specifics preserved where they carry numbers or decision criteria.

## 00 — Elements of visual style (overview)

Visual style = 8 controllable elements: **spacing, colors, elevation, iconography, typography, imagery/illustrations, motion/animation, texture/patterns**. Each is a lever for hierarchy, readability, and brand consistency.

Prerequisites before styling work (treat as an intake checklist):
- Have the brand palette / typography / existing style rules on hand before touching visuals.
- Know the target audience and usage context (e.g., professionals using a tool daily vs. casual visitors).
- Know the technical constraints of the delivery environment (web performance limits, browser support) before choosing visual treatments.

## 01 — Spacing

Decision questions to ask first:
1. How does spacing create hierarchy and readability here? (More space around an element = more emphasis.)
2. What layout pattern organizes this content best — grid, columns, whitespace blocks?
3. How does spacing adapt across screen sizes? Plan the responsive behavior, don't improvise it.
4. Are spacing units consistent everywhere?

Rules:
- **Define a base spacing unit (e.g., 8px) and use only multiples of it** (8/16/24/32…) across the whole interface. This single rule creates visual rhythm.
- **Use proximity to group:** related items (e.g., Edit/Delete/Share actions on a card) sit close together, separated from unrelated content. Spacing IS grouping.
- **Give primary actions generous whitespace** — ample padding around the main CTA makes it prominent without color tricks.
- **Touch targets: minimum 48×48px** with adequate spacing between tappable elements on mobile.
- **Body line height ≈ 1.5× font size**, applied consistently to all body text.
- **Hierarchy via spacing ratios:** larger vertical gaps BETWEEN sections than between items WITHIN a section. If between-section gap ≤ within-section gap, hierarchy reads as flat.
- **Match density to task:** tighter spacing in data-dense areas (tables, analytics), more generous spacing in reading/creation areas.
- On mobile, reduce inter-card spacing to use limited screen space — but keep the scale (drop to smaller steps of the same unit, don't invent new values).
- Balance elements against negative space deliberately; an uncluttered area around the working surface creates focus.

## 02 — Colors

Decision questions:
1. Which scheme (monochromatic / complementary / triadic) fits the brand and the emotional target?
2. What is each color's functional job — contrast, attention, meaning?
3. Does every color choice pass accessibility contrast?
4. How do the colors hold up across devices and lighting? Test on real screens.

Rules:
- **Contrast minimums: 4.5:1 for normal text, 3:1 for large text** (WCAG AA). Check especially text on colored backgrounds.
- **Limit the palette to 3–5 core colors**; get variety from shades/tints of those, not new hues.
- **Establish a color hierarchy and never break it:** one primary color reserved for main actions, one secondary for lesser actions, neutrals for everything else. A monochromatic scheme built on one brand color + neutrals is a safe, coherent default.
- **Reserve the primary/accent color for the actions you most want taken** (e.g., "Create," "Generate"). If the accent is everywhere, it points nowhere.
- **Interactive vs. static must be color-distinguishable:** clickable elements (buttons, links) get a treatment non-interactive text never gets.
- **Status colors are fixed vocabulary:** green = success, red = error, yellow = warning — used consistently everywhere, never repurposed.
- **Never rely on color alone for meaning** — verify with color-blindness simulators (Stark, Color Oracle) and adjust.
- Use subtle background color shifts to group/separate sections — cheaper and quieter than borders or heavy dividers.
- Plan light AND dark themes; dark mode is an inversion that must preserve readability and brand, not a naive flip.
- Check cultural color associations before shipping to new markets.

## 03 — Elevation (depth, shadows, layering)

Decision questions:
1. Where does depth genuinely help hierarchy (lifting interactive cards, separating sections)?
2. What depth complexity fits — flat, material-like, skeuomorphic? Pick one register and stay in it. (Course default: material-inspired, "clear but not dramatic.")
3. How does elevation respond to interaction (hover/active/selected)?
4. Does elevation reinforce the information architecture — higher elevation = more important/more interactive?

Rules:
- **Define 3–5 elevation levels** (e.g., subtle / medium / high) and use only those tokens; no per-component ad-hoc shadows.
- **Elevation must mean something:** higher elevation = interactive or focal (buttons, cards, floating toolbars); static background stays flat. Decorative-only shadows are noise.
- **Interaction feedback:** raise elevation on hover to signal interactivity; transition it smoothly, don't snap.
- **Dark mode needs its own shadow treatment** — adjust shadow color/intensity so depth survives without harsh contrast (shadows nearly vanish on dark backgrounds; compensate with lighter surface colors or adjusted shadows).
- **Performance rule: box-shadows are not free.** Use CSS `box-shadow` judiciously, especially on elements that repeat many times (lists, grids). Prefer few, simple shadows over complex multi-layer ones.
- Combine elevation with size and color for the single most important action — one cue alone is weaker than three aligned cues.
- Shadows must never obscure or reduce legibility of content underneath (modals/overlays).
- Use elevation to float working chrome (toolbars) above content, creating clear layer separation.

## 04 — Iconography

Decision questions:
1. Which icon style fits the aesthetic — outlined, solid, illustrated? Pick ONE.
2. Are the icons instantly recognizable — do they communicate without explanation?
3. Do they work at every size and in every color scheme they'll appear in?
4. Do icons support hierarchy and flow (e.g., primary nav icons slightly larger/colored vs. secondary)?

Rules:
- **One icon set, one style:** identical stroke weight, corner radius, and general style across every icon. Mixed icon sets are the fastest way to look amateur.
- **Use universal metaphors for common actions:** magnifying glass = search, bell = notifications, gear = settings, plus = add, user silhouette = profile. Don't get clever with these.
- **Label anything non-obvious:** text labels alongside icons for uncommon/specialized actions. Icon-only is earned by universality, not granted by default.
- **Ship icons as SVG** so they scale cleanly at any size and stay tiny on the wire.
- **Color icons purposefully:** accent color on icons only for the actions you want to stand out (create/generate class); everything else neutral.
- Ensure icon-to-background contrast, especially in dark mode (adjust color or add subtle outline).
- **Every icon needs accessible alt text / accessible names** for screen readers.
- Animate icons rarely and only as feedback (e.g., a save-confirmation checkmark) — never ambient decoration.
- Use icons to compress meaning (chart-type pickers, section markers), reducing reading load — but only where the metaphor is genuinely clear.
- Check icon metaphors for cultural differences before international launch.

## 05 — Typography

Decision questions:
1. What typeface matches readability needs + brand tone? (Course default: one modern sans-serif for a professional tool.)
2. How do size/weight/hierarchy guide attention?
3. How does type scale down/up responsively?
4. What mood does the type set — clarity/efficiency vs. warmth/character?

Rules:
- **One primary typeface, 2–3 weights** (regular/medium/bold). That's the whole system. Variety comes from size, weight, and spacing — not more fonts.
- **Define explicit styles for each level:** H1, H2, H3, body, captions, UI labels/buttons. Every text on screen belongs to a named style.
- **Use a modular type scale with a 1.2 or 1.25 ratio** between sizes so sizes relate harmonically instead of arbitrarily.
- **Line length 50–75 characters** for body content; **line height ≈ 1.5×** font size.
- **Contrast: 4.5:1 normal text, 3:1 large text** (same WCAG floor as colors).
- **Tracking:** slightly tighter letter-spacing on large headings; body text at default spacing. Never letter-space body copy tighter.
- **Weight = emphasis, used sparingly:** bold for primary actions/key UI, italic for subtle in-text emphasis. If everything is bold, nothing is.
- **Left-align body text** (easier reading); center-align only short headings or buttons.
- The interface must remain usable when users enlarge text — test with text scaled up.
- Reference type spec from the course's example system (useful starting shape): H1 medium ~30px, H2 regular ~24px, body 16px/line-height ~24, small body 14px, caption 12px uppercase with wide (+10) letter-spacing.

## 06 — Imagery and illustrations

Decision questions:
1. Which style (photographic / flat vector / abstract) matches brand and message? Pick one style and hold it.
2. What job does each image do — explain, orient, connect emotionally? (No job = cut it.)
3. How do images adapt across sizes/resolutions?
4. Do images support hierarchy and scannability (e.g., small icons/illustrations next to section headings)?

Rules:
- **One illustration style + one shared palette across all imagery** — consistency with the interface palette, not competing with it.
- **PERFORMANCE: compress and correctly format every image**; optimize for fast loads, especially for slow connections. This is a hard requirement, not polish.
- **Prefer SVG for illustrations** — scales to any resolution, small files.
- **Alt text on every meaningful image.** Decorative images should not pretend to carry meaning.
- **Illustrations must earn their place:** use them to simplify genuinely complex concepts (onboarding, empty states, process explanation) — never as filler. "Meaningful, not merely decorative" is the explicit test.
- **Use imagery sparingly in dashboards/functional areas** — highlight key features or empty states without crowding the actual functionality.
- Data visuals (charts/graphs) count as imagery: clear, well-designed, insight-first.
- Diverse, culturally sensitive representation when depicting people.
- Micro-animation on illustrations only as feedback (e.g., loading state for a long process) — judicious, not ambient.

## 07 — Motion and animation

(For a performance-first, non-flashy product: this section is mostly about restraint. Default to less.)

Decision questions:
1. What does this animation DO — feedback, orientation, progress? If the answer is "delight" alone, cut it.
2. Will it stay smooth on low-end devices? Test on both ends.
3. Where does motion become distraction? (Data-heavy screens: near-zero animation; only functional motion that aids understanding.)

Rules:
- **Micro-interactions: 200–300ms.** Hover states, toggles, small feedback — anything longer feels sluggish.
- **Every animation must be functional:** provide feedback, show progress/continuity, or clarify spatial relationships. No decorative motion.
- **Standardize easing curves and durations** — one animation vocabulary reused everywhere, not bespoke motion per component.
- **Spatial anchoring:** modals/panels animate from their trigger (rise from the button that opened them) so the cause-effect relationship reads instantly.
- **Respect `prefers-reduced-motion`** at the system level; provide static alternatives. Also offer an in-app reduce-animations option for motion-sensitive users.
- **Never block input with animation:** autosave indicators, transitions, etc. must not delay or prevent the user's next action (typing, clicking).
- Use attention animation (subtle highlight) only for genuinely new/changed content, and keep it non-disruptive.
- Loading/progress animation for long processes to manage expectations — this is one of the few "must-have" animations.
- Test animations across devices and browsers for smoothness; if it can't run smoothly everywhere, simplify or remove it.
- Brand-personality animation (logo/mascot) confined to loading or empty states, if used at all.

## 08 — Texture and patterns

(Lowest-priority element for a fast, minimal product; the source itself says subtle-or-nothing.)

Decision questions:
1. Does this texture/pattern add depth without overwhelming? If in doubt, omit.
2. Does it survive different screens without turning into visual noise?
3. Does it compete with buttons, icons, or text? If yes, remove or fade it.

Rules:
- **Subtlety is the entire game:** low-contrast noise/grain/paper textures only; if a texture is noticeable at a glance, it's too strong.
- **Text on patterned backgrounds needs boosted contrast** — patterns cost you legibility budget; pay it back.
- **Keep content-heavy areas pattern-free:** writing/reading surfaces stay clean; reserve texture for peripheral, non-critical areas.
- **Use SVG patterns** for sharp rendering at all sizes with small file sizes — texture must not cost load time.
- Dark mode: re-tune texture opacity/blend mode or textures create artifacts.
- Patterns can quietly separate sections (alternative to borders/dividers) and reinforce brand motifs — but consistency with the brand aesthetic is required, and sparingly is the dose.
- Animated/interactive patterns: confined to loading/welcome screens if used at all.

## Top rules from this unit

1. Define a base spacing unit (8px) and use only multiples of it everywhere; consistent scale = instant visual rhythm.
2. Larger gaps BETWEEN sections than WITHIN them — spacing ratios are how hierarchy reads.
3. Group by proximity: related controls sit close together, separated from unrelated content; spacing is grouping.
4. Touch targets minimum 48×48px with adequate spacing on mobile.
5. Contrast floors everywhere: 4.5:1 normal text, 3:1 large text — for type AND colored UI.
6. Limit the palette to 3–5 core colors; vary by shade/tint, never by adding hues.
7. Reserve the accent color for primary actions only; status colors (green/red/yellow) are fixed vocabulary, never repurposed.
8. Never encode meaning in color alone — verify with color-blindness simulation.
9. One typeface, 2–3 weights; a modular scale (1.2–1.25 ratio); every text element belongs to a named style.
10. Body text: 50–75 characters per line, ~1.5 line height, left-aligned.
11. Define 3–5 elevation tokens; elevation must mean interactivity/importance — no decorative shadows, and keep box-shadows cheap on repeated elements.
12. One icon set with uniform stroke/corner style; universal metaphors for common actions; label anything non-obvious; ship as SVG with alt text.
13. Images: compress and format for fast loading (hard requirement); SVG for illustrations; alt text on everything meaningful; no decorative filler.
14. Micro-interactions 200–300ms; standardize easing/duration; animation exists only for feedback, progress, or spatial orientation.
15. Respect `prefers-reduced-motion` and never let animation block user input.
16. Data-dense screens get tighter spacing and near-zero animation; reading/creation areas get generous spacing and clean, pattern-free surfaces.
17. Texture/patterns: subtle or absent; boost text contrast over any pattern; keep them out of content areas.
18. Dark mode is a designed variant, not an inversion: re-tune shadows, textures, and icon contrast specifically.
19. Stack cues for the single most important action (elevation + size + color together), and use that stack only once per view.
20. Before styling anything: have the brand palette/type rules on hand, know the audience and usage context, and know the performance constraints of the target environment.
