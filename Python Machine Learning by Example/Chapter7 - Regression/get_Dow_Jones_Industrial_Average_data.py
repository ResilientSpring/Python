import pandas as pd
import numpy as np
import feature_generation
import csv

with open('19920103_20191231.csv') as csv_file:
    content = csv_file.read()

with open('19920103_20191231.csv') as csv_file:
    csv_file.write(content.replace('"', ''))

# creating functions to clean the columns
## remove the ‘,’ from the column and remove the ‘ " ’ from the column as well.
a = lambda x: (x.replace(',', ''))
b = lambda x: (x.replace('"', ''))
c = lambda x: (x.replace([',', '"'], '')) # Not allowed to convert more than one string.

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date', header=0,
                       infer_datetime_format=True,
                       converters={'Open': b, 'High': b, 'Low': b, 'Close': b,
                                   'Adjusted Close': b,
                                   'Volume': b},
                       dtype={'Open': np.float64, 'High': np.float64, 'Low': np.float64,
                              'Close': np.float64, 'Adjusted Close': np.float64,
                              'Volume': np.float64})

print(data_raw)

data = feature_generation.generate_features(df=data_raw)

# Take a look at what the data with the new features looks like:
print(data.round(decimals=3).head(5))
