# -*- coding: utf-8 -*-

"""Game engine functions."""

import prompt
from random import randint


NUMBER_OF_ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_number():
    """Return random number from range."""
    return randint(MIN_NUMBER, MAX_NUMBER)


def check_answer(user_answer, correct_answer):
    """Check user answer."""
    if user_answer == correct_answer:
        message = 'Correct!'
        return True, message
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return False, message.format(wrong=user_answer, correct=correct_answer)


def get_user_answer():
    """Prompt user for answer."""
    return prompt.string('Your answer: ')


def get_user_name():
    """Prompt user for his/her name."""
    return prompt.string('May I have your name? ')


def welcome_user():
    """Ask user for a name and print greeting."""
    user_name = get_user_name()
    greeting = 'Hello, {user_name}!'.format(user_name=user_name)
    print(greeting)
    return user_name


def engine(user_name, play):
    """Game engine process."""
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = play()
        print(question)
        answer, message = check_answer(get_user_answer(), correct_answer)
        print(message)
        if not answer:
            print("Let's try again, {user_name}!".format(user_name=user_name))
            return
        correct_answers += 1
    print('Congratulations, {user_name}!'.format(user_name=user_name))


def run(game=None):
    """Run game."""
    print('Welcome to the Brain Games!')
    if game:
        print(game.DESCRIPTION)
    print()
    user_name = welcome_user()
    if game:
        print()
        engine(user_name, game.make_question)
