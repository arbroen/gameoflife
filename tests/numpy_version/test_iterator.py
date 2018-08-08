# -*- coding: utf8 -*-
import pytest

from numpy import array, zeros

from shine_on_life.numpy_version.iterator import neighbour_counter


class TestIteration:
    def test_empty_array(self):
        """raises error as not a 2 dimensional array"""
        empty = array([])

        with pytest.raises(AttributeError) as e:
            x = neighbour_counter(empty)
            next(x)

        msg = "It is only possible to iterate over two-dimensional boards."
        assert msg in str(e)

    def test_empty_2d_array(self):
        """Should work fine, just won't do much."""
        empty = array([[], [], []])

        with pytest.raises(StopIteration):
            x = neighbour_counter(empty)
            assert next(x) is None

    def test_empty_3d_array(self):
        """raises error as with empty array"""
        empty = array([[[]], [[]], [[]]])

        with pytest.raises(AttributeError) as e:
            x = neighbour_counter(empty)
            next(x)

        msg = "It is only possible to iterate over two-dimensional boards."
        assert msg in str(e)

    def test_square_array(self):
        """Test whether no weird things happens with squares"""
        input_board = array([
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ])

        # This implies 9 iterations
        all_iterations = [x for x in neighbour_counter(input_board)]

        assert len(all_iterations) == 9

        # The first corner 0, 0
        assert all_iterations[0] == (0, 0, 1)

        # The middle
        assert all_iterations[4] == (1, 1, 4)

        # The side middle one
        assert all_iterations[5] == (1, 2, 3)

        # The last corner 2, 2
        assert all_iterations[8] == (2, 2, 1)

    def test_rectangular_array(self):
        """Most basic use-case testing"""

        input_board = array([
            [1, 0, 1, 0],
            [1, 1, 1, 0]
        ])

        # This implies 8 iterations
        all_iterations = [x for x in neighbour_counter(input_board)]

        assert len(all_iterations) == 8

        # The first corner 0, 0
        assert all_iterations[0] == (0, 0, 2)

        # The last corner 1, 3
        assert all_iterations[7] == (1, 3, 2)

        # The 3rd value
        assert all_iterations[2] == (0, 2, 2)

    def test_dead_array(self):
        """Most basic use-case testing"""
        dead_board = zeros(shape=(3, 3), dtype=int)

        results = \
            [cell_value for _, _, cell_value in neighbour_counter(dead_board)]

        assert sum(results) == 0
