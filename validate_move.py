def validate_move(game_board: dict, user_choice: int, character: dict) -> bool:
    """
    A function to check if the player move is possible.

    :precondition: assumes 1 for North, 2 for East, 3 for West, 4 for South
    """
    min_border = min(game_board.keys())
    max_border = max(game_board.keys())
    character_x_position = character["X-coordinate"]
    character_y_position = character["Y-coordinate"]

    if ((1 > user_choice > 4)
        or (user_choice == 1 and character_x_position == min_border[0])
        or (user_choice == 2 and character_y_position == max_border[0])
        or (user_choice == 3 and character_y_position == min_border[0])
            or (user_choice == 4 and character_x_position == max_border[0])):
        return False
    else:
        return True


def main():
    """
    Drive the program
    """


if __name__ == '__main__':
    main()
