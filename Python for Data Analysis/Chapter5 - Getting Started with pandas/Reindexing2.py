import numpy as np
import pandas as pd

obj = pd.Series(data=["blue", "purple", "yellow"], index=[0, 2, 4]);
print(obj);

obj2 = obj.reindex(index=range(6), method="ffill");
print(obj2);