from random import randint
from brain_games.cli import *
import prompt


def check_numbers_for_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def question_for_user():
    print(f"Question: {randint(0, 100)}")
    answer = prompt.string("Your answer:")


    if answer == 'yes' and check_numbers_for_even(answer):
        print('Correct!')
    else:
        print('\'yes\' is wrong answer ;(. Correct answer was \'no\'. Let\'s try again, {brain_games.name}!')