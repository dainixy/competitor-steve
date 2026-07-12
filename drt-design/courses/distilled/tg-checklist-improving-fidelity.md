# Tommy Geoco — Making UX Decisions: Checklists / Improving Fidelity

Source: 8 checklist PDFs from the "Improving fidelity" unit. Fidelity = the level of detail showing how a design should look and *behave* in production. Use these checklists once basic structure/layout exists and you're refining toward production quality. Sections are independent — jump to whichever aspect you're refining. (Visual style is a separate unit.)

The seven fidelity aspects: component states, primary interactions, secondary interactions, content scalability, system feedback, user input, navigation.

---

## 1. Component states

States = the visual representations of a UI element per interaction/system status (default, hover, active, disabled, focus). Well-designed states are how the interface tells the user what is happening.

### Checklist
- Enumerate states for EVERY interactive component: default, hover, active, disabled — plus any app-specific states (loading, selected, error).
- Differentiate each state visually using color, opacity, border, or shadow — and keep the treatment consistent with the design system.
- Make state transitions smooth, not jarring; verify state clarity holds across devices and screen sizes.

### Rules
- Use distinct AND consistent visual cues per state. Concrete recipe: darken button color by ~10% on hover, applied identically to all buttons.
- Give every interactive element a hover state (e.g., subtle background-color change on list items to signal clickability).
- Make disabled states visibly non-interactive: muted color + remove the hover effect. A disabled button must not respond to hover.
- If you animate state changes at all, keep them quick and subtle — 200–300ms is the reference duration (e.g., a small scale on click). Nothing longer or decorative.
- Apply identical state treatments to similar components (Create/Edit/Delete buttons all share the same hover/active/disabled styling).
- Maintain sufficient contrast BETWEEN states, not just against the background — check this explicitly in dark mode (e.g., toggle "on" state vs. dark background).
- Implement clear focus states for keyboard navigation: a prominent outline or glow on the currently focused element. Never rely on hover alone.

---

## 2. Primary interactions

Primary interactions = the few critical actions users came to perform. Emphasizing them guides attention and improves usability.

### Checklist
- List the primary interactions per view (typically 1–4: create, add, generate, share).
- Verify each is immediately discoverable within its view — prominent placement (e.g., top-right or floating action button on a dashboard).
- Decide how each is visually emphasized: size, color, placement.
- Decide the affordance that communicates interactivity: button, link, drag handle.

### Rules
- Rank interactions by importance and let visual prominence follow that rank ("Create" outranks "Settings" — style accordingly).
- Use recognizable affordances — a clickable action must look like a button, not styled text.
- Put the primary action in a consistent, prominent location in every view (same spot each time).
- Pair icon + text label to reinforce the action ("+ New Cluster"), not icon alone.
- Style all primary actions identically across the interface: same color, size, general style.
- Weight prominence by frequency of use, not just importance: make "Edit" more prominent than "Delete" if editing happens more often.
- Reserve the primary brand color for the most important actions and ensure it contrasts well against the background — this is what makes primary CTAs pop; don't spend that color elsewhere.
- Give immediate visual feedback on primary actions: show a loading state or progress indicator the instant the user clicks.

---

## 3. Secondary interactions

Secondary interactions = less frequent, supporting actions. The design problem is a balance between discoverability and simplicity.

### Checklist
- List the secondary interactions and decide how each is progressively disclosed (behind an Edit button, menu, hover reveal) so it doesn't clutter the default view.
- Decide the visual cue that signals hidden options exist (tooltip, icon, microcopy).
- Verify secondary actions are still easy to reach when needed (dropdown or icon in context).

### Rules
- Group related secondary actions in a single menu (rename/move/delete together in one dropdown), not scattered as separate icons.
- Hide complexity behind progressive disclosure: hover reveals, toggles, menus.
- Use ONE consistent "more options" affordance app-wide (e.g., the three-dot "..." icon everywhere).
- Never let a secondary action visually compete with the primary action in the same view (canonical pattern: filled/dark "Save" next to plain/ghost "Cancel").
- Reuse the same pattern for the same meaning everywhere: if a gear icon means settings once, it means settings everywhere.
- Tune how buried an action is by its frequency and importance — rarely used but critical actions still need a findable home.

---

## 4. Content scalability

Content scalability = how well the interface survives varying amounts and types of content. Design must hold with 3 items and with 300.

### Checklist
- Check the layout with both extremes: short vs. long text, few vs. many items.
- Decide explicitly what happens on overflow: truncate with ellipsis, wrap to a second line, scroll, or paginate — per element (e.g., card titles).
- Define responsive breakpoints: how does the layout adapt mobile → tablet → desktop?
- Verify readability and visual hierarchy survive at every content scale (one paragraph vs. several pages).

### Rules
- Build layouts with flexbox/grid so they adapt to content size — e.g., a responsive card grid whose column count follows screen width.
- Cap text line length with max-width: target ~60–75 characters per line for body text readability.
- Pick an explicit overflow mechanism (truncation, pagination, scrolling) once a list passes a threshold — never let it silently break.
- Test with REALISTIC content at both minimal and extensive scales; lorem-ipsum-sized placeholder content hides scalability bugs.
- Use relative units (em, rem, %) for sizes — define text in rem so it scales with device size and user font-size preferences. Avoid fixed px for type.
- For large datasets, load progressively (chunked loading as the user scrolls) — this is a performance rule as much as a UX rule: don't ship the whole dataset up front.
- Keep interactive elements tap-friendly at all content scales — long titles must not shrink or crowd out the Edit/Delete tap targets on mobile.

---

## 5. System feedback

Feedback communicates the result of user actions and system status changes; it's what builds trust in the interface.

Feedback delivery patterns to choose from (each has a place): alert, top banner, bottom sheet, toast message, modal, inline alert.

### Checklist
- Define the visual cues used for each feedback type: loading indicator, success message, error state.
- Separate GLOBAL feedback (system-wide → top-bar notification/banner, e.g., "Changes saved") from LOCAL feedback (component-specific → inline, e.g., form-field validation next to the field).
- Match delivery to urgency: critical errors (data loss) → bold red + persistent modal that must be acknowledged; routine confirmations → subtle green checkmark that doesn't interrupt.
- If motion is used for feedback, it should confirm the action (e.g., a card sliding into its new place), not decorate.

### Rules
- Provide immediate feedback for every user action — color change + loading indicator the moment the click lands.
- Use one consistent visual vocabulary: checkmark = success, exclamation = warning, everywhere.
- Scale visibility to urgency: errors more prominent and more persistent than success messages.
- Never encode status in color alone — add icons or patterns so color-blind users can distinguish states (accessibility requirement).
- Every error message must include next steps or a resolution path, not just "something went wrong" — tell the user specifically how to fix it.
- Progressive-disclose complex feedback: show the summary, offer "View Details" for depth.
- Make feedback contextual to the current task ("5 items moved to 'Research' cluster"), not generic ("Operation successful").

---

## 6. User input

Well-designed inputs streamline data entry and minimize errors.

### Checklist
- Match the control to the data type: text field for free text, dropdown for predefined categories, checkboxes for multi-select, calendar picker for dates (never a free-form text field for a date).
- Define visual + interactive error handling: real-time validation, green checkmark on valid, red message on invalid.
- Audit every label: clear, concise, specific ("Enter article title" / "Paste content URL here", never "Enter text").
- Confirm the form works with touch, keyboard, and mouse; consider voice where relevant on mobile.

### Rules
- Label every field descriptively — "Summary Length", not "Length". No label-less inputs.
- Use placeholder text for format hints/examples only ("Enter tags separated by commas") — placeholders supplement labels, never replace them.
- Validate in real time and pair every error with resolution guidance (duplicate name → suggest alternatives immediately).
- Enable autofill/autocomplete wherever possible to cut typing (e.g., autocomplete on user search).
- Group related fields into logical sections (all metadata — tags, category, publish date — together).
- Make interactive input areas sufficiently large and visually distinct (dropdowns, checkboxes must be obvious tap targets).
- Progressive-disclose complex forms: show basic fields first, reveal advanced filters on demand.

---

## 7. Navigation

Navigation must answer three questions at all times: where am I, where can I go, how do I get there.

Navigation categories to keep distinct: **product** navigation (core content/features), **contextual** navigation (related to the current item), **system** navigation (help, settings, profile), plus global vs. local.

### Checklist
- Categorize and label nav options by type (e.g., Content / Team / Analytics / Settings).
- Visually separate global navigation (persistent sidebar/main menu, breadcrumbs) from local navigation (tabs/sub-menus inside a section).
- Choose organizing patterns deliberately: tabs for views within an entity ("Overview / Content / Analytics / Settings"), accordions, etc.
- Define how nav adapts per screen size (mobile: collapse into hamburger/off-canvas/dropdown).

### Rules
- Use plain, literal labels — "My Clusters", "Team", "Analytics". Never clever or ambiguous nav terms.
- Group nav options by user goals and information hierarchy (all content-management options together).
- Encode hierarchy visually: main nav prominent and always visible; sub-nav smaller and contextual.
- Show current location: breadcrumbs like "My Clusters > Marketing Campaign > Blog Post" for deep hierarchies.
- Make nav responsive: collapse gracefully on small screens.
- One selection pattern per job, app-wide — if a dropdown selects clusters in one place, use a similar dropdown for similar selection tasks elsewhere.
- Add shortcuts to frequent destinations (e.g., a "Recent items" quick-access list in global nav).
- Use sticky navigation on long scrolling pages so the main nav stays reachable.

---

## Top rules from this unit

1. Enumerate default/hover/active/disabled/focus states for EVERY interactive component before calling a design done; give each a distinct, system-consistent visual cue (color, opacity, border, shadow).
2. Standard hover recipe: darken the element's color ~10%; apply the exact same shift to every element of that kind.
3. Disabled = muted color + no hover response. Focus = prominent visible outline for keyboard users — never hover-only interactivity.
4. If animating state changes at all, keep them 200–300ms and subtle; motion exists to confirm actions, never to decorate.
5. Let visual prominence follow importance × frequency of use: primary action biggest/brand-colored/consistently placed; "Edit" beats "Delete" if it's used more.
6. Reserve the primary brand color for primary actions only, with strong contrast against the background — spending it elsewhere kills the hierarchy.
7. Give immediate visual feedback (loading/progress state) the instant any primary action is clicked.
8. Hide secondary actions behind progressive disclosure (one consistent "..." menu, related actions grouped) and never let them visually compete with the primary action.
9. Reuse one pattern per meaning app-wide: same icon = same function, same selection pattern for same task, same feedback vocabulary (checkmark = success, exclamation = warning).
10. Cap body text at ~60–75 characters per line via max-width.
11. Size type in rem (relative units), not fixed px, so it respects device and user font-size preferences.
12. Decide overflow behavior explicitly per element — truncate/wrap/scroll/paginate — and test layouts with realistic content at both extremes (3 items and 300).
13. Load large datasets progressively (chunks as the user scrolls) instead of shipping everything up front — a UX rule that doubles as a performance rule.
14. Route feedback by scope and urgency: global events → top banner; local events → inline next to the component; critical errors → persistent modal in red; routine confirmations → subtle non-blocking checkmark.
15. Never encode status with color alone — add an icon or pattern for color-blind users.
16. Every error message names the problem AND the fix ("duplicate name — try X"), in real time, next to the field.
17. Match input controls to data types (calendar picker for dates, dropdown for categories, checkboxes for multi-select); label every field specifically; placeholders show format examples, never replace labels.
18. Navigation labels are plain and literal, hierarchy is visible (prominent global nav vs. contextual sub-nav), and breadcrumbs show location in deep structures.
19. Keep tap targets large and usable at all content scales and screen sizes — long content must never crowd out interactive elements.
20. Consistency is the master rule of fidelity: identical treatments for identical roles (states, buttons, icons, feedback, nav patterns) across the entire interface.
