---
name: competitor-checks
description: Capture Dainis's hands-on review of an AI girlfriend competitor (paid account browsing) into a per-competitor HTML page. Use when user types /competitor-checks <site>, says "starting <site>" (for an AI girlfriend competitor), or shares notes/screenshots from a competitor review session.
---

# Competitor Checks — Workflow

This skill is for capturing Dainis's hands-on review notes while he browses paid accounts of AI girlfriend competitors (Kindroid, LoveScape, Swipey, Candy.AI, OurDream, SecretDesires, GirlfriendGPT, Promptchan, Joi.AI, SweetDream, Nomi, etc.). **Each competitor gets its own HTML file** (e.g. `candy.html`, `secretdesires.html`). `index.html` is the summary page. `competitor-checks.html` is a legacy single-file version — do not use it for new sessions.

## STEP 0 — Orient before doing anything

**Always run this before starting a new competitor session:**

```bash
git log --oneline -5          # see recent refactors that affect file structure
ls *.html                     # see which competitor pages already exist
```

Then read the nav in `index.html` to understand the current page list and naming conventions. This prevents creating files in the wrong format or missing nav links. The file structure may have changed since this skill was written.

## Trigger phrases

- `/competitor-checks <site>` — explicit start
- `starting <site>` / `let's do <site>` / `next is <site>` — implicit start

## Behavior contract

### 1. Starting a new competitor

When user signals start of a new competitor (e.g. "starting Kindroid"):

1. Run Step 0 — check git log and ls to confirm current file structure.
2. Check if `<slug>.html` already exists. If yes, resume it. If no, create it following the "Adding a new competitor page" section below.
3. Create `assets/checks/<slug>/` folder (slug = lowercased competitor name, no spaces — e.g. `kindroid`, `lovescape`, `secretdesires`).
4. Display the **Quick Reference Checklist** for that competitor in chat — see "Checklist composition" below.
5. Tell user: "Browse freely. Share screenshots (save to ~/Downloads as macOS default `SCR-*.png/jpeg`) and notes in chat. I'll catalogue."

### 2. Receiving notes

User shares free-form notes in chat. For each batch of notes:

1. Tag the note with one or more categories: `signup`, `memory`, `voice`, `video`, `image`, `chat`, `character-creator`, `billing`, `nsfw`, `ux`, `mobile`, `ick`, `standout`, `speed`.
2. Append to the **Findings** zone of that competitor's tab (chronological, with timestamp).
3. If the note describes a **standout** feature (the user explicitly flags it, or it's clearly novel vs. v2 matrix), **prompt for deep-dive**: ask Dainis to open Chrome DevTools and capture Network/Elements/Console for that feature. Suggest specific things to look for (e.g. WebSocket endpoints, API payloads, model names in response headers).
4. If user mentions **speed** that feels extra fast or extra slow, record it as a speed note. Otherwise stay silent on speed.

### 3. Receiving screenshots

When user references a screenshot ("here's a screenshot of X", or just shares one):

1. Find the newest matching file in `~/Downloads/` — typically `SCR-YYYYMMDD-xxxx.jpeg` or `.png`. Use: `ls -t ~/Downloads/SCR-*.{png,jpeg} 2>/dev/null | head -1`
2. Move it to `assets/checks/<slug>/NN-short-description.<ext>` where:
   - `NN` = next available 2-digit sequence number for this competitor (01, 02, ...)
   - `short-description` = kebab-case description from the user's note (e.g. `memory-codex-ui`, `subscription-page`, `live-video-call-button`)
3. Reference the image inline in the matching Findings entry: `<img src="assets/checks/<slug>/NN-short-description.png" class="check-shot">`

### 4. Standout feature deep-dive prompts

When a feature is flagged as standout, prompt Dainis to capture more. Match the prompt to the feature type:

- **Real-time feature (video call, voice call, streaming chat)**: "Open DevTools → Network → WS (WebSocket) tab. Reload the feature. Screenshot any WebSocket connections, copy a few frames showing the protocol."
- **AI generation (image, video, memory recall)**: "DevTools → Network → Fetch/XHR. Trigger the feature. Screenshot the request payload and response — we want model names, token counts, prompt structure."
- **Novel UI pattern**: "Right-click the element → Inspect. Screenshot the HTML structure. If it uses a JS framework, check the Console for visible component names."
- **Memory/state**: "DevTools → Application → Local Storage and IndexedDB. Screenshot what's stored client-side."

### 5. End-of-session synthesis

When user signals end of a competitor session ("done with X", "wrapping up Kindroid", or starts a new competitor), do three things:

**A. Generate Standout & Actions for Steve content:**
- One-paragraph verdict (companion vs. chatbot feel)
- Bullet list: "Steal immediately for DRT.FM" (1-5 items, ranked by impact)
- Bullet list: "DRT.FM already does better" (1-5 items)
- Bullet list: "Avoid / counter-position" (dark patterns, bad UX, billing traps)
- Final 1-10 scores for: memory, voice, image consistency, NSFW consistency, companion feel

**B. Restructure the completed page** — sessions are working tools; completed pages are reference docs. When a session ends, restructure `<slug>.html` so:
1. **Remove** the Quick Reference Checklist (was only useful during active browsing)
2. **Move Standout & Actions for Steve to the TOP** — immediately after `div.check-header`
3. **Relabel Findings** as "Session Findings" with an "Archive · YYYY-MM-DD" badge and move it below Actions
4. **Update the zone-badge** on the h2 to "Session complete · YYYY-MM-DD"

The correct completed-page order is: `check-header` → `h2 + div.actions` → `h2 + div.findings`

Use Python (not sed/awk) to do the block reordering — see `candy.html` or the Kindroid session in git history for the exact reassembly pattern.

**B2. Reorganize findings into toggle groups** — after restructuring, group the Session Findings into collapsible sections by feature area (all closed by default). This makes large finding sets navigable.

Add to the second `<style>` block:
```css
ul.steal,ul.win,ul.avoid{list-style:none;padding-left:0}
.finding-group{margin-bottom:6px}
.group-toggle{display:flex;align-items:center;width:100%;background:#0e0e16;border:1px solid #2a2a3e;border-radius:10px;padding:14px 18px;cursor:pointer;text-align:left;gap:10px;transition:background .15s}
.group-toggle:hover{background:#13131e}
.group-toggle.open{border-radius:10px 10px 0 0;border-bottom-color:#13131e}
.group-title{font-size:13px;font-weight:700;color:#e0e0e8;flex:1}
.group-count{font-size:11px;color:#5060a0;flex-shrink:0}
.toggle-arrow{font-size:9px;color:#5060a0;transition:transform .2s;flex-shrink:0}
.group-toggle.open .toggle-arrow{transform:rotate(90deg)}
.group-body{display:none;background:#07070f;border:1px solid #2a2a3e;border-top:none;border-radius:0 0 10px 10px;padding:12px;flex-direction:column;gap:12px}
.group-body.open{display:flex}
```

Replace `<div class="findings" id="<slug>-findings">` with `<div id="<slug>-findings" style="display:flex;flex-direction:column;gap:6px">`.

Wrap findings in groups:
```html
<div class="finding-group">
  <button class="group-toggle" onclick="toggleGroup(this)">
    <span class="group-title">Group Name</span>
    <span class="group-count">N findings</span>
    <span class="toggle-arrow">▶</span>
  </button>
  <div class="group-body">
    <!-- .finding divs here -->
  </div>
</div>
```

Add before `</body>`:
```html
<script>
function toggleGroup(btn) {
  var body = btn.nextElementSibling;
  var open = !btn.classList.contains('open');
  btn.classList.toggle('open', open);
  body.classList.toggle('open', open);
}
</script>
```

Group by product feature area (mirror the competitor's own nav/features). Typical groups: Homepage & Discovery · Onboarding & Signup · Character Creator · Chat & Progression · Voice & Calls · Video & Content · Image Generation · Group Chats · NSFW & Private Content · Billing & Monetization · Community · Distribution & Company. Adjust to what that competitor actually has.

Also add inline color styles to the h3 action headings inside `.actions`:
- "Steal immediately for DRT.FM" → `style="color:#4ade80;margin-top:4px"`
- "DRT.FM already does better" → `style="color:#60a5fa"`
- "Avoid / counter-position" → `style="color:#ff6b6b"`
- "Scores" → `style="color:#a0a0c0"`

Add `.actions h3{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:18px 0 8px}` to the main style block.

**C. Fill in the Top-3 in the Summary page** — find the `div.top3-card top3-pending` card for this competitor in `index.html` and replace it with a populated card:

```html
<div class="top3-card">
  <div class="top3-name">CompetitorName &#10003;</div>
  <ol class="top3-list">
    <li><strong>Feature 1 name.</strong> One-sentence description of why it matters.</li>
    <li><strong>Feature 2 name.</strong> One-sentence description.</li>
    <li><strong>Feature 3 name.</strong> One-sentence description.</li>
  </ol>
</div>
```

Top 3 = the three highest-impact / most novel things from that session — what Steve most needs to know about this competitor at a glance.

**Card ordering in index.html**: completed competitors go newest-first (most recently finished at top), pending competitors follow at the bottom. Apply this ordering to both the Progress status-grid and the Top 3 grid. Also mark the completed card with `status-done` class and "Done · YYYY-MM-DD" label.

### 6. Recommending the next competitor

After end-of-session synthesis, recommend the next competitor based on:

1. **Not yet reviewed** — check `index.html` status grid for pending competitors
2. **Highest expected learning** — prioritize competitors with most "Net-new features" claims in `ai_girlfriend_competitor_discovery_v2.md`, then competitors flagged as incumbents but not yet hand-verified.

State the recommendation as one sentence with reasoning, then ask Dainis to confirm or override.

## Checklist composition

The Quick Reference Checklist Dainis sees at start = **6-item always-on summary** + **~8-item competitor-specific list**.

### Always-on (every competitor) — 6 items

1. **Time it (seconds):** first chat response · first image · first video · first voice word · clicks from homepage → first message.
2. **Screenshots to always grab:** chat input area · subscription/upgrade page · homepage (logged in) · mobile view.
3. **Ick Test — flag any:** AI breaking character · unexpected NSFW blocks · mid-chat upsell prompts · UI bugs · moments that felt genuinely "human."
4. **Score 1-10 at end:** memory · voice emotional quality · image face consistency · NSFW consistency · overall "companion vs chatbot" feel.
5. **Steal:** one thing to copy into DRT.FM immediately.
6. **Win:** one thing DRT.FM already does better.

### Per-competitor 8-item list — how to source

1. Read `ai_girlfriend_competitor_discovery_v2.md` (in this repo, or in `~/Downloads/`) — find the "Net-new features" section for this competitor.
2. Read the existing per-competitor checklist in `competitor-analysis-v2.html` (line ~1981+, the "Dainis Checks" section) for any pre-existing items.
3. Compose 8 items: cover all "Net-new" features + signup/paywall + billing/dark-patterns. **Skip** items where v2 matrix marks the feature as ✗ (don't waste time checking what they explicitly don't have).
4. Show the 8 items to Dainis at start, with one ambient reminder: "I'll prompt for Chrome DevTools when you flag something standout."

## File layout

```
index.html                             — Summary tab (GitHub Pages root)
<slug>.html                            — one file per competitor (e.g. candy.html, ourdream.html)
competitor-checks.html                 — legacy single-file version (kept for reference)
assets/checks/<slug>/NN-*.png|jpeg     — screenshots, sequential, descriptive slug
.agents/skills/competitor-checks/       — this skill
```

## Adding a new competitor page

When starting a new competitor session, follow these steps to wire up the new page:

### 1. Add the competitor entry to the nav in ALL existing pages

In `index.html`, `kindroid.html`, `girlfriendgpt.html`, `ourdream.html`, `candy.html` (and any future pages), add a nav link before the `<span class="private-badge">` line:

```html
<a class="tab-btn tab-<slug>" href="<slug>.html"><CompetitorName></a>
```

Also add the tab colour rule to the `<style>` block in each file:

```css
.tab-<slug>{color:#<accent>}.tab-<slug>.active{background:#<dark-tint>}
```

### 2. Create the new competitor's HTML file

Copy the structure from an existing completed page (e.g. `candy.html`) and:
- Change the `id` on the section div to the new slug
- Update the nav `active` class to the new tab's class
- Replace the `check-header` h1, meta, and priority content
- Clear the findings and actions sections

**Always close `<div class="check-header">` before the first `<h2>`** — an unclosed check-header will silently eat all section content.

### 3. Compress screenshots before committing

After a session, compress all new screenshots with sips before git add:

```bash
cd assets/checks/<slug>
for f in *.jpeg; do sips -Z 1200 --setProperty formatOptions 75 "$f" -o "$f" > /dev/null 2>&1; done
for f in *.png;  do sips -Z 1200 "$f" -o "$f" > /dev/null 2>&1; done
```

Target: max 1200px on longest dimension, JPEG quality 75. Reduces ~55MB → ~29MB per session.

## Tab HTML structure (per competitor)

Use the same dark-mode styling as `competitor-analysis-v2.html`. Tabs have two states:

### Active session (in-progress)

```html
<div id="<slug>" class="section">
  <div class="check-header">...</div>

  <!-- Quick Reference Checklist (removed at session end) -->
  <h2 class="zone">Quick Reference <span class="zone-badge">Checklist</span></h2>
  <div class="quick-ref">...</div>

  <h2 class="zone">Findings <span class="zone-badge">Chronological · tagged</span></h2>
  <div class="findings">
    <div class="finding" data-tags="memory,ui">
      <div class="finding-meta">Session · memory · ui</div>
      <div class="finding-body">Note text. <img src="assets/checks/<slug>/01-description.png" class="check-shot"></div>
    </div>
  </div>

  <h2 class="zone">Standout &amp; Actions for Steve <span class="zone-badge">Filled at session end</span></h2>
  <div class="actions">
    <div class="actions-empty">Generated at session end.</div>
  </div>
</div>
```

### Completed (post-session cleanup)

When a session ends, restructure the tab into this layout — Actions float to the top, Quick Reference is removed, Findings become an archive:

```html
<div id="<slug>" class="section">
  <div class="check-header">...</div>

  <!-- Actions NOW AT TOP — no Quick Reference -->
  <h2 class="zone">Standout &amp; Actions for Steve <span class="zone-badge">Session complete · YYYY-MM-DD</span></h2>
  <div class="actions">
    <div class="verdict">...</div>
    <h3>Steal immediately for DRT.FM</h3>
    <ul class="steal"><li>...</li></ul>
    <h3>DRT.FM already does better</h3>
    <ul class="win"><li>...</li></ul>
    <h3>Avoid / counter-position</h3>
    <ul class="avoid"><li>...</li></ul>
    <h3>Scores</h3>
    <div class="scores">...</div>
  </div>

  <!-- Findings below, labeled as archive -->
  <h2 class="zone">Session Findings <span class="zone-badge">Archive &middot; YYYY-MM-DD</span></h2>
  <div class="findings">
    <div class="finding" data-tags="...">...</div>
  </div>
</div>
```

## Tone

Dainis is the product partner; Steve is the developer who will read this report. Write findings in his voice when transcribing his notes verbatim. Write the Standout & Actions zone in clear actionable language for Steve — "Build X" / "Avoid Y" / "Match Z's latency target."
