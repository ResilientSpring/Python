import numpy as np
import pandas as pd

d = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5};

s = pd.Series(data=d,
              index=["belated", "be privy to sth", "chastise", "prevaricate", "impasse"],
              dtype=None, name="What if the data is a dic, and an index is passed?");

print(s);