# -*- coding: utf8 -*-
import time

from shine_on_life.conf import settings

from .printer import board_printer
from .boards import random_board


def running(generations, increment):
    # 0 generations is infinite loop
    if generations == 0:
        return True

    return generations != increment


def game_of_life(height: int, width: int, generations: int):
    """
    Should combine all the logic into one point of truth.
    """
    increment = 0

    while running(generations, increment):
        board = random_board(height=height, width=width)
        board_printer(board=board)
        time.sleep(settings.DEFAULT_REFRESH_TIME)
        increment += 1
