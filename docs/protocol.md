# Kana protocol notes

This file is deliberately conservative. It will contain only protocol/interface behavior that can be confirmed through an authorized client or documentation.

## Current status

Transport: unknown

Authentication/session interface: unknown

Command request format: command names are known, transport is not yet confirmed.

Response format: unknown

Interaction/component format: unknown

Cooldown representation: only human-readable command-list values are currently known.

## Observation format

For each experiment record:

1. Command/action performed.
2. Context (server/channel/game state).
3. Observed response type.
4. Relevant non-sensitive fields.
5. Parsed state.
6. Cooldown/result.
7. Confidence: observed / confirmed / inferred.

Never store tokens, cookies, authorization headers, or other credentials in this document.
