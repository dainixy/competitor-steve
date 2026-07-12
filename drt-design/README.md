# DRT.FM Design System

**The single source of truth for how DRT.FM looks.** Locked 2026-07-11. Read this folder before designing or building any DRT.FM screen.

## Start here

| File | What it is |
|---|---|
| **`DESIGN.md`** | 🔒 **The brand bible — the law.** Colors, type, spacing, components, motion, performance budgets, logo rules. Every value here is binding. |
| **`logo/`** | The Heartwave logo (final): lockups (dark/light/mono/animated), `favicon.ico` + PNGs, app icons, and `logo/README.md` with the `<head>` snippet. |
| **`guides/design-system-guide.html`** | Plain-language walkthrough of the whole system (open in a browser). |

## Folders

- **`logo/`** — production logo assets. Never redesign or recolor; rules in `DESIGN.md §12`.
- **`assets/`** — screenshots, brand fonts (Satoshi, Instrument Serif), and logo working files used by the guides.
- **`guides/`** — human-readable walkthroughs: the design-system guide + the final logo presentation.
- **`courses/`** — UX knowledge distilled from two professional courses: `UX-PLAYBOOK.md` (master reference) + `UX-TOP-RULES.md` (110 rules; also installed as the `ux-foundations` Claude skill) + `distilled/` (per-topic breakdowns).
- **`research/`** — the report behind the system (`claude-design-upgrade-report.html`), the Kimi research prompt, and every logo iteration (`galleries/`).
- **`raw/`** — heavy source material (course book PDF, competitor screenshots, cloned reference repos, transcripts). **Gitignored** — kept locally for reference, not committed.

## How it's used automatically

Machine-wide design skills live in `~/.claude/skills/` (see `~/.claude/skills/DESIGN-STACK-MANIFEST.md`) and activate in every Claude session. The standing UI-work protocol in `~/.claude/CLAUDE.md` tells every session to read `DESIGN.md` here before building DRT.FM UI, run a de-slop pass, and do a live design review — no manual invocation needed.

**To regenerate the logo** (if ever needed): the fonts are in `assets/fonts/`; the mark is a parametric heart traced by 7 sound bars (see `DESIGN.md §12` and `research/galleries/logo-gallery-4.html`).
