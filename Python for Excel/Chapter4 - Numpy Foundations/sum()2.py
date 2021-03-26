import numpy as np

row1 = [1, 2, 3];
row2 = [4, 5, 6];
array2 = np.array([row1, row2]);

sum_row = array2.sum(axis=1);
print(sum_row);