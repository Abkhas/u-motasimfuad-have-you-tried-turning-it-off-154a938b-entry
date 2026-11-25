#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun one-line entry.

Writes a single funny line a hopeless tech support agent says to a
desperate customer to /output/entry.txt.
"""

import os

LINE = "Have you tried turning it off and on again? I did \u2014 the whole call centre. You're talking to the last light still on."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
