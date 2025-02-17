
# importing Numpy package
import numpy as np

# creating a 2X2 Numpy matrix
n_array = np.array([[50, 29], [30, 44]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given 2X2 matrix:")
print(det)

# Reference:
# https://www.geeksforgeeks.org/how-to-calculate-the-determinant-of-a-matrix-using-numpy/