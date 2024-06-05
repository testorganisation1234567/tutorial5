import pytest
import numpy as np
from search import my_search

# how can we get a sequence of data and know where each element is?
test_data = np.arange(100)


def test_search_():
    assert my_search(test_data, 8) == 8


@pytest.mark.parametrize("item, expected", [(i, i) for i in range(len(test_data))])
def test_search(item, expected):
    assert my_search(test_data, item) == expected


def test_search_not_found():
    assert my_search(test_data, len(test_data) + 1) == -1


def test_search_empty():
    assert my_search([], 10) == -1
