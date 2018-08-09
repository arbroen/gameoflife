# -*- coding: utf8 -*-
from numpy import ndarray, ndenumerate, count_nonzero, zeros, int8

from shine_on_life.world import CellTypes


def cell_lives(cycle: CellTypes, count: int) -> bool:
    """
    These cells have either 2 or 3 neighbours that are also alive,
    and hence, they will stay alive for another generation.
    :return:
    """
    return cycle is not CellTypes.DEAD and count in [2, 3]


def cell_spawns(cycle: CellTypes, count: int) -> bool:
    """
    If a cell has exactly three living neighbours, this dead cell will
    sprout new life.
    :return:
    """
    return cycle is CellTypes.DEAD and count == 3


def neighbour_count(cell_index: int, world: ndarray) -> int:
    """
    Counts the number of cells neighbouring the index that are alive.
    """
    row, col = cell_index
    row_count, column_count = world.shape

    top_row, bottom_row = max(0, row - 1), min(row_count, row + 2)
    left_column, right_column = max(0, col - 1), min(column_count, col + 2)

    subset = world[top_row: bottom_row, left_column: right_column]

    if world[cell_index] > 0:
        return max(count_nonzero(subset) - 1, 0)

    return count_nonzero(subset)


def world_mutator(world: ndarray):
    """
    Applies the various mutations to the entire world of cells.
    :param world:
    :return:
    """
    _new_world = zeros(shape=world.shape, dtype=int8)

    for index, cell_value in ndenumerate(world):
        next_cycle = CellTypes.DEAD
        previous_cycle = CellTypes(cell_value)
        count = neighbour_count(cell_index=index, world=world)

        if cell_lives(cycle=previous_cycle, count=count):
            next_cycle = CellTypes.ALIVE
        elif cell_spawns(cycle=previous_cycle, count=count):
            next_cycle = CellTypes.SPAWNED

        _new_world[index] = next_cycle

    return _new_world
