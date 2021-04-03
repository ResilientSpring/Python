import numpy as np
import pandas as pd

index = pd.date_range(start="1/1/2000", periods=8);
s = pd.Series(data=np.random.randn(5), index=['a', 'b', 'c', 'd', 'e']);
dataFrame = pd.DataFrame(data=np.random.randn(8, 3), index=index, columns=['A', 'B', 'C']);

long_series = pd.Series(data=np.random.randn(1000));

# To view a small sample of a Series or DataFrame object, use the head() and tail() methods.
# The default number of elements to display is five
print(long_series.head());
print(long_series.tail());

# but you may pass a custom number.
print(long_series.head(3));
print(long_series.tail(3));

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#head-and-tail