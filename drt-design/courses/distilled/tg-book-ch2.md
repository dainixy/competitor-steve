# Making UX Decisions (Tommy Geoco) — PDF pages 101–200

**Covers:** Module 6 "Stage your bets" (conclusion, book pp. 84–113) · Module 7 "Creating a decisioning workflow" (pp. 114–129) · Module 8 "Default design rules" (pp. 130–133) · Module 9 "Checklists for designing new interfaces" (pp. 134–159) · Module 10 "Checklists for improving fidelity" (pp. 160–179; first half — component states, primary/secondary interactions, content scalability, system feedback; user input + navigation continue past PDF page 200).
Chapter title pages passed: Module 7 (PDF p. 131), Module 8 (PDF p. 148), Module 9 (PDF p. 153), Module 10 (PDF p. 180). PDF page = book page + 17. The book's running example is "Cluster," a fictional AI content-creation/collaboration web app.

---

## Module 6 — Stage your bets (business context for UI decisions)

Purpose: understand the market just enough to answer "does this UI decision really matter?" — a lightweight pre-design analysis, not user research. Author's rule: "Do it fast or don't do it at all. Trust your intuition."

### Step 1: Analyze your industry (Porter's Five Forces, low-fidelity version)
Run a quick pulse-check on all five forces — don't build a 100% complete picture:
1. **Competitive rivalry** — how many established players exist. High rivalry → your product must bring something new; put design effort into differentiating patterns, reuse standard patterns everywhere else.
2. **Threat of new entrants** — low barriers to entry → make the UI extremely user-friendly, borrow proven design-system patterns for unimportant pages (profile, settings), invest time only in core-JTBD patterns, differentiate on branding. High barriers → more room to experiment.
3. **Bargaining power of buyers** — if users can switch easily, prioritize accuracy (testing/research) over shipping scrappy; retention is earned.
4. **Bargaining power of suppliers** — mostly informational for designers (cloud/AI providers etc.).
5. **Threat of substitutes** — count adjacent products that solve the same job; more substitutes → differentiation matters more.

Data sources: trade publications, industry newsletters, competitor sites/ads/reviews, quarterly/annual reports; tools: Google News, SimilarWeb (traffic + acquisition channels), Wayback Machine (competitor "then vs. now"), Statista, Crunchbase (funding), Moat (competitor display ads), BuiltWith (their marketing stack), Justia (legal/patents), U.S. SEC filings.

### Step 2: Analyze competitors
- Categorize as **direct** (same product, same customers) vs **indirect** (different product, same customers).
- Collect **3–8** direct + indirect competitors total.
- Do this **before a project starts; revisit only once a year** (or on big market events). Don't redo per feature.
- Data types: business data (revenue, share, growth), product data (features, pricing, distribution), customer data (demographics, behavior, reviews).
- Per-competitor evaluation grid: Timeline (founded? first to market?), Revenue (how/how much/trend), Profitability, Funding, Market share (trend, regions), Customers (who, what problems, what reviews say), Product (competitive advantage, full offering, features), Takeaways (what they do well / what we can do better / what risk they pose).
- Turn takeaways into design directives, e.g. "competitor's customizability is valued but overwhelming → design a modular UI that's simple by default with progressive customization."

### Step 3: Define customer goals (Jobs-to-be-done)
- Understand what users are trying to accomplish, not features. ("People don't want a quarter-inch drill. They want a quarter-inch hole." — Levitt)
- Write **2–3 primary JTBD statements**: **"When [situation], I want to [motivation], so I can [desired outcome]."**
- Bad JTBD = feature/solution phrased ("Let me add tags, labels, and folders to my email"). Good JTBD = situation + outcome ("When I get emails, I want to organize them so I don't lose important information").
- If no user research exists, write assumption-based JTBD from market/competitor knowledge — better than none; mark them as assumptions and be ready to learn.
- Use JTBD to test whether the UI prioritizes the correct workflows and elements.

### Step 4: Name your bets
- Every UI decision is an implicit bet ("I'll reuse Google's design-system pattern because it's easy to design, easy to build, familiar to users"). **Designing quickly is not reckless; recklessly designing quickly is.** The difference is intentionality.
- Don't write down every micro bet — name the **macro bets** the company is making, then let micro decisions serve them. Four macro-bet categories:
  - **Velocity** — win by shipping faster (reduce time-to-delivery, reuse components, borrow metaphors from other markets).
  - **Efficiency** — win by managing waste (design systems, reuse patterns, reduce work-in-progress).
  - **Accuracy** — win by being right more often (research, instrumentation, discovery sprints).
  - **Innovation** — win by finding untapped market potential.
- **A micro (UI) bet is only valid if it intentionally supports a company macro bet.** "Nicer-looking 2-step modal" is invalid unless looking nicer serves the market strategy.
- When betting, know: when you'll learn if it succeeded; its risk level; its size/scale (solve-today pattern vs reusable-tomorrow pattern).

---

## Module 7 — Creating a decisioning workflow

You make **10–20 UI decisions per hour** while designing; slow decisioning undermines the whole effort. Decisioning = gathering information and placing intentional bets.

### The simplicity curve (name the stage you're in)
1. **Uninformed simplicity** — the solution looks simple because you don't yet see the problem's complexity (Dribbble-shot syndrome).
2. **Informed complexity** — the design handles the full requirement but exposes all its complexity (convoluted dashboards, junk-drawer navigation that never stops growing).
3. **Informed simplicity** — enough is known to make the design feel obvious/invisible (Don Norman: good design is invisible). Example shape: an interface that surfaces only the tools relevant to the user's current task.
- Under time pressure, reach informed simplicity by explicitly defining "good enough" and letting the shipped design inform the next iteration.

### Narrowing decisions
- Design takes as much time as you give it; information gathered per unit time hits **diminishing returns**.
- Produce the minimum needed to reach **critical mass** (self-sustaining usefulness): core features that do the job, enough value to demonstrate without overwhelming, an interface a new user can start with quickly.

### Weighing information — the chain of command
Ask three questions in order; each later source outranks the earlier ones when available:
1. **What does institutional knowledge say?** (the "information scaffold": cognitive/behavioral psychology, established design systems — Google/Microsoft/IBM, usability best practices, accessibility guidelines). Always the first check; the fallback when nothing else exists. This is "don't reinvent the wheel."
2. **What are my customers familiar with?** (Jakob's Law + change aversion: users prefer products that behave like products they already use). Sources: top-100 products/OS conventions, competitor patterns, tangential products your users use daily (Google Sheets, Salesforce, browsers), your own product's existing patterns. **Weigh familiarity above most of the scaffold** — familiarity is the best risk reducer in the absence of data.
3. **What does our research say?** (interviews, surveys, instrumentation: FullStory, Amplitude, Google Analytics). **Research is the source of truth** — most contextually relevant; it overrides both scaffold and familiarity.

Fallback logic: no research → use familiarity; no familiarity signal → use the scaffold. Repeat per UI decision until it's muscle memory.

Institutional knowledge is not gospel — known cases where breaking it wins:
- Redesigning when users know the current product (Snapchat's redesign cost 2% of DAU and $1.3B in valuation — familiarity beat "better").
- Regulated/antiquated industries where compliance forces "bad" UX (e.g. mandated tracking flows).
- Users with entrenched workarounds — a usability-correct v1 can fail because users prefer their own unrefined process.

Worked example (data table with too many columns): scaffold says cognitive load + progressive disclosure, and Google/Microsoft/IBM systems avoid horizontal table scroll → familiarity shows leading competitors use collapsible rows and users know spreadsheet scrolling → research shows users compare all data at once in high-volume tasks (extra clicks kill productivity) → decision: table with collapsible rows (still progressive disclosure), adapted from an existing internal pattern for speed. Intentional decisioning lets you justify the decision, define "good enough," and know where clarity is still missing.

---

## Module 8 — Default design rules

- Default design rules = acknowledged biases and guidelines that give a fast, consistent starting point. Treat as **strong opinions loosely held**, not rigid law.
- Optimize for **useful over exhaustively accurate**: a slightly-generalizing rule you can apply instantly beats a comprehensive analysis that slows decisions.
- Two delivery forms: **checklists** (structured considerations; use when starting a new task AND as an audit tool on existing UI) and **patterns** (reusable solutions to common problems; adapt to context, don't copy blindly).
- Checklists are **referential** (dip in and out, any order) or **sequential** (step-by-step, for multi-stage processes).
- Key insight: give two designers the same resources and they land in radically different places — **the order (and velocity) of decisions changes the outcome**, not the quality of the ideas. Most bad "design process" is a bad decision order.
- **Override a rule** when: user research/data says otherwise; it conflicts with design direction or brand guidelines; technical constraints require it. When overriding, **document the rationale**, and promote the override into a new rule if it proves better.
- **Update rules regularly** based on research/analytics insights, industry best practices, tech/tooling advances, and changes in product or audience.

---

## Module 9 — Sequential checklist for designing NEW interfaces

Six steps, in order: **1 Define the system → 2 Model user tasks → 3 Organize information → 4 Gather inspiration → 5 Generate rapid ideas → 6 Enhance fidelity.**

Prerequisites: a one-page project brief (problem statement, target users, business objectives, success metrics); user research data or *documented assumptions*; design tool ready with a library of reusable UI components/icons/assets.

### Step 1 — Define the system
- Determine system type and constraints: **web app** (cross-platform, instant updates, but limited hardware access, can be slower than native), **mobile app** (fast, offline, device features, but two platforms), **desktop** (full power, deep access, but installs/updates), **embedded** (task-specific, fixed hardware).
- Define **inputs**: forms, uploads, URL submission, voice, scanning, bulk import, API; plus security/validation needs (auth, encryption, sanitizing free text, password/credit-card validation).
- Define **outputs**: tables, charts, maps, notifications, audio — and their **performance/scalability requirements** (real-time data must update without lag; content-heavy pages need fast loading times).
- Define the **interface platform**: browser/mobile/wearable/voice; account for device limits; support keyboard shortcuts for power users; ensure accessibility for users with disabilities.
- Match input methods to real user contexts (e.g. a browser extension for clipping while users browse).

### Step 2 — Model the user tasks
- List user types + roles/permissions per type.
- List primary tasks: which JTBD each supports; break each into a step-by-step workflow with entry points, decision points, endpoints.
- Map CRUD: how users create/read/update/delete each object, with sequencing and granularity.
- Define key data entities and their relationships (one-to-many, many-to-many).
- Best practices: **design the most frequent and important tasks first** (before settings/billing); **label actions in simple human words** ("Add Content", never "Initiate content ingestion process"); validate task flows with usability tests on prototypes.

### Step 3 — Organize information (IA)
- Define high-level categories/sections; group them logically (by status, team, topic).
- Set a **hierarchy of importance** between content areas (core object pages outrank account settings).
- Identify entity relationships (1:N, M:N) — they drive page structure.
- Define primary navigation (main menu) and secondary/contextual in-page navigation (tabs within a detail view).
- **Prioritize critical content and actions: use prominent positioning, larger text sizes, and contrasting colors** to pull the eye to the highest-priority actions.
- Best practices: validate IA with **card sorting or tree testing**; **follow established conventions** (main nav where the category's popular tools put it — e.g. left side for productivity tools; familiar labels like "Dashboard", "Team"); orient users with clear labels and **breadcrumbs** ("Dashboard > Campaign > Post").

### Step 4 — Gather design inspiration
- First pick your **stage of originality** (a deliberate ladder):
  1. **Direct copies** — replicate an existing pattern exactly.
  2. **Remixes** — combine elements from several sources.
  3. **Indirect parallels** — borrow from other domains solving a similar problem (Netflix recommendations → content suggestions).
  4. **Metaphors/analogies** — real-world concepts (physical library → content organization).
  5. **True innovation** — new pattern from first principles (rare, expensive; reserve for core differentiating JTBD).
- Sources — usual suspects: Dribbble, Behance, Awwwards, Pinterest. More interesting: ProductHunt (how startups differentiate), Layers.to, Footr.design (footer designs), Godly.website (landing pages), Pageflows.com (real user flows of popular apps), Teardowns.ai (AI-feature UI patterns).
- Document inspiration in one organized place (link/notes database, annotated screenshot page, shared moodboard); analyze each example's strengths/weaknesses and recurring patterns — don't just collect screenshots.
- **Prioritize inspiration matching your project's goals and constraints over flashy consumer apps**; look at adjacent domains (e.g. digital-asset managers for content-heavy UIs), not just direct competitors.

### Step 5 — Generate rapid ideas
- **Go wide first**: at least **6 distinct low-fidelity ideas in ~30 minutes**, no judging feasibility; include radical options next to safe ones; remix inspiration pieces.
- **Time-box ideation and stop when the timer ends**, even if you want to continue.
- Keep capture format consistent so ideas compare fairly (all sketched with the same black marker on stickies — consistent fidelity prevents polish bias).
- Involve a PM/engineer briefly for diverse viewpoints if possible.
- Then **select 1–2** ideas that are distinct from each other and aligned with goals; trust intuition.
- Variant that works (Soren Iverson): everyone deliberately designs a hilariously *bad* UI, then swaps and improves someone else's — surfaces great ideas.

### Step 6 — Enhance fidelity
- Choose *where* to raise fidelity: most important/most used parts first (main dashboard, primary flows, key CTAs); use progressive disclosure to keep complexity hidden until needed.
- Go deep on the chosen screens: color/typography/imagery per brand; legible type matching tone; hover states, transitions, subtle feedback animations; **replace placeholder content with realistic content** — real data surfaces design problems and makes prototypes honest.
- **Balance polish with speed: don't pixel-perfect while the overall direction is still open. Refine core content display before spending any time on intricate animations or background patterns.**
- Use a design system / basic component library (buttons, inputs, cards) for consistency and speed; reuse components from unshipped explorations.
- Review high-fidelity work early with engineering/product/leadership to catch feasibility issues.
- If bigger UX problems appear while polishing, **step back and diverge again** rather than sinking cost into a broken direction.

---

## Module 10 — Checklists for improving fidelity (referential; jump to what you need)

Seven aspects: 1 Component states · 2 Primary interactions · 3 Secondary interactions · 4 Content scalability · 5 System feedback · 6 User input · 7 Navigation. (Pages 101–200 cover 1–5; visual style is treated in its own later section.) Prerequisites: goals understood, low-fi wireframes exist, design tool ready.

### Component states
- Design **default, hover, active, disabled** for every interactive component; add product-specific states where needed (e.g. "processing" for async AI work) and **focus** states.
- Differentiate states with color, opacity, border, or shadow; keep the treatment consistent with the design system.
- Make state transitions smooth and responsive, never jarring.
- Test states across devices and screen sizes for clarity.
- Rules:
  - Use distinct, consistent cues per state — e.g. **darken button color by 10% on hover, same shift on every button**.
  - Provide hover states for **all** interactive elements (subtle background change on list rows signals clickability).
  - Disabled states must clearly read "not interactive": muted color + hover effect removed.
  - Use quick feedback animations of **200–300 ms** (e.g. slight scale on click) — short and purposeful, nothing decorative.
  - Same visual treatment for the same state across similar components (Create/Edit/Delete buttons match).
  - Maintain **sufficient contrast ratios between states** (check dark mode especially) for accessibility.
  - Implement clear keyboard **focus states** — a prominent outline/glow on the focused element.

### Primary interactions
- Identify the few actions that ARE the product per view (create, add, generate, share); everything else is secondary.
- Key interactions must be **immediately discoverable** in each view (prominent placement: top-right or floating action button for the main create action).
- Emphasize via **size, color, placement**; the most important button is larger, uses the brand primary color, and contrasts well with the background.
- Use recognizable affordances: button styles for clickable actions, "+" icon + text label, drag handles where items reorder.
- Rules:
  - Visual hierarchy follows importance (primary creation action ≫ settings).
  - Label + icon together reinforce purpose ("+ New Cluster").
  - Style all primary actions identically across the app (same color/size/style).
  - Weight prominence by **frequency of use** (Edit more prominent than Delete if used more).
  - Give **immediate visual feedback** on every primary action — loading state or progress indicator appears the instant the user clicks.

### Secondary interactions
- Secondary = less frequent, supporting actions. Balance discoverability with simplicity.
- **Progressively disclose** them: hide behind an Edit button, dropdown menu, hover reveal, or toggle so they never overwhelm the default view.
- Signal their presence with tooltips, icons, microcopy.
- Rules:
  - Group related secondary actions in a single menu (rename/move/delete in one dropdown).
  - Use one consistent overflow affordance everywhere (the "…" three-dot icon).
  - Secondary actions must never visually compete with primary actions.
  - Keep conventions consistent app-wide (gear = settings everywhere).
  - Access depth proportional to frequency/importance: rarely used → deeper in menus; occasional → one click away.

### Content scalability
- Design for both extremes: few items vs hundreds; short vs long text; decide explicitly what happens when content exceeds space (truncate with ellipsis vs wrap to a second line — per element).
- Define **breakpoints** and how the layout adapts mobile → tablet → desktop → widescreen.
- Maintain readability and hierarchy at every content scale (a generated summary must format well at one paragraph or several pages).
- Rules:
  - Use flexible layout (flexbox/grid); responsive column counts driven by screen size and content amount.
  - **Cap text line length at ~60–75 characters** with max-width for readability.
  - Provide explicit overflow mechanisms: truncation, pagination, or infinite scroll past a threshold.
  - **Test with realistic minimal AND extensive datasets** — the design must hold up in both.
  - Use **relative units (rem/em/%) not fixed px** so text scales with device and user preferences.
  - **Progressively load large datasets in chunks as the user scrolls** — a stated performance rule for content-heavy views; don't render everything at once.
  - Keep interactive elements **tap-friendly on mobile** even with long content (Edit/Delete stay usable, don't get crowded out by text).

### System feedback
- Feedback communicates results of actions and system status; effective feedback builds trust.
- Named surface types (choose deliberately by scope and urgency): **Alert, Toast message, Top banner, Modal, Bottom sheet, Inline alert.**
- Differentiate **global vs local**: top bar/toast for system-wide events ("Changes saved"), inline feedback next to the component for local events (form-field validation).
- Convey **urgency by severity**: critical errors = bold red + persistent modal (e.g. data loss); routine confirmations = subtle green checkmark that doesn't interrupt.
- Rules:
  - **Immediate feedback for every user action** (instant color change + loading indicator on click of any async action).
  - Consistent icon language: checkmark = success, exclamation = warning, everywhere.
  - Error messages more prominent and longer-lived than success messages.
  - **Never rely on color alone** — pair icons/patterns with color for color-blind users.
  - Error states must include **clear next steps** to resolve the issue, not just "something went wrong."
  - Progressive disclosure for complex feedback: short summary + "View details."
  - Make feedback contextual and specific to the task ("5 items moved to 'Research' cluster", not a generic "Done").

---

## Top rules from this unit

1. **Weigh information in this order: user research > customer familiarity > institutional best practices**, falling back up the chain when a level is missing. Research is the source of truth; familiarity (Jakob's Law) beats "optimal" patterns when you lack data; the scaffold (psychology, design systems, usability, a11y) is the fallback.
2. **Follow established conventions by default** — nav placement, familiar labels, standard patterns. Users prefer interfaces that behave like products they already use; breaking familiarity has a measured cost (Snapchat: −2% DAU, −$1.3B).
3. **Innovate only on patterns that serve a core JTBD in a saturated market; copy proven patterns everywhere else** (settings, profiles, auth). Pick your originality stage deliberately: copy → remix → parallel → metaphor → invention.
4. Write **2–3 JTBD statements** ("When [situation], I want [motivation], so I can [outcome]") before designing and test every screen against them — outcome-phrased, never feature-phrased. Assumption-based JTBD beat none.
5. **Aim for informed simplicity**: past Dribbble-simple, out the other side of informed complexity; if a dashboard or nav "never stops growing," you're stuck in the middle stage.
6. **Stop at "good enough" / critical mass** — design consumes all time offered and information-gathering hits diminishing returns; define good-enough for this decision, ship, learn.
7. **The order of design decisions determines the outcome** — same resources, different sequence, different product. For new builds: system → tasks → IA → inspiration → wide ideas → fidelity. Never start with visual polish.
8. **Design the most frequent, most important tasks first**; weight action prominence by frequency of use (Edit ≫ Delete).
9. **Label actions in plain words** — "Add Content", never "Initiate content ingestion process."
10. **Prioritize with position, size, and contrast**: one visually dominant primary action per view, styled identically app-wide; secondary actions progressively disclosed behind a consistent "…" affordance, never competing with the primary.
11. **Go wide before going deep**: ≥6 distinct low-fi concepts in ~30 time-boxed minutes, all at identical fidelity, then pick 1–2.
12. **Design all component states** — default, hover, active, disabled, keyboard focus (+ async "processing"). Every interactive element gets a hover state (e.g. darken 10%); disabled reads as dead; focus gets a prominent outline; state contrast meets accessibility ratios in both light and dark mode.
13. **Keep animation subtle and purposeful: 200–300 ms feedback transitions only** — animation is feedback, not decoration; refine core content before intricate animations or background effects.
14. **Cap text at ~60–75 characters per line** with max-width; use rem/em/% instead of fixed px so layouts scale with device and user preference; build layouts on flexbox/grid.
15. **Plan overflow explicitly** — truncation vs wrap decided per element; pagination or infinite scroll past a threshold; test every layout with both minimal and massive realistic datasets (lorem ipsum hides real failures).
16. **Load big data progressively in chunks; content-heavy pages must load fast; real-time data must update without lag** — performance is a stated design requirement, not an engineering afterthought.
17. **Give immediate feedback for every action**; global events in toast/banner, local events inline; critical errors persistent and prominent, routine confirmations subtle; error messages always state the fix.
18. **Never encode status in color alone** — pair with icons/patterns for color-blind users.
19. **Default rules are strong opinions loosely held**: override when research, brand, regulation, or technical constraints demand — but document the rationale and fold successful overrides back into the rulebook.
20. **Every micro design decision should trace to a company macro bet** (velocity, efficiency, accuracy, innovation); designing quickly is fine — designing quickly without intention is what's reckless.
