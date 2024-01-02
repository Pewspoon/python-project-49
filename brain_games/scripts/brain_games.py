#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import question_for_user


def welcome():
    """
Texting a welcome text
    """
    print('Welcome to the Brain Games!')


def main():
    """
main func
    """
    welcome()
    welcome_user()
    question_for_user()


if __name__ == '__main__':
    main()
