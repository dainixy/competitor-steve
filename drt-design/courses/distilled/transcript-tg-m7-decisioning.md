# Tommy Geoco — Module 7 "Creating a Decisioning Workflow" — Transcript Delta

**Source:** 8 lesson-video transcripts in `transcripts/tommy-geoco/` (whisper transcripts, no punctuation cleanup).
**Baseline already captured:** the written Module 7 content lives in `tg-book-ch2.md` § "Module 7 — Creating a decisioning workflow" (book pp. 114–129) — NOT in ch3/ch4, which cover later modules (10–17). This file diffs the 8 videos against that ch2 section (plus ch1, where the Pareto/StreamPro material already lives). Only material the spoken lessons add beyond the written page is kept below.

Video → written-lesson mapping:
1. `01-Create_a_decisioning_workflow` — module intro
2. `03-Narrowing_your_decisions` — simplicity curve / critical mass
3. `05-Good_design_decisions_are_relative` — what makes a decision "good"
4. `05-Step_1-_What_does_institutional_knowledge_say` — chain step 1
5. `06-3_pillars_of_warp-speed_decisioning` — course architecture
6. `06-Step_2-_What_are_your_users_familiar_with` — chain step 2
7. `07-Step_3-_What_does_your_research_say` — chain step 3
8. `08-Arriving_at_a_decision` — synthesis / close

---

## 1. Create a decisioning workflow (intro)

- Cites Amazon's leadership principle **"be right a lot, using strong judgment and good instincts"** as external validation that fast, confident judgment is a real institutional competency — not corner-cutting. Use this as a one-line justification when a stakeholder pushes back on moving fast without a research deck for every call.
- Names decisioning explicitly as **"a sport"** — a competency built through practice and accumulating reference points, not innate taste. Implication: the framework in this module should be run *deliberately* early on so it becomes reflexive later (pays off directly in video 8's driving analogy).
- Draws an explicit line between two decision tiers — worth keeping as a filter before applying the 3-step chain at all:
  - **Macro decisions**: "features vs. enhancements," "feature A vs. feature B," "more research vs. start building." These are the ones teams over-index on — circular debate, feels like it needs validation, drags until "the right person in the room feels good about it."
  - **Micro decisions**: the 10–20/hour calls made *while actually designing* (this component or that one, this spacing or that one). This module's framework targets the micro tier — that's where slow decisioning quietly bleeds out a competitive market.
- Rule of thumb stated directly: treat slow micro-decisioning as a **competitiveness problem**, not just a workflow inefficiency — "in a competitive market where speed and accuracy can determine whether you win or lose, slow decisioning can undermine a well-meaning design effort."

## 2. Narrowing your decisions

No material beyond `tg-book-ch2.md` (diminishing returns, critical mass definition, the Cluster critical-mass example are all already captured verbatim in spirit). Skip.

## 3. Good design decisions are relative

This is the one video with a genuinely new mental model — not in the book excerpt at all.

- **Opens with a thought experiment**, useful as a teaching device to run past a non-technical founder: two products, identical features/workflows/interaction patterns, but one looks more custom/polished and the other looks dated and uses a generic UI framework. Which is "better"? Three common answers are each offered and each called *valid but incomplete*:
  1. Aesthetic usability effect → the more appealing one is better (looks-usable ≠ actually well-decisioned).
  2. More psychology/accessibility compliance → that one is better.
  3. "Better" is subjective to the individual user.
- **The actual point of the exercise**: it's entirely possible for a visually/technically well-executed product to be built on *strategically poor design decisions* underneath — and vice versa. Concrete counterfactual given: imagine if StreamPro (the course's running case study) had **not** referenced existing competitors/UI patterns, had chased trivial customer feedback instead of its one primary value driver, and had skipped psychology references — that alone could have sunk an otherwise polished product.
- **Quotable rule, repeated verbatim by the instructor for emphasis**: *"The quality of your design decisions are either undermined or justified by the path you took to arrive at them."* — i.e., grade the process, not the final polish.
- **New 3-part rubric for "what makes a decision good" in warp-speed design** (this is the evaluation-side mirror of the 3-step chain from ch2 — useful as a post-hoc self-check, not just a pre-decision process):
  1. How well it references systems and (institutional) knowledge.
  2. How well it competes in the market.
  3. How well it satisfies users' jobs to be done.
- Target explicitly named as **effectiveness, not perfection** — "effectiveness gets us to perfection, or close to it, over time."

## 4. Step 1 — What does institutional knowledge say

Matches the book's worked example closely (data table too wide → cognitive load + progressive disclosure + no horizontal-scroll pattern in Google/Microsoft/IBM systems). Two small additions:

- Names **two concrete UI mechanisms** as the candidate fix once institutional knowledge flags overload: **expandable rows** or a **"view more" button**. (The book states the *principle* — progressive disclosure — without naming these two specific patterns.)
- Frames the output of this step precisely: institutional knowledge "doesn't automatically grant you the correct answer, but it does point you in the right direction... it helps you avoid reinventing the wheel or making some especially rookie mistakes." Set expectations accordingly — step 1 produces a *direction to explore*, not a final answer.

## 5. Three pillars of warp-speed decisioning

Second video with real new content — this is the course's own architecture map, not stated this way anywhere in ch1/ch2.

- **War story with numbers**: during the Star Wars prequels, George Lucas operated on the philosophy that **"good was good enough,"** often shooting scenes in a single take and moving on. The trilogy grossed **$2.4 billion worldwide** off a **$340 million** production budget. Lesson drawn explicitly: filmmaking and product design are both collaborative and run under compressed/uncertain conditions, but filmmaking ships in **final, irreversible form** — product design has **the luxury of iteration**. A wrong UI-pattern bet usually won't kill your product; treating every micro-decision like a costly one-take film production (i.e. over-deliberating) is what actually costs you. Practical takeaway: bias toward shipping a reversible bet over perfecting an irreversible one.
- Restates the efficient/inefficient decision dichotomy in positive-first framing: **efficient decisions are fast, intentional, and resourceful**; inefficient ones are overthought, uninformed, and usually violate the Pareto principle (the Pareto framing itself is already captured in `tg-book-ch1.md`, so only the fast/intentional/resourceful positive phrasing is new).
- **Names and defines the 3-pillar structure the whole course is organized around** (not spelled out this way in the ch2 text):
  1. **Scaffolding** — the rules you use to automate *recurring* decisions. Your personal library of design patterns, psychological references, best practices (= what Module 5 "information scaffold" built).
  2. **Decisioning** — the process you use for making *new* decisions (= this module, the 3-step chain).
  3. **Crafting** — the checklists you use to *execute* decisions once made (= the Module 9–12 checklists content).
  - Useful for an agent: this tells you which bucket any given rule you've already ingested belongs to — a fixed rule ("use 8px spacing") is Scaffolding; a *process* for resolving a novel/ambiguous UI call is Decisioning; a step-by-step execution list is Crafting. Don't run the full 3-step decisioning chain on something that's already a Scaffolding rule — that's what the scaffold is for.

## 6. Step 2 — What are your users familiar with

- **Names actual products** in the worked example where the book stayed generic: **Notion and Airtable** use nested-row patterns for complex data tables (competitor familiarity signal); **Google Sheets** is heavily used by content creators, meaning they're already comfortable with horizontally-scrolling tables (adjacent-tool familiarity signal); Cluster's **own old editorial feature** already has a working horizontal-scroll pattern — reuse it for speed even though "it's an older UI that is due for a redesign" (pragmatic reuse beats a from-scratch "better" solution when speed matters).
- **Explicit scope clarification not in the book**: this step runs on **intuition and market knowledge**, not precise usage-percentage data. If you actually have hard data on what % of your users know which competitor products, that's Step 3 (research) material, not Step 2 — don't conflate the two.

## 7. Step 3 — What does your research say

- **Permission/reassurance line worth keeping verbatim for a non-technical audience**: *"Even if you don't have a rock-solid research process, any real user data that you can get your hands on is good."* Imperative: don't skip this step just because your research infrastructure is immature — partial real data still outranks steps 1–2.
- Worked example adds one specific behavioral detail beyond the book's compressed version: users don't just compare rows within the table — they **switch browser tabs to compare against Google Analytics and social media platforms**. Generalizable pattern: users often benchmark your interface's data against *other tools*, not just against itself — check for that comparison behavior when doing research on data-heavy screens.
- Otherwise restates ch2's "research overrides both scaffold and familiarity" ranking — no new rule there.

## 8. Arriving at a decision (close)

- **New teaching analogy**: learning to drive. At first you're hyper-aware of every micro-action — checking mirrors, signaling, braking — consciously running through steps. With repetition it becomes muscle memory and you do it fast without thinking. Directly maps onto the 3-step chain to pre-empt the objection *"do I really have to run all 3 steps for every tiny UI choice?"* — answer given: yes, deliberately, at first; then it collapses into instinct through repeated use, and it "won't take long for it to stick."
- Frames the ideal outcome of the chain as **agreement across all three inputs**, not just the highest-ranked source overriding the others: the worked decision (table with collapsible rows) is presented as good specifically because it satisfies institutional knowledge (still progressive disclosure) AND matches competitor/familiar patterns AND supports the research-confirmed comparison task AND is achievable fast by reusing existing UI. Call this out as the "win-win" bar to aim for — the 3-step chain isn't just a tie-breaking hierarchy, the ranking (research > familiarity > scaffold) is only for when the three sources actually *conflict*.

---

## Condensed new rules (imperative, for reuse in an agent-facing ruleset)

1. Split every design call into macro (needs debate/validation) or micro (the 10–20/hour calls made while actively designing) — apply the 3-step decisioning chain only to the micro tier; don't let it slow down decisions that actually need macro-level validation, and don't drag micro calls into macro-style debate.
2. Grade a design decision by the path taken to reach it, not by how polished the output looks — a visually strong product can still rest on strategically poor decisions (skipped competitor/pattern reference, no psychology grounding, chased trivial feedback over the one primary value driver).
3. Evaluate any decision on 3 criteria: how well it references institutional knowledge, how well it matches what the market/competitors do, how well it satisfies the user's job to be done. Aim for effectiveness, not perfection.
4. When institutional knowledge flags cognitive overload on a data-heavy view, default candidate fixes are expandable rows or a "view more" button — start there before inventing something new.
5. Treat UI-pattern decisions as reversible bets, not final productions — product design (unlike film) allows iteration, so don't over-deliberate a single call as if it were a one-shot, unfixable production.
6. Route rule-based/recurring decisions to your scaffold (fixed rules); route novel/ambiguous decisions through the 3-step chain (process); route execution of an already-made decision to a checklist (crafting). Don't run the full chain on something that's already a settled scaffold rule.
7. Step 2 (user familiarity) is an intuition/market-knowledge exercise, not a data exercise — if you have real usage-percentage data, that belongs in step 3 (research), not step 2.
8. Don't skip the research step for lack of research infrastructure — any real user data beats none, and it still outranks scaffold and familiarity when available.
9. On data-heavy screens, check whether users are benchmarking your view against *other tools* (spreadsheets, analytics dashboards, social platforms) via tab-switching — that's a distinct research signal from in-product comparison behavior.
10. The best outcome from the 3-step chain is one where institutional knowledge, familiarity, and research all agree — use the research > familiarity > scaffold ranking only as a tie-breaker when they conflict, not as a default override.
11. Expect to consciously run all 3 steps at first; expect it to become fast/instinctive with repetition — don't abandon the framework because early reps feel slow.
