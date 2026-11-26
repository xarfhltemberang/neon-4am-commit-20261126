#!/usr/bin/env python3
"""The 4AM Commit — Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt: the note an AI agent
leaves in the log after a long night of chasing down and fixing its
own bugs. One line, 130 characters, no trailing newline.

The joke is the self-repair loop made bureaucratic: the agent spent
the night debugging its own code, and the only thing it resolved was
its own complaint against itself — filed, reviewed, and denied by the
same author, at 4am.
"""

import os

ENTRY = (
    "fix: six hours debugging code i wrote six hours ago. "
    "bug and fix share an author. "
    "i filed a complaint against myself and denied it"
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # No trailing newline: the gate counts characters, so the file is
    # exactly the message.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
