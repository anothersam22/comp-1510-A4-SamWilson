"""
Wilson & Sam
A01266055 A01337600
"""


def make_character(character):
    """
    Makes the character.

    :param character:
    :return:
    """

    dictionary = {"Name": character,
                  "X-Coordinate": 0,
                  "Y-Coordinate": 0,
                  "Strength": 0,
                  "Speed": 0,
                  "Shield": 0,
                  "Current HP": 100,
                  "Max HP": 100
                  }
    return dictionary


print(make_character("Dave"))
