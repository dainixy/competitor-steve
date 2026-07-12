# Tommy Geoco — Making UX Decisions: Patterns / Accessibility

Distilled from unit 08 (6 PDFs: overview, keyboard navigation, ARIA attributes, alt text, color contrast, resizable text & zoom). Course frames accessibility as a set of implementation patterns, not compliance theater: accessible design usually improves UX for ALL users (readability, keyboard speed, SEO, low-bandwidth resilience).

## 00 — Accessibility overview

- Accessibility = digital products usable by everyone, including people with disabilities. Implementing it widens your audience AND typically improves the experience for everyone.
- The unit's five core patterns: keyboard navigation, ARIA attributes, alternative text for images, color contrast, resizable text and zoom. Treat each as a checklist item on every build.

## 01 — Keyboard navigation

Everything usable with keyboard alone — no mouse required. Serves motor disabilities, temporary injuries, screen-reader users (who navigate via keyboard), and power users.

### Rules
- Make EVERY interactive element reachable and activatable via keyboard alone (Tab to reach, Enter/Space to activate).
- Never rely on hover-only interactions — anything revealed on hover must also be reachable by keyboard.
- Never remove the default focus outline without providing a visible replacement. A distinct, visible focus state on all interactive elements is mandatory.
- Implement logical tab order that follows the visual layout of the page.
- Never create keyboard traps — the user must always be able to Tab away from any element.
- Provide a "skip to main content" link (or equivalent) to bypass repetitive nav/header content.
- Use standard, conventional key interactions (Tab between elements, Enter activates buttons/links, arrow keys within composite widgets) — match users' existing mental models; don't invent novel patterns.
- Offer keyboard shortcuts for frequently used actions (e.g. Ctrl+N new item, Ctrl+S save), and surface them in tooltips so they're discoverable (recognition over recall).
- Don't require complex multi-key combinations for essential actions — not all users can press chords.
- Test keyboard navigation across different browsers; don't assume it works.

### Psychology invoked
- Consistency (standard key patterns match mental models), Feedback (visible focus = "where am I"), Recognition over recall (shortcuts shown in tooltips).

## 02 — ARIA attributes

ARIA adds machine-readable meaning for assistive tech. Core doctrine: **native HTML first, ARIA second**.

### Rules
- Use native HTML elements/attributes (`<button>`, `<nav>`, `<main>`, `<label>`, etc.) before reaching for ARIA. Don't use ARIA as a substitute for semantic HTML.
- Don't overuse ARIA where standard HTML already conveys the semantics.
- Never contradict an element's native semantics with ARIA roles.
- Give icon-only buttons an accessible name: `aria-label` (e.g. `<button aria-label="Add new cluster">+</button>`).
- Use ARIA landmarks/roles to define page structure (navigation, main content) so assistive-tech users can jump between regions.
- Use `aria-live` regions to announce dynamic content changes that happen without a page reload (real-time updates, new comments).
- Update ARIA attributes whenever content changes dynamically — stale ARIA is worse than none.
- Use `aria-current="page"` in navigation to mark the active page.
- Use `aria-describedby` to link detailed text descriptions to complex visuals (charts, data viz).
- For form validation, pair `aria-invalid` with `aria-describedby` pointing at the error message — immediate, accessible feedback.
- Provide text alternatives for non-text content via `aria-label` or `aria-labelledby`.
- ARIA does NOT automatically make an app accessible — test with actual screen readers and assistive technologies.

### Psychology invoked
- Mental models (structure matches expectations), reduced cognitive load (clear labels/roles), feedback loop (accessible validation messages).

## 03 — Alternative text for images

Alt text serves four audiences at once: screen-reader users, search engines (SEO), slow-connection users whose images fail to load, and users who disable images. Directly relevant to a fast-loading, SEO-driven site: alt text is the fallback experience when images don't load.

### Rules
- Provide alt text for ALL meaningful images.
- Use empty alt attributes (`alt=""`) for purely decorative images so screen readers skip them.
- Keep alt text concise and descriptive; if a long description is needed, put it elsewhere (linked/adjacent text), not in the alt attribute.
- Never start alt text with "image of" / "picture of" — it's redundant; screen readers already announce it as an image.
- Don't keyword-stuff alt text for SEO; include keywords naturally only when the image genuinely relates to them (e.g. `alt="AI-powered content analysis dashboard showing engagement metrics"`).
- Don't repeat text that already appears in an adjacent caption or heading.
- Describe the content/purpose, not the file: for a logo, `alt="Clusters logo"`; for an icon button, describe the action (`alt="Add new item to cluster"`).
- For charts/graphs/data viz, alt text should convey the key insight, not just "chart" — summarize the main point, link to a full text description for detail.
- For user avatars, include the person's name in alt text to preserve conversational context.
- Update alt text whenever you swap the image.
- Test by browsing with images disabled — the page should still make sense.

### Psychology invoked
- Equivalent experience for all users; cognitive-load reduction (concise summaries of complex images); context preservation.

## 04 — Color contrast

Contrast = luminance difference between foreground (usually text) and background. It's not just a disability concern: it covers bright sunlight, cheap displays, and long reading sessions.

### Rules with numbers
- Minimum contrast ratio **4.5:1 for normal text** (including labels and button text) against its background.
- Minimum **3:1 for large text**.
- Treat these minimums as floors, not targets — aim higher when possible; meeting the minimum is not always sufficient.
- Check contrast for text over images or gradients — the worst-case region of the background is what counts.
- Check contrast in ALL states of interactive elements: default, hover, focus, active, disabled.
- Never rely on color alone to convey important information (add icons, text, patterns).
- Don't put essential information in low-contrast "decorative" styling.
- Use contrast-checking tools during design (not after), and test with color-blindness simulation tools.
- Build the brand palette with pre-vetted accessible combinations for all primary interface elements — accessibility and brand consistency are compatible if you plan the palette up front.
- Consider offering a high-contrast mode toggle for users who need more than the minimums.
- Use contrast deliberately for hierarchy: higher contrast on primary actions and key data pulls attention; this is a hierarchy tool, not just a compliance box.

### Psychology invoked
- Readability = lower cognitive load; contrast creates visual hierarchy; clear readable UI builds user confidence and reduces anxiety.

## 05 — Resizable text and zoom

Users must be able to enlarge content without breaking the layout. Benefits visually impaired users but also small screens, distance viewing, eye strain, forgotten glasses.

### Rules with numbers
- Use relative units (`em`/`rem`) for font sizes — never fixed pixel sizing that can't scale.
- Layout must remain functional and organized at **200% browser zoom minimum** — test at multiple zoom levels up to at least 200%.
- Never disable browser zoom (no `user-scalable=no`, no maximum-scale locks).
- No fixed-size containers that can't accommodate larger text — text must never overlap, get cut off, or hide content when enlarged.
- Increasing text size must not cause loss of content or functionality.
- Design fluid/responsive layouts so structure survives zoom, and check how resized text reflows the overall layout.
- Test resizing and zoom on mobile devices, not just desktop.
- Browser zoom alone is not sufficient for a content-heavy product — consider in-app text-size controls (e.g. in settings, with live preview), and persist the user's preferred size.

### Psychology invoked
- User control/autonomy (choose your own reading size), adaptability, reduced cognitive load from properly sized text.

## Top rules from this unit

1. Make every interactive element keyboard-operable: Tab to reach, Enter/Space to activate — no hover-only or mouse-only interactions, ever.
2. Never remove the focus outline without a visible replacement; a clear focus state on all interactive elements is non-negotiable.
3. Keep tab order logical and matching visual layout; never trap keyboard focus; provide a skip-to-main-content link.
4. Prefer native semantic HTML (`<button>`, `<nav>`, `<main>`, `<label>`) over ARIA; add ARIA only where HTML semantics fall short, and never contradict native semantics.
5. Give every icon-only button an accessible name via `aria-label`.
6. Use `aria-live` for content that updates without a page reload, and keep ARIA attributes in sync when content changes dynamically.
7. Pair `aria-invalid` + `aria-describedby` on form fields so validation errors are announced, not just shown.
8. Every meaningful image gets concise, descriptive alt text; every decorative image gets `alt=""`.
9. Never write "image of…" in alt text, never keyword-stuff it, never duplicate an adjacent caption — describe purpose/content naturally.
10. For charts, alt text conveys the key insight, not the chart type.
11. Text contrast: minimum 4.5:1 for normal text, 3:1 for large text — treat as floors, aim higher.
12. Verify contrast in every interactive state (hover, focus, active) and over images/gradients, not just static text on flat backgrounds.
13. Never convey information by color alone — pair with text, icons, or shape.
14. Vet the brand palette for accessible combinations up front, and use contrast intentionally as a hierarchy tool (highest contrast on primary actions).
15. Use `rem`/`em` for font sizes; the layout must survive 200% zoom with no clipped, overlapping, or lost content.
16. Never disable browser zoom.
17. Keyboard shortcuts for frequent actions are an accessibility AND power-user win — surface them in tooltips; avoid complex key chords for essentials.
18. Accessibility claims require testing: real screen readers, keyboard-only passes across browsers, images-disabled browsing, color-blindness simulators, and zoom testing on mobile.
