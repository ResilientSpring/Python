import numpy as np

# Generate/create a random list of positive and negative floating numbers [1]
np.set_printoptions(precision=2);
arr = np.random.uniform(-1, 1, (4, 4));
print(arr);

amended_array = np.where(arr > 0, 2, None);
print(amended_array);

# Reference:
# 1. https://stackoverflow.com/questions/55020826/generate-create-a-random-list-of-positive-and-negative-floating-numbers/55021071