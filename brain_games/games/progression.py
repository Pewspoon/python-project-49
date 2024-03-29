import random
from random import randint


CONDITION = 'What number is missing in the progression?'


def game_conditions():
    progression = []
    len_of_progression = randint(5, 11)
    len_of_step = randint(0, 11)
    numbers_of_Proggression = randint(0, 100)

    while len(progression) < len_of_progression:
        progression.append(numbers_of_Proggression)
        numbers_of_Proggression += len_of_step

    missing_number = '..'
    random_hidden = random.randint(0, len(progression) - 1)
    correct_answer = progression[random_hidden]
    progression[random_hidden] = missing_number
    output = ' '.join(map(str, progression))
    question = f"Question: {output}"
    return question, correct_answer
