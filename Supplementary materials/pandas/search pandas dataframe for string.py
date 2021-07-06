import pandas as pd
import numpy as np

df = pd.read_csv('Realm.csv', header=0)
print(df)

df2 = df['City'].astype('str').str.contains("York")
print(df2)

df3 = pd.read_csv('Realm.csv')
print(df3)

df4 = df3['City'].astype('str').str.contains('York')
print(df4)

df5 = df[df4] # [2]
print(df5)

# =====================================
# setup
df1 = pd.DataFrame({'col': ['foo', 'foobar', 'bar', 'baz']})
print(df1)

# find rows in `df1` which contain "foo" followed by something.[3]
print(df1[df1['col'].str.contains(r'foo(?!$)')])

#select all rows containing "foo".[3]
print(df1[df1['col'].str.contains('foo', regex=False)])
# same as df1[df1['col'].str.contains('foo')] but faster.[3]
print(df1[df1['col'].str.contains('foo')])

# Addressing ValueError
s = pd.Series(['foo', 'foobar', np.nan, 'bar', 'baz', 123])
print(s.str.contains('foo|bar'))

## Anything that is not a string cannot have string methods applied on it,
# so the result is NaN (naturally).
# In this case, specify na=False to ignore non-string data.[3]
new = s[s.str.contains('foo|bar', na=False)]
print(new)

# Matching Entire Word(s)
df3 = pd.DataFrame({'col': ['the sky is blue', 'bluejay by the window']})
print(df3)

f4 = df3[df3['col'].str.contains('blue')]
print(f4)

# To only match full words, we will need to make use of regular expressions here—in particular,
# our pattern will need to specify word boundaries (\b).[3]
f5 = df3[df3['col'].str.contains(r'\bblue\b')]
print(f5)

# Reference:
# 1. https://stackoverflow.com/questions/11350770/select-by-partial-string-from-a-pandas-dataframe
# 2. https://stackoverflow.com/a/67749217
# 3. https://stackoverflow.com/a/55335207