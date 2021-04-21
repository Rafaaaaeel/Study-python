import pandas as pd

data = 'https://www.w3schools.com/python/pandas/dirtydata.csv.txt'

df = pd.read_csv(data)

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

print(df.to_string())