from random import randint
import prompt


def check_gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def question_for_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')

    result = 0
    while (result != 3):
        m = randint(0, 100)
        n = randint(0, 100)
        print(f"Question: {m} {n}")
        answer_user = int(prompt.string('Your answer:'))
        answer = check_gcd(m, n)
        if answer_user == answer:
            print("Correct!")
            result += 1
        else:
            print(f"{answer_user} is wrong answer ;(. Correct answer was {answer}.")
            print(f"Let's try again, {name}!")
            break
    if result == 3:
        print(f"Congratulations, {name}!")


def main():
    question_for_user()


if __name__ == '__main__':
    main()
