# O(nlogn)
# stable sorting algorithm
# not in-place sorting algorithm
def split(data=list):
    medium = int(len(data)/2)
    left = data[:medium]
    right = data[medium:]
    print(left, right)

def mergesplit(data=list):
    if len(data) <=1:
        return data
    medium = int(len(data)/2)
    left = data[:medium]
    right = data[medium:]
    return merge(left, right)

def merge(left=list, right=list):
    merge = list()
    left_point, right_point = 0,0

    # case1 : left/right 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point]

    # case2 : left만 남아있을 때
    while len(left) > left_point:

    # case3 : right만 남아있을 때
    while len(right) > right_point
