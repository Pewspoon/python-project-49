from random import randint
from brain_games.engine import run_game


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_numbers_for_simple(number):
    if number == 1:
        return 'no'
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'


def game_conditions():
    question = randint(0, 1001)
    correct_answer = 'yes' if check_numbers_for_simple(question) else 'no'
    return question, correct_answer
