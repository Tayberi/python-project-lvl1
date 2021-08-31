# -*- coding: utf-8 -*-

"""Brain gcd game functions."""

from brain_games.engine import generate_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    """Return correct answer."""
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1

    return num1 + num2


def make_question():
    """Generate make question."""
    num1 = generate_number()
    num2 = generate_number()
    question = 'Question: {num1} {num2}'.format(num1=num1, num2=num2)
    answer = gcd(num1, num2)
    return question, str(answer)
