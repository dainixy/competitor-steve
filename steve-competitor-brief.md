# Competitor Analysis Brief — Steve

## The Big Picture

Right now we're roughly 25% of where our competitors are in terms of feature depth. The goal isn't to copy everything they have — it's to identify the features every serious AI girlfriend user expects a high-quality platform to have, ship those, and along the way understand where the market is heading so we're building toward the right future, not just yesterday's standard.

The competitive landscape has 11 players we need to understand deeply. Dainis has done detailed hands-on reviews of 2 (Kindroid and GirlfriendGPT) and is working through the remaining 9. But here's the key: **we both need to experience these products independently** — not just read a summary. Two perspectives, formed separately, then compared. That's how we get the full picture.

---

## What We're Building

**DRT.FM** — a generalist AI girlfriend platform. We're moving away from niche positioning to compete directly with Candy.AI, GirlfriendGPT, OurDream, and others at their level.

**Two things we're building, with different roles:**

**Talking head** — the scaleable experience. This is the video call layer that works for any character on the platform, including ones users create. It's designed to be played with, broken, duplicated. This is the core feature that closes the gap with Kindroid and others.

**Alexis** — our unique flagship creation. She's not scaleable right now, and that doesn't need to change. Alexis is built to be the best: deepest memory, most expressive, most polished. She's Dainis's area to own and refine. The 3D character is what no competitor has — and Alexis is how we demonstrate it at its peak.

The two aren't in conflict. Talking head is the platform feature users can explore freely. Alexis is the proof of what this product can be at its best.

---

## Your Role

You own DRT.FM. Imari handles content/prompts (RunPod, Payload pages).

**Month 1:** Dainis and Steve work closely together. That's the reality right now.

**The goal we're building toward:** Dainis focuses on marketing, Steve builds autonomously, Imari handles content. But that's not where we are yet — and Steve needs to understand the direction so everything we do now is pointed at it.

**The operating model we're aiming for:**
- You build and ship features autonomously
- Daily progress updates to Dainis
- You're clear on 80% of decisions, own the next 10% yourself, and check in only on genuine surprises
- Dainis jumps in when needed, otherwise focused on marketing

Competitor analysis is the foundation for getting there. The more you understand what we're building and why — the less you need to triple-check anything.

AI-assisted development means we can code, test, and ship to prod 10x–100x faster than before. That's the pace we need to operate at.

---

## The Process

1. **Dainis reviews first.** Deep hands-on review of each competitor — screenshots, notes, full experience. Done: Kindroid and GirlfriendGPT. Remaining 9 coming.

2. **Dainis shares.** You get access to his notes, [competitor-checks.html](https://dainixy.github.io/competitor-steve/competitor-checks.html), and [competitor-analysis-v2.html](https://dainixy.github.io/competitor-steve/competitor-analysis-v2.html).

3. **You do your own review.** Same paid account access. Don't just read Dainis's notes — go in yourself and form your own opinion. Especially your technical read.

4. **Both write summaries.** Dainis writes his high-level product read. You write yours. Independent perspectives.

5. **Alignment session.** Compare notes, agree on what to build first, prototype anything complex.

6. **You build.** Full autonomy. Agreed priorities, daily updates.

---

## What to Look For

### Layer 1: As a User (30–45 min per competitor)

Experience the product the way a real user would. Don't rush to the dev tools.

- Sign up and go through onboarding. How frictionless is it?
- Start a conversation. Does the character feel like a person?
- Find the NSFW toggle or unlock. How does it handle the transition?
- Try image generation. How fast? How consistent is the character's appearance?
- Try voice. How natural? Is there emotional range?
- Test memory. Does it remember what you said 10 minutes ago? Yesterday?
- Find the subscription/pricing page. How is it structured?
- Notice what frustrates you.
- Notice what surprises you positively.

**The question to answer:** What's the dominant feeling of using this product — and what creates it?

### Layer 2: As a Developer (dev tools open)

After you've formed your user opinion, open DevTools and inspect how it's built.

- **Network tab:** What API calls happen during chat? Endpoint patterns? Payload structure?
- **Image generation:** Triggered how? Separate API call or streaming? Which service?
- **Voice/audio:** Streaming or chunked? Which TTS provider? What's the latency?
- **Memory:** Anything in network calls that hints at how memory is stored or retrieved?
- **Video calls:** WebRTC? WebSockets? Third-party service?
- **Performance:** Time to first chat response. Time to first image. Perceived vs actual speed.
- **Tech stack clues:** Frameworks, CDNs, or services visible in requests or source.

**The question to answer:** How hard would this be to build — and what's the fastest path to something equivalent?

---

## The 11 Competitors

| # | Competitor | Status | What to Know |
|---|-----------|--------|--------------|
| 1 | Kindroid | Dainis reviewed | Most technically capable competitor. 5-person team shipping fast. Camera vision during calls, 5-layer memory system. |
| 2 | GirlfriendGPT | Dainis reviewed | High visual polish, creator economy (359 characters), strong re-engagement notifications. |
| 3 | Candy.AI | Pending | Community characters, Romance Mode in testing, biggest mainstream name. |
| 4 | OurDream.AI | Pending | 10K+ voices, autonomous story mode, $5K character contests. |
| 5 | SecretDesires.AI | Pending | "YouTube of AI companions" vision, scene-matched video mid-conversation. |
| 6 | Promptchan | Pending | Image-first approach, "Create Image from Scene" feature. |
| 7 | Joi.AI | Pending | Voice-only focus, launched May 2026. |
| 8 | Nomi | Pending | — |
| 9 | LoveScape | Pending | — |
| 10 | Swipey | Pending | — |
| 11 | SweetDream | Pending | — |

---

## Account Access

All premium accounts use: **boss@thehumblehackers.com**

- Kindroid: active
- GirlfriendGPT: active
- Remaining 9: Dainis will set up and share credentials as he completes each review

**Don't pay for anything yourself.** Hit a paywall → flag it.

---

## Why Your Technical Background Matters

Dainis can navigate these products and spot what's working — he's technical enough to do the checks. But he's not a coder. He uses Claude Code now, but he doesn't have years of hands-on development experience like you do.

A concrete example: Dainis initially proposed doing competitor research with AI. You explained from experience why that approach wouldn't work and suggested a better path. That saved significant time. That kind of practical judgment is exactly what you bring that Dainis can't replicate.

Your lens is different. You can see the seams. You can tell when image generation is slow because it's not streaming, or when voice is laggy because there's no pre-buffering. You can spot when "memory" is just prompt injection versus a real retrieval system. You can look at a network tab and estimate how hard something is to replicate.

When you both review the same product independently — Dainis sees the product experience, you see the technical implementation and feasibility. Together that's the full picture.

No prescribed format for your notes. Record and share findings in whatever way works for you.

---

## After the Analysis

1. **Alignment session** — review both sets of notes, agree on top features, factor in your current connectivity and setup constraints.
2. **Prototyping** — quick prototypes for anything complex to de-risk before full build.
3. **Priority list** — ranked, agreed together.
4. **Full autonomy** — you build. Daily updates are enough. Dainis trusts your implementation judgment.

The goal isn't perfect analysis. It's **shared understanding** — enough that you and Dainis are seeing the same product and the same gaps, and you can ship without constant back-and-forth.
