#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""Brain progression game."""

from brain_games.engine import run
from brain_games.games import brain_progression


def main():
    """Run progression game."""
    run(brain_progression)


if __name__ == '__main__':
    main()
