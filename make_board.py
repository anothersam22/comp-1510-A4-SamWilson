import random
from itertools import chain


row_count = 10
column_count = 10
encounter_percent = 20  # percentage of encounters in grid represented as an integer


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


def main():
    """
    Drive the program
    """


if __name__ == '__main__':
    main()
