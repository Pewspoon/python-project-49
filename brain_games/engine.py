import prompt
from brain_games.cli import welcome_user


def run_game(get_answer_and_question, instruction):
    """
    engine of games
    :param get_answer_and_question:
    :param instruction:
    """
    print("Welcome to the Brain Games!")
    print(instruction)
    count = 0
    while count != 3:
        question, correct_answer = get_answer_and_question()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct')
            count += 1
        else:
            print(f"""{user_answer} is wrong answer ;(.
                        Correct answer was {correct_answer}.""")
            print(f"Let\'s try again, {welcome_user}!")
            break
    if count == 3:
        print(f'Congratulations, {welcome_user}!')
