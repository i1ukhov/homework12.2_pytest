import pytest
from utils import arrs


@pytest.fixture
def coll():
    array = [1, 2, 3, 4]
    return array


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(coll, 3, "test") == 4


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], None, 2) == [1, 2]
    assert arrs.my_slice([]) == []