# -*- coding: utf8 -*-
from numpy import ndarray

from .iterator import neighbour_counter
from shine_on_life.boards import CellTypes


def _cell_lives(count: int) -> bool:
    """
    These cells have either 2 or 3 neighbours that are also alive,
    and hence, they will stay alive for another generation.
    :return:
    """
    return count == (2 | 3)


def _cell_dies(count: int) -> bool:
    """
    Two conditions apply for dying cells.
    - Overcrowding. Four or more living neighbours.
    - Underpopulation. Two or less neighbours are still alive.
    :return:
    """
    return count <= 2 or count >= 4


def _cell_spawns(count: int) -> bool:
    """
    If a cell has exactly three living neighbours, this dead cell will
    sprout new life.
    :return:
    """
    return count == 3


def board_mutator(board: ndarray):
    """
    Applies the various mutations to the entire board.
    :param board:
    :return:
    """
    _board_copy = board.copy()

    for row, col, neighbour_count in neighbour_counter(board=board):
        if _cell_dies(count=neighbour_count):
            _board_copy[row, col] = CellTypes.DEAD
        elif _cell_lives(count=neighbour_count):
            _board_copy[row, col] = CellTypes.ALIVE
        elif _cell_spawns(count=neighbour_count):
            _board_copy[row, col] = CellTypes.SPAWNED
        else:
            raise AssertionError(
                "A cell must comply to one of the three cases.")

    return _board_copy
