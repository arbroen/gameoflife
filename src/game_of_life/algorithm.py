# -*- coding: utf8 -*-
import time

import numpy as np

from game_of_life.conf import settings
from game_of_life.worlds import random_world
from game_of_life.printer import WorldContextPrinter
from game_of_life.mutation import world_mutation


def still_alive(world: np.ndarray, generations: int, increment: int) -> bool:
    """
    Determines whether there is still life or that we want to continue living.
    :param generations:
    :param increment:
    :param world:
    :return:
    """
    if not np.count_nonzero(world):
        return False

    if generations == 0:
        return True

    return generations != increment


def game_generator(world: np.ndarray, generations: int) -> np.ndarray:
    """
    Generates the next sequence of life.
    :param world:
    :param generations:
    :return:
    """
    increment = 0

    while still_alive(generations=generations, increment=increment, world=world):
        world = world_mutation(world=world)
        increment += 1
        yield world


def game_of_life(height: int, width: int, generations: int) -> None:
    """
    Should combine all the logic into one point of truth.
    """
    new_world = random_world(height=height, width=width)

    with WorldContextPrinter() as printer:
        printer(world=new_world)

        for world in game_generator(world=new_world, generations=generations):
            time.sleep(settings.DEFAULT_REFRESH_TIME)
            printer(world=world)
