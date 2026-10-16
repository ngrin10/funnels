# Build prompt: <spec id and surface>

Status / version: <match source spec>
For: <builder or team and owned change ids>
Send with: <required files and confirmed access, or fully self-contained>
Owner note: <who gets this, what it asks them to do, dates/owners/costs it commits to, open items>

Copy the filled block into the builder's AI tool.

```text
Build <owned changes> for <product>. Use fifth-grade words when explaining the work. Keep exact code and event names.

1. CONTEXT
Product, buyer, offer, terms, delivery, first value:
<filled facts>
Current path and source dates:
<steps, routes, numbers with tool/account, dates, group, count/base, unit, labels>
Decided vs proposed, by whom and when:
<values>
Where things live, who owns them, due date/timezone:
<repo/tool, components, design, config, ids, tickets, flags>
Not included here, and shared dependencies:
<other changes/owners; build order; what must stay as it is and why>
Inputs not read, conflicts, data rules, and missing skills:
<limits; skills actually read; needed help; affected work>
Required files supplied:
<content or accessible paths; no unseen chat; no unnecessary sensitive data>

2. SPEC
Status and goal:
<match source; baseline/goal and known limits>
For EACH owned change, use the same id:
<reason, owner, today, next, build location, trigger/group/exclusions,
branches/destinations, inputs and existing/missing systems, exact copy,
tokens/fallbacks, states, design/device rules, event links, main measure,
acceptance proof, rollout/recovery, prior work and surface check>

3. ROLLOUT AND TEST
<fix/test per change; control/variant, group, assignment/split, flags,
guardrails, baseline, minimum useful change, statistical method,
sample/time plan, delayed outcomes, stop/read rule and owner;
needed specialist skill or N/A with reason; do not guess>

4. EVENTS
<full spec table: name, NEW/EXISTING/NOT KNOWN, live/broken/missing/not checked,
trigger, allowed properties, count/dedupe, tool/account, consent, owner, proof>

5. QUESTIONS BEFORE BUILDING
<each question or skill gap, who settles it, check, affected change,
what each answer changes, and what stage it blocks>
Ask blocking questions before dependent work. Say "I don't know" when needed.
Get a suitable available skill before doing work beyond current methods.
A skill cannot replace missing data. Do not guess sensitive facts or causes.
Continue only work that does not depend on a missing answer.

6. HOW TO WORK
Read the source spec and current code. Confirm versions and inspect live behavior.
Reuse real components and data sources. Build only the authorized scope.
Use exact approved copy and real terms. Keep sample values out of production.
Test named states, branches, back/refresh, repeat use, devices, events, and recovery.
Use sandbox payments or mocks. A real charge needs authorization.
Show each acceptance line as passed, failed, not run, or blocked, with proof.
Return changed files, checks actually run, limits, help needed, and next action.
Do not deploy, publish, or message others unless authorized for that action.
```

Cold-read the filled block with no chat history. Fix the source spec, builder version, prompt, and handoff together. Record review type and blockers. Never mark blocked changes ready.
