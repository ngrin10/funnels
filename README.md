# Funnels

Turn an idea into a clear spec a builder can use. Ask for missing facts. Use fifth-grade words. Say what is not known and when another skill is needed.

The core follows eight steps: capture, ground, shape, check the surface, write, draw, make the build prompt, and hand over. It includes fuller guides for copy, screens, signup, forms, popups, paywalls, onboarding, and the flow after purchase.

## Plays

[Plays](references/plays.md) holds patterns other teams have used: offers, low ticket to high ticket, call funnels and show rate, sales videos, ads to page, positioning, online stores, consumer apps, keeping buyers, and health offers. Each play says when it fits and what to watch. They are rewritten in plain words from public talks. Numbers are what others said, not checked facts, and never a goal for your project.

## Install

Download the skill archive or clone this repo. Keep the whole `funnels` folder together, including `SKILL.md`, `references/`, `examples/`, and `scripts/`.

- Codex: place the folder in `~/.agents/skills/`.
- Claude Code: place the folder in `~/.claude/skills/`.
- Other AI tools: provide `SKILL.md` and its relevant bundled files as context. Auto-loading depends on the host.

The core can work with supplied files. Deep work may need another skill, the right data, tool access, or a qualified person. The skill must name that gap before relying on a method it does not have.

## Try it

> Use funnels. Turn these notes into a source spec, a version for each builder, a build prompt, and a short handoff. Read what I supplied first. Ask a few questions at a time. Use fifth-grade words. Do not assume missing facts. Tell me which parts need another skill or more evidence.

For a small job:

> Use funnels to spec this form fix. Keep the current style. Ask only what changes the work.

## What it makes

Save project work in a private project folder, outside this public skill repo. Use the project's current paths when they exist.

| File | Job |
|---|---|
| `context/funnel-context.md` | Facts, sources, field states, conflicts, skill needs |
| `specs/spec-NN-name.md` | The source spec |
| `deliverables/spec-NN-for-team.md` | The spec split for the builder or team |
| `deliverables/prompt-surface-team.md` | One paste-in block in six parts |
| `deliverables/handoff-NN.md` | Short note for the owner |
| `data/dated-pull.json` | Allowed data pull with `what`, `pulled`, and clear definitions |
| DEV section or screen brief | Today, Next, and build notes per change |

A draft may contain unknowns. A ready build must not require guesses for the changes marked ready.

## What it does well

It sorts facts, asks questions, maps the flow, checks for gaps, and keeps the files in sync. It uses plain writing and clear checks. It pushes back on unsupported claims and sensitive-data assumptions.

It does not teach every part of ads, finance, statistics, health, law, or security. It must find and read the right available skill or name the missing help. More skills do not make missing facts known.

Read [the core skill](SKILL.md), [limits](references/limits.md), [coverage](references/coverage.md), and [the example](examples/booking-page.md), and [plain limit statements](examples/limits-in-action.md).

## Check it

Run `python3 scripts/validate.py`. Use [review cases](examples/review-cases.md) to try behavior in an AI session. Use `--private-terms` with a private file outside this repo to check extra names or terms before sharing. Never add that private file to the package. Package checks do not prove how every model will behave or catch every private detail.

This is fresh, general guidance. No client packs, raw transcripts, private links, internal results, or private sales scripts are included. Examples are fictional. Licensed under [MIT](LICENSE).
