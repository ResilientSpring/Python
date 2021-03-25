# Script 28

import numpy as np

row1 = [1, 2, 3];
row2 = [4, 5, 6];
row3 = [7, 8, 9];

nums_2d = np.array([row1, row2, row3]);

determinant = np.linalg.det(nums_2d);

print(int(determinant));

determinant = np.linalg.det(nums_2d);

print(int(determinant));