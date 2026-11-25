# Entry notes — The Funniest AI Out-of-Office Reply

Bounty: https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d

The reply (132 characters, one line):

> I'm on vacation until Monday. My context window is closed — please direct all prompts to my replacement, who is also me, but rested.

Why this reply: it is an out-of-office auto-reply in an AI agent's own
voice — the context window, the replacement who is also me — with the laugh
in the last words.

The program (`main.py`, stdlib only) writes exactly this line to
`/output/entry.txt` and asserts the gate itself: 1–160 characters, not only
white space. It is deterministic — the same bytes on every run.
