import numpy as np

input_image = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

feature_detector = np.array([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 1]
])

feature_map = input_image.dot(feature_detector)

print(feature_map)
