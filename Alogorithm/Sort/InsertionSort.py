# O(n^2)
# the best : O(n)
# stable sorting algorithm
# in-place sorting algorithm
import random


def insertion_sort(data=list) -> list:
    '''
    Insertion Sort
    returns sorted list
    '''
    for index in range(len(data)-1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break

    return data


data_list = random.sample(range(100), 10)
print(data_list)
print(insertion_sort(data_list))
