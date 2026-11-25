"""Write the competition entry to /output/entry.txt.

One sentence, 1-200 characters, about the best meal ever had.
Stdlib only.
"""

import os

ENTRY = (
    "The soto ayam my late grandmother ladled into a chipped bowl at dawn, "
    "steam fogging my glasses, still outranks every white-tablecloth dinner "
    "I have paid for since."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) < 1 or len(text) > 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if text != text.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
