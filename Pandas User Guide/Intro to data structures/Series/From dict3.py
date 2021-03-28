import numpy as np
import pandas as pd
import matplotlib as plt

d = {"a": 0.0, "b": 1.0, "c": 2.0};

# If an index is passed,
# the values in data corresponding to the labels in the index will be pulled out.
s = pd.Series(data=d, index=['b', 'c', 'd', 'a']);
print(s);

# NaN (not a number) is the standard missing data marker used in pandas.