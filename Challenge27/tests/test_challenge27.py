from challenge27.merge_sort import Mergesort

def test_zeros_negative_list():
    lst = [-55, 0, -45, 0, 90, -2]
    Mergesort(lst)
    assert lst == [-55, -45, -2, 0, 0, 90]

def test_few_uniques_list():
    lst = [50, 60, 50, 60, 90, 100]
    Mergesort(lst)
    assert lst == [50, 50, 60, 60, 90, 100]

def test_nearly_sorted_list():
    lst = [50, 60, 70, 80, 100, 90]
    Mergesort(lst)
    assert lst == [50, 60, 70, 80, 90, 100]

def test_sorted_list():
    lst = [50, 60, 70, 80, 90, 100]
    Mergesort(lst)
    assert lst == [50, 60, 70, 80, 90, 100]

def test_reverse_list():
    lst = [100, 90, 80, 70, 60, 50]
    Mergesort(lst)
    assert lst == [50, 60, 70, 80, 90, 100]

