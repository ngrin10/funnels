# Funnels

A public AI skill that turns a rough funnel idea into a clear plan for a builder.

It reads what is already known, asks a few useful questions at a time, and fills the spec, copy, screen brief, build prompt, and handoff. Missing facts stay visible. It works for landing pages, signup, forms, popups, paywalls, onboarding, booking, next offers, and lifecycle messages.

## Install

Download or clone this repo. Keep `SKILL.md`, `references/`, and `examples/` together in a folder named `funnels`.

- **Codex:** place that folder in `~/.agents/skills/`.
- **Claude Code:** place it in `~/.claude/skills/`.
- **Other AI tools:** provide `SKILL.md` and the bundled reference files as context. Ask the tool to follow the workflow. Skill auto-loading depends on the host.

No API key, paid connector, or other skill is required. Live tools help when available; the skill marks unavailable evidence clearly.

## Try it

> Use funnels. Turn this idea into a dev spec and build prompt. Read the notes first. Ask for missing facts in small rounds. Do not guess.

Then paste the idea, share the current page or screen if available, and provide any product notes or results.

For a smaller job:

> Use funnels to improve this form. Keep the current design. Ask only questions that change the work.

## What it makes

By default, save private project work outside this public skill repo:

- `context/funnel-context.md`: known facts, sources, conflicts and missing fields.
- `specs/<id>-<name>.md`: source of truth for each change.
- `deliverables/<id>-build-prompt.md`: prompt with the builder's needed context.
- `deliverables/<id>-handoff.md`: short owner handoff.
- Screen briefs and copy tables as needed.

Use the project's existing paths when they differ. A draft can contain unknowns. A ready build cannot require the builder to guess.

## Included guidance

The skill combines context gathering, question-to-field mapping, conversion checks, plain copy, screen planning, and build review. It is written as fresh, general guidance. It does not bundle client packs, transcript libraries, private links, or internal results. The examples are fictional.

Start with [SKILL.md](SKILL.md), [the interview](references/interview.md), or [the example](examples/booking-page.md). Use [review cases](examples/review-cases.md) to try the behavior in an AI session.

## Check the package

Run `python3 scripts/validate.py` from this repo. It checks local links, required files, frontmatter, template sections, and common private-data patterns. It does not prove interview quality or catch every private detail; review all files before publishing.

Licensed under [MIT](LICENSE).
