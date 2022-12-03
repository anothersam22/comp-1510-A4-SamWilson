"""
Wilson & Sam
A01266055 A01337600
"""
import random


def make_character(name: str) -> dict:
    """
    Makes the character.

    :param name: must be a string
    :return: dictionary for character with name, location, level, brain power, and values.
    """

    player_dictionary = {"Name": name,
                         "X-Coordinate": random.randint(0, 9),
                         "Y-Coordinate": random.randint(0, 9),
                         "Level": 1,
                         "Brain Power": 0,
                         }
    return player_dictionary


print(make_character("Dave"))


def main():
    """
    Drive the program
    """


if __name__ == '__main__':
    main()
