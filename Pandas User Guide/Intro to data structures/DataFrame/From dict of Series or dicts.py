import numpy as np
import pandas as pd

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']),
    "two": pd.Series(data=[1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd']),
};

df = pd.DataFrame(d);

print(df);