import numpy as np

data = np.random.randn(7, 4);
print(data);

data[data < 0] = 0;