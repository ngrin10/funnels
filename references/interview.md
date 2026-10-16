# Interview field map

Read the templates first. Keep a field list in the context doc. One row can feed several docs. Split these topics into rounds of one to three questions; this table is not a questionnaire to send all at once.

Ask only missing fields. Record `NOT APPLICABLE` with a reason for unused fields. Record an unknown with an owner, check, and affected change. Do not force a user to invent a number.

| Round | Fields to fill | Plain questions to choose from | Used by |
|---|---|---|---|
| Goal | Request type; desired output; scope | Is this an audit, a spec, copy, screens, or a build? What should be different when it is done? | Context, spec, prompt |
| Product | Buyer; problem; offer; delivery; price and terms | Who buys this? What do they get? What happens after payment? | Context, copy, prompt |
| Path | Entry source; steps; surface; current URL or route; next destination | Where do people come from? Which step needs work? Where should the main button take them? | Path, current and next state |
| Evidence | Live behavior; sources and dates; unavailable inputs; conflicting facts | Which screen is live? Does this note describe today or a plan? These two sources disagree: which applies? | Inputs, conflicts, current state |
| Measurement | Account; event definitions; window; cohort; count unit; baseline; target | What action counts as success? Where is it tracked? How many eligible people reached this step, and how many finished? | Numbers, events, success |
| Prior work | Earlier tests; dates; outcomes; known bugs | Has this been tried? What was different then? | Evidence, reasons |
| Audience | Segment; eligibility; exclusions; entry and exit rules | Who should see it? Who should never see it? What makes it appear or stop? | Change, events, rollout |
| Behavior | Today; next; branches; back; refresh; repeat use; empty, error and success states | What happens after the tap? What if it fails? What if someone returns? | Spec, screens, acceptance |
| Copy | Customer evidence; promise; objections; proof; claims rules; tokens and fallbacks | Which customer words can be used? What supports this claim? What should show when the name is missing? | Copy, spec, prompt |
| Design | Existing system; components; frames; responsive sizes; accessibility | Which design should this match? Is this frame current? Which devices matter? | Screen brief, build |
| Build | Repo/tool; routes; component and config ids; data contracts; dependencies; owner | Where does this live? Which parts already exist? Who owns the API or setting it needs? | Build location, prompt |
| Events | Name; new/existing; trigger; properties; dedupe; consent; destination; test method | Does this event already fire? What exactly triggers it? Which fields may be recorded? | Tracking, prompt, acceptance |
| Rollout | Fix or test; allocation; flag; rollback; baseline; minimum worthwhile change; statistical method; sample plan; stop rules; guardrails | Is this a repair or a test? How can it be turned off? What result means stop? | Rollout, test, recovery |
| Delivery | Decider; approver if needed; builder; estimate; date; timezone; artifact home | Who decides and builds? Is there a due date? What files can the builder access? | Header, handoff, prompt |
| Finish | Non-goals; proof of completion; blockers; authorization | What must stay as it is, and why? What should the builder show to prove it works? | Acceptance, handoff |

## Follow-ups that fill the gap

Vague: "We want better leads."
Ask: "For the **success measure**, does a good lead mean a valid form, a qualified booking, or a held sales call? This changes the event and test."

Vague: "Send them to checkout."
Ask: "For **C1's destination**, which checkout URL or route should open? If it does not exist, who will create it?"

Unknown: "I don't know our rate."
Record: `NOT KNOWN; owner: analytics owner; check: eligible page visitors and completed bookings in the same window; blocks: judging C1's lift, not drafting its layout.`

Conflict: old note says one price, checkout shows another.
Keep both values with dates. Ask who owns the price decision. Block price copy and payment changes until resolved.

## Completion gate

Check every heading and table column in the context, spec, prompt, and handoff templates against the field list. Ask the next high-impact missing field. Do not declare readiness just because each interview topic was visited. Propagate corrections to every affected doc and change id.
