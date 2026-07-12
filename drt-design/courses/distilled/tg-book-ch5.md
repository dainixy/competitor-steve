# Making UX Decisions (Tommy Geoco) — pages 401–500

**Covers:** end of Module 17 (Patterns for social proof: social media integration, badges & seals) · Module 18 (Patterns for feedback and visibility) · Module 19 (Patterns for error prevention and handling) · Module 20 (Patterns for accessibility) · start of Module 21 (Patterns for personalization: intro + customizable dashboards, continues past p.500).

Format note: every pattern in the book follows the same skeleton — definition → benefits/use cases → psychological principles → wrong-way/right-way comparison → DO/DON'T list. The DO/DON'T lists are the actionable core; they're preserved verbatim-in-spirit below.

---

## Module 17 (end): Patterns for social proof

### Social media integration (share buttons, social login, embedded social activity)

- Make sharing optional and unobtrusive — never force users to share or connect accounts.
- Provide pre-written content for social shares (lowers friction to share).
- Offer social login ("Sign in with Google") to reduce sign-up friction.
- DO: respect user privacy/data; keep integrations current; measure impact of the integration.
- DON'T: force account connection; overwhelm with too many share options; auto-post to users' accounts; ignore per-platform context; clutter the interface with social widgets.
- Performance/restraint angle: embedded social feeds and share widgets are decoration unless they demonstrably build trust — the book's "wrong way" example is exactly "cluttering the interface with social media."

### Badges and seals (verification badges, security seals, achievement badges)

- Use authentic, third-party-verified badges (SSL/security seals on login and payment pages; "Verified" on vetted accounts). Fake or misleading badges destroy trust — that's the book's explicit "wrong way."
- Use badges for quick visual role cues (Admin, Creator) — they communicate faster than text.
- Named principles: **Authority** (official seals raise perceived credibility), **Scarcity** (hard-to-earn badges are valued more), **Goal-Gradient Effect** (tiered badges with visible progress drive engagement).
- DO: make badge criteria clear and achievable; use visually distinct, meaningful designs; review/update the badge system regularly; make badges accessible (not image-only meaning).
- DON'T: overuse badges (dilutes their value); make badges the primary focus of the UI; ignore users gaming the system; treat badges as a substitute for real trust-building.

---

## Module 18: Patterns for feedback and visibility

Module scope: progress bars & loaders, notifications & alerts, confirmation messages, real-time validation, contextual help. Purpose: tell users what the system is doing, confirm their actions, reduce uncertainty, prevent errors.

### Progress bars and loaders

- Use a **linear/determinate progress bar** when duration or step count is known; use a **spinner/indeterminate loader** only for unknown waits.
- **Threshold: do NOT show a progress bar for operations under 1–2 seconds.** Fast operations should just complete.
- Never use fake or artificially slowed progress indicators.
- Add context when possible: percentage complete and/or estimated time remaining (reduces uncertainty and abandonment).
- For background tasks (sync, uploads), use a subtle indicator that lets the user keep working.
- Keep the indicator visible and appropriately sized, but never let it distract from main content.
- Provide non-visual alternatives (text/ARIA status) for users who can't perceive the visual indicator.
- Named principles: **Goal-Gradient Effect** (visible progress increases motivation to finish), **Uncertainty Reduction** (status info lowers anxiety), **Feedback Loop**.

### Notifications and alerts

- Prioritize by importance and relevance to the user — every notification must earn its interruption.
- Keep notification copy clear and concise; make each notification actionable.
- Give users control over notification preferences (types, frequency, channels).
- Use distinct styles/urgency levels for different notification types.
- Make notifications dismissible; never interrupt a critical task with one.
- DON'T: overwhelm with volume; notify about trivia; ignore platform notification guidelines; send at bad times (middle of the night); use notifications to paper over bad in-app communication.
- Named principles: **Zeigarnik Effect** (incomplete-task reminders pull users back), **FOMO**, **Operant Conditioning** (positive milestone notifications reinforce behavior). Use these sparingly and honestly.

### Confirmation messages (post-action feedback, e.g. toasts: "Your preferences have been saved")

- Confirm important or irreversible actions; skip confirmations for trivial or easily reversible ones (they train users to click through).
- Use clear, specific language and include relevant detail: what changed, who was affected, when it takes effect ("Post scheduled for June 3, 9:00").
- Position the confirmation close to the triggering action.
- Offer confirm/cancel options when the action hasn't happened yet; a clear dismiss when it has.
- Style confirmations consistently across the whole interface.
- Don't rely on confirmations alone to prevent errors — good design should prevent the mistake upstream.
- Named principles: **Uncertainty Reduction**, **Feedback Loop**, **Locus of Control** (confirm/cancel gives users control).

### Real-time validation (inline form validation)

- Validate as the user works, but **fire validation on blur (after the field is completed), not on every keystroke** — premature errors while typing are hostile.
- Say specifically WHY input is invalid and how to fix it; add help text or suggestions.
- Use visual cues (color + icon) for valid/invalid — **never color alone** (accessibility).
- Show positive state too (green check on valid fields) — increases long-form completion.
- Don't block submission on non-critical validation issues.
- Don't stack many simultaneous error messages.
- **Always validate server-side as well — client-side validation can be bypassed.**
- Keep validation performant; laggy validation is worse than none.
- Named principles: **Immediate Feedback**, **Progressive Disclosure** (reveal rules as they become relevant, e.g. password requirements appear as the user types), **Error Prevention**.

### Contextual help (tooltips, help icons, inline explanations)

- Put help where the question arises — next to the setting/label it explains — not in a separate docs section.
- Keep help content concise and strictly relevant to the current context.
- Use one consistent indicator (e.g. "?" icon) for help across the whole interface.
- Offer the right form per situation: tooltip, inline text, expandable section.
- Let users dismiss/hide/disable contextual help.
- DON'T: litter the UI with help elements; use help as a crutch for unclear design (fix the design); serve outdated help; bury help behind multiple clicks.
- Named principles: **Just-in-Time Learning** (info at the moment of need is retained), **Recognition over Recall**, **Progressive Disclosure**.

---

## Module 19: Patterns for error prevention and handling

Module scope: form field validation, undo/redo, dialogs, autosave & drafts, error messages & suggestions. Goal: minimize mistakes and give clear recovery paths.

### Form field validation

(Same DO/DON'T core as real-time validation above — the book repeats it deliberately.)
- Validate format/criteria before submission (email format, password rules, file type/size before upload).
- Client-side validation also **reduces server load** — catch bad input before it costs a round trip.
- Show a live password-strength meter rather than a rule dump.
- Progressively disclose detailed rules as the user starts typing in the field.
- Repeat of the two hard rules: validate on blur not per-keystroke; always duplicate validation server-side.

### Undo and redo

- Implement undo for critical or potentially destructive actions (delete, bulk edits, role changes) — it converts fear into willingness to explore.
- Prefer undo over confirm-dialogs for reversible actions (see Dialogs below: don't use dialogs for actions that can be easily undone).
- Make undo/redo visible and accessible right after the action (e.g. "Undo" button in the deletion toast).
- Give clear feedback when an action has been undone/redone.
- Offer multi-level undo for complex operations; don't limit to only the most recent action.
- Use familiar icons/labels (standard undo/redo arrows, Ctrl+Z conventions).
- Don't implement undo for trivial actions; don't make undo the only way to fix mistakes; think through how undo interacts with collaborative/multi-user editing.
- Named principles: **Error Recovery**, **Forgiveness**, **Locus of Control**.

### Dialogs (modal confirmations)

- **Use dialogs sparingly** — reserve them for important or irreversible actions (delete project, leave with unsaved changes). Overuse trains click-through.
- One dialog = one decision. Keep content focused on a single task.
- **Button labels must name the action: "Delete Project", not "OK".**
- Always provide a cancel/back path in every dialog.
- Make dialogs keyboard accessible and easily dismissible (Esc).
- Explain consequences inside the dialog for complex actions ("merging will combine permissions of both clusters").
- **Don't use a dialog for anything easily undone — use undo instead.** Don't cram many options into one dialog.
- Named principles: **Attention Focus** (modal blocking guarantees the message is seen — which is exactly why it must be rare), **Error Prevention**, **Information Scent**.

### Autosave and drafts

- Autosave at regular intervals AND after significant changes.
- Show a **subtle, unobtrusive** save indicator ("Changes saved") — reassurance without noise.
- Still allow manual save; don't take control away from the user.
- Keep prior versions / allow reverting — never silently overwrite.
- Handle conflicts in collaborative editing scenarios explicitly.
- Provide a drafts area where in-progress work is easy to find, resume, and **discard**.
- Make autosave work across devices/sessions (resume anywhere).
- Don't autosave trivial/temporary state that doesn't need preserving.
- Named principles: **Loss Aversion** (protecting work is emotionally high-stakes), **Peace of Mind** (frees working memory), **Continuity**.

### Error messages and suggestions

- Formula for every error message: (1) plain language, (2) what went wrong and why, (3) a specific, actionable next step.
- Use a friendly, non-blaming tone — never blame the user.
- Never show raw error codes without explanation.
- Tailor the message to the context where the error occurred (duplicate name → suggest alternatives; permission denied → explain why and how to request access; unsupported file → list accepted types).
- Use icons/visual cues to signal error type at a glance.
- Don't overload a single error message with too much information.
- Named principles: **Informative Feedback**, **Error Recovery**, errors as **Learning Opportunities** (a good message teaches correct usage, e.g. show correct search syntax with examples).

---

## Module 20: Patterns for accessibility

Module scope: keyboard navigation, ARIA attributes, alt text, color contrast, resizable text & zoom. Framing: accessibility widens the audience AND improves UX for everyone (bright sunlight, cheap screens, temporary injuries, forgotten glasses).

### Keyboard navigation

- Every interactive element must be reachable and operable by keyboard alone.
- **Always show a visible focus indicator. Never remove the default focus outline without providing a replacement.**
- Tab order must follow the visual layout (logical DOM order).
- Provide a "skip to main content" link to bypass repetitive navigation.
- Use standard interactions (Tab to move, Enter to activate) — match users' mental models.
- Offer keyboard shortcuts for frequent actions; surface them in tooltips for discoverability.
- Never create keyboard traps (elements you can't Tab out of).
- Never rely on hover-only interactions — they're unreachable by keyboard.
- Don't assume users can perform complex key combinations.
- Test keyboard navigation across browsers.

### ARIA attributes

- **Rule #1: use native semantic HTML first; reach for ARIA only when HTML can't express it.** (`<button>`, `<nav>`, `<main>` before `role=` hacks.)
- Use `aria-label` for buttons/links whose visible content is ambiguous (icon-only buttons: `<button aria-label="Add new content">+</button>`).
- Use landmarks/roles to define page structure (`<nav role="navigation">`, `<main role="main">`).
- Use `aria-live` to announce dynamic content changes that happen without a page reload.
- Use `aria-current="page"` in navigation to mark the active page.
- Use `aria-invalid` + `aria-describedby` to make form validation errors accessible.
- Use `aria-describedby` to link charts/visualizations to text descriptions.
- Keep ARIA in sync when content changes dynamically — stale ARIA is worse than none.
- Never contradict an element's native semantics with ARIA; never treat ARIA as a substitute for semantic HTML.
- ARIA does not equal accessible — **test with actual screen readers.**

### Alternative text for images

- Provide alt text for all **meaningful** images; keep it concise and descriptive.
- **Use empty `alt=""` for purely decorative images** (so screen readers skip them).
- Never start with "image of"/"picture of" — redundant, screen readers already announce it.
- SEO: include keywords naturally when the image matters for search — but never keyword-stuff.
- Don't repeat text already present in adjacent captions/headings.
- Long/complex images (infographics, charts): short alt summarizing the point + a separate long description, not a paragraph in the alt attribute.
- Alt text also serves slow connections and disabled-image browsing — test by browsing with images off.
- Update alt text whenever you swap the image.

### Color contrast

- **Minimum contrast ratio: 4.5:1 for normal text, 3:1 for large text (WCAG). Treat these as floors — aim higher when possible.** (Book's pass example: 15.98:1; fail example: 1.72:1.)
- Check contrast with tooling during design, not after.
- **Check contrast in every interactive state — hover, focus, active, disabled — not just resting state.**
- Check text over images and gradients explicitly (the classic failure spot).
- **Never rely on color alone to convey information** (pair with icons, labels, patterns).
- Test with color-blindness simulation tools.
- Offer a high-contrast mode for users who need more than the minimums.
- Contrast doubles as a hierarchy tool: give primary actions and key data the highest contrast.
- Build the brand palette so accessible combinations exist for every primary UI element — accessibility and brand aren't in conflict if planned up front.

### Resizable text and zoom

- **Use relative units (rem/em) for font sizes — never fixed px that can't scale.**
- **Layout must survive browser zoom to at least 200%** with no lost content or broken functionality. Test it.
- Never disable browser zoom (e.g. `user-scalable=no`).
- Avoid fixed-size containers that clip or overlap when text grows.
- Provide in-app text-size controls in addition to browser zoom (settings slider / Aa buttons).
- Test resize/zoom on mobile too.
- Persist the user's preferred text size across devices/sessions.
- Named principles: **User Control/autonomy**, **Adaptability** (fluid, responsive layout is what makes 200% zoom survivable).

---

## Module 21 (start): Patterns for personalization

Module scope (continues beyond p.500): customizable dashboards, adaptive content, personalized recommendations, user preferences & settings, localization & language selection.

### Customizable dashboards (pp. 498–500; DO/DON'T list falls after p.500)

- Let users rearrange/hide/resize dashboard widgets so the layout matches THEIR priority order (their mental model, not yours).
- Offer pre-designed templates per role/use case (e.g. "Content Research", "Team Collaboration", "Personal Organization") so customization doesn't start from a blank page.
- Let users hide rarely used features — decluttering is a personalization feature.
- Named principles: **Sense of Ownership** (customization increases investment), **Self-Determination/autonomy**, **Cognitive Load Reduction** (users prune what they don't need).

---

## Top rules from this unit

1. **Contrast floors: 4.5:1 for normal text, 3:1 for large text — and treat them as floors, aiming higher.** Check every state (hover/focus/disabled) and text over images/gradients.
2. **Never convey information by color alone** — pair color with an icon, label, or pattern (applies to validation states, statuses, charts).
3. **Never remove the focus outline without a visible replacement**, and make every interactive element keyboard-reachable with a logical tab order and no keyboard traps.
4. **Semantic HTML first, ARIA second** — use `aria-label` only for ambiguous/icon-only controls, keep ARIA in sync with dynamic content, and verify with a real screen reader.
5. **Use rem/em for font sizes, never disable browser zoom, and test the layout at 200% zoom** with nothing clipped or broken.
6. **Alt text on every meaningful image; `alt=""` on decorative ones; no "image of…" prefix; keywords natural, never stuffed** (accessibility + SEO + slow-connection fallback in one move).
7. **No progress indicator for operations under 1–2 seconds; determinate bar when duration is known; spinner only for unknown waits; never fake progress.**
8. Validate form input **on blur, not per keystroke**; state specifically why input is invalid and how to fix it; **always re-validate server-side**.
9. Don't block form submission on non-critical validation issues, and don't stack multiple simultaneous error messages.
10. Error message formula: **plain language + what went wrong/why + one specific actionable fix**, non-blaming tone, no bare error codes.
11. **Use modal dialogs sparingly — only for important/irreversible actions**; one decision per dialog; action-named buttons ("Delete Project", never "OK"); always a cancel path; Esc/keyboard dismissible.
12. **Prefer undo over confirmation dialogs for reversible actions**; put the Undo control right where the action happened (e.g. in the deletion toast).
13. Autosave at intervals and after significant changes, show a **subtle** "saved" indicator, keep versions revertible, and still allow manual save.
14. Confirm important actions with specific detail (what changed, who's affected, when) positioned near the trigger — and skip confirmations for trivial actions so they retain meaning.
15. Every notification must be relevant, concise, actionable, dismissible, and user-controllable — never interrupt a critical task, never notify about trivia.
16. Put help in context (consistent "?" affordance next to the thing it explains), keep it one-sentence short, and never use help text to excuse a confusing design.
17. Social/sharing features must be optional and unobtrusive — never auto-post, never force account connection, never clutter the UI with social widgets.
18. Badges/seals build trust only when authentic and scarce — misleading or overused badges actively erode it; put security seals where anxiety lives (login, payment).
19. Feedback everywhere: every user action gets a visible system response (validation state, confirmation, progress) — uncertainty is the enemy of trust.
20. Good design prevents the error before messaging handles it: validation, undo, autosave, and constraints upstream; dialogs and error messages are the last line, not the first.
