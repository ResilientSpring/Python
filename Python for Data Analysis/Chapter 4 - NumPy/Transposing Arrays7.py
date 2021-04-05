import numpy as np

arr = np.arange(16).reshape((2, 2, 4));
print(arr);

arr = arr.transpose((1, 0, 2));
print(arr);