# -*- coding: utf8 -*-
from pytest import fixture
from numpy import array


@fixture
def small_world():
    """Static world. Makes up for a predictable world."""
    return array([[0, 0, 2, 1], [0, 0, 0, 1], [0, 2, 2, 1], [1, 0, 0, 1]])


@fixture
def medium_world():
    """Static world. Makes up for a predictable world."""
    return array(
        [
            [0, 0, 2, 1, 0, 2, 1],
            [0, 0, 0, 1, 1, 2, 1],
            [0, 2, 2, 1, 0, 1, 2],
            [1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0],
            [2, 2, 0, 0, 1, 0, 0],
            [1, 2, 1, 0, 0, 0, 2],
        ]
    )
