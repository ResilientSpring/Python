import numpy as np
import pandas as pd

obj = pd.Series(data=range(3), index=['a', 'b', 'c']);

index = obj.index;
print(index);

print(index[1:]);