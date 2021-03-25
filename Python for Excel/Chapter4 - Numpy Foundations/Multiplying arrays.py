import numpy as np

list = [10, 100, 1000];
row1 = [1, 2, 3];
row2 = [4, 5, 6];

array1 = np.array(list);
array2 = np.array([row1, row2]);

product = array2 * array2;
print(product);