# -*- coding: utf-8 -*-

"""Brain calc game functions."""

import operator
from random import choice

from brain_games.engine import generate_number

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_operation():
    """Generate random operation."""
    return choice(list(operations.keys()))


def correct_answer(num1, operation, num2):
    """Return correct answer."""
    return str(operations[operation](num1, num2))


def make_question():
    """Generate make question."""
    num1 = generate_number()
    num2 = generate_number()
    operation = generate_operation()
    question = 'Question: {num1} {operator} {num2}'.format(
        num1=num1,
        operator=operation,
        num2=num2,
    )
    answer = correct_answer(num1, operation, num2)
    return question, answer
