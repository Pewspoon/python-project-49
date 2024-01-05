import random
from random import randint
import prompt


def question_for_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')

    result = 0
    while result != 3:
        progression = []
        len_Of_Progression = randint(5, 11)
        len_of_step = randint(0, 11)
        numbers_of_Proggression = randint(0, 100)
        while len(progression) < len_Of_Progression:
            progression.append(numbers_of_Proggression)
            numbers_of_Proggression += len_of_step
        missing_number = '..'
        random_hidden = random.randint(0, len(progression) - 1)
        old_value = progression[random_hidden]
        progression[random_hidden] = missing_number
        output = ' '.join(map(str, progression))
        print(f"Question: {output}")
        user_answer = prompt.string("Your answer:")
        if int(user_answer) == old_value:
            print("Correct!")
            result += 1
        else:
            print(f"""{user_answer} is wrong answer ;(.
            Correct answer was {old_value}.""")
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f"Congratulations, {name}!")


def main():
    question_for_user()


if __name__ == '__main__':
    main()
