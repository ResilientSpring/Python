import numpy as np
import pandas as pd

s = pd.Series(data=np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'],
              name="List of random number");

print(s);

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series