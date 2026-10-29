"""Prints the law of Equatorial Guinea as it stood on a given day, read from this repository's history.

    python tools/en_vigor_el.py 2020-01-01 ley-fundamental 80         # art. 80 of the Ley Fundamental on 1 January 2020
    python tools/en_vigor_el.py 2020-01-01 ley-fundamental art-080    # the same, by file name
    python tools/en_vigor_el.py 2020-01-01 ley-fundamental            # the whole Ley Fundamental on 1 January 2020
    python tools/en_vigor_el.py --law 2020-01-01 ley-fundamental 80   # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. A bare article number (`80`) means the file `art-080`. Standard library
only.
"""
import re
import runpy
import sys
from pathlib import Path


def article(unit: str) -> str:
    return f'art-{int(unit):03d}' if re.fullmatch(r'\d+', unit) else unit


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != '--law']
    if len(args) == 3:
        i = len(sys.argv) - 1 - sys.argv[::-1].index(args[2])
        sys.argv[i] = article(args[2])
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')
