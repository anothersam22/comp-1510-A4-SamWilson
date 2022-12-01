def character_has_leveled(game_board, character):
    """
    Returns true if character has leveled up.

    :param game_board: must be an array of 10x10
    :param character: must be the dictionary key value "name":""
    :return: True if the character has leveled up
    """
    if character["Current HP"] > game_board["level"] * 100:
        return True


def main():
    """
    Drive the program
    """
    pass


if __name__ == '__main__':
    main()
