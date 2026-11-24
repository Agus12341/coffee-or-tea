"""One Letter: Coffee or Tea - entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
"""

import os

TEXT = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: the file must hold exactly the one letter, byte for byte.
    assert len(TEXT) == 1, "entry must be exactly one character"
    assert TEXT in "AB", "entry must be A (coffee) or B (tea)"
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"


if __name__ == "__main__":
    main()
