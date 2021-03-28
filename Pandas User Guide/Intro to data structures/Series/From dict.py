import numpy as np
import pandas as pd

# Series can be instantiated from dicts:
d = {"b": 1, "a": 0, "c": 2};

# When the data is a dict, and an index is not passed,
# the Series index will be ordered by the dict’s insertion order,
s = pd.Series(data=d);

print(s);