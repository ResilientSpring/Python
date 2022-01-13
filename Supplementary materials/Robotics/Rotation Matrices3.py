import numpy as np

theta1 = 0  # Theta 1 angle in degree
theta2 = 90  # Theta 2 angle in degree

# Convert these two angles from degrees to radians
theta1 = (theta1 / 180.0) * np.pi
theta2 = (theta2 / 180.0) * np.pi

rotation_matrix_0_1 = [[np.cos(theta1), - np.sin(theta1), 0],
                       [np.sin(theta1), np.cos(theta1), 0],
                       [0, 0, 1]]

rotation_matrix_1_2 = [[np.cos(theta2), - np.sin(theta2), 0],
                       [np.sin(theta2), np.cos(theta2), 0],
                       [0, 0, 1]]

rotation_matrix_0_2 = np.dot(rotation_matrix_0_1, rotation_matrix_1_2)

print(rotation_matrix_0_2)
