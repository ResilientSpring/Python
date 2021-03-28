import pandas as pd
import numpy as np

s1 = pd.Series(data=[1.0, 2.0, 3.0], index=['a', 'b', 'c']);
print(s1);

s2 = pd.Series(data=[1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd']);
print(s2);

dictionary = {"one": s1, "two": s2};

# DataFrame is a 2-dimensional labeled data structure with columns of potentially different
# types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
dataFrame = pd.DataFrame(data=dictionary, index=['a', 'b', 'c', 'd'], columns=["one", "two"]);
print(dataFrame);

# If you pass an index and / or columns, you are guaranteeing the index and / or columns of
# the resulting DataFrame. Thus, a dict of Series plus a specific index will discard all
# data not matching up to the passed index.
dataFrame2 = pd.DataFrame(data=dictionary, index=['a', 'b', 'c', 'd'], columns=["One", "Two"], dtype=float);
print(dataFrame2);

# a dict of Series plus a specific index will discard all
# data not matching up to the passed index.
dataFrame3 = pd.DataFrame(data=dictionary, index=['a', 'b', 'c'], columns=["one", "two"]);
print(dataFrame3);

# When the data is a dict, and columns is not specified,
# the DataFrame columns will be ordered by the dict’s insertion order
dataFrame4 = pd.DataFrame(data=dictionary, index=['a', 'b', 'd']);
print(dataFrame4);

dataFrame5 = pd.DataFrame(data=dictionary, index=['d', 'b', 'a']);
print(dataFrame5);

# If axis labels are not passed, they will be constructed from the input data based on common sense rules.
dataFrame6 = pd.DataFrame(data=dictionary, );
print(dataFrame6);