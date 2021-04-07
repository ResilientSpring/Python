import numpy as np
import pandas as pd

obj = pd.Series(data=[4, 7, -3, 2], index=None);
print(obj);

obj2 = obj.sort_values(axis=0, ascending=True);
print(obj2);

obj3 = obj.sort_values(axis=0, ascending=False);
print(obj3);