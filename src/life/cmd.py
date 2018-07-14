#!/usr/bin/python
# -*- coding: utf8 -*-
import click

from .board import MIN_WIDTH_HEIGHT
from .algorithm import game_of_life


@click.command()
@click.argument(
    'height', type=click.IntRange(min=MIN_WIDTH_HEIGHT, max=None))
@click.argument(
    'generations', type=click.INT)
@click.option(
    '-w', '--width', default=None, type=click.IntRange(min=10, max=None),
    help="The width of the table. Note, that a high number might not display"
         " correctly in your shell.")
def cmd_line(height, generations, width):
    if width is None:
        width = height

    game_of_life(width=width, generations=generations, height=height)
