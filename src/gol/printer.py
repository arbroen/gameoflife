"""
Printing is going to be fancy as fly. With colors.

- green ones are freshly spouted.
- red zeros just perished.
"""
import logging
from typing import Callable

from colorama import Fore, Style
from colorama import init as colorama_init

import numpy as np

from .worlds import CellTypes

COLOUR_SCHEME = {
    CellTypes.DEAD.value: Fore.LIGHTBLACK_EX,
    CellTypes.SPAWNED.value: Fore.GREEN,
    CellTypes.ALIVE.value: Fore.YELLOW,
}


logger = logging.getLogger("printer")


def colorize(value) -> str:
    return COLOUR_SCHEME[value] + str(value)


class WorldContextPrinter:
    """
    Class to be used as a context manager that encapsulates the colorama
    library to properly init colorama and close off any open colour coding.
    """

    def __init__(self, print_func: Callable = None, formatter: Callable = None):
        """
        This init is required bye the colorama package for windows support.
        See docs: https://pypi.org/project/colorama/

        Could be writing to regular file logs by passing a different
        print_func and formatter for example.
        """
        colorama_init()
        self.print_function = print_func or logger.info
        self.formatter = formatter or colorize

    def clear_shell_display(self):
        """
        Didn't test this method. But ah well, A for effort, if I say so myself.
        """
        self.print_function(chr(27) + "[2J")

    def __call__(self, *args, **kwargs):
        return self.emit(*args, **kwargs)

    def __enter__(self):
        return self

    def emit(self, world: np.ndarray):
        self.clear_shell_display()
        _temp = ""

        for i in range(world.shape[1]):
            _temp += "  ".join([self.formatter(x) for x in world[:, i]])
            _temp += "\n"

        self.print_function(_temp)

    def __exit__(self, *args):
        self.print_function(Style.RESET_ALL)
