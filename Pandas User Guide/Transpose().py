import pandas as pd

d1 = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(data=d1)
print(df1)

df1_transposed = df1.transpose() # or df1.T
print(df1_transposed)

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html
