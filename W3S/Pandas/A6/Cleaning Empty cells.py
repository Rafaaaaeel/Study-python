import pandas as pd

data = "https://www.w3schools.com/python/pandas/dirtydata.csv.txt"

df = pd.read_csv(data)

df.dropna(inplace = True)

df.fillna(130, inplace = True) # Change all NaN values to 130

df['Calories'].fillna(130, inplace = True) # Change the NaN values to 130

x = df['Calories'].mean() # Find the collumn mean

df['Calories'].fillna(x, inplace = True) # Change the NaN values for the collumn mean

x = df['Calories'].median()

df['Calories'].fillna(x, inplace = True)

x = df['Calories'].mode()

df['Calories'].fillna(x, inplace = True)

