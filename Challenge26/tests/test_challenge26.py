from Challenge26.insertion_sort import insertion_sort

def test_insertion_sort():
    array = [8,4,23,42,16,15]
    assert [4, 8, 15, 16, 23, 42] == insertion_sort(array)

    array2 = [5,12,7,5,5,7]
    assert [5, 5, 5, 7, 7, 12] == insertion_sort(array2)

    array3 = [20,18,12,8,5,-2]
    assert [-2, 5, 8, 12, 18, 20] == insertion_sort(array3)