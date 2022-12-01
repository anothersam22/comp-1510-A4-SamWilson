import random
from itertools import chain


row_count = 10
column_count = 10
encounter_percentage = 20  # percentage of encounters in grid represented as an integer
level = 1


def make_board(rows: int, columns: int, encounter_pct: int) -> dict:
    """
    A function that creates the game board

    :param rows: must be an int
    :param columns: must be an int
    :param encounter_pct: must be an int
    :return: the game board
    """
    grid = [[(x_coordinates, y_coordinates) for y_coordinates in range(columns)]
            for x_coordinates in range(rows)]
    grid_flattened = chain.from_iterable(grid)
    empty_space = ["Empty Space"] * \
        int((rows * columns * (1 - (encounter_pct / 100))))
    encounters = ["Encounter"] * int((rows * columns * (encounter_pct / 100)))
    populated_grid = random.sample(
        empty_space + encounters, len(empty_space + encounters))
    return {coordinates: location_name for coordinates,
            location_name in zip(grid_flattened, populated_grid)}


def main():
    """
    Drive the program
    """
    pass

if __name__ == '__main__':
    main()
