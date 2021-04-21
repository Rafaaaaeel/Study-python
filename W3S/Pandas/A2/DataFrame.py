import pandas as pd

data_1 = {
    "Day 1" : 420,
    "Day 2" : 380,
    "Day 3" : 390
}

data_2 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data_2, index = ['day 1', 'day 2', 'day 3'])

print(df.loc['day 1'])

# Import external file

df_1 = pd.read_csv("trees.csv")

print(df_1)