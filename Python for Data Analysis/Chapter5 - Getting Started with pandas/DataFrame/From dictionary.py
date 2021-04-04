import numpy as np
import pandas as pd

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};

# If axis labels are not passed, they will be constructed from the input data based on
# common sense rules. [1][3]
frame = pd.DataFrame(data);
print(frame);

frame2 = pd.DataFrame(data=data);
print(frame2);

# If you specify a sequence of columns, the DataFrame's columns will be arranged
# in that order: [2]
frame3 = pd.DataFrame(data=data, columns=["year", "state", "pop"]);
print(frame3);

# Reference:
# 1. https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe
# 2. The input[47] of Textbook, page on 175.
# 3. Pandas User Guide/Intro to data structures/DataFrame/From dict of Series or dicts2.py