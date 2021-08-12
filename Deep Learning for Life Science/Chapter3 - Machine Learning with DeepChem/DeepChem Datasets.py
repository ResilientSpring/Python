import deepchem as dc
import numpy as np

x = np.random.random((4, 5))
y = np.random.random((4, 1))

dataset = dc.data.NumpyDataset(x, y)

print(dataset.X)
print(dataset.y)
