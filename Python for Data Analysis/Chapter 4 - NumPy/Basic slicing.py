import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

# Select the first two rows.
print(arr2d[:2]);

print(arr2d[:2, 1:]);

# Select the second row but only the first two columns.
print(arr2d[1, 0:2]);

# Select the third column but only the first two rows.
print(arr2d[:2, 2]);

# A colon by itself means to take the entire axis,
# so you can slice only higher dimensional axes by doing:
print(arr2d[:, :1]);

# Assigning to a slice expression assigns to the whole selection:
arr2d[:2, 1:] = 0;

print(arr2d);