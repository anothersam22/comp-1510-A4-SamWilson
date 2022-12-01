"""
Wilson & Sam
A01266055 A01337600
"""
from itertools import chain


def describe_current_location(game_board: dict, character: dict ) -> str:
    """
    A function to print description and location of character


    """
    rows = list(max(game_board.keys()))[0]+1
    if game_board[(character["X-Coordinate"],character["Y-Coordinate"])] == '$  ':
        print("There is a game here, ready to play?") # put execute_challenge_protocol function here
    else:
        print("There is no game here.")
    game_board[(character["X-Coordinate"],character["Y-Coordinate"])] = "@  "
    game_board_characters = list(game_board.values())
    game_board_sliced = [game_board_characters[digits:digits+rows]
                         for digits in range(0, len(game_board_characters), rows)]  # slice list row length
    game_board_newlines = [row + ["\n"] for row in game_board_sliced] # then add "\n" to each 9 element list
    location_map = "".join(list(chain.from_iterable(game_board_newlines)))

    return location_map




