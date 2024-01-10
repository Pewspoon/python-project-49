import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.CONDITION)
    count = 0
    ROUNDS = 3
    while count < ROUNDS:
        count += 1
        question, correct_answer = game.game_conditions()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
