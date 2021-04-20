import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

X = pd.DataFrame(data=[[1, 2], [3, 4], [1, 2], [3, 4]],
                 index=[1, 2, 3, 4],
                 columns=["data1", "data2"])

X.index.name = "label"
print(X)

X_array = X.to_numpy()
print(X_array)

y = [1, 2, 3, 4]

# initialize KFold object
kf = KFold(n_splits=2)
kf.get_n_splits(X=X_array)

print(kf)

# Method of KFold() object

## split(X, y=None, groups=None)
### Generate indices to split data into training and test set.

#### Not a useful method since the user still needs to manually
#### split the data according to the returned index and then feed them to the algorithm by hand.

# Source: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html