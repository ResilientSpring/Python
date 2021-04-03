import numpy as np

np.random.seed(1234);
arr = np.random.randn(100);

print((arr > 0).sum());  # The number of positive values.