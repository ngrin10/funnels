# Ask for the fields the files need

Read the templates and current context first. Use this map to choose the next question. It is not a form to send all at once.

Keep a field list in the context doc. Store value, source/date, state, who can answer, check, and affected change. Use one to three questions per round. Stop and wait. Keep doing only work that does not need the answer.

## Choose the next gap

Start with a gap that changes scope, truth, data safety, or what can be built. Then ask about the next unresolved build rule. Ask about polish last. Do not re-ask a fact already supplied. A suggested answer is not a decided answer.

| Field group | Fields that may be needed | Plain question examples | Used by |
|---|---|---|---|
| L. Limits | Task, allowed work, missing methods, needed skills, data rules | Which data can this work use and where may it be saved? | Context, all outputs |
| P. Product | Buyer, problem, offer, terms, delivery, first value | Who is this for? What do they get after they pay? | Product paragraph, offer, prompt |
| I. Idea | Exact words or summary, source/date, path step, changes, new/update | Does this change the price screen, the step after payment, or both? | Spec opening, numbering |
| E. Evidence | Product facts, live version, data sources, unavailable inputs, conflicts, prior tests | These two sources give different terms. Who can tell us which applies? | Inputs, reasons, limits |
| M. Measure | Main result, account, event/query, window, group, count unit, base, baseline, goal, delay | Does success mean a booking, a held call, or a paid sale? | Judging line, events, test |
| O. Offer | Included/not included, price, currency, billing, trial, refund, limits, next offer | Does this term apply to every plan or just one? | Copy, checkout, delivery |
| S. Shape | Today/next, routes, triggers, group, exclusions, branches, states, exit | What happens if they return after skipping this step? | Change fields, screens |
| D. Data | Shown outputs, inputs, source, existence, missing behavior, safe storage | Does this number already exist, or would a new system have to make it? | Input map, dependencies |
| C. Copy | Customer words, voice, questions, proof, claims rules, exact text, tokens | What should this line say when the name is missing? | Copy table, screens, prompt |
| V. Visuals | Current system, components, frame, devices, access needs, render proof | Which current screen should this match? | DEV section, acceptance |
| B. Build | Repo/tool, route/component, ids/config, contracts, dependencies, order | Who owns the service this button needs? | Builder version, prompt |
| T. Tracking | Name, new/existing, live/broken/missing, trigger, allowed properties, count/dedupe, account, check | Does this event already fire in the right account? | Events, test proof |
| R. Rollout | Fix/test, flag, arms, group split, test method, stop/read plan, recovery | How can this be turned off if it breaks the flow? | Test, recovery, acceptance |
| H. Handoff | Owner, decider, approver if needed, builder split, date/timezone, estimate, access | Which changes belong to each builder? | Header, builder view, prompt |
| A. Acceptance | Behavior proof, event proof, payment/access checks, open items, non-goals | What should the builder show to prove this works? | Acceptance, readiness |

Split questions within a group into separate rounds. Do not ask several hidden questions in one line.

## Follow up with a real distinction

"Better leads" is not a result definition. Ask whether it means useful forms, qualified bookings, held calls, or paid sales. Say which field the answer fills.

"Send them to checkout" needs a real destination and the right product or plan. Inspect the repo first if it can answer. Ask only what remains.

"The new page made the rate fall" is a claim about cause. Record the observed result separately. Ask for the version dates and other changes in the window. Get the right skill before claiming which factor caused it. Do not start a long lesson about every possible cause.

"I don't know the rate" is a valid answer. Record `NOT KNOWN`, the needed report, who can get it, and what it blocks. Draft the rest without inventing a number.

"Just use the usual rule" does not settle a sensitive-data or billing rule. Explain the risk in one plain sentence and ask for the real rule.

## No-assumption rule

Never fill an empty field with a fact-like guess. A mock can use clearly fictional sample data. A proposal must say who needs to decide. A missing skill must stay visible even when the docs are otherwise complete.

## Completion check

Walk every field in the context, checkpoint, source spec, builder version, prompt, and handoff. Mark unused fields with a reason. For each unresolved field, state whether it blocks draft, build, launch, or measurement, and which change it affects.

Check that every answer appears in all files that need it. Use the same change ids, source versions, copy, events, and status. Ask about the highest-impact remaining gap; do not end with "anything else?".
