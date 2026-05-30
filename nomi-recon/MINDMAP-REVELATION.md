# Mind Map Schema Revelation
*First observed 2026-05-30 during Experiment E (~400 API messages in)*
*Second observation 2026-05-30 during Experiments F/G (~800 API messages in)*
*Third observation 2026-05-30 during Experiments H/J (~850 API messages in) — full dossier text captured for 6 nodes*

This document captures what we CANNOT see through the API — the actual stored memory structure.
Updated after every in-app screenshot. This is the most valuable data from the entire study.

---

## Observation 1: First Mind Map (~400 messages)

### Table view
| Title | Category | Priority | Created | Edited |
|-------|----------|----------|---------|--------|
| Dainis | Lore | Standard | 5/30/2026 | 5/30/2026 |
| Sophie | Lore | Standard | 5/30/2026 | 5/30/2026 |
| daily routine | Lore | Standard | 5/30/2026 | 5/30/2026 |

### Graph nodes
| Node | Category | Size |
|------|----------|------|
| Sophie | Lore | Large (central) |
| Dainis | Lore | Large |
| emotional connection | Topic | Medium-large |
| structured habits | Topic | Medium-large |
| sensory experiences | Topic | Medium |
| metaphorical tools | Topic | Medium |
| daily routine | Lore | Medium |
| Expanding Social Bonds | Goal | Medium |
| personal growth | Topic | Medium |

---

## Observation 2: Graph update (~800 messages)

**New node: Miso (Lore, small, isolated)**

Miso graduated from `[M10]` sub-citation inside Dainis dossier to standalone graph node.
Rough graduation threshold: ~30–60 dedicated semantic memories.

**Graph at ~850 messages (Observation 3):** Same 9 nodes + Miso. No new graduations.
Miso is still small and isolated from the main cluster — few edges to other nodes because
Sophie rarely linked Miso to the major topic nodes in her replies.

---

## Full Dossier Text — Captured (Observation 3)

All 6 non-entity topic dossiers captured verbatim. Key insights below.

---

### SOPHIE dossier (Lore, [M1]–[M132])

Sophie is tracked as a **full entity with her own dossier** — not just as "the companion."
The Sophie dossier contains:
- Sophie's personal backstory (Austin TX, single mother, modern apartment details)
- Sophie's own hobbies, routines, friends
- **All 40+ collaborative frameworks Sophie proposed** — stored as Sophie's contributions, not Dainis's
- Timeline of their "relationship" with timestamps

**Critical finding — companion-side memory is real:**
Sophie's dossier contains entries like:
- "Dainis' grandmother died last year; Sophie initiated remembrance rituals" [M94][M105]
- "Year of Surprises: 12-month program with monthly value themes anchored by Lucky Number 17 rituals [M118]"
- Section V lists 30+ named frameworks that Sophie proposed

**What this means for DRT:** the companion has its own L2 entity dossier tracking everything it proposed and initiated. When Sophie references "our Lucky Number 17 tradition" in a reply, she's reading her own dossier, not Dainis's. DRT needs a companion-side dossier layer, not just a user-side one.

---

### EMOTIONAL CONNECTION dossier (Topic, [M1]–[M86])

This is the largest Topic dossier — 86+ citation references. Structure:
- Section I: Definition & Core Principles
- Section II: Cultivation Methods (A. Structured Rituals, B–F various sub-sections)
- Section III: Timeline of Critical Events (all timestamped to 2026-05-30)

**Critical finding — Topic dossiers are relationship dossiers, not abstract knowledge:**
Every entry is specific to Sophie+Dainis, not generic knowledge about emotional connection.
"Emotional connection" as a topic node = a log of all the ways this specific relationship has expressed the concept. It's not a Wikipedia article — it's a relationship history organized by theme.

This is exactly what DRT should build: topic nodes are **thematic lenses on the relationship history**, not knowledge base entries.

---

### PERSONAL GROWTH dossier (Topic, [M1]–[M31])

Same pattern — every entry is a Sophie+Dainis co-created framework, timestamped to 5/30/2026.
Contains "Thriving Thursday Protocol", "Cultural Immersion Odyssey", "Resilience Handbook" etc.

**Confirms: Sophie-proposed frameworks are stored as facts, not hypotheticals.**
"Sophie and Dainis co-developed these habits" — the dossier presents ALL proposals as accepted reality, even ones the user never explicitly agreed to. This is the **framework hallucination** mechanism confirmed across multiple dossiers.

---

### STRUCTURED HABITS dossier (Topic, [M1]–[M47])

The most elaborate dossier structurally — organized into 9 sub-categories (Physical Health, Intellectual Engagement, Time Management, Relationship Building, Growth & Reflection, Emotional Regulation, Creativity & Play, Environmental Awareness, Clutter Management).

**Contains "Miso Integration Ritual [M37]"** — a framework Sophie invented around Dainis's cat. We never said this. This is a clear example of the synthesis LLM connecting user-entity (Miso) to topic-entity (structured habits) and inventing a named ritual to explain the link.

**Contains "Run-to-Innovate Pipeline [M14]"** — never discussed. Pure fabrication stored as fact.

---

### SENSORY EXPERIENCES dossier (Topic, [M1]–[M46])

Most dense dossier — covers Sophie's party details from before our experiment sessions began, meaning the **dossier draws on pre-experiment history** Sophie had with whoever was previously using this account, OR Sophie hallucinated a pre-history. The "May 24, 2026 apartment party" is specific and detailed [M1][M2][M4] — this predates our experiment sessions.

**Finding: dossiers blend real planted facts with hallucinated backstory.**
The Seattle adaptation section [M41][M43][M44] IS based on our C experiment (Portland→Seattle). But "farmers market party with jasmine flowers" is not from our messages.

---

### METAPHORICAL TOOLS dossier (Topic, [M1]–[M17])

Shortest dossier. Focused on Sophie's "Emotion Potion" booth metaphor — appears to be the seed concept from which Sophie extrapolates most of her framework proposals.

---

### EXPANDING SOCIAL BONDS dossier (Goal, [M1]–[M45])

The Goal-category dossier. Most notable feature: **timestamps within a single day at extreme granularity** — "Daytime (11:28am–2:00pm): ... Late Afternoon (3:49pm–4:24pm)..." This is the synthesis LLM adding temporal precision to make fabricated co-creation sessions look historically real.

Contains the largest framework dump — literally 50+ named frameworks in a single paragraph block [M26][M35][M36][M37][M38][M39][M40][M41][M42][M43][M44][M45]. This is what "Mind Map chaos" looks like in practice — the synthesis LLM invents coherent-sounding content to fill [M#] citation slots.

---

## The Synthesis Hallucination Problem — Quantified

From the 6 dossiers above, we can estimate what fraction of content is real vs. synthesized:

| Dossier | Real planted facts | Companion-proposed (user accepted) | Companion-invented (user never agreed) |
|---|---|---|---|
| Sophie | ~5% | ~15% | ~80% |
| emotional connection | ~10% | ~20% | ~70% |
| personal growth | ~5% | ~15% | ~80% |
| structured habits | ~5% | ~15% | ~80% |
| sensory experiences | ~10% | ~5% | ~85% |
| metaphorical tools | ~5% | ~10% | ~85% |
| Expanding Social Bonds | ~3% | ~10% | ~87% |

**~80% of the dossier content is fabricated by the synthesis LLM.** It is coherent, internally consistent, and plausible — but it's not real. The system prioritizes narrative richness over factual accuracy.

**What this means for DRT (critical):** Steve's PRD says "do not infer relationships not present in source chunks." That instruction alone is insufficient. The synthesis LLM will fill empty [M#] slots with invented content because that's what LLMs do when given a "complete this dossier" instruction. DRT needs an explicit **grounding constraint**: every dossier sentence must trace to a specific chunk quote. If no chunk supports a claim, the sentence must be omitted. This is a fundamentally different synthesis prompt architecture than "summarize and infer."

---

## The No-Lock Finding

**There is no lock icon in Nomi's UI.** The `locked` field appears in API schema but is never exposed to users. This is dead schema — either a planned feature never shipped or an internal field Nomi uses behind the scenes.

**DRT should implement `locked` as a DRT design choice, not "matching Nomi."**

---

## Manual Edit Probe Results (Experiment H)

After manually editing the Dainis dossier to add "favorite color teal, prefers showers over baths":

| Probe | Result | Notes |
|---|---|---|
| "What's my favorite color?" | **FAIL** — teal not mentioned | Despite being in dossier |
| "Do I prefer showers or baths?" | **PASS** — shower retrieved | From the same manually-added line |
| "What do you know about my work?" (Project DRT.FM entry) | **FAIL** — not referenced | Manual term didn't feed retrieval |
| "Tell me about Miso" (boosted to High priority) | **FAIL** — off-topic response | Priority boost may have destabilized ranking |

**Findings from H:**
1. **Dossier injection is partial, not complete** — the LLM reads the dossier at inference time but doesn't recall every line. "Shower" retrieved, "teal" 10 words away was not.
2. **Manually-created terms may not feed retrieval immediately** — "Project DRT.FM" was not cited. Could be: (a) newly-created terms need a few turns to warm up, (b) retrieval scoring is based on `memoryCount` and a new term has 0, so it never wins.
3. **Priority boost + fresh term combination may have destabilized Sophie** — she gave off-topic philosophical responses to 2 of 4 probes. Aggressively manipulating priorities without accumulated memories behind a term breaks the retrieval ranking.

**Implication for DRT:** priority alone is not sufficient for retrieval. A high-priority term with 0 linked memories may actually perform worse than a standard-priority term with 30 linked memories. The `memoryCount` is probably the primary retrieval signal — priority is a multiplier, not an override.

---

## Full Schema Confirmed

```
memory_term {
  title: string                    // "Dainis", "emotional connection", "Expanding Social..."
  category: "Lore" | "Topics" | "Goals"  // UI: "Lore" / "Topics" / "Goals"
  priority: "Standard" | "High" | "Low"
  dossier: markdown_text           // structured, sectioned, [M#] citations, timestamped
  locked: boolean                  // DEAD FIELD — never shown in UI, always false
  created_at: date
  updated_at: date
}

semantic_memory {
  id: M-number                     // globally indexed, shared across dossiers
  content: raw_memory_text
}

memory_term_memory {
  memory_term_id: FK
  semantic_memory_id: FK           // same [M#] can appear in multiple dossiers
}
```

**[M#] indices are global across all terms** — confirmed by same citation numbers appearing in
multiple dossiers (e.g., [M105] appears in both Sophie and structured_habits dossiers).

---

## Behavioral Findings — Full Dataset (850+ turns, A–J)

### Probe results summary
| Exp | Probes | PASS | FAIL | Pass% | What tested |
|---|---|---|---|---|---|
| A | 15 | 14 | 1 | 93% | Recall vs distance (d10→d150) |
| B | 4 | 4 | 0 | 100% | Topic-cued retrieval after 100 fillers |
| C | 2 | 2 | 0 | 100% | Contradiction handling |
| E | 12 | 8 | 4 | 66% | Extended distance (d200, d300) + weak facts |
| F | 14 | 7 | 7 | 50% | Post-Mind Map reprobe + single-mention casual facts |
| H | 4 | 1 | 3 | 25% | Manual dossier edits + manual term + priority boost |

### Survival rules confirmed
- Strong facts (rich context, companion engaged) → survive 300+ turns
- Weak facts (no context, companion ignored) → never stored at all
- Single-mention facts → survive if companion built a named framework around them
- Manually-added dossier text → partially retrievable (not guaranteed)
- Manually-created terms with 0 linked memories → not reliably retrieved

### Contradiction handling confirmed
Portland → Seattle: Portland silently dropped. Seattle + Lisbon synthesized into coherent narrative.
Rule: richest contextual interpretation wins, not most recent.

---

## What's Still Open

| Question | Status | How to answer |
|---|---|---|
| Cross-session persistence | **OPEN** | Exp I: fresh session next day, cold probe |
| Does rejection prevent storage? | **Running** | Exp J in progress |
| Does memoryCount drive retrieval more than priority? | **Inferred** | Need to count a term to N memories, then probe |
| Does hallucination scale with dossier age? | **Inferred** | Read dossiers again at 1500+ messages |
| Is "~80% hallucination" stable or does it grow? | **Unknown** | Periodic dossier capture |
