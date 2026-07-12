# Tommy Geoco — Making UX Decisions · Patterns Unit 09: Personalization

Source: 6 short PDFs (overview + 5 pattern lessons). Personalization = tailoring the experience to individual users via their preferences, behavior, or characteristics. Two families: **explicit** (user configures: dashboards, settings, language) and **implicit** (system adapts: adaptive content, recommendations). The unit's recurring theme: sensible defaults first, customization second, and never let personalization hide essential functions, hurt performance, or disorient the user.

The five patterns covered:
1. Customizable dashboards
2. Adaptive content
3. Personalized recommendations
4. User preferences and settings
5. Localization and language selection

---

## 1. Customizable dashboards

Let users tailor their primary interface — choose which information and features are prominent and accessible.

**Why it works (use only when these apply):**
- Efficiency — users prioritize the info/tools they use most (drag-and-drop widgets like "Recent Projects," "Team Activity").
- Diverse roles in one interface — ship pre-designed templates per role (e.g., "Content Creator," "Team Manager," "Data Analyst") instead of one-size-fits-all.
- Engagement via ownership — customization increases user investment (Sense of Ownership, Self-Determination Theory / autonomy).
- User-built hierarchy — resizable widgets let users give prominence to what's critical to *them* (matches their mental model).
- Cognitive load reduction — let users hide/minimize rarely used features to declutter.

**Rules:**
- Provide an intuitive drag-and-drop interface for customization; don't overwhelm with too many customization options.
- Offer a mix of pre-designed templates AND full customization — templates are the on-ramp; most users never customize.
- Always provide an easy reset-to-default. If users can break the layout, they need a one-click way back.
- Persist user preferences across sessions AND devices; allow saving multiple named dashboard configurations (per work mode / project).
- Never hide critical features or notifications in the pursuit of customization — all essential functions must remain reachable even if not displayed by default.
- Optimize performance of customized dashboard loading — personalization must not slow first render (per-user layouts tempt heavy client-side hydration; keep them cheap).
- Provide clear instructions or a short tour explaining how to customize.

## 2. Adaptive content

System dynamically adjusts content, layout, or functionality based on user behavior/context — no explicit user configuration required.

**Why it works:**
- Relevance — surface the categories/tools the user actually interacts with most (Relevance Theory: humans focus on contextually relevant info).
- Efficiency — predict needs; prominently display tools/templates related to the user's most common tasks.
- Cognitive Fit — adapt complexity (e.g., help-content tone and depth) to demonstrated user expertise level or role.
- Familiarity — mimic structures the user commonly creates; familiarity increases comfort and speed.
- Serves different segments (creator / editor / analyst) from one interface without manual configuration.

**Rules:**
- Base adaptations on clear, consistent behavior patterns — never on a single interaction or unreliable data.
- Keep adaptive changes SUBTLE. Drastic layout changes confuse and disorient; never move things dramatically between sessions.
- Never remove access to features or content through adaptation — adaptation may reorder/emphasize, never delete.
- Be transparent about why content or layout is changing (e.g., "Based on your interest in X").
- Let users easily override or turn off adaptive features.
- Respect privacy when collecting behavioral data for adaptation.
- Don't assume one adaptive ruleset fits all users; review and update the rules regularly against real behavior.

## 3. Personalized recommendations

Proactively suggest content, features, or actions based on behavior, stated preferences, or characteristics.

**Why it works:**
- Discovery — users find relevant things they'd never search for (suggest related items from current context/tags).
- Engagement — recommend unused features matched to the user's role and usage patterns.
- Decision support — suggest sensible defaults/settings in complex choices based on past preferences.
- Connection — recommend collaborators/experts based on shared topics.
- Psychology levers: Curiosity Gap (tease with intriguing titles/snippets), Social Proof ("Trending in Your Network"), Endowment Effect ("Handpicked for You Based on Your Expertise").

**Rules:**
- Blend three signals: user behavior + stated preferences + current context. Never rely on past behavior alone — it kills discovery of new interests.
- Don't overwhelm — few recommendations at once beat a wall of them.
- Always explain WHY an item is recommended ("Because you worked on X").
- Make recommendations easy to dismiss or refine; provide an opt-out from personalized recommendations entirely.
- Keep recommendations diverse to avoid echo chambers.
- Avoid recommendations that feel invasive or presumptuous (creepy specificity destroys trust).
- Respect context — the same recommendation can be welcome in one moment and intrusive in another.
- Continuously improve the recommendation logic from user interactions (dismissals are data).

## 4. User preferences and settings

Explicit, direct user control over interface, functionality, and behavior.

**Why it works:**
- Control = satisfaction (Locus of Control: control over environment reduces stress — e.g., notification frequency/type controls).
- Accommodates diverse needs — text size, color scheme, contrast options serve accessibility.
- Productivity — custom keyboard shortcuts, preferred default views (list / card / timeline).
- Privacy/security — granular controls for sharing, access, profile visibility.
- Letting users hide/simplify complex features they don't need reduces visual clutter and cognitive load.

**Rules:**
- Offer sensible defaults; customization is opt-in, never required to make the product usable.
- Organize settings logically with clear labels AND one-line descriptions per setting.
- Don't overwhelm with too many granular settings — every toggle is a decision you failed to make.
- Never bury critical settings deep in menus; make settings discoverable without cluttering the main interface.
- Provide live previews of setting changes where possible (theme, text size) so users see effect before committing.
- Sync settings across devices for a consistent experience.
- Always allow easy reset to defaults.
- Don't drastically change core functionality via a setting without the user clearly understanding what will happen.
- The settings interface itself must be accessible (contrast, keyboard, labels) — accessibility settings behind an inaccessible UI is a classic failure.

## 5. Localization and language selection

Adapt language, date formats, numbers, units, currency, and cultural references to user preference or locale.

**Rules:**
- Offer language selection prominently — in user settings AND during initial setup.
- Never lock language to IP/geolocation; location is not preference (traveler, expat, shared machine). Let the user choose independently of location or device settings.
- Use standard language+region codes (en-US, fr-FR) — language alone is ambiguous.
- Localize more than words: date formats, number formats, units of measurement, currency displays.
- Never assume text length is constant across languages — design layouts that tolerate expansion (German/Finnish run long, CJK short); this is a layout-breaking bug class.
- Support right-to-left (RTL) languages (Arabic, Hebrew) as a design consideration from the start, not a retrofit.
- Don't ship raw machine translation without human review.
- Consider cultural differences in design elements — icons, color meanings, metaphors — not just text.
- Use a translation management system so all languages stay in sync as copy changes.
- Provide a channel to report translation issues or contribute translations.
- Localize help docs and tooltips too, not just the chrome (Cognitive Fluency: native-language info processes with lower cognitive load).

---

## Cross-pattern principles (named in the unit)

- **Sense of Ownership / Endowment Effect** — things users shape or that feel "theirs" are valued more.
- **Self-Determination Theory** — autonomy (choice) increases intrinsic motivation.
- **Locus of Control** — perceived control reduces stress and increases satisfaction.
- **Cognitive Load Theory** — personalization's core payoff is *removing* irrelevant stuff, not adding options.
- **Relevance Theory / Cognitive Fit / Familiarity Principle** — match content complexity and structure to the user's context and mental model.
- **Curiosity Gap / Social Proof** — engagement levers for recommendations; use sparingly and honestly.
- **Cognitive Fluency / Cultural Congruence / Linguistic Relativity** — native language + culturally congruent design = easier processing and more trust.

## Top rules from this unit

1. Ship sensible defaults first; personalization is always opt-in and never required to use the product.
2. Never hide or remove essential features/notifications through customization or adaptation — reorder and emphasize, don't delete.
3. Always provide one-click reset to defaults anywhere the user can change layout or settings.
4. Persist and sync personalization (settings, layouts) across sessions and devices.
5. Keep adaptive/implicit changes subtle — never dramatically rearrange the interface between visits; disorientation costs more than relevance gains.
6. Base implicit adaptation on consistent behavior patterns, never a single interaction.
7. Be transparent: tell users why content changed or why something is recommended, and let them override, dismiss, or opt out.
8. Blend behavior + stated preferences + context for recommendations; behavior-only kills discovery and creates echo chambers — keep suggestions diverse.
9. Show few recommendations at a time with a stated reason; make each dismissible.
10. Offer templates/presets (per role or use case) as the primary path; full customization as the secondary path for power users.
11. Limit the number of settings; every setting needs a clear label and one-line description, organized logically — no burying critical settings.
12. Provide live previews for visual settings (theme, text size) before the user commits.
13. Personalized dashboards must stay fast — optimize loading of per-user layouts; personalization is never an excuse for slow first render.
14. The settings UI itself must be accessible; include text size / contrast / color-scheme options as accommodation, not decoration.
15. Let users pick language explicitly in setup and settings; never force language from IP or device locale.
16. Use language+region codes (en-US, fr-FR); localize dates, numbers, units, and currency — not just strings.
17. Design layouts that survive text-length changes across languages, and plan RTL support from the start.
18. Never ship unreviewed machine translation; localize tooltips and help content, not just UI chrome.
19. Respect privacy in all behavioral personalization; avoid creepy over-specific suggestions.
20. Provide clear onboarding (short tour or instructions) wherever users can customize.
