import numpy as np
import pandas as pd

dictionary = {'x': [1, 2, 3], 'y': [3, 4, 5]};

x = pd.DataFrame(data=dictionary);
print(x);

x.iloc[1] = {'x': 9, 'y': 99};

print(x);