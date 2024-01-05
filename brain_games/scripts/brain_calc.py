import random
import prompt
from random import randint


def question_for_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    result = 0
    while (result != 3):
        numbers = randint(0, 100)
        mathematicalSigns = ('+', '-', '*')
        random_value = random.choice(mathematicalSigns)
        print(f"Question: {str(numbers)} {random_value} {str(numbers)}")
        user_answer = prompt.string('Your answer:')
        match random_value:
            case '+':
                answer = numbers + numbers
            case '-':
                answer = numbers - numbers
            case '*':
                answer = numbers * numbers
        

        if str(user_answer) == str(answer):
            print('Correct!')
            result += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}.")
            print(f"Let\'s try again, {name}!")
            break
    if result == 3:
        print(f"Congratulations, {name}!")


def main():
    question_for_user()


if __name__ == '__main__':
    main()
