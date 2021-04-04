import numpy as np
import pandas as pd

obj = pd.Series(data=[4, 7, -5, 3]);
print(obj);

# Override the default index.
obj.index = ["Bob", "Steve", "Jeff", "Ryan"];

print(obj);