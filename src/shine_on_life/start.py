# -*- coding: utf8 -*-
import click

from shine_on_life.conf import settings
from shine_on_life.algorithm import game_of_life


@click.command()
@click.argument(
    'generations', type=click.INT)
@click.option(
    '-h', '--height', default=settings.MINIMAL_BOARD_HEIGHT,
    type=click.IntRange(min=3, max=50))
@click.option(
    '-w', '--width', default=settings.MINIMAL_BOARD_WIDTH,
    type=click.IntRange(min=3, max=50))
def cmd_line(generations, height, width):
    """
    This script kicks of the Shine of Life algorithm.

    GENERATIONS is the amount of life-cycles it goes through before stopping.
    Input 0 for an infinity loop.
    """
    game_of_life(
        width=width, generations=generations, height=height)
