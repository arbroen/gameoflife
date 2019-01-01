# -*- coding: utf8 -*-
from numpy import zeros, ones

from shine_on_life.algorithm import still_alive, game_generator


class TestAlgorithm:
    def test_loop_condition(self, small_world):
        """
        Tests the function that determines whether the game should still be
        running.
        :return:
        """
        assert still_alive(world=small_world, generations=0, increment=0)
        assert still_alive(world=small_world, generations=1, increment=0)
        assert not still_alive(world=small_world, generations=1, increment=1)

        dead_world = zeros((5, 5))
        assert not still_alive(world=dead_world, generations=10, increment=1)
        assert not still_alive(world=dead_world, generations=10, increment=10)

    def test_game_generator(self, small_world, medium_world):
        """
        Test the generator, given our static worlds it should create a static
        amount.
        :param small_world:
        :return:
        """
        all_worlds = [
            world for world in game_generator(world=small_world, generations=0)
        ]

        assert len(all_worlds) == 7

        all_medium_worlds = [
            world for world in game_generator(world=medium_world, generations=0)
        ]

        assert len(all_medium_worlds) == 9

        overpopulated_world = ones((10, 10))

        food_for_though = [
            world for world in game_generator(world=overpopulated_world, generations=0)
        ]

        # 2 instances because the corners apparently survive.
        assert len(food_for_though) == 2
