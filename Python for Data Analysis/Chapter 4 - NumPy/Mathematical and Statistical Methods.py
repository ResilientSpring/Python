import numpy as np

np.random.seed(12345);
arr = np.random.randn(5, 4);
print(arr);
print(arr.mean());
print(np.mean(arr));
print(arr.mean(axis=0));
print(arr.mean(axis=1));

print(arr.sum());
print(arr.sum(axis=0));
print(arr.sum(axis=1));