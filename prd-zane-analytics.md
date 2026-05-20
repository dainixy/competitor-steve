# PRD — Zane Analytics, Phase 0

**Status:** ready-for-agent
**Owner:** built in Claude Code against the `yt-zane` repo
**Date:** 2026-05-12

---

## Problem Statement

We publish the same Zane video to 7 social channels every day via Blotato (YouTube, Instagram, TikTok, Bluesky, Facebook, Threads, Twitter), but we have no idea why some channels are dying. We don't know which channels are dead, when the decline started, or whether the failure is a hook problem, a body retention problem, an algorithm hit, or a cold-start failure that never broke through. Manually clicking into 7 different platform dashboards every week to check is a non-starter — the operator has zero time for that and no technical baseline to interpret what they'd see.

We need a way to pull analytics from all 7 channels into one machine-readable place, then have an LLM diagnose what's happening and recommend specific adjustments — with as close to zero ongoing human involvement as possible.

## Solution

Two pull scripts, one analyse script, one weekly cron, one HTML report.

Phase 0 stack: Blotato API (already paid for, all 7 channels) + YouTube Analytics API (free, OAuth, gives retention curves + traffic source + demographics on the highest-cadence channel). No Apify, no Metricool, no Meta or TikTok app review — those are explicit Phase 1+ escalations gated on what Phase 0 data reveals.

Every week, the cron pulls fresh metrics from both sources, joins them against existing scene metadata on disk (script text, pillar, hook style), and asks Claude Sonnet to diagnose. The operator reads one HTML report. Total operator click count after first-time OAuth: zero.

## User Stories

1. As the operator, I want a single weekly HTML report covering all 7 channels, so that I don't have to log into 7 dashboards to figure out what's working.
2. As the operator, I want the report to rank channels by views-per-post normalised across the YouTube cadence asymmetry (YT 3×/day vs others 1×/day), so that "YouTube wins" isn't a misleading artefact.
3. As the operator, I want the report to tell me which channels are dead, with a specific date range when the decline began, so that I can correlate it to changes I made.
4. As the operator, I want the report to classify each dead channel as "sudden cliff," "slow decay," or "never took off," so that I know whether to look for an algorithm event, a content drift, or a distribution failure.
5. As the operator, I want the report to show where viewers drop off in YouTube videos (mapped to hook style and content pillar), so that I can see whether the hook is failing or the body is failing.
6. As the operator, I want the report to show which traffic source dominates on YouTube (recommendation vs search vs follower feed) and flag any sharp recommendation-share decline, so that I can detect algorithm hits early.
7. As the operator, I want top-5 and bottom-5 posts by performance, with the actual hook text inline, so that I can pattern-match what's working.
8. As the operator, I want three specific testable adjustments per report, so that I know what to change next.
9. As the operator, I want the report to honestly state what it can't diagnose and what extra data would resolve it, so that I can make an informed Phase 1 escalation decision.
10. As the operator, I want OAuth to be a one-time click, so that I'm never asked to re-authenticate routinely.
11. As the operator, I want the analytics pull to skip posts younger than 48 hours, so that I'm not making decisions on unsettled metrics.
12. As the operator, I want posts to be re-fetched at age 7 days and 30 days, so that the long-tail performance is captured (videos can surface late).
13. As the developer (Claude Code), I want a `BlotatoClient` module with a simple interface, so that pagination, rate limiting, and auth aren't smeared across the codebase.
14. As the developer, I want a `YouTubeAnalyticsClient` module that hides OAuth token refresh and batch query construction, so that the orchestrator stays linear and readable.
15. As the developer, I want a `SceneJoiner` module that maps analytics back to scene IDs via the post URLs in existing `blotato-manifest.json` files, so that the join logic lives in one place.
16. As the developer, I want the raw API responses written to disk under `analytics/<scene_id>/<platform>.json` as versioned snapshots, so that re-running the pull doesn't lose history.
17. As the developer, I want a flat `analytics/rollup.csv` next to the HTML report, so that I can eyeball data quality without parsing JSON.
18. As the developer, I want all production config (API endpoints, refetch intervals, model IDs) to live in `production.yaml`, not hardcoded, per the yt-zane project invariant.
19. As the developer, I want unit tests for the three deep modules only (`BlotatoClient`, `YouTubeAnalyticsClient`, `SceneJoiner`), so that infrastructure isn't tested but real logic is locked.
20. As the developer, I want the pull script to be idempotent and resumable, so that a partial failure doesn't require a full re-run.
21. As the developer, I want explicit Phase 1 decision gates documented in the report output itself, so that escalation criteria are visible at the moment of decision (not buried in a separate doc).
22. As the operator, I want the report to auto-open in the browser after generation, so that I don't have to find the file.

## Implementation Decisions

### Modules

**`BlotatoClient` (deep)**
- Wraps `https://backend.blotato.com/v2`
- Auth: `blotato-api-key` from existing `.mcp.json` (read once at construction)
- Methods: `list_posts(since, until, status='published', platforms=None) → iterator`, `get_post_analytics(post_id) → dict`
- Hides: cursor pagination, 30 req/min rate limit (token bucket), retries with exponential backoff on 429/5xx
- Returns raw dict — no transformation. Schema validation happens in `SceneJoiner`.

**`YouTubeAnalyticsClient` (deep)**
- Wraps YouTube Analytics API v2 via `google-api-python-client`
- Auth: OAuth 2.0 desktop flow. Token cached to `.youtube-token.json` (gitignored). Auto-refresh via `google-auth-oauthlib`.
- Methods: `query_retention(video_ids, start, end)`, `query_traffic_sources(video_ids, start, end)`, `query_demographics(video_ids, start, end)`
- Each method issues one batched `reports.query` call with the right metrics/dimensions for that signal
- Returns raw API responses keyed by video ID

**`SceneJoiner` (deep)**
- Input: a scene_id
- Output: a single record combining `scenes/NNNN/meta.json` (script, pillar, hook style), `scenes/NNNN/artifacts/blotato-manifest.json` (post URLs, caption), and all per-platform analytics JSONs under `analytics/NNNN/`
- Critically: extracts platform-native post IDs from the URLs in `blotato-manifest.json` for the YouTube join (YT API uses video IDs, Blotato uses its own post IDs)
- Validates that every channel mentioned in `blotato-schedule.py PLATFORMS` is accounted for (missing platforms surface as gaps in the report, not silent zeros)

**`AnalyticsStore` (shallow)**
- File-IO wrapper with versioned snapshots
- Each fetch writes `analytics/<scene_id>/<platform>-<UTC-timestamp>.json`
- Lookup helpers: `latest(scene_id, platform)`, `history(scene_id, platform)`, `age_buckets(scene_id, platform)` (returns the 2d/7d/30d snapshots)

**`Diagnoser` (shallow)**
- Builds the Sonnet prompt from the joined dataset + `channel-brief.md`
- Calls `claude-sonnet-4-6` via Anthropic SDK with prompt caching on the static parts (channel brief, system prompt)
- Writes `analytics/report-YYYY-MM-DD.html` and `open`s it

**Orchestrator scripts (shallow glue)**
- `pipeline/17-pull-analytics.py` — drives BlotatoClient + YouTubeAnalyticsClient + AnalyticsStore. Idempotent. Resumable via the timestamped snapshot files (skip if snapshot for this age-bucket already exists).
- `pipeline/18-analyse-analytics.py` — drives SceneJoiner + Diagnoser. Produces rollup CSV + HTML report.

### Snapshot policy

For each post, fetch metrics at these ages:
- `~48h` (first read — metrics settled)
- `~7d` (short tail)
- `~30d` (long tail)

The pull script reads the existing snapshots and only fetches the next missing age-bucket. Posts already at 30d+ are skipped on subsequent runs.

### YouTube ↔ Blotato join

YouTube videos are referenced by `videoId` in the Analytics API. Blotato stores the public `postUrl` (e.g. `https://youtube.com/shorts/<videoId>`) on the published-post record. `SceneJoiner` parses the videoId out of the URL — single regex, no API round-trip needed.

### Cadence asymmetry handling

`SceneJoiner` emits records with a `cadence_weight` field equal to `1/posts_per_day_for_that_platform`. The CSV rollup and the Sonnet prompt both reference this so per-platform comparisons are normalised. YouTube's ~3×/day vs others' 1×/day will not produce misleading rankings.

### Sonnet prompt structure

System prompt (cached): role description + the diagnostic framing from the channel brief.
User message (not cached): the joined CSV + any platform-specific notes for this run.

Prompt asks for: (1) channel ranking by views/post, (2) cliff/decay/cold-start classification, (3) YT retention drop-off points × hook style × pillar, (4) YT traffic source breakdown and recommendation-share trend, (5) top/bottom 5 posts with hook text, (6) three testable adjustments, (7) honest limitations and what data would resolve them.

### Config

New section in `production.yaml`:

```yaml
analytics:
  blotato:
    base_url: "https://backend.blotato.com/v2"
    rate_limit_per_min: 30
  youtube:
    token_path: ".youtube-token.json"
    client_secrets_path: ".youtube-client-secrets.json"
  snapshots:
    age_buckets_hours: [48, 168, 720]
  diagnoser:
    model: "claude-sonnet-4-6"
    max_tokens: 8000
```

Per the yt-zane "all production config in production.yaml" invariant — no hardcoded endpoints or model IDs anywhere else.

### Compliance with yt-zane project rules

- `CHANGE.md` required at root before touching `production.yaml` or `pipeline/` (yt-zane invariant)
- Pre-commit hook will block until `CHANGE.md` lands and is approved
- After the change ships, `CHANGE.md` archives to `CHANGELOG/2026-MM-DD-analytics-phase0.md`
- `ARCI/Architecture.md` and `ARCI/Implementation.md` get updated in the same commit (documentation-sync invariant)

## Testing Decisions

A good test exercises the external behaviour of a module against fixture inputs. It does not assert on internal call counts, private method invocations, or the existence of specific intermediate state. If the module returns the right shape for the right input, the test passes — regardless of how the internals are organised.

**`BlotatoClient` tests** (`tests/test_blotato_client.py`)
- Mock HTTP via `responses` or `respx`. No live API.
- Pagination: simulate a 3-page list, assert all items returned.
- Rate limit: hammer the mock; assert no more than 30 calls in any 60s window.
- Retry: 429 followed by 200 → returns the 200 body.
- Error: persistent 500 raises after backoff exhausted.
- Prior art: none in yt-zane currently. Pattern to mirror: keep mocks at the HTTP boundary, not at the requests-library boundary.

**`YouTubeAnalyticsClient` tests** (`tests/test_youtube_analytics_client.py`)
- Mock the google-api-client `discovery` build → return a stub that records calls.
- Assert: `query_retention` constructs a single batched `reports.query` with the right metrics and dimensions for N video IDs.
- Assert: token refresh path is taken when the cached token is expired (use a fake expired token fixture).
- No live OAuth. No live API.

**`SceneJoiner` tests** (`tests/test_scene_joiner.py`)
- Fixture-driven. Build a `tests/fixtures/scenes/0099/` directory with a known `meta.json`, `blotato-manifest.json`, and matching `analytics/0099/*.json` files.
- Assert: joined record has correct keys for all 7 platforms.
- Assert: a missing platform analytics file surfaces as `None` in the joined record (not a KeyError).
- Assert: YT videoId is correctly parsed from the postUrl regardless of URL variant (`/shorts/<id>`, `?v=<id>`).
- Assert: `cadence_weight` is `1/3` for YouTube records and `1/1` for the other 6.

**Skip tests on:** `AnalyticsStore` (thin file IO), `Diagnoser` (LLM output is nondeterministic; would test the mock), orchestrator scripts (glue — exercised end-to-end by manual smoke test).

**Smoke test (manual, one-off):** run `17-pull-analytics.py` against the current yt-zane scene list, then `18-analyse-analytics.py`. Assert the HTML report opens and contains all 7 platforms.

## Out of Scope

- Apify scrapers for IG/TikTok depth. Reserved for Phase 1 if the gate criteria fire.
- Metricool integration. Reserved for Phase 1 if non-YT retention is needed.
- Meta Graph API (Instagram/Facebook/Threads Insights). Reserved for Phase 2+ if Metricool isn't sufficient.
- TikTok Business API. Same as Meta — Phase 2+ only.
- X API Basic ($200/mo). Rejected entirely until X becomes a top-3 channel by views.
- Competitor benchmarking. Phase 1+ via Apify if useful.
- Per-day historical backfill earlier than channel launch. We only care about Zane's own posts.
- Real-time / sub-48h metrics. Settled metrics only.
- Multi-account support. Single Zane channel only.
- Dashboard UI. The HTML report is the dashboard.
- Slack/email delivery of the report. Manual file-open is fine for Phase 0.

## Further Notes

**Why Phase 0 before more:** Three independent research agents (Claude, Grok, Kimi) converged on YouTube Analytics API as the highest-signal free addition, and disagreed only on whether to add Apify (~$10/mo, scraper maintenance) or Metricool (~$28/mo, no engineering) for the other 6 channels. The 80/20 move is to ship without either and see what the data tells us. Blotato + YT covers all 7 channels at baseline and gives full diagnostic depth on the highest-cadence channel. If that's enough to identify the failure modes, we never spend the marginal money. If it isn't, the report itself tells us exactly which Phase 1 escalation to take.

**Decision gate (built into the report output):** the Sonnet prompt asks the model to state, at the end of every report, which Phase 1 escalation (if any) the data justifies. Options are:

- *Stop here* — diagnosis is actionable from the data we already have.
- *Add Metricool* (~$25–30/mo) — needed if follower/non-follower reach split is required to confirm IG/TT hypotheses.
- *Add Apify* (~$5–15/mo) — needed for per-post depth on IG/TT or competitor benchmarking.
- *Escalate to native Meta/TikTok APIs* — only if both above prove insufficient.

**Risk:** YouTube OAuth token refresh has a known failure mode where Google revokes refresh tokens after 6 months of inactivity for unverified apps. Mitigation: weekly cron exercises the token; if revocation happens anyway, the pull script writes a `RE-AUTH-NEEDED` flag file that the next report links to.

**Risk:** Blotato API returns metrics only for posts Blotato published. Any manual cross-posts are invisible. Mitigation: explicitly call this out in every report so trends aren't misread.

**Risk:** scenes that pre-date the analytics system have no historical snapshot at the 48h / 7d marks. Mitigation: backfill what's available on first run, mark older posts as "historical-only" in the rollup so the report doesn't compare them against fully-instrumented posts.
