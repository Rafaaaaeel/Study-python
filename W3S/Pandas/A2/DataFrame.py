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

dataset = pd.DataFrame(data_2)

print(dataset)