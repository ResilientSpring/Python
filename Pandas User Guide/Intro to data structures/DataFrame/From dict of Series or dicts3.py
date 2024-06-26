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

# When a particular set of columns is passed along with a dict of data,
# the passed columns override the keys in the dict.
dataFrame2 = pd.DataFrame(data=dictionary, index=['a', 'b', 'c', 'd'],
                          columns=["Amazing", "out of hand"]);
print(dataFrame2);

dataFrame3 = pd.DataFrame(data=dictionary, index=['a', 'b', 'c', 'd'],
                          columns=["ambivalence", "repatriation"], dtype=float);
print(dataFrame3);

dataFrame4 = pd.DataFrame(data=dictionary, index=['a', 'b', 'c', 'd'],
                          columns=["lifeblood", "livelihood"], dtype="float");
print(dataFrame4);