import numpy as np

arr = np.array([1,2,3,4,5])

print(type(arr))

# 0-D Arrays

arr = np.array(42)


print(arr)


arr = np.array([1,2,3,4,5], ndmin = 5)


print(arr)

arr = np.array([[0,0,0,0],[0,0,0,0]])

arr[1][3] = 15

print(arr[1][3])