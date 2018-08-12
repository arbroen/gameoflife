# -*- coding: utf8 -*-
import time

from numpy import ndarray, count_nonzero

from shine_on_life.conf import settings
from shine_on_life.worlds import random_world
from shine_on_life.printer import WorldContextPrinter
from shine_on_life.mutation import world_mutator


def still_alive(generations: int, increment: int, world: ndarray) -> bool:
    """
    Determines whether there is still life or that we want to continue living.
    :param generations:
    :param increment:
    :param world:
    :return:
    """
    if not count_nonzero(world):
        return False

    if generations == 0:
        return True

    return generations != increment


def game_of_life(height: int, width: int, generations: int) -> None:
    """
    Should combine all the logic into one point of truth.
    """
    increment = 0
    world = random_world(height=height, width=width)

    with WorldContextPrinter() as printer:
        while still_alive(generations, increment, world):
            time.sleep(settings.DEFAULT_REFRESH_TIME)
            world = world_mutator(world=world)
            printer(world=world)
            increment += 1
