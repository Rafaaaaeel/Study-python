import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
Expl = [0.2,0,0,0]
plt.pie(y, labels = mylabels, explode=Expl, shadow=True)
plt.suptitle("Pie")
plt.legend()
plt.show()