#!/usr/bin/python
# -*- coding: utf8 -*-
import click

from shine_on_life.numpy_version.board import MIN_WIDTH_HEIGHT
from shine_on_life.numpy_version.algorithm import game_of_life


@click.command()
@click.argument(
    'generations', type=click.INT)
@click.option(
    '-h', '--height', default=MIN_WIDTH_HEIGHT,
    type=click.IntRange(min=MIN_WIDTH_HEIGHT, max=50))
@click.option(
    '-w', '--width', default=MIN_WIDTH_HEIGHT,
    type=click.IntRange(min=MIN_WIDTH_HEIGHT, max=50),
    )
def cmd_line(generations, height, width):
    """
    This script kicks of the Shine of Life algorithm.

    GENERATIONS is the amount of life-cycles it goes through before stopping.
    Input 0 for an infinity loop.
    """
    game_of_life(
        width=width, generations=generations, height=height)
