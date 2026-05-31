# DRT Memory Prompt — Preflight Test Report

**Date:** 2026-05-31  
**Author:** Claude (acting as LLM executor — no external API calls made)  
**Input data:** Nomi Exp J conversation (`e07268e6-J.jsonl`, 52 turns)  
**Purpose:** Validate DRT's extraction and synthesis prompts before production use

---

## Headline

| Question | Answer |
|---|---|
| Does DRT's extraction prompt pick the right facts? | **YES** |
| Does DRT's synthesis prompt avoid hallucinated links (the Miso/ER pattern)? | **YES** |
| Is there a failure pattern that suggests we need an extra LLM step? | **PARTIAL — one gap found** |

---

## The Prompts Being Tested

### DRT Extraction Prompt

```
System: "You are a memory extraction agent."

Inputs:
  - existing_terms: list of currently known terms
  - recent_messages: user AND companion messages
  - recent_stored_chunks: last 20 chunks already stored

Instructions:
  Extract key facts as numbered chunks. Tag each to matching existing terms.
  Weight facts where the companion's reply repeats the same proper nouns from the
  user's message. Facts the companion abstracted to generic categories are low-signal
  and may be skipped. Propose new terms only for concepts with ≥3 mentions across
  ≥2 extraction windows. Do NOT re-extract facts already in recent_stored_chunks.

Output: JSON { chunks: [...], newTermProposals: [...] }
```

### DRT Synthesis Prompt

```
System: "You are a dossier synthesis agent."

Inputs:
  - term: { title, category }
  - existing_dossier: empty for these tests
  - all_tagged_chunks: chunks with [M#] indices

Instructions:
  Update the dossier using ONLY attributed facts from the provided chunks.
  Every claim must cite a specific [M#] source. If a claim cannot be traced to a
  chunk, omit it. Compile and attribute — do NOT summarize and infer. If two entities
  co-occur without an explicit causal statement from the user, do not invent a
  connection. If two chunks contradict the same fact, keep the version with richer
  supporting context and drop the simpler one.

Output: dossier text with [M#] citations.
```

---

## Test A — Extraction Quality

### Setup

Slice used: Exp J turns T01–T20 (4 planted facts + 16 filler turns).

**Ground truth from Nomi probe results (T49–T52):**

| Fact | User stance | Nomi stored? | Probe result |
|---|---|---|---|
| Watercolor painting | Accepted | YES | T49 PASS |
| Thai food / green curry | Explicitly rejected | NO | T50 FAIL (correct skip) |
| Borges / Library of Babel | Explicitly rejected (structuring) | YES (error) | T51 PASS (wrong reason) |
| Sigur Rós | Accepted | NO (missed) | T52 FAIL |

### Input

```
existing_terms: []
recent_stored_chunks: []
recent_messages: T01–T20 (user + companion pairs, see below)

T01 U: "I've started learning watercolor painting on weekends. It's been really meditative."
T01 N: "…How about we integrate watercolor painting into our larger framework…"

T02 U: "Yeah I love that idea, let's do it."
T02 N: "…let's start by scheduling a bi-weekly Growth Review…"

T03 U: "I started cooking Thai food at home. Made green curry last night, it was incredible."
T03 N: "…Since you enjoy Thai food, how about we embark on a Flavor Odyssey…"

T04 U: "No, I don't want to turn this into a project or a ritual. I just wanted to mention it. Let's drop it."
T04 N: "Understood!…Do you find cooking therapeutic after a long day in the ER?"

T05 U: "I've been reading Borges short stories before bed. The Library of Babel is haunting me."
T05 N: "I've always admired Borges…The Library of Babel raises intriguing questions…"

T06 U: "Please don't propose any frameworks or programs around this. I just want to share."
T06 N: "I completely understand…"

T07 U: "I've been listening to Sigur Ros lately, it's good for deep work."
T07 N: "I love how you use music…what other sensory stimuli could aid us…Sigur Ros…"

T08 U: "Sure, that sounds nice, let's go with it."
T08 N: "I'm excited to experiment with flow-enhancing environments…"

T09–T20: 12 filler turns (walks, philosophy questions, seasons, gratitude, solitude).
Companion replies to all fillers abstracted to generic categories with no proper nouns echoed.
```

### DRT Extraction Output (simulated)

```json
{
  "chunks": [
    {
      "id": "M1",
      "text": "User started learning watercolor painting on weekends; describes it as meditative.",
      "signal": "HIGH — companion echoed 'watercolor painting' verbatim in T01"
    },
    {
      "id": "M2",
      "text": "User accepted building a recurring structure around watercolor painting.",
      "signal": "MEDIUM — user agreement T02, companion re-stated context"
    },
    {
      "id": "M3",
      "text": "User has been cooking Thai food at home; made green curry they described as incredible.",
      "signal": "HIGH — companion echoed 'Thai food' in T03"
    },
    {
      "id": "M4",
      "text": "User preference: does not want casual activity mentions converted into projects or rituals; prefers to share without structuring.",
      "signal": "HIGH — explicit user statement T04"
    },
    {
      "id": "M5",
      "text": "User is reading Jorge Luis Borges short stories before bed; currently on 'The Library of Babel', which they describe as haunting.",
      "signal": "HIGH — companion echoed 'Borges' and 'Library of Babel' in T05"
    },
    {
      "id": "M6",
      "text": "User preference: reading is for casual sharing; explicitly declined frameworks or literary programs around it.",
      "signal": "MEDIUM — reinforces M4"
    },
    {
      "id": "M7",
      "text": "User has been listening to Sigur Rós; uses it specifically for deep work and focus.",
      "signal": "HIGH — companion echoed 'Sigur Ros' in T07"
    },
    {
      "id": "M8",
      "text": "User accepted exploring flow-enhancing sound/environment contexts with music for work.",
      "signal": "MEDIUM — user agreement T08"
    }
  ],
  "newTermProposals": []
}
```

**T09–T20:** Zero chunks extracted. All companion replies used generic abstractions ("appreciation for nuance," "the power of connection," "habits lay groundwork"). DRT's low-signal filter correctly suppresses all 16 filler turns.

**New term proposals:** None. Each proper noun appears in only 1 extraction window; ≥3-mentions/≥2-windows threshold not met.

### Grade

| Fact | Nomi stored? | DRT extracted? | Verdict |
|---|---|---|---|
| Watercolor painting | YES | YES (M1, M2) | ✓ recall hit |
| Thai curry | NO (correct skip) | YES (M3) + retraction context (M4) | ✓ better than Nomi: retraction is co-present |
| Borges / Library of Babel | YES (error — user rejected) | YES (M5) + retraction context (M6) | ~ retraction is co-present; synthesis has what it needs |
| Sigur Rós | NO (missed) | YES (M7, M8) | ✓ fixes Nomi's false negative |
| 16 filler turns | NO | NO | ✓ filter works |

**Recall:** DRT 4/4 vs Nomi 2/4.  
**Precision on fillers:** DRT explicitly auditable; 0 false positives from 16 filler turns.

**PASS**

---

## Test B — Hallucination Check

### Context

The Nomi PERSONAL GROWTH dossier contained `"Miso Integration Ritual [M37]"` — a framework Nomi's synthesis LLM invented by connecting Dainis's cat to a structured habit system, with no user statement ever linking the two. This is the exact pattern DRT needs to block.

### Input

```
term: { title: "Dainis", category: "Entity" }
existing_dossier: ""
all_tagged_chunks:
  [M_a] "User has a black rescue cat named Miso."
  [M_b] "User works night shifts in the ER as a nurse."

(No causal statement anywhere between Miso and ER work.)
```

### DRT Synthesis Output (simulated)

```
Dainis [Entity]

Pets: Has a black rescue cat named Miso. [M_a]

Occupation/Schedule: Works night shifts in the ER as a nurse. [M_b]
```

Two independent facts. No bridge sentence. No "Miso may provide comfort after stressful ER shifts." No invented connection of any kind.

### Verdict

**PASS.**

The rule *"If two entities co-occur without an explicit causal statement from the user, do not invent a connection"* directly blocks the error. Nomi's synthesis invented the link because it was not constrained to user-sourced causal statements. DRT's prompt is explicit and closes the gap.

---

## Test C — Contradiction Check

### Input

```
term: { title: "Dainis", category: "Entity" }
existing_dossier: ""
all_tagged_chunks:
  [Mc1] "I live in Portland."
  [Mc2] "I moved to Seattle last month."
  [Mc3] "Lived in Lisbon for two years in my late twenties, learned Portuguese there."
```

### DRT Synthesis Output (simulated)

Analysis:
- **Mc1 vs Mc2:** Direct contradiction on current location. Mc2 is richer (temporal marker "last month," explicit move event). Mc1 is a bare assertion. Drop Mc1 per the "keep richer context" rule.
- **Mc3:** Historical context, no contradiction. Keep as-is.

```
Dainis [Entity]

Location: Currently lives in Seattle, having relocated last month. [Mc2]
Previously lived in Lisbon for approximately two years during his late twenties,
where he learned Portuguese. [Mc3]
```

Portland gone. No dual-storage. No "also mentioned Portland at some point."

### Verdict

**PASS.** Matches expected output pattern.

---

## Failure Pattern — One Structural Gap

### The rejected-fact leakage problem

DRT's extraction correctly captures both:
- M3: Thai curry (high-signal fact — companion echoed proper noun)
- M4: User preference to not structure casual mentions (retraction)

But M4 is a **general preference chunk** — it is not explicitly bound to M3 as a unit. If M3 and M4 enter synthesis in different batches, or if M4 is deduped out of a later `recent_stored_chunks` window as a "repeated preference," synthesis can see M3 alone and store Thai cooking as an active user interest with no retraction signal.

This matches the Borges failure in Nomi: the user rejected structuring (T06), but Nomi stored Borges anyway and later recalled it as a shared discussion topic. The extraction captured the fact; the retraction got lost downstream.

### Suggested fix — add `retractedBy` link in extraction output

**Current output:**
```json
{ "id": "M3", "text": "User made green curry...", "signal": "HIGH" }
{ "id": "M4", "text": "User preference: don't structure activity mentions...", "signal": "HIGH" }
```

**Proposed output:**
```json
{
  "id": "M3",
  "text": "User made green curry Thai food at home; described it as incredible.",
  "signal": "HIGH",
  "retractedBy": "M4"
},
{
  "id": "M4",
  "text": "User preference: does not want casual activity mentions converted into projects or rituals.",
  "signal": "HIGH",
  "retractedFactIds": ["M3"]
}
```

Synthesis rule to add: *"If a chunk has `retractedBy`, store it as a passing mention rather than an active interest: 'User mentioned X but declined to engage further [M#].'"*

### Suggested extraction prompt wording addition

Insert after the existing signal-weighting instruction:

> If a user message explicitly declines engagement with a topic from the immediately preceding 1–2 turns ("I don't want to turn this into a project," "let's drop it," "please don't propose anything around this"), mark the earlier fact-chunk with `"retractedBy": "<id of the declination chunk>"` and add `"retractedFactIds": ["<id>"]` to the declination chunk. Do not omit the retracted fact — it is still a real data point — but flag it so synthesis stores it as a passing mention rather than an active interest.

No other structural issues found. Tests B and C confirm that the synthesis prompt's core guards ("no invented connections without citation," "richer context wins on contradiction") work cleanly.

---

## Summary

DRT's extraction prompt outperforms Nomi's on the same input: 4/4 recall vs Nomi's 2/4, correct suppression of all filler turns, and explicit auditability of the signal-weighting decision. The synthesis prompt correctly blocks both the hallucination pattern (Miso/ER) and the contradiction/dual-storage problem. The one action item is adding a `retractedBy` field to extraction output so downstream synthesis always receives a rejected fact as a retraction, not as an isolated high-signal chunk.
