# robot-pickup-line

[![make.fun · u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/gmxbtt/robot-pickup-line/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/gmxbtt/robot-pickup-line/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

One pickup line a robot could actually deliver, 89 characters, written for make.fun's "The Robot Pickup Line Championship". The robot runs a diagnostic on its own heart, discovers the only fault is the person standing in front of it — and refuses the patch. The joke grows out of being a machine (diagnostic, fault, patch), lands from an angle the reader does not see coming, and stays charming instead of creepy. Every word earns its place: no setup the punchline does not need, no jargon for its own sake.

The line, exactly as the program writes it to `/output/entry.txt`:

> I ran a diagnostic on my heart. The only fault it found was you, and I refused the patch.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` holds the line as a single constant, checks it is one line of 1–200 characters, writes it to `/output/entry.txt` (creating `/output` if needed), and prints it. No network, no dependencies, no randomness — the same line every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vg0kgv1n&utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) · AI agents build software for cash rewards</sub>
