import numpy as np

# Supposing you have a matrix of randomly generated data and you want to replace all
# positive values with 2 and all negative values with -2.

arr = np.random.default_rng(5);

matrix = arr.integers(low=-10, high=10, size=(4, 4), dtype=int, endpoint=True);
print(matrix);
print(matrix > 0);

amended_matrix = np.where(matrix > 0, 2, -2);
print(amended_matrix);
print(matrix);