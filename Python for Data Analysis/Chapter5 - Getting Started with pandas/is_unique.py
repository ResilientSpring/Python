import numpy as np
import pandas as pd

obj = pd.Series(data=np.arange(5), index=['a', 'a', 'b', 'b', 'c']);
print(obj);

print(obj.index.is_unique);