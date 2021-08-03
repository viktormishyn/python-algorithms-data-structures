from MergeSort import sort, merge


def test_MergeSort():
    l = [6, 3, 12, 27, 1, 5]
    assert sort(l) == [1, 3, 5, 6, 12, 27]


def test_merge():
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    assert merge(l1, l2) == [1, 2, 3, 4, 5, 6]
