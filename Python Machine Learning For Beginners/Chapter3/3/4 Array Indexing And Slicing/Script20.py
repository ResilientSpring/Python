import numpy as np

row1 = [10, 12, 13];
row2 = [45, 32, 16];
row3 = [45, 32, 16];

nums_2d = np.array([row1, row2, row3]);
print(nums_2d[1 : , 1: ]);