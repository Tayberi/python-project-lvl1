# -*- coding: utf-8 -*-

"""CLI function."""

import prompt


def welcome_user():
    """Input your name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name
