import numpy as np

array2 = np.array([[1, 2, 3], [4, 5, 6]]);
dot = array2 @ array2.T;  # array2.T is a shortcut for array2.transpose()
print(dot);