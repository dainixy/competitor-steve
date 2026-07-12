# The UX Playbook — Unified Reference

Merged from two professional courses:
- **[TG]** = Tommy Geoco, *Making UX Decisions* (603-page book + Modules 4–8 video transcripts). A decisioning framework: how to make fast, defensible UI decisions and a catalog of reusable patterns.
- **[NL]** = Nguyen Le, *Process Masterclass* (Modules 1–2 + video transcripts). A process + craft masterclass: design thinking upstream, execution craft (grids, type, spacing) downstream.
- **[both]** = both courses assert it.

Organized by topic, not by course. Imperative voice. Every concrete number preserved. Where the courses conflict, both positions are stated with attribution. Freelancing/pricing/client-management content excluded.

---

## 1. Design Process & Decision-Making

**The three circles every decision must sit inside [NL].** Users (motivation, goals, pain points) × Business (metrics, objectives, stakeholders) × Design (the craft that services the other two). Design is never decoration first — it is the delivery mechanism for user needs and business outcomes. If a choice serves only aesthetics, cut or rethink it.

**Work the layers in order: Outcome → Structure → Interaction → Visual [NL].** Never start at the visual layer. Color, grids, and typography come last, after the outcome and the system are settled. Structure/interaction/visual influence each other and can iterate concurrently — have the courage to change your mind. The straight-line process diagram is a lie; plan for loops.

**TG's parallel sequence for a new interface [TG]:** Define the system → Model user tasks → Organize information (IA) → Gather inspiration → Generate rapid ideas → Enhance fidelity. Same principle as NL: never begin with visual polish. **The order of decisions determines the outcome** — give two designers identical resources and ideas and they land in radically different places; most bad "design process" is a bad decision *order*, not bad ideas [TG].

**The tap-on-the-shoulder test [NL].** For any page, section, or component, you must be able to answer instantly, in business terms, "what were you trying to achieve with this?" Nobody senior cares that a button is red if the design delivered happy customers and more sales — argue at that level, not the pixel level.

**Grade the process, not the polish [TG].** "The quality of your design decisions are either undermined or justified by the path you took to arrive at them." A visually flawless product can rest on strategically poor decisions (ignored competitors, chased trivial feedback over the one primary value driver, skipped psychology). The *aesthetic-usability effect* — "the prettier one must be better designed" — is the tempting wrong answer; name it when a stakeholder picks a design purely on looks.

**Aim for effectiveness, not perfection [TG].** "Effectiveness gets us to perfection, or close to it, over time." Ship a reversible bet over perfecting an irreversible one — product design, unlike film, has the luxury of iteration; a wrong UI-pattern bet rarely kills a product, but an expensive *process* for reaching it compounds the damage.

**Pareto for design: ~80% of business impact comes from ~20% of design decisions [TG].** Identify the 20% and stop agonizing over the rest. You make 10–20 UI micro-decisions per hour; slow decisioning is a competitiveness problem, not just an inefficiency.

### The decisioning chain — weigh information in this order [TG]
When resolving any contested UI micro-decision, ask three questions; each later source outranks the earlier ones *when it exists*:
1. **What does institutional knowledge say?** (the scaffold — psychology, mature design systems, usability heuristics, accessibility). Always the first check; the fallback when nothing else exists. Produces a *direction*, not a final answer. Candidate fixes for cognitive overload on a data view: expandable rows or a "view more" button.
2. **What are users familiar with?** (Jakob's Law — users expect your product to work like the products they already use). Weigh familiarity *above most of the scaffold* — it is the best risk-reducer absent hard data. This step runs on intuition/market knowledge, not usage percentages.
3. **What does our research say?** (interviews, surveys, instrumentation). **Research is the source of truth** and overrides both. "Even if you don't have a rock-solid research process, any real user data you can get is good" — don't skip it for immature infrastructure.

The ranking (research > familiarity > scaffold) is a **tie-breaker for when the three conflict**, not a default override. The best outcome is when all three agree. Known cases where breaking institutional knowledge wins: redesigning a product users already know (Snapchat's redesign cost −2% DAU and −$1.3B valuation), regulated/legacy industries, users with entrenched workarounds. Run all three steps deliberately at first; it collapses into instinct with reps (the "learning to drive" analogy).

### Three buckets — route each decision correctly [TG]
- **Scaffolding** = fixed rules that automate *recurring* decisions (e.g. "8px spacing"). Don't run the full chain on these.
- **Decisioning** = the 3-step chain, for *novel/ambiguous* calls.
- **Crafting** = step-by-step checklists for *executing* a decision already made.

Also split every call into **macro** (features vs. enhancements, more-research vs. build — needs genuine debate/validation) vs. **micro** (the 10–20/hour calls made while designing). Apply the chain to the micro tier; don't drag micro calls into macro-style debate, and don't let the chain slow calls that truly need validation.

### Pace: warp-speed vs. mine-sweeper [TG]
Speed-favoring conditions (from Reid Hoffman, *Blitzscaling*): big new opportunity in a leaderless market; first-*scaler* advantage (being first to scale beats first to market — network effects/data returns/economies of scale, e.g. eBay beat Amazon/Yahoo; Amazon+Microsoft couldn't unseat Google search); active competition; pre-product-market-fit. If 3+ check out, default to warp speed.

Mine-sweep (go slow) when: risk to humans (medical/security/infrastructure), risk to market positioning, **or when high personalization is required to deliver value** (generic fast shipping won't demonstrate it).

**Eisenhower Design Matrix** (clarity × risk, built by researcher Jeanette Ficella to answer "when to prioritize research over speed"):
| Condition | Decision |
|---|---|
| High clarity, low risk | Warp-speed research AND craft; measure and iterate |
| High clarity, high risk | Mine-sweep research, then warp-speed the craft |
| Low clarity, high risk | Mine-sweeper pace on research BEFORE building anything tangible |
| Low clarity, low risk | Warp-speed everything; measure and iterate |
"Not a magic eight ball — a guideline."

### Stage your bets [TG]
Frame every UI decision as "how important is this to the company's plan to win the market?" If **not** critical → take the simplest solution (even the loudest person's) and move on. If **critical** → decide with scaffold + research, choose the simplest path, let user feedback finalize. Cap debates: when a pattern debate stalls, its cost exceeds its value — choose the simplest path to a decision. Name the *macro bets* (Velocity / Efficiency / Accuracy / Innovation); a micro UI bet is only valid if it intentionally supports one. "Designing quickly is fine; recklessly designing quickly is not" — the difference is intentionality.

### Design thinking upstream [NL]
5-step arc: **Discover** (research, inspiration → raw data) → **Interpret** (personas, scenarios, outcomes → information) → **Ideate** (generate + refine ideas) → **Prototype** (mocks to test feel) → **Test** (feedback, refine, repeat). Treat it as a roadmap to discover answers, not a forced linear path.

**Design sprints** (Google playbook, 2–5 days): plan 1 day of prep per sprint day; team of 5–8; stages Understand → Define → Diverge → Decide → Prototype → Validate. Write a **design challenge statement** first (relevant, concise, inspiring, names the target audience, specifies deliverables). "First tweet" exercise: force strategy into ≤140 characters. **Zen voting**: review and vote in silence first so no one is biased.

**Extract business goals before designing — max 5 [NL].** Refuse "we just want a good-looking website" as a brief; ladder it down with ~3 rounds of "why" until the answer is stated in outcome terms (revenue/conversion/retention), not feature terms (responsive/fast/modern). Convert to department goals (marketing: leads/traffic; sales: conversions; support: fewer calls; ops: lower cost) and make them **SMART** with numbers + deadlines ("increase conversion 5% in 3 months," "cut task-completion time 20%").

**Go wide before deep [both].** TG: ≥6 distinct low-fi concepts in ~30 time-boxed minutes, all at identical fidelity (consistent fidelity prevents polish bias), then pick 1–2. NL: "8 ideas in 5 minutes" warm-up (fold paper into 8 rectangles). Look at conventional patterns *first*, then reach for novel ones. Build 2+ real layout alternatives before committing, and keep the rejected variant "in your back pocket" for a future split test [NL].

**Scale research to project length [NL].** A 2-week sprint cannot spend 4 days on research; a 6-month project might reasonably spend 2 weeks. On short sprints, hypothesize from quick channel checks and defer validation to testing. Don't produce 100-page research docs — they don't improve outcomes. Time-box everything and say "enough" [both].

**Craft is built two ways only [NL].** Develop the eye (study work better than yours) + put in the reps (hundreds to thousands of hours). Keep a private folder of non-commercial experiments, including deliberate imitation of masters, purely to internalize *why* their work works.

---

## 2. Information Architecture & User Tasks

**Structure content before styling anything [both].** IA, sitemap, user flows, and wireframes come before visual design. If you can't justify an element's position by pointing to a user goal or business objective, its position (or the element) is wrong [both].

**Paper notebook before any tool [NL].** Dump discovery, objectives, insight takeaways, and a rough block-out of sections into a plain notebook first — faster than digital for synthesis, and re-reading it re-triggers full context. The act of writing is what processes the information.

**Build IA around the top tasks [both].**
- Ask: what are the **top 5–10 tasks** users want to perform? Structure IA around those first [NL]. TG: model user types + roles, list primary tasks (which JTBD each serves), map CRUD per object, define entity relationships (1:N, M:N).
- **Design the most frequent, most important tasks first** — before settings/billing [TG].
- **Identify edge cases last** and defer their optimization [NL].
- Treat the first IA as a **hypothesis**; validate with card sorting or tree testing [both].

**Group items the way users think, not the way the org chart thinks [both].** Get the mental model from research (do users split "shirts vs. tops"?), don't guess internally. Match vocabulary to the audience (mass-market = generic terms; Gen-Z product = terser, less text).

**Jobs-to-be-done, not features [both].** Write 2–3 primary JTBD: "When [situation], I want to [motivation], so I can [outcome]." Outcome-phrased, never feature-phrased ("organize my emails so I don't lose information," never "add tags, labels, and folders"). Assumption-based JTBD beat none — mark them as assumptions. NL's user-story form: "[persona role] + [specific, filterable need]" granular enough to map to a UI affordance ("As a hunter, Dan wants jeans, 32" waist, long length"). Real projects have ~10–20 primary actions and 50–100 secondary — focus effort on the primary list.

**Map every micro goal to a macro goal [NL].** Every user story should ladder up to a business objective; delete work that ladders up to nothing.

**Sourcing IA when you don't know where to start [NL].** If a product exists, audit and evolve its current structure — don't start from zero. If nothing exists, study competitor sites in the same category directly (use Mobbin to browse real current screens by app / flow / element). Reusing common patterns matters because the more products use a pattern, the more calibrated users' expectations are — reinventing standard patterns adds cognitive load.

**Design for every entry point, not just the homepage [NL].** Users land via search, social, ads, direct links. Every standalone page must make sense on its own regardless of entry point. Design separate flows per persona/intent (a "hunter" who knows what they want needs filter/search; a "browser" needs an inspiration flow), not one universal flow. Scale UI complexity to catalog size — ~100 items doesn't need ASOS-grade filtering.

**Navigation labels are literal, never clever [both].** "My Clusters," "Team," "Analytics" — organized by user goals, not internal org structure. Orient users with breadcrumbs on any hierarchy deeper than one level ("Dashboard > Campaign > Post"). Follow established conventions for nav placement.

**Classify every nav item into one of three groups first [TG]:** Product/Entity nav (mainline features), Contextual nav (changes with task — recents, related, bookmarks), System nav (account/billing/settings, behind the avatar menu). Don't mix system items into primary nav.

**Prioritize with position, size, and contrast [both].** Give the highest-priority actions prominent positioning, larger text, and contrasting color. Prioritize nav items by *frequency of use* (data, not opinion); keep few grouped items up front, everything else behind a clearly-cued "More" — but every option must stay discoverable, including on small screens.

**Turn competitor takeaways into design directives [TG].** Collect 3–8 direct + indirect competitors before a project; revisit ~yearly, not per feature. Convert findings to directives ("competitor's customizability is valued but overwhelming → modular UI, simple by default with progressive customization").

---

## 3. Visual Hierarchy

**Hierarchy comes from structure, not assets — all five levers are zero-byte [TG]:** typography, color & contrast, whitespace & grouping, size & scale, proximity & alignment.

**The flatness diagnostic [NL].** When a design feels off and you can't say why, check whether every element is competing at the same visual weight — "nothing is accentuated, everything is ranked the same" is usually the actual bug.

**Build hierarchy from different mechanisms for different tiers [NL].** Don't assume hierarchy = size only. Size, contrast, and color are separate levers you can mix: on a product page the hero image wins tier-1 via *size*, while a smaller Add-to-Cart button wins tier-1 attention via *contrast/color*.

**De-emphasize on purpose [NL].** Actively shrink/tighten a secondary headline that would otherwise compete with the primary one — don't just size everything by importance-guess. Simplification is a clarity tactic: removing surrounding noise makes the one remaining message read as emphasized by default, with no extra styling.

**Size & scale [TG].** Larger = noticed first and read as more important. Make the primary action visibly larger than secondary. Use a fixed sizing scale (S/M/L tokens), not ad-hoc sizes. Step heading → subheading → body down progressively. Subtle size differences are sometimes more effective than huge ones — don't assume bigger is always better. Make key dashboard metrics/numbers/charts larger.

**Typography for hierarchy [TG].** Distinct styles for header/subheader/body/UI; differentiate with weight + size + color *together*, never one channel alone. Same information type always uses the same style (consistency itself lowers cognitive load). Too many fonts/sizes = visual chaos.

**Color for hierarchy [TG].** One bright contrasting color for the primary CTA; muted palette for backgrounds/cards. Reserve one unique high-contrast color for the thing that must be noticed (Von Restorff effect — e.g. unread notifications). Never rely on color alone.

**Whitespace & grouping [both].** Whitespace is a structural tool, not wasted space. Group related tightly, separate unrelated with more space (Gestalt proximity). Give CTAs extra surrounding whitespace to make them stand out at zero cost. **Prefer whitespace over borders/boxes for grouping.**

**Proximity & alignment [both].** Adjacency creates association — false proximity creates false associations. Left-align text as the default; align labels to fields; use a grid system. Consistent alignment reads as simplicity (Law of Prägnanz). Use indentation to show hierarchical relationships.

**The "turn off the image" test [NL].** Good typographic composition should look complete and strong even with the accompanying photo hidden. Align the type block's eye-path with the photo subject's pose/shape deliberately (a skater's diagonal pose leading into the headline), not by accident.

**Named laws in play [TG]:** Hick's Law (fewer choices = faster), Miller's Law (~7±2 working memory), Fitts's Law (bigger/closer targets are faster to hit), Von Restorff (the different one is remembered), Gestalt proximity/similarity, Prägnanz, figure-ground, Goal-Gradient, signal-to-noise.

---

## 4. Typography

**Decide type once, up front, then stop thinking about it [TG].** Pick a default from your library first with zero deliberation; get to the real work of solving software problems; revisit type only at the end for "special treatment." (TG's own war story: he used to spend hours picking a typeface at the start — now he defers it entirely.)

**One typeface, 2–3 weights [both].** Regular / medium / bold is the whole system. Variety comes from size, weight, and spacing — not more fonts. NL frames a typeface as a *weight system* (à la Univers 45 Light → 55 Roman → 65 Bold → 75 Black → 85 Extra Black); pick a family with enough weights to build hierarchy. If everything is bold, nothing is.

**Base size and scale [TG].**
- **16px base** font size (the browser default; good for perf and zoom behavior).
- Use a **modular scale, ratio 1.2 or 1.25**, so sizes relate harmonically.
- TG's provided custom scale: **12 / 14 / 16 / 18 / 20 / 24 / 30 / 36 / 48 / 60 / 72 px**.
- TG's Cluster example spec: H1 32px medium, H2 24px regular, Body 14px medium, small body 13px, Body-3 12px, caption 10px with +10 letter-spacing. (Note the internal tension: Cluster's body is 14px while the visual-style checklist example uses 16px body / 24px line-height — treat 16px as the web-reading default, 14px as an acceptable dense-UI body.)
- Every text element on screen belongs to a **named, defined style** (H1/H2/H3, body, caption, UI labels) — no improvised sizes.

**Line length and leading [both].** Line length **50–75 characters** (content-scalability places it at 60–75); cap with max-width. Line height **≈ 1.5× font size**, consistent across body text.

**Alignment [both].** Left-align body copy as the default (ragged-right). Center/right/justified are deliberate, occasional choices verified on the grid. **NL rule of thumb: don't use centered or heavily justified text past ~5 lines** — ragged edges on both sides get "wonky." Justify quality is tool-dependent: Photoshop's algorithm is bad (visible rivers), InDesign's is good, modern web justify is now usable. The interface must survive user text-enlargement without breaking.

**Type classification — pick by the mood each class carries [NL].** Three top-level families: serif, sans-serif, and **display** (headlines/decorative only — never body copy). Fold script into display or serif.

*Four serif classes* (era + stroke contrast are the signal): **Old Style** (Minion Pro — bookish, classic, low contrast), **Transitional** (Baskerville — refined, literary), **Modern/Didone** (Didot — pronounced thick/thin, high fashion/luxury), **Slab** (Rockwell — no contrast, rigid/robust/sporty).

*Four sans classes:* **Grotesque** (Akkurat — more character), **Neo-Grotesque** (Helvetica Neue — plain, neutral workhorse), **Humanist** (Lucida Grande — serif-like warmth, very legible), **Geometric** (Futura — built from shapes, modern).

*Visual diagnostics [NL]:* Grotesque vs Neo-Grotesque → compare the lowercase **g** (Grotesque more serif-like). Humanist vs Geometric → compare the lowercase **a** (Humanist "more like a serif," Geometric "more like a shape," near-circular O).

**Selection rule [both]:** neutral product UI → neo-grotesque or humanist sans. Warmth/legibility at small sizes → humanist. Branded/display moments → geometric or a serif class matching the brand's era. NL's personal note: loves geometric sans for headlines, not for body copy. Prefer a clean sans-serif for interface text generally [TG].

**Tracking (letterspacing) [NL].** Kerning = a specific letter *pair*; tracking = uniform across a run — don't conflate. Wide tracking on **caps** → grandeur/epicness (movie posters). Tight tracking → motion/edginess/urgency (skate brands). Tracking pairs best with geometric and condensed sans. **Hard rule (~99% of the time): never wide-track lowercase** — lowercase doesn't hold as a clean block when spread; it reads wonky. Slight *tightening* of lowercase is sometimes fine. Numbers are picked by eye, not formula. TG: tighter tracking on large headings, default on body — never letter-space body copy.

**Italic vs oblique vs small caps [NL].** Italic = a genuinely redrawn character set (serif tradition, elegant). Oblique = the upright form mechanically slanted (less refined). Small caps are their own glyph set drawn to sit on the **x-height** — *not* shrunk capitals. Use small caps (or spaced all-caps) for meta labels ("WRITTEN BY," "PHOTOGRAPHY BY").

**Match icon stroke weight to adjacent letterform stroke weight [NL]** — a concrete craft check most designers skip.

---

## 5. Color

**Limit the core palette to 3–5 colors [both].** Get variety from tints and shades of those, not new hues. Too many colors = visual clutter.

**Establish a color hierarchy and never break it [both].** One primary/brand color reserved for the actions you most want taken (Create, Generate); one secondary for lesser actions; neutrals for everything else. If the accent is everywhere, it points nowhere. A monochromatic scheme (one brand color + neutrals) is a safe, coherent default.

**Reserve color as the signal for interactivity [TG].** Clickable elements (buttons, links) get a color treatment static text never gets.

**Status colors are fixed vocabulary [both].** Green = success, red = error, yellow = warning — used identically everywhere, never repurposed. **Never encode meaning in color alone** — pair with icon/label/pattern (color-blind users). Verify with simulators (Stark, Color Oracle).

**Contrast floors (WCAG AA), treat as floors not targets [both]:** **4.5:1 for normal text, 3:1 for large text.** Check especially text on colored backgrounds, images, and gradients. Check every interactive state (hover/focus/active/disabled), not just resting. (TG pass example 15.98:1; fail example 1.72:1.) Contrast doubles as a hierarchy tool — give primary actions and key data the highest contrast. Build the brand palette so accessible combinations exist for every primary UI element; accessibility and brand aren't in conflict if planned up front.

**Subtle background color shifts group/separate sections** — cheaper and quieter than borders or heavy dividers [TG].

**Dark mode is a designed variant, not an inversion [TG].** Preserve readability and brand; re-tune shadows, textures, and icon contrast specifically. Check cultural color associations before shipping to new markets.

**E-commerce color rule [NL].** For shopping sites, "use the imagery as the basis for color — the image is the product; we want to be invisible and get out of the way most of the time." Brand color should recede so product photography reads as the primary color signal.

**Semantic button color [NL].** Make button color itself carry meaning consistently across the whole product (e.g. one color always = a code action, black always = download), not per-screen.

---

## 6. Spacing & Layout / Grids

**Define one base spacing unit and use only multiples of it [both].** TG: **8px** base → 8/16/24/32… everywhere; one scale, no ad-hoc values. This single rule creates visual rhythm.

**Spacing IS grouping and hierarchy [both].** Larger vertical gaps BETWEEN sections than between items WITHIN a section — if the between-section gap ≤ the within-section gap, hierarchy reads flat. Keep related controls (Edit/Delete/Share) close, separated from unrelated content. Give the primary CTA generous whitespace. NL calls consistent, considered spacing "the single biggest tell between amateur and polished work" — stronger than layout structure itself. NL's unit-block technique: make the gap *within* a related group smaller than the gap *between* groups (watch title + price tight = one unit; larger gap to the next section).

**Density matches task [TG].** Tighter spacing in data-dense areas (tables, analytics); more generous in reading/creation areas. On mobile, reduce inter-card spacing to use limited space — but drop to smaller steps of the same unit, don't invent new values.

**Grids create order, consistency, and rhythm [NL].** Decisions made once, then reused; shareable across people; help users scan. When a layout feels vaguely "off," audit grid and baseline alignment first — rhythm is felt before it's seen. Practice grids on pure typography/imagery layouts first, then carry that editorial discipline into UI. Reference: Müller-Brockmann's *Grid Systems*.

**Two grid systems — pick by product type [NL]:**
- **12-column + baseline grid** → responsive websites / web products. 12 is divisible by 1/2/3/4/6 (max layout flexibility) and matches the Bootstrap convention devs expect.
- **8px / 8pt grid** → web apps / high-density interfaces (dashboards). In Figma, just set the row/column grid value to 8px — that's the whole spec.

**Concrete grid numbers from NL's live build (1440px desktop artboard):** 12 columns; margins ~30–50px (he uses 50); gutter ~30px; **baseline unit = body line-height ÷ 2** (24px line-height → **12px baseline**). Tablet: keep 12 columns, margin ~20px, gutter ~15px. Mobile: **drop to 4 columns**, margin ~25px, gutter ~20px. In the homepage build NL states the baseline unit as **12px and keeps spacing to multiples of 3 or 4** of it. (Note the reconcilable tension: TG's 8px spacing base vs NL's 12px baseline unit — 8px suits dense app UIs, a 12px baseline derives naturally from a 24px reading line-height. Choose the one that matches your line-height, and keep the multiples discipline either way.)

**Save every grid setup as a reusable Figma style/template [NL].** Drill: from one base grid, generate many layout variations (2/3/4-col, asymmetric) with type/shapes to build a personal library of layout "moves."

**The grid is a guide, not gospel [NL].** Snapping is the default; breaking it is a deliberate, occasional optical call. NL's targets: sit type on the baseline ~95% of the time; break ~5% for deliberate optical correction. **Advice for beginners: stick close to the grid until you have the experience to know when an override is actually correct.**

**Responsive layout [both].**
- Design **desktop and mobile concurrently** [NL] — NL is explicitly anti-"mobile-first," starting from the largest canvas (chose 1920px, cross-checked against analytics), bouncing between desktop and mobile, doing tablet last unless it's primary. Prefer to "step into the mind of the user" per context rather than apply a blanket rule.
- **Don't design to named devices [NL].** "The design should just break whenever it's naturally occurring — could be 1400, 1200, any size." Don't design to iPhone/iPad sizes; design so the layout breaks wherever content demands.
- Card-grid responsive cascade default: **3-column → 2-column → 1-column** as width shrinks [NL].
- TG: define breakpoints and plan the mobile → tablet → desktop → widescreen adaptation; build layouts on flexbox/grid; use **relative units (rem/em/%), not fixed px**, so text scales with device and user preference.

**Cap text line length at ~60–75 characters with max-width [TG].** (See Typography for the 50–75 variant.)

**Auto Layout for resilience, not just spacing [NL].** Build reflowing panels (e.g. a cart modal) with nested Auto Layout so they adapt as items are added/removed; stress-test by pasting ~30 line items to check the edge case.

---

## 7. Components & States

**Design every component state [TG]:** default, hover, active, disabled, and keyboard **focus** — plus product-specific states (e.g. "processing" for async work). Differentiate with color/opacity/border/shadow, consistent with the system.

- **Every interactive element gets a hover state** — e.g. darken the button by **10%** on hover, the same shift on every button. Subtle background change on list rows signals clickability.
- **Disabled reads as dead:** muted color + hover effect removed.
- **Focus gets a prominent outline/glow.** Never remove the default focus outline without a replacement.
- Maintain sufficient contrast between states in **both light and dark mode**.
- Feedback animations **200–300ms** (e.g. a slight scale on click) — short and purposeful, nothing decorative.
- Same visual treatment for the same state across similar components (Create/Edit/Delete buttons match).

**Button / action hierarchy [TG].** One visually dominant primary action per view, styled *identically app-wide* (same color/size/style). Emphasize via size + color + placement (top-right or a floating action button for the main create action). Pair label + icon ("+ New Cluster"). Weight prominence by **frequency of use** (Edit ≫ Delete if used more). Give immediate visual feedback the instant the user clicks (loading state/progress). Secondary actions progressively disclosed behind a consistent overflow affordance (the "…" three-dot icon), never competing with the primary; access depth proportional to frequency.

**Input controls match the data type [TG].** Calendar picker for dates (never free-text), dropdown for predefined categories, checkbox for multi-select, radio for single-select. NL's concrete rules: default a quantity field to 1 if ~90%+ buy one; use a dropdown only for a small range (~≤4), an input box beyond that; use **buttons not a dropdown** for a small set of size options (user sees all choices + stock state at a glance); fall back to dropdown only for long lists.

**Label every field specifically [TG].** "Enter article title," not "Enter text"; "Summary Length," not "Length." Placeholder text is for format hints only ("tags separated by commas"), never the label itself. Group related inputs (all metadata together). Enable autofill/autocomplete. Prefer a smart/searchable input over a very long dropdown (Hick's Law).

**Content scalability [TG].** Design for both extremes (few items vs hundreds; short vs long text). Decide overflow per element: truncate-with-ellipsis vs wrap. Provide pagination or infinite scroll past a threshold. **Test with realistic minimal AND massive datasets** — lorem ipsum hides real failures. Keep interactive elements tap-friendly on mobile even with long content.

**Componentize the moment something repeats [NL].** As soon as a type style or block appears twice, turn it into a Figma style/component and file it in a running library. Name components exactly what they are (h1, navigation, paragraph) so search works. Payoff: one global edit propagates across "30 to 100 screens" instead of manual updates. Organize the library by what a component *is* (product, cart, footer, navigation), **never by breakpoint**. Enforce one team-wide term per component ("navigation" never "menu"; "banner" never "hero").

**Elevation / shadows [TG].** Define **3–5 elevation levels** (subtle/medium/high) and use only those tokens — no per-component ad-hoc shadows. Elevation must *mean* something: higher = interactive/focal (cards, buttons, floating toolbars); static background stays flat. Raise elevation on hover as feedback. Combine elevation + size + color for the single most important action (use that stack once per view). **Performance: box-shadows are not free** — use judiciously on elements that repeat many times; prefer few simple shadows over multi-layer ones. Dark mode needs its own shadow treatment. NL's concrete spec for a modal that must separate from the page: **250px blur at 20% opacity** — soft-and-wide beats hard-and-tight (arrived at by testing no-shadow → grey stroke → wide soft shadow).

**Iconography [TG].** One style (outlined/solid/illustrated) with uniform stroke weight and corner radius. Universal metaphors for common actions (magnifying glass = search, gear = settings, bell = notifications, plus = add). Icon-only is earned by universality — label anything non-obvious ("Generate AI Summary"). Ship as **SVG**. Accent color only on create/primary actions. Every icon needs an accessible name. Animate only as feedback (save → checkmark).

**Shapes as tools, not decoration [NL].** Use simple geometric shapes as image-crop masks, number/label badges, or points of interest. The cutout/clip technique (subject silhouette clipping type behind it) creates cheap depth. Multiply blend mode is the default for lifting text over strong-color brand imagery. Present work "in devices" (laptop/phone frames) so stakeholders can imagine it on real hardware.

---

## 8. UI Patterns

**Default to established patterns; innovate only with a clear UX win and the resources to validate it [both].** Battle-tested + familiar + fast beats novel in almost every low-risk situation. Convergent-looking interfaces are not a failure state — familiarity is a usability feature. Never invent a new interaction for originality's sake; if a standard dropdown works, ship the dropdown.

**5-level originality spectrum — pick a level deliberately [TG]:** 1. Direct copies (login, settings, nav, upload — the commodity) → 2. Remixes (combine proven elements, must improve on either source alone) → 3. Indirect parallels (borrow the *underlying principle* from another domain, not the surface UI) → 4. Metaphors (map product functions to a known metaphor; don't overextend past its useful limit) → 5. True innovation (only where existing solutions are inadequate; expect many failed iterations; reserve for a core differentiating JTBD). Copy the commodity, design the differentiator.

### Chunking (reduce load by grouping) [TG]
- **Card layouts** for collections of similar items: consistent sizes, clear title, internal hierarchy, whitespace, hover state; don't overload or use for a single linear process.
- **Tabs** (switch/compare categories) and **accordions** (hide detail/advanced). Never put content users must see simultaneously — or critical info/primary actions — behind them. Don't nest accordions deeply.
- **Grouped form fields** under clear labels with visual separation; collapse advanced/rare groups by default; don't group short forms.
- **Chunk lists into groups of 5–9 items** (Miller's Law) with clear headings; cap top-level nav at **5–9 categories** (ideally 4–5). Tighten spacing within a group, add whitespace between.
- **Pagination:** 10–20 items per page; show current/total; preserve position on back-navigation. Loading a subset per request is an explicit **performance win** (faster loads, less server load).
- **Carousels:** auto-rotating with no user control is the *wrong way*; if used, make it user-controlled with pause/play — and keep critical content out of carousels entirely.

### Progressive disclosure [TG]
Reveal essentials first, detail on demand. **Never put essential information or primary actions behind any disclosure container** (tooltip, collapsed section, drawer, read-more). Every drilldown has three designed parts: **trigger** (click/hover), **container** (modal/popup/drawer), **contextual reference** back to the parent (overlay/breadcrumb) so users don't hold context in working memory. Make every disclosure keyboard-accessible. Avoid layout shift from expansion (CLS).
- **Tooltips** (hover, brief) vs **popovers** (click, richer). Add a short hover delay; don't hide too quickly; never put critical info only in a tooltip.
- **Nested menus:** limit to **2–3 levels**; never put actions (Edit/Delete) inside navigation menus; never a category with a single item.
- **Expandable rows:** default open when most users need the content, closed otherwise — all-open and all-closed both defeat the pattern.
- **Modals/dialogs:** reserve for critical/irreversible actions; one decision per modal; action-verb button labels ("Delete Project," never "OK"); closable via button, Esc, and click-outside; don't nest. **Prefer undo over a confirmation dialog for reversible actions.**
- **Read-more:** action-specific link text ("Read full article," never "More…"); don't cut mid-sentence; provide a re-collapse near the end.

### Cognitive load [TG]
- **Pagination for goal-oriented tasks** (search, tables, reports — need to find an item / know position / reach the end); **infinite scroll only for exploratory feeds** — always preserve list position on back.
- **Steppers/wizards:** label each step + describe it, show position + steps remaining, allow back-editing and save-and-resume; keep step count low; don't force strict order when unnecessary; don't hide required info in optional steps. Visible progress raises completion (Goal-Gradient).
- **Minimalist navigation:** 4–5 top-level items; strip nav to near-zero on focused work surfaces (editors, checkout); never ambiguous icons without labels.
- **Simplified forms:** ask only what's essential now; smart defaults + pre-fill + autofill; replace long dropdowns with autocomplete; reveal advanced/conditional fields via progressive disclosure, not a wall of "(optional)"; plain-language labels; single-column vertical alignment.

### Feedback & visibility [TG]
- **Immediate feedback for every action.** Global events → toast/banner ("Changes saved"); local events → inline next to the component.
- **Progress:** determinate bar when duration/steps are known; spinner only for unknown waits. **No indicator for operations under 1–2 seconds.** Never fake or artificially slow progress. Add percentage / estimated time where possible.
- **Confirmations:** confirm important/irreversible actions with specific detail (what changed, who's affected, when — "Post scheduled for June 3, 9:00"); skip confirmations for trivial actions so they retain meaning.
- **Notifications:** relevant, concise, actionable, dismissible, user-controllable; never interrupt a critical task; never notify about trivia.
- **Contextual help:** put it where the question arises (consistent "?" affordance next to the thing it explains), one sentence, dismissible — never used to excuse a confusing design.

### Error prevention & handling [TG]
- **Prevent errors upstream** (validation, undo, autosave, constraints); dialogs and error messages are the last line, not the first.
- **Real-time validation:** fire **on blur (field completed), not on every keystroke**; state specifically why input is invalid and how to fix it; show the positive state (green check) too; don't block submission on non-critical issues; don't stack many simultaneous errors; **always re-validate server-side** (client-side can be bypassed and also reduces server load).
- **Error message formula:** plain language + what went wrong and why + one specific actionable fix. Non-blaming tone. No bare error codes. Tailor to context (duplicate name → suggest alternatives; unsupported file → list accepted types).
- **Undo:** implement for destructive/bulk actions; put the Undo control right where the action happened (deletion toast); offer multi-level undo; use Ctrl+Z conventions.
- **Autosave & drafts:** save at intervals and after significant changes; show a *subtle* "saved" indicator; keep versions revertible; still allow manual save; provide a drafts area to resume/discard.

### Empty states [TG]
Design zero-content states to be helpful and actionable — a common place for a single explanatory illustration + a clear next action ("Generate your first summary"). Don't crowd the real functionality.

### Onboarding & learning [TG]
- **Tours, tips, and tutorials are never a substitute for intuitive design** — if you're explaining basic UI in a tooltip, redesign the UI.
- Onboarding must always be **skippable/dismissible**; never gate app usage behind a tour, tutorial, or checklist.
- **Product tours:** concise, key features only, show step progress ("1 of 13"), explain *why* each feature is valuable.
- **Contextual tips:** one at a time, at the moment of need, action-oriented, dismiss-and-stay-dismissed, tested timing.
- **Onboarding checklists:** small actionable items, visible progress ("2/4"), pre-check completed steps (Endowed Progress Effect), stop showing once the user is active.
- **Help docs:** clear categories with article counts, robust search, embedded context-sensitive "Learn more" links, promote inside the app.

### Navigation & wayfinding [TG]
- **Bottom navigation (mobile): 3–5 items max**, icons + short labels, clear active state, never hidden on scroll, never on desktop (Fitts's Law — bottom minimizes thumb travel).
- **Breadcrumbs:** every level clickable except the current page; supplement primary nav, never replace it; skip on shallow sites.
- **Off-canvas/hamburger:** for scarce space (mobile); on desktop show a visible sidebar and transform to off-canvas only on small screens; always slide from the same side (spatial memory); never the only navigation.
- **Sticky vs fixed:** pin only what matters, keep it small, consider shrinking/fading on scroll; test rendering performance on low-end devices (position:fixed/sticky can jank); watch collisions with form inputs and the mobile keyboard.
- **Global search** prominent in top nav with a visible shortcut (⌘K) + autocomplete; scoped search states its scope and offers one-click expansion to global.
- **Faceted filters:** show result count per facet value, one-click reset-all, visible total-results ("Showing 10 of 68"); optimize search performance at scale.

### Social proof [TG]
- Authentic, permissioned, current testimonials — specific over generic; average rating + review count *at the decision point* (pricing page); never fake quotes or stock faces; don't hide negative reviews; moderate/curate UGC before showcasing.
- Badges/seals build trust only when authentic and scarce; put security seals where anxiety lives (login, payment). Misleading or overused badges erode trust.
- Social/sharing features optional and unobtrusive: never auto-post, never force account connection, never clutter the UI with widgets. Offer social login to cut sign-up friction.

### Personalization [TG]
Customizable dashboards (drag-and-drop, role templates, save multiple configs, easy reset, sync across sessions — and don't let customization slow load). Adaptive content must be **subtle, explained, override-able, based on consistent (not single) signals, and never remove access to anything** — adapt = reorder/emphasize, never delete. Recommendations: blend behavior + stated preference + context, explain the "why," keep diverse, keep visually secondary, offer opt-out. Settings: sensible defaults, logical grouping with one-line descriptions, live preview, easy reset. Localization: standard locale codes; localize dates/numbers/units/currency and visuals, not just strings; plan for text expansion and RTL; never lock language to IP location.

---

## 9. Accessibility

**POUR is the floor [TG]:** Perceivable (text alternatives, captions), Operable (full keyboard, enough time, no seizure triggers), Understandable (readable, predictable, error-forgiving), Robust (valid markup compatible with assistive tech). Accessibility can't be achieved by design alone — but design leads.

**Accessibility-first is cheaper than retrofitting [TG].** "Implementing accessibility from the start is always faster and cheaper than retrofitting later — and it often leads to better usability for everyone." (The direct counter to "we need to ship.") It also improves UX for everyone: bright sunlight, cheap screens, temporary injuries, forgotten glasses.

**Keyboard navigation [TG].** Every interactive element reachable and operable by keyboard alone. **Always show a visible focus indicator; never remove the default outline without a replacement.** Tab order follows visual/DOM layout. Provide a "skip to main content" link. Never create keyboard traps. Never rely on hover-only interactions (unreachable by keyboard). Surface shortcuts in tooltips.

**Semantic HTML first, ARIA second [TG].** Use `<button>`, `<nav>`, `<main>` before `role=` hacks. `aria-label` only for ambiguous/icon-only controls (`<button aria-label="Add new content">+</button>`). Use `aria-live` for dynamic changes, `aria-current="page"` for the active nav item, `aria-invalid` + `aria-describedby` for form errors. Keep ARIA in sync with dynamic content (stale ARIA is worse than none). Never contradict native semantics. **ARIA ≠ accessible — test with a real screen reader.**

**Alt text [TG].** Every meaningful image gets concise descriptive alt text; **`alt=""` for purely decorative images** (so screen readers skip them). Never start with "image of…" (redundant). Keywords natural, never stuffed. Don't repeat adjacent caption text. Long/complex images: short alt + separate long description. Test by browsing with images off. Update alt text whenever you swap the image.

**Color contrast [TG].** 4.5:1 normal / 3:1 large — floors, aim higher. Check every state and text over images/gradients. Never rely on color alone. Test with color-blindness simulators. Offer a high-contrast mode. (See §5.)

**Resizable text & zoom [TG].** **Use rem/em for font sizes, never fixed px that can't scale.** **Layout must survive browser zoom to at least 200%** with nothing clipped or broken — test it. Never disable browser zoom (`user-scalable=no`). Avoid fixed-size containers that clip when text grows. Provide in-app text-size controls. Persist the user's preferred size across sessions.

---

## 10. Performance / Speed

Both courses treat performance as a design requirement, not an engineering afterthought.

- **Respect the Doherty Threshold [TG]:** slow products frustrate — speed of response is a UX feature. Define real-time data as "must update without lag" and content-heavy pages as "must load fast" during the Define-the-system step.
- **Load large datasets in subsets, never all at once [TG]:** pagination / lazy-load / infinite scroll is both a cognitive-load win and a direct Core Web Vitals win (faster load, less server load). Progressively load in chunks as the user scrolls.
- **Compress and correctly format every image; optimize for slow connections [TG]** — a hard requirement, not polish. Prefer **SVG** for icons, illustrations, and patterns (sharp at any size, tiny files).
- **Box-shadows are not free [TG]:** use `box-shadow` judiciously on frequently repeated elements; prefer few simple shadows over multi-layer ones.
- **Test sticky/fixed elements on low-end devices [TG]** — position:fixed/sticky can trigger repaints and jank.
- **Test animations on low-end devices [TG]:** an animation that stutters is worse than none; if it can't run smoothly everywhere, simplify or remove it. Never let animation block user input.
- **Feedback animations 200–300ms [TG]** — anything longer feels sluggish.
- **Responsive images: maintain one aspect ratio from full-size to thumbnail [NL]** so a single source scales cleanly across contexts instead of needing per-size crops.
- **Avoid layout shift (CLS) from disclosure/expansion [TG]** — expanded content must not shove page elements around.
- **Customized dashboards and search must stay fast at scale [TG].**
- **Provide an XML sitemap for public pages [TG]** — directly supports SEO/indexing (plus a user-facing sitemap of main sections only).
- Alt text also serves slow connections and image-off browsing [TG].

---

## 11. Copywriting in UI

- **"Copy is part of design" [NL]** — repeated across lessons. Use real copy in wireframes wherever possible; use lorem ipsum sparingly. Pull actual client copy into a doc and paste it in. Real data/content surfaces design problems that filler text hides [both].
- **Words are a first-class design-system section [NL]** — tone-of-voice sits equal to typography and color, not as an afterthought.
- **Label actions in plain human words [both].** "Add Content," never "Initiate content ingestion process." Instruction copy is one or two plain sentences ("To create a new Cluster, select this button, then add a title"). No jargon in labels, tooltips, step descriptions, or error messages.
- **Button labels name the action [TG]:** "Delete Project" / "Save," never "OK." Link text is action-specific: "Read full article," never "More…."
- **Error messages [TG]:** plain language + what went wrong + one actionable fix, non-blaming tone. A good message teaches correct usage (show correct search syntax with an example).
- **Heading discipline [NL]:** h1 occurs only once per page; if text is visually too big for its importance, demote it to h2/h3 rather than force it — heading level tracks information hierarchy, not "biggest thing I want to be big."
- **Brand-voice copy in the UI [NL].** Feed design principles into actual microcopy (a returning-user discount written "Hey, thanks for being part of the fam, get 50% off — yep, not a typo" to express a "personable and human" principle). Personalization is copy as much as layout.
- **Preserve users' own words [NL].** When synthesizing research, quote respondents verbatim rather than paraphrasing, so intent doesn't get flattened.
- **Match vocabulary to the audience [NL]** (mass-market = generic widely-understood terms; niche/Gen-Z = terser, less text overall).
- **Run a spell-checker over all copy as a required last step before a page is "done" [NL].**

---

## 12. Moodboards / Styleboards & Encoding a Visual Direction

**Test directions cheaply before committing [NL].** Never build a full high-fidelity concept just to test a visual direction — board it first, get a reaction, then invest. Boards cost a fraction of a comp and earn early stakeholder buy-in through involvement (collaboration, not a big reveal). You're slow at first; each board gets faster.

- **Moodboard** = curated *references* (images/videos) capturing the essence of the end result. Broad. Use to communicate direction early while exploring territory.
- **Styleboard** = you *build the actual assets yourself* (real type, color, imagery treatments applied) — more detailed and specific, closer to real UI. Use when narrowing to one direction.

**Moodboard doc anatomy [NL]** (Figma template): (1) Cover — concept name, client, prepared-by + date, a one-line **purpose statement** for skimming stakeholders, a live Figma link, collaborator list; (2) Target audience — pasted straight from discovery so the visual direction has a stated "why"; (3) Visual direction — plain adjectives ("neutral, minimalistic, content- and typography-driven") each with a short description; (4) Reference grid — branding/type/imagery/UI pinned Pinterest-style, loose; (5) native Figma comments for team annotation. Add dedicated pages (just type, just UI) as needed.

**Styleboard structure [NL].** Typically: (1) art direction / imagery + typefaces named explicitly with lockups; (2) that type applied inside the actual app/site; (3) card UI + color palette + motifs. **Time-box it: a few hours to one day, not weeks.** No fixed template — the only constants across NL's real styleboards: color, typography, imagery, text lockups, iconography, a couple of representative UI elements. A styleboard should include **written personality/copywriting direction** ("the simplicity and sophistication of Everlane meets the vibrant, infectious personality of Luxy Hair") and can dictate photography art direction, not just UI.

**The design-vision doc that precedes the system [NL]** (spend ~1 hour re-reading all prior discovery artifacts first): North Star statement(s) → "What we know" (hard business/analytics stats — "70% of purchases from social+email," "1 in 8 repeat customers") → quarterly business objectives as numbers → light personas (name, role label, primary device) → user epics (one line per persona) → user goals as **verbatim research quotes** → target emotional arc mapped to funnel stage (browsing = *informed*, post-purchase = *satisfied/happy*) → a **maturity pyramid you climb: functional → reliable → usable → pleasurable** (don't ship "delightful" on day one; earn it in that order) → design principles as **principle + concrete action + intended result** triples, not just adjectives.

**Define 3 words users should describe the product with [NL];** after testing, ask users for their 3 words and compare — a measurable check on design intent.

**Working reference wall [NL].** Before high-fidelity work, paste the styleboard, goals, sitemap, wireframes, and personas loosely around the artboard edges — "not to be pretty; every time we design we're checking if we're hitting these goals." Start with the page that dictates direction for everything else (dashboard for a complex app, home/landing for e-commerce, the most-used screen for mobile). Block-first: rough layout as flat colored rectangles with no content to lock macro structure before touching type or imagery.

**Offline-first inspiration [NL].** Deliberately mine print magazines and books (Monocle, Mindfood) *before* Dribbble/Behance, specifically so your output doesn't look like everyone else's "popular reference" work. Then move to online functional-pattern references (Mobbin, CodePen, Site Inspire). Prioritize inspiration matching your project's goals/constraints over flashy consumer apps, and look at adjacent domains, not just direct competitors [both].

**Design system [NL]** — build one when multiple sub-brands/teams produce many pages off one system (Airbnb); a small site doesn't need one. Shipped-system sections: cover + purpose + named owner + live Figma link + feedback channel; copywriting/tone-of-voice (first-class); typography (downloadable fonts; a tight base UI set + a deliberately looser approved-display set for campaigns; a live scale table with hover-preview + a separate small-screen table); color (primary vs secondary palettes, click-to-copy hex); a governed searchable image library; the grid shown responsive; components organized **Atomic-Design style** (Atoms = buttons/icons/fields/type styles/spacing blocks, on the grid unit; Components = navigation/banners/product blocks/footers). Keep flexibility — "you don't want it so rigid people feel they can't add to it and make it better."

**Atomic Design [TG]:** Atoms (buttons, inputs, text) → Molecules (forms, menus) → Organisms (headers, footers) → Templates → Pages. Use it to define reusable patterns and to port an optimal pattern from another product into yours.

---

## Cross-Cutting: Restraint & Consistency

**Restraint is the demonstrated house style [NL]:** 1–2 typefaces, strict grid, black/white plus one accent color — hierarchy through structure, not decoration. Simplify for clarity, not for a minimalist aesthetic.

**Consistency is the meta-rule [TG]:** same menu behavior everywhere, same type styles for the same content class, same spacing scale, same size scale, same color meanings — every inconsistency is added cognitive load. Textures/patterns are optional polish — subtle, never under text, never in content areas, first thing to cut for speed.

**Eliminate visual clutter [TG]:** prefer whitespace over borders/backgrounds/shadows for grouping; add shadows only for functional elevation; only necessary information (Nielsen #8 + Hick's Law); recognition over recall — never force users to remember information across screens.

---

## Notable Conflicts & Tensions Between the Two Courses

1. **Touch-target minimum (internal to TG):** 48×48px in the spacing/visual-style checklists vs 44×44px in the visual-hierarchy module. (44 = Apple HIG, 48 = Material.) Use 48 to satisfy both; never below 44.
2. **Body font size (internal to TG):** 16px web-reading default (base rule + visual-style example) vs 14px body in the Cluster type spec. Resolution: 16px for content/reading UIs, 14px acceptable for dense app UIs.
3. **Base unit — TG 8px spacing vs NL 12px baseline.** Reconcilable: 8px suits dense app UIs; a 12px baseline derives from a 24px reading line-height (line-height ÷ 2). Pick the one matching your line-height; keep the "multiples only" discipline either way.
4. **Mobile-first — NL is explicitly against it** (design desktop+mobile concurrently, start from the largest canvas, don't design to named device sizes). TG is neutral (responsive adaptation mobile→desktop). No hard contradiction, but NL's stance is the sharper opinion.
5. **UX/UI separation — NL explicitly rejects the wireframe-then-skin relay** (visual richness changes how hierarchy reads; work structure/interaction/visual concurrently). TG's sequence puts fidelity last but also says loop back and diverge again. Mild tension: don't hand off a "UX-approved" skeleton for someone else to color in, but still don't start *with* the visual.
6. **Personas — both keep them light**, but NL says some projects need none at all (go straight from data synthesis to design). TG builds JTBD statements regardless. Aligned in spirit (avoid 100-page dossiers).
