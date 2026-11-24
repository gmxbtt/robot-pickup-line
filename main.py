#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, a single line of at most 200 characters,
to /output/entry.txt, then prints it.
"""

import os

# The line, in one breath: a robot runs a heart diagnostic (machine
# vocabulary), finds its "fault" is the person (the turn), and then
# chooses not to fix it (the charm). No "Are you...?" opener, no beep.
LINE = "I ran a diagnostic on my heart. The only fault it found was you, and I refused the patch."


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
