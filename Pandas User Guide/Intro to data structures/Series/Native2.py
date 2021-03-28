import numpy as np
import pandas as pd

# data can be many different things:

# a Python dictionary
s = pd.Series(
    data={1: "undertake", 2: "lifeblood", 3: "livelihood", 4: "repatriation"},
    index=['A', 'B', 'C'],
    name="Using Python dictionary as the Series' data"
);

print(s);

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series