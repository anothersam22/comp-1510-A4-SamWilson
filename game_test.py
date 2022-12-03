import csv
import random
import string
from itertools import chain

rows = 10
columns = 10
encounter_percentage = 20
achieved_goal = False


# run this at beginning of game once to get puzzle data into a list
with open("puzzle_set_1.csv", newline='') as file:
    reader = csv.reader(file)
    puzzles = list(reader)


def get_user_choice(choices):
    while True:
        # result = ""
        for number, choice in enumerate(choices, 1):
            print(number, choice)
        print(f"Pick a number between 1 and {len(choices)}: ")

        # user_pick = input()
        # if user_pick.isnumeric():
        #     user_choice = int(input())
        #     if 1 <= user_choice <= len(choices):
        #         result = user_choice - 1
        #     else:
        #         print("That's not a valid choice")
        # else:
        #     print("Must enter a number!")

        # return result

        user_choice = int(input())
        if 1 <= user_choice <= len(choices):
            return user_choice - 1
        else:
            print("That's not a valid choice")


def make_character(name: str) -> dict:
    """
    Makes the character.

    :param name:
    :return: dictionary for character with name, location, level, brain power, max brain power values.
    """

    player_dictionary = {"Name": name,
                         "X-Coordinate": random.randint(0, 9),
                         "Y-Coordinate": random.randint(0, 9),
                         "Level": 1,
                         "Brain Power": 0,
                         }
    return player_dictionary


def make_board(rows: int, columns: int, encounter_percentage: int) -> dict:
    """
    A function to create game board and printable game map


    """
    grid = chain.from_iterable([[(x_coordinates, y_coordinates) for y_coordinates in range(columns)]
                                for x_coordinates in range(rows)])

    room_markers = [".  "] * int((rows*columns*(1-(encounter_percentage/100)))) +\
                   ["$  "] * int((rows*columns*(encounter_percentage/100)))

    rooms = random.sample(room_markers, len(room_markers))
    game_board = {coordinates: room for coordinates, room in zip(grid, rooms)}

    return game_board


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


def move_character(character):
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
            print("That is not a valid move")
            move_character(character)

        print(character)
        # return direction_choices[character_direction]

        return character


def check_for_challenge(board, character):
    if board[(character["X-Coordinate"], character["Y-Coordinate"])] == "$  ":
        print()
        print("There is a puzzle here.")
        print()
        return True


def challenge_protocol(player, puzzles, cheat_mode):
    puzzle_and_solution = random.sample(puzzles, 1)
    puzzle = "".join(puzzle_and_solution[0][0])
    solution = puzzle_and_solution[0][1]
    quit_state = False
    print()
    print("What are the values of A, B and C?")
    print()
    print(puzzle)
    print()
    if cheat_mode == True:
        print("Solution:", solution)
    print()

    number_of_choices = 3
    answer_choices = ["  A = "+str(random.randint(0, 9))+"   B = "+str(random.randint(0, 9))+"   C = "+str(random.randint(0, 9))
                      for _ in range(number_of_choices)]
    solution_choice = " ".join(["  "+letter+" = "+str(digit)
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
            print()
            print("Congratulations, you solved the puzzle!")
            print()
            if player['Level'] <= 3:
                player["Brain Power"] += 10
                print(player)
                print()
                print()
            else:
                player["Brain Power"] += 1000
                print(player)
                print()
                print()
        else:
            print()
            print("That is not the correct answer.")
            print()
            if player['Level'] <= 3:
                player["Brain Power"] -= 10
                print(player)
                print()
                print()
            else:
                player["Brain Power"] -= 1000
                print(player)
                print()
                print()

    return player, quit_state


def character_has_leveled(player, encounter_percentage):
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
        print("YOU FISNISHED ALL PUZZLES")
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


cheat_mode = False
player_name = input("Welcome to game land, what is your name? ")
character = make_character(player_name)
board = make_board(rows, columns, encounter_percentage)
quit_state = False

while not achieved_goal:
    describe_current_location(board, character)
    move_character(character)
    describe_current_location(board, character)
    challenge = check_for_challenge(board, character)
    if challenge:
        character, quit_state = challenge_protocol(
            character, puzzles, cheat_mode)

    if quit_state is True:
        print("Goodbye!")
        break

    character, boss_state, dead_state = character_has_leveled(
        character, encounter_percentage)

    if boss_state or dead_state == True:
        achieved_goal = True

# print(answers)

# print(type(solution))
# print(solution)
# print(correct_answer)
# #return puzzle, solution
