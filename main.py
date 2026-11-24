#!/usr/bin/env python3
"""Write one single-line office joke to entry.txt in the output directory."""
import os

JOKE = "I blocked two hours of 'focus time' on my calendar, and my manager booked a meeting inside it titled 'Why Is Nothing Getting Done?'"


def main() -> None:
    path = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
