# -*- coding: utf8 -*-
import click

from game_of_life.conf import settings
from game_of_life.algorithm import game_of_life


_help_messages = {
    "width": "The width of the world, an integer between {min} and {max}."
        .format(min=settings.MINIMAL_BOARD_WIDTH, max=50),
    "height": "The height of the world, an integer between {min} and {max}."
        .format(min=settings.MINIMAL_BOARD_HEIGHT, max=50)
}


@click.group()
def game_of_life_command():
    """Where all the magic happens"""


@game_of_life_command.command()
def preset():
    """
    A preset starting world.


    :return:
    """
    pass


@game_of_life_command.command()
@click.argument("generations", type=click.INT)
@click.option(
    "-h",
    "--height",
    "height",
    default=settings.MINIMAL_BOARD_HEIGHT,
    show_default=True,
    help=_help_messages["height"],
    type=click.IntRange(min=settings.MINIMAL_BOARD_HEIGHT, max=50),
)
@click.option(
    "-w",
    "--width",
    "width",
    default=settings.MINIMAL_BOARD_WIDTH,
    show_default=True,
    help=_help_messages["width"],
    type=click.IntRange(min=settings.MINIMAL_BOARD_WIDTH, max=50),
)
def random(generations, height, width):
    """
    A randomized starting world.

    [INT] GENERATIONS is the number of life-cycles it iterates through
    before forcing and end. Input 0 for an infinite loop.
    """
    game_of_life(width=width, generations=generations, height=height)
