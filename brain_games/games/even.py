from random import randint
from brain_games.consts import BRAIN_EVEN
from brain_games.engine import run_game


def get_num_and_evenres():
    numbers = randint(0, 100)
    correct_answer = 'yes' if numbers % 2 == 0 else 'no'
    print(f"Question: {numbers}")
    return numbers, correct_answer


def run_enev_game():
    run_game(get_num_and_evenres(), BRAIN_EVEN)
