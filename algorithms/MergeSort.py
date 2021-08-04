# The time complexity of merge sort is linearithmic O(n log n)


def sort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarray = dataset[mid:]

        # recursively break down the arrays
        sort(leftarr)
        sort(rightarray)

        # perform the merging
        i = 0     # index into the left array
        j = 0     # index into the right array
        k = 0     # index into merged array
        # while both arrays have content
        while i < len(leftarr) and j < len(rightarray):
            if leftarr[i] < rightarray[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarray[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        # if the right array still has values, add them
            # if the left array still has values, add them
        while j < len(rightarray):
            dataset[k] = rightarray[j]
            j += 1
            k += 1

    return dataset


# def merge(l1, l2):
#     """Merge two arrays"""
#     result = []
#     i = j = 0
#     while i < len(l1) and j < len(l2):
#         if l1[i] < l2[j]:
#             result.append(l1[i])
#             i += 1
#         else:
#             result.append(l2[j])
#             j += 1
#     while i < len(l1):
#         result.append(l1[i])
#         i += 1
#     while j < len(l2):
#         result.append(l2[j])
#         j += 1
#     return result


if __name__ == '__main__':
    import timeit
    num = 100000
    print(timeit.timeit('sort([6, 3, 12, 27, 1, 5])',
          'from __main__ import sort', number=num))

    # print(timeit.timeit('merge([1, 3, 5], [2, 4, 6])',
    #       'from __main__ import merge', number=num))
