#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from logging import DEBUG, debug, getLogger

# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would int ercept it
# You can hovever do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    l = input()
    l = l.split()
    return (int(l[-2]), int(l[-1][:-1]))


def parse_field(field_size: tuple) -> list:
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowecase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player int: Represents whether we're the first or second player
    """
    field = []
    info = input()
    for _ in range(field_size[0]):
        info = input()
        field.append(info.split()[-1])
    return field


def possible_moves(field: list, piece: list, player: int) -> list:
    """
    Function that returns coordinates of all possible moves
    """
    lst_of_coordinates = []
    counter = 0
    char = "O" if player == 1 else "X"
    opponent_char = "O" if player == 2 else "X"
    for n in range(len(field) - len(piece) + 1):
        for m in range(len(field[0]) - len(piece[0]) + 1):
            coordinates = (n, m)
            counter = 0
            smth = False
            for i, item in enumerate(piece):
                for k in range(len(piece[0])):
                    if item[k] == char and field[n + i][m + k] == char:
                        counter += 1
                    elif field[n + i][m + k] == opponent_char:
                        smth = True
            if counter == 1 and smth is False:
                lst_of_coordinates.append(coordinates)
    return lst_of_coordinates


def opponent_coordinates(field: list, player: int) -> list:
    """
    Function that returns all current coordinates of opponent
    """
    opponent_char = "X" if player == 1 else "O"
    coordinates = []

    for i, _ in enumerate(field):
        for j, _ in enumerate(field[0]):
            if field[i][j] == opponent_char:
                coordinates.append((i, j))

    return coordinates


def closest_move(oppent_coords: list, possible_moves_: list, piece: list) -> tuple:
    """
    Function that finds the closest possible move to opponent
    """
    min_distance = 1000000000000
    assert possible_moves_[0], "There are no possible moves"
    selected_move = possible_moves_[0], ""

    for move in possible_moves_:
        for y, line in enumerate(piece):
            
        for opponent_coord in oppent_coords:
            distance = (move[0] - opponent_coord[0]) ** 2 + (
                move[1] - opponent_coord[1]
            ) ** 2
            if distance < min_distance:
                min_distance = distance
                selected_move = move

    return selected_move


def parse_figure(player: int):
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    info = input()
    info = info[:-1].split()[1:]
    info = [int(i) for i in info]
    piece = []
    for _ in range(info[0]):
        info = input()
        info = info.replace("*", "O" if player == 1 else "X")
        piece.append(info)
    return piece


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    move = None

    field_info = parse_field_info()
    field = parse_field(field_info)
    piece = parse_figure(player)
    coor_of_moves = possible_moves(field, piece, player)
    coords_opponent = opponent_coordinates(field, player)
    move = closest_move(coords_opponent, coor_of_moves)

    return move


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    """
    Function that starts a program
    """
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
