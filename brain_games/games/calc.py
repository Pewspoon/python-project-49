import random
from random import randint


CONDITION = 'What is the result of the expression?'


def game_conditions():
    numbers = randint(0, 100)
    mathematical_signs = ('+', '-', '*')
    random_value = random.choice(mathematical_signs)
    correct_answer = 0
    question = f"{str(numbers)} {random_value} {str(numbers)}"
    if random_value == '+':
        correct_answer = numbers + numbers
    elif random_value == '-':
        correct_answer = numbers - numbers
    elif random_value == '*':
        correct_answer = numbers * numbers
    return question, correct_answer
