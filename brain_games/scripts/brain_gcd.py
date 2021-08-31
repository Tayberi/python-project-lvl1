#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""Brain gcd game."""

from brain_games.engine import run
from brain_games.games import brain_gcd


def main():
    """Run gcd game."""
    run(brain_gcd)


if __name__ == '__main__':
    main()
