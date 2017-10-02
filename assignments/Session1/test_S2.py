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
    # test max value with positive values
    my_list = []
    with pytest.raises(ValueError):
        res = s1.max_value(my_list)
