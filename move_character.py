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


def main():
    """
    Drive the program
    """
    pass


if __name__ == '__main__':
    main()
