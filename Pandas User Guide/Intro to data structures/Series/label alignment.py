import numpy as np
import pandas as pd

np.random.seed(12345);

s = pd.Series(data=np.random.randn(5), index=["a", "b", "c", "d", "e"]);
print(s);

matrix = s[1:] + s[ : -1];
print(matrix);

# The result of an operation between unaligned Series will have the union of the indexes involved.
# If a label is not found in one Series or the other, the result will be marked as missing NaN.

# Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#vectorized-operations-and-label-alignment-with-series