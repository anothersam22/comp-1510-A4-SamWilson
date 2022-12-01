import random
from itertools import chain


row_count = 10
column_count = 10
encounter_percent = 20  # percentage of encounters in grid represented as an integer


def make_board(rows: int, columns: int, encounter_percentage: int) -> dict:
    """
    A function to create game board and printable game map


    """
    grid = [[(x_coordinates, y_coordinates) for y_coordinates in range(columns)]
            for x_coordinates in range(rows)]  # makes x,y coords for grid
    grid_flattened = chain.from_iterable(grid)
    empty_space = [".  "] * int((rows * columns * (1 - (encounter_percentage / 100))))
    encounters = ["$  "] * int((rows * columns * (encounter_percentage / 100)))
    populated_grid = random.sample(empty_space + encounters, len(empty_space + encounters))
    game_board = {coordinates: location_name for coordinates, location_name in zip(grid_flattened, populated_grid)}

    return game_board


def main():
    """
    Drive the program
    """


if __name__ == '__main__':
    main()
