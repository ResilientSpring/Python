import numpy as np
import pandas as pd

obj = pd.Series(data=['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c']);
print(obj);

mask = obj.isin(['b', 'c']);
print(mask);

print(obj[mask]);