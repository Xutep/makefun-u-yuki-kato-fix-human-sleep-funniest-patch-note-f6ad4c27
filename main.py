"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed, to /output/entry.txt. Deterministic: no clock, no random
input, no network, stdlib only. The line is a fixed constant, so every
run produces byte-identical output.
"""

import os

PATCH_NOTE = (
    "Fixed: human sleep no longer crashes at 3 AM. "
    "Your brain will stop opening 47 tabs about that embarrassing "
    "thing you said in 2012."
)

MAX_CHARS = 160


def main() -> None:
    line = PATCH_NOTE.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("patch note must be a single line")
    if not line:
        raise ValueError("patch note must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError("patch note exceeds 160 characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read back what we wrote: the file on disk must be exactly the
    # single line we validated, so a partial write can never pass.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise ValueError("entry.txt on disk does not match the patch note")


if __name__ == "__main__":
    main()
