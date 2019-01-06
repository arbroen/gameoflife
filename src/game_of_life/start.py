# -*- coding: utf8 -*-
"""
The interface to the algorithm via command line.

    gol <<subcommand>> --options

The implementation logic is completely separated from this interface, to easily allow
for different interfaces in the possible future.
"""
import click

from game_of_life.conf import settings
from game_of_life.algorithm import random_life, preset_life, custom_life


_HELP_MSG = {
    "width": "The width of the world, an integer between {min} and {max}.".format(
        min=settings.MINIMAL_BOARD_WIDTH, max=50
    ),
    "height": "The height of the world, an integer between {min} and {max}.".format(
        min=settings.MINIMAL_BOARD_HEIGHT, max=50
    ),
    "generations":
        "GENERATIONS is the number of life-cycles it iterates through"
        "before forcing and end. Input 0 for an infinite loop.",
    "preset": "Select a possible option."
}


@click.group()
def game_of_life_command():
    """My implementation of the game of life algorithm.

    For any of the commands below you can access it's information with:

    \b
        gol <<command>> --help

    PS. This interface was written with the use of click. A beautiful alternative to
    argparse hell.
    """


@game_of_life_command.command()
@click.argument(
    "choice",
    type=click.Choice([
        # @TODO: Insert list of names here.
    ]),
)
@click.option(
    "-g",
    "--generations",
    "generations",
    default=settings.DEFAULT_GENERATIONS,
    show_default=True,
    help=_HELP_MSG["generations"],
    type=click.INT
)
def preset(choice, generations):
    """
    A preset starting world.
    """
    preset_life(preset=choice, generations=generations)


@game_of_life_command.command()
@click.argument(
    "file_path",
    type=click.Path(),
)
@click.option(
    "-g",
    "--generations",
    "generations",
    default=settings.DEFAULT_GENERATIONS,
    show_default=True,
    help=_HELP_MSG["generations"],
    type=click.INT
)
def custom(file_path, generations):
    """
    Pass your own file to play your custom made game_of_life.
    """
    custom_life(path=file_path, generations=generations)


@game_of_life_command.command()
@click.option(
    "-g",
    "--generations",
    "generations",
    default=settings.DEFAULT_GENERATIONS,
    show_default=True,
    help=_HELP_MSG["generations"],
    type=click.INT
)
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
def random(generations, height, width):
    """A randomized starting world for the game_of_life algorithm."""
    random_life(width=width, generations=generations, height=height)
