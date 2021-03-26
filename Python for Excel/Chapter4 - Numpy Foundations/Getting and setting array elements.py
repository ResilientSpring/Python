import numpy as np

array1 = np.array([10, 100, 1000]);

row1 = [1, 2, 3];
row2 = [4, 5, 6];
array2 = np.array([row1, row2]);

print(array1[2]); # Returns a scalar.
print(array2[0][0]); # Returns a scalar
print(array2[0, 0]); # Returns a scalar

print(array2[1][2]);
print(array2[1, 2]);

print(array2[ : ][1 : ]);
print(array2[ : , 1 : ]); # Returns a 2d array

print(array2[ : , 1]); # Returns a 1d array.

print(array2[1, : 2]); # Returns a 1d array.
