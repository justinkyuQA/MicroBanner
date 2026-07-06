import sys

from .core import grab

HELP = """
MicroBanner v0.1

Usage

python3 -m microbanner <host>

Example

python3 -m microbanner example.com
"""

def main():

    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    grab(args[0])
