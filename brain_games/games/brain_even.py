# -*- coding: utf-8 -*-

"""Brain even game functions."""

from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def correct_answer(number):
    """Return expected answer."""
    return 'no' if number % 2 else 'yes'


def make_question():
    """Generate game question."""
    number = generate_number()
    question = 'Question: {number}'.format(number=number)
    answer = correct_answer(number)
    return question, answer
