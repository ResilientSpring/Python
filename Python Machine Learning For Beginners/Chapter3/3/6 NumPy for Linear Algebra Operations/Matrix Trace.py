# Script 29

import numpy as np

row1 = [1, 2, 3];
row2 = [4, 5, 6];
row3 = [7, 8, 9];

nums_2d = np.array([row1, row2, row3]);

trace = np.trace(nums_2d);

print(trace);