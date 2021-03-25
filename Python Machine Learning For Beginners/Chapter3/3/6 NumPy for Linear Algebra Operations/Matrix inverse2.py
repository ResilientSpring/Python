# Script 27

import numpy as np

row1 = [6, 1, 1];
row2 = [4, -2, 5];
row3 = [2, 8, 7];

nums_2d = np.array([row1, row2, row3]);

print(nums_2d);

inverse = np.linalg.inv(nums_2d);

print(inverse);