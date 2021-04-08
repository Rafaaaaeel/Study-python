import numpy as np

a = np.ones((2,3))

print(a)

b = np.full((3,2), 2)
print(b)

c = np.matmul(a,b)
print(c)