# -*- coding: utf8 -*-
import enum
from pathlib import Path

import numpy as np
from gol.conf import settings


class CellTypes(enum.IntEnum):
    DEAD = 0
    ALIVE = 2
    SPAWNED = 1


def is_valid_world(world: np.ndarray):
    """
    Validates a given world for it's shape and content.
    :param world:
    :return:
    """
    _errors = []
    width, height = world.shape

    if width < settings.MINIMAL_BOARD_WIDTH:
        _errors.append(
            "A board's width is at least {minimal}.".format(
                minimal=settings.MINIMAL_BOARD_WIDTH
            )
        )

    if height < settings.MINIMAL_BOARD_WIDTH:
        _errors.append(
            "A board's height is at least {minimal}.".format(
                minimal=settings.MINIMAL_BOARD_WIDTH
            )
        )

    if str(world.dtype) != settings.NUMPY_DATA_TYPE:
        _errors.append(
            "A world, type numpy 2d array, should contain  data_type {}".format(
                settings.NUMPY_DATA_TYPE
            )
        )

    possible_values = list(map(int, CellTypes))
    if any([value not in possible_values for value in np.unique(world)]):
        _errors.append(
            "Invalid value found in array, values must be one off: {}".format(
                possible_values
            )
        )

    if _errors:
        raise TypeError("\n".join(_errors))


def random_world(height: int, width: int) -> np.ndarray:
    """
    Constructs a numpy ndarray of the given height and width with random
    living cells, denoted by integer 1.

    :param height: positive integer
    :param width: positive integer
    :return:
    """
    chaos_world = np.random.randint(
        low=2, size=(width, height), dtype=settings.NUMPY_DATA_TYPE
    )

    is_valid_world(world=chaos_world)

    return chaos_world


def preset_world(preset: Path) -> np.ndarray:
    loaded_world = np.loadtxt(
        str(preset), delimiter=";", dtype=settings.NUMPY_DATA_TYPE
    )

    is_valid_world(world=loaded_world)

    return loaded_world


def custom_world(preset: str = None) -> np.ndarray:
    pass
