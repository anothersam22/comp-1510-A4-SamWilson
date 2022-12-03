
def validate_move(move, player, rows):
    """
    A Function that checks if player move is outside the boundary of the game.

    :precondition: rows must be equal to columns
    :postcondition: boolean value of True of False depending on user move
    returns: boolean True of False depending on if user move is out of bounds

    """
    move_key_values = {"Up": -1, "Down": 1,
                       "Right": 1, "Left": -1, }
    return 0 <= (player["X-Coordinate"] + move_key_values[move] if (move == "Up" or move == "Down") else
                 player["Y-Coordinate"] + move_key_values[move]) <= rows - 1, move_key_values[move]



def main():
    """
    Drive the program
    """


if __name__ == '__main__':
    main()
