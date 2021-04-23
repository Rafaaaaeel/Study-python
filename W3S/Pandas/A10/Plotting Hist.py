import pandas as pd
import matplotlib.pyplot as plt

data = "https://www.w3schools.com/python/pandas/data.csv.txt"
df = pd.read_csv(data)

df['Duration'].plot(kind = 'hist')
plt.show()

