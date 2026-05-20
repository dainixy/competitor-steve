# Competitor Discovery Prompt — AI Girlfriend Category

**Purpose:** Find AI girlfriend competitors that should be added to the existing v2 analysis (`competitor-analysis-v2.html`), beyond the 6 already covered (Candy.AI, OurDream.AI, SecretDesires.AI, GirlfriendGPT, Promptchan, Joi.AI). End user: Steve (DRT's developer) — he needs feature-parity leads, not marketing essays.

**How to use this file:**
1. Run the **Core Prompt + Kimi Addendum** in Kimi Deep Research.
2. Run the **Core Prompt + Grok Addendum** in Grok.
3. Once both finish, run the **Opus Adjudicator Prompt** in Claude Opus, pasting in both prior outputs.
4. Manually verify (Dainis Checks) before adding anything to v2.

---

## CORE PROMPT (identical for Kimi and Grok)

You are doing competitor discovery for an AI girlfriend product. **Today's date is May 17, 2026.** I have already deeply analyzed 6 incumbents. Your job is to find what I am missing — recent fast-growers and innovators — not to re-analyze what I already know.

### What I already have (do NOT re-research these)

Existing v2 matrix covers: **Candy.AI, OurDream.AI, SecretDesires.AI, GirlfriendGPT, Promptchan, Joi.AI**.

### Hard exclusions (do NOT include — different research track)

- **Replika** and **Oshikoi.io** — these are reserved for a separate flagship-product research track. Skip them entirely.
- Any **SFW-only / wellness / therapy** positioning (e.g., Pi, Woebot) — different category.
- Any **B2B chatbot platform** — different category.
- Any product **shut down, region-locked outside English markets, or only available in non-English regions.**

### Your job

Find the **AI girlfriend competitors that should be added to my v2 analysis** because they are either (a) where users are actually going right now, or (b) shipping innovation the incumbents are about to copy. Then return them in the exact output format below.

### Selection criteria — must hit at least 2 of 3

1. **Traffic / audience momentum.** Either large absolute traffic OR meaningful growth in the last 6 months. Triangulate from:
   - Press mentions (TechCrunch, The Verge, Wired, Decoder, etc.)
   - Reddit thread volume and upvotes on relevant subs (r/AICompanions, r/CharacterAI_NSFW, r/AIGirlfriend, etc.)
   - YouTube review video view counts and recency
   - X/Twitter mentions and creator buzz
   - Public traffic claims from the company itself (often in PR / pitch decks / "we hit X users" announcements)
   - SimilarWeb snippets if they appear in search results
   - **There is no clean SimilarWeb-equivalent API for you. Triangulate. Cite every source.**
2. **Recent innovation.** Shipped a notable feature in the last 6-12 months that is *not* already a row on my v2 matrix. The v2 matrix columns are listed below — anything outside those columns is potentially "net new" and should be flagged.
3. **NSFW-capable subscription product.** Matches the shape of our product. NSFW must be a real, working capability — not a "coming soon" or jailbreak.

### Scope — narrow main list + active carve-out

**Main shortlist:** subscription-based AI girlfriend products (same product shape as the incumbents).

**Active carve-out — "Adoptable Patterns from Character-Roleplay Platforms":** Separately, look at character-card roleplay platforms (Janitor.ai, Chub.ai, SpicyChat, and similar). **Do not put them on the main shortlist** — their business model is different (free / BYO-API, user-generated character marketplaces). **But** these platforms have huge audiences and ship UX patterns that subscription sites are starting to adopt or could profitably adopt (character cards, lorebooks, persona swapping, open-source model integration, group chats, etc.). I specifically want to know what patterns from this world a subscription product like ours should consider importing. Janitor's open-source / clonable model is exactly the kind of thing I want surfaced.

### Output format

**1. Main Shortlist — up to 5 new competitors.** Cap at 5. If you find more than 5, rank and cut — force the trade-off. For each, fill in this table mirroring my v2 matrix columns:

| Feature | Site Name |
|---|---|
| Video generation (user-facing) | ✓ / ✗ / ~ + 1-line annotation + URL |
| Voice calls (emotional) | ✓ / ✗ / ~ + 1-line annotation + URL |
| Images auto-generated in chat | ✓ / ✗ / ~ + 1-line annotation + URL |
| Auto-memory (builds invisibly) | ✓ / ✗ / ~ + 1-line annotation + URL |
| Memory visible to user | ✓ / ✗ / ~ + 1-line annotation + URL |
| 3D animated character | ✓ / ✗ / ~ + 1-line annotation + URL |
| Named video engines + flat pricing | ✓ / ✗ / ~ + 1-line annotation + URL |
| Character creator / community | ✓ / ✗ / ~ + 1-line annotation + URL |
| Romance/progression mechanic | ✓ / ✗ / ~ + 1-line annotation + URL |
| Gift-giving mechanic | ✓ / ✗ / ~ + 1-line annotation + URL |
| User sends images to character | ✓ / ✗ / ~ + 1-line annotation + URL |
| Age verification compliance | ✓ / ✗ / ~ + 1-line annotation + URL |
| NSFW sound in video | ✓ / ✗ / ~ + 1-line annotation + URL |
| Content private by default | ✓ / ✗ / ~ + 1-line annotation + URL |
| Multi-language chat | ✓ / ✗ / ~ + 1-line annotation + URL |
| **Dainis Checks** | (leave empty — Dainis fills manually) |

Plus per site:
- **Why included** (which 2-of-3 criteria it hits, with evidence)
- **Traffic / momentum evidence** (cite all sources used to triangulate)
- **Net-new features** — anything this site does that is NOT a row on the v2 matrix above. *This is the most valuable part of your answer.* If 3 sites all do the same net-new thing, that's a candidate new row on my matrix and a roadmap item for Steve.
- **Freshness flag** — for any claim, if the source page is older than 6 months or you can't confirm it currently exists, mark it `⚠ STALE` with explanation. Do not fill in from training data without a current URL.

**2. Honorable Mentions — up to 5 more.** Sites that were close but didn't make the cut. One paragraph each explaining why included, why not in the top 5. Same Dainis-Checks-friendly format (URL-cited claims).

**3. Adoptable Patterns from Character-Roleplay Platforms.** Separate section. 2-5 specific patterns from Janitor.ai / Chub.ai / SpicyChat / similar that a subscription product like ours could adopt. For each: pattern name, where it lives (which site, with URL), why it works there, how it would translate to a subscription product. Janitor's open-source / clonable model is one candidate — find the others.

### Style requirements

- **Every claim needs a URL.** Changelog page, pricing page, feature page, press article, Reddit thread, X post — anything verifiable. No URL = don't include the claim.
- **No screenshots.** URLs are sufficient.
- **Today is May 17, 2026.** If your training data is older, say so. Filter sources by date. Anything you can't verify against a post-November 2025 source must be marked `⚠ STALE`.
- **You are producing leads for manual verification, not truth claims.** Dainis will check every site before adding it to v2. Optimize for "did I surface the right candidates with enough evidence to verify quickly," not "did I write a polished report."
- **Do not pad.** If you only find 3 sites that meet the criteria, return 3. Five honorable mentions cap, not floor. Better to return fewer high-quality leads than to pad with weak ones.

### Example rows from v2 (so you see the shape and tone)

**Candy.AI** (existing — for reference only):

| Feature | Candy.AI |
|---|---|
| Video generation (user-facing) | ✓ "Live Action Video" Feb 2026 — `https://candy.ai/...` |
| Voice calls (emotional) | ✓ standard quality — `https://candy.ai/...` |
| Images auto-generated in chat | ✓ Story Mode — `https://candy.ai/blog/story-mode` |
| Auto-memory (builds invisibly) | ~ testing — `https://candy.ai/changelog` |
| Memory visible to user | ~ partial — `https://candy.ai/...` |
| 3D animated character | ✗ |
| Named video engines + flat pricing | ✓ — `https://candy.ai/pricing` |
| Character creator / community | ✓ — `https://candy.ai/community` |

**SecretDesires.AI** (existing — for reference only):

| Feature | SecretDesires.AI |
|---|---|
| Video generation (user-facing) | ✓ "Inferno" Apr 2026 — `https://secretdesires.ai/inferno` |
| NSFW sound in video | ✓ Inferno — `https://secretdesires.ai/inferno` |
| Named video engines + flat pricing | ✓ Inferno flat pricing — `https://secretdesires.ai/pricing` |
| Memory visible to user | ~ partial — `https://secretdesires.ai/...` |
| 3D animated character | ✗ |

(That's the level of brevity per cell. One-line annotation + URL. Nothing more.)

### Reference document

`competitor-analysis-v2.html` is the existing analysis. Use it **only to cross-check that you're not duplicating** — do not let its findings about the incumbents bias your discovery. You are looking for what is *missing* from it.

---

## KIMI ADDENDUM (append to Core Prompt when running in Kimi Deep Research)

**Today is May 17, 2026.** Your training data may be 3-6 months stale on this category, which moves fast. Do not rely on training data. For every site you surface and every feature you claim:

- The URL must resolve, and the page content must be from the last 6 months. Prefer changelog pages, recent press, recent Reddit threads, recent YouTube reviews.
- If you can only find a source older than 6 months, mark the claim `⚠ STALE` with the source date.
- Prioritize multi-step web search across press (TechCrunch, The Verge, Decoder), Reddit (r/AICompanions, r/AIGirlfriend, NSFW-specific subs), YouTube reviews, and product changelog pages.
- Specifically check **product launch announcements from the last 6 months** — that's where the fast-growers will surface.

---

## GROK ADDENDUM (append to Core Prompt when running in Grok)

**Today is May 17, 2026.** Lean heavily on your real-time X/Twitter access — this is your unique strength versus Kimi and Opus.

- Surface AI girlfriend products that are **trending or being actively discussed on X in the last 60 days** among AI creators, NSFW creators, builders, and end users.
- Include representative X posts/threads as evidence (post URL, author, post date, brief quote of what they're saying).
- Pay attention to small accounts and niche communities, not just headline tech press — fast-growers often surface on X before they hit press.
- For each site you surface, include at minimum 2-3 X posts as evidence of momentum.

---

## OPUS ADJUDICATOR PROMPT (run after Kimi and Grok finish)

I ran the attached Core Prompt in Kimi Deep Research and Grok separately. Their outputs are below. Your job is to adjudicate, deduplicate, and produce the final shortlist.

### Inputs

**Kimi output:** [paste Kimi's full response here]

**Grok output:** [paste Grok's full response here]

**Reference:** `competitor-analysis-v2.html` (the existing v2 analysis — use this to verify nothing on the v2 matrix is being re-surfaced as "new").

### Your task

1. **Overlap = high confidence.** Any site both Kimi and Grok independently surfaced is a strong candidate. Promote these.
2. **Disagreement = verification queue.** Sites only one tool found: assess the evidence quality. Strong evidence from one tool can still be a real lead; thin evidence from one tool is probably noise. Flag these as "needs Dainis check first."
3. **Novelty check.** For every "net-new feature" claim, verify it's actually not already on the v2 matrix columns (listed in the Core Prompt). Reject claims that are just rebrands of existing v2 features.
4. **Freshness audit.** Flag any claim with stale or missing sources. Do not promote any claim where the URL is older than November 2025 unless it's foundational (e.g., the site's existence).
5. **Adoptable Patterns section.** Merge Kimi's and Grok's lists; cut duplicates; rank by adoptability (how easily a subscription product like ours could import the pattern).

### Final output

- **Final Main Shortlist** (≤5 sites) — same table format as Core Prompt, with a confidence rating per site (`HIGH` / `MEDIUM` / `LOW`) based on overlap and evidence quality.
- **Final Honorable Mentions** (≤5 sites) — same format, with confidence ratings.
- **Final Adoptable Patterns** — merged, deduplicated, ranked.
- **Verification queue** — explicit list of claims Dainis needs to manually verify before adding anything to v2, ordered by how load-bearing each claim is to the recommendation.

Optimize for: Dainis can open this doc, do manual checks against the verification queue, and decide what to add to v2 in under 30 minutes.
