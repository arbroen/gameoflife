# -*- coding: utf8 -*-
"""
The interface to the algorithm via command line.

    gol <<subcommand>> --options

The implementation logic is completely separated from this interface, to easily allow
for different interfaces in the possible future.
"""
import click

from collections import namedtuple

from game_of_life.conf import settings
from game_of_life.algorithm import random_life, preset_life, custom_life


_HELP_MSG = {
    "width": "The width of the world, an integer between {min} and {max}.".format(
        min=settings.MINIMAL_BOARD_WIDTH, max=50
    ),
    "height": "The height of the world, an integer between {min} and {max}.".format(
        min=settings.MINIMAL_BOARD_HEIGHT, max=50
    ),
    "generations": "GENERATIONS is the number of life-cycles it iterates through"
    "before forcing and end. Input 0 for an infinite loop.",
    "preset": "Select a possible option.",
}


Context = namedtuple("Context", ["generations"])


@click.group()
@click.option(
    "-g",
    "--generations",
    "generations",
    default=settings.DEFAULT_GENERATION_COUNT,
    show_default=True,
    help=_HELP_MSG["generations"],
    type=click.INT,
)
@click.pass_context
def game_of_life_command(ctx, generations):
    """My implementation of the game of life algorithm.

    For any of the commands below you can access it's information with:

    \b
        gol <<command>> --help
    \b
    Example command
    \b
        gol --generations 0 random

    PS. This interface was written with the use of click. A beautiful alternative to
    argparse hell.
    """
    ctx.obj = Context(generations=generations)


@game_of_life_command.command()
@click.pass_obj
@click.argument(
    "choice",
    type=click.Choice(
        [
            # @TODO: Insert list of names here.
        ]
    ),
)
def preset(context, choice):
    """
    A preset starting world.
    """
    preset_life(preset=choice, generations=context.generations)


@game_of_life_command.command()
@click.pass_obj
@click.argument("csv_file_path", type=click.File(mode="r"))
def custom(file_path, generations):
    """
    Pass your own csv_file to play your custom made game_of_life. The input must be rows
    off integers supported. These can be checked in the CellTypes class.
    """
    custom_life(path=file_path, generations=generations)


@game_of_life_command.command()
@click.pass_obj
@click.option(
    "-h",
    "--height",
    "height",
    default=settings.MINIMAL_BOARD_HEIGHT,
    show_default=True,
    help=_HELP_MSG["height"],
    type=click.IntRange(min=settings.MINIMAL_BOARD_HEIGHT, max=50),
)
@click.option(
    "-w",
    "--width",
    "width",
    default=settings.MINIMAL_BOARD_WIDTH,
    show_default=True,
    help=_HELP_MSG["width"],
    type=click.IntRange(min=settings.MINIMAL_BOARD_WIDTH, max=50),
)
def random(context, height, width):
    """A randomized starting world for the game_of_life algorithm."""
    random_life(width=width, height=height, generations=context.generations)
