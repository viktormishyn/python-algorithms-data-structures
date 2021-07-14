from BubbleSort import sort, sort_bad


def test_BubbleSort():
    l = [6, 3, 12, 27, 1, 5]
    assert sort(l) == [1, 3, 5, 6, 12, 27]
    assert sort_bad(l) == [1, 3, 5, 6, 12, 27]
