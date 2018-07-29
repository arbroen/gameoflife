# -*- coding: utf8 -*-
from numpy import ndarray, ndenumerate


def iterate_3x3_shapes(board: ndarray):
    """
    Iterate over the board, yielding all cells connected to the current cell.
    In a 3x3 shape.
    :param board:
    :return:
    """
    row_count, column_count = board.shape

    for (row, column), _ in ndenumerate(board):
        top_row, bottom_row = \
            max(0, row - 1), min(row_count, row + 2)

        left_column, right_column = \
            max(0, column - 1), min(column_count, column + 2)

        yield board[top_row: bottom_row, left_column: right_column]
