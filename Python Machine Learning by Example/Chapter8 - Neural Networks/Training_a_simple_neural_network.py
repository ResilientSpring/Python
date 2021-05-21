import csv

import pandas as pd
import numpy as np

data_raw = pd.read_csv(filepath_or_buffer='19920103_20191231.csv', index_col='Date',
                       skipinitialspace=True, sep=',', engine='python',
                       dtype={'Open': float, 'High': float, 'Low': float, 'Close': float,
                              'Adjusted Close': float, 'Volume': float}, quoting=csv.QUOTE_NONE)

print(data_raw)

print(data_raw.info())
