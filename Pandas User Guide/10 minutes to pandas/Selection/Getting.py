import numpy as np
import pandas as pd

date = pd.date_range(start="2013-01-01", periods=6);
print(date);

df = pd.DataFrame(data=np.random.randn(6, 4), index=date, columns=['A', 'B', 'C', 'D']);
print(df);

# Selecting a single column, which yields a Series, equivalent to df.A:
print(df['A']);

# Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#getting