#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Destroyer Vityala BOT.
Domain Expansion Malevolent Shrine
Ryoiki Tenkai, Fukuma Mizushi
"""

from random import choice
from copy import deepcopy
from logging import DEBUG, debug, getLogger


getLogger().setLevel(DEBUG)


def parse_field_info():
    descr = input().split()
    return int(descr[1]), int(descr[2][:-1])


def check_pos(field, figure, player, position):
    counter = -1
    for i in range(figure[0]):
        for j in range(figure[1]):
            tmp_chr_field = field[position[0] + i][position[1] + j]
            tmp_chr_figure = figure[2][i][j]
            if tmp_chr_field == "." or tmp_chr_figure == ".":
                continue
            elif tmp_chr_field.upper() != tmp_chr_figure.upper():
                return False
            if tmp_chr_field.upper() == tmp_chr_figure.upper():
                counter += 1

    return True if counter == 0 else False


def get_piece_cord(figure):
    coordinates = []
    for i in range(figure[0]):
        for j in range(figure[1]):
            if figure[2][i][j] != ".":
                coordinates.append((i, j))

    return coordinates


def count_dist(put_coord, figure_coords, enemy_coords):
    distances = []
    for p_row, p_col in figure_coords:
        for e_row, e_col in enemy_coords:
            distances.append(
                (put_coord[0] + p_row - e_row) ** 2
                + (put_coord[1] + p_col - e_col) ** 2
            )
    assert len(distances) != 0
    return min(distances)


def check_enemy(i, j, field, field_info, player):
    if field[i][j] != "." and field[i][j].upper() != player and field[i][j].islower():
        return True
    return False


def parse_field(player: int, field_info: tuple, previous_field):
    player = "X" if player else "O"
    field = []
    possible_moves = []
    enemy_cords = []
    distances = []
    for i in range(field_info[0] + 1):
        line = input()
        # debug(line)
        field.append(line.split(" ")[1])

    field = field[1:]
    figure = parse_figure(player)

    for i in range(field_info[0] - figure[0] + 1):
        for j in range(field_info[1] - figure[1] + 1):
            if check_pos(field, figure, player, (i, j)):
                possible_moves.append((i, j))
            # if check_enemy(i, j, field, field_info, player):
            # debug("LOL")
            # enemy_cords.append((i, j))
            if (
                len(previous_field) != 0
                and field[i][j] != "."
                and previous_field[i][j] == "."
                and field[i][j] != player
            ):
                debug("YEAH BITCHESSS")
                enemy_cords.append((i, j))

    if len(enemy_cords) == 0:
        for i in range(field_info[0] - figure[0] + 1):
            for j in range(field_info[1] - figure[1] + 1):
                if field[i][j] != "." and field[i][j].upper() != player:
                    enemy_cords.append((i, j))

    piece_cords = get_piece_cord(figure)

    for possibility in possible_moves:
        distances.append(
            (possibility, count_dist(possibility, piece_cords, enemy_cords))
        )

    distances.sort(key=lambda x: x[1])

    assert len(distances) != 0
    return distances[0][0]


def parse_figure(player: str):
    size_ = input().split()
    height = int(size_[1])
    figure = []
    for _ in range(height):
        figure.append(input().replace("*", player))

    return int(height), int(size_[2][:-1]), figure


def step(player: int, previous_field):
    move = None
    field_info = parse_field_info()
    move = parse_field(player, field_info, previous_field)
    return move


def play(player: int):
    previous_field = []
    while True:
        move = step(player, previous_field)
        print(*move)


def parse_info_about_player():
    i = input()
    return 0 if "p1 :" in i else 1


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
