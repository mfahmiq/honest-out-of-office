#!/usr/bin/env python3
"""Honest Out-of-Office — make.fun entry.

Writes the champion out-of-office auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The entry is the winner of a 16-candidate internal pairwise tournament,
judged against the competition brief in weight order: (1) honesty,
(2) politeness, (3) turn of phrase. See CANDIDATES.md for the full bracket.
"""

import os
from pathlib import Path

# Tournament champion (C11): admits the private truth — the sender's own
# email was opened, sighed at, and closed — while still promising a proper
# reply, so a manager would let it stand. One sentence, 111 characters.
ENTRY = "I'm away, and let's be honest: I opened your email, sighed, and closed it — I'll answer properly when I'm back."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
