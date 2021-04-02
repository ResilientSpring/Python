# You may access an index on a Series or column on a DataFrame
# directly as an attribute.

import numpy as np
import pandas as pd

sa = pd.Series(data=[1, 2, 3], index=list("abc"));