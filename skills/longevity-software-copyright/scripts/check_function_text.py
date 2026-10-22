#!/usr/bin/env python3
"""Count Han characters in a UTF-8 main-functions text; length is not factual review."""
import argparse
import json
from pathlib import Path
import sys


def count_cjk(text):
    ranges = ((0x3400, 0x4DBF), (0x4E00, 0x9FFF), (0xF900, 0xFAFF),
              (0x20000, 0x2EE5F), (0x30000, 0x3347F))
    return sum(any(start <= ord(char) <= end for start, end in ranges) for char in text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text_file", type=Path)
    parser.add_argument("--min-cjk", type=int, default=500,
                        help="Agency/project threshold; not a universal statutory minimum")
    args = parser.parse_args()
    if args.min_cjk < 1:
        parser.error("--min-cjk must be positive")
    count = count_cjk(args.text_file.read_text(encoding="utf-8"))
    passed = count >= args.min_cjk
    print(json.dumps({"cjk_characters": count, "minimum": args.min_cjk,
                      "length_pass": passed, "factual_review": "not_performed"}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
