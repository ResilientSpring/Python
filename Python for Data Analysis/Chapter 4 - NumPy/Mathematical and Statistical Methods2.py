import numpy as np
import pandas as pd

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7]);
print(arr.cumsum());  # cumulative sum

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]);
print(arr);
print(arr.cumsum(axis=0));
print(arr.cumsum(axis=1));