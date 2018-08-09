# -*- coding: utf8 -*-
import time

from numpy import ndarray

from shine_on_life.conf import settings

from shine_on_life.printer import world_printer
from shine_on_life.world import random_board
from shine_on_life.mutation import world_mutator


def still_alive(generations: int, increment: int, world: ndarray) -> bool:
    """
    Determines whether there is still life or that we want to continue living.
    :param generations:
    :param increment:
    :param world:
    :return:
    """
    if world.sum() == 0:
        return False

    if generations == 0:
        return True

    return generations != increment


def game_of_life(height: int, width: int, generations: int) -> None:
    """
    Should combine all the logic into one point of truth.
    """
    increment = 0
    world = random_board(height=height, width=width)
    world_printer(board=world)

    while still_alive(generations, increment, world):
        world = world_mutator(world=world)
        time.sleep(settings.DEFAULT_REFRESH_TIME)
        world_printer(board=world)
        increment += 1
