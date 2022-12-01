"""
Wilson & Sam
A01266055 A01337600
"""


def describe_current_location():
    """
    A string is returned with a description of the location the character is in.

    :return: A string with the description of the location the character is in
    """
    location = make_character("Dave")


def describe_current_location(game_board: dict, character: dict) -> str:
    """
    A function to find and describe current location of player

    not done yet

    """
    return game_board[(character["X-coordinate"], character["Y-coordinate"])]


def main():
    """
    Drive the program
    """
    pass


if __name__ == '__main__':
    main()
