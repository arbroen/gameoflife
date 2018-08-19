# -*- coding: utf8 -*-
from numpy.testing import assert_array_equal

from shine_on_life.worlds import CellTypes
from shine_on_life.mutation import cell_lives, cell_spawns, cell_mutation, \
    neighbour_count, world_mutation


class TestMutation:
    def test_cell_spawns_life(self):
        """
        Only one specific scenario creates new life.
        :return:
        """
        assert not cell_spawns(cycle=CellTypes.DEAD, count=2)
        assert cell_spawns(cycle=CellTypes.DEAD, count=3)
        assert not cell_spawns(cycle=CellTypes.DEAD, count=4)

        assert not cell_spawns(cycle=CellTypes.ALIVE, count=2)
        assert not cell_spawns(cycle=CellTypes.ALIVE, count=3)
        assert not cell_spawns(cycle=CellTypes.ALIVE, count=4)

        assert not cell_spawns(cycle=CellTypes.SPAWNED, count=2)
        assert not cell_spawns(cycle=CellTypes.SPAWNED, count=3)
        assert not cell_spawns(cycle=CellTypes.SPAWNED, count=4)

    def test_cell_stays_alive(self):
        """
        Staying alive is slightly easier than creating life. The following
        input should always hold true.
        :return:
        """
        assert not cell_lives(cycle=CellTypes.ALIVE, count=1)
        assert cell_lives(cycle=CellTypes.ALIVE, count=3)
        assert cell_lives(cycle=CellTypes.ALIVE, count=2)
        assert not cell_lives(cycle=CellTypes.ALIVE, count=4)

        assert not cell_lives(cycle=CellTypes.SPAWNED, count=1)
        assert cell_lives(cycle=CellTypes.SPAWNED, count=3)
        assert cell_lives(cycle=CellTypes.SPAWNED, count=2)
        assert not cell_lives(cycle=CellTypes.SPAWNED, count=4)

        assert not cell_lives(cycle=CellTypes.DEAD, count=1)
        assert not cell_lives(cycle=CellTypes.DEAD, count=3)
        assert not cell_lives(cycle=CellTypes.DEAD, count=2)
        assert not cell_lives(cycle=CellTypes.DEAD, count=4)

    def test_neighbour_counting(self, small_world):
        """
        Neighbour count should count the 8 cells close to the index, but
        exclude it's own value.
        :param small_world:
        :return:
        """
        assert neighbour_count(cell_index=(0, 0), world=small_world) == 0
        assert neighbour_count(cell_index=(0, 3), world=small_world) == 2
        assert neighbour_count(cell_index=(3, 0), world=small_world) == 1
        assert neighbour_count(cell_index=(1, 2), world=small_world) == 6
        assert neighbour_count(cell_index=(3, 3), world=small_world) == 2

    def test_cell_mutation(self, small_world):
        """
        Test all possible cell mutations given their neighbours.
        :param small_world:
        :return:
        """
        assert cell_mutation(
            index=(0, 0), world=small_world) == CellTypes.DEAD
        assert cell_mutation(
            index=(0, 3), world=small_world) == CellTypes.ALIVE
        assert cell_mutation(
            index=(3, 0), world=small_world) == CellTypes.DEAD
        assert cell_mutation(
            index=(1, 2), world=small_world) == CellTypes.DEAD
        assert cell_mutation(
            index=(3, 3), world=small_world) == CellTypes.ALIVE
        assert cell_mutation(
            index=(1, 1), world=small_world) == CellTypes.SPAWNED
        assert cell_mutation(
            index=(3, 1), world=small_world) == CellTypes.SPAWNED

    def test_world_mutation(self, small_world, medium_world):
        """
        Test the next instances of a given world.
        :param small_world:
        :param medium_world:
        :return:
        """
        expected = \
            [[0, 0, 2, 2],
             [0, 1, 0, 0],
             [0, 2, 0, 2],
             [0, 1, 0, 2]]
        next_world = world_mutation(world=small_world)
        assert_array_equal(x=next_world, y=expected)

        medium_expected = \
            [[0, 0, 2, 2, 0, 0, 2],
             [0, 1, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 2],
             [2, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 2, 0, 0],
             [0, 0, 0, 0, 2, 1, 0],
             [2, 0, 2, 0, 0, 0, 0]]
        next_world_medium = world_mutation(world=medium_world)
        assert_array_equal(x=next_world_medium, y=medium_expected)
