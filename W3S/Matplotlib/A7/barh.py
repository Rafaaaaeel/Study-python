import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Banana","Apple","Strawberry","Bluebarry"])
y = np.array([3,8,1,10])

plt.barh(x,y)
plt.suptitle("Barh")
plt.show()
