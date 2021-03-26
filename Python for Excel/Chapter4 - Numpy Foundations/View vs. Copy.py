import numpy as np

row1 = [1, 2, 3];
row2 = [4, 5, 6];

array = np.array([row1, row2]);
print(array);

subset = array[ : , : 2];
print(subset);

subset[0, 0] = 1000;
print(subset);

print(array);

