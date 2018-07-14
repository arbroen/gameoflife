#!/usr/bin/python
# -*- coding: utf8 -*-
import numpy as np


MIN_WIDTH_HEIGHT = 10


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

    def __init__(self, height: int, width: int) -> None:
        # A low randint indicates an two-dimensional array of zeros and ones.
        self.width = width
        self.height = height
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

    def _get_living_cells(self):
        """
        These cells have either 2 or 3 neighbours that are also alive,
        and hence, they will stay alive for another generation.
        :return:
        """
        pass

    def _get_dying_cells(self):
        """
        Two conditions apply for dying cells.
        - Overcrowding. Four or more living neighbours.
        - Underpopulation. Two or less neighbours are still alive.
        :return:
        """

    def _get_growing_cells(self):
        """
        If a cell has exactly three living neighbours, this dead cell will
        sprout new life.
        :return:
        """

    def _error_check(self):
        """
        Checks whether no cells index match with the others.
        :return:
        """

    def _kill_cells(self, locations):
        pass

    def _birth_cells(self, locations):
        pass

    def mutate(self):
        pass
