#!/usr/bin/env python3
"""Build steve-insights.html from Steve's 6 markdown competitor reviews.

Reads ~/Downloads/Steve -competitor checks/*.md, converts each to HTML,
and assembles a single dark-mode page with:
  1. Hero
  2. Cross-cutting architecture insights (hand-synthesized from Steve's docs)
  3. Framework Steve wants the AI to use (verbatim from the kindroid-ggpt file)
  4. Per-competitor key insights cards (hand-synthesized)
  5. Deep notes tabs (markdown -> HTML for each file)
"""

import re
from pathlib import Path

SRC_DIR = Path("/Users/admin/Downloads/Steve -competitor checks")
OUT_PATH = Path("/Users/admin/Documents/claude/drt-steve/steve-insights.html")

FILES = [
    # (tab id, file name, display name, color class)
    ("kindroid",     "1-kindroid-gptgirlfriend-steve.md", "Kindroid + GirlfriendGPT", "tab-kindroid"),
    ("candy",        "DAINIS_RESPONSE_CANDY_AI (1).md",    "Candy.AI",                 "tab-candy"),
    ("nomi",         "DAINIS_RESPONSE_NOMI.md",            "Nomi",                     "tab-nomi"),
    ("ourdream",     "DAINIS_RESPONSE_OURDREAM.md",        "OurDream",                 "tab-od"),
    ("secretdesires","DAINIS_RESPONSE_SECRETDESIRES.md",   "SecretDesires",            "tab-sd"),
    ("sweetdream",   "DAINIS_RESPONSE_SWEETDREAM_AI.md",   "SweetDream",               "tab-sweetdream"),
]


# ---------- Markdown -> HTML ----------

def inline_md(text: str) -> str:
    """Inline transformations: backtick code, bold, italics."""
    # Escape HTML first
    text = (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))
    # Inline code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # Italics (single asterisk, avoid double-asterisk leftovers)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def md_to_html(md: str) -> str:
    """Minimal but accurate converter for Steve's specific markdown patterns."""
    lines = md.split("\n")
    out = []
    paragraph: list[str] = []
    in_ul = False
    in_ol = False

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            joined = " ".join(p.strip() for p in paragraph).strip()
            if joined:
                out.append(f"<p>{inline_md(joined)}</p>")
            paragraph = []

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    for line in lines:
        stripped = line.rstrip()

        # Blank line: end paragraph and lists
        if not stripped.strip():
            flush_paragraph()
            close_lists()
            continue

        # Headings
        if stripped.startswith("### "):
            flush_paragraph()
            close_lists()
            out.append(f'<h3 class="md-h3">{inline_md(stripped[4:].strip())}</h3>')
            continue
        if stripped.startswith("#### "):
            flush_paragraph()
            close_lists()
            out.append(f'<h4 class="md-h4">{inline_md(stripped[5:].strip())}</h4>')
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            close_lists()
            out.append(f'<h3 class="md-h3 md-h3-major">{inline_md(stripped[3:].strip())}</h3>')
            continue

        # Steve's quote pattern: `+ "quote": ...`
        if stripped.startswith('+ "quote":'):
            flush_paragraph()
            close_lists()
            quote_text = stripped[len('+ "quote":'):].strip()
            out.append(
                f'<div class="dainis-quote"><span class="quote-label">Dainis quote</span>'
                f'<div class="quote-body">{inline_md(quote_text)}</div></div>'
            )
            continue

        # Bullet list
        if stripped.lstrip().startswith("- "):
            flush_paragraph()
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            content = stripped.lstrip()[2:]
            out.append(f"<li>{inline_md(content)}</li>")
            continue

        # Numbered list (1. ... 9.)
        ol_match = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if ol_match:
            flush_paragraph()
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(ol_match.group(2))}</li>")
            continue

        # Normal text -> add to paragraph buffer
        paragraph.append(stripped)

    flush_paragraph()
    close_lists()
    return "\n".join(out)


# ---------- Per-competitor synthesized data ----------
# These are TOP insights I'm pulling from Steve's full notes for the summary cards.

PER_COMP_CARDS = [
    {
        "id": "kindroid",
        "name": "Kindroid",
        "color": "tab-kindroid",
        "anchor": "deep-kindroid",
        "insights": [
            ("Talking-head wraps the existing chat brain, not replaces it",
             "User speaks → STT → existing LLM/chat (memory, personas, history intact) → response goes to voice/video instead of UI → loop. Alexis already works this way conceptually. Talking-head should be the scalable layer for ALL characters; Alexis stays as the premium 3D flagship. Don't make them separate product worlds."),
            ("Camera vision is cheap to add: periodic frame capture → vision model → short description → inject into LLM context",
             "Smarter pattern: only trigger extra vision calls when the user says 'look at this' or 'what is this?' Don't need native multimodal LLMs — a separate vision service is enough for high-impact moments like noticing clothing or surroundings."),
            ("Reset chat needs two modes",
             "DRT's current reset chat only deletes messages, NOT semantic memories. Equivalent of Kindroid's behavior: 'Reset chat/messages only' (current) and 'Reset chat + memories' (new destructive opt-in)."),
            ("LLM/model selection is heavier than it looks",
             "Exposing a model selector is trivial code; the hard part is prompting and QA. Imari spent real time stabilizing the current models. Letting users pick multiple models multiplies failure modes (empty responses, broken tone, lost consistency). Do not prioritize before current LLM reliability is fixed."),
            ("LiveKit confirmed for calls — but the exact endpoints don't matter",
             "`get-call-token` returns server URL + room + token + voice_avatar_provider. What matters is the shape: LiveKit-style real-time transport with AI/voice/video work hidden server-side. WebRTC binary streams confirm media is invisible to normal HTTP capture."),
            ("Memory: don't over-credit Kindroid",
             "UI labels suggest deep memory but the journal-recall test (favorite color) didn't succeed. Recall may be keyphrase-based rather than true vector retrieval. Backstory + response directive + key memories + example message + journal entries look like prompt assembly more than magic."),
        ],
    },
    {
        "id": "girlfriendgpt",
        "name": "GirlfriendGPT",
        "color": "tab-ggpt",
        "anchor": "deep-kindroid",  # GGPT is in the same file as Kindroid
        "insights": [
            ("'Recent Chats per character' is structural, not a UI tab",
             "DRT's `getChatByCharacterAndUser()` and `getOrCreateChat()` reuse one chat per user per character. Multiple threads per character = changing the chat model, reset behavior, chat lists, message loading, AND memory scoping. Kindroid is closer to DRT here; GGPT is structurally different."),
            ("Public character usage is a binary product-direction choice",
             "GGPT-style: users chat with public originals, creators matter as profiles, reviews live on the character. Kindroid/DRT-style: users duplicate to private copy first, social profiles for characters, feed-based discovery. Scoring rules (likes/comments/usage) depend on which you pick — child copy vs rolled-up to parent vs the public character."),
            ("Canvas without unified schema = 4 fragmented generation surfaces",
             "DRT already has: in-chat (WordPress character fields), gallery (`/create/futanari-image-generator` schema), and RunPod/spoke. Adding GGPT-style Canvas as a 4th makes users reasonably ask: why can't gallery images become characters? why don't chat images behave like gallery? Treat Canvas as a generation-architecture decision, not a page."),
            ("Beamer integration confirmed — small/medium DRT lift",
             "Network shows user ID, email, name, language, plan/free filter, notification state passed in. Supports changelog, in-app announcements, browser push, email, segmentation. The lift is mostly SaaS + deciding what updates to publish."),
            ("Dark/light theme + NSFW toggle are NOT toggles",
             "Light mode means designing light mode across the whole site first. NSFW filter is currently useless because all characters are NSFW; turning it off would leave nothing unless we create real SFW inventory."),
            ("Public-character moderation becomes mandatory at scale",
             "Report modal categories (underage, real person, ads/spam, copyright, other) and review systems aren't optional — they're a prerequisite for opening public character creation/usage."),
            ("Suggested replies and user personas already exist in DRT",
             "GGPT's 'Chat Profiles' isn't missing; it may just be under-surfaced compared to how visible their account tab makes it."),
        ],
    },
    {
        "id": "candy",
        "name": "Candy.AI",
        "color": "tab-candy",
        "anchor": "deep-candy",
        "insights": [
            ("Candy is server-rendered Rails/Turbo, not a heavy SPA",
             "Routes like `/home/live_actions`, `/home/live_audio`, `/companions/anais/scenes_content` return HTML/Turbo Stream fragments. This makes per-character feature gating easy without a fully client-side architecture."),
            ("Interactive Stories = pre-rendered branch graph, not live generation",
             "`/interactive_stories/{slug}/episodes/{ep}/choices` with `option_slug=give_em_hell`. Paywall resume URL `?from_scene=clip_3&status=payment_success` preserves narrative state across payment — payment becomes part of the story state machine, not a billing detour."),
            ("Romance Mode 'presence' = pre-rendered idle videos per scene/outfit combo",
             "DOM loads multiple `companion-scene-{uuid}-av1.mp4` videos with opacity/z-index swap. `/companions/anais/select_scene` with `id=11&type=location|outfit` swaps the asset set. Cost = asset production + storage, NOT live inference. Gifts trigger reaction videos + chat prose — gifts are monetized media events, not metadata."),
            ("Live Action is a clip-entitlement system, not generation",
             "`/user_purchases/live_actions` returns ready H.264/AV1 URLs immediately with `character_state: \"clothed\"`. XP/token gates which clips you can play. The system feels earned because of XP; the endpoint reveals it's an operationally gated video library."),
            ("Calls use ElevenLabs Conversational AI",
             "Signed websocket URL `wss://api.elevenlabs.io/v1/convai/conversation?agent_id=...&conversation_signature=...`. Candy outsources realtime audio + VAD + alignment + transport, then keeps transcript first-party by posting `/audio_messages` with conversation_id, call_id, body, role."),
            ("In-chat image generation is structured prompt IDs, not free text",
             "`/messages` sends `gen_ai_suggestion_id` and `gen_ai_prompt_id`; the prompts themselves live at `/gen_ai_suggestions/prompts`. 'Natural' image UX is structured prompt selection under the hood."),
            ("Video provider routing by content type",
             "SFW prompts use `provider: \"kling\"` with `durations: [5]`. NSFW prompts use `provider: \"pika\"` with `durations: [5, 10]`. Some NSFW categories ship `excluded_for_model_types: [\"big_love\"]`. They route by content category and model capability, not one generic provider."),
            ("Character creation persists a real draft before final",
             "UUID in `/characters_v2/{uuid}/edit_attribute`. `/regenerate_face?regenerate_face=true` is cheap because attributes already live on the draft. Final `/bring_my_ai_to_life` is both creation fee and psychological commitment point. `/user_feedbacks/sd_faces` with `sd_face_id` + `reaction=like` also gives them training data on generated faces before character is finalized."),
            ("Group chat is one conversation context, not stitched chats",
             "`/conversations/{id}/group_chat_continuation` — one LLM turn can emit multiple character messages. `/group_chat_scene` suggests media generation can use multi-character state as one scene prompt. Hard part is context partitioning and speaker control, not the UI."),
        ],
    },
    {
        "id": "nomi",
        "name": "Nomi",
        "color": "tab-nomi",
        "anchor": "deep-nomi",
        "insights": [
            ("The Nomi memory delta to DRT is the SECOND-ORDER index, not summaries",
             "DRT already has semantic memory rows (`semantic_memories` with summary, chatId, personaId, characterSlug, etc.). Missing layer: `memory_terms` table (title/category/dossier/priority/state/selected/candidate/locked/userEdited/aiEdited/memoryIds/memoryCount/importanceScore) + `memory_term_edges` (graph) + background term extraction after createSemanticMemory + retrieval that selects high-priority + relevant terms rather than just the latest 10 summaries."),
            ("Nomi uses REST for writes, Socket.IO for async truth",
             "Browser posts an action → gets immediate object or job id → waits for `NomiChatEvent` / `UserEvent` over `wss://beta.nomi.ai/socket/?EIO=4&transport=websocket` to reconcile UI. Chat replies, creation status, Shared Note normalization, speech, selfie status, video completion all arrive over websocket."),
            ("Nomi creation = async bootstrap pipeline, not a single save",
             "`POST /api/nomis` returns `status: \"Creating\"`. Socket.IO then emits: `nomi_status → Default`, generates Shared Notes (boundaries draft, appearances `nomiAppearance` / `v4NomiAppearance` / `nomiChatAppearance`), inserts starter message. Creation feels alive because the bootstrap happens after the record exists."),
            ("Private workspace home — no marketplace at all",
             "`/api/home` returns ordered personal entries (`nomiId` / `groupChatId` / `homeFolderUuid`) plus folders. NO public characters, NO creator graph, NO clone economy in the captured surface. Radically different product thesis from every competitor."),
            ("ElevenLabs BYOK is data-modelled — but DRT has a singleton-client trap",
             "Nomi object includes `voiceSource`, `builtInVoiceId`, `customVoiceId`, `elevenLabsVoiceId`. DRT-specific warning: `elevenlabs-api-service.ts` has a module-level `let elevenlabs: ElevenLabsClient` singleton — UNSAFE for BYOK because the first user's key sticks as the global client. Need per-request client or per-user fingerprint cache, never one global."),
            ("Group chat is turn-orchestrated with a backchanneling flag",
             "Group object has `nextSpeakerNomiId`; continuation calls `/request-next-speaker` with `autoRepliesNum`. Backchanneling enabled = response context includes that Nomi's private memories/notes plus group transcript. Disabled = only group-level note/memory. This is the boundary that lets group chat be either 'extension of private relationships' or 'self-contained adventure.'"),
            ("Mind Map categories map to internal taxonomy",
             "UI Lore=`Entity`, Topics=`Keyword`, Goals=`Goal`. API returns `highPriorityTermCountForCategory` so the high-priority cap is enforced at API, not just UI copy. `memoryCount: 0` on manual entries means terms are EXPECTED to link to underlying memory records once enough conversation accumulates."),
            ("Shared Notes are draft-aware async context",
             "Changes return `backstoryDraft` + `backstoryStatus: \"Pending\"` while the previous `backstory` stays committed. Notes are asynchronously validated/rewritten/propagated, not saved as blind text. `/api/shared-notes/backstory/expand` returns a `jobId` — background enhancement."),
            ("Image edit is a separate job model with NSFW score",
             "`/api/selfie-images/{id}/image-edit-requests` returns `imageEditRequestUuid`; browser polls `/api/image-edit-requests/{uuid}` until `Completed`. Includes `parentImageEditRequestUuid` (edit chains), `nsfwScore`, `memory`. `UserEvent: ImageEditRequestCompleted` fires globally."),
        ],
    },
    {
        "id": "ourdream",
        "name": "OurDream",
        "color": "tab-od",
        "anchor": "deep-ourdream",
        "insights": [
            ("OurDream is a creative media studio with companion bolted on, not a companion product",
             "Separate service surfaces for chat, generation, audio, feedback, community rankings, public collections, notifications, and search. Their roadmap likely optimizes for media output, creator supply, and coin velocity more than pure companion quality."),
            ("Bugs/Features board is FIRST-PARTY tRPC, not Zendesk",
             "`feedback.create`, `feedback.toggleUpvote`, `feedback.addComment`, `feedback.getBySlug`, `feedback.deleteComment`. Zendesk = public help center, Front = support email routing. They built the product feedback board in-app because they want votes/status/changelog inside the experience."),
            ("Voice calls confirmed LiveKit Cloud",
             "Voice session start returns `wss://ourdream-538xbbnc.livekit.cloud`. Token has LiveKit-style permissions: `roomJoin`, `canPublish`, `canSubscribe`, `canPublishData`. The weak call UX is product/orchestration (passive character, no initiative, leaky roleplay context), NOT lack of realtime infra."),
            ("Video metadata exposes provider routing",
             "Job records include `provider: \"wavespeed\"` (with `videoModel: \"wan-2.7-spicy\"`) and `svi`, plus `performanceMode`, `coinsConsumed`, `lengthMs`, `inputImageUrl`, `audioText`, `voiceId`, `originalVideoId`. UI sells 'Spicy 1.0/2.0'; backend reveals provider + model + quality + cost accounting + job tracking."),
            ("Async generation is the universal pattern: triggerRunId placeholder → notification with final URL",
             "Scene/edit endpoints return immediately with `imageUrl: null`, `triggerRunId`, message shell. Notifications carry job state and final media. Users can keep chatting/browsing while jobs finish. App treats generation as a background job queue with UI placeholders + activity inbox."),
            ("Memory cap (15K Pinned + 15K Custom Instructions) is context-budget partition, not a vector failure",
             "Auto Memory Log + Pinned Memories + Custom Instructions. The 15K cap is almost certainly latency/cost/quality/model-partition tuning, not a broken vector store. The user-relations issue is communication, not architecture."),
            ("Character search uses Typesense with creator metadata merged",
             "`0pwc4xvbo6znaj57p.a1.typesense.net/collections/character/documents/search`. Fields: name, tags, embed_text, visibility, estimated_message_count, like_count, created_by_user_id, plus `$public_profile(username, avatar_url)`. Discovery is an indexed public catalogue, not just a DB list."),
            ("Roleplay engine leaks scene-state markers inside generated text",
             "Hidden-ish HTML comment with fields like `scn`, `loc`, `dt`, `wth`, `chpr`, `usr`, `cst`, `mem`, `flags`, `loop`. Explains both strong immersive continuity AND the repeated context headers that annoy users and leak into voice."),
            ("Donations + creator economy are native first-party",
             "Activity API records `donation_received` with amount/sender/recipient/message/hidden/anonymous flags. Three leaderboard dimensions hit separate endpoints: `profile.getTopCreators` (followers/characters/messages), `profile.getTopCharacters` (messages/likes), `profile.getTopPacks` (purchases/media counts)."),
        ],
    },
    {
        "id": "secretdesires",
        "name": "SecretDesires",
        "color": "tab-sd",
        "anchor": "deep-secretdesires",
        "insights": [
            ("Public/community characters are cloned into private user-owned partners",
             "`/api/character/privatize/{publicCharacterId}` returns a new private `_id`, `parent_char_id`, `cloned_from_public: true`, and a new conversation entry. That's why community partners can be deeply edited after selection. Template marketplace, not shared social graph — the same model DRT uses."),
            ("Per-character settings silently override global account defaults",
             "Account can globally have `isImage/isVoice/isCall: true` while a new character defaults to `false`. This causes the 'feature feels broken until I find the buried switch' UX problem. Feature availability = subscription + global defaults + per-character override, and UI usually only surfaces one layer."),
            ("Auto-memory is a VISIBLE field on the character record",
             "`auto_memory_notes` is right next to editable `user_memory_notes`. The captured first-person summary covered context, user behavior, conversation events, inferred relationship tone. Recurring conversation summarization → readable per-character memory field → fed back into future chat. More transparent than a hidden vector."),
            ("Character creation is a staged partial DB record",
             "`/api/character/partial` returns `character_id` + image `run_id`. `/api/chat/generate_about_me` writes persona text. PATCH finalizes. Flexible editing but more chances for half-created broken states."),
            ("'Video' tab is actually text → image → I2V under the hood",
             "Progress events show `step_name: \"image_saved\"` at progress 80 BEFORE `step_name: \"video_saved\"` at 100. Even from the video tab, SD first generates a still then runs image-to-video. Live Photo uses the same endpoint with `imageToVideo: true` and an existing image id."),
            ("Cartesia Sonic-2 confirmed for TTS — slow voice elsewhere is config, not tech",
             "Calls open `wss://api.cartesia.ai/tts/websocket` with `model_id: \"sonic-2\"`, voice `mode: \"embedding\"`, `max_buffer_delay_ms: 0`, raw PCM streaming. Provider can stream fast. Slow competitor voices are voice/prosody/playback defaults or punctuation-heavy generation, not provider limits."),
            ("Bad call UX is STT mismatch, not Cartesia TTS",
             "Calls go through first-party Render service (`/api/v1/call/initiate-call` → `/call-response` → `/end-call`); browser streams the assistant reply to Cartesia separately. Visible `call-response` only receives already-transcribed user text — the STT capture layer is where calls broke."),
            ("Retention is data-backed account state",
             "`discountsData` stores BOTH `2xHEARTS`/600 hearts AND `2.5xHEARTS`/750 hearts as pending credits, not just modal copy. The escalating cancellation offer is structurally an entitlement waiting to process."),
            ("Account payload exposes live model & feature state",
             "`/api/user` ships `llm_model: \"anthropic/claude-opus-4.6\"`, `image_engine: \"vermeer\"`, `video_engine: \"Inferno\"`, `subscription_tier: \"Max\"`, `heart_balance: 156.81`. Lots of feature gating lives in one payload."),
        ],
    },
    {
        "id": "sweetdream",
        "name": "SweetDream",
        "color": "tab-sweetdream",
        "anchor": "deep-sweetdream",
        "insights": [
            ("LiveCam is pre-rendered clip orchestration with chat glue, NOT live video generation",
             "DOM preloads MP4 loops (`l1_idle_1.mp4`, `l5_idle3_1.mp4`, `l1_bounce_1.mp4`). `LIVE_CAM_ACTION` returns ready `videoUrl`. XP gates time-based progression; tokens unlock instant clips. Content production expensive; runtime cheap. Doesn't scale to user-created characters without a template clip-pack pipeline."),
            ("SSE is the app event bus, carrying multiple topics",
             "`https://api.sweetdream.ai/v1/chat/sse` carries both `CHAT` and `LIVE_CAM` events. WebRTC/WebSocket only used where voice/video require it. SSE for server-to-client is the right fit when the browser doesn't need full duplex."),
            ("Twilio for normal voice calls",
             "`eventgw.us1.twilio.com`, `publisher: \"twilio-js-sdk\"`, `sdk_version: \"2.14.0\"`, `wss://voice-js.roaming.twilio.com/signal`, `callsid: CA47b8942cd2e6304659cdc6bdce1f68dc`. Phone-filter EQ on call voice is intentional processing or codec behavior — calls and chat TTS use different delivery paths."),
            ("Video calls = HeyGen/LiveAvatar over LiveKit, per-character only",
             "Only Chloe has it. `api.liveavatar.com/v1/sessions/start` returns `livekit_url: wss://heygen-feapbkvq.livekit.cloud`, `ws_url: wss://webrtc-signaling.heygen.io/...`, `max_session_duration: 1200`. Each video-call character likely needs a configured avatar/session with the provider."),
            ("Chat-triggered images are first-class SSE messages",
             "User prompt → assistant text reply → `IMAGE` message with `status: \"PROCESSING\"` → same message id updated to `SUCCESS` with CDN URL. Final image stored under `character/{slug}/ug_{timestamp}.webp`."),
            ("Standalone image generation reveals provider abstraction with first-party CDN persistence",
             "Processing record: `provider: \"OH_XYZ\"`, `providerJobId`, intermediate `lgpt-characters.s3.amazonaws.com` URL. Final saved asset lands on first-party `aigf.sfo2.cdn.digitaloceanspaces.com/character/...`. They pull generation output into their own CDN namespace after completion."),
            ("Publicity is a first-party per-character server action",
             "`[\"marcia-franklin-30e9\",\"PRIVATE\"]` posted to character route changes listing state without changing slug or deleting media. Public/private/unlisted state without losing chat/media identity."),
            ("Stale-gallery risk is real",
             "Regenerating a character changes main photo (`mp_sfw_{timestamp}.png`) but old generated images stay under the same `characterId` and slug with older prompts. Owner editing of deep visuals is risky because media is anchored to the character record."),
            ("Character creation maps directly into a structured persona, not free prompt",
             "Create POST sends a normalized persona object (`age`, `hobbies`, `specialFeatures`, `style`, `eyeColor`, `ethnicity`, `bodyType`, `personality`, `voice`, `occupation`, `relationship`, `clothing`). This drives chat identity, avatar prompt construction, and media generation downstream."),
        ],
    },
]


# ---------- Cross-cutting insights (synthesized from Steve's docs) ----------

CROSS_CUTTING = [
    {
        "title": "Character storage in WordPress is the #1 structural debt — fix before social/marketplace work",
        "body": "DRT still creates/updates/duplicates characters through WordPress. Mongo already has chats, messages, personas, memories, users, gallery — but characters are external. Moving characters into Mongo is a large refactor, but Steve strongly recommends doing it BEFORE serious public characters, creator economy, reviews, social feed, rankings, or character marketplace work. The more we build on top of WordPress character storage, the more painful the migration becomes later.",
        "tag": "Structural warning",
        "color": "warn",
    },
    {
        "title": "Image/video generation fragmentation will compound — unify before adding Canvas",
        "body": "DRT currently has 3 separate generation systems with non-matching schemas: in-chat generation (WordPress character fields: age, body, prompt tags, Imari-tested fixed actions); standalone gallery (separate schema: gender, model, style, face, age, ethnicity, hair, body, clothing, SFW/NSFW action); RunPod/spoke advanced (third system). Adding a GirlfriendGPT-style Canvas without unifying fields = 4 separate generation surfaces. Users will reasonably ask: why can't gallery images become characters? Why can't character images be edited in gallery? Why do chat images behave differently? Treat Canvas as a generation-architecture decision, not a page.",
        "tag": "Structural warning",
        "color": "warn",
    },
    {
        "title": "'Recent chats per character' is structural, not a UI tab",
        "body": "DRT's code uses one chat per user per character — `getChatByCharacterAndUser()` and `getOrCreateChat()` reuse the same chat. Multiple threads per character requires changing the chat model, reset behavior, chat lists, message loading, and possibly memory scoping. Kindroid is closer to DRT here (one relationship/chat). GirlfriendGPT is structurally different.",
        "tag": "Structural warning",
        "color": "warn",
    },
    {
        "title": "Public character usage is a binary product-direction choice that drives downstream architecture",
        "body": "Three patterns observed: (1) GirlfriendGPT — users chat with the original public character, creators matter as profiles, reviews live on the character. (2) Kindroid — messaging another's character duplicates/remixes it into your space, social profiles for characters, feed-based discovery. (3) SecretDesires / DRT — explicit `/api/character/privatize/{id}` clones before use, user can deeply edit private copy. Scoring rules (likes/comments/usage) depend on which you pick — child copy vs rolled up to parent vs the public character.",
        "tag": "Product decision",
        "color": "decide",
    },
    {
        "title": "Talking-head should wrap the existing chat brain, not replace it",
        "body": "User speaks → STT → existing DRT LLM/chat (memory, personas, history intact) → response goes to voice/video instead of UI → loop. Alexis already works this way conceptually, even though her 3D implementation is much more complex. The scalable talking-head layer should follow the same pattern — making it the unified layer for ALL characters, while Alexis/3D stays as the premium flagship. Don't make regular characters and Alexis separate product worlds.",
        "tag": "Architecture",
        "color": "arch",
    },
    {
        "title": "Memory delta to Nomi is the SECOND-ORDER index, not summaries",
        "body": "DRT already has semantic memory rows (`semantic_memories` with summary, chatId, personaId, characterSlug, source). Missing layer: `memory_terms` table with title/category (Entity/Keyword/Goal)/dossier/priority/state/selected/candidate/locked/userEditedAt/aiEditedAt/memoryIds/memoryCount/importanceScore + `memory_term_edges` graph + background term extraction triggered after `createSemanticMemory` + retrieval change in chat (select high-priority + relevant terms, then pull underlying memory summaries behind them) + UI for table view and graph view. Nomi makes 'infinite memory' practical by storing unbounded long-term memory but maintaining a bounded ranked concept map that chooses what to retrieve.",
        "tag": "Architecture",
        "color": "arch",
    },
    {
        "title": "Async generation with first-party CDN persistence is the universal pattern",
        "body": "Every competitor implements it the same way: POST creates placeholder/status:PROCESSING + run_id → progress events via SSE/Socket.IO/polling → status:SUCCESS with final media URL stored in OWN object storage. Examples: SweetDream (intermediate `lgpt-characters.s3.amazonaws.com` → final `aigf.sfo2.cdn.digitaloceanspaces.com`), SecretDesires (Comfy → Azure blob), OurDream (`triggerRunId` placeholder → notification). The UI never blocks the user — they can keep navigating/chatting while jobs finish.",
        "tag": "Standard pattern",
        "color": "pattern",
    },
    {
        "title": "Realtime transport mapping is consistent across the category",
        "body": "LiveKit for video calls and high-quality voice (Kindroid, OurDream, SweetDream-video via HeyGen). Twilio for normal phone-style voice calls (SweetDream). Cartesia Sonic-2 for streaming TTS with voice embeddings (SecretDesires). ElevenLabs Conversational AI for fully outsourced realtime agent calls (Candy). SSE/Socket.IO for app event bus (SweetDream SSE, Nomi Socket.IO, SecretDesires Socket.IO). WebRTC binary streams hide the actual call media. Pick the right primitive for the latency/duplex requirement — don't over-engineer.",
        "tag": "Standard pattern",
        "color": "pattern",
    },
    {
        "title": "Pre-rendered video loops = cheap 'presence' (production-cost, not runtime-cost)",
        "body": "Candy Romance Mode loads multiple `companion-scene-{uuid}-av1.mp4` videos per location/outfit combo and swaps via opacity. SweetDream LiveCam preloads `l1_idle_1.mp4`, `l5_idle3_1.mp4`, `l1_bounce_1.mp4` and orchestrates state. LoveScape ambient panel loops. The 'live' feeling comes from short loop transitions + chat copy + visual states + action unlocks, NOT from generating new video every turn. Cost concentrates in asset production + storage, not inference. Hard to scale to user-created characters without a clip-pack template pipeline.",
        "tag": "Standard pattern",
        "color": "pattern",
    },
    {
        "title": "Character creation = persisted DRAFT entity, then finalize",
        "body": "Candy: `/characters_v2/{uuid}/edit_attribute` step-by-step + `/regenerate_face` is cheap (attributes already on draft) + `/bring_my_ai_to_life` finalizes (creation fee + commitment point). SecretDesires: `/api/character/partial` returns character_id + image run_id, then `/api/chat/generate_about_me`, then PATCH finalizes. Nomi: POST returns `status: \"Creating\"`, Socket.IO bootstraps (status → Default, generates Shared Notes/appearances, inserts starter message). Pattern: draft entity → background generation jobs → final activation step.",
        "tag": "Standard pattern",
        "color": "pattern",
    },
    {
        "title": "Per-user vs per-character settings split causes silent 'feature broken' UX",
        "body": "SecretDesires example: account globally has `isImage/isVoice/isCall: true` while a new character has all three `false`. Feature feels broken until you find the buried switch. Feature availability is really `subscription + global defaults + per-character override`, and UI usually only surfaces one layer. Same risk applies to BYOK, voice selection, image/video engine pickers, time-awareness, etc.",
        "tag": "UX trap",
        "color": "trap",
    },
    {
        "title": "BYOK gotcha: DRT's ElevenLabs client is a module-level singleton — unsafe for multi-user keys",
        "body": "Nomi has ElevenLabs BYOK via `voiceSource` + `customVoiceId` + `elevenLabsVoiceId` fields. DRT-specific warning from Steve: `elevenlabs-api-service.ts` has a module-level `let elevenlabs: ElevenLabsClient` cache. Fine for one global key, UNSAFE for BYOK — the first user's key could stick as the singleton client. A BYOK implementation should either create a client per request/key or cache by a secure key fingerprint / user id, never as one global client. Plus needs: encrypted per-user integration credentials table, per-character voice-source metadata, voice library UI backed by the user's provider account, clear cost ownership rules.",
        "tag": "Code-level warning",
        "color": "warn",
    },
    {
        "title": "Provider routing by content category is now standard",
        "body": "Candy: SFW video = Kling (5s), NSFW video = Pika (5/10s) with `excluded_for_model_types: [\"big_love\"]` per category. OurDream: video metadata exposes `wavespeed` with `wan-2.7-spicy`, plus `svi`, `performanceMode`. Abstract over providers behind your own job system. The UI sells named tiers; the backend picks the right model per content type and capability.",
        "tag": "Standard pattern",
        "color": "pattern",
    },
    {
        "title": "Suggested replies, user personas, daily rewards already exist in DRT — they may just be buried",
        "body": "Suggested replies are part of DRT's LLM JSON contract and render in chat. User personas exist scoped per chat/default. Daily rewards exist through the earn/streak system. GirlfriendGPT's 'Chat Profiles' and Kindroid's daily rewards aren't missing — they're under-surfaced. Surfacing is a UI/UX exercise, not a backend feature build.",
        "tag": "Already exists",
        "color": "exists",
    },
    {
        "title": "Public-character moderation becomes mandatory at scale",
        "body": "Report modal taxonomy (underage, real person, ads/spam, copyright, other), review workflows, NSFW scoring on generated media (Nomi returns `nsfwScore: 0.07...` on every image edit completion). These aren't optional features — they're prerequisites for opening up public character creation and usage. If DRT goes the GirlfriendGPT route, this gates the whole public-character launch.",
        "tag": "Prerequisite",
        "color": "decide",
    },
    {
        "title": "Camera vision is doable cheaply on top of any LLM",
        "body": "Pattern: periodic frame capture → independent vision model/service → short visual description → inject into LLM context. Smarter: only fire extra vision calls when the user says 'look at this' or 'what is this?' Don't need natively multimodal LLMs for this. Cost rises with frame frequency; balance UX against per-frame inference cost.",
        "tag": "Cheap win",
        "color": "win",
    },
    {
        "title": "Reset chat needs a second mode in DRT",
        "body": "Current `reset chat` only deletes messages; semantic memories survive. Kindroid-equivalent behavior: 'Reset chat/messages only' (current) AND 'Reset chat + memories' (new destructive opt-in toggle). Cascaded delete is a small UI add but a structural choice about what 'reset' means.",
        "tag": "Cheap win",
        "color": "win",
    },
    {
        "title": "Suggested chips and prompt enhancers are usually client-side or cheap",
        "body": "SweetDream suggestion chips just append text fragments to the prompt box — no server filter. Candy `/gen_ai_suggestions/prompts` exposes the actual prompts; the client sends `gen_ai_prompt_id` not free text. SweetDream prompt enhancer is a separate endpoint from generation. Polished media UIs are often structured prompt selection under the hood — not magic, just curated.",
        "tag": "Standard pattern",
        "color": "pattern",
    },
]


GLOBAL_NOTES_HTML = """
<p>Steve's exact ask for how the AI should frame findings on the remaining 9 competitor checks (from his Kindroid + GirlfriendGPT writeup, addressed to Dainis):</p>

<p><strong>For large features, ask the AI to compare the competitor feature against what already exists in DRT.FM before turning it into a build request.</strong> Many of these features are not simply "add a page" or "add a button." Some are small UI additions, some already exist but are hidden, some conflict with how DRT.FM is currently structured.</p>

<p>Example: <em>"Recent Chats per character"</em> sounds like a UI tab, but DRT currently has one chat per user per character. The code reuses the same chat instead of creating multiple threads. So that feature is structural, not small. Same with social/community characters: DRT can duplicate public characters into a user's private space, closer to Kindroid, while GirlfriendGPT lets users chat with public originals. Those are different product architectures.</p>

<p><strong>For the next competitor checks, the most useful output is less "how did they call the API?" and more these 8 questions:</strong></p>

<ol class="framework-list">
  <li>Does DRT already have this feature?</li>
  <li>If yes, is it visible enough, polished enough, or buried?</li>
  <li>If no, is it a small UI feature, a medium feature, or a structural feature?</li>
  <li>Does it require a new data model?</li>
  <li>Does it touch character ownership, public/private character access, chats, memory, image generation, billing, or moderation?</li>
  <li>Does it require Imari's prompt engineering work, not just code?</li>
  <li>Does it add another generation surface, social surface, or content moderation surface?</li>
  <li>Is this a matter of taste/product direction, or a clear competitor-standard feature?</li>
</ol>

<p>The API/network tab is still worth checking — but mostly for leaks or product clues. Seeing SSE vs WebSocket vs polling usually doesn't matter much by itself. If we want latency we already know WebSockets/WebRTC are better in certain cases. If we want background jobs, polling/SSE can both work. Every company may implement the same product idea differently, and we are only seeing the black-box client side unless something meaningful leaks.</p>

<p><strong>So for the remaining sites, I'd ask the AI to separate findings into:</strong></p>

<ul class="framework-list">
  <li><strong>Product pattern:</strong> what the user sees and why it matters.</li>
  <li><strong>Structure pattern:</strong> how the feature fits into characters/chats/memory/media/social.</li>
  <li><strong>DRT comparison:</strong> exists, hidden, missing, or structurally different.</li>
  <li><strong>Build size:</strong> small UI, medium feature, large refactor, or product-direction decision.</li>
  <li><strong>Prompt/content dependency:</strong> whether Imari needs to design prompts, presets, character fields, or model behavior.</li>
</ul>
"""


# ---------- HTML scaffolding ----------

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:72px}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0d0d12;color:#e0e0e8;line-height:1.65;padding-top:56px}

/* NAV */
nav.top{position:fixed;top:0;left:0;right:0;z-index:100;background:#0a0a10;border-bottom:1px solid #1e1e2e;display:flex;align-items:center;gap:4px;padding:0 16px;height:56px;overflow-x:auto}
nav.top::-webkit-scrollbar{height:3px}nav.top::-webkit-scrollbar-thumb{background:#2a2a3e}
.nav-label{font-size:11px;font-weight:700;color:#3a3a5a;text-transform:uppercase;letter-spacing:1px;white-space:nowrap;margin-right:8px;padding-right:12px;border-right:1px solid #1e1e2e}
.nav-link{flex-shrink:0;padding:6px 14px;border-radius:6px;border:none;cursor:pointer;font-size:13px;font-weight:600;background:transparent;transition:all .15s;white-space:nowrap;text-decoration:none;color:#9090b8}
.nav-link:hover{background:#1e1e2e;color:#fff}
.nav-link.home{color:#34d399}
.nav-link.active-section{color:#fff;background:#1e1e2e}
.private-badge{margin-left:auto;flex-shrink:0;background:#3a1020;border:1px solid #6a2040;color:#ff8aaa;font-size:10px;font-weight:700;padding:3px 10px;border-radius:20px}

/* LAYOUT */
.section{max-width:1180px;margin:0 auto;padding:32px 32px 80px}

/* HERO */
.hero{background:linear-gradient(135deg,#0a0a1a 0%,#1a0820 100%);border:1px solid #3a1a4a;border-radius:14px;padding:30px 36px;margin-bottom:32px}
.hero .author-tag{display:inline-block;font-size:11px;font-weight:700;background:#2a0a3a;color:#d0a0ff;padding:4px 10px;border-radius:6px;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}
.hero h1{font-size:26px;font-weight:800;color:#fff;margin-bottom:12px;line-height:1.3}
.hero h1 span.accent{color:#d0a0ff}
.hero p.lede{font-size:15px;color:#b8b8d8;max-width:920px;line-height:1.7;margin-bottom:18px}
.hero p.lede code{background:#1a0a2a;color:#d0a0ff;padding:1px 6px;border-radius:4px;font-family:'SF Mono',monospace;font-size:13px}
.hero .meta{margin-top:14px;font-size:12px;color:#6a6a8a;display:flex;flex-wrap:wrap;gap:14px}
.hero .meta span{display:inline-flex;align-items:center;gap:6px}
.hero .meta b{color:#9090b8;font-weight:600}

/* ZONE HEADER */
h2.zone{font-size:13px;font-weight:700;color:#d0a0ff;text-transform:uppercase;letter-spacing:1.5px;margin:48px 0 14px;padding-bottom:8px;border-bottom:2px solid #1e1e2e;display:flex;align-items:center;gap:10px}
h2.zone .zone-badge{font-size:10px;background:#2a0a3a;color:#d0a0ff;padding:2px 8px;border-radius:4px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px}
h2.zone:first-of-type{margin-top:8px}
p.zone-desc{font-size:14px;color:#8090a8;margin-bottom:18px;max-width:880px}

/* CROSS-CUTTING CARDS */
.cross-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:14px}
.cross-card{background:#0e0e16;border:1px solid #2a2a3e;border-radius:10px;padding:18px 22px;transition:border-color .15s}
.cross-card:hover{border-color:#3a3a5e}
.cross-card .tag{display:inline-block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:0.5px;padding:3px 8px;border-radius:4px;margin-bottom:10px}
.cross-card .tag.warn{background:#3a1020;color:#ff8aaa;border:1px solid #6a2040}
.cross-card .tag.arch{background:#1a2a3a;color:#7ed4ff;border:1px solid #2a4a6a}
.cross-card .tag.pattern{background:#0a2820;color:#5eead4;border:1px solid #1a4a3a}
.cross-card .tag.decide{background:#2a1a3a;color:#d0a0ff;border:1px solid #4a2a5a}
.cross-card .tag.trap{background:#3a2a10;color:#ffc78a;border:1px solid #6a4a20}
.cross-card .tag.win{background:#1a2a1a;color:#9ee080;border:1px solid #2a4a2a}
.cross-card .tag.exists{background:#1a1a2a;color:#9090d8;border:1px solid #2a2a4a}
.cross-card h3{font-size:15px;font-weight:700;color:#fff;margin-bottom:8px;line-height:1.4}
.cross-card p{font-size:13px;color:#b8b8d0;line-height:1.65}
.cross-card p code{background:#0a1a28;color:#7ed4ff;padding:1px 5px;border-radius:3px;font-family:'SF Mono',monospace;font-size:12px}

/* FRAMEWORK SECTION */
.framework-card{background:linear-gradient(135deg,#0a1a14,#0e2820);border:1px solid #1a4a3a;border-radius:12px;padding:24px 28px}
.framework-card p{font-size:14px;color:#c0d8c8;margin-bottom:14px;line-height:1.7}
.framework-card p strong{color:#5eead4}
.framework-card p em{color:#9ee0c8;font-style:italic}
.framework-card ol.framework-list,.framework-card ul.framework-list{padding-left:24px;margin:10px 0 16px;color:#b8d8c8;font-size:14px;line-height:1.8}
.framework-card ol.framework-list li,.framework-card ul.framework-list li{margin-bottom:5px}
.framework-card ul.framework-list li strong,.framework-card ol.framework-list li strong{color:#5eead4}

/* PER-COMPETITOR CARDS */
.comp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:18px}
.comp-card{background:#0e0e16;border:1px solid #2a2a3e;border-radius:12px;padding:22px 26px}
.comp-card .comp-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid #1e1e2e}
.comp-card .comp-name{font-size:15px;font-weight:800;text-transform:uppercase;letter-spacing:0.5px}
.comp-card .comp-name.tab-kindroid{color:#5eead4}
.comp-card .comp-name.tab-ggpt{color:#ff6b9d}
.comp-card .comp-name.tab-candy{color:#ff4da6}
.comp-card .comp-name.tab-nomi{color:#22d3ee}
.comp-card .comp-name.tab-od{color:#4da6ff}
.comp-card .comp-name.tab-sd{color:#9b4dca}
.comp-card .comp-name.tab-sweetdream{color:#a78bfa}
.comp-card .comp-link{font-size:11px;font-weight:600;color:#7070a0;text-decoration:none;padding:4px 10px;border:1px solid #2a2a3e;border-radius:5px;transition:all .15s}
.comp-card .comp-link:hover{color:#fff;border-color:#3a3a5e;background:#1a1a2a}
.comp-card .insight{margin-bottom:14px;padding-bottom:14px;border-bottom:1px dashed #1e1e2e}
.comp-card .insight:last-child{margin-bottom:0;padding-bottom:0;border-bottom:none}
.comp-card .insight-title{font-size:13px;font-weight:700;color:#fff;margin-bottom:6px;line-height:1.5}
.comp-card .insight-body{font-size:12.5px;color:#9090b8;line-height:1.65}
.comp-card .insight-body code{background:#0a1a28;color:#7ed4ff;padding:1px 5px;border-radius:3px;font-family:'SF Mono',monospace;font-size:11.5px}

/* TABS */
.tabs-bar{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:20px;padding:6px;background:#0a0a14;border:1px solid #1e1e2e;border-radius:10px;position:sticky;top:60px;z-index:50;backdrop-filter:blur(6px)}
.tab-btn{flex:1;min-width:140px;padding:10px 16px;border-radius:6px;border:none;cursor:pointer;font-size:13px;font-weight:600;background:transparent;transition:all .15s;white-space:nowrap;color:#7070a0;font-family:inherit}
.tab-btn:hover{background:#1e1e2e;color:#e0e0e8}
.tab-btn.active{background:#1e1e2e;color:#fff}
.tab-btn.active.tab-kindroid{color:#5eead4;background:#0a2820}
.tab-btn.active.tab-candy{color:#ff4da6;background:#2a0a1a}
.tab-btn.active.tab-nomi{color:#22d3ee;background:#0a1a2a}
.tab-btn.active.tab-od{color:#4da6ff;background:#0a1a2a}
.tab-btn.active.tab-sd{color:#9b4dca;background:#1a0a28}
.tab-btn.active.tab-sweetdream{color:#a78bfa;background:#1a0a28}
.tab-panel{display:none}
.tab-panel.active{display:block}

/* DEEP NOTES (markdown body) */
.deep-notes{background:#0e0e16;border:1px solid #2a2a3e;border-radius:12px;padding:32px 38px}
.deep-notes .md-h3{font-size:18px;font-weight:800;color:#fff;margin-top:32px;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid #2a2a3e}
.deep-notes .md-h3:first-child{margin-top:0}
.deep-notes .md-h3-major{font-size:22px;color:#d0a0ff;border-bottom-color:#3a1a4a;padding-bottom:12px;margin-top:48px}
.deep-notes .md-h4{font-size:15px;font-weight:700;color:#5eead4;margin-top:24px;margin-bottom:10px;text-transform:uppercase;letter-spacing:0.5px}
.deep-notes p{font-size:14.5px;color:#c0c0d8;line-height:1.75;margin-bottom:14px}
.deep-notes p code{background:#0a1a28;color:#7ed4ff;padding:2px 6px;border-radius:4px;font-family:'SF Mono',Menlo,Monaco,monospace;font-size:13px;border:1px solid #1a2a3a}
.deep-notes ul,.deep-notes ol{padding-left:26px;margin-bottom:16px;color:#c0c0d8}
.deep-notes ul li,.deep-notes ol li{font-size:14.5px;line-height:1.75;margin-bottom:8px}
.deep-notes ul li code,.deep-notes ol li code{background:#0a1a28;color:#7ed4ff;padding:1px 5px;border-radius:3px;font-family:'SF Mono',monospace;font-size:12.5px}
.deep-notes strong{color:#fff;font-weight:700}
.deep-notes em{color:#d0a0ff;font-style:italic}

/* DAINIS QUOTE INLINE */
.deep-notes .dainis-quote{background:#1a0a2a;border-left:3px solid #d0a0ff;border-radius:6px;padding:14px 18px;margin:18px 0}
.deep-notes .dainis-quote .quote-label{display:inline-block;font-size:10px;font-weight:700;color:#d0a0ff;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}
.deep-notes .dainis-quote .quote-body{font-size:14px;color:#e8d8ff;line-height:1.7;font-style:italic}
.deep-notes .dainis-quote .quote-body code{background:#2a1a3a;color:#f0d8ff;font-style:normal}

/* TABLE OF CONTENTS (cross-cutting section anchor list) */
.anchors{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 22px}
.anchors a{font-size:12px;color:#7070a0;text-decoration:none;padding:5px 11px;border:1px solid #2a2a3e;border-radius:5px;transition:all .15s}
.anchors a:hover{color:#fff;background:#1e1e2e;border-color:#3a3a5e}

@media (max-width:760px){
  .section{padding:24px 16px 60px}
  .hero{padding:22px 20px}
  .hero h1{font-size:20px}
  .cross-grid,.comp-grid{grid-template-columns:1fr}
  .tabs-bar{flex-direction:column;position:static}
  .tab-btn{width:100%}
}
"""


JS = r"""
(function(){
  const buttons = document.querySelectorAll('.tab-btn[data-tab]');
  const panels = document.querySelectorAll('.tab-panel');
  function activate(id){
    buttons.forEach(b => b.classList.toggle('active', b.dataset.tab === id));
    panels.forEach(p => p.classList.toggle('active', p.id === 'panel-' + id));
    history.replaceState(null, '', '#tab-' + id);
  }
  buttons.forEach(b => b.addEventListener('click', () => activate(b.dataset.tab)));

  // initial: hash or first
  const hash = location.hash;
  if (hash.startsWith('#tab-')) {
    activate(hash.slice(5));
  } else if (hash.startsWith('#deep-')) {
    activate(hash.slice(6));
    // scroll to tabs section
    document.getElementById('deep-notes-section').scrollIntoView();
  } else if (buttons.length) {
    activate(buttons[0].dataset.tab);
  }

  // jump-to-tab links from per-competitor cards
  document.querySelectorAll('a.jump-to-tab').forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      const id = a.dataset.target;
      activate(id);
      document.getElementById('deep-notes-section').scrollIntoView({behavior:'smooth'});
    });
  });
})();
"""


# ---------- Build it ----------

def build_cross_cutting_html() -> str:
    parts = ['<div class="cross-grid">']
    for c in CROSS_CUTTING:
        parts.append(
            f'<div class="cross-card">'
            f'<span class="tag {c["color"]}">{c["tag"]}</span>'
            f'<h3>{c["title"]}</h3>'
            f'<p>{inline_md_keep_html(c["body"])}</p>'
            f'</div>'
        )
    parts.append("</div>")
    return "\n".join(parts)


def inline_md_keep_html(text: str) -> str:
    """Like inline_md, but the input is already trusted HTML-safe English text.
    We only need to translate backticks and bold/em, NOT escape angle brackets,
    because hand-authored cross-cutting content uses HTML-safe wording."""
    # Inline code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def build_per_competitor_html() -> str:
    parts = ['<div class="comp-grid">']
    for comp in PER_COMP_CARDS:
        insights_html = "\n".join(
            f'<div class="insight">'
            f'<div class="insight-title">{inline_md_keep_html(title)}</div>'
            f'<div class="insight-body">{inline_md_keep_html(body)}</div>'
            f'</div>'
            for title, body in comp["insights"]
        )
        parts.append(
            f'<div class="comp-card">'
            f'<div class="comp-header">'
            f'<span class="comp-name {comp["color"]}">{comp["name"]}</span>'
            f'<a class="comp-link jump-to-tab" data-target="{comp["id"]}" href="#tab-{comp["id"]}">Full notes →</a>'
            f'</div>'
            f'{insights_html}'
            f'</div>'
        )
    parts.append("</div>")
    return "\n".join(parts)


def build_tabs_bar_html() -> str:
    buttons = []
    for tab_id, _, name, color_cls in FILES:
        buttons.append(
            f'<button class="tab-btn {color_cls}" data-tab="{tab_id}">{name}</button>'
        )
    return f'<div class="tabs-bar">{"".join(buttons)}</div>'


def build_tab_panels_html() -> str:
    panels = []
    for tab_id, fname, name, _ in FILES:
        src = SRC_DIR / fname
        md = src.read_text()
        html_body = md_to_html(md)
        panels.append(
            f'<div class="tab-panel" id="panel-{tab_id}">'
            f'<div class="deep-notes" id="deep-{tab_id}">{html_body}</div>'
            f'</div>'
        )
    return "\n".join(panels)


def build_page() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Steve's Technical Insights · DRT.FM Competitor Reviews</title>
<style>{CSS}</style>
</head>
<body>

<nav class="top">
  <span class="nav-label">Steve's Technical Insights</span>
  <a class="nav-link home" href="index.html">← Index</a>
  <a class="nav-link" href="#cross-cutting">Cross-Cutting</a>
  <a class="nav-link" href="#framework">Framework</a>
  <a class="nav-link" href="#per-competitor">Per-Competitor</a>
  <a class="nav-link" href="#deep-notes-section">Deep Notes</a>
  <span class="private-badge">DRT.FM · Private</span>
</nav>

<div class="section">

  <div class="hero">
    <span class="author-tag">Written by Steve · DRT's developer</span>
    <h1>What would actually <span class="accent">break or accelerate DRT.FM</span> if we shipped these competitor features?</h1>
    <p class="lede">
      Steve's hands-on technical review of 7 competitors (Kindroid, GirlfriendGPT, Candy.AI, Nomi, OurDream, SecretDesires, SweetDream),
      written on top of Dainis's product research and the network captures. The focus is architecture &amp; build implications:
      what's <strong>already in our codebase</strong>, what's <strong>buried but exists</strong>, what's <strong>missing</strong>, and what would
      require a <strong>structural refactor</strong> — not a "add a page" build.
    </p>
    <p class="lede">
      Two structural warnings he keeps returning to: (1) <code>character storage still lives in WordPress</code> while everything else (chats,
      messages, personas, memories, gallery) is in Mongo — fix this <em>before</em> serious social/marketplace work; (2) image/video generation is
      currently fragmented across 3 systems with non-matching schemas — adding a "Canvas" without unifying makes it 4.
    </p>
    <div class="meta">
      <span><b>Source:</b> 6 markdown writeups from Steve</span>
      <span><b>Covers:</b> Kindroid · GirlfriendGPT · Candy.AI · Nomi · OurDream · SecretDesires · SweetDream</span>
      <span><b>Date:</b> 2026-05-23</span>
    </div>
  </div>

  <h2 class="zone" id="cross-cutting">Cross-Cutting Architecture Insights <span class="zone-badge">{len(CROSS_CUTTING)} themes</span></h2>
  <p class="zone-desc">Themes Steve flagged repeatedly across competitors. Address these <strong>before</strong> building competitor-style features — they're the architectural decisions that compound.</p>
  <div class="anchors">
    <a href="#cross-cutting">Architecture warnings</a>
    <a href="#framework">AI framework</a>
    <a href="#per-competitor">Per-competitor insights</a>
    <a href="#deep-notes-section">Full deep notes</a>
  </div>
  {build_cross_cutting_html()}

  <h2 class="zone" id="framework">Framework Steve Wants the AI to Use Going Forward <span class="zone-badge">From Kindroid + GGPT writeup</span></h2>
  <p class="zone-desc">Steve's exact ask for how the AI should frame findings on the remaining competitor checks — shift from "how did they call the API?" to product/structure/DRT-comparison/build-size/prompt-dependency.</p>
  <div class="framework-card">
    {GLOBAL_NOTES_HTML}
  </div>

  <h2 class="zone" id="per-competitor">Per-Competitor Key Insights <span class="zone-badge">{len(PER_COMP_CARDS)} competitors · click "Full notes" for deep-dive</span></h2>
  <p class="zone-desc">Steve's highest-leverage technical findings per competitor. Click <strong>Full notes →</strong> on any card to jump to the complete writeup (Executive Summary · Extracted Product Structure · Key Technical Findings · Quotes + Analysis).</p>
  {build_per_competitor_html()}

  <h2 class="zone" id="deep-notes-section">Deep Notes — Full Writeups <span class="zone-badge">Tab to switch competitor</span></h2>
  <p class="zone-desc">Steve's full markdown writeup per competitor, preserved verbatim. Pick a tab; the content scrolls within this section. Each writeup has 4 sections: Executive Summary · Extracted Product Structure · Key Technical Findings · Quotes + Analysis.</p>
  {build_tabs_bar_html()}
  {build_tab_panels_html()}

</div>

<script>{JS}</script>

</body>
</html>
"""


def main():
    html = build_page()
    OUT_PATH.write_text(html)
    print(f"Wrote {OUT_PATH} ({len(html):,} chars)")


if __name__ == "__main__":
    main()
