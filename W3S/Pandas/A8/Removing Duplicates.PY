import pandas as pd

data = "https://www.w3schools.com/python/pandas/dirtydata.csv.txt"

df = pd.read_csv(data)

print(df.duplicated())

df.drop_duplicates(inplace = True)

print(df.duplicated())