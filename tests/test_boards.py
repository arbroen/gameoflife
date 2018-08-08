# -*- coding: utf8 -*-
from shine_on_life.boards import random_board


class TestRandomBoard:
    def test_functional_board(self):
        b = random_board(10, 10)

        assert len(b) == 10
