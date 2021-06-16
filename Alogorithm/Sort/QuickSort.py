# O(n log n)
# the worst : O(n^2)
# pivot 중심점[축]
def qsort(data=list) -> list:
    '''
    Quick Sort
    returns sorted list
    '''
    if len(data) <= 1:
        return data

    pivot = data[0]
    # left, right = list(), list()

    # for i in range(1, len(data)):
    #     if pivot > data[i]:
    #         left.append(data[i])
    #     else:
    #         right.append(data[i])

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)
