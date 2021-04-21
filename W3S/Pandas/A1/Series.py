import pandas as pd


list_to_series = ['420','380','390']

series = pd.Series(list_to_series, index = ['Day 1','Day 2','Day 3'])

print(series)