import pandas as pd
import matplotlib.pyplot as plt

data = "https://www.w3schools.com/python/pandas/data.csv.txt"
df = pd.read_csv(data)

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

