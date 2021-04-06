import numpy as np
import pandas as pd

obj = pd.Series(data=np.arange(4.), index=['a', 'b', 'c', 'd']);
print(obj);

print(obj['b']);
print(obj[['b', 'a', 'd']]);
print(obj['b' : 'c']);

print(obj[1]);
print(obj[2:]);
print(obj[[1, 3]]);

print(obj[obj < 2]);