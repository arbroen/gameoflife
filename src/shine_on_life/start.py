#!/usr/bin/python
# -*- coding: utf8 -*-
import click

from shine_on_life.board import MIN_WIDTH_HEIGHT
from shine_on_life.algorithm import game_of_life


@click.command()
@click.argument(
    'generations', type=click.INT)
@click.argument(
    'height', default=MIN_WIDTH_HEIGHT,
    type=click.IntRange(min=MIN_WIDTH_HEIGHT, max=50))
@click.option(
    '-w', '--width', default=MIN_WIDTH_HEIGHT,
    type=click.IntRange(min=MIN_WIDTH_HEIGHT, max=50),
    help="The width of the table. Note, that a high number might not display"
         " correctly in your shell.")
def cmd_line(height, generations, width):
    game_of_life(width=width, generations=generations, height=height)
