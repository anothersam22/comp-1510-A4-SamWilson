"""
Wilson & Sam
A01266055 A01337600
"""
from itertools import chain



def describe_current_location(game_board: dict, character: dict) -> str:
    """
    A function to print description and location of character


    """
    rows = list(max(game_board.keys()))[0]+1
    # if game_board[(character["X-Coordinate"], character["Y-Coordinate"])] == '$  ':
    #     print("There is a puzzle here.")
    # else:
    #     print("There is no puzzle here.")
    game_board_copy = game_board.copy()
    game_board_copy[(character["X-Coordinate"],
                     character["Y-Coordinate"])] = "@  "
    game_board_characters = list(game_board_copy.values())
    game_board_sliced = [game_board_characters[digits:digits+rows]
                         for digits in range(0, len(game_board_characters), rows)]  # slice list row length
    game_board_newlines = [row + ["\n"]
                           for row in game_board_sliced]  # then add "\n" to list
    location_map = "".join(list(chain.from_iterable(game_board_newlines)))

    print(location_map)

    # return location_map



