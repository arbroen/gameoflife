# -*- coding: utf8 -*-
import time

from numpy import ndarray

from shine_on_life.conf import settings

from .printer import board_printer
from .boards import random_board
from .mutators import mutation


def still_alive(generations: int, increment: int, board: ndarray) -> bool:
    """
    Determines whether there is still life or that we want to continue living.
    :param generations:
    :param increment:
    :param board:
    :return:
    """
    if board.sum() == 0:
        return False

    if generations == 0:
        return True

    return generations != increment


def game_of_life(height: int, width: int, generations: int) -> None:
    """
    Should combine all the logic into one point of truth.
    """
    increment = 0
    board = random_board(height=height, width=width)
    board_printer(board=board)

    while still_alive(generations, increment, board):
        board = mutation(board=board)
        board_printer(board=board)
        time.sleep(settings.DEFAULT_REFRESH_TIME)
        increment += 1
