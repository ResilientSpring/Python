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

feature_map = feature_detector.dot(input_image)

print(feature_map)

feature_map = np.dot(input_image, feature_detector)

print(feature_map)

feature_map = np.multiply(input_image, feature_detector)

print(feature_map)
