import random
from random import randint
from brain_games.consts import BRAIN_PROGRESSION
from brain_games.engine import run_game


def get_num_and_progressionres():
    progression = []
    len_of_progression = randint(5, 11)
    len_of_step = randint(0, 11)
    numbers_of_Proggression = randint(0, 100)
    
    while len(progression) < len_of_progression:
        progression.append(numbers_of_Proggression)
        numbers_of_Proggression += len_of_step
    
    missing_number = '..'
    random_hidden = random.randint(0, len(progression) - 1)
    old_value = progression[random_hidden]
    progression[random_hidden] = missing_number
    output = ' '.join(map(str, progression))
    question = f"Question: {output}"
    return question, old_value


def run_progression_game():
    run_game(get_num_and_progressionres(), BRAIN_PROGRESSION)