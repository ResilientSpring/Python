import numpy as np

arr = np.random.randn(6, 3);
print(arr);

arr2 = np.dot(arr.T, arr);
print(arr2);