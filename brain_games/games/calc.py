import random
from random import randint
from brain_games.engine import run_game


MESSAGE = 'What is the result of the expression?'


def get_num_and_calcres():
    numbers = randint(0, 100)
    mathematical_signs = ('+', '-', '*')
    random_value = random.choice(mathematical_signs)
    correct_answer = None
    question = f"{str(numbers)} {random_value} {str(numbers)}"
    if random_value == '+':
        correct_answer = numbers + numbers
    elif random_value == '-':
        correct_answer = numbers - numbers
    elif random_value == '*':
        correct_answer = numbers * numbers
    return question, correct_answer


def run_calc_game():
    run_game(get_num_and_calcres, BRAIN_CALC)
