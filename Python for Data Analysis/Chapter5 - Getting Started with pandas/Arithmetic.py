import numpy as np
import pandas as pd

s1 = pd.Series(data=[7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e']);
s2 = pd.Series(data=[-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g']);

print(s1);
print(s2);

s3 = s1 + s2;
print(s3);