import pandas as pd

s = pd.Series([1, 2], index=["a", "b"])
print(s)

s_copy = s.copy()
print(s_copy)

# Shallow copy versus default (deep) copy:
deep = s.copy()
shallow = s.copy(deep=False)

## Shallow copy shares data and index with original.
print(s is shallow)
print(s.values is shallow.values and s.index is shallow.index)

## Deep copy has own copy of data and index.
print(s is deep)
print(s.values is deep.values or s.index is deep.index)

# Updates to the data shared by shallow copy and original is reflected in both; deep copy remains unchanged.
s[0] = 3
shallow[1] = 4

print(s)
print(shallow)
print(deep)

# Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html