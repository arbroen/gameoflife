# -*- coding: utf8 -*-
"""
Printing is going to be fancy as fly. With colors.

- green ones are freshly spouted.
- red zeros just perished.
"""
import os
import platform

from numpy import ndarray
from typing import Callable
from colorama import init as colorama_init
from colorama import Fore, Style

from .worlds import CellTypes

COLOUR_SCHEME = {
    CellTypes.DEAD.value: Fore.LIGHTBLACK_EX,
    CellTypes.SPAWNED.value: Fore.GREEN,
    CellTypes.ALIVE.value: Fore.YELLOW
}


def colorize(value) -> str:
    return COLOUR_SCHEME[value] + str(value)


def clear_shell_display():
    """
    Didn't test this method. But ah well, A for effort, if I say so myself.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


class WorldContextPrinter:
    """
    Class to be used as a context manager that encapsulates the colorama
    library to properly init colorama and close off any open colour coding.
    """

    def __init__(self, print_func: Callable = None,
                 formatter: Callable = None):
        """
        This init is required bye the colorama package for windows support.
        See docs: https://pypi.org/project/colorama/

        Could be writing to regular file logs by passing a different
        print_func and formatter for example.
        """
        colorama_init()
        self.print_function = print_func or print
        self.formatter = formatter or colorize

    def __call__(self, *args, **kwargs):
        return self.print_function(*args, **kwargs)

    def __enter__(self):
        return self

    def print(self, world: ndarray):
        clear_shell_display()
        _temp = ""

        for i in range(world.shape[1]):
            _temp += "  ".join([self.formatter(x) for x in world[:, i]])
            _temp += "\n"

        self.print_function(_temp)

    def __exit__(self, *args):
        self.print_function(Style.RESET_ALL)
