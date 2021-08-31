# -*- coding: utf-8 -*-

"""Brain progression game functions."""

from random import choice, randint

from brain_games.engine import generate_number

DESCRIPTION = 'What number is missing in the progression?'
LENGTH_OF_PROGRESSION = 10
STEP_MIN = 1
STEP_MAX = 5


def make_progression():
    """Generate arithmetic progression."""
    first_number_of_progression = generate_number()
    step = randint(STEP_MIN, STEP_MAX)
    last_number_of_progression = (step * LENGTH_OF_PROGRESSION) + first_number_of_progression
    return range(first_number_of_progression, last_number_of_progression, step)


def make_question():
    """Generate make question."""
    progression = make_progression()
    secret = choice(progression)

    progression_witch_secret_number = ' '.join([
        '..' if num == secret else str(num) for num in progression
    ])
    question = 'Question: {progression}'.format(
        progression=progression_witch_secret_number,
    )

    return question, str(secret)
