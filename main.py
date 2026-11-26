"""Best-meal entry: prison noodles shared on a cellmate's last night.

Writes one single sentence (<=200 chars, no trailing newline) to
/output/entry.txt. Stdlib only. Kept short on purpose: on an exact
judge-rate tie the smaller text wins the tie-break.
"""

import os

ENTRY = (
    "The instant noodles my cellmate and I split on his last night inside "
    "\u2014 one cracked egg, two plastic forks, bleach in the air \u2014 beat "
    "every free meal I have eaten since."
)


def _single_sentence(text):
    """Return True when text is exactly one sentence ending in a period."""
    stripped = text.strip()
    if not stripped or stripped != text:
        return False
    if not stripped.endswith("."):
        return False
    return stripped.count(".") == 1


def _checked_entry():
    """Validate the entry against the competition gate before writing."""
    if not ENTRY:
        raise ValueError("entry is empty")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(ENTRY) > 200:
        raise ValueError("entry exceeds 200 characters: %d" % len(ENTRY))
    if not _single_sentence(ENTRY):
        raise ValueError("entry is not exactly one sentence")
    return ENTRY


def main():
    sentence = _checked_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(sentence)


if __name__ == "__main__":
    main()
