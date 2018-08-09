# -*- coding: utf8 -*-
import enum

from numpy import random

from shine_on_life.conf import settings


class CellTypes(enum.IntEnum):
    DEAD = 0
    ALIVE = 2
    SPAWNED = 1


def random_board(height: int, width: int):
    """
    Constructs a numpy ndarray of the given height and width with random
    living cells, denoted by integer 1.

    :param height: positive integer
    :param width: positive integer
    :return:
    """
    _errors = []

    # if width < settings.MINIMAL_BOARD_WIDTH:
    #     _errors.append(
    #         "A board's width is at least {minimal}.".format(
    #             minimal=settings.MINIMAL_BOARD_WIDTH))
    #
    # if height < settings.MINIMAL_BOARD_WIDTH:
    #     _errors.append(
    #         "A board's height is at least {minimal}.".format(
    #             minimal=settings.MINIMAL_BOARD_WIDTH))

    if _errors:
        raise TypeError("\n".join(_errors))

    return random.randint(
        low=2, size=(width, height), dtype=settings.NUMPY_DATA_TYPE)
