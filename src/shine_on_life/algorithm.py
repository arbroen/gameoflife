#!/usr/bin/python
# -*- coding: utf8 -*-
import time

from shine_on_life.printer import board_printer
from shine_on_life.board import Board


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
        board = Board(height=height, width=width)
        board_printer(board=board)
        time.sleep(.25)
        increment += 1
