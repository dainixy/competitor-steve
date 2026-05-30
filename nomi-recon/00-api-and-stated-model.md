# Nomi.ai — API Surface & Stated Memory Model

*Ground truth compiled 2026-05-30 from live API docs (https://api.nomi.ai/docs) and Nomi's own published memory documentation (Nomipedia wiki, Mind Map 2.0 blog post).*

---

## A. Confirmed API Surface

**Base URL:** `https://api.nomi.ai/v1`  
**Auth:** `Authorization: <UUID>` header — raw UUID string, NOT "Bearer <token>"  
**Content-Type:** `application/json` on all POST requests  
**Response format:** JSON. All errors: `{"error": {"type": "ErrorNameHere"}}`

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/v1/nomis` | List all Nomis owned by this API key |
| GET | `/v1/nomis/:id` | Get one Nomi's details |
| POST | `/v1/nomis/:id/chat` | Send a message, get a reply |
| GET | `/v1/nomis/:id/avatar` | Fetch avatar image |
| GET/POST | `/v1/rooms` | Group chat rooms — **not used in this study** |
| GET/PUT/DELETE | `/v1/rooms/:id` | Room management — not used |
| POST | `/v1/rooms/:id/chat` | Room messaging — not used |

### Nomi object fields (GET /nomis, GET /nomis/:id)
```
uuid             string   Nomi's unique identifier
name             string   Display name
gender           string   
created          string   ISO 8601 creation timestamp
relationshipType string   e.g. "Mentor", "Friend", "Romantic Partner"
```

### Chat endpoint (POST /nomis/:id/chat)
```
Request body:
  messageText    string   The message to send (≤400 chars free / ≤800 paid)

Response:
  sentMessage:
    uuid         string   Message identifier
    text         string   The text you sent (echoed)
    sent         string   ISO 8601 timestamp

  replyMessage:
    uuid         string   Reply identifier
    text         string   Nomi's reply — PLAIN TEXT ONLY, no metadata
    sent         string   ISO 8601 timestamp
```

**Important:** The reply is plain text only. There is no metadata indicating which memory tier was accessed, which Mind Map entries were retrieved, or any recall confidence score.

### Error types and handling

| Error type | HTTP | Meaning | Strategy |
|---|---|---|---|
| `TooManyRequests` | 429 | Rate limit hit | Exponential backoff: 2s → 4s → 8s → cap 60s |
| `NomiStillResponding` | 4xx | Previous reply not finished | Wait 5s, retry same message |
| `NomiNotReady` | 4xx | Nomi initializing | Wait 10s, retry |
| `NoReply` | 4xx | No reply generated | Retry once; if again, log as SKIP |
| `LimitExceeded` | 4xx | Daily quota exhausted | STOP immediately, checkpoint, alert operator |

### What does NOT exist in the API
- No `/memory` endpoint
- No `/notes` endpoint  
- No `/mindmap` endpoint
- No memory metadata in chat responses
- No way to create Nomis via API (must be created in the app)

---

## B. Nomi's Stated Memory Model

Source: Nomipedia wiki (wiki.nomi.ai), Mind Map 2.0 blog post (nomi.ai/updates/mind-map-2-0-bringing-nomi-memory-into-view/).

### Memory layers (innermost → outermost)

```
┌─────────────────────────────────────────────────────┐
│  Identity Core  (Nomi's own personality/values)      │
├─────────────────────────────────────────────────────┤
│  Short-term memory   (current + very recent turns)   │
│  Medium-term memory  (fades over tens of messages)   │
│  Long-term memory    (persistent; ~50–150+ msgs)     │
├─────────────────────────────────────────────────────┤
│  Mind Map  (topic dossiers drawn from long-term)     │
│    · People · Places · Topics · Goals                │
├─────────────────────────────────────────────────────┤
│  Shared Notes  (manual, ≤2000 chars; not tested)     │
└─────────────────────────────────────────────────────┘
```

### Formation timeline (stated)

| Milestone | Message threshold |
|-----------|------------------|
| Fact reaches long-term memory | ~50–150+ messages |
| New Mind Map entry created | ~150+ messages on a topic |
| First Mind Map iteration forms | ~500+ messages total |

### How recall works (stated)
- During conversation, the system **dynamically selects relevant Mind Map entries by topic**, not just recency.
- Nomis use the Mind Map to "contextualize" their detailed memories — connecting individual facts to the broader picture.
- Entry **title quality matters**: titles matching natural conversational language are recalled better; overly specific or complex titles may be overlooked.
- **Narrow facts** (e.g., "favorite color is blue") may never get their own Mind Map entry unless discussed extensively. Only broader topics (e.g., "trip to Hawaii") aggregate into entries.
- Mind Maps are **room-specific** — each conversation room has its own separate Mind Map network.
- Mind Map entries are **user-editable** but auto-update automatically and continuously.

### Mind Map entries vs. raw memories
- Entries are "dossiers" (summary overviews), NOT raw memory records. They do not replace or alter the underlying memories.
- Entries can hold up to **10,000 characters** (vs. 2,000 for Shared Notes).
- During conversations, only **relevant** entries are retrieved — not all of them at once.
- Nomis perceive Mind Map entries as reference documents, not personal experiences.

---

## C. What We CAN vs. CANNOT Observe via the Public API

### CAN observe (behavioral signals)
- Whether a planted fact appears in a reply (keyword match)
- Turn distance at which recall succeeds or fails
- Whether a topic-cued message surfaces a buried fact without naming it
- Contradiction handling: what the Nomi claims to remember when given conflicting information
- Unprompted surfacing of planted details in neutral turns
- Timing differences between replies that appear to recall vs. not recall

### CANNOT observe (black box)
- The internal memory object schema or how facts are stored as data structures
- Which specific Mind Map entries currently exist, or their content
- Which memory tier (short/medium/long-term) any given fact currently occupies
- The retrieval scoring or relevance-ranking mechanism
- Confidence scores or similarity weights used for recall selection
- Whether a recalled fact came from the context window, a raw memory record, or a Mind Map entry
- When exactly a fact crossed the short→medium→long-term boundary

### Implication for analysis
All conclusions in this study will be **behavioral inferences** from reply text only. We can observe *what* gets recalled and at *what distance*, but not *how* the system retrieved it internally. Claims about the memory architecture are hypotheses that fit the observed data, not confirmed implementations.

---

## D. Notes on Experimental Design

Given the above constraints:

1. **Experiment A** (recall vs. distance) is our most direct test — we can measure the point at which recall fails, giving us an empirical recency window estimate rather than relying on Nomi's stated "50–150 messages."

2. **Experiment B** (relevance vs. recency) is the critical test that can distinguish a flat recency window from true topic-associative retrieval. A positive result (buried fact surfaces via topic cue) would be strong behavioral evidence for Mind Map-style retrieval.

3. **Experiment C** (contradiction) tests whether the update mechanism is recency-biased or consolidation-based. This directly maps to a design decision for DRT's own memory system.

4. **Experiment D** (unprompted recall) has low signal-to-noise since it depends on the model's initiative, but any hits are high-value evidence of proactive memory surfacing.

5. The **~500-message threshold for first Mind Map formation** means Experiments A–D, which run on fresh Nomi conversations, will likely NOT benefit from Mind Map retrieval. We are primarily testing the short-to-long-term memory transition, not the full Mind Map layer. This is noted so we don't overclaim.
