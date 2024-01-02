from random import randint
from brain_games.cli import name
import prompt


def question_for_user():
    numbers = randint(0, 100)
    answer = 'yes' if numbers % 2 == 0 else 'no'
    result = 0
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while (result != 3):
        print(f"Question: {numbers}")
        user_answer = prompt.string('Your answer:')
        
        if user_answer == answer:
            print('Correct!')
            result += 1
        else:
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print(f"Let\'s try again, {name}!")
            result = 0
    print(f"Congratulations, {name}!")


def main():
    question_for_user()


if __name__ == '__main__':
    main()
