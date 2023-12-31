from random import randint
from brain_games.engine import run_game


MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_numbers_for_simple(number):
    if number == 1:
        return 'no'
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_num_and_primeres():
    number = randint(0, 1001)
    question = f"Question: {number}"
    correct_answer = 'yes' if check_numbers_for_simple(number) else 'no'
    print(question)
    return question, correct_answer


def run_prime_game():
    run_game(get_num_and_primeres)
