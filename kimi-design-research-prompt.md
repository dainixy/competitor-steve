# Deep Research: How real designers make Claude Code produce professional UI/UX

## Mission

I use Claude Code to build web products. Out of the box, Claude's design output is generic "AI slop" — bootstrap-looking pages, purple gradients, rounded cards everywhere, no typographic hierarchy, bloated markup. I want to install a permanent "design taste" upgrade into Claude Code so it reliably produces clean, professional, FAST-loading web UI.

Your job: find what real, credible UI/UX designers and design engineers ACTUALLY do to get great design out of Claude — their exact setups, prompts, files, and workflows. Social media is your primary source: X/Twitter, Reddit, YouTube, Bluesky/Threads, Hacker News, designer newsletters and blogs. I explicitly do NOT want a list of official Anthropic skills or Anthropic marketing posts — I want field-tested practice from working designers with receipts.

## What "great design" means here (hard filter — read carefully)

- **Practical, foundation-driven design:** visual hierarchy, typography systems, spacing scales, color discipline, accessible contrast, real content design. Usable and functional first.
- **FAST:** lightweight pages, minimal JavaScript, fast load times (Core Web Vitals matter — this site must rank on Google). Speed is a hard requirement, not a nice-to-have.
- **NOT flashy:** no WebGL hero scenes, no scroll-jacking, no heavy animation showcases, no awwwards-bait, no "flying horses." Ignore that entire scene. If a workflow's main output is flashy motion design, skip it.
- Websites that convert and rank, not art projects.

## Who counts as a credible source

1. Working designers / design engineers with receipts: shipped products, portfolios, before/after screenshots, real client or product work.
2. People who share the actual artifact: their CLAUDE.md design rules, prompt text, skill/agent file, repo, or component setup — not just "Claude is amazing" hype.
3. Recency: mid-2025 through July 2026 (the Claude Code era). Older LLM-design advice only if it's clearly still in use.

Disqualify: engagement-bait threads with no artifacts, AI-news channels that don't themselves design, course sellers whose only shipped work is the course, official vendor announcements repackaged as tips.

## Questions to answer

1. **Recurring methods.** What setups keep appearing across INDEPENDENT practitioners? Investigate at least these candidates, plus whatever else you find:
   - Writing a design-system / style-guide file FIRST (tokens: type scale, spacing scale, palette, radii), then making Claude build only within it
   - Distilling design-book rules (e.g. Refactoring UI-style heuristics) into CLAUDE.md instructions
   - Feeding Claude reference screenshots of well-designed sites to imitate
   - Screenshot-feedback loops: Claude renders its page, looks at a screenshot of it (Playwright/browser tools), critiques, iterates
   - Component libraries (shadcn/ui and friends) + registry/MCP servers so Claude assembles proven components instead of inventing CSS
   - A separate "design review" pass or subagent that grades output against a checklist
   - Theme/token generators (e.g. tweakcn) to escape default-shadcn look
   For each: how it works in plain terms, who uses it, evidence it improves output.
2. **Tools with real adoption.** Which community tools, skills, agents, or MCP servers do practitioners actually USE (not just star)? Evidence = shown results, active discussions, repeated independent recommendations.
3. **Encoding a design language.** How do people teach Claude a specific visual identity so every page stays on-system across sessions — and how do they extract quality principles from sites they admire WITHOUT cloning them?
4. **Speed discipline.** How do practitioners keep Claude's output lightweight and fast — rules against dependency bloat and heavy JS, performance budgets in prompts, checking Lighthouse/Core Web Vitals in the loop? Any shared prompt/rule text specifically for performance?
5. **People to follow.** 10–20 credible designers/design engineers publicly working with Claude Code on UI, each with a link and a one-line receipt (what they shipped/shared).
6. **Top 5 complete workflows** worth replicating end-to-end (define look → build → review loop), ranked. For each: source links, exact steps, the artifacts involved, and why you rank it there.

## Where to dig (cover all of these)

- **X/Twitter:** threads on "Claude Code" + design / UI / CLAUDE.md / design system / frontend; the design-engineer scene (people around the shadcn ecosystem, Vercel designers, tweakcn, superdesign, 21st.dev — verify these leads and expand beyond them); viral before/after posts and what their authors say they did.
- **Reddit:** r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/webdev, r/web_design, r/UXDesign — mine the COMMENTS of top threads from the past year; that's where real setups get described.
- **YouTube:** end-to-end workflow demos; only count creators whose shown output is genuinely good.
- **Hacker News:** threads on LLMs and design taste, "AI slop" design discussions, Show HNs of design tools for coding agents.
- **Newsletters/blogs** by working designers (design-engineering newsletters, personal blogs with walkthroughs).
- **GitHub:** shared CLAUDE.md files, design-focused skills/agent definitions, MCP servers — with adoption signals.

## Output format

1. **Executive summary:** the 5–7 things that actually work, one plain-language paragraph each.
2. **Method table:** method → who uses it → evidence links → setup effort → expected impact on output quality.
3. **The artifacts (most valuable section):** paste the actual prompt texts, CLAUDE.md/file contents, and repo links you find. Full text, not paraphrase, when the source shows it.
4. **People list** with links and receipts.
5. **Top 5 workflows** ranked, with steps.
6. Mark every claim: **[VERIFIED]** = you saw the artifact and its results; **[CLAIMED]** = described but not shown.

Direct URLs for everything. Primary sources over articles about them. Depth over breadth — 15 verified findings beat 50 vague ones.
