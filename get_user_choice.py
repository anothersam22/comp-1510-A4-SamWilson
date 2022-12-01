"""
Wilson & Sam
A01266055
"""


def get_user_choice(choices):
    """
    Asks the player for their choices and uses their choice.

    :param choices: must be an enumerated string
    :return: an action for the character
    """
    while True:
        print("What would you like to do?")
        for number, choice in enumerate(choices, 1):
            print(number, choice)
        print(f"Pick a number between 1 and {len(choices)}: ")
        user_choice = int(input())
        if 1 <= user_choice <= len(choices):
            return user_choice - 1
        else:
            print("That's not a valid choice")


def main():
    directions = ("North", "East", "South", "West")
    character_direction = get_user_choice(directions)
    print(f"The character has chosen to go {directions[character_direction]}")
    combat_choices = ("Try to negotiate", "Run for our lives", "Fight to the death!")
    character_combat = get_user_choice(combat_choices)


if __name__ == "__main__":
    main()
