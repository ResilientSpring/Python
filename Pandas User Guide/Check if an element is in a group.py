import pandas as pd

df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
                  index=['falcon', 'dog'])
print(df)

# When values is a list, check whether every value in the DataFrame is present in the list
# (which animals have 0 or 2 legs or wings):
print(df.isin(values=[0, 2]))

# When values is a dict, we can pass values to check for each column separately:
print(df.isin({'num_wings': [0, 3]}))

# When values is a Series or DataFrame, the index and column must match.
# Note that ‘falcon’ does not match based on the number of legs in df2.
other = pd.DataFrame({'num_legs': [8, 2], 'num_wings': [0, 2]},
                     index=['spider', 'falcon'])
print(other)

print(df.isin(values=other))

# Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html
