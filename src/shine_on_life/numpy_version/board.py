#!/usr/bin/python
# -*- coding: utf8 -*-
import numpy as np

from shine_on_life.conf import settings


class Cell:
    alive: bool = None
    died: bool = None
    sprouted: bool = None


class Board:
    """
    Basically encapsulates all state of the algorithm and the operations that
    can change said state.
    """
    _height: int = None
    _width: int = None
    _two_d_array: np.ndarray = None

    def __init__(self, height: int=None, width: int=None):
        # A low randint indicates an two-dimensional array of zeros and ones.
        self.width = width or settings.DEFAULT_BOARD_WIDTH
        self.height = height or settings.DEFAULT_BOARD_HEIGHT
        self._two_d_array = np.random.randint(
            low=2, size=(self.width, self.height), dtype=int)

    @staticmethod
    def _min_checker(value, attr_name) -> None:
        if value < MIN_WIDTH_HEIGHT:
            raise TypeError(
                "A board's {attr_name} is at least {minimal}."
                .format(attr_name=attr_name, minimal=MIN_WIDTH_HEIGHT))

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        self._min_checker(value=value, attr_name="width")
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._min_checker(value=value, attr_name="height")
        self._height = value

    @property
    def contents(self) -> np.ndarray:
        """Used by the printer function."""
        return self._two_d_array

    def kill_cell(self, point):
        pass

    def grow_cell(self, point):
        pass
