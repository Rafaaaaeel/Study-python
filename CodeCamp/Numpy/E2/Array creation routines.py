import numpy as np

# Create a nre array of 2*2 integers, without initializing entries.

x = np.zeros((2,2))
print(x)

x = np.empty([2,2])
print(x)

# Create a 3-D array with ones on the diagonal and zeros elsewhere.

x = np.eye(3)
print(x)

x = np.identity(3)
print(x)

# Create a new array of 3*2 float numbers, filled with ones.

x = np.ones([3,2], float)
print(x)

# let x = np.arange(4, dtype=np.int64). Create an array of ones with the same shape an type as X

x = np.arange(4, dtype=np.int64)
z = np.ones_like(x)
print(z)

# Create a new array of 2*5 uints, filled with 6

x = np.full((2,5), 6, dtype=np.uint)
print(x)

# 