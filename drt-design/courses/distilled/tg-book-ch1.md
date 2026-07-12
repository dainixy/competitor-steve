# Making UX Decisions (Tommy Geoco) — Distilled, Part 1

**Covers:** book pages 1-100 of 603.
**Chapters in this range:** Front matter + full table of contents (pp. 1-11) · Module 1: Initiating the Warp Drive (pp. 12-21) · Module 2: Anchors (pp. 22-42) · Module 3: Introduction to Cluster [fictional case-study product] (pp. 43-50) · Module 4: Designing at Warp-Speed (pp. 51-68) · Module 5: Create an Information Scaffold (pp. 69-95) · Module 6: Stage Your Bets (starts p. 96, continues past p. 100).

---

## Book structure map (from the TOC, for the merge step)

Part 1 — Design Decisioning Framework: M1 intro · M2 anchors · M3 Cluster case study · M4 warp-speed rationale · M5 information scaffold · M6 stage your bets · M7 decisioning workflow · M8 default design rules intro.
Part 2 — Default Design Rules: M9 checklist for designing new interfaces (define system → model tasks → organize info → gather inspiration → rapid ideas → enhance fidelity) · M10 checklists for fidelity (component states, interactions, content scalability, system feedback, user input, navigation) · M11 checklists for visual style (spacing, colors, elevation, iconography, typography, imagery, motion, texture) · M12 innovating (5-level originality spectrum) · M13-M24 pattern catalogs (chunking, progressive disclosure, cognitive load, visual hierarchy, social proof, feedback/visibility, error prevention, accessibility, personalization, onboarding, information relationships, wayfinding/navigation) · M25 growth.

---

## Module 1: Framing — the point of divergence

The book answers "what do I do next?" once you have all knowable information and start focused work. It is about UI decisions AFTER research is gathered — not a substitute for user research.

- As soon as you start designing, three things are true: the clock is ticking, knowable information is fixed, and an optimal path exists hidden in plain view.
- Cost of deciding slowly: you become the bottleneck, competitors outpace you, the team loses trust.
- The four deliverables of the method: (1) rules that automate recurring decisions, (2) a framework for new decisions, (3) step-by-step checklists for executing decisions, (4) a catalog of reusable UI patterns.

## Module 2: The 7 Anchors (named principles, one line each)

Mostly mindset material — captured briefly. The anchors are mental models to return to under pressure:

1. **Pursue your purpose** — evaluate features/projects against the product's core purpose; choose the design that best serves the core purpose even if it's less visually striking.
2. **Marathon mindset** — prefer a phased release over shipping a half-baked feature; when tempted by a quick-but-limiting technical solution, weigh short-term benefit vs. long-term scalability and schedule the refactor explicitly.
3. **Be intentional** — define the objective before starting any task; time-box research to avoid rabbit holes; say "enough" when you have sufficient information to move.
4. **Embrace your unique perspective** — propose unconventional solutions with rationale + a small-scale test, not as opinion.
5. **Just-in-time learning** — learn only what the current task needs; apply immediately; keep a reference/checklist of what you learned (e.g., a checklist of new accessibility requirements).
6. **Challenge assumptions** — assumption-map at project start and prioritize which need validation; use "five whys"; test with quick prototypes/A-B tests; look for data that contradicts your expectations.
7. **Two truths exist** (dialectical thinking) — speed AND quality: split a feature into core (ship fast) + enhancements (iterate); innovation AND familiarity: use familiar elements in a new way, roll out innovations progressively.

Concrete rules worth keeping from the examples:
- Against feature creep: use a criteria-based system for evaluating new feature ideas and a "one in, one out" backlog policy.
- Before adopting a new tool: define specific criteria it must meet, run a bounded trial, judge against the criteria.

## Module 3: Cluster (context only)

"Cluster" is the book's fictional B2B content-production tool used for all exercises. No rules here — just note that later examples reference it.

## Module 4: Designing at Warp-Speed — when to move fast

### When to design at warp-speed (conditions favoring speed)
- **Big new opportunity:** large market with no dominant leader, or a technology disruption incumbents can't capture.
- **First-scaler advantage:** being first to SCALE beats being first to market (network effects, returns to data, economies of scale — e.g., Amazon/Yahoo failed vs. eBay's network effects).
- **Competition:** if someone else can realize the opportunity sooner, moving faster reduces risk. Competition is global.
- **Pre product-market fit:** limited runway to validate fit.

### When to design like a mine-sweeper (slow, careful)
- Risk to humans: harm/mortality (medical), critical systems (security), infrastructure.
- Risk to market positioning: growth outpacing ability to deliver value; positioning into the wrong segment of a regulated/legacy supply chain.

### Eisenhower Design Matrix (clarity × risk → pace) — use this to pick speed
| Condition | Decision |
|---|---|
| High clarity, low risk | Warp-speed on research AND craft; measure and iterate on higher-fidelity ideas |
| High clarity, high risk | Mine-sweep the research, then warp-speed the craft; use tangibles to uncover new risks |
| Low clarity, high risk | Mine-sweeper pace on research BEFORE crafting anything tangible |
| Low clarity, low risk | Warp-speed everything; measure and iterate as much as possible |

### Quality of a fast decision (definition)
A good warp-speed design decision is measured by:
1. How well it references systems and knowledge (heuristics, psychology, existing patterns)
2. How well it competes in the market
3. How well it satisfies user jobs-to-be-done

Key insight: a product can be "objectively well-designed" yet built from strategically poor decisions (ignoring competitors, chasing trivial feedback instead of one primary value driver, ignoring psychology). The path to the decision justifies or undermines it.

- Efficient decisions are: fast, intentional, resourceful.
- Costly decisions are: overthought, uninformed, Pareto-violating.
- **Pareto rule for design:** ~80% of business impact comes from ~20% of design decisions — many decisions you agonize over are not worth the time.

### 3 pillars of warp-speed decisioning
1. **Scaffolding** — rules that automate recurring decisions.
2. **Decisioning** — the process for making new decisions.
3. **Crafting** — checklists for executing decisions.

### StreamPro case study (worked example of the method)
- Round 1 (speed-to-market MVP in 12 weeks): used first-order references for guidelines; designed workflows similar to the leading competitor; used UI patterns from an existing framework. Result: fast adoption, but copycat competitors → churn.
- Round 2 (speed-to-precision): bet everything on ONE differentiator (WYSIWYG editor). To make an unfamiliar pattern learnable, borrowed a metaphor users already knew (Photoshop) per **Jakob's Law** — imported its text styling/alignment controls, grids + rulers + snap-to-grid, grouped property labels (chunking), and z-index "move forward/backward."
- To reduce redesign friction for existing users, applied psychology deliberately: instant feedback in the editor (Goal-Gradient Effect), kept the old widget-selection flow (Familiarity Bias), trusted invested users to push through initial friction (Sunk Cost), made the end result impressive (Peak-End Rule).
- Takeaway procedure for introducing a novel UI: (1) find a tool your users already know that solves an analogous problem, (2) copy its interaction vocabulary, (3) keep everything else identical to what users had before, (4) make feedback instant and the end state rewarding.

## Module 5: Create an Information Scaffold (the core reference toolkit)

**Rule: start every project with an information scaffold, not a UI kit.** Most of a UI kit gets discarded; designers reduce it to foundations (rules, grid, type) anyway. A scaffold = deliberately collected principles, psychology, and pattern references that inform your designs.

Scaffold's three purposes: (1) starting point for new projects, (2) at-a-glance reference for fundamentals, (3) light enough to evolve. Replace parts with project-specific assets (e.g., the company's design system) when they exist.

The 10 scaffold components: Atomic Design principles · Nielsen's usability principles · UX psychology reference · economics fundamentals · accessibility reference · grid & vertical rhythm · default typefaces · icon library · design system reference · default design rules.

### 5.1 Atomic Design (Brad Frost)
Five levels: **Atoms** (buttons, inputs, text) → **Molecules** (forms, menus) → **Organisms** (headers, footers) → **Templates** (page structure) → **Pages** (templates + real content).
Use it for: (1) defining reusable patterns when inspecting an interface (separate the popup from the cancel/save button group inside it), (2) transforming ideas — pinpointing an optimal pattern in another product and porting it into yours.

### 5.2 Nielsen's 10 usability heuristics (book's paraphrase — treat as guidelines, not strict rules)
1. **Keep users informed** — always show what's happening; give feedback within a reasonable time.
2. **Use familiar language** — users' words, not technical terms; follow real-world conventions.
3. **Give users control** — easy undo/redo; a clear exit from unwanted states.
4. **Be consistent** — same words/actions mean the same thing; follow platform conventions.
5. **Prevent errors** — design errors out, or confirm before destructive/mistake-prone actions.
6. **Make information easy to find** — don't force users to remember information across screens (recognition over recall).
7. **Be efficient** — shortcuts/customization for experts while staying easy for novices.
8. **Keep the design simple** — only necessary information; no clutter of needless detail.
9. **Help users fix errors** — error messages that state the problem plainly and suggest a solution.
10. **Provide help** — searchable, task-focused documentation when needed.

When to use: during ideation (structure/layout decisions) and as an evaluation checklist when an interface underperforms (e.g., users stuck → check "visibility of system status").

### 5.3 Design psychology reference (full table — each is a decision tool; categories: Filtering = information overload, Sense-making = assigning meaning, Recall = memory, Efficiency = acting fast)

| Principle | One-line definition | Category |
|---|---|---|
| Aesthetic-Usability Effect | Attractive products are perceived as more usable on first impression (even when not) | Filtering |
| Anchoring | People fixate on the first impression/piece of information | Filtering |
| Banner Blindness | Users ignore elements that look like ads | Filtering |
| Center-Stage Effect | More attention goes to centered content | Filtering |
| Cognitive Load | Effort required to process and understand information | Filtering |
| Decision Fatigue | Decision quality drops after extended decision-making | Efficiency |
| Decoy Effect | A third, less attractive option steers choice between two others | Filtering |
| Default Bias | Users stick with the default option | Efficiency |
| Discoverability | Ease of finding and learning features | Efficiency |
| Doherty Threshold | The point of frustration with a slow product (keep response fast) | Efficiency |
| Fitts's Law | Time to hit a target depends on its distance and size | Filtering |
| Fresh Start Effect | People make progress when starting from a clean slate | Sense-making |
| Goal-Gradient Effect | Motivation increases as the goal gets closer | Sense-making |
| Hick's Law | More options = harder decisions | Filtering |
| Hyperbolic Discounting | Immediate rewards valued over future rewards | Efficiency |
| IKEA Effect | People value what they helped create | Efficiency |
| Investment Loops | Users engage more with things they've invested time in | Efficiency |
| Jakob's Law | Users expect your product to work like the products they already use | Sense-making |
| Law of Common Region | Items inside the same visual boundary are seen as related | Sense-making |
| Law of Prägnanz | Simpler shapes/objects are processed more easily | Sense-making |
| Law of Proximity | Items close together are perceived as related | Filtering |
| Law of Similarity | Visually similar elements are perceived as related | Sense-making |
| Law of Uniform Connectedness | Elements linked by a visual element are perceived as related | Sense-making |
| Miller's Law | ~7 items max in short-term memory | Recall |
| Nudging | Subtle cues steer behavior in a desired direction | Filtering |
| Occam's Razor | Prefer the simplest explanation/solution | Sense-making |
| Pareto Principle | 80% of effects from 20% of inputs | Efficiency |
| Parkinson's Law | Work expands to fill the time allocated | Efficiency |
| Peak-End Rule | Experiences are judged by their most intense point and their ending | Recall |
| Picture Superiority Effect | Visual information is remembered better than text | Recall |
| Planning Fallacy | We underestimate time and resources needed | Efficiency |
| Priming | Prior cues influence decisions | Filtering |
| Progressive Disclosure | Reveal information gradually as needed | Filtering |
| Second-Order Effect | Every consequence has a subsequent consequence | Efficiency |
| Serial Position Effect | First and last items are most memorable | Recall |
| Social Proof | People conform to observed behavior | Sense-making |
| Sunk Cost Effect | Continued investment despite poor returns | Efficiency |
| Tesler's Law | Complexity can't be removed, only moved; a more complex system supports fewer features well | Filtering |
| Von Restorff Effect | The item that stands out is remembered | Filtering |
| Weber's Law | Big changes are noticeable; small ones aren't | Efficiency |
| Zeigarnik Effect | Unfinished tasks are remembered better than finished ones | Recall |

Usage examples given: Peak-End Rule → design the final step of a flow (publishing) to feel great; Zeigarnik → structure task lists so open items pull users back; Goal-Gradient → progress indicators accelerate completion.

### 5.4 Economics fundamentals (microeconomics literacy for judging design speed/priorities)
- **Economies of scale** — per-unit cost falls with volume; feature cost is spread across all customers.
- **Opportunity cost** — every choice forfeits the next-best alternative.
- **Time value of money** — money now > money later.
- **Supply and demand** — scarcity + desire set price.
- **Zero marginal cost of production** — software copies cost ~nothing; once built, distribution is free.
- **Network effects** — value grows with each additional user.
- **Diseconomies of scale** — too big = coordination costs rise, efficiency falls.
- **Economies of scope** — cheaper to build multiple products on shared tools/frameworks.
- **Veblen goods** — some products sell more at higher prices (premium positioning).
- **The invisible hand** — markets self-select winners; users pick the best apps.

### 5.5 Accessibility reference — POUR (WCAG's four founding principles)
- **Perceivable:** text alternatives for non-text content; captions/transcripts for multimedia; users can change content presentation; content easy to see and hear.
- **Operable:** everything works from a keyboard; users have enough time to read/use content; nothing causes seizures or physical reactions; easy navigation and findability; support input modalities beyond keyboard.
- **Understandable:** text and UI readable and understandable; UI appears and operates predictably; help users avoid and correct mistakes.
- **Robust:** compatible with different browsers and assistive technologies; markup should be valid.
Note: accessibility can't be achieved by design alone (needs engineering), but design leads the way. Deeper refs cited: WCAG 2.1 spec, overlayfactsheet.com (why a11y overlay widgets are a bad idea), hidde.blog/common-a11y-issues.

### 5.6 Default typefaces (scaffold rule: decide once, stop thinking about it)
- **Select ONE typeface** to start: a neutral sans-serif — system messages, labels, and data must be legible first; add personality to headings later. Recommended free/system faces that scale well across screen sizes: **Inter, Nunito Sans, Mona Sans, SF Pro, Segoe UI**.
- **Start with a 16px base font size** — it's the default in most browsers (also good for perf/zoom behavior).
- **Choose a modular or custom type scale.** Modular scales compute sizes from a fixed ratio (online calculators exist). The book's provided custom scale: **12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72 px**.
- Swapping typefaces/scale later is cheap — don't agonize at the start.

### 5.7 Icon library
Choose ONE versatile library for system indicators (tooltips, arrows) and labels (Dashboard, Settings). If the product already has a library, use that instead. Recommended: **Atlas Icons, Font Awesome, SF Symbols, Myicons**. Criteria: covers your domain's symbols, wide range, consistent style.

### 5.8 Design system reference
Reference mature public design systems (Google Material, Apple HIG, etc. — chosen because they serve the most-used products, are maintained by mature teams, and have great documentation). Two benefits: (1) match the UI language of popular products your customers already use, (2) leverage their thoughtful research. Use them during decisioning to inventory how noteworthy systems handle a specific pattern — as one input among several, not gospel.

### 5.9 Default design rules (your personal design system)
Your default rules are **acknowledged biases** about visual and interaction patterns — "strong opinions loosely held." Goal: fast, informed, flexible. Acknowledging biases lets you (1) use them competitively, (2) change them with new information.

Example defaults (the book's own):
- **Element placement:** "Confirm" button on the right, "Cancel" on the left.
- **Workflow actions:** default to CRUD (Create/Read/Update/Delete) as the important actions for data tables.
- **Information architecture:** consistent nav groups — "Product" (feature entry points), "User" (account management), "System" (search, notifications).

Example overrides (loosely held):
- PM says the product places Confirm on the left everywhere → follow existing pattern for consistency.
- Research shows users duplicate rows in high volume → promote that "secondary" action to visible.
- Many features have inner-page navigation → create a new "Contextual" nav category.

**Precedence order:** established design system > your default rules; default rules are the FIRST reference checked and the EASIEST to override when user/product data challenges them.
Three maintenance actions: create a new rule (decide once + document the pattern), override a rule (when defending it creates costly circular debate), update a rule (with new information; possibly per-product-type).

## Module 6 (start): Stage Your Bets

You make 20-30 UI micro-decisions a day. When a debate (with yourself or your team) about one of them stalls, the debate's cost starts to exceed its value. "Staging your bets" = framing every UI decision as "how important is this to the company's plan to win the market?" — then deciding intentionally.

Hierarchy: Company plan → Product → Design decisions. Know your industry and competitors.

### Decision flow for any contested UI decision
1. Is this UI pattern critical to the company's plan for the market?
   - **Yes** → does the cost of debating outweigh its value?
     - Yes → choose the simplest path to a decision.
     - No → decide with collective knowledge + scaffold + available research; choose the simplest path and let user feedback drive the final decision.
   - **No** → choose the simplest solution — including whichever belongs to the strongest opinion in the room — and move on to more important decisions.

### Pre-work (4 steps, detailed after p. 100)
1. Analyze your industry · 2. Analyze competitors · 3. Define customer goals · 4. Name your bets.
Shortcut: you can often get this by interviewing people in the org. Questions checklist: What is the product's goal? What was tried before and failed? What do we want to learn? What trade-offs / opportunity costs? What products already accomplish this goal? Who will we compete with soon? What's our business model? Primary vs. secondary customers? What's our competitive advantage / unique position? What could kill this product? Could we hit the goal with reduced size and scope? How often will we iterate?

---

## Top rules from this unit

1. **Start with an information scaffold, not a UI kit** — collect principles, psychology, and pattern references once; most of a UI kit gets thrown away.
2. **Pareto for design: ~80% of business impact comes from ~20% of design decisions** — identify the 20% and stop agonizing over the rest.
3. **Pick pace with the clarity×risk matrix:** high clarity + low risk → ship fast and measure; low clarity + high risk → research before crafting anything; high clarity + high risk → careful research, then fast craft.
4. **Judge a fast decision by three tests:** does it reference known systems/heuristics, does it compete in the market, does it satisfy the user's job-to-be-done — the path to the decision justifies it.
5. **Use Jakob's Law to introduce anything novel:** borrow the interaction vocabulary of a tool your users already know (StreamPro copied Photoshop's rulers, snap-to-grid, grouped properties, z-index controls).
6. **When redesigning for existing users, keep one familiar anchor flow unchanged**, give instant feedback, and make the end state rewarding (Familiarity Bias + Goal-Gradient + Peak-End).
7. **Decide typography once at project start:** ONE neutral sans-serif (Inter/Nunito Sans/Mona Sans/SF Pro/Segoe UI), 16px base (browser default), a fixed scale (12/14/16/18/20/24/30/36/48/60/72px) — then stop thinking about it.
8. **Choose ONE icon library** for indicators and labels; inherit the product's existing one if present.
9. **Follow Hick's Law and Nielsen #8:** fewer options, only necessary information, no clutter — simplicity is a measurable usability property, not a style.
10. **Recognition over recall:** never force users to remember information from one screen to another.
11. **Prevent errors first, explain them second:** confirm before destructive actions; error messages must state the problem and suggest the fix.
12. **Respect the Doherty Threshold:** slow products frustrate — speed of response is a UX feature, not an infra detail.
13. **POUR is the accessibility floor:** text alternatives, full keyboard operability, predictable behavior, valid markup compatible with assistive tech.
14. **Group by geometry:** proximity, common region, similarity, and uniform connectedness are how users infer relationships — use whitespace and boundaries instead of decorative dividers.
15. **Maintain default design rules as documented, overridable biases** (Confirm right/Cancel left, CRUD table actions, Product/User/System nav groups); an established design system always outranks them; product data overrides both.
16. **Stage your bets:** if a UI decision isn't critical to the company's market plan, take the simplest solution (even the loudest person's) and move on; if it is critical, decide with scaffold + research and let user feedback finalize.
17. **Cap decision debates:** the value of a pattern debate is undermined by the clock — when it stalls, choose the simplest path to a decision.
18. **Bet on one primary value driver, not trivial feedback requests** — copycat parity gets you to market; a single sharp differentiator keeps you there.
19. **Reference mature public design systems** (Google/Apple-grade) to match the UI language users already know and inherit their research for free.
20. **Time-box research and say "enough":** define the questions first, set time limits, and move when you can act — uncertainty is resolved by shipping and measuring, not more deliberation (when risk is low).
