import numpy as np
import pandas as pd

# Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1, 3, 5, np.nan, 6, 8]);

print(s);

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range("20130101", periods=6);

print("\n", dates);

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"));
print(df);

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#min