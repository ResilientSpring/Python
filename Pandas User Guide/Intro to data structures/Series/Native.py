import numpy as np
import pandas as pd

# Series is a one-dimensional labeled array capable of holding any data type (integers,
# strings, floating point numbers, Python objects, etc.).
# The axis labels are collectively referred to as the index.

# The basic method to create a Series is to call:
s = pd.Series(data=["civilization", "ignorance", "zap"], index=[1, 2, 3], name="Word list");

print(s);

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series