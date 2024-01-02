from random import randint
import prompt
import random


def calc():
    result = 0
    while (result != 3):
        numbers = randint(0, 100)
        mathematicalSigns = ('+', '-', '*')
        random_value = random.choice(mathematicalSigns)
        print(f"Question: {str(numbers) + random_value + str(numbers)}")
        user_answer = prompt.string('Your answer:')
        match random_value:
            case '+':
                answer = numbers + numbers
            case '-':
                answer = numbers - numbers
            case '*':
                answer = numbers * numbers
