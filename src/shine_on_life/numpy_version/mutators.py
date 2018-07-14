#!/usr/bin/python
# -*- coding: utf8 -*-
from shine_on_life.numpy_version.board import Board


def _get_living_cells(board: Board):
    """
    These cells have either 2 or 3 neighbours that are also alive,
    and hence, they will stay alive for another generation.
    :return:
    """
    pass


def _get_dying_cells(board: Board):
    """
    Two conditions apply for dying cells.
    - Overcrowding. Four or more living neighbours.
    - Underpopulation. Two or less neighbours are still alive.
    :return:
    """


def _get_growing_cells(board: Board):
    """
    If a cell has exactly three living neighbours, this dead cell will
    sprout new life.
    :return:
    """


def _error_check(board: Board):
    """
    Checks whether no cells index match with the others.
    :return:
    """


def _terminated_cells(locations):
    pass


def _genesis(locations):
    pass


def mutate(board: Board):
    pass
