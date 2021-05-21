import pandas as pd
import feature_generation

data_raw = pd.read_csv('19920103_20191231.csv', index_col='Date')

print(data_raw)

data = feature_generation.generate_features(df=data_raw)

# Take a look at what the data with the new features looks like:
print(data.round(decimals=3).head(5))
