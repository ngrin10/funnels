# Build prompt: <spec id and surface>

Status: <match spec>
For: <builder and owned changes>
Spec version: <version/date>
Send with: <required files and confirmed access, or self-contained>

Copy the block below into the builder's AI tool.

```text
Build <owned changes> for <product>. Work only within the authorized scope below.

1. CONTEXT
Product, buyer, offer, price/terms, and what happens after purchase:
<filled facts>
Current path and evidence:
<steps, routes, sources with dates; full number definitions or NOT KNOWN>
Inputs not available and source conflicts:
<facts>
Repo/tool, design system, components, ids, owners, due date and timezone:
<values>
Required files supplied with this prompt:
<contents or accessible paths; no dependence on earlier chat>

2. SPEC
Status and decisions:
<match source spec; approvals and blockers per change>
Goal, main metric, and non-goals with reasons:
<values>
For EACH change, with the same id:
<reason, owner, today, next, trigger, audience, exclusions, destinations,
data contracts/dependencies, exact copy and fallbacks, all states,
responsive/accessibility rules, acceptance checks, recovery steps>

3. ROLLOUT AND TEST
<fix or test per change; assignment, arms, split, flag, guardrails,
baseline, minimum worthwhile change, statistical method, sample and time plan, delayed outcomes, stop rule, owner; no made-up rules>

4. EVENTS
<complete event table from spec: names, NEW/EXISTING/NOT KNOWN,
triggers, allowed properties, count unit/dedupe, destination/account,
consent, owner, and test proof>

5. QUESTIONS BEFORE BUILDING
<each unresolved question, owner/check, affected change, what each answer changes>
Ask blocking questions before dependent work. An unknown baseline may block
measurement while a missing payment rule blocks payment work. Continue
unblocked work. Never silently turn a proposal into a decision.

6. HOW TO WORK
Inspect the repo and current behavior. Reuse its components and conventions.
Implement only authorized changes. Preserve exact approved copy and terms.
Test the stated happy path, failures, back/refresh, repeat use, and devices.
Use sandbox payments or mocks; require authorization for real charges.
Check events and recovery. Return acceptance checks with evidence, changed
files, tests actually run, limitations, and remaining blockers.
Do not deploy, publish, or message others unless separately authorized.
```

Cold-read the filled block with no chat history. Repair gaps in both the prompt and spec. Record review type and unresolved blockers. Do not mark an unchecked prompt ready.
