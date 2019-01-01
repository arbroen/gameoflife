# -*- coding: utf8 -*-
import click

from shine_on_life.conf import settings
from shine_on_life.algorithm import game_of_life


# @click.group()
# def commands():
#     """
#     Groups all commands nicely together. #fancy click library.
#     :return:
#     """
#     pass
#
#
# @commands.command()
# def preset():
#     """
#     Game of life with a preset starting world.
#     """
#     pass


@click.command()
@click.argument(
    'generations', type=click.INT)
@click.option(
    '-h', '--height', default=settings.MINIMAL_BOARD_HEIGHT,
    type=click.IntRange(min=settings.MINIMAL_BOARD_HEIGHT, max=50))
@click.option(
    '-w', '--width', default=settings.MINIMAL_BOARD_WIDTH,
    type=click.IntRange(min=settings.MINIMAL_BOARD_WIDTH, max=50))
def commands(generations, height, width):
    """
    Game of life with a random starting world.

    GENERATIONS is the amount of life-cycles it goes through before stopping.
    Input 0 for an infinity loop.
    """
    game_of_life(
        width=width, generations=generations, height=height)
