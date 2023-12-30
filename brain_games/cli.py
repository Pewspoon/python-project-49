import prompt


def welcome_user():
    """
welcome to user
    """
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
