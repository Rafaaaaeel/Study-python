import pandas as pd

data = "https://www.w3schools.com/python/pandas/data.js"
df = pd.read_json(data)

print(df.to_string())