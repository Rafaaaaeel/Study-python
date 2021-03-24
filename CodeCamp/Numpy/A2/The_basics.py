import numpy as np

a = np.array([1,2,3,4], dtype='int64')

print(a)

b = np.array([[9,0,8,0,7,0],[6,0,5,0,4,0]])

print(b)

# Get dimentsion

print(a.ndim)
print(b.ndim)

# Get Shape

print(a.shape)
print(b.shape)

# Get type

print(a.dtype)

# Get Size

print('item Size: ',a.itemsize)


# Get total size

print(f"nbytes: {a.nbytes}")