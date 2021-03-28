import numpy as np
import pandas as pd
import matplotlib as plt

# If a data is a scalar value, an index must be provided.
s = pd.Series(data=5.0, index=[1]);

s2 = pd.Series(data=5.0, index=['A']);

# The value will be repeated to match the length of index.
s3 = pd.Series(data=5.0, index=['a', 'b', 'c', 'd', 'e']);

print(s, "\n", s2, "\n", s3);