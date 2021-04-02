# A Series is a fixed-size dict in that you can get and set values by index label.

import numpy as np
import pandas as pd

np.random.seed(12345);

s = pd.Series(data=np.random.randn(5), index=["a", "b", "c", "d", "e"]);
print(s);

print(s["a"]);

s["a"] = 12;
print(s["a"]);

print("e" in s);
print("f" in s);