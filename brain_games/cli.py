# -*- coding: utf-8 -*-


"""CLI functions."""


import prompt


def welcome_user():
    """Input your name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name = name))
