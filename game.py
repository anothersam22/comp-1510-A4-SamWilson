"""
Sam A01337600
Wilson A01266055
"""

import csv
import random
import string
from itertools import chain

with open("puzzle_set_1.csv", newline='') as file:
    reader = csv.reader(file)
    puzzles = list(reader)


def get_user_choice(choices: tuple or list) -> int:
    """
    Gets the user choice from choices.

    :param choices: must be a tuple or a list
    :precondition: user must enter a number, any other type of entry will crash the program.
    :precondition: choices must be a tuple or a list
    :postcondition: prints if input is not within the range print "That's not a valid choice"
    :postcondition: returns user choice - 1 if input is within the range
    :return: the user choice
    """
    while True:
        for number, choice in enumerate(choices, 1):
            print(number, choice)
        print(f"\nPick a number between 1 and {len(choices)}: ")

        user_choice = int(input())
        if 1 <= user_choice <= len(choices):
            return user_choice - 1


def make_character(name: str) -> dict:
    """
    Makes the character.

    :param name: must be a string
    :precondition: name must be a string
    :postcondition: returns a dictionary for character with name, location, level, brain power, max brain power values
    :return: dictionary for character with name, location, level, brain power, max brain power values
    """

    player_dictionary = {"Name": name,
                         "X-Coordinate": random.randint(0, 9),
                         "Y-Coordinate": random.randint(0, 9),
                         "Level": 1,
                         "Brain Power": 0,
                         "Level Tracker": [],
                         }
    return player_dictionary


def make_board(rows: int, columns: int, encounter_percentage: int) -> dict:
    """
    Creates the game board.

    :param rows: must be a positive integer
    :param columns: must be a positive integer
    :param encounter_percentage: must be a positive integer
    :precondition: parameters must follow conditions
    :postcondition: returns a dictionary with rows, column, and the encounter rate
    :return: a dictionary with rows, columns, and the encounter rate
    """
    grid = chain.from_iterable([[(x_coordinates, y_coordinates) for y_coordinates in range(columns)]
                                for x_coordinates in range(rows)])

    room_markers = [".  "] * int((rows * columns * (1 - (encounter_percentage / 100)))) + \
                   ["$  "] * int((rows * columns * (encounter_percentage / 100)))

    rooms = random.sample(room_markers, len(room_markers))
    game_board = {coordinates: room for coordinates, room in zip(grid, rooms)}

    return game_board


def describe_current_location(game_board: dict, character: dict) -> str:
    """
    Prints the description and location of character on a map.

    :param game_board: must be a dictionary
    :param character: must be a dictionary
    :precondition: must have two dictionaries that have location values
    :postcondition: a string print out of map and location of character and puzzles
    :returns a string print out of map and location of character represented by a "@" as well as puzzle locations
    """
    rows = list(max(game_board.keys()))[0] + 1
    game_board_copy = game_board.copy()
    game_board_copy[(character["X-Coordinate"],
                     character["Y-Coordinate"])] = "@  "
    game_board_characters = list(game_board_copy.values())

    game_board_sliced = [game_board_characters[digits:digits + rows]
                         for digits in range(0, len(game_board_characters), rows)]  # slice list row length
    game_board_newlines = [row + ["\n"]
                           for row in game_board_sliced]  # then add "\n" to list
    location_map = "".join(list(chain.from_iterable(game_board_newlines)))

    print(location_map)
    return location_map


def validate_move(move: int, player: dict, rows: int) -> tuple:
    """
    A Function that checks if player move is outside the boundary of the game.

    :param move: must be an integer of 1 or -1
    :param player: must contain the value from key "X-Coordinate" and "Y-Coordinate"
    :param rows:
    :precondition: rows must be equal to columns
    :postcondition: boolean value of True of False depending on user move
    :return: a tuple of consisting of: a boolean True of False depending on if user move is out of bounds
             and an integer value of the amount to move the characters x or y coordinate.
    """
    move_key_values = {"Up": -1, "Down": 1,
                       "Right": 1, "Left": -1, }
    return 0 <= (player["X-Coordinate"] + move_key_values[move] if (move == "Up" or move == "Down") else
                 player["Y-Coordinate"] + move_key_values[move]) <= rows - 1, move_key_values[move]


def move_character(character: dict, rows: int) -> dict:
    """
    Moves the character on the game board.

    :param character: must be a dictionary
    :param rows: must be a positive integer
    :precondition:
    :postcondition:
    :return: the character dictionary
    """
    while True:
        print("Which way do you want to go?")
        direction_choices = ("Up", "Down", "Right", "Left")
        character_direction = get_user_choice(direction_choices)
        state, move_value = validate_move(
            direction_choices[character_direction], character, rows)
        if state:
            if direction_choices[character_direction] == "Up":
                character["X-Coordinate"] += move_value
            elif direction_choices[character_direction] == "Down":
                character["X-Coordinate"] += move_value
            elif direction_choices[character_direction] == "Right":
                character["Y-Coordinate"] += move_value
            elif direction_choices[character_direction] == "Left":
                character["Y-Coordinate"] += move_value
        else:
            print("\nThat is not a valid move!\n")
            move_character(character, rows)

        return character


def check_for_challenge(board: list or tuple, character: dict) -> bool:
    """
    Checks for a challenge.

    :param board: must be a list containing the values from the character keys "X-Coordinate" and "Y-Coordinate"
    :param character: must be a dictionary with values from the keys "X-Coordinate" and "Y-Coordinate"
    :precondition: parameters must follow conditions
    :postcondition: returns True if the character moves to a "$ " on the game board
    :return: True if the character moves to a "$ " on the game board
    """
    if board[(character["X-Coordinate"], character["Y-Coordinate"])] == "$  ":
        print("\nThere is a puzzle here.")
        return True


def challenge_protocol(player: dict,
                       abc_puzzles: tuple or list,
                       cheat_mode: bool,
                       level_3: int, ) -> dict and bool:
    """
    Activates challenge protocol when check_for_challenge returns True

    :param player: must be a dictionary
    :param abc_puzzles: must be a tuple or list
    :param cheat_mode: must be a positive integer
    :param level_3: must be a positive integer
    :precondition: parameters must follow conditions
    :postcondition: returns the player dictionary and quit state
    :return: player and quit state
    """
    brain_power = player['Brain Power']
    puzzle_and_solution = random.sample(abc_puzzles, 1)
    puzzle = "".join(puzzle_and_solution[0][0])
    solution = puzzle_and_solution[0][1]
    quit_state = False

    print("\nWhat are the values of A, B and C?\n")
    print(puzzle, "\n")
    if cheat_mode:
        print("Solution:", solution, "\n")

    number_of_choices = 3
    answer_choices = ["  A = " + str(random.randint(0, 9)) + "   B = " + str(random.randint(0, 9)) + "   C = " + str(
        random.randint(0, 9))
                      for _ in range(number_of_choices)]
    solution_choice = " ".join(["  " + letter + " = " + str(digit)
                                for letter, digit in
                                zip(string.ascii_uppercase, "".join(solution.split())) if digit.isnumeric()])
    correct_answer = "".join(solution.split())

    answer_choices.append(solution_choice)
    random.shuffle(answer_choices)
    answer_choices.append("  Q = Quit")
    answers = answer_choices

    player_choice = get_user_choice(answers)
    player_choice_numerals = "".join(
        [char for char in answers[player_choice].split() if char.isnumeric()])

    if player_choice == "  Q = Quit":
        quit_state = True
    else:
        if player_choice_numerals == correct_answer:
            print("\nCongratulations, you solved the puzzle!")
            if brain_power <= level_3:
                player["Brain Power"] += 10
                print("\n")
            else:
                player["Brain Power"] += 1000
                print("\n")
        else:
            print("That is not the correct answer!")
            if brain_power <= level_3:
                player["Brain Power"] -= 10
                print("\n")
            else:
                player["Brain Power"] -= 1000
                print("\n")

    return player, quit_state


def character_has_leveled(player: dict,
                          encounter_percentage: int,
                          level_1: int,
                          level_2: int,
                          level_3: int,
                          ) -> dict and bool:
    """
    Increases the character's stats.

    :param player: must be a dictionary
    :param encounter_percentage: must be a positive integer
    :param level_1: must be a positive integer
    :param level_2: must be a positive integer
    :param level_3: must be a positive integer
    :precondition: parameters must follow conditions
    :postcondition: returns player, boss_state, and dead_state
    :return: player, boss_state, and dead_state
    """

    boss_level = 1000
    name = player["Name"]
    brain_power = player['Brain Power']
    boss_state = False
    dead_state = False

    if level_2 > player['Brain Power'] > level_1:
        encounter_percentage += 20
        if len(player['Level Tracker']) == 0:
            print()
            print("""\
                                                You have passed level 1!
              ..............................................................................................   
              ,................................................................................................ 
              ,................................................................................................ 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,@@@%,,,,,,,,,,,@@@@,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,@@@%,,,,,,,,,,,@@@@,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,*************,,&&@@@(,,,,,,,@@@@&&,,*************,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,,*@@@@@*,,,@@@@@@,,,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@#,,,,,,,,,,,,,,/@@@*,,,@@@@,,,,,(@@@*,,,,,,,,,,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@#,,,,,,,,,,,,,,/@@@@@,,,,@@,,,,,(@@@*,,,,,,,,,,/@@@/,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@@@@@@@@@,,@@@@@@@@@@@@@,,,,,,,#@@@@@,,,,,,,,,(@@@@@@@@@@@@@,/@@@@@@@@@@@,,,,,,,,,. 
              ,,,,,,,,,,,(@@@@@@@@@@@,,@@@@@@@@@@@@@,,,,,,,,,&@@@,,,,,,,,,(@@@@@@@@@@@@@,/@@@@@@@@@@@,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,(//////*,,,,,,,,,,,,,////////////////////////////////,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,,(((((((((((((((((((((((((((((((((/,,,,,,,,,,,,,,,,,,,,, 
              ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,,(((((((((((((((((((((((((((((((((((*,,,,,,,,,,,,,,,,,,, 
              ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,*(((((((,,,,,,,,,,,,,,,,,,,,,(((((((((*,,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,*(((((((,,,,,,,,,,,,,,,,,,,,,,,(((((((*,,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,,,,#((((((/,,,,,,,,,,,,*#((((((*,,,,,,,,,,,,,,,,,,,,,,(((((((*,,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,,,,#######/,,,,,,,,,,,,*#######*,,,,,,,,,,,,,,,,,,,,,,#######**,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,*,*#######(,,,,,,,,,,,,*#######**,**,,,,,,,,,,,,,**,#######/*,,,,,,,,,,,,,,,,,, 
              *********************#######(*************#######****########################/*****************,, 
              *********************%%#####(*************#####%#****#######%%%%%%%%%%%%%#,,********************, 
              *********************%%%%%%#(*************%%%%%%%****%%%%%%%(***********,***********************, 
              *********************%%%%%%%%%/,,*****,*%%%%%%%%%****%%%%%%%(***********************************, 
              ***********************%%%%%%%%%%%%%%%%%%%%%%%%******%%%%%%%(***********************************, 
              *************************%%%%%%%%%%%%%%%%%%%%(*******%%%%%%%(***********************************, 
              **************************/%%%%%%%%%%%%%%%%#*********%%%%%%%(***********************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
                *********************************************************************************************   
                    """)
            player['Level Tracker'].append(1)

    elif level_3 > player['Brain Power'] >= level_2:
        player['Level Tracker'].append(2)
        encounter_percentage += 20
        if player['Level Tracker'][-1] != player['Level Tracker'][-2]:
            print("""\
                                                You have passed level 2!
              ..............................................................................................   
              ,................................................................................................ 
              ,................................................................................................ 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,@@@%,,,,,,,,,,,@@@@,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,@@@%,,,,,,,,,,,@@@@,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,*************,,&&@@@(,,,,,,,@@@@&&,,*************,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,,*@@@@@*,,,@@@@@@,,,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@#,,,,,,,,,,,,,,/@@@*,,,@@@@,,,,,(@@@*,,,,,,,,,,/@@@*,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@*,,,,,,,,,@@@#,,,,,,,,,,,,,,/@@@@@,,,,@@,,,,,(@@@*,,,,,,,,,,/@@@/,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,(@@@@@@@@@@@,,@@@@@@@@@@@@@,,,,,,,#@@@@@,,,,,,,,,(@@@@@@@@@@@@@,/@@@@@@@@@@@,,,,,,,,,. 
              ,,,,,,,,,,,(@@@@@@@@@@@,,@@@@@@@@@@@@@,,,,,,,,,&@@@,,,,,,,,,(@@@@@@@@@@@@@,/@@@@@@@@@@@,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,(//////*,,,,,,,,,,,,,////////////////////////////////,,,,,,,,,,,,,,,,,,,,,,. 
              ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,,(((((((((((((((((((((((((((((((((/,,,,,,,,,,,,,,,,,,,,, 
              ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,,(((((((((((((((((((((((((((((((((((*,,,,,,,,,,,,,,,,,,, 
              ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,*(((((((,,,,,,,,,,,,,,,,,,,,,(((((((((*,,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,*(((((((,,,,,,,,,,,,,,,,,,,,,,,(((((((*,,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,,,,#((((((/,,,,,,,,,,,,*#((((((*,,,,,,,,,,,,,,,,,,,,,,(((((((*,,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,,,,#######/,,,,,,,,,,,,*#######*,,,,,,,,,,,,,,,,,,,,,,#######**,,,,,,,,,,,,,,,, 
              *,,,,,,,,,,,,,,,,,*,*#######(,,,,,,,,,,,,*#######**,**,,,,,,,,,,,,,**,#######/*,,,,,,,,,,,,,,,,,, 
              *********************#######(*************#######****########################/*****************,, 
              *********************%%#####(*************#####%#****#######%%%%%%%%%%%%%#,,********************, 
              *********************%%%%%%#(*************%%%%%%%****%%%%%%%(***********,***********************, 
              *********************%%%%%%%%%/,,*****,*%%%%%%%%%****%%%%%%%(***********************************, 
              ***********************%%%%%%%%%%%%%%%%%%%%%%%%******%%%%%%%(***********************************, 
              *************************%%%%%%%%%%%%%%%%%%%%(*******%%%%%%%(***********************************, 
              **************************/%%%%%%%%%%%%%%%%#*********%%%%%%%(***********************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
              ************************************************************************************************, 
                *********************************************************************************************   
                    """)
    elif boss_level > player['Brain Power'] >= level_3:
        player['Level Tracker'].append(3)
        if player['Level Tracker'][-1] != player['Level Tracker'][-2]:
            print("""\
                                    You have passed level 3!
      ..............................................................................................   
      ,................................................................................................ 
      ,................................................................................................ 
      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,@@@%,,,,,,,,,,,@@@@,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,@@@%,,,,,,,,,,,@@@@,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,(@@@*,,,,,,,,,*************,,&&@@@(,,,,,,,@@@@&&,,*************,/@@@*,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,(@@@*,,,,,,,,,@@@@@@@@@@@@@,,,*@@@@@*,,,@@@@@@,,,(@@@@@@@@@@@@@,/@@@*,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,(@@@*,,,,,,,,,@@@#,,,,,,,,,,,,,,/@@@*,,,@@@@,,,,,(@@@*,,,,,,,,,,/@@@*,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,(@@@*,,,,,,,,,@@@#,,,,,,,,,,,,,,/@@@@@,,,,@@,,,,,(@@@*,,,,,,,,,,/@@@/,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,(@@@@@@@@@@@,,@@@@@@@@@@@@@,,,,,,,#@@@@@,,,,,,,,,(@@@@@@@@@@@@@,/@@@@@@@@@@@,,,,,,,,,. 
      ,,,,,,,,,,,(@@@@@@@@@@@,,@@@@@@@@@@@@@,,,,,,,,,&@@@,,,,,,,,,(@@@@@@@@@@@@@,/@@@@@@@@@@@,,,,,,,,,. 
      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,,,,,,,,,,,(//////*,,,,,,,,,,,,,////////////////////////////////,,,,,,,,,,,,,,,,,,,,,,. 
      ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,,(((((((((((((((((((((((((((((((((/,,,,,,,,,,,,,,,,,,,,, 
      ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,,(((((((((((((((((((((((((((((((((((*,,,,,,,,,,,,,,,,,,, 
      ,,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,*(((((((,,,,,,,,,,,,,,,,,,,,,(((((((((*,,,,,,,,,,,,,,,,, 
      *,,,,,,,,,,,,,,,,,,,,(((((((/,,,,,,,,,,,,*(((((((,,,,,,,,,,,,,,,,,,,,,,,(((((((*,,,,,,,,,,,,,,,,, 
      *,,,,,,,,,,,,,,,,,,,,#((((((/,,,,,,,,,,,,*#((((((*,,,,,,,,,,,,,,,,,,,,,,(((((((*,,,,,,,,,,,,,,,,, 
      *,,,,,,,,,,,,,,,,,,,,#######/,,,,,,,,,,,,*#######*,,,,,,,,,,,,,,,,,,,,,,#######**,,,,,,,,,,,,,,,, 
      *,,,,,,,,,,,,,,,,,*,*#######(,,,,,,,,,,,,*#######**,**,,,,,,,,,,,,,**,#######/*,,,,,,,,,,,,,,,,,, 
      *********************#######(*************#######****########################/*****************,, 
      *********************%%#####(*************#####%#****#######%%%%%%%%%%%%%#,,********************, 
      *********************%%%%%%#(*************%%%%%%%****%%%%%%%(***********,***********************, 
      *********************%%%%%%%%%/,,*****,*%%%%%%%%%****%%%%%%%(***********************************, 
      ***********************%%%%%%%%%%%%%%%%%%%%%%%%******%%%%%%%(***********************************, 
      *************************%%%%%%%%%%%%%%%%%%%%(*******%%%%%%%(***********************************, 
      **************************/%%%%%%%%%%%%%%%%#*********%%%%%%%(***********************************, 
      ************************************************************************************************, 
      ************************************************************************************************, 
      ************************************************************************************************, 
      ************************************************************************************************, 
      ************************************************************************************************, 
      ************************************************************************************************, 
        *********************************************************************************************   
            """)
            print("\nTime to solve the final puzzle:\n")
    elif player['Brain Power'] > boss_level:
        print("YOU FINISHED ALL PUZZLES!")
        print(f"{name} has achieved the level of PUZZLE MASTER!")
        print("""\
                       *    *
           *         '       *       .  *   '     .           * *
                                                                       '
               *                *'          *          *        '
           .           *               |               /
                       '.         |    |      '       |   '     *
                         \*        \   \             /
               '          \     '* |    |  *        |*                *  *
                    *      `.       \   |     *     /    *      '
          .                  \      |   \          /               *
             *'  *     '      \      \   '.       |
                -._            `                  /         *
          ' '      ``._   *                           '          .      '
           *           *\*          * .   .      *
        *  '        *    `-._                       .         _..:='        *
                     .  '      *       *    *   .       _.:--'
                  *           .     .     *         .-'         *
           .               '             . '   *           *         .
          *       ___.-=--..-._     *                '               '
                                          *       *
                        *        _.'  .'       `.        '  *             *
             *              *_.-'   .'            `.               *
                           .'                       `._             *  '
           '       '                        .       .  `.     .
               .                      *                  `
                       *        '             '                          .
             .                          *        .           *  *
                     *        .                                    '
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⠇⠀⠀⠀⠀⠀
        ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⣀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠀⠀⠀⠀⠀⠀
        ⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣁⣼⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠀⣠⣶⣿⣷⣆⠀⠀⠀⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀
        ⠀⢰⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣧⣾⣿⣿⣿⣿⡟⠀⠀⠀⠀⣼⣿⡟⠀⠀⣠⠀⠀⠀⠀
        ⢀⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⠟⣻⣿⣿⣿⣷⣤⠀⠀⠀⣿⣿⣃⣤⣾⣿⣀⣤⣤⡀
        ⢸⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡟⠀⢸⣿⡇⠀⠀⠀⢀⣀⣀⡀⠀⠸⣿⣿⠁⣰⣿⣿⡿⠋⢹⣿⡇⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⢸⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣦⣄⠀⣿⣿⡇⠀⣼⣿⡇⠀⢀⣴⣿⣿⣿⣿⣀⣴⣿⣿⠀⠛⠻⠿⠁⠀⢸⣿⣿⣿⣿⣿⡿⠋⢻⣿⣿⠋⠉⠉⠁
        ⠘⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡇⠀⣿⣿⣧⠀⣼⣿⣿⢿⣿⣿⣿⡿⢹⣿⠀⠀⢀⣤⣶⣶⣿⣿⡟⠁⢸⣿⡇⠀⠸⣿⣏⠀⠀⠀⠀
        ⠀⢻⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⡏⠀⠘⣿⣿⣿⣿⣿⡇⠀⢻⣿⣿⣷⣿⣿⠃⠀⢿⣿⣿⠁⣼⣿⠀⣰⣿⡿⠛⢻⣿⣿⣿⠀⢸⣿⡇⠀⠀⠹⣿⣦⡀⠀⠀
        ⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢹⣿⣿⣿⣿⠃⠀⠸⣿⣿⣿⣿⣿⠀⠀⢸⣿⡏⢠⣿⣿⡆⣿⣿⠀⠀⣼⣿⣿⣿⣦⣿⣿⠉⣷⣦⣄⠹⣿⣿⣦⠀
        ⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⡿⠟⢿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠿⠆⠀⠀⠹⣿⣿⣿⣿⣆⣠⣿⣿⠃⣾⣿⣿⡇⢻⣿⣷⣿⣿⠟⢿⣿⣿⣿⣿⡇⠸⣿⣿⠀⣿⣿⣿⡇
        ⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⢸⣿⣿⣿⣿⣤⣴⣿⣿⣿⡟⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠻⠀⠉⠉⠉⠀⠀⠀⠉⠛⣿⣿⣷⠀⢻⣿⣿⣿⣿⣿⠃
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣠⣆⠀⠀⠀⠙⠛⠛⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣧⡀⠉⠛⠛⠋⠁⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠛⠉⠀⠀⢀⣴⣿⣿⡄⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣶⣤⣄⣀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣄⠀⠀⢠⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣷⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀

                                """)
        boss_state = True
    elif player['Brain Power'] < 0:
        print()
        print(f"{name} has lost all brain power trying to solve final puzzle and died")
        print()
        dead_state = True

    print(f"{name} now has {brain_power} brain power.")

    return player, boss_state, dead_state


def game():
    """
    Initializes the game.
    """
    rows = 10
    columns = 10
    encounter_percentage = 20
    achieved_goal = False
    cheat_mode = True  # set to True if you want to see solution while playing.
    print("""\
        .d8888b.  888     888 8888888b.   .d88888b.  888    d8P  888     888           
        d88P  Y88b 888     888 888  "Y88b d88P" "Y88b 888   d8P   888     888           
        Y88b.      888     888 888    888 888     888 888  d8P    888     888           
         "Y888b.   888     888 888    888 888     888 888d88K     888     888           
            "Y88b. 888     888 888    888 888     888 8888888b    888     888           
              "888 888     888 888    888 888     888 888  Y88b   888     888           
        Y88b  d88P Y88b. .d88P 888  .d88P Y88b. .d88P 888   Y88b  Y88b. .d88P           
         "Y8888P"   "Y88888P"  8888888P"   "Y88888P"  888    Y88b  "Y88888P"            
                                                                                        
                                                                                        
                                                                                        
        888             d8888 888b    888 8888888b.                                     
        888            d88888 8888b   888 888  "Y88b                                    
        888           d88P888 88888b  888 888    888                                    
        888          d88P 888 888Y88b 888 888    888                                    
        888         d88P  888 888 Y88b888 888    888                                    
        888        d88P   888 888  Y88888 888    888                                    
        888       d8888888888 888   Y8888 888  .d88P                                    
        88888888 d88P     888 888    Y888 8888888P
 
        """




)
    player_name = input("Welcome to Sudoku Land, what is your name? ")
    puzzle_player = make_character(player_name)
    game_board = make_board(rows, columns, encounter_percentage)
    quit_state = False
    level_1 = 11  # change these for higher/lower threshold for passing levels
    level_2 = 33
    level_3 = 66

    while not achieved_goal:
        describe_current_location(game_board, puzzle_player)
        move_character(puzzle_player, rows)
        describe_current_location(game_board, puzzle_player)
        challenge = check_for_challenge(game_board, puzzle_player)
        if challenge:
            puzzle_player, quit_state = challenge_protocol(
                puzzle_player, puzzles, cheat_mode, level_3)
        if quit_state is True:
            print("Goodbye!")
            break

        character, boss_state, dead_state = character_has_leveled(
            puzzle_player, encounter_percentage, level_1, level_2, level_3)

        if boss_state or dead_state:
            achieved_goal = True


def main():
    """
    Runs the game.
    """
    game()


if __name__ == '__main__':
    main()
