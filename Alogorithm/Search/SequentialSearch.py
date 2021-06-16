# O(n)

def sequential(data: list, search: int):
    for index in range(len(data)):
        if data[index] == search:
            return index
    return -1
