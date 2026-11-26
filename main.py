"""A tiny writer for two funny lines about ordinary days.

The program puts a pair of short, everyday observations
into /output/entry.txt for a two-line joke contest.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")


def daily_pair():
    """Return two funny lines about everyday life."""
    first = "My alarm clock and I have an agreement: it rings, and I pretend not to hear it."
    second = "The laundry pile grows faster than my motivation to fold it ever will."
    return first + "\n" + second


def confirm_pair_saved(expected):
    """Make sure the saved pair is still word for word the same."""
    stored = ENTRY_PATH.read_text(encoding="utf-8")
    assert stored == expected


def main():
    pair = daily_pair()
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Lay the two lines down exactly, with no newline at the end.
    ENTRY_PATH.write_text(pair, encoding="utf-8")
    # Give the saved text one last look to be sure it matches.
    confirm_pair_saved(pair)


if __name__ == "__main__":
    main()
