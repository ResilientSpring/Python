import numpy as np
import pandas as pd

labels = pd.Index(data=np.arange(3));
print(labels);

obj = pd.Series(data=[1.5, -2.5, 0], index=labels);
print(obj);