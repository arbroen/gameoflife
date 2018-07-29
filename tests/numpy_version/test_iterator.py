# -*- coding: utf8 -*-
import pytest

from numpy import array

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
