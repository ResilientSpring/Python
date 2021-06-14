import pandas as pd

df = pd.DataFrame({'age':    [ 3,  29],
                   'height': [94, 170],
                   'weight': [31, 115]})

print(df)

# Only the values in the DataFrame will be returned, the axes labels will be removed. [1]
print(df.values)

print(df.to_numpy())

# References:
# 1. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.values.html
