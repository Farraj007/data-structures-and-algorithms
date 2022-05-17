from challenge26.insertion_sort import insertion_sort
import pytest

def test_insertion_sort1():
    arr = [8,4,23,42,16,15]
    assert [4, 8, 15, 16, 23, 42] == insertion_sort(arr)
def test_insertion_sort2():

    arr = [5,12,7,5,5,7]
    assert [5, 5, 5, 7, 7, 12] == insertion_sort(arr)
def test_insertion_sort3():

    arr = [20,18,12,8,5,-2]
    assert [-2, 5, 8, 12, 18, 20] == insertion_sort(arr)
def test_insertion_sort_exception1():
    arr = []
    with pytest.raises(Exception):
        insertion_sort(arr)
def test_insertion_sort_exception2():
    arr = [5,'HI',7,5,]
    with pytest.raises(Exception):
        insertion_sort(arr)        