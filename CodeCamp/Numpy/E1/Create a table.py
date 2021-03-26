import numpy as np

arr = np.array([[1,1,1,1,1],[1,0,0,0,1],[1,0,9,0,1],[1,0,0,0,1],[1,1,1,1,1]])


out = np.ones((5,5))
out_z = np.zeros((3,3))

print(out)
print(out_z)

out_z[1,1] = 9

out[1:4,1:4] = out_z

print(out)