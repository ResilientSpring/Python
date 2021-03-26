import numpy as np

row1 = [1, 2, 3];
row2 = [4, 5, 6];

array2 = np.array([row1, row2]);

# if you want the sum of each column, do the following:
sum_1d = array2.sum(axis=0); # Returns a 1d array
print(sum_1d);