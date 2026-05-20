# DRT-Steve

This workspace is used to prepare context, competitor analysis, and tasks for Steve — DRT's developer.

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
