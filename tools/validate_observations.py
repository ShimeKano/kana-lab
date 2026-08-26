from __future__ import annotations

import argparse
import json
from pathlib import Path

from kana.observation_schema import validate_observation_shape


def iter_json_files(root: Path):
    if root.is_file():
        yield root
    else:
        yield from sorted(root.rglob("*.json"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Kana Lab observation JSON files")
    parser.add_argument("path", nargs="?", default="observations", help="file or directory to validate")
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists():
        print(f"No observations found: {root}")
        return 0

    files = list(iter_json_files(root))
    if not files:
        print(f"No JSON files found under: {root}")
        return 0

    failed = 0
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"FAIL {path}: invalid JSON ({exc})")
            failed += 1
            continue

        errors = validate_observation_shape(data)
        if errors:
            print(f"FAIL {path}: " + "; ".join(errors))
            failed += 1
        else:
            print(f"OK   {path}")

    print(f"Validated {len(files)} file(s); failures: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
