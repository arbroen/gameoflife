# -*- coding: utf8 -*-
from typing import Generator, Tuple

from numpy import ndarray, ndenumerate


def neighbour_counter(board: ndarray) -> \
        Generator[Tuple[int, int, int], None, None]:
    """
    Iterate over the board, yielding all cells connected to the current cell
    (e.g. index) of the iteration loop. It returns subsets in a 3x3 shape at
    most, 2x2 at minimum (e.g. the corners).
    :param board:
    :return:
    """
    if len(board.shape) != 2:
        raise AttributeError(
            "It is only possible to iterate over two-dimensional boards.")

    row_count, column_count = board.shape

    for (row, column), current_cell in ndenumerate(board):
        top_row, bottom_row = \
            max(0, row - 1), min(row_count, row + 2)
        left_column, right_column = \
            max(0, column - 1), min(column_count, column + 2)

        subset = board[top_row: bottom_row, left_column: right_column]

        if current_cell is 1:
            yield row, column, subset.sum() - 1
        else:
            yield row, column, subset.sum()
