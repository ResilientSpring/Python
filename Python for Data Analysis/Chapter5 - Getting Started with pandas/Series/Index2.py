import numpy as np
import pandas as pd

obj = pd.Series(data=np.arange(4.), index=['a', 'b', 'c', 'd']);
print(obj);

print(obj['b' : 'c']);

obj['b' : 'c'] = 5;
print(obj);