import numpy as np
# All 0s matrix

a = np.zeros((2,3))

print(a)


# All 1s matrix

b = np.ones((4,2,2), dtype='int32')

print(b)

# Any other number

c = np.full((2,2), 99)

print(c)

# Any other number (full_like)
arr = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

d = np.full_like(arr, 4)

print(d)

# Random decimal numbers

e = np.random.rand(4,2)

f = np.random.random_sample(arr.shape)

print(e)
print("------")
print(f)

# Random Integer values

g = np.random.randint(9, size=(2,3))

print(g)

# The identity matrix

h = np.identity(5)

print(h)

# Repeat an aray

arry = np.array([[1,2,3]])
r1 = np.repeat(arry,3, axis=0)

print(r1)



