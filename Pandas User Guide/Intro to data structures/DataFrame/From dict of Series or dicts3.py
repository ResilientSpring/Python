import numpy as np
import pandas as pd

s1 = pd.Series(data=[1.0, 2.0, 3.0], index=['a', 'b', 'c'], dtype=float, name="Series 1");
print(s1);

s2 = pd.Series(data=[1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'], dtype=float,
               name="Series 2");
print(s2);

dictionary = {"One": s1, "Two": s2};
print(dictionary);

# If no columns are passed, the columns will be the ordered list of dict keys.
dataFrame = pd.DataFrame(data=dictionary, index=['d', 'b', 'a', 'c']);

print(dataFrame);