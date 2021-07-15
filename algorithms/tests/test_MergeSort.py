from MergeSort import sort


def test_BubbleSort():
    l = [6, 3, 12, 27, 1, 5]
    assert sort(l) == [1, 3, 5, 6, 12, 27]
