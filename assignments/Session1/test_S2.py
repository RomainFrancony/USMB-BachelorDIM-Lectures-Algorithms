""" Unit test file
@brief unit test
"""

import S1_algotools as s1
import pytest


def test_average_above_zero_positive_values():
    ##
    # test average above zero with positive values
    my_list = [1, 2, 3, 4, 5]
    assert s1.average_above_zero(my_list) == 3


def test_average_above_zero_mixed_values():
    ##
    # test average above zero with mixed values
    my_list = [1, 2, 3, 4, -7]
    assert s1.average_above_zero(my_list) == 2.5


def test_average_above_zero_negative_values():
    ##
    # test average above zero with only negative values
    my_list = [-2, -2, -3, -4, -7]
    assert s1.average_above_zero(my_list) == 0


def test_average_above_zero_empty_list():
    ##
    # test average above zero with empty list
    my_list = []
    assert s1.average_above_zero(my_list) == 0


# --------------------------------------------------

def test_max_value_positive_values():
    ##
    # test average above zero with positive values
    my_list = [1, 18, 8, 7, 48, 45]
    assert s1.max_value(my_list) == (48, 4)


def test_max_value_mixed_values():
    ##
    # test max value with positive values
    my_list = [1, -8, 8, 7, -48, 45]
    assert s1.max_value(my_list) == (45, 5)


def test_max_value_negative_values():
    ##
    # test max value with positive values
    my_list = [-1, -8, -8, -7, -48, -45]
    assert s1.max_value(my_list) == (-1, 0)


def test_max_value_empty_list():
    ##
    # test max value with empty list
    my_list = []
    with pytest.raises(ValueError):
        res = s1.max_value(my_list)


# --------------------------------------------------


def test_reverse_table_normal_values():
    ##
    # test reverse table with normal values
    my_list = [1, 8, 8, -7, -48, -45]
    assert s1.reverse_table(my_list) == [-45, -48, -7, 8, 8, 1]


def test_reverse_table_empty_list():
    ##
    # test max value with empty list
    my_list = []
    with pytest.raises(ValueError):
        res = s1.reverse_table(my_list)


# --------------------------------------------------
"""
import numpy


def test_roi_bbox_normal_values():
    ##
    # test reverse table with normal values
    my_matrix = numpy.zeros([10, 10], bool)
    my_matrix[3:4, 6:9] = numpy.ones([1, 3])
    my_matrix[2:4, 6:8] = numpy.ones([2, 2])
    assert s1.roi_bbox(my_matrix).all() == numpy.array([[2, 6], [2, 8], [3, 6], [3, 8]]).all()
"""