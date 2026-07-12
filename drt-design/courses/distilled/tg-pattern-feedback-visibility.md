# Feedback & Visibility Patterns — Tommy Geoco, Making UX Decisions (Patterns Unit 06)

Source: 6 short PDFs covering system feedback and its five implementation patterns: progress bars/loaders, notifications/alerts, confirmation messages, real-time validation, contextual help. Distilled for a fast, restrained, foundation-driven web UI (no decorative effects; feedback should be light-weight — mostly text, color, and small icons, not animation).

## 00 — System feedback (overview)

Feedback and visibility tell the user three things: (1) what the system is doing right now, (2) that their action was received and what it resulted in, (3) what to do next. Good feedback reduces uncertainty, prevents errors, and guides users through multi-step processes.

The five patterns and when each applies:

| Pattern | Use when |
|---|---|
| Progress bars / loaders | An operation takes noticeable time (upload, import, AI generation, multi-step setup) |
| Notifications / alerts | The system must proactively tell the user something (event, update, required action) |
| Confirmation messages | Verifying a user action — before it (destructive) or after it (success reassurance) |
| Real-time validation | Checking user input as it is entered, before submission |
| Contextual help | Explaining a control/feature at the exact place and moment it's needed |

Canonical lightweight example: a small dismissible toast ("Your Cluster is saved") — confirms the action, doesn't block, disappears. Default to this weight class of feedback before reaching for modals or persistent banners.

## 01 — Progress bars and loaders

Purpose: make otherwise opaque system operations visible; manage expectations, give a sense of control, prevent users from assuming the app froze and abandoning it.

### Decision rule: which indicator
- **Known duration or known steps → linear/determinate progress bar** (percentage, step counter).
- **Unknown duration → spinner/indeterminate loader.** Never fake a percentage.
- **Multi-step flows (setup, onboarding, wizards) → stepped progress bar** showing steps completed. Exploits the Goal-Gradient Effect: visible progress toward completion increases motivation to finish (why onboarding completion bars work).
- **Background tasks (sync, autosave) → subtle, small indicator** (e.g. thin bar in the header) that lets the user keep working.

### Rules
- Do NOT show a progress indicator for operations under **1–2 seconds** — it adds noise and makes the app feel slower.
- Never use fake or artificially slowed progress indicators.
- Add context when you can compute it: percentage complete, items processed ("412/1000 imported"), estimated time remaining. Percentage + time-remaining together best reduce anxiety on long uploads (Uncertainty Reduction).
- Keep the indicator visible and appropriately sized, but never let it distract from or cover the main content.
- Use familiar visualizations only (bar, spinner, step dots). No novel/clever progress graphics — users shouldn't have to decode the indicator.
- Provide non-visual alternatives for users who can't perceive the visual indicator (e.g., `aria-live` status text / `role="progressbar"` with `aria-valuenow`).
- Animation is allowed here only in service of the indicator itself (moving fill feels alive); keep it minimal — a determinate bar with real numbers beats an elaborate animated loader, and costs nothing in performance.

## 02 — Notifications and alerts

Purpose: proactively inform users about events, updates, or required actions — including when they're not actively in the app.

### Use cases
- Inform: collaborator commented/edited a shared item.
- Prompt timely action: scheduled item is due — review and approve.
- Warn before destructive actions: "Are you sure you want to delete this? …consequences" (alert-as-error-prevention).
- Re-engage: digests, milestone/achievement notices (use sparingly — psychology levers below cut both ways).

Psychology it leans on: Zeigarnik Effect (unfinished-task reminders pull users back), FOMO (activity notices), Operant Conditioning (positive milestone notices reinforce behavior). These are engagement levers — powerful and easy to abuse.

### Rules
- Do NOT overwhelm users with notifications. Prioritize by importance and relevance to *this* user; if everything notifies, nothing does.
- Never notify for trivial information. Every notification must be worth an interruption.
- Keep notification copy clear and concise — event + what to do, nothing else.
- Give users control: notification preferences, per-category opt-out.
- Use distinct styles/urgency levels for different notification types (info vs. warning vs. critical) so severity is readable at a glance.
- Make every notification dismissible; never let one interrupt or block a critical task in progress.
- Respect timing — don't send at inappropriate hours (e.g., middle of the night).
- Follow platform-specific notification guidelines (web push, iOS, Android differ).
- Notifications are not a patch for bad in-app communication — if users need a notification to find a feature or state, fix the interface first.

## 03 — Confirmation messages

Purpose: verify user actions. Two distinct kinds:
1. **Pre-action confirmation (dialog)** — for important/irreversible operations: "Are you sure you want to delete X?" with the consequences stated and Cancel + destructive action buttons.
2. **Post-action confirmation (toast/inline message)** — reassures the action completed: "Your notification preferences have been saved." Best paired with **Undo** where feasible ("Cluster deleted — Undo"), which is often better UX than a pre-action dialog.

### Rules
- Do NOT overuse confirmations. Reserve pre-action dialogs for irreversible or high-consequence actions; trivial/easily-reversible actions get at most a lightweight post-action toast (or nothing). Overuse trains users to click through blindly.
- Prefer Undo over "Are you sure?" for reversible operations (course's own Do-example shows delete + undo toast).
- Use clear, specific language — say exactly what happened or will happen. No technical jargon, no vague "Operation completed."
- Include relevant details: what was changed, who was affected, exact scheduled date/time. Specificity is what reduces uncertainty ("Post scheduled for Feb 11, 2:00 PM" beats "Post scheduled").
- For complex actions (merge, bulk edit), explain the consequences in the confirmation *before* the user commits — what happens to the data and permissions.
- Always provide both confirm and cancel options in pre-action dialogs; give the user real control (Locus of Control).
- Position the confirmation close to the triggering action, not in a far corner of the screen.
- Use one consistent style for confirmations across the whole interface.
- Always give a clear way to dismiss or act on the message.
- Confirmation dialogs are a last line of defense, not the first: design so mistakes are hard to make in the first place (separation of destructive buttons, undo, etc.).

## 04 — Real-time validation

Purpose: check input as it's entered so users fix errors immediately, forms complete more often, and bad data never reaches the system.

### Rules
- **Validate on blur (after the user finishes a field), not on every keystroke** — premature error messages while someone is still typing are hostile.
- Give clear, specific feedback about *why* the input is invalid, plus a suggestion or help text on how to fix it ("Enter a valid phone number: xxx-xxx-xxxx" beats "Invalid input").
- Never rely on color alone to signal valid/invalid — pair color with icons and text (accessibility; colorblind users).
- Use positive confirmation too: green checkmark on correctly completed fields encourages completion of long forms (incremental progress).
- Do NOT stack many simultaneous error messages — show what's relevant, one field at a time as the user moves through.
- Do NOT block submission for non-critical validation issues; only hard requirements should block.
- Plain language only in validation messages — no technical jargon, no regex-speak.
- **Always validate server-side as well** — client-side validation is UX, not security; it can be bypassed.
- Keep validation performant: checks must feel instant or the form feels broken (debounce remote checks; prefer local rules).
- Reveal complex requirements progressively as they become relevant (e.g., password rules appear/check off as the user types) instead of dumping the full rulebook upfront.
- Character-limit fields: validate live against the limit and say the limit in the error.

## 05 — Contextual help

Purpose: put explanations exactly where and when they're needed — beside the control — instead of in external docs. Reduces cognitive load (no remembering/searching), improves feature discoverability, cuts support tickets.

Forms, in escalating weight: tooltip on a help icon → inline helper text → expandable section. Pick the lightest one that fits the content length.

### Rules
- Make help easily discoverable but unobtrusive — a small consistent indicator (e.g., "?" icon) next to the setting, never a layer of clutter.
- Use ONE consistent help indicator across the whole interface so users learn to recognize it (Recognition over Recall).
- Keep help content concise and directly relevant to the current context — one control, one short explanation. Long-form content doesn't belong in a tooltip.
- Help must be reachable in one click/hover — never buried behind multiple clicks.
- Reveal complexity progressively: basic explanation first, deeper detail only as the user digs (e.g., advanced metric definitions appear where the advanced metrics are).
- Let users dismiss or disable contextual help (first-run tooltips especially); respect that preference.
- Do NOT overwhelm the interface with help elements — if a screen needs help icons on everything, the design has failed.
- Contextual help is never a substitute for clear, intuitive design. Fix the label/layout before adding a tooltip explaining it.
- Keep help content correct and current — outdated in-context help is worse than none.
- Good moment for proactive contextual help: a user's *first* encounter with a complex feature (one-time tooltip explaining what it does), or right before a consequential choice (explaining permission levels before sharing, tiers before purchase).

## Top rules from this unit

1. No progress indicator for operations under 1–2 seconds — feedback for instant actions is noise that makes the app feel slower.
2. Match indicator to knowledge: determinate bar when duration/steps are known, plain spinner when unknown; never fake or artificially slow progress.
3. Add real numbers to progress when computable — percentage, items done, time remaining — a truthful determinate bar beats any fancy animated loader.
4. Use stepped progress bars in onboarding/wizards; visible progress toward completion measurably increases finish rates (Goal-Gradient Effect).
5. Give background tasks (sync, autosave) a subtle non-blocking indicator; the user keeps working.
6. Every notification must be worth an interruption: prioritize by relevance, never notify trivia, and let users control preferences per category.
7. Make all notifications dismissible and never let them interrupt a critical task in progress.
8. Encode urgency visually: distinct styles for info / warning / critical so severity reads at a glance.
9. Reserve "Are you sure?" dialogs for irreversible, high-consequence actions only; overusing them trains blind click-through.
10. Prefer post-action toast + Undo over pre-action dialogs for reversible operations.
11. Confirmation copy must be specific: state exactly what changed, who's affected, or the exact scheduled time — vague "Done" messages don't reduce uncertainty.
12. In destructive/complex confirmations, spell out the consequences before the user commits, and always offer Cancel.
13. Validate form fields on blur, not on every keystroke; never scold users mid-typing.
14. Validation errors must say why it's invalid and how to fix it, in plain language — and never signal state by color alone (add icon + text).
15. Don't block submission on non-critical issues; do always re-validate on the server (client validation is UX, not security).
16. Show green checkmarks on completed fields in long forms; incremental positive feedback raises completion.
17. Reveal complex input rules progressively (e.g., live password-requirements checklist) instead of a wall of rules upfront.
18. Put help beside the control it explains, behind one consistent "?" indicator, one click/hover away, in one short sentence — and let users dismiss it.
19. Contextual help and notifications are patches, not foundations: if a screen needs tooltips everywhere or a push to be understood, redesign the screen.
20. Position feedback near the action that triggered it, style it consistently app-wide, and mirror it non-visually (aria-live/status roles) for accessibility.
