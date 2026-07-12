# Tommy Geoco — Making UX Decisions · Checklists · Unit 04: Innovating (The Originality Spectrum)

Source: 6 checklist PDFs on how original a design solution should be. Core model: **the 5-level originality spectrum** — Direct copies → Remixes → Indirect parallels → Metaphors & analogies → True innovation. Each level trades familiarity/speed against novelty/risk. The unit's central bias: **originality is a tool, not a goal — solve the problem with the least novelty that works.**

## The 5 levels of the originality spectrum (overview)

The spectrum, from least to most original:

1. **Direct copies** — replicate an existing pattern with little/no modification.
2. **Remixes** — combine elements from multiple proven designs into one solution.
3. **Indirect parallels** — borrow a solution from an unrelated domain and adapt it.
4. **Metaphors & analogies** — structure the UI around a familiar real-world concept.
5. **True innovation** — invent something with no precedent.

**When to consult this model:** starting a new project and choosing an approach; stuck and needing inspiration; evaluating how novel a current design is; balancing originality against usability and efficiency (especially under time constraints).

### Rules of thumb (innovating vs. reproducing)
- Aim for originality, but learn from the past — look at existing solutions and improve on them rather than starting blank.
- Embrace the remix: adapt ideas from outside your domain (e.g., OS file management informing a content-clustering UI).
- **Don't get hung up on being 100% original — focus on solving problems.** If a standard dropdown works best, use it; never invent a new interaction just for originality's sake.
- The goal is effective solutions, not reinventing the wheel every time.

**Prerequisites before choosing a level:** a clear statement of the design problem and constraints; familiarity with existing solutions in the domain; basic knowledge of standard design patterns.

## Level 1 — Direct copies

Replicating existing concepts/designs with little or no modification. Least original, but valuable for learning, rapid prototyping, and standardized interface elements.

### Decision criteria — when to copy directly
- Copy the **standard, non-differentiating features** users expect to work in familiar ways: login forms, settings pages, basic navigation menus, file upload UIs, list views.
- Do NOT rely on copies for **core, differentiating features** — those must be uniquely designed.
- Verify legal right to use what you copy; avoid unique/trademarked/patented features and interaction patterns (consult legal before copying a distinctive system).
- Check the copied element supports, not detracts from, your unique value proposition — a standard profile layout shouldn't overshadow your differentiator.
- Treat copies as a starting point: plan how you'll iterate/customize the copy later.

### Do
- Use direct copies for rapid prototyping and early-stage development (mock a dashboard with a standard layout to get feedback fast).
- Use standard icons/layouts for common actions (gear = settings) to leverage users' existing mental models — familiarity and learnability are the payoff.
- Test copied designs with YOUR users and use cases — standard ≠ automatically fits your context.
- Use the copy as a **benchmark**: ship the standard baseline, then measure whether your enhanced version actually improves on it.
- Credit inspirations where appropriate (team docs, learning contexts).
- Be ready to justify copies to stakeholders: "standard here frees resources for the unique features."

### Don't
- Don't copy patented/unique interaction patterns from competitors.
- Don't make the whole product a copy — differentiators need original design.

## Level 2 — Remixes

Combining elements from multiple existing designs into one new solution. More originality than copying while still leveraging proven ideas.

### Decision criteria
- Pick elements to remix based on **proven effectiveness and relevance to your specific problem** (e.g., Google Docs real-time editing + GitHub threaded comments).
- Before committing, verify the combination offers genuine benefit over either concept alone — if not, use the simpler single pattern.
- Assess implementation feasibility and user reaction to the hybrid before building.

### Do
- Integrate cohesively: transitions between combined views must feel seamless and intuitive, not stitched.
- Maintain consistent visual styles and interaction patterns across the combined elements (e.g., card layout + list view must share one visual system).
- Check the remix fits the REST of the interface — it must still work with existing search/filter/navigation.
- Test the remix for usability issues; hybrids confuse users in ways single patterns don't.
- Iterate on user feedback (e.g., if a sidebar+topbar hybrid nav confuses people, refine or drop it).
- Document why you combined specific elements, for stakeholders.

### Don't
- **Don't force incompatible elements together just for the sake of remixing** — e.g., don't bolt a data-heavy dashboard onto a minimalist writing surface when they serve different needs.
- Don't remix proprietary/patented designs without checking licensing.

## Level 3 — Indirect parallels

Borrowing a solution from an unrelated domain and adapting it (library cataloging → content organization; music "playlists" → content grouping).

### Procedure
1. Find analogous problems in other domains — match on process, user needs, or desired outcomes, not surface look.
2. Analyze what modifications the borrowed concept needs to work in your field.
3. Weigh innovative potential against the learning curve it introduces (a map-based navigation borrowed from GPS apps may be clever or just confusing).
4. Plan how you'll communicate the parallel so it feels natural in the new context.

### Do
- Cast a wide net: project-management tools, social platforms, games, nature, urban planning — anything with structurally similar problems.
- **Extract the underlying principle, not the surface UI** — from a dating app's matching, take "intelligent recommendation," not the swipe cards.
- Use parallels to challenge assumptions (must this be hierarchical? how do non-hierarchical systems organize things?).
- Test the adapted concept with real users to confirm it translates.
- Budget onboarding/education if the parallel raises the learning curve.
- Be able to explain/justify the parallel to stakeholders in one short pitch.

### Don't
- **Don't force a parallel that doesn't fit real user needs** — e.g., no game-like achievement system in a professional tool if it doesn't serve the job.
- Don't ignore cultural translation — a sports metaphor may not travel across markets.

## Level 4 — Metaphors and analogies

Structuring the product around a familiar concept from another domain to make abstract functionality understandable ("library" with shelves and books; "garden" where creating = planting, curating = pruning).

### Selection criteria
- Choose metaphors the target audience already understands and relates to.
- Verify the metaphor **maps accurately** to actual features and interactions — every major feature should have a sensible counterpart in the metaphor.
- Check scalability: can the metaphor absorb future features without breaking?
- Check cultural portability: a "baseball diamond" stage metaphor fails outside baseball countries.

### Do
- Use metaphors to simplify genuinely complex concepts (AI analysis presented as a "smart assistant").
- Align visual design and interactions with the chosen metaphor so it's coherent, not just a label.
- Use the metaphor **consistently** across UI, feature names, icons, and documentation.
- Multiple complementary metaphors are fine for different product areas ("canvas" editor + "gallery" showcase) — as long as each is internally consistent.
- Test that the metaphor actually improves comprehension; be ready to swap it if users find it confusing.

### Don't
- **Don't overextend a metaphor past its useful limit** — "file cabinet" works for basic organization, not for real-time collaboration; drop the metaphor where it stops mapping.
- **Don't let the metaphor overshadow real functionality** or overpromise ("magic wand" framing that implies capabilities the product lacks).

## Level 5 — True innovation

Creating concepts with no precedent. Rare, expensive, high-failure-rate — reserve it for problems existing solutions genuinely can't address.

### Decision criteria — when innovation is justified
- Only where existing solutions are **inadequate or non-existent** — an unaddressed pain point, not a solved one.
- Challenge fundamental assumptions explicitly (e.g., "content must be hierarchical") rather than tweaking within them.
- Envision the ideal outcome unconstrained first, then work backwards to what's achievable.
- Watch emerging tech that makes previously impossible ideas feasible.

### Do
- Plan for multiple iterations and failures — extensive prototyping/testing, most versions won't work.
- Collaborate across disciplines (engineers + designers + domain specialists) for fresh angles.
- Use empathy research to surface deep, unarticulated user needs as the seed for innovation.
- **Balance innovation with usability and learnability** — a revolutionary interface users can't adopt without training is a failure.
- Think through long-term scalability of the new concept.
- Protect genuinely novel work (IP/patents) where warranted.

### Don't
- **Don't innovate for innovation's sake.** If a simpler solution meets user needs more effectively (e.g., plain lists vs. a complex 3D visualization), ship the simpler one. This is the unit's strongest restraint rule.

## How this maps to fast, foundation-driven web design

(Implications for our use case — standard patterns are also the performance-cheap patterns.)

- Levels 1–2 (copy/remix proven patterns) are the default for 90% of web UI: they're familiar, learnable, testable — and implementable with plain HTML/CSS, no heavy JS, no novel animation frameworks. Novelty almost always costs bytes and interaction latency.
- The unit's repeated pattern: every step up the spectrum adds a **learning curve** and a **testing burden**. Reserve those costs for the one thing that differentiates the product; everything else should be the boring standard.
- "Don't innovate for innovation's sake" and "don't force incompatible elements" are the same discipline as avoiding decorative effects: novelty must earn its place by solving a real user problem.

## Top rules from this unit

1. Don't get hung up on being 100% original — focus on solving the problem; use a standard pattern whenever it works best.
2. Match the originality level to the feature: copy the standard for non-differentiating UI (login, settings, nav, upload); reserve original design for the product's actual differentiator.
3. Never invent a new interaction just for the sake of originality — familiarity and learnability are features.
4. Use standard icons, layouts, and patterns for common actions to leverage users' existing mental models.
5. Use direct copies for rapid prototyping; ship the standard baseline first, then measure whether your "improved" version actually beats it.
6. Test even copied/standard designs with your specific users — standard doesn't guarantee fit.
7. Remix only when the combination is genuinely better than either source pattern alone; otherwise use the simpler single pattern.
8. When remixing, keep one consistent visual system and interaction language across the combined elements, and verify the hybrid still fits the rest of the interface.
9. Don't force incompatible elements together — patterns that serve different user needs don't belong fused in one view.
10. When borrowing from other domains, extract the underlying principle, not the surface UI.
11. Use cross-domain parallels to challenge assumptions ("must this be hierarchical?"), then validate the adapted concept with real users.
12. Every step up the originality spectrum raises the learning curve — budget onboarding for novel concepts or don't ship them.
13. Choose metaphors your audience already knows, verify they map accurately to real features, and apply them consistently across UI, naming, and docs.
14. Stop a metaphor at its useful limit — drop it where it no longer maps, and never let it overpromise what the product does.
15. Check cultural portability of any metaphor or parallel before adopting it.
16. Attempt true innovation only where existing solutions are inadequate or absent — not where a solved pattern exists.
17. Don't innovate for innovation's sake: if a simpler solution meets user needs more effectively, ship the simpler one.
18. Balance any innovation against usability and learnability — an interface requiring training has failed.
19. Never copy unique, trademarked, or patented features/interactions; standard commodity patterns are the safe copy zone.
20. Be able to justify your originality-level choice to stakeholders in one sentence ("standard here frees resources for the differentiator").
