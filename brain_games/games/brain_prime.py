# -*- coding: utf-8 -*-

"""Brain prime game functions."""

from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check if number is prime or not."""
    if number < 2 or not number % 2:
        return False

    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2

    return True


def make_question():
    """Generate game question."""
    number = generate_number()
    question = 'Question: {number}'.format(number=number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
