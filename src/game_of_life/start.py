# -*- coding: utf8 -*-
import click

from game_of_life.conf import settings
from game_of_life.algorithm import game_of_life


@click.group()
def random():
    """
    Groups all commands nicely together. #fancy click library.
    :return:
    """
    pass


#
#
# @commands.command()
# def preset():
#     """
#     Game of life with a preset starting world.
#     """
#     pass


_help_messages = {
    "width": "The width of the world, an integer between {min} and {max}."
    "If omitted, it will be defaulted to minimal value.".format(
        min=settings.MINIMAL_BOARD_WIDTH, max=50
    ),
    "height": "The height of the world, an integer between {min} and {max}. "
    "If omitted, it will be defaulted to minimal value.".format(
        min=settings.MINIMAL_BOARD_HEIGHT, max=50
    ),
}


@click.command()
@click.argument("generations", type=click.INT)
@click.option(
    "-h",
    "--height",
    default=settings.MINIMAL_BOARD_HEIGHT,
    help=_help_messages["height"],
    type=click.IntRange(min=settings.MINIMAL_BOARD_HEIGHT, max=50),
)
@click.option(
    "-w",
    "--width",
    default=settings.MINIMAL_BOARD_WIDTH,
    help=_help_messages["width"],
    type=click.IntRange(min=settings.MINIMAL_BOARD_WIDTH, max=50),
)
def commands(generations, height, width):
    """
    A game of life algorithm with a randomized starting world.

    [INTEGER] GENERATIONS is the number of life-cycles it iterates through
    before forcing and end. Input 0 for an infinite loop.
    """
    game_of_life(width=width, generations=generations, height=height)
