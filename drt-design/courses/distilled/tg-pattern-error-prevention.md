# Error Prevention & Handling — Patterns (Tommy Geoco, Making UX Decisions)

Source: 03-Patterns / 07-Error prevention and handling (6 PDFs). Distilled for a coding agent building practical, fast, foundation-driven web UI.

## Overview

Error prevention and handling minimize user mistakes and provide clear recovery paths when errors occur. Five patterns, ordered roughly from "prevent" to "recover":

1. **Form field validation** — catch bad input at the source, before submission.
2. **Undo and redo** — reversibility as a safety net; makes exploration safe.
3. **Dialogs** — a confirmation gate reserved for irreversible/critical actions.
4. **Autosave and drafts** — protect work from loss (crashes, closures, disconnects).
5. **Error messages and suggestions** — when errors do happen, explain what/why and give a concrete fix.

Core stance: prefer prevention (validation, autosave) over recovery (dialogs, error messages); prefer reversibility (undo) over confirmation (dialogs). None of these patterns substitutes for a well-designed flow in the first place.

## 1. Form field validation

Check user input in real time or on submission against specific criteria; give immediate feedback.

**Why:** prevents bad data reaching the system; immediate correction beats waiting for a server round-trip; client-side checks reduce server load (validate file type/size BEFORE upload); keeps stored data clean (e.g., enforce tag character limits before accepting).

**Psych principles:** immediate feedback (e.g., password strength meter updating as you type), error prevention (block invalid dates in a date picker), progressive disclosure (reveal detailed rules only once the user starts typing — lowers initial cognitive load).

### Do
- Provide clear, specific feedback about WHY input is invalid — not just "invalid."
- Use visual cues (color AND icons) to mark valid/invalid state.
- Validate after the user finishes entering input (on blur), not while they're mid-typing — avoid premature error messages.
- Offer suggestions or help text that guides the correction (show the expected format).
- Keep validation performant — it runs on every interaction; it must never make typing feel laggy.
- ALWAYS validate server-side too; client-side validation can be bypassed. Client-side is UX, server-side is truth.

### Don't
- Rely on color alone to indicate validation status (accessibility — pair with icon + text).
- Overwhelm users with many simultaneous error messages.
- Block form submission over non-critical validation issues.
- Show errors before the user has had a chance to finish the field.

## 2. Undo and redo

Let users reverse or reinstate recent actions. A safety net that makes experimentation feel safe.

**Why:** encourages trying features (changes are reversible); reduces anxiety around deletes (undo on delete recovers accidents); faster than manually reversing complex operations (bulk actions especially); supports non-linear work (backtrack and compare approaches, e.g., formatting changes).

**Psych principles:** error recovery, locus of control (user feels in charge of the interface), forgiveness (interface tolerates mistakes).

### Do
- Make undo/redo easily accessible and visible (e.g., toast with an Undo button right after the action).
- Give clear feedback when an action has been undone or redone (state what changed: "X has been restored").
- Offer multi-level undo for complex operations — don't stop at one step.
- Use familiar icons/labels for undo/redo (curved arrows, "Undo").
- Prioritize undo for critical or potentially destructive actions (delete, bulk edits, role changes) — that's where it earns its keep.

### Don't
- Limit undo to only the most recent action when history is feasible.
- Make undo the ONLY way to fix mistakes — prevention still comes first.
- Add undo/redo to trivial actions that don't need it (scope discipline; keeps the system simple).
- Ignore collaborative contexts — define what undo means when multiple people edit the same thing.
- Use undo as a substitute for good error-prevention design.

**Design rule of thumb:** delete + undo-toast beats delete + confirm-dialog for common, recoverable actions. Reserve dialogs for what genuinely can't be undone.

## 3. Dialogs (confirmation modals)

Modal windows that block the main interface to demand a decision before an action proceeds. For CRITICAL or IRREVERSIBLE operations only.

**Why:** stops accidental irreversible actions (delete an entire project); adds context before commitment (unsaved-changes prompt with Save / Discard options); guarantees attention for important messages; breaks a complex decision into a single focused choice (confirm + refine a bulk action).

**Psych principles:** attention focus, error prevention, information scent (dialog explains consequences before the user commits — e.g., publish dialog summarizing what will go live and any conflicts).

### Do
- Use dialogs SPARINGLY — only for important or irreversible actions. Frequency kills their power.
- Keep dialog content concise and focused on ONE task or decision.
- Use clear, action-oriented button labels: "Delete Project", not "OK". The button text should state the consequence.
- Always provide a cancel/back path in every dialog.
- Make dialogs keyboard accessible (focus trap, Esc to dismiss) and easy to dismiss.
- For genuinely complex decisions, use progressive disclosure inside the dialog rather than dumping everything at once.
- In an unsaved-changes dialog, state consequences plainly ("You've made changes that haven't been saved") and offer explicit Save / Cancel choices — never silently discard work.

### Don't
- Overuse dialogs for minor or frequent actions — users start clicking through blindly (banner blindness for modals).
- Cram many options or complex information into a single dialog.
- Use a dialog for actions that can be easily undone — use undo instead.
- Ship a dialog with no way to cancel or go back.
- Rely on dialogs to patch a badly designed flow.

## 4. Autosave and drafts

Automatically save user progress at regular intervals or on significant changes; keep in-progress work retrievable as drafts.

**Why:** prevents data loss from crashes/closures/connection drops; reduces anxiety (users focus on the task, not on saving); drafts support working on multiple items and resuming later; enables cross-device continuity (start on desktop, continue on mobile).

**Psych principles:** peace of mind (removes "remember to save" from cognitive load), continuity (surface in-progress drafts on return — e.g., a login notification "you have a draft in progress"), loss aversion (protecting existing work matters more to users than almost anything else).

### Do
- Autosave at regular intervals AND after significant changes (e.g., every few minutes or after a major edit) — event-based + time-based.
- Show clear but UNOBTRUSIVE feedback when autosave happens (subtle "Changes saved" / "Automatically saved at 3:56pm" indicator — not a toast, not a modal).
- Keep manual save available alongside autosave — users want control.
- Keep versions/revert available — never overwrite previous versions without a way back.
- Handle conflicts in collaborative editing scenarios explicitly (two people editing the same draft).
- Provide a drafts area with easy access and organization (list with titles + last-edited timestamps), and an easy way to discard drafts no longer needed.
- Make autosave work across devices and platforms.

### Don't
- Rely on autosave alone with no user control over saving.
- Silently overwrite prior versions with no revert path.
- Autosave trivial or temporary state that doesn't need preserving (noise in version history, wasted writes).
- Force users to keep stale drafts (no delete path).

**Anti-pattern from the course's example:** requiring an explicit Save button click on content that should just persist ("Don't": Edit/Save buttons on an auto-generated summary) vs. quietly autosaving with a timestamp indicator ("Do").

## 5. Error messages and suggestions

When an error happens, the message must do three jobs: say WHAT went wrong, WHY (if known), and HOW to fix it.

**Why:** a message with a suggested fix resolves the issue in-place (duplicate name error → suggest alternative names); explains system limits (unsupported file type → list the accepted types AND why); turns failures into education (failed AI generation → explain likely causes like content length and suggest optimizations; broken workflow → suggest simpler alternatives or link a tutorial).

**Psych principles:** informative feedback (permission denied → explain why and how to request access), error recovery (integration failure → step-by-step troubleshooting in the message itself), learning opportunity (syntax error → show the correct syntax with examples).

### Do
- Use clear, non-technical language. Write for the user, not the log file.
- Explain what went wrong and why, when the cause is known.
- Provide specific, ACTIONABLE suggestions for resolving the error — a next step, not just a diagnosis ("Please check your internet connection and try again", "To fix it, remove the extra link").
- Use a friendly, non-blaming tone.
- Use visual cues (icons, color) to communicate error type at a glance — paired with text, never alone.
- Place the error in context — next to the field/element that caused it, aware of what the user was doing.
- Keep the retry/fix action adjacent to the error (e.g., error state includes a "Re-summarize" button).

### Don't
- Use vague ("Something went wrong") or overly technical messages.
- Blame the user.
- Show raw error codes without explanation.
- Ignore the context in which the error occurred.
- Overwhelm with too much information in a single message — one problem, one fix.

**Silent-failure anti-pattern:** an empty/blank state where output should be ("Do" example replaced a silent empty panel with an explicit error + cause + retry). Never fail silently — absence of feedback is the worst error message.

## Pattern-selection cheat sheet

| Situation | Pattern |
|---|---|
| User is entering data | Inline validation (on blur, specific message, server-side backup) |
| Action is common and recoverable | Do it immediately + undo toast |
| Action is irreversible or high-stakes | Confirmation dialog with consequence-naming button label |
| User is creating content over time | Autosave + drafts + subtle saved-indicator |
| System operation failed | Error message: what + why + actionable fix + retry control in place |
| Leaving with unsaved work | Dialog offering explicit Save / Discard — never silent loss |

## Top rules from this unit

1. Prevent > recover: validation and autosave first; dialogs and error messages are the fallback, not the strategy.
2. Prefer undo over confirmation: for recoverable actions, act immediately and offer an undo toast; reserve modal dialogs for genuinely irreversible operations.
3. Validate on blur, not on keystroke — never show an error before the user finished the field.
4. Every validation error must say WHY the input is invalid and what valid looks like, not just flag it red.
5. Never use color alone for validation or error state — always pair with an icon and text (accessibility).
6. Client-side validation is UX only; always re-validate server-side — client checks can be bypassed.
7. Don't block form submission on non-critical validation issues.
8. Keep validation performant — input feedback must never make typing feel slow.
9. Dialog button labels state the consequence: "Delete Project", never "OK". Every dialog has a cancel path and is keyboard accessible (Esc dismisses).
10. One dialog = one decision. No option-dumps; use progressive disclosure if the decision is complex.
11. Overused dialogs train users to click through them — ration them so they retain force.
12. Offer multi-level undo for complex/bulk operations, with clear feedback naming what was undone.
13. Don't add undo to trivial actions — scope reversibility to critical/destructive ones.
14. Autosave both on a timer and after significant changes; confirm with a subtle inline indicator ("Saved at 3:56pm"), never an interruptive one.
15. Never overwrite prior versions without a revert path; keep manual save available alongside autosave.
16. Give drafts a home: listed, timestamped, resumable across devices, and deletable.
17. Error messages carry three parts: what went wrong, why (if known), how to fix — in plain, non-blaming language.
18. Put the error and its fix where the problem is: message adjacent to the failing field/element, retry button inside the error state.
19. Never fail silently — a blank space where output should be is the worst error message.
20. One error message = one problem + one fix; don't stack simultaneous errors or bury users in detail.
