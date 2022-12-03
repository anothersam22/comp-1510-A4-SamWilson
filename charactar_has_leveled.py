
def character_has_leveled(player, encounter_percentage):
    """
    Implements game functionalities when player levels up.

    :param player: must be a dictionary key pair of the character and stats
    :param encounter_percentage: must be a positive integer
    :return: the players stats, if the player is alive, and if the boss is dead or not
    """
    level_1 = 80
    level_2 = 220
    level_3 = 500
    boss_level = 1000
    name = player["Name"]
    boss_state = False
    dead_state = False

    if level_2 > player['Brain Power'] > level_1:
        player['Level'] += 1
        encounter_percentage += 20
        print()
        print("You are on level 1")
        print()  # add level up acii func here
    elif level_3 > player['Brain Power'] > level_2:
        player['Level'] += 1
        encounter_percentage += 20
        print()
        print("You are on level 2")  # add level up acii func here
        print()
    elif boss_level > player['Brain Power'] > level_3:
        player['Level'] += 1
        print()
        print("You have passed level 3")  # add level up acii func here
        print()
        print("Time to solve final puzzle:")
        print()
        # except you boss_puzzle instead of puzzles
        # puzzles = boss_puzzles
    elif player['Brain Power'] > boss_level:
        print()
        print("YOU FINISHED ALL PUZZLES")
        print(f"{name} has achieved the level of PUZZLE MASTER")
        print()
        boss_state = True
    elif player['Brain Power'] < 0:
        print()
        print(f"{name} has lost all brain power trying to solve final puzzle and died")
        print()
        dead_state = True

    # print(player)  # check to see if brain power increased and decreased.
    print(player['Brain Power'])

    return player, boss_state, dead_state


def main():
    """
    Drive the program
    """
    pass


if __name__ == '__main__':
    main()
