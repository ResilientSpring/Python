import numpy as np
import pandas as pd

dataFrame = pd.DataFrame(data=np.random.randn(4, 3),
                         index=["Taipei", "Taichung", "Tainan", "Kaohsiung"],
                         columns=["GDP per capita", "Air quality index", "Housing price"]);
print(dataFrame);

# The row and column labels can be accessed respectively
# by accessing the index and columns "attributes": [1]
print(dataFrame.index, dataFrame.columns);

# Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#from-dict-of-series-or-dicts