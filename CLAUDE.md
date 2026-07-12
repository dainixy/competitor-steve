# DRT-Steve

This workspace is used to prepare context, competitor analysis, and tasks for Steve — DRT's developer.

## DRT.FM design system (LOCKED — do not redesign)

Everything design-related lives in **`drt-design/`** (top-level folder; start at `drt-design/README.md`):

- **`drt-design/DESIGN.md`** is the brand bible: colors, type, components, motion, performance budgets, logo rules. Read it before building ANY DRT.FM screen; its values are law.
- **`drt-design/logo/`** is the final logo (Heartwave mark + lockup, locked 2026-07-11): SVGs, favicon.ico, app icons, README with the `<head>` snippet. Never redesign or recolor; usage rules in `DESIGN.md §12`.
- `drt-design/guides/design-system-guide.html` explains the whole system in plain language; `drt-design/courses/` holds the distilled UX playbook + 110 rules; `drt-design/research/` holds the report and logo iterations.
- The UI-work protocol (auto de-slop, live design review, variants for big decisions) lives in user-level `~/.claude/CLAUDE.md` and applies here automatically.

## Handoff repo sync (MANDATORY)

Steve reads snapshot GitHub repos under the `dainixy` account (`alexis-soul-handoff`, `alexis-voice-handoff`, `competitor-steve`). They do NOT auto-update. After editing any file that is mirrored in one of them (e.g. `alexis-harness/content/*`, `alexis-soul-rules.html`, `alexis-handoff.html`), mirror + commit + push to the handoff repo **in the same session** (secret-scan first). Check for drift any time with `scripts/check-handoff-sync.sh`. When Steve writes "Dainis/<name>" he means `github.com/dainixy/<name>`.

## Agent skills

Local skills live in `.agents/skills/<skill-name>/SKILL.md`. When the user types `/<skill-name>`, read the corresponding SKILL.md and follow its instructions exactly.

**Note on invocation:** Claude Code's `/` prefix only works for built-in CLI commands. To invoke a local skill in a fresh tab, say: `Starting <task>. Read .agents/skills/<skill-name>/SKILL.md and begin.`

Available skills:
- `/caveman` — simplify communication
- `/competitor-checks` — capture hands-on competitor review notes (paid-account browsing) into per-competitor tabs in `competitor-checks.html`
- `/diagnose` — diagnose a problem in the codebase
- `/grill-me` — interview the user relentlessly about a plan until reaching shared understanding
- `/grill-with-docs` — grill with documentation context
- `/improve-codebase-architecture` — suggest architecture improvements
- `/prototype` — prototype a feature quickly
- `/setup-matt-pocock-skills` — scaffold per-repo config for engineering skills
- `/tdd` — test-driven development workflow
- `/to-issues` — convert plans to GitHub issues
- `/to-prd` — convert ideas to a PRD
- `/triage` — triage incoming issues
- `/write-a-skill` — write a new skill
- `/zoom-out` — step back and assess the big picture

### Issue tracker

Issues live as markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary (`needs-triage` / `needs-info` / `ready-for-agent` / `ready-for-human` / `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context — one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
