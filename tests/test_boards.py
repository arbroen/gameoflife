# -*- coding: utf8 -*-
from game_of_life.worlds import random_world


class TestRandomBoard:
    def test_functional_board(self):
        b = random_world(10, 10)

        assert len(b) == 10
