from __future__ import annotations

import argparse
from pathlib import Path

from kana.collector import collect_manual, save_observation


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Kana Lab observation JSON from copied text")
    parser.add_argument("id", help="observation id, e.g. 001-hoso")
    parser.add_argument("command", help="command, e.g. .hoso")
    parser.add_argument("--text-file", required=True, help="UTF-8 text file containing sanitized response text")
    parser.add_argument("--output", default=None, help="output JSON path")
    parser.add_argument("--notes", default="", help="optional context notes")
    args = parser.parse_args()

    content = Path(args.text_file).read_text(encoding="utf-8")
    data = collect_manual(args.id, args.command, content, notes=args.notes)
    output = args.output or f"observations/{args.id}.json"
    save_observation(output, data)
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
