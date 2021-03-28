import pandas as pd
import numpy as np

s1 = pd.Series(data=[1.0, 2.0, 3.0], index=['a', 'b', 'c']);
print(s1);

s2 = pd.Series(data=[1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd']);
print(s2);

dictionary = {"one": s1, "two": s2};

dataFrame = pd.DataFrame(data=dictionary, );
print(dataFrame);