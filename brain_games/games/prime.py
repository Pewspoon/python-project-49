import math
from random import randint


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_numbers_for_simple(number):
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
    return is_prime


def game_conditions():
    question = randint(0, 1001)
    correct_answer = 'yes' if check_numbers_for_simple(question) else 'no'
    return question, correct_answer
