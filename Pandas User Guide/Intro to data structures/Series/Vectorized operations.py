import numpy as np
import pandas as pd

np.random.seed(12345);

s = pd.Series(data=np.random.randn(5), index=["a", "b", "c", "d", "e"]);
print(s);

print(s + s, s * 2, np.exp(s));