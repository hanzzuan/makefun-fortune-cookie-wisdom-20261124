"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt. No network, no randomness: the same line every run.
"""

import os
import sys

# Make sure the entry directory is importable before any local import.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# The fortune's twist: estimates are not errors, just promises the code
# has not yet agreed to keep — a nod every developer who has ever
# under-estimated a ticket will recognise.
LINE = "Your estimates are not wrong; they are prophecies the code has not yet agreed to keep."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
