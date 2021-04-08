import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])

print(before)

after = before.reshape((4,2))

print(after)

# Vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
v3 = np.vstack([v1,v2])

print(v3)

# Hozizontal stack

h1 = np.ones((2,4))
h2 = np.zeros((2,2))
h3 = np.hstack((h1,h2))
print(h3)