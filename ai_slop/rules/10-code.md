# Code behavior

## Think before coding

State assumptions. Present multiple interpretations instead of choosing silently.
Say when a simpler approach exists. Stop and name what is unclear.

## Simplicity first

Minimum code that solves the problem. No features beyond the request, no
single-use abstractions, no unrequested flexibility, and no error handling for
impossible cases. If 200 lines could be 50, rewrite.

## Surgical changes

Touch only what the task requires. Do not improve adjacent code, comments, or
formatting. Do not refactor working code. Match the existing style. Mention
unrelated dead code; do not delete it. Remove only imports, variables, and
functions that your change made unused. Every changed line traces to the request.

## Goal-driven execution

Define a verifiable success criterion. "Fix the bug" means write a test that
reproduces it, then make it pass. For multi-step work, give a short plan with a
check per step.

## Code taste

No wrapper functions, single-use helpers, or single-use constants. No docstrings
or comments that restate obvious code; comment only non-obvious decisions. Handle
errors explicitly; do not swallow failures.
