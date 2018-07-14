#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Printing is going to be fancy as fly. With colors.

- green ones are freshly spouted.
- red zeros just perished.
"""
import os
import platform

from shine_on_life.board import Board


def clear_shell_display():
    """
    Didn't test this method. But ah well, A for effort, if I say so myself.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def board_printer(board: Board):
    # Print the numpy array as such
    clear_shell_display()
    _temp = ""

    for i in range(board.contents.shape[1]):
        _temp += "  ".join([str(x) for x in board.contents[:, i]])
        _temp += "\n"

    print('\033[34m{msg}\033[0m'.format(msg=_temp), flush=True)
