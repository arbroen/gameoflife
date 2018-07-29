# -*- coding: utf8 -*-
import pytest

from numpy import array, array_equal

from shine_on_life.numpy_version.iterator import iterate_3x3_shapes


class TestIteration:
    def test_empty_array(self):
        """raises error as not a 2 dimensional array"""
        empty = array([])

        with pytest.raises(AttributeError) as e:
            x = iterate_3x3_shapes(empty)
            next(x)

        msg = "It is only possible to iterate over two-dimensional boards."
        assert msg in str(e)

    def test_empty_2d_array(self):
        """Should work fine, just won't do much."""
        empty = array([[], [], []])

        with pytest.raises(StopIteration):
            x = iterate_3x3_shapes(empty)
            assert next(x) is None

    def test_empty_3d_array(self):
        """raises error as with empty array"""
        empty = array([[[]], [[]], [[]]])

        with pytest.raises(AttributeError) as e:
            x = iterate_3x3_shapes(empty)
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
        subsets = [x for x in iterate_3x3_shapes(input_board)]

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
            [1, 2, 3, 4],
            [1, 2, 3, 4]
        ])

        # This implies 8 iterations
        subsets = [x for x in iterate_3x3_shapes(input_board)]

        assert len(subsets) == 8

        # The first corner 0, 0
        assert array_equal(subsets[0], [[1, 2], [1, 2]])

        # The third element
        assert array_equal(subsets[2], [[2, 3, 4], [2, 3, 4]])

        # The last corner 3, 3
        assert array_equal(subsets[7], [[3, 4], [3, 4]])
