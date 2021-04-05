import numpy as np
import pandas as pd

obj = pd.Series(data=[4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c']);
print(obj);

obj2 = obj.reindex(index=['a', 'b', 'c', 'd', 'e']);
print(obj2);