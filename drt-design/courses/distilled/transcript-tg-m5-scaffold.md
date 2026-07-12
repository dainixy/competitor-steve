# Tommy Geoco — Module 5 (Information Scaffold) — Transcript DELTA

Source: 9 video transcripts, `transcripts/tommy-geoco/0X-*.txt`. Compared against `tg-book-ch1.md` §5.1–5.9 (Module 5 write-up) and `tg-book-ch2.md`. Only NEW spoken material is captured below — worked examples, reasoning, war stories, numbers, and framing not already in the written distillation. Rules already in ch1/ch2 are not repeated.

---

## 01 — Create an information scaffold (module intro)

New framing not in the book text:

- **The scaffold answers 4 specific questions on demand** — use these as a self-check when looking at any interface: *Is this an effective interface? Which psychology concepts are at work here? What market opportunity does this interface support? Which UI patterns best fit this use case?* If you can't answer these fast, your scaffold has a gap.
- **The point isn't permanent reference — it's internalization.** His words: "Eventually, you won't have to refer back to this every time, but having put it together solidifies the things you've learned." The act of building the scaffold is what cements the knowledge, not the document itself.
- **Concrete example of extending the scaffold to a new discipline:** if you take on a motion design project and it's your first time learning spatial/motion principles, add that new section to your scaffold as you learn it — the scaffold isn't fixed at 10 components, it grows into whatever new craft you pick up.

## 02 — Atomic design principles

Book already has the 5 levels + the two use cases (defining patterns / transforming ideas) nearly verbatim. One new worked example:

- **Cluster's atomic breakdown, spoken example:** Atoms = text inputs and buttons. Molecules = formatting toolbars. Organisms = full-fledged editors. Applied to unify the visual language of collaborative features across the app. (Different from the book's own example — the book uses "popup vs. cancel/save button group.") Use both examples as reference points when explaining atomic levels to someone.

## 03 — Introduction to patterns

Not covered in ch1/ch2 as a standalone concept — this is a genuine delta section.

- **Claim: UI pattern innovation for desktop/web/mobile has hit a ceiling.** Direct quote: "As of the 2020s, we can safely assume that we've reached a ceiling on many of the UI pattern use cases for desktop, web, and mobile devices. There's only so much more we can invent that isn't now working very well for human-computer interaction." His prediction for where NEW patterns will come from: **voice, spatial, and other emerging modalities** — not screens.
- **Quality bar for a pattern library:** "Ideally, a non-designer should be able to take these patterns and design a sufficient interface that conveys a usable idea." Use this as a literal test — if a pattern reference requires design judgment to apply correctly, it's not documented well enough.
- **Reasoning for reuse over "reinventing":** "Why solve a problem from scratch if somebody else has already cracked the most optimal path?" — patterns encode collective knowledge of what already works; using them isn't copying, it's not re-deriving a solved problem.
- **Evaluation checklist when picking a pattern** (spoken, not written elsewhere as a list): look for relevant patterns → evaluate their benefits/use cases → consider what psychological principles they support and whether those align with your business/user goals → check fit within your specific context → adapt to user needs and brand guidelines → check technical constraints.

## 04 — Design psychology reference

Book has the full 38-principle table with categories (Filtering/Sense-making/Recall/Efficiency) and 3 usage examples (Peak-End, Zeigarnik, Goal-Gradient). The video uses a **different, non-overlapping set of 4 worked examples** — capture these as additional applied cases:

- **Aesthetic-Usability Effect (Filtering)** → Cluster example: make the interface visually appealing specifically to *encourage users to explore more features* — the effect isn't just "looks nice," it's a lever for feature discovery.
- **Hick's Law (Efficiency)** → Cluster example: streamline content-creation tools by presenting only the most relevant options at each stage (not all options at once) — a direct design response to "more options = slower decisions."
- **Chunking (Recall)** → Cluster example: organize content into groups/categories so users can hold more of it in memory.
- **Scarcity Effect (Sense-making)** → Cluster example: create urgency around limited-time collaboration features or exclusive templates. **Note: "Scarcity Effect" does not appear anywhere in the ch1 38-principle table — it's a principle missing from the written distillation entirely.** Definition as given: people value things more when they're perceived as scarce.

## 05 — Good design decisions are relative

~95% overlap with ch1's "Quality of a fast decision" section (same StreamPro-style counterfactual, same 3-part test). Only new material:

- **Soundbite worth keeping verbatim** (he explicitly says "listen to that again," signaling it's the load-bearing line of the section): *"The quality of your design decisions are either undermined or justified by the path you took to arrive at them."*
- **New framing not in the book:** "We are not aiming for perfection. We are aiming for effectiveness, because effectiveness gets us to perfection, or close to it, over time." Use this as the guiding answer to "good enough vs. perfect" tension — effectiveness is the target metric, perfection is a byproduct over time, not a direct goal.

## 06 — Accessibility reference

POUR breakdown and examples match ch1 almost exactly. One new argument worth keeping — it's the practical rebuttal to "we don't have time for accessibility":

- **"Implementing accessibility from the start is always faster and cheaper than retrofitting it later. Plus, it often leads to better usability for everyone."** This is the direct counter to teams saying "we need to ship" — not in the written material, and it's the most useful line for a non-technical founder pushback moment.

## 07 — Typefaces and icons

Font/icon shortlists and the 16px-base rule match ch1 exactly. New material is a personal workflow anecdote plus one worked example:

- **War story — how his own process changed:** "At the beginning of my career, I would start from the typeface first. I'd spend hours picking the right one. Now, I start with a default from my library so that I can get to the real work of solving software problems. Later, I'll come back to typeface and icons to consider if they'd benefit from special treatments." — the lesson: pick the default typeface/icon set FIRST with zero deliberation, ship the real design work, and only revisit typography for "special treatment" refinement at the end, never at the start.
- **Cluster icon example (not in book):** for a content-creation/collaboration product, choose an icon library covering editing tools, sharing icons, and file-organization symbols — i.e., pick the library based on your product's *verb set*, not generic aesthetics.

## 08 — Design system reference

This is the highest-value delta in the module. **The specific system→strength mapping does not appear anywhere in ch1–ch6** (grepped for "Material Design" across all chapter files — zero matches). The book only says "reference mature public design systems" in the abstract; the video gives the actual per-system cheat sheet:

- **Google Material Design** → go here for motion, dark theme, and elevation principles.
- **Apple Human Interface Guidelines** → go here for keyboard shortcuts and general usability principles. Apple Vision OS specifically → spatial design principles (the emerging modality he flags in video 03).
- **IBM Carbon** → go here for data visualization and accessibility guidelines.
- **Microsoft (Fluent)** → go here for AI interaction patterns that keep a human in the loop.
- **Worked Cluster example:** reference Material Design for content-organization patterns, Apple HIG for keyboard shortcuts, Microsoft for AI feature workflows — i.e., don't pick one system as your bible, pull the specific strength from each as needed per pattern.
- Reasoning restated for why this beats building from scratch: these companies "have done the heavy lifting in terms of research and testing" — treat their guidelines as free access to research budgets you don't have.

**Actionable takeaway for the design-taste doc:** when stuck on motion/elevation → check Material. Keyboard shortcuts/general usability → check Apple HIG. Data viz/accessibility → check IBM Carbon. AI/human-in-the-loop patterns → check Microsoft Fluent.

## 09 — Default design rules

Examples (confirm-right/cancel-left, CRUD table actions, Product/User/System nav groups) and the create/override/update maintenance actions match ch1 exactly. One new piece of framing worth keeping as motivating context:

- **Cost-of-debate framing, spoken only:** "Every day, somewhere, a software team is spending thousands of dollars in time debating some UI pattern. Engineers, managers, and designers argue from their experience, references, and intuitions." — this is the concrete stakes-setting line for *why* default rules exist at all: undocumented bias still drives every decision, it just costs more in meeting time when it isn't written down.
- The spoken usage loop is a slightly cleaner restatement of the book's 3 actions as a sequence: **start with your default → check it fits the current project → if not, adapt based on user research/product data → update the default if the adaptation proves better.** Same content as ch1's create/override/update, just ordered as a linear checklist rather than three named actions.

---

## Summary of genuinely new content (not derivable from ch1/ch2 at all)

1. Full per-system strength mapping for Material/Apple HIG/IBM Carbon/Microsoft Fluent (video 08) — the single most useful new reference.
2. "Scarcity Effect" as a psychology principle — absent from the book's 38-entry table (video 04).
3. Accessibility-first-is-cheaper-than-retrofit argument (video 06).
4. "Ceiling on UI patterns, next frontier is voice/spatial" claim + the "non-designer should be able to use your patterns" quality bar (video 03).
5. Personal workflow anecdote on deferring typeface/icon decisions to defaults-first (video 07).
