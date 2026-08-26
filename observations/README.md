# Observations

Store sanitized observations of normal Kana interactions here.

## Never commit

- Discord account tokens
- cookies
- Authorization headers
- passwords
- session credentials
- private IDs that are not needed for parsing

## Recommended workflow

1. Run a normal Kana command in Discord.
2. Copy non-sensitive response text or manually transcribe visible embed/component data.
3. Create one JSON file per observation from `examples/observation.example.json`.
4. Validate:

```bash
python tools/validate_observations.py observations
```

## Suggested filenames

```text
001-hoso.json
002-tuido.json
003-danhboss.json
004-shop.json
005-bicanh.json
```

Use `notes` to describe context such as success, cooldown, no active boss, or which UI option was selected.
