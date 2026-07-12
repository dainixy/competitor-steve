# Process Masterclass (Nguyen Le) — Module 2: Design Execution

Source: all PDFs in `02-Module 02. Design Execution` (lesson decks + one-page lesson summaries). Lessons: Overview → 01 Structure & Hierarchy → 02 Styleboards & Moodboards → 03 Grids → 04 Typography → 05 Visual Design Concepts → 06 Prototyping → 07 Putting It All Together → 08 Design Systems.

Note on depth: the decks in this module are sparse (one statement per slide); the fine-grained demos live in the companion videos. Everything below is what the PDFs actually contain, distilled into rules.

---

## Overview — the execution mindset

- Pair high-level thinking (design thinking, strategy) with great execution. The combination — not either alone — is what makes design work valuable.
- "God is in the details." Treat detail-level craft (spacing, alignment, type) as the substance of quality, not polish added at the end.
- "Be a yardstick of quality. Some people aren't used to an environment where excellence is expected." (Steve Jobs) — set the quality bar deliberately and hold it.
- There is no magic pill for craft. Two levers only:
  1. **Develop a good eye** — surround yourself with great work and great people; study work better than yours.
  2. **Put in the reps** — gym analogy: ability builds through repetitions (learning → practice → application). Close the distance to designers you admire through volume of practice.
- These are simple concepts, not easy ones. Expect mastery to take hundreds to thousands of hours.

---

## 01. Structure & Hierarchy (information architecture first)

Order of operations: structure the content BEFORE styling anything.

- Organize content in a logical way users can understand — information architecture, wireframes, and user flows come before visual design.
- Organize content so it **tells a story**: sequence sections in the order the user needs to hear them.
- Lay out content based on **top-priority user goals** and the user stories you defined earlier — the most important goal earns the most prominent placement.
- Check the layout against **business objectives** as well as user goals; the page must serve both.
- Deliverables at this stage: site map, user flows, page structure (wireframes).
- Tools named: Whimsical, UXPin, Figma, Axure.

Decision rule: if you cannot justify an element's position by pointing to a user goal or business objective, its position (or the element) is wrong.

---

## 02. Styleboards & Moodboards (cheap direction-testing before committing)

Definitions:
- **Moodboard** = a collection of references (images, videos) that capture the *essence* of the end result you want. Broad.
- **Styleboard** = displays look-and-feel at a **more detailed level** than a moodboard (closer to real UI: type, color, components applied). Specific.

When to use which:
- Use a **moodboard** when you need to communicate visual direction in a **broader sense** (early, exploring territory).
- Use a **styleboard** when you need to get **more detailed and specific** (narrowing to one direction).

Why bother (the economics):
- Boards let you **explore multiple directions without committing much time to each concept** — much shorter than building a full design concept per direction.
- They are the quick, efficient way to communicate ideas and art direction to a client/stakeholder.
- They give the client **input early**, which builds a sense of collaboration and ownership — buy-in through involvement rather than a big reveal.
- Speed compounds: you're slow at first, but each board you make gets faster. Keep making them.

Workflow rule: never build a full high-fidelity concept just to test a visual direction. Board it first, get a reaction, then invest.

---

## 03. Grids (order, consistency, rhythm)

Why grids:
- A grid is a tool for creating **order & consistency**.
- It streamlines the process by **creating a system you can follow** — decisions are made once, then reused.
- Other collaborating designers (and developers) can use the same system, keeping the output consistent across people.
- Grids promote structure and hierarchy, which **helps users scan and digest information more easily**.
- The payoff is "crispness and rhythm you can't quite put your finger on" — the thing that makes a layout feel *just right*. Alignment discipline is felt even when not consciously seen.

Grid anatomy covered:
- **Columns** — vertical divisions that text/UI blocks align to.
- **Baseline grid** — horizontal rhythm; text baselines land on a repeating increment so vertical spacing stays consistent.
- The lesson distinguishes **building** a grid system (define columns, gutters, margins, baseline once) from **using** it (snap all layout decisions to it thereafter).

Practice sequence prescribed: first practice grid layouts with **typography and imagery only**, then apply the grid to **UI design**. Merging editorial-grid thinking with UI thinking is presented as the path to exceptional work.

Further reading named: *Grid Systems* (Josef Müller-Brockmann, graphic-design classic).

Working rules:
- Define the grid before designing screens; never place elements ad hoc.
- Every element aligns to a column edge; every text baseline sits on the baseline grid.
- When something feels "off" but you can't say why, check grid/baseline alignment first.

---

## 04. Typography 101 (the biggest lesson in the module)

### Serif classification (know these 4 — each carries a mood)
Serifs = typefaces with "feet." Sub-classes by age and stroke contrast:

| Class | Example | Traits / feel |
|---|---|---|
| **Old Style** | Minion Pro | Dates to mid-1400s; low contrast; feels "old school," bookish, classic (editorial/travel demo: "Venice") |
| **Transitional** | Baskerville | Mid-1700s; visible thick-&-thin strokes; refined, literary |
| **Modern (Didone)** | Didot | Late-1700s; **pronounced** thick-&-thin contrast; high fashion / luxury (demo: Dior) |
| **Slab** | Rockwell | **No contrast** between thick & thin; rectangular serifs; loud, sturdy, sporty (demo: sports magazine "IT'S A FOUL") |

Use the class, not just the font: pick Old Style/Transitional for long-form credibility, Modern for fashion/luxury display, Slab for bold editorial impact.

### Sans-serif classification (know these 4)
"Sans" = "without" in French — without serifs.

| Class | Example | Traits / feel |
|---|---|---|
| **Grotesque** | Akkurat | A bit more character/quirk than neo-grotesque |
| **Neo-Grotesque** | Helvetica Neue | Plainer, more neutral appearance; the "invisible" workhorse (demo channels Massimo Vignelli — simplicity, swissness, execution) |
| **Humanist** | Lucida Grande | Carries characteristics of serif letterforms ("I'm more like a serif a") — warmer, very legible |
| **Geometric** | Futura | Letterforms built from geometric shapes ("I'm more like a shape") — modern, constructed (demo: 1969 "MOON" poster) |

(Reference credited: Ellen Lupton.)

Selection rule: neutral product UI → neo-grotesque or humanist; warmth/legibility at small sizes → humanist; branded/display moments → geometric or a serif class that matches the brand's era/feel.

### Weights, widths, styles
- Weight families follow the **Univers numbering** model: 45 Light, 55 Roman, 65 Bold, 75 Black, 85 Extra Black — a typeface is a *system* of weights, not one file. Pick a family with enough weights to build hierarchy.
- **Condensed** cuts (e.g., Univers Ultra Condensed Thin/Light/Roman) exist for tight horizontal space — a width axis on top of the weight axis.
- **Italic vs Oblique**: italic = a distinct drawn letterform (serif tradition); oblique = the upright form slanted (sans tradition). **Small caps** = capital letterforms at lowercase height — use for labels/meta text (the decks use small caps for captions like "WRITTEN BY", "PHOTOGRAPHY BY").

### Tracking (letterspacing)
- Wide tracking (`T R A C K I N G`) = airy, formal, label-like — works for small all-caps labels.
- Tight tracking on big bold display type = dense, punchy.
- Default body text: keep tracking normal ("keeping it legit") — don't letterspace lowercase body copy.

### Alignment
Four options: **left, center, right, justified** — and the deck immediately re-shows all four sitting on the column grid and baseline grid: alignment choices must be verified against the grid, not eyeballed.
- Left-aligned ragged-right is the demonstrated default for body copy columns.
- Center/right/justified are deliberate, occasional choices (the justified demo shows the stretched word-spacing it produces).

### Demonstrated pairing pattern
Throughout the deck: one display face for the headline + small-caps meta line + modest body text, on a strict grid, mostly black-on-white with a single red accent. That restraint — one or two typefaces, hierarchy via size/weight/caps, almost no color — is the module's implicit typographic recipe.

---

## 05. Visual Design Concepts

- The lesson is a set of base concepts to "bounce off and explore further" — the transferable instruction is the practice regimen:
  - **Always make time to play as a designer. Make things to learn.**
  - Mastery of craft is forged through **hundreds to thousands of hours** of practice; the more you make, the better you become.
  - Start side projects specifically to exercise concepts you haven't used in client work.
- Develop taste by studying "masters" — named influences for visual concepts include Jessica Walsh, Paula Scher, and indie creators like Beth Wilkinson and Tina Smith.
- Notable claim: there are **no UI/UX "masters" yet** — the industry is too young and changes too fast. Corollary: pull craft lessons from graphic-design masters (grids, type, hierarchy) and apply them to UI.

---

## 06. Prototyping

What prototypes are for:
- Testing **micro-interactions**, **user flows**, and **how something feels** — with the ability to test with **real users**.
- Building something quickly to get **immediate feedback** → iterate in small increments and **recognize pitfalls early**, before expensive build-out.
- **Communicating complex ideas to clients** — a prototype explains an interaction better than a static comp or a paragraph.
- Key line: a prototype determines how something **"feels," not just how it looks**. If a decision is about feel (timing, response, transition), you cannot judge it from a static mock.

Tool named: Principle (course files ship as Principle prototypes).

Decision rule: prototype the risky/novel interactions; don't prototype what standard patterns already prove.

---

## 07–08. Putting It All Together & Design Systems

- The closing lessons walk the full Vespi case-study project applying every principle in sequence: structure/hierarchy → boards → grid → typography → visual concepts → prototype → **design system**.
- A design system is the end state of execution discipline: the grid, type scale, and components codified so the consistency survives beyond one screen and one designer.
- Explicit claim: **the process principles remain the same regardless of project type** (responsive website vs. SaaS mobile app, different audiences and goals — same process). Don't reinvent process per project; re-run the same sequence with new inputs.

---

## Top rules from this unit

1. Structure before style: define information architecture, flows, and wireframes before any visual design.
2. Position every element by a top-priority user goal or a business objective; if you can't name one, the layout is wrong.
3. Organize page content to tell a story — sequence sections in the order the user needs them.
4. Test visual directions with moodboards (broad) and styleboards (detailed) before building any full concept; boards cost a fraction of a comp and earn early stakeholder buy-in.
5. Use a moodboard to communicate broad direction; switch to a styleboard when the conversation needs detail and specificity.
6. Build a grid system once (columns + baseline), then snap every layout decision to it — order, consistency, and scan-ability come from the system, not from taste in the moment.
7. Share the grid system with collaborators; consistency across people requires a shared system, not shared intentions.
8. When a layout feels vaguely "off," audit grid and baseline alignment first — rhythm is felt before it is seen.
9. Practice grids on pure typography/imagery layouts, then carry that editorial discipline into UI.
10. Know the four serif classes (Old Style, Transitional, Modern, Slab) and four sans classes (Grotesque, Neo-Grotesque, Humanist, Geometric) and pick by the mood each class carries — era and stroke contrast are the signal.
11. For neutral product UI default to neo-grotesque/humanist sans; reserve high-contrast Modern serifs for luxury/display and slabs for loud editorial moments.
12. Choose typefaces as weight systems (Light→Black, à la Univers 45–85); build hierarchy from size + weight + small caps within one or two families instead of adding more fonts.
13. Use small caps (or spaced all-caps) for meta labels; keep body-copy tracking normal; left-align body text by default and treat center/right/justified as deliberate exceptions verified on the grid.
14. Prototype anything whose success depends on feel — micro-interactions, flows, timing — and put it in front of real users; static comps can't answer "how does it feel."
15. Use prototypes to catch pitfalls early and to explain complex interactions to stakeholders instead of describing them.
16. End every project by codifying grid, type, and components into a design system so the consistency outlives the first screens.
17. Run the same execution sequence on every project regardless of type (web, mobile, SaaS) — change the inputs, not the process.
18. Improve craft only two ways: develop the eye (study great work) and put in reps (hundreds to thousands of hours); schedule deliberate practice and side projects.
19. Details are the work, not the polish — hold a visibly high quality bar ("be a yardstick of quality").
20. Restraint is the demonstrated house style: 1–2 typefaces, strict grid, black/white plus one accent color — hierarchy through structure, not decoration.
