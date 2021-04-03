import numpy as np
import pandas as pd

date = pd.date_range(start="2013-01-01", periods=7);
print(date);

dataFrame = pd.DataFrame(data=np.random.randn(7, 4), index=date, columns=['A', 'B', 'C', 'D']);
print(dataFrame);

print(dataFrame.head());
print(dataFrame.tail(3));
print(dataFrame.index);
print(dataFrame.columns);