# -*- coding: utf8 -*-
import pytest

from numpy import array, array_equal

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
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ])

        # This implies 9 iterations
        subsets = [x for x in neighbour_counter(input_board)]

        assert len(subsets) == 9

        # The first corner 0, 0
        assert array_equal(subsets[0], [[1, 2], [1, 2]])

        # The middle
        assert array_equal(subsets[4], input_board)

        # The side middle one
        assert array_equal(subsets[5], [[2, 3], [2, 3], [2, 3]])

        # The last corner 2, 2
        assert array_equal(subsets[8], [[2, 3], [2, 3]])

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
        assert all_iterations[0] == (0, 0, 3)

        # The last corner 1, 3
        assert all_iterations[7] == (1, 3, 2)

        # The 3rd value
        assert all_iterations[2] == (0, 2, 2)
