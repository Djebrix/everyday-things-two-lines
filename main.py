"""Everyday Things, Two Lines.

Writes entry.txt: two lines explaining a traffic jam to a 10-year-old
through a supermarket-checkout analogy, then why the analogy works
(and where it breaks down).
"""

import os

ENTRY_TEXT = (
    "A traffic jam is like a supermarket checkout queue where every shopper "
    "has a full trolley but only one till is open, so the whole line inches "
    "forward one beep at a time.\n"
    "The analogy works because it maps cars to shoppers and the narrow road "
    "to the single open till, but it leaves out that drivers can honk, "
    "switch lanes, or escape down a side street — shoppers stuck at a till "
    "cannot.\n"
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
