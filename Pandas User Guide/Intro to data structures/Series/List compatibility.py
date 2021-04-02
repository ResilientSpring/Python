import numpy as np
import pandas as pd

s = pd.Series(data=[2, 4, 6, 8, 10], index=['a', 'b', 'c', 'd', 'e'], dtype=int, name=
              "Check if pandas.Series is compatible with Python's built-in list type.");
print(s);