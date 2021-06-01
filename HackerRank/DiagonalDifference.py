import numpy as np

arr = np.array([[11,2,4],[4,5,6],[10,8,-12]])
print(arr)
def diagonalDifference(arr):
    l = [arr[0,0],arr[1,1],arr[2,2]]
    r = [arr[0,-1],arr[1,-2],arr[2,-3]]
    test_1 = 0
    test_2 = 0
    ans = 0
    for i in l:
        test_1 += i
    for i in r:
        test_2 += i
    return test_2 - test_1

print(diagonalDifference(arr))

