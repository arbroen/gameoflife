# -*- coding: utf8 -*-
from numpy import ndarray, ndenumerate


def iterate_3x3_shapes(board: ndarray):
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

    for (row, column), _ in ndenumerate(board):
        top_row, bottom_row = \
            max(0, row - 1), min(row_count, row + 2)
        left_column, right_column = \
            max(0, column - 1), min(column_count, column + 2)

        yield board[top_row: bottom_row, left_column: right_column]
