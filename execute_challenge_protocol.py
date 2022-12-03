import random
import string


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
    if cheat_mode:
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


def main():
    """
    Drive the program
    """

    pass


if __name__ == '__main__':
    main()

