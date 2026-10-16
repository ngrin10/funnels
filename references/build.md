# Build from the spec and design

Read the canonical spec, the version for the builder, the prompt, exact copy, event table, and linked design. Check their versions. Use the repo's own instructions. Run the limits check for any tool or code area that needs more expertise.

## Find the real work

Read the route and current components. Compare live behavior, the spec, and the design. Mark what exists, what needs a change, and what is blocked. A frame shows appearance; it does not settle billing, access, data, or business rules.

| Change | Route / component | Current behavior | Needed work | Data or config source | Dependency / owner | Test proof |
|---|---|---|---|---|---|---|

Use the owner's version to divide work, but read shared dependencies so one change does not break another. Keep out-of-scope work visible with its reason.

## Use the actual system

Reuse the shell, components, tokens, and data hooks. Read changing prices, limits, dates, balances, and access from their source. Define loading, missing, and error behavior. Do not type sample values into production code.

Use approved exact copy. Resolve a conflict between the copy table and frame before coding that text. Keep annotation text and layer names out of the UI. Check which frames are active and which are history.

## Make rules testable

Implement triggers, groups, exclusions, branch rules, back, refresh, repeat use, retries, and partial success. Preserve input after failure. Avoid duplicate records or charges. Keep secrets and sensitive data out of logs and events. Use the existing tracking wrapper and event names when they apply.

Build a blocked part behind a disabled flag only if the user authorized that work and its behavior is clear. A flag does not make an unresolved price or access rule safe to guess.

## Show proof

Check each acceptance line with the relevant evidence: screen, query, test, sandbox transaction, or preview. Verify the payment and access together if both are affected. Check the right tracking account and allowed properties. Test turning the change off and returning to the old flow where required.

For each line, report passed, failed, not run, or blocked. Say what was actually tested and what remains. Keep technical test detail short and explain why it matters in plain words.

Distinguish built, tested, deployed, and measured. Open or link a PR when authorized and possible. A spec request alone does not authorize a deployment, real charge, or message to another person.
