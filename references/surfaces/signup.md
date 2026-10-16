# Signup and quiz flows

Map the first question through access, verification, and the next useful action. A finished form is only one step.

## Fill the rules

Name the account type, entry source, required data, reason for each question, account creation point, verification rules, next destination, and first value. For a quiz, state which answers change a result or route. Do not collect sensitive answers just because a template asks for them.

## Check each field and step

Use visible labels and the right keyboard. Explain required phone, company, or profile fields. Keep optional fields clear. Use defaults only when safe and allowed; never use a default answer as evidence that the person chose it.

For passwords and sign-in, use the product's auth rules. Do not remove checks without the right security review. Cover social sign-in failure, duplicate accounts, forgotten passwords, expired links, and return visits when relevant.

For each step, say why it must happen before first value. Defer it only when the product can still work and the owner agrees. If adding a step, name what it replaces or what benefit it is meant to test.

## Define the branches

| Step | Fields and rules | Next step by answer | Back / edit behavior | Saved progress | Failure and recovery |
|---|---|---|---|---|---|

State when answers are saved, where they may live, and how edits affect later results. Keep data when a submit fails. Explain a wait or verification step and provide a safe retry.

## Check after submit

Confirm success, show how to get access, and name the next action. Avoid a dead end or a welcome tour that blocks first value. For email verification, define the resend, expired-link, changed-email, and already-verified paths.

## Measure and prove

Track the eligible start, step completion, errors, created account, verified access, and first value as relevant. Check whether these events exist before adding more. Keep personal answers out of event properties unless the project allows them.

Show proof for each branch, phone layout, keyboard path, error, and retry. Judge useful accounts and first value as well as raw signup count. Get a tracking or test skill if the task needs new data rules or a causal claim.
