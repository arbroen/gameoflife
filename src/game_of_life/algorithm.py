# -*- coding: utf8 -*-
import time

import numpy as np

from game_of_life.conf import settings
from game_of_life.worlds import random_world, preset_world, custom_world
from game_of_life.printer import WorldContextPrinter
from game_of_life.mutation import world_mutation
from game_of_life.presets import PRESETS


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


def world_generator(world: np.ndarray, generations: int) -> np.ndarray:
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


def game_generator(world: np.ndarray, generations: int):
    """

    :param world:
    :param generations:
    :return:
    """
    with WorldContextPrinter() as printer:
        printer(world=world)

        for world in world_generator(world=world, generations=generations):
            time.sleep(settings.DEFAULT_REFRESH_TIME)
            printer(world=world)


def preset_life(preset: str, generations: int) -> None:
    choice = PRESETS[preset]
    print(choice)
    # world = preset_world()
    # game_generator(world=world, generations=generations)


def random_life(height: int, width: int, generations: int) -> None:
    world = random_world(height=height, width=width)
    game_generator(world=world, generations=generations)


def custom_life(path: str, generations: int) -> None:
    world = custom_world()
    game_generator(world=world, generations=generations)
