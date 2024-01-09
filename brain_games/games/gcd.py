from random import randint
from brain_games.engine import run_game

MESSAGE = 'Find the greatest common divisor of given numbers.'


def check_gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def get_num_and_gcdres():
    m = randint(1, 101)
    n = randint(1, 101)
    question = f'{m} {n}'
    correct_answer = check_gcd(m, n)
    return question, correct_answer


def run_gcd_game():
    run_game(get_num_and_gcdres, MESSAGE)
