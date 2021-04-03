import numpy as np
from matplotlib import pyplot as plt 

ys = 200 + np.random.randn(100) # Array
print(ys)

x = [x for x in range(len(ys))] # List

print(x)
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 190, where=(ys > 190), facecolor='r', alpha=0.6)

plt.title('GRAPHIC')
plt.show