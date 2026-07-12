# Tommy Geoco — Making UX Decisions
## Patterns Unit 10: Onboarding & Learning

Source: 6 PDFs from `03-Patterns/10-Onboarding and learning`. Five onboarding/learning patterns, each with use cases, the psychological principle it exploits, and do/don't implementation rules. Course examples use a fictional app "Cluster" (content-organization SaaS); examples generalized here.

**Unit-wide theme:** onboarding drives adoption, engagement, and retention — but every pattern comes with the same warning: guidance is never a substitute for intuitive design, it must be skippable, and it must stay in sync with the actual UI. If the interface needs heavy explanation, fix the interface first.

---

## 1. Product tours & walkthroughs

**What:** Guided, step-by-step introduction to the interface and key features on first use (spotlight/coach-mark style popovers pointing at real UI elements).

**Use when:** the app is feature-rich enough that a new user can't infer the layout, or a differentiating feature would otherwise go unnoticed.

**Psychology it exploits:**
- **Cognitive load reduction** — introduce ONE main feature per step; chunk the interface instead of dumping it all at once.
- **Curiosity** — tease advanced features briefly to invite later exploration; don't teach them in the tour.
- **Self-efficacy** — include a "quick win" early (user completes one real, small action) so they feel immediate accomplishment.

**DO:**
- Keep the tour concise and focused on key features only.
- Allow skip/exit at ANY point — every step needs a visible dismiss.
- Use visual cues (element highlight, arrow, spotlight) anchored to the specific UI element being explained.
- Give the *why* for each feature (value/benefit), not just the *what*.
- Offer replay: let users re-run the tour or jump to a specific part later.
- Structure: welcome → orient to main layout areas → one flagship differentiator → close with a summary of what the user can now accomplish.

**DON'T:**
- Force completion before the app is usable.
- Cram multiple concepts into one step.
- Use technical jargon in tour copy.
- Assume every user needs the same guidance depth (returning/expert users should be able to bail instantly).
- Let the tour drift out of date when the UI changes — a tour pointing at moved elements is worse than no tour.

---

## 2. Contextual tips & hints

**What:** Small, targeted, just-in-time messages attached to a specific element, shown at the moment of interaction (hover hint, inline tip next to a field, "Did you know?" callout).

**Use when:** guidance is needed at a specific point of action — a field with non-obvious conventions, a powerful-but-hidden feature, a best practice worth reinforcing (e.g. suggest role-based access next to permission settings).

**Psychology it exploits:**
- **Just-in-time learning** — information delivered exactly at the moment of need is retained and applied; a tip next to the tagging field beats a tagging chapter in the docs.
- **Progressive disclosure** — reveal advanced-feature tips only after the user has demonstrated mastery of basics; sequence tips by engagement, not calendar.
- **Curiosity** — "Did you know?" framing for lesser-known valuable features.

**DO:**
- Keep each tip concise and directly relevant to what the user is doing *right now*.
- Use clear, action-oriented language ("Try `tag:` to filter by tag"), not passive description.
- Always provide dismiss/hide; remember the dismissal — never re-show a dismissed tip.
- Make tips noticeable but visually quiet — a subtle cue, not a modal.
- Test timing and frequency with real usage; a mistimed tip reads as an interruption, not help.

**DON'T:**
- Show many tips at once — one at a time, ever.
- Use tips to paper over bad design. If an element needs a tip to be understood, first ask whether the element should be redesigned.
- Interrupt an in-progress task with an intrusive hint.
- Let tips describe stale behavior after features change.

---

## 3. Interactive tutorials

**What:** Hands-on "learning by doing" — the user actually performs the task (creates the item, adds the content, invites the teammate) with guidance at each step, vs. passively watching a tour.

**Use when:** the skill is procedural (multi-step task) and retention matters; or when users need a safe sandbox to try consequential features without touching real data.

**Psychology it exploits:**
- **Learning by doing** — active performance beats passive demonstration for retention. Have the user create/tag/generate, don't show a video of it.
- **Immediate feedback** — confirm every correct action instantly (success message + why it matters); correct mistakes on the spot.
- **Scaffolding** — order steps so each builds on the previous skill: basics first, then advanced features that reuse them. End with a "graduation" task that combines several learned skills.

**DO:**
- Break tutorials into small, manageable steps — one action per step.
- Give clear instructions AND feedback at every stage.
- Allow pause, resume, and restart at any time.
- Use real-world scenarios/sample data so the practice maps to actual use.
- Keep tutorials accessible later as refreshers.
- Provide a sandbox for destructive or complex features so experimentation can't damage real data.

**DON'T:**
- Make tutorials long or complex.
- Gate app access behind tutorial completion.
- Use a tutorial to compensate for unintuitive design.
- Let tutorials rot when the UI changes.
- Force one guidance depth on all users.

---

## 4. Onboarding checklists

**What:** A visible, persistent list of setup/getting-started tasks with progress indication ("Create your first X", "Add content", "Invite a teammate"), usually in a dismissible panel.

**Use when:** getting to value requires several independent setup actions and you want users to reach early success without a forced linear flow.

**Psychology it exploits:**
- **Goal-gradient effect** — motivation rises as completion nears; show percentage/progress bar and emphasize how close the user is.
- **Endowed progress effect** — pre-check items the user has already done ("Create account", "Set up profile") so the list starts partially complete; a head start increases completion of the rest.
- **Gamification (light)** — completion feedback/milestone celebration makes progress rewarding. Keep it restrained; the reward is the working product.

**Concrete numbers from the source:** group the checklist into 2–3 sections, each with **2–3 tasks** — i.e. roughly 4–9 items total, never a long list.

**DO:**
- Keep items clear, concise, and actionable — each item is a single verb-first task.
- Give immediate feedback (check-off animation/confirmation) when an item completes.
- Allow any-order completion when tasks aren't dependent.
- Attach guidance/help to each item so the user can actually do it from the checklist.
- Offer skip/dismiss for the whole checklist.
- Make it prominent but not intrusive (persistent card/panel, not a blocking modal).
- **Auto-retire it:** stop showing the checklist once the user is clearly active — a checklist nagging an established user is noise.

**DON'T:**
- Overwhelm with too many items.
- Include complex or time-consuming tasks in initial onboarding — save those for later surfaces.
- Force full completion before app use.

---

## 5. Help centers & documentation

**What:** Centralized, searchable knowledge base: getting-started guides, feature documentation, FAQ, troubleshooting. Serves new AND experienced users; reduces support load via self-service.

**Psychology it exploits:**
- **Competence (Self-Determination Theory)** — docs let motivated users master the product themselves; include an advanced/"mastery" section for power users.
- **Recognition over recall** — clear categories, tags, and browsable structure let users *recognize* their problem rather than recall exact terminology.
- **Multiple formats** — text steps, screenshots/visuals, and video for the same key tasks; different users learn differently.

**DO:**
- Organize logically: clear top-level categories with subcategories; article counts visible per category.
- Lead with a prominent search box ("How can we help?") — search is the primary path, browse is the fallback.
- Surface common/popular topics directly on the help landing page.
- Use plain language; avoid jargon; keep structure shallow (don't bury key info levels deep).
- Keep docs updated in lockstep with feature changes — stale docs destroy trust.
- **Bring help to the user:** embed context-sensitive help links inside the app at relevant screens ("Learn more" next to the setting); never assume users will proactively visit the help center.
- Collect feedback on article helpfulness ("Was this helpful?") and iterate.

**DON'T:**
- Skip basic "Getting Started" content because it seems obvious.
- Rely on text alone — add visuals/video where they clarify.
- Hide the help center; promote it inside the product.

---

## Cross-pattern decision guide

Pick the pattern by the *shape* of the learning need:

| Need | Pattern |
|---|---|
| Orient a brand-new user to layout + flagship feature | Product tour (short, skippable) |
| Explain one element at the moment of use | Contextual tip |
| Teach a multi-step procedural skill | Interactive tutorial (do, don't show) |
| Drive completion of several independent setup tasks | Onboarding checklist (4–9 items, pre-checked head start) |
| Ongoing reference, troubleshooting, advanced depth | Help center + in-app context links |

Rules that repeat across ALL five patterns (treat as law):
1. Never gate the product behind guidance — everything skippable, dismissible, exitable.
2. Guidance is not a bandage for bad design — if it needs explaining, consider redesigning first.
3. Keep every unit of guidance small: one concept per step, one tip at a time, one action per tutorial step.
4. Guidance must be versioned with the UI — update or remove it when features change.
5. Don't assume uniform users — experts must be able to opt out instantly; novices must be able to replay.

---

## Top rules from this unit

1. Never force users through a tour, tutorial, or checklist before they can use the app — every guidance surface needs a visible skip/exit/dismiss.
2. Guidance is not a substitute for intuitive design; if an element needs a tip or tour step to be understood, redesign the element before writing the tip.
3. One concept per step: tours introduce one feature at a time, tips appear one at a time, tutorial steps demand one action each.
4. Include a "quick win" early in any first-run flow — one small real accomplishment builds self-efficacy faster than any explanation.
5. Explain *why* a feature matters (its value), not just what it does; write all guidance copy in plain, action-oriented language with zero jargon.
6. Anchor guidance visually: highlights/arrows on the exact element, noticeable but not intrusive — never a blocking modal for a hint.
7. Remember dismissals — never re-show a tip the user has already dismissed.
8. Sequence by mastery (progressive disclosure): show advanced-feature tips only after the user demonstrates the basics, not on a timer.
9. Prefer doing over showing: for procedural skills, have the user perform the real actions with instant feedback rather than watch a walkthrough.
10. Scaffold tutorials — basics first, each step building on the last, ending with a graduation task that combines the learned skills; keep sandboxes for risky features.
11. Keep onboarding checklists to ~4–9 verb-first items (2–3 sections × 2–3 tasks); allow any-order completion.
12. Exploit endowed progress: pre-check items already done (account created, profile set) so the checklist starts partially complete.
13. Show progress explicitly (bar/percentage) — goal-gradient motivation rises near completion.
14. Auto-retire onboarding UI once the user is active; a checklist or tour prompt haunting an established user is clutter.
15. Version all guidance with the UI: update or delete tours, tips, tutorials, and docs the moment the interface changes — stale guidance is worse than none.
16. In help centers, lead with search and shallow, clearly-categorized structure; support recognition over recall.
17. Provide the same key task in multiple formats (text steps + visuals/video) for different learners.
18. Bring help into the app: context-sensitive "learn more" links at the relevant screen; never assume users will visit the help center on their own.
19. Always include basic "Getting Started" docs, however obvious they seem, and gather "was this helpful?" feedback to iterate.
20. Make replay/refresher access permanent — users must be able to re-run a tour or tutorial and re-find any tip's information later.
