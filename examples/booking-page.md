# Fictional example: a booking button

All names and facts in this example are invented. No real client data is used.

Request: "People cannot tell where to book. Spec a clearer button."

Known from the supplied page: a coaching service has a page with a button labeled "Continue". The owner says it should open an existing booking page. No analytics export was supplied.

First round:

1. For **C1's destination**, what is the booking URL or route?
2. For **success**, should this be judged on bookings or qualified held calls?
3. For **scope**, is this a wording fix or a test against today's button?

Fictional answers: route `/book`; qualified held calls; wording fix, approved to draft and implement. The existing button already routes to `/book`.

Next, inspect the repo for the event, current component and design rules. Do not ask the owner to supply facts the repo answers. If held-call reporting is unavailable, record it as an unknown instead of inventing a rate.

## Context rows

| Field | Value | Status | Source | Next step / blocker |
|---|---|---|---|---|
| C1 destination | /book | KNOWN | Fictional owner answer, confirmed in fictional code inspection | None |
| C1 label | Book a call | KNOWN | Fictional owner approves this wording in a follow-up | None |
| Main outcome | Qualified held calls per eligible visitor | KNOWN | Fictional owner answer | Define qualification and attribution window before measurement |
| Baseline | NOT KNOWN | NOT KNOWN | No export supplied | Analytics owner pulls same-window eligible visitors and held calls; blocks lift claims |
| Qualification rule | NOT KNOWN | NOT KNOWN | Not supplied | Sales owner defines it; blocks outcome measurement |

## C1 draft

- Today: button says "Continue" and routes to `/book`.
- Next: button says "Book a call"; same destination and design.
- Audience: current eligible visitors; existing visibility rules stay.
- Events: inspect existing click tracking; name and properties NOT KNOWN until checked. Do not invent a second event.
- Rollout: wording fix; use the existing release process, still to be checked.
- Recovery: restore the prior label and verify the destination.
- Acceptance: visible and accessible label matches; keyboard activation opens `/book`; existing visibility and click tracking still work; phone layout fits.
- Non-goals: form, calendar rules, offer, price, and page layout.
- Status: DRAFT. Event and release checks still need to be completed. The baseline alone does not block the wording fix.

The builder version, prompt, and handoff must carry these same unknowns. Do not call this a completed build or a proven conversion lift.

Data rules for this fictional narrow edit: no new fields, storage, joining, sharing, or retention changes are in scope. Existing tracking must be checked without adding personal answers.
