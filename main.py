#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - one-line entry.

Writes a single line to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8.
"""
import os
import sys

LINE = """Blank screen at midnight.\nI added one print, then two.\nThe bug now prints me."""
MAX = 200
OUT = "/output/entry.txt"

def main():
    if not (1 <= len(LINE) <= MAX) or not LINE.strip():
        sys.exit(f"line failed gate ({len(LINE)} chars)")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
