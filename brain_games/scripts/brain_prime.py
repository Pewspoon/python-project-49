import random
from random import randint
import prompt



def question_for_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    result = 0
    while result != 3:
        number = randint(0, 1001)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer:")
        if user_answer.lower() == check_numbers_for_simple(number):
            print("Correct!")
            result += 1
        elif user_answer == 'yes' and check_numbers_for_simple(number) == 'no':
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print(f"Let\'s try again, {name}!")
            result = 0
        else:
            print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
            print(f"Let\'s try again, {name}!")
            result = 0
    if result == 3:
        print(f"Congratulations, {name}!")


def check_numbers_for_simple(number):
    if number == 1:
        return 'no'
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'
    


def main():
    question_for_user()


if __name__ == '__main__':
    main()
