import pandas as pd

data = "https://www.w3schools.com/python/pandas/data.csv.txt"

df = pd.read_csv(data)

print(df.head(10))

print("-----------")

print(df.tail(10))

print("-----------")

print(df.info())