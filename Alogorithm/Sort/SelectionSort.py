# O(n^2)
# unstable sorting algorithm
# in-place sorting algorithm
import random


def selection_sort(data=list) -> list:
    '''
    Selection Sort
    returns sorted list
    '''
    for standard in range(len(data)-1):
        lowest = standard
        for index in range(standard + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[standard] = data[standard], data[lowest]
    return data


data_list = random.sample(range(100), 10)
print(data_list)
print(selection_sort(data_list))
