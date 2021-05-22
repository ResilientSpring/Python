import pandas as pd

data_raw = pd.read_csv('20051201_20051210.csv', index_col='Date')
print(data_raw)
print(data_raw.info())