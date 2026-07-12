# Tommy Geoco — Making UX Decisions
## Checklist: Designing New Interfaces (6-step sequential process)

Source: `02-Checklists/01-Designing new Interfaces` (7 PDFs). A sequential process checklist: Define system → Model tasks → Organize information → Gather inspiration → Generate ideas → Enhance fidelity. Follow the steps IN ORDER — visual polish is deliberately the LAST step, after structure and flows are settled.

---

## 00 — Overview & prerequisites

Before designing anything, have these three things in hand:

1. **A one-page project brief** — problem statement, target users, business objectives, success metrics. If it doesn't exist, write it first.
2. **User research data OR documented assumptions** — a summary of interviews/surveys/analytics. If no research exists, explicitly write down your assumptions about the audience (from industry knowledge or competitive analysis) so they can be challenged later. Never design on unstated assumptions.
3. **A ready component library** — reusable UI components, icons, and assets set up before you start, to save time and keep the work consistent.

The six steps, in mandatory order:
1. Define the system (what it is, how data flows in/out)
2. Model user tasks (who, what jobs, what workflows)
3. Organize information (structure, navigation, priority)
4. Gather inspiration (best practices, avoid pitfalls)
5. Generate rapid ideas (wide, fast, then pick 1-2)
6. Enhance fidelity (polish, interaction, real content — last)

---

## 01 — Step 1: Define the system

Answer four questions before any layout work:

1. **What sort of system is it?** Web app / mobile app / desktop software / embedded system. Identify the technical constraints and capabilities of that platform up front (e.g. web must support multiple browsers; embedded has limited processing power).
2. **How do users input data?** Forms, voice, gestures, scanning, etc. Define security and validation requirements per input (password complexity, credit-card validation, sanitizing free-text fields).
3. **How does the system output information?** Tables, charts, maps, images, notifications, audio. **Define performance and scalability requirements for output up front** — e.g. a stock-trading interface must update prices in real time without lag. Performance is a Step-1 design requirement, not an afterthought.
4. **Through what device/platform will users interface?** Desktop browser, mobile, wearable, voice assistant — each has different strengths; account for device limits (e.g. smartwatch = tiny screen).

System-type tradeoffs (know which you're building for and design to its strengths):
- **Web apps**: any-device access, instant updates, easy cross-platform — but limited hardware access and can be slower than native. Design web UIs knowing speed is their known weakness — don't add weight.
- **Mobile apps**: fast, offline-capable, deep device integration (camera/GPS/push) — but need separate iOS/Android versions.
- **Desktop software**: full processing power, deep system access — but users must install updates.
- **Embedded systems**: simple task-specific functions — fixed hardware constraints.
- Spatial computing is its own category; see Apple's visionOS guidelines if relevant.

Best practices:
- Match the system type to the use case, not to preference (web app for a cross-device project tool; native app for offline/sensor-heavy needs like a running tracker).
- Match input methods to user context (voice for hands-busy quick notes; keyboard for complex forms). Support multiple input options where practical, for accessibility.

---

## 02 — Step 2: Model the user tasks

Do this BEFORE organizing screens — screens serve tasks, not the reverse.

1. **Define user types and permissions.** List every distinct user role and what each can create/edit/view (e.g. project manager = full CRUD; team member = update status + comment; client = view-only).
2. **Define jobs-to-be-done (JTBD), then the primary tasks that serve them.** For each task, write the step-by-step workflow and mark its **entry point, decision points, and endpoint** (e.g. JTBD "manage client projects" → task "Create a new project" → Select "New Project" > enter details > assign team > set timeline > confirm).
3. **Map CRUD explicitly.** For every key object, define how users create, read, update, and delete it, and the sequencing/granularity of those actions within flows.
4. **List the key data entities and their relationships** (Projects contain Tasks; Tasks assigned to Members; Projects belong to Clients). Entity relationships directly define the information architecture in Step 3.

Best practices:
- **Prioritize the most frequent and important tasks first** (e-commerce: browse/add-to-cart/checkout before account settings). Frequency × importance decides where design effort goes.
- **Use simple, clear language for tasks and labels.** "Add to Cart", never "Initiate item purchase process". Label buttons with plain verbs.
- **Validate task models with users** — usability-test prototypes to check flows match expectations and find friction points; don't trust the model untested.

---

## 03 — Step 3: Organize information

Information architecture before visuals:

1. **Define high-level categories/sections** (e.g. Home, Products, Cart, Account) and group content logically into subcategories.
2. **Rank content areas by importance** — an explicit hierarchy (Products outranks About Us). Map entity relationships (one-to-many, many-to-many) since they shape structure.
3. **Define primary vs secondary navigation.** Primary = main menu structure. Secondary = contextual/in-page navigation (e.g. filters by price/brand inside a category).
4. **Prioritize critical content and actions per page**, then use visual hierarchy to point at them: **prominent positioning, larger text sizes, and contrasting colors for high-priority content** (product page: details, price, "Add to Cart" get the emphasis).

Best practices:
- **Validate IA with card sorting or tree testing** — let users show you how they'd naturally group content; don't guess.
- **Follow established conventions.** Main nav at the top of the page; common labels like "Home" and "Contact". Meet expectations; don't innovate on navigation.
- **Give clear labels and signposts** — e.g. breadcrumbs showing location in hierarchy ("Home > Products > Electronics").

---

## 04 — Step 4: Gather design inspiration

1. **Deliberately choose your stage of originality** (a named 5-level ladder — pick a rung on purpose, don't drift):
   - **Direct copies** — replicate an existing pattern exactly (e.g. a competitor's solution).
   - **Remixes** — combine elements from multiple sources into a new design.
   - **Indirect parallels** — borrow from a different domain that solves a similar problem (Netflix catalog flow → digital book catalog).
   - **Metaphors/analogies** — real-world concepts inform the design (music player modeled on a physical stereo).
   - **True innovation** — new patterns from first principles. Highest risk; use only when justified.

2. **Inspiration sources** (beyond the usual Dribbble/Behance/Awwwards/Pinterest):
   - ProductHunt.com — how new startups differentiate
   - Layers.to — curated real product UI
   - Footr.design — best footer designs
   - Godly.website — top landing pages
   - Pageflows.com — recorded user flows of popular apps
   - Teardowns.ai — UI patterns used in AI features

3. **Document inspiration in an organized reference** — a database/board of links, screenshots, and annotated takeaways; moodboard to share with the team.

4. **Analyze, don't just collect**: note each example's strengths AND weaknesses; identify patterns repeated across multiple examples (repetition across products = probable best practice); note how you'd adapt or improve.

Best practices:
- **Filter inspiration by project goals and constraints** — for a B2B SaaS tool, study successful B2B apps, NOT flashy consumer apps. Flashiness that doesn't fit the job is explicitly a trap.
- **Look at adjacent domains, not just competitors** (e-learning platform → study how news publishers structure content-heavy pages).

---

## 05 — Step 5: Generate rapid ideas

Two-phase divergence → convergence, with numbers:

1. **Go wide.**
   - Brainstorm without judgment: **at least 6 distinct ideas in ~30 minutes**. Ignore feasibility at this stage.
   - Include radical options alongside safe ones (all-text interface, minimal-text visual interface, conversational interface) — extremes reveal what matters.
   - Remix elements from your inspiration collection into new combinations.
2. **Converge: select 1-2 ideas.**
   - Pick the most promising — trust intuition here.
   - The 1-2 you keep should be **distinct from each other**, not variants of one idea.

Best practices:
- **Hard time-limit the ideation session** — commit to stopping at 30 minutes even if you want to continue. Momentum beats overthinking.
- Involve stakeholders (PM, engineer) for diverse perspectives if possible.
- **Keep fidelity consistent across all sketches** (same medium, same style — e.g. all black-marker sticky notes) so ideas compare on merit, not on rendering quality.
- Technique worth stealing (Soren Iverson): have each person design an intentionally terrible UI for the task, then swap and improve each other's — forces novel ideas out.

---

## 06 — Step 6: Enhance the fidelity

Fidelity comes LAST, and selectively — not everywhere at once.

1. **Choose where to raise fidelity:**
   - Start with the most important/most-used parts (main dashboard, primary flows).
   - Prioritize areas with the greatest impact on user understanding (key CTAs, data-table interactions).
   - **Use progressive disclosure** — ship a simplified view first; let users expand into advanced actions/content as needed. Don't front-load complexity.
2. **Go deep on the chosen screens:**
   - Add color, typography, imagery per brand guidelines. **Use color to highlight important elements** (color = hierarchy tool, not decoration). **Choose typography for legibility and tone-match.**
   - Interaction states: hover states, transitions, and animations that give **feedback and orientation** — subtle animation guides the user; transitions between screens maintain context. That is their entire job; nothing decorative.
   - **Replace ALL placeholder content with realistic or real content** — real product names, descriptions, metrics, imagery. Realistic content surfaces design problems that lorem ipsum hides.

Best practices (restraint rules — capture these hard):
- **Balance polish with speed.** Do NOT perfect pixels while open questions remain about direction. Refine core content display and organization BEFORE spending any time on intricate animations or background patterns.
- **Use a design system / component library** (buttons, inputs, cards) to keep screens consistent and fast to build; reuse components from earlier ideas if no system exists.
- **Review high-fidelity designs with engineering early** to catch feasibility problems before investment.
- **Be willing to step back.** If testing the hi-fi prototype reveals a structural UX problem (e.g. users can't navigate the content organization), return to divergent exploration — do not respond to structural problems with more visual polish.

---

## Top rules from this unit

1. Follow the six steps in order: system → tasks → information → inspiration → ideas → fidelity. Visual polish is always last.
2. Before designing, write a one-page brief (problem, users, objectives, success metrics) and document your audience assumptions explicitly if no research exists.
3. Define performance requirements at Step 1 (system definition), not after — output that must be fast is a design constraint from day one.
4. Match input/output methods to user context and device limits; support multiple input options for accessibility where practical.
5. Model tasks as JTBD → primary tasks → step-by-step workflows with explicit entry points, decision points, and endpoints.
6. Map CRUD for every key entity and diagram entity relationships — they ARE the information architecture.
7. Spend design effort proportional to task frequency × importance; core flows (browse/cart/checkout-class tasks) before settings-class tasks.
8. Label with plain verbs: "Add to Cart", never "Initiate item purchase process".
9. Rank content areas in an explicit importance hierarchy per page, then express it with position, size, and color contrast — the only three emphasis tools named.
10. Follow navigation conventions: main nav at top, standard labels, breadcrumbs for location. Never innovate on navigation.
11. Validate IA with card sorting/tree testing and task flows with usability tests — models are hypotheses until users confirm them.
12. Choose your originality level deliberately from the 5-rung ladder (copy → remix → parallel → metaphor → innovation); true innovation is the exception, not the default.
13. Filter inspiration by fit: for business tools study successful business tools, not flashy consumer apps.
14. Ideate wide and fast: ≥6 distinct ideas in a hard-capped 30 minutes, then converge to 1-2 ideas that differ from each other.
15. Keep sketch fidelity uniform so ideas are compared on merit, not rendering quality.
16. Raise fidelity selectively — most-used screens and highest-impact elements first; use progressive disclosure instead of showing all complexity at once.
17. Color is a hierarchy tool (highlight what matters); typography is chosen for legibility first, tone second.
18. Animation exists only for feedback and orientation (hover states, context-preserving transitions) — keep it subtle; skip intricate animations and background patterns until core content/organization is right, and even then treat them as lowest priority.
19. Replace placeholder text with real content early — lorem ipsum hides layout and hierarchy failures.
20. If testing reveals a structural problem, go back to idea exploration; never answer a structure problem with more polish.
