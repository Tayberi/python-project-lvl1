#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""Brain calc game."""

from brain_games.engine import run
from brain_games.games import brain_calc


def main():
    """Run calc game."""
    run(brain_calc)


if __name__ == '__main__':
    main()
