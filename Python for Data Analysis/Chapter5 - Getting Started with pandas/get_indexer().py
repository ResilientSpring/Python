import numpy as np
import pandas as pd

to_match = pd.Series(data=['c', 'a', 'b', 'b', 'c', 'a']);

unique_vals = pd.Series(data=['c', 'b', 'a']);

print(pd.Index(unique_vals).get_indexer(to_match));