# O(n^2)
# stable sorting algorithm
# in-place sorting algorithm
def bsort(data=list) -> list:
    '''
    Bubble Sort
    returns sorted list
    '''
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-index-1):
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap = True

        if swap == False:
            break
    return data
