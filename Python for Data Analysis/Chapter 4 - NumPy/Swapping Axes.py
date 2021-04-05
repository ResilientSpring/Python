import numpy as np

array = np.arange(16);
print(array);

array = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[8, 9, 10, 11], [12, 13, 14, 15]]]);
print(array);

array = np.array([
    [
        [0, 1, 2, 3],
        [4, 5, 6, 7]
    ],
    [
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]
]);

# print(array.swapaxes(axis1=1, axis2=2));
print(array.swapaxes(1, 2));