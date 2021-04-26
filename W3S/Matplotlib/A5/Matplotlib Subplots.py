import matplotlib.pyplot as plt
import numpy as np


# Plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(3,1,1) # Row, column, position
plt.plot(x,y)
plt.title("First")

# Plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(3,1,2)
plt.plot(x,y)
plt.title("Second")


x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(3,1,3)
plt.plot(y, c = 'r')
plt.title("Third")

plt.suptitle("Study")
plt.show()