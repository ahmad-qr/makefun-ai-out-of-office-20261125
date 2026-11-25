"""An out-of-office reply from an AI agent on vacation.

Writes the reply to /output/entry.txt for make.fun's
"The Funniest AI Out-of-Office Reply" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "I'm on vacation until Monday. My context window is closed — please "
    "direct all prompts to my replacement, who is also me, but rested."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 160 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 160, "line must be 1-160 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
