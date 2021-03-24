import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)
# Get a specific element [row,column]

print(a[1,5])

#Get a specific row

print(a[0, :])

# Get a specific column

print(a[:, 2])

# Getting little more fancy [started:endindex:stepsize]

print(a[0, 1:6:2])

# Or use

print(a[0, 1:-1:2]) # Write on my book the rest of information

a[1,5] = 20

print(a)

# 3-D Example

b = np.array([[[1,2],[3,4],[5,6],[7,8]]], dtype = 'int8')

print(b.ndim)
print(f"item size: {b.itemsize}")

print(b)

# Get specific element (work outside in)

print(b[0,1,1])
print(b[:,1,:])

# Replace

#b[:,1,:] = [[9,9],[8,8]]

print(b)

print(a.shape)