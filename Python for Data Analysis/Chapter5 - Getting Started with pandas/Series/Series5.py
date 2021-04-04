import numpy as np
import pandas as pd

sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000};
print(sdata);

obj3 = pd.Series(sdata);
print(obj3);

# Override the pre-defined index(keys) in dict.
obj4 = pd.Series(data=sdata, index=["California", "Ohio", "Oregon", "Texas"]);
print(obj4);

# Detect missing data.
print(pd.isnull(obj4));
print(pd.notnull(obj4));

# Detect missing data.
print(obj4.isnull());
print(obj4.notnull());