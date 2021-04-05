import pandas as pd
import numpy as np

val = pd.Series(data=[-1.2, -1.5, -1.7], index=["two", "four", "five"]);
print(val);

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};

frame = pd.DataFrame(data=data, columns=["year", "state", "pop", "debt"],
                     index=["one", "two", "three", "four", "five", "six"]);
print(frame);

frame["debt"] = val;

print(frame);