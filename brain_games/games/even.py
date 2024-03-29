from random import randint


CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_conditions():
    question = randint(0, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
