#!/usr/bin/python
# -*- coding: utf8 -*-
import time

from shine_on_life.printer import board_printer
from shine_on_life.board import Board


def game_of_life(height: int, width: int, generations: int):
    """
    Should combine all the logic into one point of truth.
    """
    for i in range(generations):
        board = Board(height=height, width=width)
        board_printer(board=board)
        time.sleep(.23)
