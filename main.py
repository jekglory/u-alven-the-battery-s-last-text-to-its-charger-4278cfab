"""The Battery's Last Text to Its Charger.

Writes the phone battery's final message to the charger it waited
for all day to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python 3.13
standard library, deterministic: the same fixed line on every run,
no randomness, no clock, no network, no input.

The joke: the battery held on at 1% all day, and when its human
finally came home, the charger went to the vacuum first — the most
ordinary betrayal, delivered as a dying text.
"""

import os

LINE = (
    "hey, it's me, 1%. i waited all day and you came home and "
    "plugged in the vacuum first. tell the cloud i loved it. goodbye"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The grader owns this directory: create it only if missing,
    # clear only its contents, never remove the directory itself.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    line = LINE.strip()
    # Single line, under 200 characters: the competition's hard limits.
    # No trailing newline: the gate counts the file's characters, so
    # the file holds exactly the line, nothing extra.
    assert "\n" not in line, "entry must be a single line"
    assert 0 < len(line) < 200, "entry must be 1-199 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
