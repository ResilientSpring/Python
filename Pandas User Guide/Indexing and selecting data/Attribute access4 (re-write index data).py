import numpy as np
import pandas as pd

list = list("abc");
print(list);

sa = pd.Series(data=[1, 2, 3], index=list);
print(sa);

sa.a = 5;

print(sa);