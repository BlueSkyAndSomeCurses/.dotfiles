#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from random import choice
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
            elif tmp_chr_field != tmp_chr_figure:
                return False
            if tmp_chr_field == tmp_chr_figure:
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
    assert len(distances) != 0, put_coord
    return min(distances)


def parse_field(player: int, field_info: tuple):
    player = "X" if player else "O"
    field = []
    possible_moves = []
    enemy_cords = []
    distances = []
    for i in range(field_info[0] + 1):
        line = input()
        field.append(line.split(" ")[1])

    field = field[1:]
    figure = parse_figure(player)

    for i in range(field_info[0] - figure[0] + 1):
        for j in range(field_info[1] - figure[1] + 1):
            if check_pos(field, figure, player, (i, j)):
                possible_moves.append((i, j))
            elif field[i][j] != "." and field[i][j] != player:
                enemy_cords.append((i, j))

    piece_cords = get_piece_cord(figure)
    debug(figure)
    debug(possible_moves)
    debug(piece_cords)
    debug(enemy_cords)

    for possibility in possible_moves:
        distances.append(
            (possibility, count_dist(possibility, piece_cords, enemy_cords))
        )

    distances.sort(key=lambda x: x[1])

    assert len(distances) != 0
    debug(f"pre-release move {distances[0][0]}")
    return distances[0][0]


def parse_figure(player: str):
    size_ = input().split()
    height = int(size_[1])
    figure = []
    for _ in range(height):
        figure.append(input().replace("*", player))

    return int(height), int(size_[2][:-1]), figure


def step(player: int):
    move = None
    field_info = parse_field_info()
    move = parse_field(player, field_info)
    return move


def play(player: int):
    # --TODO remove counter
    while True:
        move = step(player)
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
