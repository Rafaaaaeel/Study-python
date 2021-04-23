import pandas as pd

data = "https://www.w3schools.com/python/pandas/data.csv.txt"
df = pd.read_csv(data)

print(df.head())
print(df.corr())