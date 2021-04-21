import pandas as pd

data = "C:\\Users\\rafae\\Documents\\Python\\W3S\\Pandas\\A3\\data.csv"

df = pd.read_csv(data)

print(df) # Only first 5 rows and last 5 rows

print(df.to_string()) # All Rows