import numpy as np
import pandas as pd

s = pd.Series(data=np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'],
              name="List of random number");

print(s, "\n");

print(s.index, "\n");

#  If no index is passed, one will be created having values [0, ..., len(data) - 1].
s2 = pd.Series(data=np.random.randn(10), name="A list of 10 random numbers");
print(s2);

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series