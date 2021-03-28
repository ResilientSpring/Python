import pandas as pd
import numpy as np

s1 = pd.Series(data=[1.0, 2.0, 3.0], index=['a', 'b', 'c']);
print(s1);

s2 = pd.Series(data=[1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd']);
print(s2);

dictionary = {"one": s1, "two": s2};

# DataFrame is a 2-dimensional labeled data structure with columns of potentially different
# types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
dataFrame = pd.DataFrame(data=dictionary, );
print(dataFrame);