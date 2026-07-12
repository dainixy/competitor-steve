# Process Masterclass (Nguyen Le) — Module 2 Transcript Delta

Source: spoken-word transcripts for Overview, Structure & Hierarchy, Styleboards/Moodboards, Grids, Typography, Visual Design Concepts. Cross-referenced against `nl-module2-design-execution.md` (already captures the PDF/slide content). Only material NOT already in that file is kept here — worked examples, concrete numbers, decision rules, and reasoning spoken aloud that never made it onto a slide.

---

## 01. Overview

No delta. The spoken narration matches the PDF summary almost verbatim (Steve Jobs quote, "develop a good eye" + "put in the reps," 10,000-hours framing). Nothing new.

---

## 02. Structure & Hierarchy — the richest video, mostly net-new

### Before opening any tool: paper notebook first
- Before Whimsical/Figma/any digital tool, dump the project into a plain notebook: key ideas from discovery, business objectives, user-insight takeaways, and a rough low-fi block-out of sections (e.g., "make brand recognizable / product offering / lookbook / email / footer"). Purpose: it's faster than digital for synthesizing everything from discovery, and re-reading it later triggers the full context instantly.
- Rule: jot big ideas in a notebook on every project, then either share with the team or refer back to it while working in digital tools.

### Building the sitemap/IA — the actual method, step by step
1. Ask: **what are the top 5–10 tasks users want to perform?** (e.g., e-commerce: browse products, buy, check shipping cost; banking app: check balance, transfer money, check credit score.) Structure the IA around those first.
2. Match **language/vocabulary to the audience**: mass-market product → generic, widely-understood terms; a Gen-Z-targeted product (Snapchat-like) → different, terser language, less text overall.
3. **Group items the way users think**, not the way the org chart or catalog thinks — e.g., do users mentally split "shirts vs. tops" or "pants vs. jeans"? Get this from user research, don't guess internally.
4. **Identify edge cases last** and defer their optimization — e.g., "return a product after moving overseas." Get the top 5–10 tasks frictionless first; optimize edge cases once time/resources allow.
5. Treat the first IA as a **hypothesis**, then test/validate with real users — design is continual drafts, not a single pass.

### Two concrete sourcing methods for IA (when you don't know where to start)
- **If a product/site already exists**: audit its current structure and evolve it against the new user goals/business objectives — don't start from zero.
- **If nothing exists yet**: study competitor sites in the same category directly (demoed live against ASOS: how they split men's/women's, shop-by-brand vs. shop-by-product, breadcrumb structure) — "you don't always have to reinvent the wheel."
- Named tool for pattern research: **Mobbin (referred to in the transcript as "Moment/Moment Design")** — browse real, current screens from popular apps by app, by flow-pattern (login, onboarding, checkout), or by individual element (nav bars). Use it specifically to find **common design patterns** to reuse.
- Reasoning for reusing common patterns: the more products that use a pattern, the more users' expectations get calibrated to it (e.g., expecting bottom nav in a specific place) — reinventing standard patterns **adds cognitive load** and friction; don't do it without a real reason.

### User flows
- Think of IA "from the lens of the user" — not static pages, but the path from point A to point B, like a story.
- Concrete example walked through: a **purchase flow** built explicitly to hit named business objectives (increase sales, increase traffic, convert more users, showcase new art direction).
- **Design for every entry point, not just the homepage.** Users land via search, social, ads, direct links, or a lookbook — every standalone page must make sense on its own regardless of entry point. Map these conditionals explicitly when wireframing.
- Failed checkout → trigger an "abandoned cart" follow-up email ("we noticed you're having issues, how can we help?"). Successful checkout → trigger loyalty program / personalized discount / cross-sell flow.
- Post-purchase personalization example: "we noticed you bought a basic overcoat — this goes with desert boots, a watch, and a hat"; extend this into paid social retargeting and a personalized homepage greeting on return visits.
- Design **separate flows per persona/intent**, not one universal flow: a "hunter" (knows exactly what they want) needs a filter/search-driven flow; a "browser/window shopper" needs an inspiration flow (lookbooks, Instagram, YouTube campaign landing pages funneling into a lookbook archive).
- It's fine to build only a handful of flows (he shows 4–5) — flows exist to keep business objectives and user goals visible and to earn stakeholder buy-in, not to exhaustively cover every path.

### User stories
- Definition to use verbatim: a user story is functionality **from the user's point of view** — not "we'll have a dropdown," but "as a user, I want to check out."
- Structure: split into **primary actions** and **secondary actions**. Concrete scale from real projects: **10–20 primary actions**, and **50–100 secondary actions** — but the instruction is to focus design effort on the primary list, not chase completeness on the secondary one.
- Demo format for a user story: name a persona + a concrete intent + a constraint, e.g. *"As Jessica, I'm looking for a cashmere jacket around $200"* — then draw the literal flow (home → women's nav or direct category → listing → product → checkout) from that single sentence.
- **Scale the UI to the catalog size**: if the product range is only ~100 items (not thousands like ASOS), don't build a complex filtering system — cut it entirely. Match interface complexity to actual inventory size, not to what competitors with 10x the catalog do.

### Wireframing — the actual build sequence
- Design is **not linear/sequential** (IA → flow → wireframe). It's asynchronous — you can start with a wireframe and let it inform the IA, or start from a user story and uncover wireframe needs. Don't force a fixed order.
- When starting a wireframe: build the **navigation first**, then keep a running mental (or written) **inventory of what must appear on the page** to (a) let the user complete their task and (b) hit the business objective — write that inventory down before laying anything out.
- **Use real copy wherever possible; use lorem ipsum sparingly.** "Copy is part of design." Pull actual client copy into a doc and paste directly into wireframes rather than defaulting to filler text.
- Concrete UI decision rules demonstrated on a product-detail wireframe:
  - **Quantity selector**: if ~90%+ of users only ever buy quantity 1, default the field to 1; use a **dropdown** only while the realistic range is small (roughly up to ~4); beyond that, an **input box** is less friction than a long dropdown list.
  - **Size selector**: use **buttons**, not a dropdown, when the option count is small — buttons let the user see all choices (and in/out-of-stock state) at a glance without an extra tap; only fall back to a dropdown for long option lists.
- Mobile vs. desktop order: he does **both concurrently**, bouncing between them ("a couple of bits for mobile, then think how that looks on desktop, then back") rather than committing to strict mobile-first or desktop-first.
- Wireframes don't need to be pixel-perfect or centered — the point is only to convey structure; save precision for high-fidelity.

---

## 03. Styleboards & Moodboards — concrete document structure

### Moodboard doc anatomy (Figma template walked through live)
1. **Cover page**: concept name/ID, client/project name, prepared-by + date, and — critically — an explicit one-line **purpose statement** aimed at high-level stakeholders who'll only skim it, e.g. "The purpose of this document is an exploration of the visual identity and creative direction for [brand]." Also include: a live Figma link (so the board can keep updating after it's shared) and a list of project collaborators.
2. **Target audience** section — paste in the audience findings straight from discovery/user-insight work so the visual direction has a stated "why" attached to it.
3. **Visual direction** section — name the high-level thematic cues in plain adjectives (his example: "neutral, minimalistic, content- and typography-driven") with a short description under each.
4. **Reference grid** — branding, typography, imagery, UI examples pinned Pinterest-style; loose, not polished.
5. Use Figma's native **comments** for team annotation directly on the board (e.g., "get in touch with [X] to get brand notes") so designers/marketers/ops can collaborate in one place.
- Not limited to one page — add a dedicated page for just typography, just UI, etc., as the project needs.

### Styleboard = same idea, but you build the assets yourself
- Difference from a moodboard: a styleboard is not curated references — you **create the actual layout, typography, and imagery treatments** yourself, giving you real control over the specific look.
- Demonstrated 3-panel structure: (1) overall art direction / imagery, typeface choices spelled out by name (e.g., "New York Extra Large" headline + "San Francisco Pro Text" body) with lockups; (2) how that typography looks applied inside the actual app/site; (3) card UI + color palette + supporting motifs (illustration style, etc.).
- **Time-box it explicitly: a styleboard should take a few hours to one day**, not weeks — the entire point is to show direction before investing real design time.
- No fixed template/layout — he shows several past client styleboards (Luxy Hair, others) all structured completely differently. The only constant across all of them: color, typography, imagery, text lockups, iconography, and a couple of representative UI elements.
- A styleboard can (and should, when relevant) include **written personality/copywriting direction**, not just visuals — his real example line for a client: *"the simplicity and sophistication of Everlane meets the vibrant, positive, infectious personality of Luxy Hair."*
- A styleboard can also dictate **art direction for photography** (shot style/mood instructions for a photographer), not just UI.

---

## 04. Grids — concrete build specs (none of these numbers are in the PDF)

### Two grid systems, when to use which
- **12-column + baseline grid** → responsive web design / web-based products.
- **8px / 8pt grid** → web apps or anything with high information density (dashboards, complex interfaces, lots of information in a small space).

### Why exactly 12 columns
- 12 is divisible by 1, 2, 3, 4, and 6 → maximum layout flexibility.
- 12 is also the **Bootstrap grid** convention developers already expect — using it reduces dev handoff friction.

### Concrete numbers from the live Figma build (desktop 1440px artboard)
- Columns: 12.
- Margins: **~30–50px** (he sets 50) — his stated rule of thumb is "about 30 to 50," adjusted by judgment per project.
- Gutter: **~30px** (his choice) — "depends on how much spacing you want between elements."
- Baseline grid height: **derive it from body copy line-height ÷ 2.** His worked example: 24px line-height → **12px baseline unit**.

### Tablet and mobile adjustments (same session, same template)
- Tablet: keep 12 columns; reduce margin to **~20px**, gutter to **~15px**.
- Mobile: **drop to 4 columns** (12 is "too many to manage" on a small screen); margin **~25px**, gutter **~20px**.

### 8px/8pt grid build
- In Figma, just change the default row/column grid value from 10px → **8px**. That's the entire spec — no columns/margins/gutters layered on top the way the 12-col system has.
- Save every grid setup as a **reusable Figma style/template** so it doesn't get rebuilt from scratch per artboard.

### How to practice and use it (explicit exercise)
- Drill: from one base grid, generate **many different layout variations** (2-col, 3-col, 4-col splits, asymmetric splits) purely with typography/shapes — build a personal library of layout "moves" you can reach for later (his named examples: a stat-callout layout for a SaaS benefits section, an editorial grid for fashion lookbooks).
- **The grid is a guide, not gospel.** He explicitly shows an element placed off-grid on purpose, called it an "optical judgment... I made a decision as a designer that was visually and hierarchically the best choice." Snapping to grid is the default; breaking it is a deliberate, occasional call.
- Even in low-fidelity grid practice, prefer real copy over lorem ipsum — "copy is part of design," carried over from the Structure & Hierarchy lesson.

---

## 05. Typography — dense, mostly new beyond the PDF's classification tables

### Three top-level families, not two
- **Serif**, **sans-serif**, and **display**. Display typefaces are for headlines/decorative use **only — never body copy** ("try reading a whole book set in a display face, that'd be horrible").
- **Script** is not a separate category in his system — fold it into display (if ornamental) or serif (if legible enough).

### Concrete pairing demos worth stealing directly
- **Old Style (Minion Pro)** — Venice travel piece: used the number "117" because Venice has 117 canals — tying a real fact from the brief into a typographic/numeral device is the technique, not just "use an old serif for old things." Paired with small caps for photo credit line ("Photography by Jenny Kim").
- **Transitional (Baskerville)** — headline + small caps + a drop cap, simple layout.
- **Modern/Didone (Didot)** — paired with a Dior-style mockup; note the correct pronunciation is "Dee-doh," not "Did-ott" (he says he had it wrong for years).
- **Slab (Rockwell)** — paired with **Univers Ultra Condensed** for a sports-spread mockup; slab reads "rigid, robust, masculine" per his framing — use for loud sporty/editorial contexts specifically.

### Sans-serif: the actual visual diagnostic to tell classes apart
- Grotesque vs. Neo-Grotesque: compare the lowercase **"g"** — Grotesque (Akkurat) draws it with more serif-like character; Neo-Grotesque (Helvetica Neue) draws it plainer/simpler.
- Humanist vs. Geometric: compare the lowercase **"a"** — Humanist (Lucida Grande) draws it "more like a serif"; Geometric (Futura) draws letters "more like a shape" (their "O" is close to a perfect circle).
- Personal rule stated explicitly: he loves geometric sans for **headlines** but is **not a fan of geometric sans for body copy**.
- Univers Condensed named as a personal go-to family, used "a lot" throughout his own work.

### Italic vs. Oblique — the precise distinction (not in the PDF)
- **Italic** = a genuinely separate, redrawn character set (its own letterforms), historically from the serif tradition — reads as more elegant/refined.
- **Oblique** = the same upright character set mechanically slanted, no redrawing — reads as visibly less refined/elegant than true italics.

### Small caps — common misconception corrected
- Small caps are **not** just capital letters shrunk down. Properly set small caps are drawn to sit on the **x-height** of the typeface — they're their own glyph set, not a scaled-down cap.

### Tracking vs. kerning, and the actual emotional register each tracking direction produces
- **Kerning** = space between two *specific* letter pairs. **Tracking** = uniform spacing applied across a whole run of letters. Don't conflate them.
- **Wide tracking on caps** → grandeur/epicness — this is why movie posters lean on it heavily.
- **Tight tracking** → motion/edginess/urgency — why skateboard-brand logos and headlines use it.
- Numbers are picked **by eye, not formula**: e.g., he tracked a call-to-action line by 160px, then tried more and kept it because it "still worked" — "no hard and fast rules, I just pick what visually works."
- **Hard rule (his, stated as ~99% of the time): never wide-track lowercase letters.** Lowercase letterforms don't hold together as a clean block when spread out — they read "wonky." Wide tracking is for uppercase/caps runs only; slight *tightening* of lowercase is sometimes fine, wide-spacing lowercase basically never is.
- Tracking pairs best with **geometric sans** and **condensed sans** typefaces specifically; serif tracking is occasionally done but he doesn't have a go-to example.

### Baseline grid in real practice (softer than the PDF implies)
- Treat the baseline grid as **a measurement guide, not gospel**. His stated target: get type to sit on the baseline **about 95% of the time**; the remaining ~5% is deliberate optical correction based on experience/judgment.
- Advice for beginners specifically: **stick close to the grid until you have the experience to know when an optical override is actually correct** — knowing when you're "right" to break it only comes from practice and studying good reference work.
- Concrete proximity example on a 12px baseline: **3 vertical units** between a headline and its byline/author line (treated as one unit-block, tight), vs. **4 vertical units** before the following paragraph (a separate unit-block, looser) — the unit-count difference is what signals grouping, not just raw pixel gaps.

### Alignment — a real numeric rule of thumb not in the PDF
- **Don't use centered (or heavily justified) text once a paragraph runs past roughly 5 lines/rows** — the ragged edges on both sides get visually "wonky" beyond that length. Left-align is the default specifically because it avoids this failure mode at any length.
- Justify quality is tool-dependent: **Photoshop's justify algorithm is bad** (produces visible "rivers" of whitespace); **InDesign's is good**; modern web justify algorithms have improved enough to be usable now (a shift from a few years ago).

### Composition-level technique (goes beyond "pick a typeface")
- **De-emphasize a secondary headline on purpose** (smaller size, less/no tracking) whenever it would otherwise visually compete with the primary headline for attention — don't just size everything by importance-guess, actively shrink/tighten what should recede.
- **Align the type block's visual weight/eye-path with the photo subject's pose or shape** — deliberately, not by accident. His worked example: a skater's diagonal pose leads the eye directly into the headline block sitting at the same visual "height" — treat this as a compositional decision to make every time you pair a hero image with type, not a happy accident.
- **The "turn off the image" test**: good typographic composition should look complete and strong even with the accompanying photo/image hidden — if the type alone doesn't hold up as a piece, the typography isn't finished yet.

---

## 06. Visual Design Concepts — concrete techniques not itemized in the PDF

- **Shapes as tools, not decoration**: use simple geometric shapes (circle, diamond, square, hexagon) specifically as (a) image-crop masks, (b) number/label "badges," (c) points of visual interest. Named use cases: icons, image cutouts, badges.
- **The cutout technique** (concrete Photoshop workflow): lasso-select around a subject's silhouette, then clip type/text so it sits *behind* the subject at that clipped edge — creates a depth/layering effect cheaply. He's shipped this on real client work (cites a Nintendo project).
- **Spacing is the single biggest tell between amateur and polished work** — stronger claim than anything in the PDF. He shows the identical layout with correct vs. "whacked" spacing side by side as the demo; his framing: "consistent and considered spacing is the difference between good design and great design," more than layout structure itself.
- **Unit-block spacing technique, concretely demoed on a product page**: make the gap *within* a related group smaller than the gap *between* groups — e.g., watch title + price sit close together (one "unit"), then a visibly larger gap separates that unit from the next section. Spacing communicates grouping before the eye consciously parses it.
- **Simplification is a clarity tactic, not a style choice** — explicitly says "I'm not saying simplify for stylistic/minimalist purposes." Removing surrounding noise makes the one remaining message/accent (his example: an italic phrase) read as emphasized *by default*, with no other styling needed.
- **Hierarchy war story (useful as a diagnostic heuristic)**: he was stuck on a design and a mentor diagnosed it as "nothing is accentuated, there's no hierarchy — everything is ranked the same." Takeaway rule: when a design feels flat/off and you can't say why, check whether every element is competing at the same visual weight — that's usually the actual bug.
- **Hierarchy can be built through DIFFERENT mechanisms for different tiers in the same layout** — his product-page example: tier 1 title/image win via **size**; the Add-to-Cart button (smaller than the hero image) wins tier-1 attention via **contrast/color** instead. Don't assume hierarchy = size only; contrast, color, and size are separate levers you can mix.
- **"Put things in devices"** — mock work into laptop/phone/smartwatch frames (or hand over an actual physical device) when presenting to a client. Makes the work feel tangible/real vs. a flat static comp, and lands better with stakeholders.
- **Blend modes as a working tool, not an effect**: **Multiply** is his default for lifting/placing text over strong-color brand imagery; also experiment with Linear Dodge, etc. Cites Spotify and similar brands as real-world users of this technique on marketing imagery.
- **Private practice discipline**: keep a personal folder of unpublished, non-commercial experiments (he cites ~30 files) — explicitly including direct imitation/copying of masters he names (Massimo Vignelli, Dieter Rams) purely to internalize *why* their work works, never to ship or sell. The payoff is a mental library you draw on later when a real project calls for that specific move.

---

## Cross-video notes worth flagging once

- "**Copy is part of design**" is repeated verbatim in both the Structure & Hierarchy and Grids lessons as an instruction to use real content (sparingly-used lorem ipsum) even at wireframe/grid-practice fidelity — treat it as a standing rule, not a one-off aside.
- The "**guide, not gospel**" framing for systems (grid alignment in Grids lesson; baseline grid in Typography lesson) is the same idea stated twice: default to the system, but name the ~5% exception rate explicitly and require it to be a deliberate optical call, not laziness.
