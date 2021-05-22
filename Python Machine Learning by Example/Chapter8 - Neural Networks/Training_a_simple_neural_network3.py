import pandas as pd

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date')
print(data_raw)
print(data_raw.info())
