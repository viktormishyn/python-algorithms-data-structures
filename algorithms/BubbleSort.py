# The time complexity of bubble sort is quadratic O(n^2)

def sort(dataset):
    for i in range(len(dataset)-1, 0, -1):
        # start at the last index, end at the first index, decrease one step at a time
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                # temp = dataset[j]
                # dataset[j] = dataset[j+1]
                # dataset[j+1] = temp
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
    return dataset


def sort_bad(dataset):
    for _ in range(len(dataset)):
        for i in range(len(dataset)):
            try:
                prev, next = dataset[i], dataset[i+1]
                if prev > next:
                    dataset[i], dataset[i+1] = next, prev
            except IndexError:
                break
    return dataset


def less_bad(dataset):
    for item in dataset:
        for i in range(len(dataset)-1):
            if dataset[i] > dataset[i+1]:
                dataset[i], dataset[i+1] = dataset[i+1], dataset[i]
    return dataset


if __name__ == '__main__':
    import timeit
    num = 100000
    print(timeit.timeit('sort([6, 3, 12, 27, 1, 5])',
          'from __main__ import sort', number=num))
    print(timeit.timeit('sort_bad([6, 3, 12, 27, 1, 5])',
                        'from __main__ import sort_bad', number=num))
    print(timeit.timeit('less_bad([6, 3, 12, 27, 1, 5])',
                        'from __main__ import less_bad', number=num))
